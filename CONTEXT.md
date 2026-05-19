# Tall Talents Context

Tall Talents is a file-backed workflow library for coding agents.

## Language

- Self-iteration means the system can automatically refine, add, archive, or otherwise modify active talent files based on evidence from completed agent sessions.
- Direct talent edit means a self-iteration pass can write to active talent packages without human approval.
- Talent change log means a simple per-talent append-only record of automatic talent changes, including enough before/after rationale to detect repeated add/delete loops.
- A talent is an operational workflow file that should make a future agent perform materially better on the same class of work.
- A talent package is a directory for one reusable workflow, with a primary talent document plus local supporting files such as a changelog, examples, scripts, templates, or helper code.
- `TALENT.md` is the primary instruction document inside a talent package.
- `CHANGELOG.md` is a required append-only history file inside every talent package.
- Talent effectiveness is the observed usefulness of a talent in a real session, judged against evidence such as avoided mistakes, reduced ambiguity, better verification, or unnecessary context cost.
- Oscillation check is the required changelog explanation that a self-iteration change is not undoing or re-adding a recent change without new evidence.
- Self-iteration pass is the post-conversation review that evaluates whether talent activation, non-activation, or talent content should change.
- Talent self-iteration report is a tiny per-conversation audit file that records the self-iteration pass result, including no-change decisions.
- Concrete evidence is session-observed proof that a talent caused measurable waste, prevented or caught a real failure, missed a needed repeatable rule, or should have activated but did not.
- Refine means editing a talent package to narrow triggers, add a missing rule, remove bloat, or clarify a proven failure mode.
- Create means adding a new talent package for a clearly reusable workflow that was missing.
- Archive means removing a talent from active use after repeated evidence shows it activates incorrectly or adds net bloat.
- Split means creating a narrower talent when one broad talent keeps doing unrelated jobs.
- Negative report means a self-iteration report with evidence that a talent activated incorrectly, caused net bloat, or made the session worse.
- Package-only active format means active talents must live as package directories with `TALENT.md`, not as single markdown files.
- Package read path means the agent reads `index.md`, selects the smallest applicable package set, then loads only each selected package's `TALENT.md` by default.
- Self-iteration implementation surface is split between agent instructions and small deterministic scripts.
- Package validation contract is the deterministic rule set that keeps talent packages structurally valid after automatic edits.
- Raw self-iteration report means the local-only report card that may include private session context needed for honest evaluation.
- Sanitized self-iteration report means the public-safe report card that can be committed without exposing private paths, repo names, customer context, secrets, or sensitive debugging details.
- Self-iteration run sequence means the required end-of-conversation order for reporting, evidence review, talent edits, changelog updates, and verification.
- Package index entry means the compact routing entry in `index.md` that summarizes an active talent package and points to its `TALENT.md`.
- Archived talent package means a retired package stored under `archive/<slug>/` with its instructions, changelog, and supporting assets preserved.
- Self-created talent package means a new active package created by self-iteration from concrete session evidence.

## Relationships

