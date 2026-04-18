---
slug: minimal-diff-execution
title: Minimal Diff Execution
summary: Solve the stated task with the smallest justifiable diff, resist scope creep, and separate follow-ups from the patch itself.
tags:
  - execution
  - scope
  - review
triggers:
  - A bug fix, compatibility patch, or tightly scoped change is requested.
  - The user cares about exact scope boundaries and does not want opportunistic cleanup.
  - Review or implementation work risks expanding into refactor or redesign.
inputs:
  - Exact task statement or approved requirement.
  - Smallest failing surface area and candidate files.
  - Current diff and any tempting out-of-scope follow-ups discovered along the way.
outputs:
  - Small scoped patch that satisfies the task.
  - Explicit list of follow-ups noted but intentionally not included.
agent_behavior:
  - Read the task literally before opening extra files.
  - Prefer the boring smaller diff over the elegant larger one when both solve the task.
  - Justify every changed line against the stated requirement.
safety:
  - Do not refactor, modernize, or generalize unless the task explicitly requires it.
  - Do not silently absorb review-time or discovery-time scope expansion into the current patch.
status: active
version: 1.0.0
---

# Goal

Deliver exactly the change that was requested and no more. This talent exists because many clean bug fixes and targeted features get buried under accidental refactors, speculative abstraction, and "while I'm here" edits that increase review time and failure risk without increasing delivered value.

## Use It When

- fixing a specific bug
- adding one feature flag or one narrow behavior branch
- making a compatibility, versioning, or build patch
- working in a repo where the user explicitly values scope discipline

## Do Not Use It When

- the user explicitly asked for structural cleanup or redesign
- the task is a planned architecture refactor
- the current code cannot satisfy the requirement without a broader change and that broader change has already been approved

# Procedure

## 1. Read The Task Literally

Start with the exact wording, not your preferred interpretation.

Focus on the verbs:

- "fix" means fix, not improve
- "add" means add only what is required
- "remove" means remove, not replace with a larger system

If the task could reasonably mean a much bigger change, ask once before widening scope. Do not choose the larger interpretation silently.

## 2. Find The Minimum Surface Area

Trace the smallest set of files and functions that must change for the task to succeed.

Questions to ask:

- what code path actually produces the failing behavior
- what file owns that behavior
- what tests or verification touch the same path
- which neighboring files are truly required and which are merely nearby

If you are opening a fourth or fifth file for a supposed small fix, stop and justify why each one is necessary.

## 3. Prefer The Smallest Working Shape

When several approaches work, choose the one that changes fewer lines and fewer responsibilities.

Biases to preserve:

- one branch over a new framework
- one local variable over a new config system
- direct duplication over premature abstraction
- a targeted edit over a module rewrite

Three similar lines are usually cheaper than a helper added for hypothetical future reuse. Extract only when the repetition burden is real, not imagined.

## 4. Avoid Defensive Or Future-Proofing Drift

Do not add code for scenarios the current task does not require.

Examples of drift:

- config flags for a second caller that does not exist
- error handling for impossible internal states
- compatibility shims for unused code paths
- type, comment, or naming cleanup in untouched areas
- framework migrations hidden inside a bug fix

Validate at true system boundaries. Do not spray defensive checks through internal code just because you touched it.

## 5. Walk The Diff Line By Line

Before finalizing, inspect every changed line and ask:

"Does the task require this exact line?"

Delete anything whose justification sounds like:

- "while I was here"
- "this is cleaner"
- "might help later"
- "for consistency"
- "I noticed something nearby"

The correct place for those thoughts is a follow-up list, not the patch.

## 6. Separate Follow-Ups From The Current Patch

Capture adjacent real issues without solving them here.

Default format:

```markdown
## Follow-Ups Not Included
- [item] - [why it is real] - [why it stays out of this patch]
```

This preserves awareness without widening the diff.

## 7. Resist Review-Time Scope Expansion

When feedback includes "while you're here" requests:

- check whether the new request is required to make the current patch correct
- if not, defer it to a separate follow-up
- if yes, explain why the patch scope changed and update the scope statement explicitly

Do not let review comments turn a clean patch into an unrelated bundle.

## 8. Verify The Targeted Behavior

Minimal diffs still require real proof.

- run the smallest verification that proves the requested change
- if the task is a bug fix, verify the failing path
- if the task is a small feature, verify the exact new behavior
- if broader checks are still needed by repo policy, run them, but keep the patch itself small

Use `verification-gate` before claiming the diff is done.

## Scope Self-Check

Use this before handing off or merging:

```markdown
## Scope Self-Check
- Task as stated: [exact text]
- Files touched:
  - [path] - required because [reason]
- Out-of-scope items noticed:
  - [item]
- Abstractions considered and rejected:
  - [item] - rejected because current need is too small
- Could this diff be smaller:
  - yes | no
```

## Decision Boundaries

- If the requirement can be satisfied by a one-line or one-branch change, prefer that.
- If the broader cleanup is genuinely required, state the scope change explicitly before proceeding.
- If you cannot explain why a touched file is necessary, it should probably not be in the patch.

## Integration Notes

- Pair with `verification-gate` before completion claims.
- Pair with `review-feedback-triage` when review comments try to widen the patch.
- Pair with `implementation-planning` when the work is larger than the original literal task and needs a re-bounded plan.

# Success Criteria

- The patch solves the requested problem without unrelated cleanup.
- Every touched file has a clear task-level justification.
- Future-proofing and speculative abstraction are absent.
- Real adjacent issues are surfaced as follow-ups instead of being smuggled into the patch.
- The targeted behavior is verified after the minimal change lands.

# Common Failure Modes

- Treating "fix" as permission to redesign the subsystem.
- Adding defensive code for impossible internal cases.
- Extracting helpers before repeated need exists.
- Touching nearby files for consistency rather than necessity.
- Accepting review-time scope expansion without re-bounding the task.
- Calling a diff minimal without checking each changed line against the task.

# Example Prompt

"Use `minimal-diff-execution` for this bug fix. Read the task literally, touch the minimum surface area, justify every changed line, list real follow-ups separately, and verify only the behavior this patch is supposed to change."
