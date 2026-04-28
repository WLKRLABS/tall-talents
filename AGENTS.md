# Tall Talents Repo Protocol

This repository has two valid operating modes. Do not confuse them.

## Source Of Truth Modes

### 1. Normal user mode

- Live library root is `~/.tall-talents`
- Agents read and write live talents there
- If repo snapshot updates are needed, run:
  - `python3 scripts/sync-bootstrap.py --live-root ~/.tall-talents --bootstrap-root bootstrap`

### 2. Repo contributor mode

- Install with:
  - `python3 scripts/dev-env.py install`
- This repoints `~/.tall-talents` to this repo's `bootstrap/` directory
- In this mode, editing `~/.tall-talents` and editing `bootstrap/` are the same thing
- `.githooks/pre-commit` validates `bootstrap/`, regenerates `bootstrap/index.md`, and updates `bootstrap/manifest.txt`

## When Working In This Repo

Before changing talent content or install/sync tooling:

1. Read:
   - `README.md`
   - `ARCHITECTURE.md`
   - `scripts/install.sh`
   - `scripts/dev-env.py`
   - `scripts/sync-bootstrap.py`
2. Determine which mode is active:
   - `python3 scripts/dev-env.py status`
3. If repo contributor mode is not active, do not assume edits to `~/.tall-talents` will appear in this repo automatically.
4. If you changed the live library outside repo contributor mode, sync it back into `bootstrap/` before finishing.

## Edit Boundary

- Committed repo snapshot lives in `bootstrap/`
- Shipped install seed is defined by `bootstrap/manifest.txt`
- `bootstrap/index.md` is derived from active bootstrap talents
- `bootstrap/private/` is local-only and must not be committed
- `scripts/install.sh` must stay in sync with the manifest-based bootstrap workflow

## Required Verification

For repo changes that touch talent content or bootstrap/install flow, run:

- `python3 scripts/validate-talents.py --root bootstrap`
- `python3 scripts/scan-talent-privacy.py --root bootstrap`
- `python3 scripts/sync-bootstrap.py --live-root bootstrap --bootstrap-root bootstrap`
- `git diff --check`

If operating in normal user mode and importing from the live library, also run:

- `python3 scripts/sync-bootstrap.py --live-root ~/.tall-talents --bootstrap-root bootstrap`

## Failure To Avoid

- Writing only to `~/.tall-talents` while expecting this repo's `bootstrap/` to update itself
- Editing `bootstrap/` but forgetting to regenerate `bootstrap/index.md` and `bootstrap/manifest.txt`
- Committing owner-only private context instead of keeping it in `~/.tall-talents/private/`
- Modifying install/dev-mode tooling without checking how contributor mode repoints the live root
