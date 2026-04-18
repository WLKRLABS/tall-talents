---
slug: review-feedback-triage
title: Review Feedback Triage
summary: Evaluate review comments technically before agreeing or implementing, then respond with clear accept, clarify, pushback, or escalation decisions.
tags:
  - review
  - collaboration
  - decision-making
triggers:
  - Review feedback arrives from a human, teammate, QA pass, or external reviewer.
  - Comments appear technically questionable, vague, over-broad, or in tension with existing constraints.
  - Multi-item feedback must be processed without blind agreement or scope creep.
inputs:
  - Review comments or QA verdict.
  - Current code or diff state.
  - Relevant requirements, constraints, and prior architectural decisions.
outputs:
  - Technical response per item: accept, clarify, push back, defer, or escalate.
  - Ordered implementation sequence for accepted items with verification after each.
agent_behavior:
  - Read all feedback before reacting.
  - Verify each item against repo reality before agreeing or changing code.
  - Keep replies factual and technical rather than performatively agreeable.
safety:
  - Do not implement unclear feedback before the unclear parts are resolved.
  - Do not agree with comments that conflict with code reality, user decisions, or required scope.
status: active
version: 1.0.0
---

# Goal

Turn incoming review feedback into technically sound action instead of social performance. This talent exists because comments can be correct, wrong, vague, incomplete, or scope-expanding, and each case needs a different response.

## Use It When

- Pull request comments arrive.
- QA returns a fail verdict with issue lists.
- A human asks for multiple fixes at once.
- An external reviewer suggests changes that might not fit the codebase or product constraints.

## Do Not Use It When

- No review feedback exists yet. Use `code-review`.
- The task is still in implementation and no review boundary has happened.

# Procedure

## 1. Read The Entire Feedback Set First

Do not start fixing item 1 while items 4 and 5 are still misunderstood.

Make one pass over the full feedback and group items into:

- clearly understood
- unclear
- obviously blocked on more context
- likely wrong or questionable

If any unclear item could change how the rest should be handled, stop and resolve that first.

## 2. Restate Each Item In Technical Terms

Convert commentary into a precise requirement.

Example conversions:

- "This feels brittle" -> "The reviewer suspects this branch can fail when input X is absent."
- "Implement this properly" -> "The reviewer is asking for a wider abstraction or stronger contract."
- "Fix 1-6" -> six distinct technical items, each with scope and expected result.

If you cannot restate an item precisely, you do not understand it yet.

## 3. Verify Each Item Against Repo Reality

For every comment, inspect the real code, tests, and constraints:

- is the reviewer describing the current behavior accurately
- is there already a guard, test, or compatibility reason they missed
- does the suggestion break existing supported behavior
- does it widen scope beyond the requested task
- does it conflict with an earlier explicit user decision

Review feedback is input, not truth.

## 4. Choose A Disposition Per Item

Each item gets one of five outcomes.

### Accept

The reviewer is correct and the change belongs in the current scope.

### Clarify

The intent is unclear enough that implementation would be guesswork.

### Push Back

The suggestion is technically wrong, context-blind, conflicts with a higher-priority constraint, or would create unjustified scope.

### Defer

The point is valid, but it belongs in a separate follow-up rather than the current patch.

### Escalate

The item conflicts with user direction, architecture policy, or another reviewer in a way that requires a decision rather than a coding change.

## 5. Use Technical Responses, Not Performance Language

Keep acknowledgments factual.

Strong patterns:

- "Verified. This branch can return the wrong value when `token` is empty. Fixing it in `auth/session.ts`."
- "Need clarification on items 4 and 5 before changing anything because they affect the same control flow."
- "Checked this against the current compatibility target. Removing the legacy path would drop supported versions."
- "Valid point, but it widens scope. Logging it as a follow-up instead of adding it to this patch."

Weak patterns:

- "You're absolutely right."
- "Great point."
- "Let me implement that now." before verification
- vague gratitude or agreement with no technical content

## 6. Handle Unclear Multi-Item Feedback As A Stop Condition

When feedback comes as a list, do not implement the understood subset if the unclear items could affect the same area.

Preferred response:

```markdown
I understand items 1, 2, and 3.
I need clarification on items 4 and 5 before changing this area because they appear related to the same flow.
```

Partial understanding is not a safe implementation basis.

## 7. Order Accepted Work Deliberately

After triage, apply accepted items in this order:

1. blockers: correctness, security, breakage
2. simple low-risk fixes
3. complex logic or structural changes
4. optional cleanups that remain in scope

Verify each accepted fix independently before moving to the next one. Do not batch a large ambiguous set and hope the final test run sorts it out.

## 8. Run A YAGNI And Scope Check

When feedback sounds like "make this more proper," check whether the requested expansion is actually needed now.

Useful questions:

- Is the broader abstraction already needed by another caller?
- Is the unused endpoint, code path, or config actually exercised anywhere?
- Would this change belong in a separate ticket if the reviewer had not seen the current diff?

If the answer is no, prefer defer or pushback over silent expansion.

## 9. Escalate Conflicts Explicitly

Escalate when:

- two reviewers disagree materially
- the comment conflicts with explicit user direction
- the change would alter a product or architecture decision
- the correct answer depends on policy rather than code facts

Escalation should include:

- the conflicting items
- what the code currently does
- what each path would change
- the decision required

## Response Template

```markdown
## Review Feedback Triage
- Item: [short label]
- Disposition: Accept | Clarify | Push back | Defer | Escalate
- Reasoning: [repo-grounded explanation]
- Action:
  - [fix now]
  - [question to ask]
  - [follow-up to file]
  - [decision needed]
```

## Integration Notes

- Use after `code-review`, QA verdicts, or pull request comments.
- Pair with `minimal-diff-execution` when accepted feedback risks widening scope.
- Pair with `verification-gate` after each accepted fix is applied.

# Success Criteria

- Every feedback item receives an explicit technical disposition.
- No unclear item is implemented by guesswork.
- Correct comments are fixed efficiently.
- Wrong or over-broad comments receive reasoned pushback instead of blind agreement.
- Scope expansion is separated into follow-ups rather than silently absorbed.

# Common Failure Modes

- Agreeing before verification.
- Implementing only the understood subset of a related feedback batch.
- Treating external review comments as automatically correct.
- Using gratitude or performative agreement instead of technical acknowledgment.
- Rolling multiple accepted fixes together without per-item verification.
- Allowing review-time comments to smuggle unrelated new work into the patch.

# Example Prompt

"Use `review-feedback-triage` on these PR comments. Read the full set first, verify each item against the codebase, decide accept, clarify, push back, defer, or escalate, then implement only the accepted items in a verified order."
