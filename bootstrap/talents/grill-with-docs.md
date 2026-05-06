---
slug: grill-with-docs
title: Grill With Docs
summary: Stress-test a plan against existing domain language, code reality, and ADRs while updating CONTEXT.md and decision records as decisions crystallize.
tags:
  - planning
  - domain-modeling
  - documentation
triggers:
  - User wants to stress-test a plan against a project's existing language or documented decisions.
  - A design discussion is using fuzzy, overloaded, or conflicting domain terms.
  - CONTEXT.md or ADRs should be updated while a plan is being clarified.
inputs:
  - Current plan, design, or decision under discussion.
  - Existing CONTEXT.md, CONTEXT-MAP.md, docs/adr, and relevant source code.
  - User feedback to one question at a time.
outputs:
  - Resolved decision tree with precise terminology.
  - Updated CONTEXT.md entries and ADRs only where justified.
  - Explicit unresolved questions and code/documentation contradictions.
agent_behavior:
  - Read existing domain docs and ADRs before challenging terminology.
  - Ask one question at a time and provide a recommended answer with each question.
  - Explore the codebase instead of asking when the answer is discoverable.
  - Update domain docs inline as terms resolve instead of batching all edits at the end.
safety:
  - Do not put implementation details or generic programming concepts in CONTEXT.md.
  - Do not create ADRs unless the decision is hard to reverse, surprising without context, and the result of a real trade-off.
  - Do not let polished language hide unresolved terminology conflicts.
status: active
version: 1.0.0
---

# Goal

Turn a planning or design conversation into precise shared understanding by challenging it against the project's documented domain model, real code behavior, and recorded architectural decisions.

# Procedure

## 1. Load The Domain And Decision Context

Before asking design questions, inspect:

- `CONTEXT-MAP.md` if present
- root or context-local `CONTEXT.md`
- root or context-local `docs/adr/`
- relevant source files when the plan describes current behavior

If `CONTEXT-MAP.md` exists, use it to choose the right context. If no context file exists, create one only after the first domain term is actually resolved.

## 2. Challenge Terminology Immediately

When the user uses a term that conflicts with existing language, call that out before moving on.

Use this shape:

```text
Your glossary defines [term] as [definition], but this plan seems to use it as [different meaning]. Which meaning should control?
Recommended answer: [specific recommendation].
```

When a term is vague or overloaded, propose one canonical term and name the avoided aliases.

## 3. Ask One Question At A Time

Walk the design tree one branch at a time:

- ask the next highest-leverage question
- explain why it matters
- provide your recommended answer
- wait for feedback before continuing

If the answer can be found in code, inspect the code instead of asking the user.

## 4. Stress-Test With Concrete Scenarios

Use specific scenarios to expose hidden ambiguity:

- edge cases
- partial success or failure
- lifecycle transitions
- ownership handoffs
- conflicts between two domain concepts

Prefer scenarios that force the plan to distinguish adjacent terms.

## 5. Cross-Reference Code Reality

When the user states how something works, check the source if practical.

Surface contradictions directly:

```text
The plan says partial cancellation is possible, but the current code cancels whole Orders. Which is the product truth?
Recommended answer: [specific recommendation].
```

## 6. Update CONTEXT.md Inline

When a term resolves, update the applicable `CONTEXT.md` immediately.

Use this structure:

- `# [Context Name]`
- short context description
- `## Language`
- tight one-sentence definitions with avoided aliases
- `## Relationships`
- `## Example dialogue`
- `## Flagged ambiguities`

Rules:

- define what the term is, not what it does
- include only domain-specific terms
- express obvious relationships and cardinality
- record ambiguity resolutions explicitly

## 7. Offer ADRs Sparingly

Create or offer an ADR only when all three conditions are true:

- hard to reverse
- surprising without context
- result of a real trade-off

ADRs live in `docs/adr/` and use sequential filenames such as `0003-short-slug.md`. A minimal ADR can be one paragraph explaining the context, decision, and why.

## 8. End With A Decision Ledger

Close the session with:

- terms resolved
- docs updated
- decisions recorded
- contradictions found
- open questions still blocking the plan

# Success Criteria

- The plan uses domain terms consistently with `CONTEXT.md`.
- Code/documentation contradictions are surfaced instead of smoothed over.
- Each question resolves a real branch in the decision tree.
- CONTEXT.md changes are domain-specific, tight, and made as terms resolve.
- ADRs are created only for durable, trade-off-bearing decisions.

# Common Failure Modes

- Asking a long questionnaire instead of one decision at a time.
- Treating glossary cleanup as copyediting rather than domain clarification.
- Adding implementation details, utilities, or generic programming terms to CONTEXT.md.
- Creating ADRs for every decision instead of only durable and surprising trade-offs.
- Accepting the user's explanation when the code cheaply proves or disproves it.

# Example Prompt

"Use `grill-with-docs` on this plan. Challenge the terminology against CONTEXT.md and ADRs, inspect code when it can answer a question, ask one question at a time with your recommended answer, and update CONTEXT.md or ADRs inline as decisions crystallize."
