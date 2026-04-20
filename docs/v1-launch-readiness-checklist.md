# Tall Talents v1.0.0 Launch Readiness Checklist

## Reality Check

- Audit date: 2026-04-19
- Release target: Tall Talents `v1.0.0` plus canonical GitHub move to WLKRLABS
- Verdict: `NEEDS WORK`
- Release recommendation: do not cut `v1.0.0` and do not switch the canonical install/docs surface to WLKRLABS yet
- Current quality rating: `B-` for core repo/tooling, `FAILED` for the `v1.0.0` launch gate

Tall Talents is not fantasyware. The core repo is real, the install/validate/rebuild flows work, and the contributor-mode model is coherent. But the public "create a new talent" path is broken, CI does not cover the full release surface, and the repo is still wired to the current `scwlkr` home instead of being migration-ready for WLKRLABS.

## Evidence Reviewed

Fresh repo-native evidence collected on 2026-04-19:

- `python3 scripts/dev-env.py status`
- `bash scripts/doctor.sh`
- `python3 scripts/validate-talents.py --root bootstrap`
- `python3 scripts/rebuild-index.py --root bootstrap`
- `python3 scripts/sync-bootstrap.py --live-root bootstrap --bootstrap-root bootstrap`
- `git diff --check`
- fresh local install smoke in a temp `HOME`
- fresh remote install smoke via `bash <(curl -fsSL https://raw.githubusercontent.com/scwlkr/tall-talents/main/scripts/install.sh)` in a temp `HOME`
- fresh doctor/validate/rebuild checks against the remotely installed live root
- fresh `create-talent.py` smoke in a temp `HOME`
- source inspection of `README.md`, `PLAN.md`, `.github/workflows/ci.yml`, `scripts/install.sh`, and `scripts/create-talent.py`
- repo state inspection via `git remote -v` and `git tag --sort=-creatordate`

Observed outcome summary:

- Local install path: pass
- Remote raw-GitHub install path: pass
- Doctor: pass
- Validator on shipped active talents: pass
- Rebuild and sync in place: pass
- Diff hygiene: pass
- `create-talent.py` followed by validation: fail
- Git tag history in this checkout: none found

## v1.0.0 Checklist

### Core Product Integrity

- [x] Fresh local bootstrap install works on a clean temp `HOME`.
- [x] Fresh raw-GitHub install works on a clean temp `HOME`.
- [x] `doctor.sh` passes on an initialized live root.
- [x] `validate-talents.py` passes on the shipped active talent set.
- [x] `rebuild-index.py` regenerates the active index cleanly.
- [x] `sync-bootstrap.py` regenerates derived bootstrap files cleanly in contributor mode.
- [ ] `scripts/create-talent.py` generates a validator-clean draft talent file.
- [ ] README claims about the "safe talent scaffolder" are true for the shipped code.
- [ ] The `PLAN.md` release gate is actually proven by automated or scripted smoke coverage, not just by spot checks.

### Release Governance

- [x] `VERSION` and `CHANGELOG.md` exist and agree on the current release marker (`0.6.0`).
- [ ] An official repo-root release playbook exists for version bump, changelog update, tag, smoke verification, and launch sign-off.
- [ ] The official release path has been proven with at least a dry run or prior tag history.
- [ ] CI covers the user-facing release surface: install, doctor, validator, rebuild, and create/validate loop.
- [ ] The release gate is strong enough that a broken public workflow cannot pass CI unnoticed.

### WLKRLABS Migration Readiness

- [ ] README badges, clone URL, star-history link, and raw install examples are updated for the WLKRLABS canonical home.
- [ ] `scripts/install.sh` defaults (`BOOTSTRAP_BASE`, `SCRIPT_BASE`) are updated for the WLKRLABS canonical home.
- [ ] Shipped examples and prompts are scrubbed of personal-only identity defaults such as `github-scwlkr` unless they are intentionally documented as private examples.
- [ ] The repo remote, install docs, and smoke commands are re-verified against the post-move canonical GitHub location.
- [ ] The first WLKRLABS-hosted install smoke is captured before calling the launch complete.

