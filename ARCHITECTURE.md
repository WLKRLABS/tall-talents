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

### 3) Tooling layer
- `install.sh`: initialize live folder
- `doctor.sh`: health checks
- `validate-talents.py`: contract enforcement
- `rebuild-index.py`: deterministic index generation
- `create-talent.py`: safe scaffolding

## Read path

1. Agent reads `~/.tall-talents/index.md`.
2. Agent selects relevant active talent slug(s).
3. Agent opens specific `~/.tall-talents/talents/{slug}.md` files.
4. Agent executes workflow as written.

## Write path

1. Agent derives workflow from completed real session.
2. Agent writes or updates one talent markdown file.
3. Agent validates file against format contract.
4. Agent updates index (manual edit or rebuild script).

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
