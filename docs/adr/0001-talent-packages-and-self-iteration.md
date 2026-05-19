# ADR-0001: Talent Packages And Self-Iteration

## Status

Accepted

## Context

Tall Talents began as one markdown file per reusable workflow under `talents/*.md`. That kept the system simple, but the library is now expected to self-improve after real work and to support package-local assets such as examples, scripts, templates, helper code, and per-talent history.

The old shape made per-talent changelogs awkward. A single global log would keep the file model unchanged, but it would separate history from the talent it explains and make oscillation checks less local. Supporting both single-file talents and package talents would double the read, validation, sync, install, and documentation paths.

## Options Considered

- Keep single-file talents and add sidecar changelog files.
- Support both single-file talents and package directories during migration.
- Perform a one-time migration to package-only active talents.

## Decision

Tall Talents will use package-only active talents.

Each active talent lives at:

```text
talents/<slug>/
  TALENT.md
  CHANGELOG.md
```

Optional package-local assets may live beside those files, including `examples/`, `scripts/`, and `templates/`.

The agent read path stays compact:

1. Read `index.md`.
2. Select the smallest applicable package set.
3. Load only each selected package's `TALENT.md` by default.
4. Load `CHANGELOG.md` during self-iteration or before changing, archiving, or splitting a package.
5. Load package assets only when `TALENT.md` references them or the task needs them.

Self-iteration runs after every non-trivial conversation, writes a tiny report card, and edits talents only when concrete conversation evidence exists. Allowed automatic actions are `refine`, `create`, `archive`, and `split`; automatic merge is intentionally out of scope.

## Consequences

- Validators, index rebuild, sync, install, dev import, privacy scan, templates, docs, and pre-commit behavior must use package directories.
- Single-file active talents become invalid after the migration.
- Every package must include `CHANGELOG.md`, seeded with a migration entry for existing talents.
- `index.md` remains an activation routing surface and must not become a changelog summary.
- Archived packages move to `archive/<slug>/` instead of remaining active-path candidates under `talents/`.
- The system remains plain-file and git-diff friendly, but automatic edits now require local package history and self-iteration reports to make loops visible.
