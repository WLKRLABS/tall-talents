#!/usr/bin/env bash
set -euo pipefail

ROOT="${HOME}/.tall-talents"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
BOOTSTRAP_DIR="${REPO_ROOT}/bootstrap"

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

copy_if_missing "${BOOTSTRAP_DIR}/README.md" "${ROOT}/README.md"
copy_if_missing "${BOOTSTRAP_DIR}/index.md" "${ROOT}/index.md"

for file in "${BOOTSTRAP_DIR}/talents"/*.md; do
  name="$(basename "${file}")"
  copy_if_missing "${file}" "${ROOT}/talents/${name}"
done

copy_if_missing "${BOOTSTRAP_DIR}/incoming/.gitkeep" "${ROOT}/incoming/.gitkeep"
copy_if_missing "${BOOTSTRAP_DIR}/archive/.gitkeep" "${ROOT}/archive/.gitkeep"

echo
echo "[install] Tall Talents initialized at ${ROOT}"
echo "[install] Next commands:"
echo "bash scripts/doctor.sh"
echo "python3 scripts/validate-talents.py --root ~/.tall-talents"
echo "python3 scripts/rebuild-index.py --root ~/.tall-talents"
