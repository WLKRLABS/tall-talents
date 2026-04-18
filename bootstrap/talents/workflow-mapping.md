---
slug: workflow-mapping
title: Workflow Mapping
summary: Discover real workflows in code and operations, map their branches, states, handoffs, and cleanup paths, and maintain a registry that stays aligned with reality.
tags:
  - architecture
  - workflow
  - specification
triggers:
  - A system flow is complex enough that happy-path understanding is not sufficient.
  - Background jobs, multi-service behavior, approvals, or state transitions need a real spec.
  - The code clearly contains workflows that are undocumented, risky, or hard to verify.
inputs:
  - Relevant routes, workers, jobs, migrations, configs, infrastructure, and existing specs.
  - Business rules, user journeys, and operational expectations.
  - Access to code or authoritative system behavior artifacts.
outputs:
  - Workflow registry and one-workflow-per-document specs with triggers, branches, states, handoffs, cleanup inventory, tests, assumptions, and audit log.
  - Gaps where workflows exist in reality but not in documentation.
  - Test-case seeds and review questions for downstream implementation or QA.
agent_behavior:
  - Discover workflows from the real system surface before writing specs.
  - Map failure branches, timing assumptions, and cleanup paths explicitly.
  - Keep the registry current as workflows are found or revised.
safety:
  - Do not write workflow specs from descriptions alone when the code or runtime behavior can be inspected.
  - Do not stop at the happy path or leave system boundaries and cleanup behavior undefined.
status: active
version: 1.0.0
---

# Goal

Expose the real behavior of a system flow so it can be built, tested, operated, and changed safely. This talent exists to prevent critical workflows from living only in scattered code, tribal memory, or partial diagrams.

## Use It When

- A workflow spans multiple steps, actors, services, or states.
- Failure handling, retries, cleanup, or handoffs are easy to miss.
- You need a spec QA can derive tests from and operators can trust.

## Do Not Use It When

- The flow is truly trivial and has no meaningful branching or cleanup behavior.
- The request is to make an architecture choice rather than document a concrete workflow.
- You do not have access to the actual code or authoritative behavior and cannot responsibly infer the path.

## Preconditions

You need the real surfaces that imply workflows:

- routes and handlers
- jobs and workers
- migrations and state enums
- scheduled tasks
- infrastructure and service config
- current specs or decision records

If a workflow already exists in code, the code outranks the meeting summary.

# Procedure

## 1. Start With Discovery, Not With Diagramming

Before writing any spec, scan the system for workflow entry points:

- request handlers and endpoints
- event consumers and message handlers
- background workers and scheduled jobs
- state transitions in code
- migrations that imply lifecycle rules
- infrastructure ordering dependencies
- config flags that change runtime behavior

A workflow you do not discover is the one most likely to fail later.

## 2. Maintain A Workflow Registry

Keep one registry that answers the system from multiple angles:

- by workflow
- by component
- by user or operator journey
- by state

The registry should also show which workflows are missing a real spec. A workflow that exists in code but has no spec is a risk item, not a documentation nicety.

## 3. Scope One Workflow Per Spec

Write one workflow per document. If a neighboring workflow appears, reference it and move on. Do not silently bundle unrelated flows because they share a component or table.

This keeps specs:

- reviewable
- testable
- ownership-friendly
- resistant to drift

## 4. Define The Core Shape Before Branching

For the selected workflow, record:

- purpose
- trigger
- actors
- prerequisites
- intended terminal states
- key artifacts or entities touched

Only then write the successful path end to end.

## 5. Branch Every Step

For each step, ask:

- what can fail here
- what is retryable
- what is permanent
- what times out
- what conflicts with concurrent execution
- what was already created that must be cleaned up

Happy-path-only workflow maps are not acceptable for production-grade work.

## 6. Define Observable State At Each Meaningful Point

For important steps and failure modes, say what each audience can observe:

- customer or end user
- operator or support staff
- database or durable state
- logs or monitoring systems

If a system state cannot be observed, note that as an operational gap.

## 7. Define Explicit Handoff Contracts

At every service or system boundary, specify:

- payload shape
- success response
- failure response
- timeout
- recovery action

If the boundary is currently implicit, call that out. Unspecified handoffs are where systems become brittle.

## 8. Write The Cleanup Inventory

List every resource the workflow creates or mutates:

- database rows
- queued jobs
- external resources
- cache entries
- notifications
- derived records

For each one, define what must happen on partial failure or abort. Cleanup is part of the workflow, not an appendix.

## 9. Derive Test Cases From The Branches

Every meaningful branch should produce at least one test case:

- happy path
- invalid input
- timeout
- dependency failure
- duplicate or conflict
- partial failure after earlier success
- cleanup failure if material

If the workflow branch has no test case, it is likely not truly specified.

## 10. Track Assumptions And Open Questions Explicitly

Whenever you cannot verify a fact from code or authoritative behavior, write it down:

- assumption
- where it was or was not verified
- risk if wrong

Untracked assumptions are deferred failures.

## 11. Keep A Spec-Versus-Reality Audit Log

When the code and the workflow spec diverge:

- note the divergence
- classify whether the spec is stale or the code is violating intent
- record the action taken

Do not allow quiet drift.

## 12. Require A Reality Check Before Approval

Before marking the workflow usable:

- compare the spec against the actual code or observed behavior
- confirm entry points, state changes, and cleanup rules
- verify that the registry references remain accurate

If the map cannot survive code review, it is not ready.

## 13. Use Build-Ready Document Structures

Registry example:

```markdown
## Workflow Registry

| Workflow | Spec | Status | Trigger | Primary actor | Last reviewed |
|---|---|---|---|---|---|
```

Workflow spec example:

```markdown
# Workflow: [Name]

## Overview
## Actors
## Prerequisites
## Trigger
## Workflow Tree
## State Transitions
## Handoff Contracts
## Cleanup Inventory
## Test Cases
## Assumptions
## Open Questions
## Spec vs Reality Audit Log
```

For each workflow step, include:

- actor
- action
- timeout if relevant
- input
- output on success
- output on failure
- observable states

# Success Criteria

- Discovery starts from real routes, jobs, config, and state surfaces.
- The registry exposes missing specs as visible gaps.
- Each workflow spec covers branches, timeouts, cleanup, and observability.
- Handoff contracts and state transitions are explicit enough for implementers and QA to use.
- Assumptions and spec drift are tracked instead of buried.

# Common Failure Modes

- Writing the workflow from a meeting summary without inspecting code.
- Mapping only the happy path.
- Leaving cleanup behavior undefined after partial success.
- Failing to note what users, operators, and logs show during key states.
- Bundling multiple workflows into one vague document.
- Treating undocumented workflows in code as acceptable until later.

# Example Prompt

"Use talent `workflow-mapping` on this system flow. Start with discovery across routes, jobs, migrations, and config, update the workflow registry, then write one workflow spec that covers branches, states, handoffs, cleanup, tests, and assumptions."
