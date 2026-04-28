# Tall Talents Architecture

## Core model

Tall Talents uses the filesystem as the source of truth.

- Live root: `~/.tall-talents`
- Active talents: `~/.tall-talents/talents/*.md`
- Index: `~/.tall-talents/index.md`

No hidden cache, no database, no background process.

## Layers

### 1) Spec layer
- Rules in `rules/`
- Talent template in `templates/talent-template.md`
- Required front matter + required sections

### 2) Content layer
- Talent markdown files in `talents/`
- Index markdown derived from active talents
- Incoming/archive directories for lifecycle handling
- Optional local-only private notes in `private/`

### 3) Distribution snapshot layer
- Repo snapshot in `bootstrap/`
- In repo dev mode, `bootstrap/` is the live library via a symlink from `~/.tall-talents`
- `bootstrap/talents/` holds the editable talent files that contributors review and commit
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
3. Agent opens specific `~/.tall-talents/talents/{slug}.md` files.
4. Agent executes workflow as written.

## Composition model

Tall Talents is allowed to use one or more talents for a task.

- Use one talent when one workflow covers the real task.
- Use multiple talents when the work has distinct stages or disciplines.
- Choose a primary talent for overall control and supporting talents for specialist steps.
- State the execution order before applying them.
- Do not force extra talents into a task that one talent already covers cleanly.

There is no hidden orchestration engine. Composition is an agent discipline over plain files.

## Write path

1. Agent derives workflow from completed real session.
2. Agent writes or updates one talent markdown file.
3. Agent validates file against format contract.
4. Agent updates the live index (manual edit or rebuild script).
5. In repo dev mode, edits land directly in `bootstrap/` and the pre-commit hook refreshes derived files.
6. Outside repo dev mode, run manual bootstrap sync when the repo snapshot must catch up to a separate live root.

## Privacy model

Talents may be personal in origin, but committed active talents must be publishable.

- `~/.tall-talents/talents/` is the active library and can be mirrored into the public repo.
- `~/.tall-talents/private/` is for owner-only context and is not shipped in `bootstrap/manifest.txt`.
- Public talents should use placeholders for private names, paths, accounts, URLs, customers, and providers.
- Secrets, tokens, API keys, service-role values, reset links, auth headers, and private logs do not belong in talents.
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
