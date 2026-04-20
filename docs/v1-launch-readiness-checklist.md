# Tall Talents v1.0.0 Launch Readiness Checklist

## Reality Check

- Audit/update date: 2026-04-20
- Release target: Tall Talents `v1.0.0` plus canonical GitHub move to WLKRLABS
- Verdict: `READY`
- Release recommendation: cut `v1.0.0` from the WLKRLABS canonical home
- Current quality rating: `A` for the `v1.0.0` launch candidate

Step 1 and Step 2 are complete. Tall Talents now has a repo-root release contract, a public GitHub install smoke, a full release dry run, a live WLKRLABS canonical repo, and a successful first CI run on that new home.

## Evidence Reviewed

Fresh repo-native evidence collected on 2026-04-20:

- `python3 scripts/dev-env.py status`
- `bash scripts/doctor.sh`
- `python3 scripts/validate-talents.py --root bootstrap`
- `python3 scripts/rebuild-index.py --root bootstrap`
- `python3 scripts/sync-bootstrap.py --live-root bootstrap --bootstrap-root bootstrap`
- `git diff --check`
- `bash -n scripts/smoke-public-workflow.sh`
- `bash -n scripts/validate-versioning.sh`
- `bash -n scripts/smoke-github-install.sh`
- `bash -n scripts/release-dry-run.sh`
- `python3 -m py_compile scripts/create-talent.py scripts/validate-talents.py scripts/rebuild-index.py scripts/sync-bootstrap.py`
- `bash scripts/smoke-public-workflow.sh`
- `bash scripts/validate-versioning.sh`
- `bash scripts/smoke-github-install.sh --owner WLKRLABS --ref main`
- `bash scripts/release-dry-run.sh --github-owner WLKRLABS --ref main`
- `git ls-remote --heads https://github.com/WLKRLABS/tall-talents.git`
- `curl -fsSI https://raw.githubusercontent.com/WLKRLABS/tall-talents/main/scripts/install.sh`
- `gh run list --repo WLKRLABS/tall-talents --limit 5`
- source inspection of `README.md`, `PLAN.md`, `.github/workflows/ci.yml`, `scripts/install.sh`, `scripts/create-talent.py`, `scripts/smoke-public-workflow.sh`, `scripts/validate-talents.py`, `scripts/rebuild-index.py`, and `scripts/sync-bootstrap.py`
- repo state inspection via `git remote -v` and `git tag --sort=-creatordate`

Observed outcome summary:

- Contributor mode: pass (`linked: yes`)
- Local install path: pass
- Remote-style raw install path against the current checkout: pass
- Doctor: pass
- Validator on shipped active talents: pass
- Rebuild and sync in place: pass
- `create-talent.py` followed by validation: pass
- CI release gate coverage: pass in repo definition and in the first WLKRLABS push run
- Current remote: `https://github.com/WLKRLABS/tall-talents.git`
- Git tag history in this checkout: none found
- Repo-root release playbook: pass (`RELEASE.md`, `VERSIONING.md`)
- Release dry run against WLKRLABS canonical home: pass (`scripts/release-dry-run.sh --github-owner WLKRLABS --ref main`)
- Live GitHub install smoke against WLKRLABS canonical home: pass (`scripts/smoke-github-install.sh --owner WLKRLABS --ref main`)
- WLKRLABS repo availability: pass
- First WLKRLABS CI run: pass (`Prepare WLKRLABS launch surface`, GitHub Actions `ci`, push to `main`)

## v1.0.0 Checklist

### Core Product Integrity

- [x] Fresh local bootstrap install works on a clean temp `HOME`.
- [x] Fresh remote-style raw install works on a clean temp `HOME`.
- [x] `doctor.sh` passes on an initialized live root.
- [x] `validate-talents.py` passes on the shipped active talent set.
- [x] `rebuild-index.py` regenerates the active index cleanly.
- [x] `sync-bootstrap.py` regenerates derived bootstrap files cleanly in contributor mode.
- [x] `scripts/create-talent.py` generates a validator-clean draft talent file.
- [x] README claims about the "safe talent scaffolder" are true for the shipped code.
- [x] The `PLAN.md` release gate is actually proven by automated or scripted smoke coverage, not just by spot checks.

### Release Governance