## Highest-Priority Findings

### 1. Critical: the shipped scaffolder breaks a core product journey

`README.md` markets a "safe talent scaffolder," but a fresh smoke test showed that `scripts/create-talent.py` creates draft files that immediately fail `python3 scripts/validate-talents.py`. The root cause is visible in the generator template: it emits empty list items as `  -` instead of the parser's expected `  - ` structure, so the validator treats the generated file as invalid front matter.

Impact:

- a core advertised workflow is broken for first-time users
- the repo fails its own "documentation + rules + templates align with actual script behavior" release gate
- `v1.0.0` would ship with a known self-contradiction

### 2. High: CI does not test the actual public release surface

`.github/workflows/ci.yml` only copies `bootstrap/` into a temp root and runs validator + rebuild. It does not exercise:

- `scripts/install.sh`
- `scripts/doctor.sh`
- `scripts/create-talent.py`
- the create-then-validate workflow a new user would actually hit

Impact:

- the exact scaffolder regression above escaped the current gate
- passing CI currently does not prove the `PLAN.md` release gate

### 3. High: the official `1.0.0` release process is not formalized enough yet

The repo has `VERSION` and `CHANGELOG.md`, but this audit found no git tags in the checkout, no repo-root `RELEASE.md` or `VERSIONING.md`, and no release-oriented workflow beyond general CI validation.

Impact:

- there is no durable, repeatable "this is how we cut and verify `1.0.0`" contract yet
- the official launch would depend on memory and ad hoc commands instead of a repo-native release path

### 4. High: the repository is not yet WLKRLABS-ready

The public surface is still hard-coded to the current `scwlkr` home:

- README badges and clone/install examples
- raw GitHub install URLs
- `scripts/install.sh` default GitHub bases
- shipped example prompt using `github-scwlkr`

Impact:

- moving the canonical repo without updating these surfaces would break or misdirect public installs
- the launch would ship mixed identity signals at the exact moment trust needs to increase

## Two-Step Implementation Plan

### Step 1: Fix product truth and strengthen the release gate

Goal: make the shipped product honestly match its own claims before any branding or repo move.

Tasks:

1. Fix `scripts/create-talent.py` so generated draft files pass `validate-talents.py` out of the box.
2. Add a scripted smoke check for the full public workflow:
   - fresh temp-home install
   - doctor pass
   - validator pass
   - rebuild pass
   - create-talent pass
   - second validator pass
3. Expand CI to run that smoke check instead of only validating copied bootstrap content.
4. Re-run the full evidence loop and update this checklist from fresh output.

Exit criteria:

- all `Core Product Integrity` items are checked
- CI would fail if the scaffolder or install path regresses again
- the repo can honestly claim that its public workflows are working

### Step 2: Cut a launch-grade release surface and migrate to WLKRLABS cleanly

Goal: make `1.0.0` a real release event rather than a version number swap.

Tasks:

1. Add a repo-root release playbook for version bump, changelog update, verification commands, tag creation, and launch sign-off.
2. Update every canonical public URL and badge from the current `scwlkr` home to the WLKRLABS target.
3. Remove or neutralize personal-only identity examples from shipped assets where they would look productized.
4. Switch the canonical remote and re-run the raw-GitHub install smoke against the WLKRLABS-hosted repo.
5. Only after the above passes, bump `VERSION` to `1.0.0`, tag it, and treat that tag as the official launch candidate.

Exit criteria:

- all `Release Governance` items are checked
- all `WLKRLABS Migration Readiness` items are checked
- a fresh post-move install works from the final public URLs
- the repo is ready for an evidence-backed `v1.0.0` launch call

## Bottom Line

Tall Talents is close enough that this should be a focused hardening pass, not a rebuild. But it is not honest to call this `v1.0.0`-ready today. The right move is:

1. stay on `0.6.0`
2. fix the broken scaffolder and CI blind spot
3. formalize the release path
4. then do the WLKRLABS move and final `1.0.0` cut from a re-audited state
