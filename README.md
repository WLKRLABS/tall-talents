<p align="center">
  <img src="brand/logo.png" alt="Tall Talents logo" width="148">
</p>

<p align="center"><strong>Always Exceptional Design.</strong></p>
<p align="center"><strong>A global, file-based talent library for coding agents.</strong></p>
<p align="center">Capture real workflows. Reuse them everywhere. Keep the source of truth in plain files.</p>

<p align="center">
  <a href="https://github.com/scwlkr/tall-talents/stargazers">
    <img src="https://img.shields.io/github/stars/scwlkr/tall-talents?style=flat-square" alt="GitHub stars">
  </a>
  <a href="https://github.com/scwlkr/tall-talents/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/scwlkr/tall-talents/ci.yml?branch=main&style=flat-square&label=ci" alt="CI status">
  </a>
  <img src="https://img.shields.io/badge/version-0.6.0-black?style=flat-square" alt="Version 0.6.0">
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/scwlkr/tall-talents?style=flat-square" alt="MIT License">
  </a>
</p>

Tall Talents is the reference implementation and tooling for the live global library at `~/.tall-talents`.

If you already solved a painful workflow once, Tall Talents gives you a strict place to capture it, validate it, and reuse it later instead of rediscovering it under pressure.

> No apps.
>
> No databases.
>
> No abstractions.
>
> Just files.

## Why Tall Talents Exists

Most hard-won agent workflows disappear into chat history, terminal scrollback, or personal memory.

That is wasted leverage.

Tall Talents turns those one-off wins into reusable operational assets:

- a global live folder at `~/.tall-talents`
- one markdown file per real workflow
- strict rules and templates so the library stays usable
- small deterministic scripts so setup, validation, and indexing stay trustworthy
- a repo-live contributor mode so the public repository can act as the working source when needed

## What a Talent Actually Is

A talent is a reusable operational workflow written as a markdown file.

It is not a vibe, a persona, or a generic best-practices checklist.

It is something you actually struggled through, solved, and would want an agent to follow literally the next time the same class of problem appears.

If handing that file to an agent would produce a meaningfully better outcome than starting from scratch, it qualifies as a talent.

## Why This Repo Is Different

Tall Talents is deliberately narrow.

- `~/.tall-talents` is the live system, not a hidden database
- `bootstrap/` is the distributable snapshot of that live system
- `bootstrap/talents/*.md` are the real reviewable assets
- `rules/` and `templates/` define the contract
- `scripts/` keep install, validation, sync, and rebuild behavior deterministic
- `.github/workflows/ci.yml` verifies the bootstrap snapshot on macOS

This repo is small enough to inspect quickly and strict enough to trust under real use.

## What You Get

- Global live library bootstrap for `~/.tall-talents`
- Strict talent rules and reusable templates
- A validator that enforces format and structure
- An index rebuild script driven by active talent files
- A safe talent scaffolder
- A doctor script for environment checks
- Repo-live dev mode for contributors working directly against `bootstrap/`
- Real example talents instead of placeholder demo content

## Included Talents

Tall Talents already ships with working examples:

- [`fix-ad-hoc-codesign-fallback`](bootstrap/talents/fix-ad-hoc-codesign-fallback.md) - restore runnable macOS binaries by removing invalid signatures and applying deterministic ad-hoc signing
- [`gh-pages-site-subfolder-assets`](bootstrap/talents/gh-pages-site-subfolder-assets.md) - fix broken asset paths when GitHub Pages serves a site from a repo subpath
- [`github-ssh-repo-alias-setup`](bootstrap/talents/github-ssh-repo-alias-setup.md) - pin a repo to the right SSH alias and identity safely
- [`literal-wordpress-port-mode`](bootstrap/talents/literal-wordpress-port-mode.md) - reproduce legacy WordPress structure literally before cleanup or refactor
- [`repo-talent-acquisition-pass`](bootstrap/talents/repo-talent-acquisition-pass.md) - mine external repos for durable, reusable Tall Talents candidates

