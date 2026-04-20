# Tall Talents v1.0.0 Step 2 Handoff

## Handoff Document

### Metadata

- From: Codex agent executing Step 2 of `docs/v1-launch-readiness-checklist.md`
- To: Any follow-on launch reviewer or maintenance owner
- Phase or workstream: `v1.0.0` launch readiness / Step 2
- Task reference: `docs/v1-launch-readiness-checklist.md`
- Priority: high
- Timestamp: 2026-04-20T06:15:00-0500

### Context

- Current state: Step 2 is complete. The canonical public home is now `WLKRLABS/tall-talents`, the local `origin` remote points there, the public GitHub install smoke passes there, and the full release dry run passes there.
- Relevant files:
  - `docs/v1-launch-readiness-checklist.md` - updated source-of-truth checklist and Step 2 scope
  - `README.md` - canonical badges, clone/install URLs, star-history link, and version badge now point at WLKRLABS
  - `VERSIONING.md` - new version/changelog/tag contract
  - `RELEASE.md` - new release playbook and cutover order
  - `scripts/validate-versioning.sh` - new version/changelog validator
  - `scripts/smoke-github-install.sh` - new live GitHub raw-install smoke
  - `scripts/release-dry-run.sh` - new end-to-end release dry run
  - `scripts/install.sh` - default raw GitHub bases now point at `WLKRLABS/tall-talents`
  - `CHANGELOG.md` - release notes surface for `1.0.0`
  - `VERSION` - now set to `1.0.0`
  - `.github/workflows/ci.yml` - smoke gate already in place and should remain the Step 2 verification backbone
  - `scripts/smoke-public-workflow.sh` - rerun before closing Step 2, then add the final GitHub-hosted smoke on top
  - `bootstrap/talents/github-ssh-repo-alias-setup.md` - personal-only alias example has been neutralized to `github-work`
- Dependencies:
  - Step 1 completed on 2026-04-20
  - `bash scripts/smoke-public-workflow.sh` passed
  - `bash scripts/validate-versioning.sh` passed
  - `bash scripts/smoke-github-install.sh --owner WLKRLABS --ref main` passed
  - `bash scripts/release-dry-run.sh --github-owner WLKRLABS --ref main` passed
  - `bash scripts/doctor.sh` passed
  - `python3 scripts/validate-talents.py --root bootstrap` passed
  - `python3 scripts/rebuild-index.py --root bootstrap` passed
  - `python3 scripts/sync-bootstrap.py --live-root bootstrap --bootstrap-root bootstrap` passed
  - `git diff --check` passed
  - `gh run list --repo WLKRLABS/tall-talents --limit 5` shows the first `ci` run completed successfully on the WLKRLABS `main` push
- Constraints:
  - Contributor mode is active: `python3 scripts/dev-env.py status` reports `linked: yes`, so `~/.tall-talents` and `bootstrap/` are the same files in this checkout.
  - Cut the `v1.0.0` tag only from the verified release commit.
  - Keep future canonical-home changes gated by the same public smoke path used here.

### Deliverable Request

- What is needed: if anything follows this handoff, it is post-launch monitoring or later release work, not unfinished Step 2 launch gating.
- Acceptance criteria:
  - Keep the `Release Governance` and `WLKRLABS Migration Readiness` sections green.
  - Preserve the verified public install path from `https://raw.githubusercontent.com/WLKRLABS/tall-talents/main/scripts/install.sh`.
  - Preserve the repo-root release contract in `RELEASE.md` and `VERSIONING.md`.
- Reference materials:
  - `docs/v1-launch-readiness-checklist.md`
  - `README.md`
  - `VERSIONING.md`
  - `RELEASE.md`
  - `scripts/install.sh`
  - `scripts/validate-versioning.sh`
  - `scripts/smoke-github-install.sh`
  - `scripts/release-dry-run.sh`
  - `CHANGELOG.md`
  - `VERSION`
  - `.github/workflows/ci.yml`
  - `scripts/smoke-public-workflow.sh`

### Quality Expectations

- Must pass:
  - `bash scripts/validate-versioning.sh`
  - `bash scripts/smoke-github-install.sh --owner WLKRLABS --ref main`
  - `bash scripts/release-dry-run.sh --github-owner WLKRLABS --ref main`
  - `bash scripts/smoke-public-workflow.sh`
  - `bash <(curl -fsSL https://raw.githubusercontent.com/<final-home>/tall-talents/main/scripts/install.sh)` in a clean temp `HOME`
  - `bash scripts/doctor.sh`
  - `python3 scripts/validate-talents.py --root bootstrap`
  - `python3 scripts/rebuild-index.py --root bootstrap`
  - `python3 scripts/sync-bootstrap.py --live-root bootstrap --bootstrap-root bootstrap`
  - `git diff --check`
- Evidence required:
  - Exact canonical remote URL: `https://github.com/WLKRLABS/tall-talents.git`
  - Exact release playbook file path and the commands it prescribes: `RELEASE.md`
  - Exact public URLs changed in `README.md` and `scripts/install.sh`
  - Install smoke summary for the final GitHub-hosted path
  - First successful WLKRLABS GitHub Actions run ID
- Next handoff: none required for Step 2; if the `v1.0.0` tag is cut in the same session, this handoff can be treated as the completion record
