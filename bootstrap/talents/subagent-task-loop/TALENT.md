---
slug: subagent-task-loop
title: Subagent Task Loop
summary: Execute a written plan through one task-scoped implementer at a time, with mandatory spec-compliance and code-quality review loops before a task can close.
tags:
  - delegation
  - execution
  - review
triggers:
  - A written implementation plan exists and work should be delegated task by task while the controller keeps coordination context.
  - Quality must be enforced through explicit review loops rather than trusting a single implementation pass.
inputs:
  - Exact plan text with task boundaries already defined.
  - Delegation tools, model options, and enough repo context to create self-contained task packets.
outputs:
  - Task-by-task implementation with review evidence and explicit approval before each task closes.
  - Final integrated result plus a record of open concerns, fixes, and escalation points.
agent_behavior:
  - Keep controller context focused on orchestration, not direct implementation.
  - Give each implementer only the scoped context needed for the current task.
  - Require spec review before code-quality review on every task.
safety:
  - Do not dispatch overlapping implementation work that writes the same files.
  - Do not let any task advance while spec or quality review still has open issues.
status: active
version: 1.0.0
---

# Goal

Raise implementation quality by separating execution from review, keeping each task narrowly scoped, and forcing every task through a repeatable review loop before moving on.

## Use It When

- A real implementation plan already exists.
- Tasks are independent enough to execute one by one with isolated delegated context.
- You have working subagent or delegated-worker support.
- The controller needs to preserve its own context for coordination, not coding.

## Do Not Use It When

- No written plan exists yet.
- The work is tightly coupled enough that each task depends on constant shared implementation context.
- Delegation tooling is unavailable. Use `plan-execution` instead.
- The task is so small that adding three review stages would cost more than the work itself.

## Non-Negotiable Loop

For every task:

1. implement
2. spec-compliance review
3. code-quality review
4. mark complete

If either review fails, the same task re-enters the loop. No exceptions.

# Procedure

## 1. Read The Whole Plan And Extract Task Packets Up Front

Before dispatching anyone:

- read the full plan once
- extract each task's exact text
- note acceptance criteria, dependencies, and file scope
- identify which context each task packet must include

Do not make delegated implementers hunt through the plan file for meaning. The controller should front-load that work and provide the task in self-contained form.

## 2. Decide Whether The Task Shape Fits This Talent

Use this talent only if all of the following are true:

- each task has a coherent end state
- the controller can describe the task without dumping the entire project
- the task's write scope is narrow enough to review cleanly
- there is a meaningful chance that review will catch under-build or over-build

If the plan is still vague, go back to `implementation-planning`. If the task scope is too entangled, do not force a delegated loop.

## 3. Choose The Right Model Or Worker Level For The Task

Match implementation complexity to the cheapest worker that can reliably do it.

Use lower-cost implementers for:

- tightly scoped mechanical edits
- 1-2 file changes
- well-specified test or docs work

Use stronger implementers for:

- multi-file coordination
- debugging
- integration-sensitive changes
- tasks requiring substantial judgment

Use stronger reviewers than implementers when the task carries architectural, security, or correctness risk.

## 4. Build A Self-Contained Implementer Prompt

Each implementer prompt should include:

- task name
- exact goal
- required file scope
- relevant context only
- acceptance criteria
- constraints and non-goals
- verification to run
- output format

Good prompts are narrow, concrete, and impossible to misunderstand.

Bad prompts say "implement Task 4 from the plan" and assume the subagent can infer the rest.

## 5. Handle Implementer Status Explicitly

Require implementers to return one of these states:

- `DONE`
- `DONE_WITH_CONCERNS`
- `NEEDS_CONTEXT`
- `BLOCKED`

Controller actions:

- `DONE`: move to spec review
- `DONE_WITH_CONCERNS`: read the concern first, resolve material issues, then review
- `NEEDS_CONTEXT`: answer clearly and re-dispatch
- `BLOCKED`: change something real before retrying: context, task shape, model, or plan

Never punish a `BLOCKED` signal by blindly retrying the same prompt.

## 6. Run Spec-Compliance Review Before Any Quality Review

The first reviewer checks only this question:

Did the implementation match the written task and nothing more?

Review against:

- scope
- acceptance criteria
- task-specific constraints
- banned extras
- missing required behavior

If spec review fails:

- send the findings back to the implementer
- keep the task open
- rerun spec review after the fix

Do not start quality review while scope alignment is still unresolved.

## 7. Run Code-Quality Review Only After Scope Is Green

Once spec compliance is approved, run a second review for implementation quality:

- correctness
- maintainability
- test quality
- edge-case handling
- naming and structure
- obvious regression risk

If quality review fails:

- send concrete findings back to the implementer
- rerun quality review after fixes
- do not mark the task complete while any quality issue remains open

The review order matters. Spec first prevents polishing the wrong thing.

## 8. Keep One Active Implementation Writer Per Write Scope

This talent is task-loop delegation, not uncontrolled concurrency.

Do:

- allow multiple reviewers on the same task only sequentially
- keep only one active implementer on the current write scope
- queue later tasks until the current task closes when scopes overlap

Do not:

- run multiple implementers against the same files
- let a later task begin just because the current implementer said "almost done"
- accept merge-conflict cleanup as a normal part of the process

## 9. Mark A Task Complete Only After All Three Checks Pass

A task can close only when:

- implementation exists
- spec-compliance review approves it
- code-quality review approves it

Record:

- reviewer verdicts
- key issues fixed
- verification that passed
- any residual concern worth carrying to final review

Without this record, the loop becomes memory-dependent and fragile.

## 10. End With A Final Integration Review

After all tasks close:

- run whole-change verification
- review cross-task interactions
- check for hidden inconsistencies created across individually correct tasks
- hand off to the repo's branch-finish or integration workflow if required

Per-task review does not replace whole-system validation.

## Review Packet Template

Use a compact structure for each stage:

```markdown
## Task Review

- Task:
- Review type: spec-compliance | code-quality
- Verdict: approved | issues found
- Issues:
- Required fixes:
- Verification checked:
```

## Strong vs Weak Execution

Strong:

- extracts task packets before dispatch
- gives implementers scoped context
- enforces review order
- treats reviewer findings as blocking
- keeps controller attention on orchestration and integration

Weak:

- makes implementers read the whole plan themselves
- starts quality review before scope is validated
- treats review as optional advice
- advances tasks with open issues
- uses delegation to avoid thinking instead of increasing quality

# Success Criteria

- Every task passed implementation, spec review, and code-quality review before closing.
- Implementers received self-contained, tightly scoped task packets.
- Review findings were fixed and re-reviewed instead of waved through.
- The controller preserved overall coordination context and integrated results cleanly.
- Final validation confirmed that individually approved tasks also work together.

# Common Failure Modes

- Dispatching work before the plan is actually clear enough to delegate.
- Letting implementers infer missing context from the repo or from prior conversation history.
- Running code-quality review before confirming the task actually matches the spec.
- Allowing multiple implementers to edit overlapping files because "they are on different tasks."
- Marking tasks complete when reviewer findings remain open.
- Forgetting the final integrated verification because each task looked good in isolation.

# Example Prompt

"Use `subagent-task-loop` on this implementation plan. Extract each task into a self-contained packet, dispatch one implementer at a time, require spec-compliance review before code-quality review, loop until both reviewers approve, and only then mark each task complete."
