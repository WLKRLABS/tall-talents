#!/usr/bin/env bash
set -euo pipefail

ROOT="${HOME}/.tall-talents"
missing=0

check_path() {
  local path="$1"
  local label="$2"
  if [[ -e "${path}" ]]; then
    echo "[ok] ${label}: ${path}"
  else
    echo "[missing] ${label}: ${path}"
    missing=1
  fi
}

if command -v python3 >/dev/null 2>&1; then
  echo "[ok] python3: $(python3 --version)"
else
  echo "[missing] python3 is required"
  exit 1
fi

check_path "${ROOT}" "live root"
check_path "${ROOT}/talents" "talents dir"
check_path "${ROOT}/incoming" "incoming dir"
check_path "${ROOT}/archive" "archive dir"
check_path "${ROOT}/index.md" "index file"

if [[ "${missing}" -ne 0 ]]; then
  echo "[fail] doctor checks failed"
  exit 1
fi

echo "[pass] doctor checks passed"
