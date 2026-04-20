#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
VERSION_FILE="${REPO_ROOT}/VERSION"
CHANGELOG_FILE="${REPO_ROOT}/CHANGELOG.md"

fail() {
  echo "[fail] $*" >&2
  exit 1
}

if [[ ! -f "${VERSION_FILE}" ]]; then
  fail "missing VERSION file"
fi

if [[ ! -f "${CHANGELOG_FILE}" ]]; then
  fail "missing CHANGELOG.md"
fi

VERSION="$(tr -d '[:space:]' < "${VERSION_FILE}")"

if [[ ! "${VERSION}" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  fail "VERSION must be plain SemVer (found: ${VERSION})"
fi

if ! grep -Eq '^## Unreleased$' "${CHANGELOG_FILE}"; then
  fail "CHANGELOG.md must include a top-level '## Unreleased' section"
fi

FIRST_RELEASE_LINE="$(grep -En '^## [0-9]+\.[0-9]+\.[0-9]+ - [0-9]{4}-[0-9]{2}-[0-9]{2}$' "${CHANGELOG_FILE}" | head -n 1 || true)"

if [[ -z "${FIRST_RELEASE_LINE}" ]]; then
  fail "CHANGELOG.md must include at least one released version heading"
fi

FIRST_RELEASE_VERSION="$(printf '%s\n' "${FIRST_RELEASE_LINE}" | sed -E 's/^[0-9]+:## ([0-9]+\.[0-9]+\.[0-9]+) - .*/\1/')"

if [[ "${FIRST_RELEASE_VERSION}" != "${VERSION}" ]]; then
  fail "VERSION (${VERSION}) must match the latest released changelog heading (${FIRST_RELEASE_VERSION})"
fi

echo "[ok] VERSION is valid SemVer: ${VERSION}"
echo "[ok] CHANGELOG includes an Unreleased section"
echo "[ok] Latest released changelog entry matches VERSION"
