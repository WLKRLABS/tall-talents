---
slug: automation-governance
title: Automation Governance
summary: Decide whether automation should exist at all, choose the right rollout posture, and require reliability, fallback, ownership, and audit standards before approval.
tags:
  - governance
  - automation
  - risk
triggers:
  - A team is proposing to automate a recurring business or operational process.
  - An integration chain, workflow engine, or agent loop needs a go, pilot, partial, or reject decision.
  - Technical feasibility is being mistaken for sufficient justification.
inputs:
  - Current manual process, frequency, and pain points.
  - Systems involved, data criticality, dependency chain, and scale expectations.
  - Existing controls, ownership model, and operational constraints.
outputs:
  - Governance verdict with rationale.
  - Approved architecture standard and rollout guardrails when automation is justified.
  - Explicit fallback, testing, monitoring, and re-audit requirements.
agent_behavior:
  - Evaluate business value and operational risk before architecture preference.
  - Require source-of-truth clarity, ownership, and fallback design.
  - Prefer controlled partial automation over fragile full automation.
safety:
  - Do not approve automation only because it is technically possible.
  - Do not recommend uncontrolled live changes to critical flows without explicit guardrails and ownership.
status: active
version: 1.0.0
---

# Goal

Decide whether automation is worth building, how much of the process should be automated, and what controls must exist before it is safe to deploy. This talent exists to prevent low-value or high-risk automation from being shipped as if automation were inherently progress.

## Use It When

- Someone asks "should we automate this?"
- A workflow engine, integration pipeline, or agentic process is being proposed.
- Repeated manual work suggests automation, but the true risk and value are unclear.

## Do Not Use It When

- The task is plain software implementation with no automation design or governance decision.
- A simple internal script has no meaningful operational or data risk and no one is asking for a governance verdict.
- The system already has an approved automation pattern and the current work clearly falls inside it.

## Preconditions

You need the actual manual process and its operating context:

- how often it occurs
- what value or cost it carries
- which systems it touches
- what happens when it is wrong
- who owns it today

Without that, automation review turns into tool enthusiasm.

# Procedure

## 1. Summarize The Current Process Before Talking About Automation

Write down:

- process name
- business goal
- current steps
- systems involved
- frequency
- failure impact

If the manual process is still unstable or poorly understood, that is already a governance signal.

## 2. Evaluate The Four Mandatory Decision Dimensions

For every proposal, score or describe:

- `Time savings`: is the recurring savings material enough to justify automation cost
- `Data criticality`: what happens if records are wrong, duplicated, delayed, or lost
- `Dependency risk`: how many external services or unstable APIs sit in the chain
- `Scalability`: will retries, deduplication, and exception handling still work under growth

Do not substitute engineering elegance for business value.

## 3. Decide The Verdict Explicitly

Choose exactly one:

- `APPROVE`
- `APPROVE AS PILOT`
- `PARTIAL AUTOMATION ONLY`
- `DEFER`
- `REJECT`

The verdict must match the evidence. If value is plausible but uncertainty is high, pilot or partial automation is often the correct answer.

## 4. Prefer Safe Segmentation Over End-To-End Fragility

If the process mixes low-risk and high-risk steps:

- automate the safe, deterministic segments
- keep human checkpoints at irreversible or judgment-heavy steps
- ensure the handoff between automation and human review is explicit

This is usually stronger than forcing full automation for narrative neatness.

## 5. Define The Minimum Architecture Standard For Approved Work

Any production-grade automation should include these stages in some form:

1. trigger
2. input validation
3. normalization or enrichment
4. business logic
5. external actions
6. result validation
7. logging and audit trail
8. error branch
9. fallback or manual recovery
10. completion or status writeback

No uncontrolled sprawl, no hidden side paths, and no silent failure sinkholes.

## 6. Require Reliability Baselines

Approved automation should define:

- idempotency or duplicate protection where relevant
- retry behavior with stop conditions
- timeout handling
- alerting or notification behavior
- manual fallback path
- rollback or compensating action where applicable

If the process cannot tolerate duplicate execution, say how duplicates are prevented.

## 7. Require Logging And Audit Baselines

At minimum, automation should record:

- workflow name and version
- execution time
- source system
- affected entity ID
- success or failure state
- error class and short cause

If the process touches sensitive or regulated data, the audit requirements usually need to be stricter.

## 8. Require Testing Before Production Approval

Baseline tests include:

- happy path
- invalid input
- dependency failure
- duplicate event
- fallback or recovery
- scale or repetition sanity check

If the proposal cannot support these tests, that is a governance issue, not just a QA issue.

## 9. Clarify Source Of Truth And Ownership

For every connected system, define:

- source of truth
- read and write boundaries
- auth method and token lifecycle
- rate limits and failure modes
- owner
- escalation path

No integration is well-governed until write authority and ownership are unambiguous.

## 10. Define Re-Audit Triggers Before Launch

Automation should be reviewed again when:

- schemas or APIs change
- volume changes materially
- error rate rises
- repeated manual fixes appear
- compliance obligations change

Governance is ongoing. Approval is not permanent immunity from review.

## 11. Return A Structured Verdict

```markdown
# Automation Governance Verdict

## Process Summary
- Process:
- Goal:
- Systems:
- Frequency:

## Evaluation
- Time savings:
- Data criticality:
- Dependency risk:
- Scalability:

## Verdict
- APPROVE | APPROVE AS PILOT | PARTIAL AUTOMATION ONLY | DEFER | REJECT

## Rationale
- Business value:
- Key risks:
- Why this verdict fits:

## Required Architecture
- Trigger:
- Validation:
- Logging:
- Error handling:
- Fallback:

## Preconditions And Guardrails
- Owner:
- Tests:
- Monitoring:
- Re-audit triggers:
```

# Success Criteria

- The review starts from the real process and economics, not technical excitement.
- The verdict is explicit and justified.
- Approved automation includes fallback, ownership, testing, logging, and re-audit rules.
- Partial automation is used where full automation would be fragile or unsafe.
- Source-of-truth and write authority are defined for every integrated system.

# Common Failure Modes

- Approving automation because the platform can technically do it.
- Ignoring how damaging duplicate or delayed writes would be.
- Treating dependency count as irrelevant until the first outage hits.
- Automating judgment-heavy or irreversible steps without human checkpoints.
- Launching with no owner, no monitoring, or no fallback.
- Calling a pilot "production ready" because it worked on happy-path demos.

# Example Prompt

"Use talent `automation-governance` on this proposed workflow automation. Evaluate value, data criticality, dependency risk, and scalability first, choose one verdict, and define the minimum guardrails required before any approval."
