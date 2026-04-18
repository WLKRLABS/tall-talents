---
slug: systematic-debugging
title: Systematic Debugging
summary: Debug through root-cause investigation, pattern analysis, single-hypothesis testing, and only then a minimal verified fix.
tags:
  - debugging
  - quality
  - verification
triggers:
  - Test failures, production bugs, build breaks, unexpected behavior, performance regressions, or integration failures.
  - Situations where a quick fix feels tempting or multiple failed attempts have already happened.
inputs:
  - Reproduction steps, error output, recent changes, and access to the relevant system boundaries.
  - Available tests, logs, traces, or ways to instrument the failing path.
outputs:
  - Root-cause statement backed by evidence.
  - Minimal fix, verification evidence, and a clear escalation decision if architecture is the real problem.
agent_behavior:
  - Treat symptom fixes as failure until the root cause is understood.
  - Investigate with evidence first, then test one hypothesis at a time.
  - Stop after repeated failed fixes and question the underlying pattern instead of thrashing.
safety:
  - Do not propose or apply fixes before completing root-cause investigation.
  - Do not bundle multiple speculative fixes into one attempt.
status: active
version: 1.0.0
---

# Goal

Resolve technical issues by finding the real cause before changing code. The talent exists to stop guess-and-check debugging, reduce regression risk, and surface architectural problems early instead of normalizing thrash.

## Use It When

- Any technical issue exists: bug, failing test, broken build, incident, performance problem, or integration error.
- The problem spans multiple components and the break point is unclear.
- The environment encourages rushing, guessing, or piling fixes on top of uncertainty.

## Do Not Skip It Because

- the issue looks simple
- time pressure is high
- the first fix seems obvious
- someone wants "just a quick patch"

Those are exactly the situations where ad hoc debugging causes the most damage.

## Iron Law

```text
No fixes without root-cause investigation first.
```

If Phase 1 is incomplete, you are not debugging yet. You are guessing.

# Procedure

## Phase 1: Root-Cause Investigation

Do this before proposing any fix.

### 1. Read The Error Carefully

- read the full error, warning, stack trace, line numbers, file paths, and codes
- do not skip to the location that looks fixable before understanding what the message is saying
- capture the exact failing symptom in writing

### 2. Reproduce Reliably

- define the exact steps to trigger the issue
- determine whether it happens every time, under certain conditions, or only with certain inputs
- if you cannot reproduce it reliably, gather more evidence instead of guessing

### 3. Check Recent Change Surface

- inspect recent diffs, config changes, dependency updates, migrations, and environment shifts
- look for the smallest plausible set of changes that could have introduced the issue

### 4. Instrument Multi-Component Boundaries

When the system spans layers or services, gather evidence at each boundary before deciding where the bug lives:

- log what enters and exits each component
- verify config and environment propagation
- inspect state changes at each layer
- use the first run to locate the break point, not to patch it

The goal is to learn where the system stops matching expectation.

### 5. Trace The Bad Data Backward

When the symptom appears deep in a call chain:

- ask where the bad value or state came from
- inspect the caller, then the caller of that caller
- keep tracing backward until you find the source condition that made the failure inevitable

Fixing the location where the error becomes visible is often only a symptom patch.

## Phase 2: Pattern Analysis

Once the failing path is understood, compare it against reality that already works.

### 1. Find Working Examples

- locate similar working code or workflows in the same codebase when possible
- compare broken and working cases side by side

### 2. Read The Reference Completely

- if a pattern or reference implementation exists, read it all the way through
- do not skim and "adapt the gist"
- note preconditions, hidden dependencies, and sequencing rules

### 3. List Differences Explicitly

- write down every observed difference between working and broken behavior
- keep even the ones that look too small to matter

### 4. Understand Dependencies

- identify required state, config, timing assumptions, side effects, and external contracts
- confirm whether the broken path satisfies those expectations

## Phase 3: Hypothesis And Minimal Testing

Use one hypothesis at a time.

### 1. State A Single Hypothesis

Write it plainly:

```text
I think [specific cause] is the root cause because [evidence].
```

If you cannot write that sentence, the investigation is not finished.

### 2. Test The Smallest Possible Change

- change one variable at a time
- use the smallest experiment that can confirm or reject the hypothesis
- do not stack fixes or "improve while here"

### 3. Evaluate The Result Honestly

- if the hypothesis is confirmed, move to implementation
- if it is rejected, return to investigation with the new information
- if you still do not understand the system, say so and gather more evidence

## Phase 4: Fix And Verify

Only now should code change.

### 1. Create A Failing Reproduction

- add the smallest failing automated test when possible
- if no test framework exists, create a one-off script or command that reproduces the failure
- verify the reproduction fails before applying the fix

### 2. Implement One Minimal Fix

- change only what is needed to address the identified root cause
- avoid bundled refactors, cleanup, or unrelated improvements

### 3. Verify The Fix

- re-run the failing reproduction
- run the relevant surrounding verification to check for regressions
- confirm the original issue is actually resolved, not merely hidden

## Escalation Rule After Repeated Failures

Count failed fix attempts.

- after one failed fix, return to Phase 1
- after two failed fixes, become suspicious that the current model is wrong
- after three failed fixes, stop and question the architecture or core pattern

Repeated failures often mean the issue is not another local bug. It may be a design problem, shared-state problem, or wrong abstraction. Do not attempt a fourth speculative fix without explicitly surfacing that possibility.

## When Investigation Ends With "No Root Cause"

Sometimes the best answer is that the issue is environmental, external, or timing-dependent:

- document what was investigated
- state why a deterministic internal root cause was not established
- implement appropriate handling such as retry, timeout, validation, or monitoring
- keep the unresolved risk visible instead of pretending it was solved

Most "no root cause" outcomes are incomplete investigation. Treat that conclusion skeptically.

## Suggested Debug Report

Use a short report so the reasoning stays auditable:

```markdown
## Debug Report

- Symptom:
- Reproduction:
- Root cause:
- Evidence:
- Hypothesis tested:
- Minimal fix:
- Verification:
- Remaining risk or escalation:
```

# Success Criteria

- A concrete root-cause statement exists and is backed by observed evidence.
- The final fix is minimal and directly tied to that cause.
- Verification proves the original failure is resolved.
- The workflow avoided stacked speculative fixes.
- If the issue is architectural, that conclusion was surfaced instead of buried under repeated local patches.

# Common Failure Modes

- Proposing fixes before reproducing the issue or reading the full error.
- Changing multiple things at once, making it impossible to learn what mattered.
- Fixing the symptom location instead of tracing the originating bad state.
- Skipping the failing reproduction and relying on manual confidence.
- Continuing past three failed attempts without questioning the architecture.
- Claiming "probably fixed" without fresh verification evidence.

# Example Prompt

"Use talent `systematic-debugging` on this failure. Reproduce it, inspect recent changes, instrument the relevant boundaries, trace the bad state to its source, test one hypothesis at a time, implement only the minimal verified fix, and stop for escalation if repeated fixes point to an architectural problem."
