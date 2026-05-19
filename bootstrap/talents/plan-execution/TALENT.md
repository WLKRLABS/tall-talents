---
slug: plan-execution
title: Plan Execution
summary: Execute a written implementation plan faithfully, stop on ambiguity, and only finish after the plan's required verification passes.
tags:
  - execution
  - planning
  - verification
triggers:
  - A written implementation plan, task list, or approved execution document already exists and the main need is faithful delivery rather than redesign.
  - Work must proceed step by step with explicit verification, blocker handling, and completion reporting.
inputs:
  - The exact plan file or written task list to execute.
  - Current repo state, workspace isolation method, and known verification commands.
outputs:
  - Completed plan execution with per-task progress, verification evidence, and a clear record of blockers or required clarifications.
  - Final finish-state report describing what was completed exactly as planned, what changed, and what remains unresolved.
agent_behavior:
  - Read the whole plan before editing anything and challenge gaps before work starts.
  - Execute tasks in the written order unless a dependency or contradiction requires a documented deviation.
  - Stop on ambiguity, repeated failures, or missing prerequisites instead of guessing.
safety:
  - Do not silently widen scope beyond the written plan.
  - Do not skip required verification, branch isolation, or finish-state review.
status: active
version: 1.0.0
---

# Goal

Turn a written implementation plan into completed work without improvising away requirements, skipping verification, or hiding blockers under momentum.

## Use It When

- The plan already exists and has enough detail to execute directly.
- The user wants delivery, not another design or planning pass.
- The work benefits from disciplined task tracking and explicit stop conditions.

## Do Not Use It When

- No written plan exists yet. Use `implementation-planning` first.
- The written plan is obviously stale, contradictory, or missing key scope decisions.
- The task is better handled through a per-task delegated loop. In that case use `subagent-task-loop`.

## Core Boundary

This talent is the non-delegated execution path.

- `implementation-planning` defines the work.
- `plan-execution` carries it out faithfully.
- `subagent-task-loop` is the delegated execution variant when subagents are available and appropriate.

# Procedure

## 1. Load The Exact Plan And Review It Before Touching Files

Read the whole plan, not just the first task.

Confirm:

- the goal is still current
- the task ordering still makes sense
- the files and commands named in the plan still exist
- the acceptance criteria are specific enough to verify
- the plan does not quietly require missing design decisions

If the plan has critical gaps, stop before implementation. Raise the gap explicitly and ask for clarification or a plan revision. Do not "fill in the blanks" with your preferred approach.

## 2. Set Up Safe Execution Conditions

Before the first edit, confirm the execution surface:

- correct repository and working directory
- isolated branch or worktree unless the user explicitly wants otherwise
- required tools, env vars, and dependencies available
- any repo-specific rules that constrain how changes must be made

If the plan assumes isolated execution, do not start on `main` or another integration branch without explicit approval.

## 3. Build A Concrete Task Tracker From The Plan

Translate the plan into a progress tracker you can execute against.

For each task capture:

- task name
- exact files or surfaces touched
- required verification
- completion signal
- current state: pending, in progress, blocked, completed

This tracker is not a rewrite of the plan. It is the minimum structure needed to make progress visible and prevent skipped steps.

## 4. Execute One Task At A Time

For each task:

1. mark it in progress
2. re-read the task text and acceptance criteria
3. make only the edits needed for that task
4. run the task-specific verification before calling it done
5. record the result honestly

Do not blur neighboring tasks together because the code is nearby. If the plan separated them, there was probably a reason: reviewability, verification clarity, or rollback safety.

## 5. Follow The Written Steps Literally Unless Reality Forces A Change

The plan should do most of the thinking for you. Your job is execution discipline.

Allowed reasons to deviate:

- the repo has drifted since the plan was written
- a named file or interface no longer exists
- a prerequisite task was wrong or incomplete
- verification proves the plan's sequence is unsafe or impossible

When deviation is necessary:

- state it clearly
- keep the change as small as possible
- preserve the original intent
- document the new sequence before continuing

Unexplained deviation is scope creep disguised as initiative.

## 6. Stop Immediately On These Conditions

Stop execution and surface the issue when:

- an instruction is ambiguous enough that multiple incompatible implementations are possible
- a required dependency or secret is missing
- the plan's assumptions are false in the current repo
- verification fails repeatedly without a clear fix path
- following the plan would break unrelated work or violate repo rules

Do not push through blockers because "the intent is obvious." That is how plan execution silently becomes redesign.

## 7. Treat Verification As Part Of The Task, Not Cleanup Afterward

Each task is incomplete until its required verification passes.

Verification can include:

- targeted tests
- builds or type checks
- linting
- local runtime checks
- screenshots or manual walkthroughs
- document accuracy checks

If the plan names multiple layers of verification, run them in the order written. Do not skip the expensive one because the cheap one passed.

## 8. Revisit Earlier Tasks When New Evidence Requires It

If a later task reveals a defect in an earlier one:

- reopen the earlier task explicitly
- fix the issue with minimal blast radius
- rerun the earlier verification
- rerun any downstream verification that could be affected

Do not bury cross-task fixes inside the current task with no record. That makes the plan look complete while hiding rework.

## 9. Finish With A Whole-Plan Review

After all tasks appear complete, perform a final pass against the original plan:

- every task marked complete
- every acceptance criterion covered
- every required verification run
- no known blocker left implicit
- no unapproved scope additions mixed into the delivery

If the plan required a final branch-finishing or integration workflow, do that now rather than declaring success early.

## 10. Report What Actually Happened

Close with a concise execution report:

```markdown
## Plan Execution Report

- Plan source:
- Tasks completed:
- Verification run:
- Deviations from plan:
- Blockers encountered:
- Remaining risks:
```

The report should let another engineer understand whether the plan was executed faithfully or whether it needs revision before more work continues.

## Strong vs Weak Execution

Strong:

- reads the plan first
- catches plan gaps before code changes
- keeps task boundaries intact
- records deviations when reality forces them
- stops on blockers instead of guessing

Weak:

- starts editing after skimming the first task
- merges tasks because "it is faster"
- skips verification until the end
- hides drift between plan and repo
- reports completion while known acceptance criteria remain unverified

# Success Criteria

- The work delivered matches the written plan or documented, justified deviations from it.
- Every completed task has corresponding verification evidence.
- The executor stopped on true ambiguity instead of inventing missing decisions.
- Final reporting makes task status, deviations, and remaining risk explicit.
- No silent scope expansion occurred during execution.

# Common Failure Modes

- Treating a plan like a suggestion and redesigning on the fly.
- Starting work before verifying the plan is still valid in the current repo.
- Skipping task-level verification and hoping the full suite at the end will catch everything.
- Continuing after repeated failures without surfacing that the plan may be wrong.
- Collapsing multiple planned tasks into one large edit that becomes hard to review or roll back.
- Finishing the code but forgetting the plan's required closeout workflow.

# Example Prompt

"Use `plan-execution` on this approved implementation plan. Review the plan critically before editing, execute one task at a time with the required verification, stop on ambiguity instead of guessing, and finish with a whole-plan execution report."
