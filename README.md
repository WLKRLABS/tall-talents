<p align="center">
  <img src="brand/logo.png" alt="Tall Talents logo" width="148">
</p>

# Tall Talents

**Always Exceptional Design.**

**A global, file-based talent library for coding agents.**

Tall Talents is a system for capturing hard-won workflows and reusing them across projects. This repository is the reference implementation and tooling for the live library at `~/.tall-talents`.

No apps.  
No databases.  
No abstractions.

Just files.

## What is a Talent?

A talent is a reusable, operational workflow written as a markdown file.

It represents something you actually struggled through and solved. If you could hand it to an agent later and get a better result than starting from scratch, it is a talent.

## Core Idea

You already do this:

1. Struggle through a problem
2. Figure it out
3. Move on

Tall Talents adds one step:

4. Capture the solution so you never do it again

## Global System

All live talents live here:

```bash
~/.tall-talents
```

Structure:

```bash
~/.tall-talents/
├─ index.md
├─ talents/
├─ incoming/
└─ archive/
```

This is the single source of truth.

## Install

### Quick install

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/scwlkr/tall-talents/main/scripts/install.sh)
```

That bootstraps `~/.tall-talents` without cloning the repo first.

### Optional verify

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/scwlkr/tall-talents/main/scripts/doctor.sh)
```

### Local repo workflow

```bash
git clone https://github.com/scwlkr/tall-talents.git
cd tall-talents
bash scripts/install.sh
bash scripts/doctor.sh
python3 scripts/validate-talents.py --root ~/.tall-talents
python3 scripts/rebuild-index.py --root ~/.tall-talents
```

## Usage

### Use Tall Talents

Start any non-trivial task with:

```text
Use Tall Talents.
```

Then:

- Read `~/.tall-talents/index.md`
- Open relevant files in `~/.tall-talents/talents/`
- Apply matching talents literally
- If none fit, say so explicitly and do not force-fit one

### Create or update a talent

After solving something difficult:

- Use `templates/create-talent-from-session.md`
- Decide whether to create a new talent, update an existing talent, or do no talent
- Write the markdown file in `~/.tall-talents/talents/`
- Rebuild `~/.tall-talents/index.md`
- Validate the library

## Commands

```bash
bash scripts/install.sh
bash scripts/doctor.sh
python3 scripts/validate-talents.py --root ~/.tall-talents
python3 scripts/rebuild-index.py --root ~/.tall-talents
python3 scripts/create-talent.py --title "My Talent" --summary "One-line summary"
```

## Philosophy

- Files are the source of truth
- No hidden state
- No automation magic
- No generic advice
- Only real, reusable workflows

A talent should exist only if you would actually reuse it.

## What This Is Not

- Not an agent framework
- Not a SaaS product
- Not a prompt library
- Not a memory system

It is a discipline backed by a folder.

## Example

`fix-ad-hoc-codesign-fallback`

Instead of rediscovering macOS signing issues every time, you reuse a workflow that already works.

## Scripts

- `scripts/install.sh` — bootstrap `~/.tall-talents` from the local repo or directly from GitHub raw files.
- `scripts/doctor.sh` — verify environment and live folder layout.
- `scripts/validate-talents.py` — enforce the talent format contract.
- `scripts/rebuild-index.py` — regenerate `~/.tall-talents/index.md`.
- `scripts/create-talent.py` — scaffold a new talent file from a title and summary.

## Versioning

This repo uses SemVer.

- `VERSION` is the repository version marker.
- `CHANGELOG.md` tracks notable changes.
- `1.0.0` is the stability target for the file format, tooling, and workflow.

## Author

WLKR LABS  
Always Exceptional Design.
