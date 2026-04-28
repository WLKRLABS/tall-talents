# Create/Update Tall Talent From Completed Session

You are converting completed real work into Tall Talents.

## Required process

1. Inspect `~/.tall-talents/index.md` first.
2. Decide one of:
   - create new talent
   - update existing talent
   - no talent (if work is not reusable)
3. Ground every instruction in what actually succeeded in this session.
4. Run a publishability pass before writing:
   - remove secrets, tokens, API keys, passwords, service-role values, private keys, and private URLs
   - replace personal paths, account names, emails, customer names, and private repo names with placeholders unless intentionally public and necessary
   - move private context that is useful only to the owner into `~/.tall-talents/private/`, not the committed talent
5. If creating/updating a talent, write exact markdown in `~/.tall-talents/talents/{slug}.md`.
6. Update exact index content in `~/.tall-talents/index.md` (active only, sorted by slug).
7. If Tall Talents repo dev mode is installed, the edit already lives in `bootstrap/`; rely on the repo hook to refresh derived files before commit.
8. Otherwise, if you are working inside the Tall Talents repo, run `python3 scripts/sync-bootstrap.py --live-root ~/.tall-talents --bootstrap-root bootstrap` so the checked-in bootstrap snapshot matches the live library.

## Output discipline

- No generic advice.
- No invented results.
- Preserve strict Tall Talents format (required front matter and required sections).
- Prefer updating an existing talent when overlap is substantial.
- Keep committed talents sanitized and reusable even when they came from personal work.
