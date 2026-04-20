# Changelog

## Unreleased

## 1.0.0 - 2026-04-20

- Added repo-root `VERSIONING.md` and `RELEASE.md` so versioning, dry runs, cutover rules, and tag flow are explicit instead of ad hoc.
- Added `scripts/validate-versioning.sh`, `scripts/smoke-github-install.sh`, and `scripts/release-dry-run.sh` to prove the release path from both the checkout and a live GitHub raw-install surface.
- Scrubbed the shipped personal-only SSH alias example and completed the canonical-home cutover to `WLKRLABS/tall-talents`.
- Switched the canonical public README/install surface and installer defaults to the WLKRLABS GitHub home.
- Proved the launch candidate with a live GitHub install smoke and a full release dry run against the WLKRLABS-hosted repo.

## 0.6.0 - 2026-04-17

- Rewrote `README.md` around the Tall Talents brand position, usage model, and repo role.
- Added a true one-command install path by making `scripts/install.sh` work from either a local checkout or a raw GitHub script invocation.
- Refreshed `bootstrap/README.md` so the seeded live library copy matches the tighter product language.

## 0.5.0 - 2026-04-17

- Marked Phase 3 (Enforcement), Phase 4 (Agent workflow hardening), and Phase 5 (v1 hardening) as complete in `PLAN.md`.
- Verified enforcement and hardening scripts against bootstrap content, including install/doctor/validate/rebuild flows.
- Verified bootstrap and examples talent content remain synchronized for the three baseline talents.

## 0.2.0 - 2026-04-17

- Marked Phase 2 (Bootstrap) complete in the implementation plan.
- Confirmed bootstrap root includes live README, index, lifecycle folders, and three real talents.

## 0.1.0 - 2026-04-17

- Initial reference implementation scaffold.
- Strict talent format rules and templates.
- Three operational example talents.
- Bootstrap global live-folder contents.
- Install/doctor/validate/rebuild/create scripts.
- Minimal macOS CI workflow.
