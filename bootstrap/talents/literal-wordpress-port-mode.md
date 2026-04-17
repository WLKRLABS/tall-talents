---
slug: literal-wordpress-port-mode
title: Literal WordPress port mode for static migration parity
summary: Reproduce legacy WordPress page structure literally during migration before any cleanup/refactor pass.
tags:
  - wordpress
  - migration
  - static-site
triggers:
  - "Migration accuracy is blocked by early redesign or template abstraction."
inputs:
  - Exported WordPress content snapshot.
  - Target folder containing generated static pages/templates.
outputs:
  - File-by-file parity pass preserving URL/content fidelity.
  - Clear log of deferred refactors after parity is reached.
agent_behavior:
  - Prefer literal translation over optimization in first pass.
  - Defer componentization until parity checks pass.
safety:
  - Do not rewrite URL structure during parity phase.
  - Keep a migration log for every intentional deviation.
status: active
version: 1.0.0
---

# Goal

Achieve a high-confidence first migration pass that mirrors legacy WordPress behavior and layout before introducing improvements.

# Procedure

1. Freeze scope: declare "literal port mode" for current pass.
2. Mirror permalink and folder layout as-is in target output.
3. Port template sections directly (header/footer/content blocks) without abstraction.
4. Preserve legacy class names and anchor IDs where they impact behavior.
5. Run URL and content spot checks across representative pages.
6. Record any deviations in a migration log with reason and follow-up task.
7. Only after parity acceptance, open separate refactor phase.

# Success Criteria

- Representative legacy URLs resolve to equivalent static pages.
- Content and major structure match legacy output closely.
- Deferred refactor list exists and is explicitly separated from parity work.

# Common Failure Modes

- Refactoring component structure too early and breaking fidelity.
- Changing slugs/permalinks during first-pass migration.
- Mixing parity fixes with design improvements in the same change set.

# Example Prompt

"Use `literal-wordpress-port-mode` for this migration batch, produce parity-first files, and list deviations in a separate log section."
