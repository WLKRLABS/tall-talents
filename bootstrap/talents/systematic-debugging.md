---
slug: systematic-debugging
title: Systematic Debugging
summary: Diagnose hard bugs and performance regressions through a fast feedback loop, ranked hypotheses, targeted instrumentation, and only then a minimal verified fix.
tags:
  - debugging
  - quality
  - verification
triggers:
  - Test failures, production bugs, build breaks, unexpected behavior, performance regressions, or integration failures.
  - User says "diagnose this", "debug this", reports something broken, throwing, failing, or slow.
  - Situations where a quick fix feels tempting or multiple failed attempts have already happened.
inputs:
  - Reproduction steps, error output, recent changes, and access to the relevant system boundaries.
  - Available tests, logs, traces, fixtures, profilers, or ways to instrument the failing path.
outputs:
  - Root-cause statement backed by evidence.
  - Minimal fix, regression test or documented missing seam, verification evidence, and a clear escalation decision if architecture is the real problem.
agent_behavior:
  - Spend disproportionate effort creating a fast, deterministic pass/fail loop before hypothesizing.
  - Treat symptom fixes as failure until the root cause is understood.
  - Generate ranked falsifiable hypotheses, then test one hypothesis at a time with probes mapped to predictions.
  - Stop after repeated failed fixes and question the underlying pattern instead of thrashing.
safety:
  - Do not propose or apply fixes before completing root-cause investigation.
  - Do not bundle multiple speculative fixes into one attempt.
status: active
version: 1.1.0
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

## Diagnose Rule

Build the feedback loop first. If you have a fast, deterministic, agent-runnable pass/fail signal for the user-described bug, bisection, instrumentation, and hypothesis testing have something real to consume. If you do not have that loop, staring at code will turn into guesswork.

# Procedure

## Phase 1: Root-Cause Investigation

Do this before proposing any fix.

### 0. Build A Pass/Fail Feedback Loop

Create the narrowest loop that reproduces the user's symptom and can be run repeatedly.

Try options in this order:

- failing test at the seam that reaches the bug
- curl or HTTP script against a running dev server
- CLI invocation with fixture input and stdout or snapshot diff
- headless browser script that asserts on DOM, console, or network behavior
- captured trace replay through the failing path
- throwaway harness around the smallest service or function cluster
- property or fuzz loop for intermittent wrong-output bugs
- bisection harness suitable for `git bisect run`
- differential loop against old version, new version, or two configs
- HITL script only when a human must click, with captured output feeding back into the loop

Improve the loop itself before moving on:

- make it faster by skipping unrelated setup
- make the signal sharper by asserting the exact symptom
- make it deterministic by pinning time, seeds, filesystem, and network

For nondeterministic bugs, raise the reproduction rate instead of waiting for a perfect repro. Loop the trigger, add stress, parallelize, narrow timing windows, or inject delays until the failure rate is high enough to debug.

If no loop is possible, stop and say exactly what was tried. Ask for the missing environment, captured artifact, or permission to add temporary instrumentation. Do not proceed to hypotheses without a loop.

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

For hard bugs, generate 3-5 ranked hypotheses before testing any one of them. Each must be falsifiable:

```text
If [X] is the cause, then [changing or observing Y] will make [Z] happen.
```

When useful, show the ranked list to the user before testing. They may have domain knowledge that reranks or eliminates candidates. If the user is not available, proceed with the best-ranked hypothesis and keep the list visible.

### 2. Test The Smallest Possible Change

- change one variable at a time
- use the smallest experiment that can confirm or reject the hypothesis
- do not stack fixes or "improve while here"

Each instrumentation probe must map to a specific hypothesis prediction. Prefer debugger or REPL inspection when available, then targeted logs at decision boundaries. Never spray logs everywhere and grep later.

Tag temporary debug logs with a unique prefix such as `[DEBUG-a4f2]` so cleanup is mechanical.

For performance regressions, establish a baseline measurement before changing code. Use timing harnesses, browser performance APIs, profilers, query plans, or bisection. Measure first, fix second.

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

Write the regression test at the correct seam. The seam is correct only if the test exercises the real bug pattern as it appears at the call site. If the only available seam is too shallow, document that missing test seam as an architecture finding instead of creating a misleading test.

### 2. Implement One Minimal Fix

- change only what is needed to address the identified root cause
- avoid bundled refactors, cleanup, or unrelated improvements

### 3. Verify The Fix

- re-run the failing reproduction
- run the relevant surrounding verification to check for regressions
- confirm the original issue is actually resolved, not merely hidden
- re-run the original unminimized feedback loop from Phase 1
- remove all tagged debug instrumentation and throwaway prototypes, or move retained harnesses to a clearly marked debug location
- state the winning hypothesis in the commit, PR, or handoff so the next debugger inherits the learning

After the fix, ask what would have prevented the bug. If the answer is no good test seam, tangled callers, hidden coupling, or similar structural friction, hand off to `improve-codebase-architecture` after the fix is in.

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
