# Tall Talents

Tall Talents is a **filesystem-first, markdown-based global talent library** for coding agents.

A **talent** is a reusable operational workflow captured from real solved work. This repository is the **reference implementation and tooling**. The live library is always global at:

`~/.tall-talents`

## What this repository is (and is not)

This repo is:
- a strict format spec for talents
- lightweight scripts to install, validate, scaffold, and rebuild index files
- bootstrap content for initializing a new global library

This repo is not:
- an app
- a web service
- a database product
- a daemon
- a cloud backend

## Install

```bash
chmod +x scripts/install.sh scripts/doctor.sh scripts/*.py
bash scripts/install.sh
bash scripts/doctor.sh
python3 scripts/validate-talents.py --root ~/.tall-talents
python3 scripts/rebuild-index.py --root ~/.tall-talents
```

## Daily usage flow

1. Solve real work with your coding agent.
2. Run the create-talent prompt template from `templates/create-talent-from-session.md`.
3. Agent creates or updates one file in `~/.tall-talents/talents/`.
4. Agent updates `~/.tall-talents/index.md` (or run rebuild script).
5. Reuse that talent in future work.

## Create-after-session flow

Use `templates/create-talent-from-session.md` in the same session where work was completed. The template forces the agent to:
- inspect `~/.tall-talents/index.md`
- decide whether to create new, update existing, or do no talent
- keep output grounded in what actually worked
- update index content after changes

## Available scripts

- `scripts/install.sh` — bootstrap `~/.tall-talents` from `bootstrap/` without overwriting existing talents.
- `scripts/doctor.sh` — verify required tools and required live folder layout.
- `scripts/validate-talents.py` — enforce format contract over all talent files.
- `scripts/rebuild-index.py` — regenerate `~/.tall-talents/index.md` from active talents only.
- `scripts/create-talent.py` — scaffold a new talent file from title + summary.

## Versioning and releases

- `VERSION` is the repository version marker.
- `CHANGELOG.md` tracks notable changes.
- v1.0.0 quality gate: strict format, deterministic index rebuild, successful install/doctor/validate/rebuild on macOS, and real example talents.

## License

See `LICENSE`.
