---
slug: parallel-agent-dispatch
title: Parallel Agent Dispatch
summary: Run independent investigations or implementation tracks concurrently only when their context, dependencies, and write scopes are cleanly separated.
tags:
  - delegation
  - concurrency
  - coordination
triggers:
  - Two or more workstreams are independent enough to benefit from concurrent execution.
  - Sequential handling would waste time because each problem domain can be understood and verified separately.
inputs:
  - A set of candidate tasks, failures, or workstreams to classify.
  - Clear file boundaries, dependency knowledge, and a way to review integrated results.
outputs:
  - Parallelized task execution with isolated prompts, non-overlapping scopes, and coordinated integration.
  - Final integration report showing what each agent handled, how conflicts were prevented, and what verification proved the results work together.
agent_behavior:
  - Prove independence before dispatching.
  - Give each agent a focused, self-contained brief instead of a shared pile of context.
  - Review and integrate results centrally rather than trusting concurrent changes blindly.
safety:
  - Do not parallelize tasks with overlapping write scopes or hidden sequential dependencies.
  - Do not confuse concurrency with reduced review or reduced verification.
status: active
version: 1.0.0
---

# Goal

Increase throughput without creating coordination chaos by dispatching only the work that is truly independent and keeping the controller responsible for task isolation and integration.

## Use It When

- There are multiple failures with different root causes.
- Separate subsystems can be investigated or implemented independently.
- Tasks can be described without requiring a shared mental model of the entire system.
- Write scopes are disjoint or the work is read-only.

## Do Not Use It When

- Fixing one problem might resolve the others.
- Tasks depend on the output of earlier tasks.
- Agents would need to edit the same files, shared configs, or shared generated artifacts.
- The real problem is still unclear and needs unified investigation first.

## Independence Test

Dispatch in parallel only if the answer is "yes" to all of these:

- Can each task be understood on its own?
- Can each task be worked without waiting on another task's result?
- Are the write scopes disjoint, or is the work read-only?
- Can the final controller integrate and verify the results coherently?

If any answer is "no," do not parallelize.

# Procedure

## 1. Group The Work By Problem Domain, Not By Convenience

Start by clustering the incoming work:

- same failing test file
- same subsystem
- same service boundary
- same user flow
- same deployment surface

Do not split work just to create more parallelism. Parallelization should follow real independence, not artificial slicing.

## 2. Reject False Independence Early

Many tasks look independent but are not.

Examples of false independence:

- multiple failing tests caused by one shared event-ordering bug
- frontend and backend work that both change the same API contract
- several bugs that all depend on understanding one shared state machine
- multiple agents editing the same refactor branch "in different parts"

If you have not inspected the dependency surface, you have not earned parallel dispatch yet.

## 3. Define One Narrow Brief Per Agent

Each agent brief should specify:

- exact scope
- exact goal
- relevant files or error output
- constraints
- prohibited scope expansion
- expected return format

Keep each brief focused on one domain. "Fix all failing tests" is not a parallel brief. "Investigate and fix `tool-approval-race-conditions.test.ts` only" is.

## 4. Separate Read-Only Parallelism From Write Parallelism

Read-only tasks are safer to parallelize:

- repo exploration
- threat modeling
- docs auditing
- competitive research
- log analysis

Write tasks need stronger isolation:

- disjoint files
- no shared generated outputs
- no dependency on another unfinished concurrent change
- no concurrent Git operations that will fight over the same state

If the write isolation is not obvious, default back to sequential execution.

## 5. Dispatch Concurrently, Coordinate Centrally

Once the tasks are proven independent:

- launch them in parallel
- keep the controller responsible for overall status
- do not redo delegated work locally while it is running
- use the waiting time for non-overlapping coordination or follow-on prep

Parallel dispatch is wasted if the controller just sits idle or duplicates agent effort.

## 6. Require Structured Returns

Each agent should return:

- what it investigated or changed
- root cause or decision reached
- files touched
- verification run
- remaining uncertainty

This gives the controller enough signal to integrate results without rereading everything from scratch.

## 7. Review For Conflicts Before Integration

Before accepting concurrent results:

- compare file touch sets
- check for semantic conflicts, not just textual ones
- verify shared interfaces still match
- reconcile assumptions that diverged across agents

Two changes can merge cleanly and still be logically incompatible.

## 8. Integrate In Dependency Order

If the outputs have any light coupling, integrate in the order that preserves stability:

- shared contracts first
- downstream consumers second
- whole-system verification last

Parallel work does not eliminate the need for ordered integration.

## 9. Run Full Verification After Integration

Always run integrated verification after the concurrent work lands together.

At minimum:

- targeted checks from each agent
- a broader suite covering shared surfaces
- build or lint if the touched surfaces require it
- spot checks for the user-visible behavior

Parallel success is not real success until the combined result passes.

## Agent Brief Template

```markdown
## Parallel Dispatch Task

- Domain:
- Goal:
- Scope:
- Relevant files or failures:
- Constraints:
- Expected output:
- Verification to run:
```

## Strong vs Weak Execution

Strong:

- proves task independence first
- gives each agent a tight scope
- keeps write scopes disjoint
- reviews summaries before integration
- runs full verification after combining results

Weak:

- parallelizes because the backlog is long
- gives vague prompts
- ignores overlapping files
- assumes clean merges mean safe merges
- forgets that integration is its own step

# Success Criteria

- Only genuinely independent tasks were parallelized.
- Each agent had a focused, self-contained brief.
- Concurrent work did not collide in file scope or semantic assumptions.
- The controller integrated results intentionally and ran combined verification.
- Overall throughput improved without reducing correctness or review discipline.

# Common Failure Modes

- Treating different symptoms as different root causes without checking shared dependencies.
- Sending multiple agents into overlapping write scopes.
- Writing prompts that are too broad for agents to stay focused.
- Accepting agent summaries without checking how their changes interact.
- Skipping full-suite or cross-surface verification after integrating concurrent work.
- Using parallelism while the real need is better decomposition or better planning.

# Example Prompt

"Use `parallel-agent-dispatch` on these failures. First prove which domains are actually independent, then create one narrow brief per domain, dispatch only the disjoint work in parallel, integrate the results centrally, and run combined verification before declaring success."
