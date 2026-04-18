---
slug: workflow-orchestration
title: Workflow Orchestration
summary: Coordinate multi-phase delivery with explicit phase gates, retry limits, structured handoffs, and evidence-backed status reporting.
tags:
  - coordination
  - delivery
  - quality-gates
triggers:
  - Multi-phase work spans planning, build, QA, hardening, or launch-style readiness.
  - Several specialists or workstreams must move in sequence without losing state between handoffs.
  - A controller must decide when work can advance, retry, split, or stop.
inputs:
  - Approved scope, spec, or task backlog.
  - Defined or discoverable phases, owners, and verification signals.
  - Acceptance criteria for each phase boundary.
outputs:
  - Orchestration ledger with phase, task, owner, attempt, blocker, and evidence state.
  - Gate verdicts, escalation records, and structured handoff packages.
  - Honest completion or stop-state report.
agent_behavior:
  - Treat every phase boundary as a hard control point rather than a soft status update.
  - Require evidence for advancement and keep failure history visible.
  - Decompose work into controlled loops instead of letting the pipeline sprawl.
safety:
  - Do not advance a phase because the team feels close; advance only when the gate evidence exists.
  - Do not hide repeated failures inside vague progress language; surface retries, blockers, and decisions explicitly.
status: active
version: 1.0.0
---

# Goal

Run a larger delivery effort as a controlled pipeline instead of a sequence of hopeful status claims. This talent exists to keep phase boundaries explicit, preserve context across handoffs, and stop quality gates from collapsing under schedule pressure.

## Use It When

- Work naturally breaks into phases such as discovery, design, build, QA, hardening, or launch readiness.
- Multiple specialists or teams need clear sequencing, ownership, and retry rules.
- The cost of losing state between phases is high.

## Do Not Use It When

- One engineer or one agent can complete the work in a single direct loop.
- The problem is still too ambiguous to define phase outcomes or gate criteria.
- The real need is task execution, not program-level coordination.

## Preconditions

You need an approved goal, a bounded backlog or phase definition, and a believable way to verify progress. If the pipeline has no measurable gate criteria, you are not orchestrating work; you are narrating it.

# Procedure

## 1. Qualify Whether Orchestration Is Actually Needed

Start by proving the work is orchestration-sized:

- list the major delivery phases
- identify which phases can run in parallel and which must remain sequential
- name the gatekeeper or decision owner for each phase
- name the evidence required to pass each phase

If the work reduces to "implement this plan and verify it," use a simpler execution talent instead.

## 2. Define The Pipeline Before Any Work Starts

Write a compact pipeline contract before dispatching tasks:

- phase name
- purpose
- required inputs
- expected outputs
- entry criteria
- exit criteria
- gatekeeper
- fail path

Every phase needs a non-pass branch. Valid gate outcomes are usually:

- `PASS`: advance to the next phase
- `CONTINUE`: stay in the current phase because more work remains
- `RETURN`: send work back to an earlier phase with a fix list
- `ESCALATE`: stop normal flow and request a higher-level decision

## 3. Build A Control Ledger

Maintain one authoritative ledger for the whole pipeline. At minimum it should track:

- current phase
- task ID or workstream
- owner
- status
- attempt count
- last evidence
- open blockers
- next action
- escalation state

Do not rely on memory or scattered chat messages. If the state is not written down, it will drift.

## 4. Run A Phase Entry Check Before Activating Work

Before a phase starts, verify:

- all required inputs from the prior phase exist
- owners know what they are responsible for
- acceptance criteria are concrete
- the evidence collection method is known
- unresolved assumptions are logged

If those conditions are missing, the correct action is not "start anyway." The correct action is to repair the entry package.

## 5. Manage Work Inside Explicit Delivery Loops

Inside each phase, run tasks through a controlled loop:

1. assign the current task or track to the right owner
2. require implementation or analysis only for that scoped unit
3. route the result to the appropriate validator
4. capture a clear verdict with evidence
5. decide: pass, retry, decompose, reassign, defer, or escalate

For retryable task loops, set the retry limit up front. A three-attempt ceiling is a reasonable default when no better project-specific rule exists. After the limit is hit, orchestration must make a new decision instead of repeating the same failing loop.

## 6. Parallelize Only Independent Tracks

Parallel tracks are allowed only when all of the following are true:

- write scopes do not overlap materially
- the tracks do not depend on the same evolving artifact
- merge order is known
- a controller can review them independently

Parallel work without dependency discipline creates false velocity. The orchestration ledger must show which tracks are truly independent and which are waiting on a gate or dependency.

## 7. Enforce Phase Gates With Evidence, Not Optimism

At each boundary, compare actual evidence against the gate contract:

- required artifacts exist
- critical defects are resolved or consciously accepted
- acceptance criteria are met
- known risks are documented
- downstream consumers have what they need

If evidence is partial or contradictory, the gate fails. "Almost done" is not a gate outcome.

## 8. Use Structured Handoffs

Every handoff should answer the same questions:

- what state is the work in right now
- what was completed
- what evidence proves it
- what remains unresolved
- what the next owner must do
- what constraints or risks must be preserved

Use a simple handoff structure like this:

```markdown
## Handoff

### Metadata
- From:
- To:
- Phase:
- Task / Workstream:
- Priority:

### Current State
- Completed:
- Evidence:
- Relevant files or artifacts:
- Dependencies:

### Request
- Deliverable needed:
- Acceptance criteria:
- Constraints:

### Risks
- Open issues:
- Retry history:
- Escalation threshold:
```

## 9. Escalate Repeated Failure Instead Of Normalizing It

Escalation is required when:

- a task exhausts its retry budget
- a gate cannot be evaluated because evidence is missing
- two tracks conflict on scope or sequencing
- upstream assumptions collapse
- the pipeline can no longer satisfy the approved objective without scope or architecture change

An escalation record should include:

- failure history by attempt
- suspected root cause
- impact on timeline and adjacent work
- candidate resolutions
- the decision required

## 10. Report Status In A Way That Can Be Audited

Good orchestration status reporting is short, specific, and falsifiable:

- current phase
- tasks complete versus total
- tasks currently under validation
- blockers with owners
- attempt counts where relevant
- next action
- expected decision point

Status reports should never substitute adjectives for state. "Good progress" is useless; "Phase 3, task 7 of 12, second retry pending validator feedback" is useful.

## 11. Close The Pipeline Deliberately

End with a completion or stop-state report:

- what phases passed
- what work shipped or finished
- unresolved risks or deferred items
- evidence that justified the final verdict
- whether the result is ready, needs work, or is blocked

Completion is not "we ran out of obvious next steps." Completion is "the terminal verdict is supported by the gate evidence."

# Success Criteria

- Every phase has explicit entry criteria, exit criteria, and fail paths.
- Retries, blockers, and escalations are visible instead of buried.
- Parallel work is limited to independent tracks.
- Handoffs preserve the information the next owner actually needs.
- Final status claims are backed by ledger state and evidence.

# Common Failure Modes

- Starting the pipeline without defining what passes each gate.
- Treating phase boundaries as calendar milestones instead of evidence checks.
- Letting repeated task failure continue without decomposition or escalation.
- Running overlapping tracks in parallel and calling the merge damage "normal."
- Writing handoffs that say what to do next but omit what was actually proven.
- Reporting morale or effort instead of state, evidence, and remaining risk.

# Example Prompt

"Use talent `workflow-orchestration` for this multi-phase delivery effort. Define the phases and gate criteria first, build a control ledger, keep retries and escalations explicit, and do not advance any phase without the required evidence."