- [x] `VERSION` and `CHANGELOG.md` exist and agree on the current release marker (`1.0.0`).
- [x] An official repo-root release playbook exists for version bump, changelog update, tag, smoke verification, and launch sign-off.
- [x] The official release path has been proven with at least a dry run or prior tag history.
- [x] CI covers the user-facing release surface: install, doctor, validator, rebuild, and create/validate loop.
- [x] The release gate is strong enough that a broken public workflow cannot pass CI unnoticed.

### WLKRLABS Migration Readiness

- [x] README badges, clone URL, star-history link, and raw install examples are updated for the WLKRLABS canonical home.
- [x] `scripts/install.sh` defaults (`BOOTSTRAP_BASE`, `SCRIPT_BASE`) are updated for the WLKRLABS canonical home.
- [x] Shipped examples and prompts are scrubbed of personal-only identity defaults such as `github-scwlkr` unless they are intentionally documented as private examples.
- [x] The repo remote, install docs, and smoke commands are re-verified against the post-move canonical GitHub location.
- [x] The first WLKRLABS-hosted install smoke is captured before calling the launch complete.

## Step 1 Completion Update

- `scripts/create-talent.py` now emits validator-clean draft content with explicit placeholders instead of invalid blank list-item lines.
- `scripts/validate-talents.py`, `scripts/rebuild-index.py`, and `scripts/sync-bootstrap.py` now tolerate the prior blank-list form so older drafts cannot break the parser path unexpectedly.
- `scripts/smoke-public-workflow.sh` now exercises the full public workflow in both local-install and remote-style-install modes.
- `.github/workflows/ci.yml` now runs the public-workflow smoke gate instead of only validating a copied bootstrap snapshot.
- `README.md` now documents the smoke gate as part of the repo's proof surface.

## Remaining Highest-Priority Findings

No Step 2 launch blockers remain from this checklist.

## Two-Step Implementation Plan

### Step 1: Fix product truth and strengthen the release gate

Status: completed on 2026-04-20

Completed tasks:

1. Fixed `scripts/create-talent.py` so generated draft files pass `validate-talents.py` out of the box.
2. Added `scripts/smoke-public-workflow.sh` for the full public workflow:
   - fresh temp-home install
   - doctor pass
   - validator pass
   - rebuild pass
   - create-talent pass
   - second validator pass
3. Expanded CI to run that smoke check instead of only validating copied bootstrap content.
4. Re-ran the evidence loop and refreshed this checklist from fresh output.

Exit criteria met:

- all `Core Product Integrity` items are checked
- CI now fails if the scaffolder or install path regresses inside the covered smoke path
- the repo can honestly claim that its local and remote-style public workflows are working

### Step 2: Cut a launch-grade release surface and migrate to WLKRLABS cleanly

Status: completed on 2026-04-20

Persistent handoff: [docs/v1-launch-step-2-handoff.md](/Users/shanewalker/Desktop/dev/tall-talents/docs/v1-launch-step-2-handoff.md)

Goal: make `1.0.0` a real release event rather than a version number swap.

Tasks:

1. Add a repo-root release playbook for version bump, changelog update, verification commands, tag creation, and launch sign-off.
   Status: completed via `RELEASE.md`, `VERSIONING.md`, `scripts/validate-versioning.sh`, `scripts/smoke-github-install.sh`, and `scripts/release-dry-run.sh`.
2. Update every canonical public URL and badge from the current `scwlkr` home to the WLKRLABS target.
   Status: completed in `README.md`.
3. Remove or neutralize personal-only identity examples from shipped assets where they would look productized.
   Status: completed via the shipped SSH-alias talent example cleanup.
4. Switch the canonical remote and re-run the raw-GitHub install smoke against the WLKRLABS-hosted repo.
   Status: completed. `origin` now points at `https://github.com/WLKRLABS/tall-talents.git`, and the WLKRLABS smoke passes.
5. Only after the above passes, bump `VERSION` to `1.0.0`, tag it, and treat that tag as the official launch candidate.
   Status: in progress in this session. `VERSION` and `CHANGELOG.md` are now on `1.0.0`, and the tag can be cut from the verified release commit.

Exit criteria:

- all `Release Governance` items are checked
- all `WLKRLABS Migration Readiness` items are checked
- a fresh post-move install works from the final public URLs
- the repo is ready for an evidence-backed `v1.0.0` launch call

## Bottom Line

Tall Talents does not need a rebuild. The repo is now ready for the `v1.0.0` tag from the WLKRLABS canonical home. The public installer works, the release dry run passes, the canonical remote is switched, and the first WLKRLABS CI run is green.
