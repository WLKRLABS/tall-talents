#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
GITHUB_OWNER=""
GITHUB_REPO="tall-talents"
REF="main"

usage() {
  cat <<'EOF'
Usage: bash scripts/release-dry-run.sh [--github-owner <owner>] [--github-repo tall-talents] [--ref main]
EOF
}

parse_owner_from_remote() {
  local remote_url="$1"

  if [[ "${remote_url}" =~ ^git@[^:]+:([^/]+)/([^/]+)(\.git)?$ ]]; then
    printf '%s\n' "${BASH_REMATCH[1]}"
    return 0
  fi

  if [[ "${remote_url}" =~ ^https://github\.com/([^/]+)/([^/]+)(\.git)?$ ]]; then
    printf '%s\n' "${BASH_REMATCH[1]}"
    return 0
  fi

  return 1
}

fail() {
  echo "[fail] $*" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --github-owner)
      GITHUB_OWNER="${2:-}"
      shift 2
      ;;
    --github-repo)
      GITHUB_REPO="${2:-}"
      shift 2
      ;;
    --ref)
      REF="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "${GITHUB_OWNER}" ]]; then
  ORIGIN_URL="$(git -C "${REPO_ROOT}" remote get-url origin 2>/dev/null || true)"
  GITHUB_OWNER="$(parse_owner_from_remote "${ORIGIN_URL}" || true)"
fi

if [[ -z "${GITHUB_OWNER}" ]]; then
  fail "could not determine GitHub owner; pass --github-owner explicitly"
fi

VERSION="$(tr -d '[:space:]' < "${REPO_ROOT}/VERSION")"
TAG="v${VERSION}"

echo "[release] validating versioning"
bash "${REPO_ROOT}/scripts/validate-versioning.sh"

echo "[release] proving local and remote-style workflow from this checkout"
bash "${REPO_ROOT}/scripts/smoke-public-workflow.sh"

echo "[release] proving live GitHub install path"
bash "${REPO_ROOT}/scripts/smoke-github-install.sh" --owner "${GITHUB_OWNER}" --repo "${GITHUB_REPO}" --ref "${REF}"

echo "[release] validating bootstrap content"
python3 "${REPO_ROOT}/scripts/validate-talents.py" --root "${REPO_ROOT}/bootstrap"
python3 "${REPO_ROOT}/scripts/rebuild-index.py" --root "${REPO_ROOT}/bootstrap"
python3 "${REPO_ROOT}/scripts/sync-bootstrap.py" --live-root "${REPO_ROOT}/bootstrap" --bootstrap-root "${REPO_ROOT}/bootstrap"

echo "[release] checking diff hygiene"
git -C "${REPO_ROOT}" diff --check

if git -C "${REPO_ROOT}" rev-parse -q --verify "refs/tags/${TAG}" >/dev/null; then
  fail "tag already exists: ${TAG}"
fi

echo "[ok] tag is available: ${TAG}"
echo "[pass] release-dry-run completed for ${TAG} using ${GITHUB_OWNER}/${GITHUB_REPO}@${REF}"