- Self-iteration acts on talents.
- Talent effectiveness evidence should drive self-iteration.
- Automatic talent changes still belong to the file-backed Tall Talents library and must remain inspectable through normal diffs.
- Direct talent edits require a per-talent change log.
- Active talents should migrate from single markdown files into talent packages when package-local history and supporting assets matter.
- Every talent package has a `CHANGELOG.md`; newly migrated talents seed it with a migration entry.
- Automatic changelog entries include session, change, evidence, expected effect, and oscillation check.
- A self-iteration pass runs after every non-trivial conversation.
- A self-iteration pass edits talents only when there is concrete evidence from the conversation.
- Every self-iteration pass writes a tiny report under `reports/self-iteration/`, even when no talent changes are made.
- Automatic talent edits require concrete evidence.
- Automatic talent edits are not allowed for vague usefulness, nicer wording, or model confidence.
- Automatic self-iteration may refine, create, archive, or split talents.
- Automatic self-iteration may not merge talents at first.
- Automatic archive requires three evidence-backed negative reports across at least two sessions, unless the talent has a serious safety or privacy problem.
- Serious safety or privacy problems can trigger immediate archive.
- One bad use should trigger refinement first, not archive.
- The migration from single-file talents to talent packages is a one-time full migration.
- After the migration, single-file active talents are invalid.
- Package `CHANGELOG.md` is loaded during self-iteration or before modifying, archiving, or splitting that package.
- Package assets such as `examples/`, `scripts/`, and `templates/` are loaded only when `TALENT.md` explicitly references them or the current task needs them.
- Agent instructions require a self-iteration pass after every non-trivial conversation.
- Scripts handle file mechanics such as report paths, package-shape validation, recent changelog checks, and optional changelog appends from explicit arguments.
- The model makes the judgment call using conversation evidence; scripts do not decide usefulness.
- Package validation requires `talents/<slug>/TALENT.md`, `talents/<slug>/CHANGELOG.md`, existing `TALENT.md` front matter fields, folder-name slug match, allowed status, required `TALENT.md` headings, at least one `CHANGELOG.md` entry, and no active single-file `talents/*.md`.
- Package validation does not validate helper file contents until a repeated failure proves stricter rules are needed.
- Raw self-iteration reports live under `private/self-iteration/` and are local-only.
- Sanitized self-iteration reports live under `reports/self-iteration/` and may be committed when safe.
- Self-iteration changelog entries cite the sanitized report when one exists; otherwise they cite the private report generically without sensitive details.
- A self-iteration run writes a raw report first, checks for concrete evidence, writes a sanitized no-change report when safe, reads affected `TALENT.md` and `CHANGELOG.md` when evidence exists, runs the oscillation check, applies refine/create/archive/split, appends the package changelog, runs validation/index/privacy/diff checks, and updates the sanitized report with exact changes made.
- `index.md` remains a compact activation-routing list and points to package entrypoints such as `talents/<slug>/TALENT.md`.
- `index.md` does not include changelog summaries.
- Archived packages move to `archive/<slug>/`.
- `talents/` contains active and draft working packages, not archived packages.
- Archive packages preserve `TALENT.md`, `CHANGELOG.md`, package assets, and the archive changelog entry that cites the justifying self-iteration reports.
- Self-iteration creates finished active packages directly under `talents/<slug>/` when evidence is strong enough.
- `incoming/` is reserved for externally imported or unfinished talent candidates.

## Example Dialogue

- "The system should self-iterate." means automatic talent changes are in scope, not only human-reviewed suggestions.
- "Keep it simple." means use direct file edits plus a lightweight change record, not a heavy approval pipeline or orchestration engine.
- "Each talent folder" means each active talent should own its primary instructions, changelog, and optional supporting assets inside one package directory.
- "Migrated from single-file talent format." is the seed changelog entry for existing talents moved into package form.
- "Keep it small but hard to fake" means automatic changelog entries should be concise but must include concrete evidence and an oscillation check.
- "Only edit talents when there is concrete evidence" means the default result of a self-iteration pass may be no change.
- A talent self-iteration report includes conversation type, talents activated, talents that should not have activated, talents that should have activated, evidence found, changes made, and no-change rationale.
- "Do not edit for vibes" means self-iteration cannot change a talent only because the change might be useful, reads better, or made the model feel more confident.
- "No automatic merge at first" means self-iteration should preserve specificity until merge safety is proven later.
- Archive changelog entries must cite the self-iteration report files that justify the archive.
- "One-time full migration" means the repo does not support both single-file talents and package talents as parallel active formats.
- "`TALENT.md` stays the activation surface" means package folders do not permit automatic context dumping of all package files.
- "Dumb script" means deterministic file operations and validation only, not an orchestration engine or hidden decision maker.
- "Keep assets flexible" means examples, scripts, templates, and helper code are allowed inside packages without a stricter schema at first.
- "Commit only sanitized reports" means the raw report is not automatically public just because the talent change is public.
- "Run sequence" means the system must record evidence before mutating talent files and verify after mutation.
- "The index is for activation routing" means historical review belongs in package changelogs and self-iteration reports, not in `index.md`.
- "Move archived packages" means archived talents should not remain in `talents/` with only `status: archived`.
- "No hidden human review queue" means self-iteration creates active packages or makes no change.

## Flagged Ambiguities

- None. The package migration is implemented as the active repo contract.
