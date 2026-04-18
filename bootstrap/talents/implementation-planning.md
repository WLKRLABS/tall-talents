---
slug: implementation-planning
title: Implementation Planning
summary: Convert an approved design into an execution-ready plan with exact files, tasks, tests, commands, and acceptance criteria.
tags:
  - planning
  - execution
  - specification
triggers:
  - An approved design or exact requirement set must be turned into a plan another agent or engineer can execute faithfully.
  - Multi-step work needs exact paths, verification commands, and commit-sized task boundaries before coding starts.
inputs:
  - Approved spec or exact requirement source.
  - Current repo structure, existing patterns, and known verification commands.
outputs:
  - Saved implementation plan with exact task boundaries, file paths, step-level actions, and acceptance criteria.
  - Clear execution handoff into inline execution or a reviewed subagent loop.
agent_behavior:
  - Assume the executor has zero context and will take shortcuts if the plan leaves room for interpretation.
  - Quote exact requirements from the spec instead of paraphrasing them into broader scope.
  - Favor realistic, testable task boundaries over ambitious all-at-once plans.
safety:
  - Do not add premium polish, refactors, or platform work that the approved spec did not ask for.
  - Do not leave placeholders, vague steps, or undefined interfaces in the plan.
status: active
version: 1.0.0
---

# Goal

Turn an approved design into a plan that can be executed with minimal interpretation. The plan should tell a skilled but context-poor executor what to touch, in what order, how to verify progress, and what counts as done.

## Use It When

- A design has been approved and implementation is non-trivial.
- Another agent, another session, or a human engineer needs a faithful execution artifact.
- The task spans multiple files, tests, or verification commands.

## Do Not Use It When

- No approved design exists yet. Use `design-before-build` first.
- The task is a tiny, safe one-pass edit where planning overhead would dominate the work.
- Requirements are still ambiguous enough that a plan would bake in guesses.

## Preconditions

You need the real requirement source in hand: an approved spec, a written brief, or a direct requirement document. Planning from memory or a chat summary is not sufficient.

# Procedure

## 1. Re-Read The Actual Requirements

Start with the source artifact, not your recollection of it:

- read the approved spec or requirement file
- quote the exact requirements that materially affect implementation
- extract hard constraints: stack, interfaces, rollout rules, migration needs, performance limits, or compliance boundaries
- identify any unresolved gaps that would make the plan speculative

If important ambiguity remains, stop and return to design clarification instead of papering over the gap in the plan.

## 2. Run A Scope Reality Check

Confirm the plan is for one coherent delivery slice:

- if the spec covers multiple independent subsystems, split it into separate plans
- each plan should produce working, testable software on its own
- prefer the smallest slice that creates usable progress without fake completeness

Large plans fail when they mix unrelated changes and hide missing dependencies.

## 3. Lock The File Map Before Writing Tasks

Before defining task order, map the files and responsibilities:

- list exact files to create, modify, test, or document
- state what each file is responsible for
- keep boundaries clear and interfaces explicit
- follow existing codebase patterns unless the spec explicitly includes structural cleanup

This is the point where decomposition quality is won or lost. Files that change together should usually be planned together. Files with different responsibilities should not be fused into one task just because they share a language or layer.

## 4. Write A Plan Header That Frames The Work

Begin the saved plan with a compact header that gives any executor immediate orientation:

- feature or change name
- one-sentence goal
- short architecture summary
- relevant tech stack or libraries
- any required execution mode or workspace assumptions

The header is not decoration. It explains why the tasks are shaped the way they are.

## 5. Break Work Into Real Tasks

Each task should be a coherent unit a developer can finish in roughly 30-60 minutes:

- group work by deliverable, not by vague project phase
- give each task a clear end state
- include acceptance criteria
- include exact files touched
- keep the task self-contained enough that it can be reviewed independently

Good task boundaries reduce merge risk, review ambiguity, and context switching. Bad task boundaries create sprawling edits that are hard to verify.

## 6. Break Tasks Into One-Action Steps

Each step inside a task should be a single action that usually takes 2-5 minutes:

- write the failing test
- run it and confirm failure
- implement the minimal code needed
- run the targeted verification again
- commit or checkpoint the task

Do not collapse these into one vague instruction. The point is to make progress observable and recoverable.

## 7. Make Every Step Concrete

For every task and step, include the details the executor would otherwise invent:

- exact file paths
- exact commands
- expected outcomes for those commands
- function names, interface shapes, payloads, queries, migrations, or config keys when they matter
- docs and follow-up verification steps if the spec requires them

Weak planning language is banned:

- `TBD`
- `TODO`
- "implement later"
- "add error handling"
- "handle edge cases"
- "write tests for the above"
- "similar to Task N"

If a step changes code, give enough concrete structure that the executor does not have to decide the API, data shape, or control flow from scratch.

## 8. Keep The Plan Faithful To The Approved Scope

Use the exact spec, not an aspirational rewrite of it:

- do not add luxury, premium, or polish work unless explicitly requested
- prefer functional completeness before extra refinement
- include migration, docs, or cleanup only when they are required for the approved outcome
- when optional follow-ups are valuable, place them in a separate deferred section instead of smuggling them into the main plan

This is where project-manager realism matters. A plan that quietly expands scope is already wrong.

## 9. Self-Review The Whole Plan

Review the finished plan before handing it off:

- spec coverage: every material requirement maps to at least one task
- placeholder scan: remove vague language and implied work
- consistency check: names, types, interfaces, and file paths stay consistent across tasks
- verification check: commands are runnable and appropriate for the repo
- dependency check: no task depends on definitions that only appear later without saying so

Fix issues inline. Do not hand off a plan that still requires interpretation.

## 10. End With An Execution Handoff

The plan ends when the execution mode is clear:

- use an inline execution path when the same agent will carry out the work directly
- use a reviewed subagent loop when tasks are independent enough to dispatch and review

The handoff should state the plan path, the chosen execution mode, and any required verification cadence.

# Success Criteria

- The plan is traceable to an approved design or exact requirement source.
- Tasks are small, coherent, and independently reviewable.
- Every task includes exact files, acceptance criteria, and meaningful verification steps.
- No placeholders or scope-creep language remain.
- A new executor could carry out the work without inventing missing structure.

# Common Failure Modes

- Planning from memory instead of re-reading the approved spec.
- Creating one giant task that hides real dependencies and makes review impossible.
- Using vague language where exact commands, files, or interfaces were required.
- Quietly adding polish or refactors that the approved scope did not include.
- Forgetting acceptance criteria, which turns completion into opinion instead of evidence.
- Handing off a plan whose later tasks depend on names or shapes that were never actually defined.

# Example Prompt

"Use talent `implementation-planning` on this approved spec. Re-read the exact requirements, map the file responsibilities first, produce an execution-ready plan with exact tasks and verification commands, self-review it for placeholders and scope creep, and stop at the execution handoff."
