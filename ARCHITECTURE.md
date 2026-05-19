# Tall Talents Architecture

## Core model

Tall Talents uses the filesystem as the source of truth.

- Live root: `~/.tall-talents`
- Active talents: `~/.tall-talents/talents/<slug>/TALENT.md`
- Per-talent history: `~/.tall-talents/talents/<slug>/CHANGELOG.md`
- Index: `~/.tall-talents/index.md`

No hidden cache, no database, no background process.

## Layers

### 1) Spec layer
- Rules in `rules/`
- Talent template in `templates/talent-template.md`
- Required front matter + required sections

### 2) Content layer
- Talent package directories in `talents/`
- Index markdown derived from active talents
- Incoming/archive directories for lifecycle handling
- Public-safe self-iteration reports in `reports/self-iteration/`
- Optional local-only private notes in `private/`

### 3) Distribution snapshot layer
- Repo snapshot in `bootstrap/`
- In repo dev mode, `bootstrap/` is the live library via a symlink from `~/.tall-talents`
- `bootstrap/talents/` holds the editable talent packages that contributors review and commit
- `bootstrap/index.md` and `bootstrap/manifest.txt` include active talents only
- `scripts/sync-bootstrap.py` regenerates the snapshot from the live library
- `.githooks/pre-commit` regenerates derived files before commit
- `scripts/dev-env.py` installs repo-live dev mode for contributors and restores the previous live root on uninstall

### 4) Tooling layer
- `install.sh`: initialize live folder
- `dev-env.py`: install/uninstall/status for repo-live dev mode
- `doctor.sh`: health checks
- `validate-talents.py`: contract enforcement
- `rebuild-index.py`: deterministic index generation
- `create-talent.py`: safe scaffolding
- `sync-bootstrap.py`: repo snapshot import + derived-file generation

## Read path

1. Agent reads `~/.tall-talents/index.md`.
2. Agent selects relevant active talent slug(s).
3. Agent opens specific `~/.tall-talents/talents/{slug}/TALENT.md` files.
4. Agent executes workflow as written.

Package folders are not automatic context dumps. The default activation surface is only `TALENT.md`.

Load package-local assets only when:

- `TALENT.md` explicitly references them
- the current task needs them
- self-iteration is inspecting history or changing the package

Load `CHANGELOG.md` during self-iteration or before modifying, archiving, or splitting the package.

## Composition model

Tall Talents is allowed to use one or more talents for a task.

- Use one talent when one workflow covers the real task.
- Use multiple talents when the work has distinct stages or disciplines.
- When the user explicitly invokes a non-Tall-Talents Codex skill, plugin, or slash-style workflow, that invoked workflow controls by default.
- Do not add Tall Talents under an external controlling skill only because a nearby talent matches the same domain.
- Add Tall Talents under an external controlling skill only when the user also asks for Tall Talents, the invoked skill requests it, the task has a separate uncovered stage, or the task is about Tall Talents itself.
- Choose a primary talent for overall control and supporting talents for specialist steps.
- State the execution order before applying them.
- Do not force extra talents into a task that one talent already covers cleanly.

There is no hidden orchestration engine. Composition is an agent discipline over plain files.

## Write path

1. Agent runs a self-iteration pass after every non-trivial conversation.
2. Agent writes a raw local report under `private/self-iteration/`.
3. If there is no concrete evidence, the pass may write a tiny sanitized no-change report under `reports/self-iteration/`.
4. If concrete evidence exists, agent reads the affected package's `TALENT.md` and `CHANGELOG.md`.
5. Agent performs the oscillation check.
6. Agent applies one of: `refine`, `create`, `archive`, or `split`.
7. Agent appends the package changelog entry with session, change, evidence, expected effect, and oscillation check.
8. Agent validates package shape, rebuilds the index, runs the privacy scan, and checks diff hygiene.
9. In repo dev mode, edits land directly in `bootstrap/` and the pre-commit hook refreshes derived files.
10. Outside repo dev mode, run manual bootstrap sync when the repo snapshot must catch up to a separate live root.

## Privacy model

Talents may be personal in origin, but committed active talents must be publishable.

- `~/.tall-talents/talents/` is the active package library and can be mirrored into the public repo.
- `~/.tall-talents/reports/self-iteration/` is for sanitized report cards that are safe to commit.
- `~/.tall-talents/private/` is for owner-only context, including raw self-iteration reports, and is not shipped in `bootstrap/manifest.txt`.
- Public talents should use placeholders for private names, paths, accounts, URLs, customers, and providers.
- Secrets, tokens, API keys, service-role values, reset links, auth headers, private logs, and raw private reports do not belong in committed talents or sanitized reports.
- `scripts/scan-talent-privacy.py` blocks high-confidence secrets and warns about personal identifiers before commit.

## Constraints

- macOS-first shell tooling
- plain files only
- git-friendly markdown content
- deterministic script behavior
- no overwrite of existing user talents by default

## Hard limitations

- No semantic/vector search built in.
- No automatic merge conflict resolution for concurrent edits.
- No schema migration engine beyond file validation + manual edits.
- No cloud sync; users can manage sync separately (git, rsync, etc.).
- Repo dev mode repoints `~/.tall-talents` for this clone; contributors who do not want that should stay in manual sync mode.