These examples matter because they prove the system is about operational reuse, not placeholder theory.

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
python3 scripts/dev-env.py install
bash scripts/doctor.sh
python3 scripts/validate-talents.py --root ~/.tall-talents
python3 scripts/rebuild-index.py --root ~/.tall-talents
```

`python3 scripts/dev-env.py install` is maintainer and contributor mode.
It points `~/.tall-talents` at this clone's `bootstrap/` directory and enables the committed pre-commit hook so talent edits happen directly in the repo while derived files stay synchronized.

If you already have unsynced local live-library changes that should be imported into this clone first:

```bash
python3 scripts/dev-env.py install --import-live
```

## How Agents Use It

Start any non-trivial task with:

```text
Use Tall Talents.
```

Then:

1. Read `~/.tall-talents/index.md`
2. Open only the relevant files in `~/.tall-talents/talents/`
3. Name the matching talents being used
4. Apply their procedures literally
5. If none fit, say so explicitly and do not force-fit one

This is the discipline:

- solve something real
- turn it into a reusable workflow
- stop paying the same thinking cost twice

## Create or Update a Talent

After solving something difficult:

1. Use `templates/create-talent-from-session.md`
2. Decide whether this should be a new talent, an update to an existing talent, or no talent at all
3. Write the markdown file in `~/.tall-talents/talents/`
4. In repo dev mode, those edits land directly in `bootstrap/`
5. Derived files refresh automatically at commit time via the repo hook
6. Outside repo dev mode, run manual bootstrap sync
7. Validate the library

## Commands

```bash
bash scripts/install.sh
bash scripts/doctor.sh
python3 scripts/validate-talents.py --root ~/.tall-talents
python3 scripts/rebuild-index.py --root ~/.tall-talents
python3 scripts/create-talent.py --title "My Talent" --summary "One-line summary"
python3 scripts/dev-env.py install
python3 scripts/dev-env.py install --import-live
python3 scripts/dev-env.py status
python3 scripts/dev-env.py uninstall
python3 scripts/sync-bootstrap.py --live-root ~/.tall-talents --bootstrap-root bootstrap
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

## How The Repo Proves Itself

This repository does not just describe the idea.
It includes the pieces required to keep the idea honest:

- `scripts/install.sh` initializes the live folder from a local clone or a raw GitHub install path
- `scripts/dev-env.py` switches `~/.tall-talents` into repo-live contributor mode and restores the prior root on uninstall
- `scripts/doctor.sh` verifies environment and folder layout
- `scripts/validate-talents.py` enforces the talent format contract
- `scripts/rebuild-index.py` regenerates `~/.tall-talents/index.md`
- `scripts/create-talent.py` scaffolds new talent files
- `scripts/sync-bootstrap.py` imports a live library into `bootstrap/` or regenerates derived files in place
- `.github/workflows/ci.yml` validates the shipped bootstrap snapshot on `push` and `pull_request`

## Versioning

This repo uses SemVer.

- `VERSION` is the repository version marker
- `CHANGELOG.md` tracks notable changes
- `1.0.0` is the stability target for the file format, tooling, and workflow

Current version: `0.6.0`

## GitHub Stars

If Tall Talents is useful, star the repo.
Stars are the simplest signal that the project is solving a real problem for real people.

[![Star History Chart](https://api.star-history.com/svg?repos=scwlkr/tall-talents&type=Date)](https://star-history.com/#scwlkr/tall-talents&Date)

## Support the Project

If Tall Talents saves you time:

- Star the repository
- Open issues or pull requests with real improvements
- Share the project with people building serious agent workflows

Buy me a coffee support link coming soon.

<!-- Replace the line above with the real Buy Me a Coffee URL when it exists publicly. -->

## A WLKR LABS Product

Tall Talents is a WLKR LABS product.

That means the project is intentionally opinionated about a few things:

- boring, inspectable systems beat clever hidden ones
- plain files beat opaque state when the asset is knowledge
- strict workflows beat loose prompts when repeatability matters
- small tools with sharp edges beat large systems with fuzzy boundaries

Built and maintained by [scwlkr](https://github.com/scwlkr).

## License

MIT.
