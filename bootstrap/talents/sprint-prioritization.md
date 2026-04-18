---
slug: sprint-prioritization
title: Sprint Prioritization
summary: Choose the right sprint work and shape it into realistic, verifiable tasks using explicit prioritization, capacity, dependency, and scope-control rules.
tags:
  - product
  - planning
  - delivery
triggers:
  - A backlog must be prioritized into a realistic sprint or delivery slice.
  - Requirements need to be turned into executable, acceptance-driven tasks with capacity and dependency awareness.
inputs:
  - Backlog items, current goals, constraints, team capacity, and relevant requirement sources.
  - Historical delivery data or informed capacity assumptions when available.
outputs:
  - Prioritized sprint plan with goal, selected work, dependencies, risks, and acceptance-driven task breakdowns.
  - Clear record of what was excluded, deferred, or protected by buffer.
agent_behavior:
  - Quote exact requirement sources instead of paraphrasing them into larger scope.
  - Optimize for realistic delivery, not aspirational backlog clearing.
  - Protect the sprint from hidden dependencies and mid-sprint scope drift.
safety:
  - Do not add luxury scope or speculative polish that was not requested.
  - Do not commit more work than capacity and dependency reality can support.
status: active
version: 1.0.0
---

# Goal

Turn a backlog into a sprint plan that maximizes value while staying believable, testable, and resilient to the usual failure modes of overcommitment and vague task shaping.

## Use It When

- A team needs to decide what fits in the next sprint or delivery window.
- Backlog items need comparable scoring and realistic decomposition.
- Stakeholders need a documented rationale for why some work is in and some work is out.

## Do Not Use It When

- Product intent is still undefined. Use `product-requirements` first.
- The work is a single small change that does not need sprint-level coordination.
- The team lacks even minimal requirement inputs and would just be guessing in calendar form.

## Sprint Rule

A sprint is not a wish list. It is a constrained commitment backed by capacity, dependencies, and acceptance criteria.

# Procedure

## 1. Re-Read The Actual Requirement Sources

For each candidate item, inspect the real source:

- PRD
- opportunity assessment
- bug report
- support escalation
- release blocker
- stakeholder decision log

Quote the requirement exactly where it matters. Do not let backlog shorthand mutate the scope.

## 2. Normalize Candidate Work Into Comparable Units

Each candidate should state:

- user or business outcome
- acceptance criteria
- dependency surface
- estimated effort or size
- risk level
- owner or likely execution team

If an item cannot be normalized, it is not sprint-ready.

## 3. Score Priority Explicitly

Use a prioritization framework that fits the moment:

- RICE when reach and impact are estimable
- value vs effort when speed matters and data is lighter
- Kano or must-have framing when baseline expectations dominate

The point is not to fetishize a formula. The point is to force trade-offs into the open.

## 4. Account For Capacity Like An Adult

Estimate available capacity using:

- historical velocity when trustworthy
- vacations and meeting overhead
- onboarding or context-switch tax
- shared support or incident burden
- a deliberate uncertainty buffer

Do not schedule 100% of theoretical capacity. Leave room for reality.

## 5. Map Dependencies Before Commitment

For each selected item, identify:

- prerequisite decisions
- upstream teams or services
- design or content inputs
- external APIs or vendors
- sequencing constraints inside the sprint

An item that depends on unfinished or unowned inputs is either a risk call or not actually ready.

## 6. Shape Selected Work Into Real Tasks

Break chosen items into tasks that are:

- small enough to complete and review cleanly
- tied to acceptance criteria
- explicit about files or surfaces touched when possible
- clear about what "done" means

A good sprint item becomes a task list.
A bad sprint item becomes a recurring standup discussion.

## 7. Define The Sprint Goal And Cut List

State:

- the sprint goal
- why these items serve that goal
- what is intentionally excluded
- what would be cut first if risk materializes

This protects the sprint from death by "just one more thing."

## 8. Lock Scope-Change Rules Before Work Starts

Decide in advance how new requests are handled:

- accepted only if they replace equal or greater effort
- deferred to backlog by default
- escalated if they are true blockers or incidents

Invisible scope creep is one of the main reasons sprint plans become fiction.

## 9. Track Risk And Reassess Mid-Sprint

During execution, monitor:

- blockers older than 24 hours
- dependency slips
- quality failures
- underestimated tasks
- capacity loss from incidents or interruptions

If the sprint needs to change, change it explicitly and document the reason.

## 10. End With Delivery Reality, Not Backlog Theater

At sprint close, report:

- committed vs delivered
- what moved out and why
- unresolved blockers
- lessons for the next prioritization pass

Feed those lessons back into future capacity estimates and task shaping.

## Sprint Prioritization Template

```markdown
## Sprint Plan

- Sprint goal:
- In scope:
- Out of scope:
- Capacity assumption:
- Highest-risk dependency:
- First cut if needed:
- Success signal:
```

## Strong vs Weak Execution

Strong:

- uses real requirement sources
- scores trade-offs explicitly
- respects capacity and dependencies
- shapes items into acceptance-driven tasks
- keeps a visible cut list

Weak:

- prioritizes from memory or stakeholder volume
- commits all available backlog value with no buffer
- ignores hidden dependency risk
- keeps tasks vague
- lets mid-sprint additions slip in without replacing anything

# Success Criteria

- The sprint goal is clear and defensible.
- Selected items fit within realistic capacity and dependency constraints.
- Each committed item has enough definition to execute and verify.
- Exclusions and cut-line logic are explicit.
- The plan reduces ambiguity instead of just renaming backlog items.

# Common Failure Modes

- Planning from backlog titles instead of actual requirements.
- Treating scoring frameworks as objective truth rather than structured judgment.
- Overcommitting because historical velocity was treated as guaranteed capacity.
- Ignoring dependency timing until the sprint is already running.
- Turning large initiatives into one-line sprint items with no task structure.
- Accepting scope creep informally because it "seems small."

# Example Prompt

"Use `sprint-prioritization` on this backlog. Re-read the actual requirement sources, score the candidates explicitly, account for real capacity and dependencies, shape the selected work into clear acceptance-driven tasks, and make the sprint cut line explicit."
