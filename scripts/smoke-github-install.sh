#!/usr/bin/env bash
set -euo pipefail

OWNER=""
REPO="tall-talents"
REF="main"
WORK_DIR=""

usage() {
  cat <<'EOF'
Usage: bash scripts/smoke-github-install.sh --owner <github-owner> [--repo tall-talents] [--ref main]
EOF
}

cleanup() {
  if [[ -n "${WORK_DIR}" && -d "${WORK_DIR}" ]]; then
    rm -rf "${WORK_DIR}"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --owner)
      OWNER="${2:-}"
      shift 2
      ;;
    --repo)
      REPO="${2:-}"
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

if [[ -z "${OWNER}" ]]; then
  usage >&2
  exit 1
fi

if ! command -v curl >/dev/null 2>&1; then
  echo "[missing] curl is required for smoke-github-install.sh" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "[missing] python3 is required for smoke-github-install.sh" >&2
  exit 1
fi

RAW_BASE="https://raw.githubusercontent.com/${OWNER}/${REPO}/${REF}"
SCRIPT_BASE="${RAW_BASE}/scripts"
BOOTSTRAP_BASE="${RAW_BASE}/bootstrap"
WORK_DIR="$(mktemp -d "${TMPDIR:-/tmp}/tall-talents-github-smoke.XXXXXX")"
trap cleanup EXIT

HOME_DIR="${WORK_DIR}/home"
LIVE_ROOT="${HOME_DIR}/.tall-talents"
mkdir -p "${HOME_DIR}"

echo "[smoke] GitHub install path: ${OWNER}/${REPO}@${REF}"

HOME="${HOME_DIR}" \
TALL_TALENTS_INSTALL_MODE=remote \
TALL_TALENTS_BOOTSTRAP_BASE="${BOOTSTRAP_BASE}" \
TALL_TALENTS_SCRIPT_BASE="${SCRIPT_BASE}" \
  bash <(curl -fsSL "${SCRIPT_BASE}/install.sh")

HOME="${HOME_DIR}" bash <(curl -fsSL "${SCRIPT_BASE}/doctor.sh")
HOME="${HOME_DIR}" python3 <(curl -fsSL "${SCRIPT_BASE}/validate-talents.py") --root "${LIVE_ROOT}"
HOME="${HOME_DIR}" python3 <(curl -fsSL "${SCRIPT_BASE}/rebuild-index.py") --root "${LIVE_ROOT}"
HOME="${HOME_DIR}" python3 <(curl -fsSL "${SCRIPT_BASE}/create-talent.py") \
  --root "${LIVE_ROOT}" \
  --title "GitHub Smoke Test Talent" \
  --summary "Verify the public GitHub install path stays validator-clean."
HOME="${HOME_DIR}" python3 <(curl -fsSL "${SCRIPT_BASE}/validate-talents.py") --root "${LIVE_ROOT}"

echo "[pass] smoke-github-install completed for ${OWNER}/${REPO}@${REF}"
