# Format Rule

Every active talent is a package directory in `~/.tall-talents/talents/<slug>/`.

Required package files:
- `TALENT.md`
- `CHANGELOG.md`

Optional package-local assets may include:
- `examples/`
- `scripts/`
- `templates/`

Required front matter keys:
- slug
- title
- summary
- tags
- triggers
- inputs
- outputs
- agent_behavior
- safety
- status
- version

Required headings:
- `# Goal`
- `# Procedure`
- `# Success Criteria`
- `# Common Failure Modes`
- `# Example Prompt`

Status values allowed: `active`, `draft`, `archived`.

The `slug` field must match the package directory name.

`CHANGELOG.md` must include at least one `##` entry. Automatic self-iteration entries must include session, change, evidence, expected effect, and oscillation check.

Single-file active talents such as `talents/<slug>.md` are invalid after the package migration.

The `safety` field must include any publishability guardrail that matters for the workflow. Talents may come from personal sessions, but committed active talents must not contain secrets, private identifiers, customer data, or owner-only context that should stay local.
