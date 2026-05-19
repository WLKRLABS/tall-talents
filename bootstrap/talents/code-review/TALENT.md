---
slug: code-review
title: Code Review
summary: Review completed work against exact requirements and real code, then return one-pass findings ordered by severity and evidence.
tags:
  - review
  - quality
  - correctness
triggers:
  - A major task, plan step, or feature slice is complete and needs independent scrutiny.
  - A risky refactor, bug fix, or pre-merge diff needs severity-ranked findings.
  - Another reviewer needs a precise review request with requirement context and diff boundaries.
inputs:
  - Requirement source such as a spec, plan, ticket, or exact task text.
  - Review target such as a diff range, branch comparison, or exact files.
  - Tests run, known constraints, and any intentional deviations from the original plan.
outputs:
  - Findings ordered by severity with file references, reasoning, and clear next actions.
  - Explicit statement when no findings are discovered, plus residual risks or test gaps.
agent_behavior:
  - Re-read the requirement source before reviewing implementation.
  - Read the changed code directly and inspect adjacent surfaces when needed to judge correctness.
  - Deliver complete feedback in one pass instead of drip-feeding comments across rounds.
safety:
  - Do not review from summaries alone when the code or diff can be read directly.
  - Do not bury blocking issues under style commentary or low-value nits.
status: active
version: 1.0.0
---

# Goal

Produce a review that improves correctness and decision quality, not just code aesthetics. A real review checks the implementation against the exact requirement source, identifies the highest-risk problems first, and gives feedback another engineer can act on immediately.

## Use It When

- A logical implementation chunk is complete.
- Work is about to be merged, handed off, or released.
- A risky change needs an independent pass on security, correctness, or test coverage.
- A plan step was completed and must be checked against that plan before continuing.

## Do Not Use It As A Substitute For

- `review-feedback-triage`, which governs how to respond to received comments.
- `verification-gate`, which proves status claims with fresh evidence.
- A design discussion that should happen before coding.

# Procedure

## 1. Lock The Requirement Source First

Review against the real source of truth, not a paraphrase.

Priority order:

1. approved spec or plan
2. exact user task text
3. acceptance criteria or ticket text
4. explicit design notes for the change

Pull out the items that materially constrain the review:

- required behavior
- prohibited scope
- interfaces and compatibility promises
- performance, security, or compliance expectations
- tests or verification the work was expected to include

If the requirement source is unclear, say so. A review without a real target can only be partial.

## 2. Define The Review Surface

Set the review boundary before reading:

- base and head commit or branch
- exact files changed
- related tests or config affected by the change
- any intentional deviations the implementer already called out

For a dispatched or asynchronous review request, include at minimum:

- what was implemented
- plan or requirement source
- base SHA
- head SHA
- short description of the change

That keeps the reviewer focused on the work product rather than chat history.

## 3. Read The Code, Not Just The Summary

Inspect the changed code directly.

Also inspect adjacent surfaces when needed to judge whether the change is safe:

- touched interfaces and callers
- tests that should prove the behavior
- related config or migration files
- surrounding control flow or data flow

Do not invent context that was not inspected. If the review is intentionally narrow, say so.

## 4. Review Through The Five Primary Lenses

### Correctness And Plan Alignment

- Does the code actually do what the requirement source asked for?
- Are there missing branches, edge cases, or regressions?
- Did the implementation drift from the approved plan, and if so, was that justified or risky?

### Security And Safety

- Are inputs validated at the right boundaries?
- Did the change create auth, injection, exposure, or data-loss risk?
- Are secrets, permissions, and failure paths handled safely?

### Maintainability

- Will the next engineer understand the change in context?
- Are naming, boundaries, and control flow clear enough to sustain future edits?
- Did the change quietly add scope, coupling, or untracked complexity?

### Performance And Scale

- Are there obvious inefficient queries, loops, allocations, or chatty calls?
- Does the change increase work in a hot path without justification?
- Are there opportunities where a blocker should be raised now rather than after merge?

### Testing And Verification

- Do tests cover the behavior that actually changed?
- Did the work prove the highest-risk paths or only the easy ones?
- Is there a missing regression test, smoke test, or manual verification note?

## 5. Classify Findings By Decision Weight

Use three levels and keep the threshold disciplined.

### Critical

Must fix before merge or release.

Typical cases:

- broken required behavior
- security vulnerability
- data corruption or loss risk
- missing critical failure handling
- change clearly contradicts the approved requirement

### Important

Should fix before continuing if it affects confidence, maintainability, or non-trivial risk.

Typical cases:

- missing tests for high-value behavior
- confusing or brittle logic
- performance risk likely to matter soon
- requirement coverage gaps that are real but not catastrophic

### Suggestion

Useful improvement but not a blocker to the current scope.

Use sparingly. If the review has real problems, lead with those and keep suggestions secondary.

## 6. Write Findings In A Reusable Format

Each finding should answer:

- where is the issue
- what is wrong
- why it matters
- what change or verification would resolve it

Default format:

```markdown
[Severity] [Short label]
File: [path]
Why it matters: [impact on correctness, safety, maintenance, or performance]
Evidence: [what in the code or diff led to the finding]
Recommended action: [specific fix or follow-up verification]
```

If intent is unclear, ask a focused question instead of asserting a false positive.

## 7. Return Complete Feedback In One Pass

Order the review output like this:

1. findings by severity
2. open questions or assumptions
3. brief summary of strengths or overall shape
4. residual test gaps if no findings were discovered

Do not drip-feed comments across multiple rounds unless new evidence appears.

## 8. State The No-Findings Case Honestly

When no findings are discovered, say that explicitly.

Still include:

- what surfaces were reviewed
- what was not reviewed
- any residual risk or missing verification that keeps the review bounded

"No findings" does not mean "proven perfect."

## Review Request Template

Use this when handing a change to a reviewer:

```markdown
## Review Request
- What was implemented: [exact change]
- Requirement source: [path or task text]
- Base SHA: [sha]
- Head SHA: [sha]
- Files of interest: [paths]
- Tests run: [commands and results]
- Known concerns: [optional]
```

## Output Shape

Default review output:

```markdown
## Findings
- [Critical] ...
- [Important] ...
- [Suggestion] ...

## Open Questions
- ...

## Summary
- ...
```

## Integration Notes

- Pair with `review-feedback-triage` after comments land.
- Pair with `verification-gate` before any "safe to merge" or "done" claim.
- Pair with `implementation-planning` when review findings reveal plan drift rather than isolated bugs.

# Success Criteria

- The review is grounded in the exact requirement source and the real changed code.
- Findings are ordered by severity and connected to concrete evidence.
- Blocking problems are easy to distinguish from non-blocking suggestions.
- The output is complete enough to drive the next implementation or decision round.
- If no findings are discovered, the remaining review limits are stated clearly.

# Common Failure Modes

- Reviewing against memory instead of the actual requirement source.
- Reading the summary but not the changed code.
- Leading with nits while correctness or security issues go unstated.
- Calling something a blocker without explaining why it matters.
- Drip-feeding comments across rounds instead of giving one complete pass.
- Equating "no findings" with full verification or release readiness.

# Example Prompt

"Use `code-review` on this completed implementation. Review the diff against the exact plan, read the changed files directly, and return one-pass findings ordered by severity with concrete file references."
