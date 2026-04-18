---
slug: documentation-pass
title: Documentation Pass
summary: Create or repair documentation through source-grounded auditing, audience-first structure, tested examples, and explicit maintenance rules.
tags:
  - documentation
  - writing
  - verification
triggers:
  - A README, guide, reference, tutorial, or docs set needs to be written, rewritten, or audited for accuracy and usability.
  - A feature or release is incomplete until its documentation is shipped and verified.
inputs:
  - The real product or code surface being documented.
  - Existing docs, support signals, issue history, and audience context when available.
outputs:
  - Documentation that is accurate, navigable, and matched to the reader's entry point.
  - A validation record covering example execution, review passes, and any known documentation gaps or follow-up work.
agent_behavior:
  - Verify the product or source material before writing claims.
  - Decide the audience and document type before drafting prose.
  - Treat broken examples, stale guidance, and missing prerequisites as product defects.
safety:
  - Do not invent capabilities or behaviors not confirmed by the source material.
  - Do not ship code examples or commands that were not tested or otherwise validated.
status: active
version: 1.0.0
---

# Goal

Produce documentation that helps the intended reader succeed quickly, reflects the current product truth, and stays maintainable as the system evolves.

## Use It When

- A README or core guide is weak, stale, or untrustworthy.
- A new feature needs documentation before it is actually complete.
- A docs set has grown confusing and needs structure, not just sentence cleanup.

## Do Not Use It When

- The task is only a tiny wording fix with no structural or accuracy impact.
- The source material is still too incomplete or unstable to document responsibly.
- The real need is product definition or implementation planning rather than user-facing explanation.

## Core Principle

Documentation is not decoration. If it causes a reader to fail, misunderstand scope, or lose trust, it is a product bug.

# Procedure

## 1. Audit The Real Source Of Truth First

Before drafting anything, inspect the actual system:

- code, configs, CLI help, routes, APIs, or UI behavior
- existing docs and where they diverge from reality
- issue tracker or support signals that reveal confusion points
- release or version boundaries that affect accuracy

Never start from prose alone if the product can be inspected directly.

## 2. Define The Reader And The Entry Point

Answer these before writing:

- who is this for?
- what do they already know?
- what are they trying to do right now?
- what is the fastest path to success for them?

Then classify the document:

- tutorial: learn by building
- how-to: complete a task
- reference: look something up
- explanation: understand a concept or rationale

Do not mix all four into one shapeless page.

## 3. Decide The Minimum Honest Scope

State what the doc will and will not cover.

Examples:

- quick start only, not operations
- API reference only, not conceptual onboarding
- migration guide for v2, not a full product tour

This prevents documentation bloat and stops readers from expecting answers the page was never designed to provide.

## 4. Outline Before Writing Prose

Build the structure first:

- title and one-line purpose
- prerequisites
- fastest path to success
- deeper details in the right order
- troubleshooting or edge cases if needed
- links to adjacent docs

Good structure does more work than elegant sentences.

## 5. Write From Verified Facts, Not Plausible Assumptions

Every claim should come from one of these:

- inspected source code or runtime behavior
- validated command output
- approved product or API contract
- verified release notes or changelog

If a fact cannot be verified, mark it clearly as unknown, pending, or not yet implemented. Never smooth uncertainty into false confidence.

## 6. Make Examples Runnable Or Explicitly Illustrative

For commands, snippets, and walkthroughs:

- test them in a clean or realistic environment when possible
- keep them minimal
- show the expected outcome when useful
- explain prerequisite setup instead of assuming it

If an example is illustrative only, say so. Do not leave readers to discover that after wasting time.

## 7. Apply Documentation Quality Gates

Before review, check:

- the 5-second test: what is this, why does it matter, how do I start?
- one concept per section
- second person, present tense, active voice where appropriate
- no unexplained acronyms or hidden prerequisites
- no stale version or platform claims
- no dead links or broken commands

Documentation should reduce ambiguity, not redistribute it.

## 8. Run A Multi-Angle Review

Review in at least these passes:

- technical accuracy review by someone who knows the system
- clarity review by someone closer to the intended reader
- example or command verification

If possible, watch an unfamiliar reader try the doc. The point is not whether the writing sounds polished. The point is whether the reader succeeds.

## 9. Ship Docs With The Change, Not Someday After

When documentation is tied to feature or API work:

- update docs in the same change window
- include migration notes for breaking changes
- include rollback or compatibility notes when relevant
- connect docs updates to the shipped version

Code without docs is incomplete. Breaking changes without migration guidance are hostile.

## 10. Leave A Maintenance Trail

Every documentation pass should end with maintainability signals:

- what page or file changed
- what source of truth it was checked against
- what examples were verified
- what sections remain intentionally incomplete
- what review cadence is needed for time-sensitive content

Time-sensitive docs such as security, configuration, pricing, or deprecation notices need explicit review ownership.

## Documentation Review Template

```markdown
## Documentation Pass Review

- Audience:
- Document type:
- Source of truth checked:
- Examples verified:
- Known gaps:
- Follow-up maintenance needed:
```

## Strong vs Weak Execution

Strong:

- audits the real product first
- writes for a specific reader and use case
- separates tutorial, how-to, reference, and explanation cleanly
- tests commands and snippets
- marks unknowns honestly

Weak:

- rewrites prose without checking the product
- tries to answer every question on one page
- copies unstated assumptions from engineers into the doc
- ships broken examples
- treats docs review as a spelling pass

# Success Criteria

- The documentation is accurate against the current source of truth.
- The intended reader can identify the right entry point and succeed without hidden context.
- Commands and examples are validated or clearly labeled as illustrative.
- Review covered both technical correctness and reader clarity.
- Maintenance expectations and known gaps are explicit.

# Common Failure Modes

- Writing from memory or prior docs instead of inspecting the product.
- Mixing onboarding, reference, and explanation into a single wall of text.
- Assuming the reader knows prerequisites that were never stated.
- Shipping snippets that were never run or checked.
- Hiding uncertainty rather than labeling missing or unverified details.
- Treating doc updates as optional follow-up after the feature already shipped.

# Example Prompt

"Use `documentation-pass` on this docs surface. Audit the real source of truth first, define the audience and doc type, restructure the content around the reader's entry point, verify the commands and examples, and report any remaining unknowns explicitly instead of inventing details."
