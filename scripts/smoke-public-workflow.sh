#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
MODE="both"
WORK_DIR=""
SERVER_PID=""
SERVER_PORT=""
SERVER_LOG=""

usage() {
  cat <<'EOF'
Usage: bash scripts/smoke-public-workflow.sh [--mode local|remote|both]
EOF
}

cleanup() {
  if [[ -n "${SERVER_PID}" ]]; then
    kill "${SERVER_PID}" >/dev/null 2>&1 || true
    wait "${SERVER_PID}" 2>/dev/null || true
  fi
  if [[ -n "${WORK_DIR}" && -d "${WORK_DIR}" ]]; then
    rm -rf "${WORK_DIR}"
  fi
}

find_free_port() {
  python3 - <<'PY'
import socket

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 0))
    print(sock.getsockname()[1])
PY
}

wait_for_url() {
  local url="$1"
  local attempts=50

  for ((i = 1; i <= attempts; i += 1)); do
    if curl -fsSL "${url}" >/dev/null 2>&1; then
      return 0
    fi
    sleep 0.1
  done

  echo "[fail] timed out waiting for ${url}" >&2
  if [[ -n "${SERVER_LOG}" && -f "${SERVER_LOG}" ]]; then
    cat "${SERVER_LOG}" >&2
  fi
  return 1
}

run_checks() {
  local home_dir="$1"
  local live_root="${home_dir}/.tall-talents"

  HOME="${home_dir}" bash "${REPO_ROOT}/scripts/doctor.sh"
  HOME="${home_dir}" python3 "${REPO_ROOT}/scripts/validate-talents.py" --root "${live_root}"
  HOME="${home_dir}" python3 "${REPO_ROOT}/scripts/scan-talent-privacy.py" --root "${live_root}"
  HOME="${home_dir}" python3 "${REPO_ROOT}/scripts/rebuild-index.py" --root "${live_root}"
  HOME="${home_dir}" python3 "${REPO_ROOT}/scripts/create-talent.py" \
    --root "${live_root}" \
    --title "Smoke Test Talent" \
    --summary "Verify the scaffolder produces a validator-clean draft."
  HOME="${home_dir}" python3 "${REPO_ROOT}/scripts/validate-talents.py" --root "${live_root}"
  HOME="${home_dir}" python3 "${REPO_ROOT}/scripts/scan-talent-privacy.py" --root "${live_root}"
}

run_local_smoke() {
  local home_dir="${WORK_DIR}/local-home"
  mkdir -p "${home_dir}"

  echo "[smoke] local install path"
  HOME="${home_dir}" TALL_TALENTS_INSTALL_MODE=local bash "${REPO_ROOT}/scripts/install.sh"
  run_checks "${home_dir}"
}

run_remote_smoke() {
  local home_dir="${WORK_DIR}/remote-home"
  mkdir -p "${home_dir}"

  SERVER_PORT="$(find_free_port)"
  SERVER_LOG="${WORK_DIR}/http-server.log"

  echo "[smoke] remote-style install path"
  python3 -m http.server "${SERVER_PORT}" --bind 127.0.0.1 --directory "${REPO_ROOT}" >"${SERVER_LOG}" 2>&1 &
  SERVER_PID=$!
  wait_for_url "http://127.0.0.1:${SERVER_PORT}/scripts/install.sh"

  HOME="${home_dir}" \
  TALL_TALENTS_INSTALL_MODE=remote \
  TALL_TALENTS_BOOTSTRAP_BASE="http://127.0.0.1:${SERVER_PORT}/bootstrap" \
  TALL_TALENTS_SCRIPT_BASE="http://127.0.0.1:${SERVER_PORT}/scripts" \
    bash <(curl -fsSL "http://127.0.0.1:${SERVER_PORT}/scripts/install.sh")

  run_checks "${home_dir}"
}

if [[ $# -eq 2 && "$1" == "--mode" ]]; then
  MODE="$2"
elif [[ $# -ne 0 ]]; then
  usage >&2
  exit 1
fi

case "${MODE}" in
  local|remote|both)
    ;;
  *)
    usage >&2
    exit 1
    ;;
esac

if ! command -v curl >/dev/null 2>&1; then
  echo "[missing] curl is required for smoke-public-workflow.sh" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "[missing] python3 is required for smoke-public-workflow.sh" >&2
  exit 1
fi

WORK_DIR="$(mktemp -d "${TMPDIR:-/tmp}/tall-talents-smoke.XXXXXX")"
trap cleanup EXIT

case "${MODE}" in
  local)
    run_local_smoke
    ;;
  remote)
    run_remote_smoke
    ;;
  both)
    run_local_smoke
    run_remote_smoke
    ;;
esac

echo "[pass] smoke-public-workflow completed (${MODE})"
