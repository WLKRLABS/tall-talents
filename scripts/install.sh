#!/usr/bin/env bash
set -euo pipefail

ROOT="${HOME}/.tall-talents"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
BOOTSTRAP_DIR="${REPO_ROOT}/bootstrap"
INSTALL_MODE="${TALL_TALENTS_INSTALL_MODE:-auto}"
TALL_TALENTS_REF="${TALL_TALENTS_REF:-main}"
BOOTSTRAP_BASE="${TALL_TALENTS_BOOTSTRAP_BASE:-https://raw.githubusercontent.com/scwlkr/tall-talents/${TALL_TALENTS_REF}/bootstrap}"
SCRIPT_BASE="${TALL_TALENTS_SCRIPT_BASE:-https://raw.githubusercontent.com/scwlkr/tall-talents/${TALL_TALENTS_REF}/scripts}"

# Keep this list in sync with bootstrap/ when adding or removing seeded files.
REMOTE_BOOTSTRAP_FILES=(
  "README.md"
  "index.md"
  "talents/fix-ad-hoc-codesign-fallback.md"
  "talents/gh-pages-site-subfolder-assets.md"
  "talents/literal-wordpress-port-mode.md"
  "incoming/.gitkeep"
  "archive/.gitkeep"
)

mkdir -p "${ROOT}" "${ROOT}/talents" "${ROOT}/incoming" "${ROOT}/archive"

copy_if_missing() {
  local src="$1"
  local dst="$2"
  if [[ ! -e "${dst}" ]]; then
    cp "${src}" "${dst}"
    echo "[install] copied: ${dst}"
  else
    echo "[install] kept existing: ${dst}"
  fi
}

download_if_missing() {
  local rel="$1"
  local dst="$2"
  if [[ ! -e "${dst}" ]]; then
    curl -fsSL "${BOOTSTRAP_BASE}/${rel}" -o "${dst}"
    echo "[install] downloaded: ${dst}"
  else
    echo "[install] kept existing: ${dst}"
  fi
}

has_local_bootstrap() {
  [[ -f "${BOOTSTRAP_DIR}/README.md" ]] \
    && [[ -f "${BOOTSTRAP_DIR}/index.md" ]] \
    && [[ -d "${BOOTSTRAP_DIR}/talents" ]]
}

install_from_local() {
  copy_if_missing "${BOOTSTRAP_DIR}/README.md" "${ROOT}/README.md"
  copy_if_missing "${BOOTSTRAP_DIR}/index.md" "${ROOT}/index.md"

  for file in "${BOOTSTRAP_DIR}/talents"/*.md; do
    name="$(basename "${file}")"
    copy_if_missing "${file}" "${ROOT}/talents/${name}"
  done

  copy_if_missing "${BOOTSTRAP_DIR}/incoming/.gitkeep" "${ROOT}/incoming/.gitkeep"
  copy_if_missing "${BOOTSTRAP_DIR}/archive/.gitkeep" "${ROOT}/archive/.gitkeep"
}

install_from_remote() {
  if ! command -v curl >/dev/null 2>&1; then
    echo "[missing] curl is required for remote install mode"
    exit 1
  fi

  for rel in "${REMOTE_BOOTSTRAP_FILES[@]}"; do
    download_if_missing "${rel}" "${ROOT}/${rel}"
  done
}

print_next_commands() {
  local source="$1"
  echo
  echo "[install] Tall Talents initialized at ${ROOT}"
  if [[ "${source}" == "remote" ]]; then
    echo "[install] Optional follow-up commands:"
    echo "bash <(curl -fsSL ${SCRIPT_BASE}/doctor.sh)"
    echo "python3 <(curl -fsSL ${SCRIPT_BASE}/validate-talents.py) --root ~/.tall-talents"
    echo "python3 <(curl -fsSL ${SCRIPT_BASE}/rebuild-index.py) --root ~/.tall-talents"
  else
    echo "[install] Next commands:"
    echo "bash scripts/doctor.sh"
    echo "python3 scripts/validate-talents.py --root ~/.tall-talents"
    echo "python3 scripts/rebuild-index.py --root ~/.tall-talents"
  fi
}

case "${INSTALL_MODE}" in
  auto)
    if has_local_bootstrap; then
      install_from_local
      print_next_commands "local"
    else
      install_from_remote
      print_next_commands "remote"
    fi
    ;;
  local)
    if ! has_local_bootstrap; then
      echo "[fail] local bootstrap content not found at ${BOOTSTRAP_DIR}"
      exit 1
    fi
    install_from_local
    print_next_commands "local"
    ;;
  remote)
    install_from_remote
    print_next_commands "remote"
    ;;
  *)
    echo "[fail] invalid TALL_TALENTS_INSTALL_MODE: ${INSTALL_MODE}"
    echo "[fail] expected one of: auto, local, remote"
    exit 1
    ;;
esac
