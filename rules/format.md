# Format Rule

Every active talent is one markdown file in `~/.tall-talents/talents/`.

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

The `safety` field must include any publishability guardrail that matters for the workflow. Talents may come from personal sessions, but committed active talents must not contain secrets, private identifiers, customer data, or owner-only context that should stay local.
