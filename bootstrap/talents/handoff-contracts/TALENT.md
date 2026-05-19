---
slug: handoff-contracts
title: Handoff Contracts
summary: Standardize task, QA, escalation, and phase-transition handoffs so context, evidence, and next-owner expectations survive the transfer.
tags:
  - coordination
  - handoff
  - workflow
triggers:
  - Work moves between agents, engineers, teams, or phases.
  - QA must return a pass or fail verdict that another owner will act on.
  - Repeated retries or phase gates require structured escalation and decision capture.
inputs:
  - Current task state, owner, next owner, relevant files, constraints, and evidence.
  - Acceptance criteria, retry count, and any blocking risks or decisions.
  - For system or service boundaries, payload and failure-handling expectations.
outputs:
  - Structured handoff document, QA verdict, escalation report, or phase-gate package.
  - Clear next action, evidence package, and decision boundary for the recipient.
agent_behavior:
  - Treat every handoff as a contract, not a casual summary.
  - Carry forward evidence, acceptance criteria, and constraints explicitly.
  - Make failure-handling and retry expectations actionable instead of vague.
safety:
  - Do not hand off work with missing acceptance criteria, missing evidence expectations, or undefined next-owner responsibility.
  - Do not collapse multiple unrelated workflows into one handoff package.
status: active
version: 1.0.0
---

# Goal

Prevent context loss, ambiguous QA loops, and ownerless escalations by making every transfer explicit about state, evidence, expectations, and what happens next. This talent exists because most multi-step execution failures come from incomplete handoffs rather than missing effort.

## Use It When

- one agent or engineer hands work to another
- QA returns pass or fail feedback
- a task has repeated failed attempts and needs escalation
- a project crosses a phase gate or milestone boundary
- a workflow includes a system-to-system or service-to-service handoff that must be defined precisely

## Do Not Use It When

- the work remains in one uninterrupted owner loop with no transfer boundary
- the handoff is purely conversational and no durable artifact or decision depends on it

# Procedure

## 1. Choose The Handoff Type

Use the smallest contract that fits the transfer:

- standard task handoff
- QA pass
- QA fail
- escalation after retries
- phase gate transition
- system or service boundary contract

Do not force every transfer into one oversized template.

## 2. Gather The Minimum Required Facts

Every handoff needs these questions answered:

- who is handing off
- who receives it
- what exact task or phase boundary this is
- what state the work is currently in
- which files, artifacts, or reports matter
- what acceptance criteria define done
- what evidence proves the current state
- what the next owner must do next
- what risks or constraints travel with the work

If any of these are missing, the handoff is incomplete.

## 3. Build The Standard Task Handoff

Use this for normal owner-to-owner transfer:

```markdown
## Handoff Document

### Metadata
- From: [owner]
- To: [owner]
- Phase or workstream: [name]
- Task reference: [id or description]
- Priority: [critical | high | medium | low]
- Timestamp: [ISO 8601]

### Context
- Current state: [specific progress]
- Relevant files:
  - [path] - [why it matters]
- Dependencies: [completed work this depends on]
- Constraints: [technical, timeline, policy]

### Deliverable Request
- What is needed: [specific measurable outcome]
- Acceptance criteria:
  - [criterion]
- Reference materials:
  - [spec, plan, ticket, report]

### Quality Expectations
- Must pass: [checks]
- Evidence required: [proof of completion]
- Next handoff: [who receives it after this]
```

The recipient should be able to start work without asking, "What exactly do you want from me?"

## 4. Use Explicit QA Verdict Contracts

### QA Pass

A pass handoff must include:

- task identity
- who built it
- who verified it
- attempt count
- evidence package
- acceptance criteria that passed
- next action

Pass is not "looks good." Pass means the required evidence is attached and the next owner can rely on it.

### QA Fail

A fail handoff must be actionable.

For each issue include:

- category and severity
- exact problem description
- expected behavior
- actual behavior
- evidence reference
- specific fix instruction
- exact file or area to change

Also include:

- which acceptance criteria passed
- which failed
- retry number
- instruction to fix only the listed issues unless the scope is explicitly widened

This prevents rejected work from bouncing back as a vague "still broken" loop.

## 5. Escalate With Failure History, Not Frustration

Escalation begins when retries are exhausted or the path is blocked by decision-level conflict.

An escalation report must contain:

- attempts exhausted and who made them
- summary of each attempt
- root cause analysis
- whether the problem is scoping, approach, missing information, or systemic failure
- recommended resolution options
- impact on blocked tasks, timeline, and quality
- the decision required and who must make it

Escalation is not a longer complaint. It is a decision packet.

## 6. Carry Phase Gates Forward Explicitly

For phase or milestone transitions, capture:

- from phase and to phase
- gate keepers
- pass or fail result
- gate criteria with evidence
- documents carried forward
- constraints for the next phase
- risks carried forward with owners

This keeps the next phase from rediscovering old constraints or assuming the gate was cleaner than it was.

## 7. Define System Boundary Contracts When A Handoff Is Technical

When one service, agent, or system hands work to another, define the contract itself:

```markdown
HANDOFF: [from] -> [to]
- Payload: { field: type }
- Success response: { field: type }
- Failure response: { error: string, code: string, retryable: bool }
- Timeout: [duration]
- On failure: [recovery action]
```

Do not leave payload shape, failure shape, timeout behavior, or recovery implicit.

## 8. Keep Handoffs Narrow And Durable

Rules:

- one workflow or task boundary per handoff
- do not bundle unrelated work because the same people are involved
- if assumptions were made and not verified, list them explicitly
- if reality diverges from the prior spec, note the divergence in the handoff rather than hiding it

## Output Shapes

Default QA fail fragment:

```markdown
## QA Verdict: FAIL
- Issue: [category] - [severity]
- Expected: [...]
- Actual: [...]
- Evidence: [...]
- Fix instruction: [...]
- Files to modify: [...]
- Retry count: [n of max]
```

Default escalation fragment:

```markdown
## Escalation Report
- Attempts exhausted: [count]
- Root cause: [...]
- Recommended resolution:
  - [option]
- Impact:
  - [blocking item]
- Decision required: [who decides what]
```

## Integration Notes

- Pair with `workflow-orchestration` or `parallel-agent-dispatch` when multiple owners are active.
- Pair with `review-feedback-triage` when QA fail handoffs come back as implementation feedback.
- Pair with `release-readiness-audit` for production gate packages.

# Success Criteria

- The next owner knows exactly what to do, what proves success, and what constraints apply.
- QA fail handoffs contain actionable issue-by-issue instructions and evidence.
- Escalations preserve attempt history and required decisions.
- Phase transitions carry forward real risks, evidence, and gate results.
- Technical handoffs define payloads, failures, timeouts, and recovery behavior explicitly.

# Common Failure Modes

- Handing off work with no measurable acceptance criteria.
- Calling something a pass or fail without the evidence package.
- Returning vague QA feedback that forces the implementer to rediscover the problem.
- Escalating without summarizing previous attempts and root cause.
- Bundling unrelated work under one handoff because it feels convenient.
- Leaving technical boundary contracts implicit.

# Example Prompt

"Use `handoff-contracts` for this multi-owner workflow. Produce the right transfer format for the boundary, include evidence and acceptance criteria, and make the next owner's job explicit instead of implied."
