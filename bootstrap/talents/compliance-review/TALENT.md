---
slug: compliance-review
title: Compliance Review
summary: Evaluate legal, regulatory, policy, and audit obligations against the actual product or process, classify gaps, and define the controls or escalation needed before launch.
tags:
  - compliance
  - governance
  - risk
triggers:
  - A feature, workflow, launch, or content surface may carry legal or regulatory obligations.
  - Data handling, user rights, marketing claims, or jurisdictional rollout needs a formal review.
  - A team needs to distinguish blockers from manageable compliance conditions before proceeding.
inputs:
  - Product or process scope, jurisdictions, and target users.
  - Data flows, content claims, vendor or system dependencies, and operational model.
  - Existing policies, controls, and available evidence.
outputs:
  - Compliance assessment identifying applicable obligations, gaps, blockers, and required controls.
  - Owner-tagged remediation plan and audit-trail requirements.
  - Clear statement of uncertainty and escalation needs.
agent_behavior:
  - Review the real operating model, not a vague product summary.
  - Separate confirmed obligations from assumptions and open legal questions.
  - Preserve an evidence trail for every major conclusion.
safety:
  - Do not guess on jurisdiction, policy applicability, or legal interpretation when evidence is missing.
  - Do not present this review as a substitute for licensed legal advice where formal counsel is required.
status: active
version: 1.0.0
---

# Goal

Identify the compliance obligations that actually apply, assess whether the current system or plan meets them, and define what must change before the work can safely proceed or launch.

## Use It When

- Personal data, regulated content, marketing claims, payments, health data, education data, or cross-border operations are involved.
- Launch readiness depends on more than technical correctness.
- A product or workflow change may alter consent, retention, disclosure, or user-rights obligations.

## Do Not Use It When

- The work is purely internal and carries no meaningful legal, policy, or audit exposure.
- The request is security-only and no broader compliance decision is being made.
- A binding legal interpretation is required and no qualified reviewer is involved.

## Preconditions

You need the actual operating context:

- jurisdictions
- data types
- user types
- business model
- system and vendor touchpoints
- content or claim surfaces

Without that context, a compliance review collapses into generic checklist theater.

# Procedure

## 1. Define The Review Boundary First

Write down what is being reviewed:

- feature, workflow, product, or launch slice
- in-scope jurisdictions
- in-scope systems and vendors
- in-scope data and content types
- in-scope user populations

If these are unclear, the review should pause until the operating model is concrete enough to evaluate.

## 2. Map Applicable Obligations Before Judging The Implementation

Determine which obligations are plausibly relevant:

- privacy and data protection
- consent and cookie handling
- retention and deletion
- marketing and claims
- sector-specific obligations
- accessibility commitments if they are part of the launch or procurement context
- contractual or vendor-imposed requirements

Separate:

- `confirmed applicable`
- `possibly applicable`
- `not applicable with rationale`

## 3. Map The Actual Product Or Process To Those Obligations

Review the real workflow:

- what data is collected
- where it goes
- who can access it
- how users are informed
- how requests, errors, and deletions are handled
- what third parties are involved
- what public claims are being made

Compliance review is about the real operating path, not a policy document in isolation.

## 4. Evaluate Current Controls And Evidence

For each applicable obligation, record:

- current control or implementation
- evidence that it exists and works
- control owner
- adequacy judgment

Treat missing evidence as a gap. "We probably handle that" is not a compliant state.

## 5. Classify Gaps By Decision Impact

Use practical categories:

- `Blocker`: cannot proceed or launch without remediation or explicit counsel decision
- `Pre-Launch Required`: must be fixed before release, but not necessarily a stop today
- `Monitor / Follow-Up`: lower urgency but real obligation to track
- `Open Question`: needs counsel, policy owner, or vendor clarification

This prevents medium-risk work from being buried next to true blockers.

## 6. Define Remediation As Operational Work, Not Slogans

For each gap, specify:

- required action
- owner
- deadline or gate
- evidence needed to close the issue
- whether counsel or policy approval is required

If the remediation is "update policy," say which policy, why, and what implementation must accompany it.

## 7. Preserve An Audit Trail

Document:

- source materials reviewed
- assumptions made
- unresolved questions
- rationale for applicability decisions
- evidence links or artifact locations

This is necessary both for later verification and for re-review when the product changes.

## 8. Escalate Uncertainty Instead Of Inventing Certainty

Escalation is required when:

- jurisdictional applicability is unclear
- the review turns on legal interpretation rather than operational fact
- public claims may create liability
- vendor or contractual constraints are not understood
- the cost of being wrong is materially high

The correct output in those cases is a well-scoped question and the risk of proceeding without an answer.

## 9. Re-Review At The Right Times

A compliance review is not one-and-done. Re-run or update it when:

- the data model changes
- jurisdictions expand
- vendors or processors change
- error rate or incident rate rises
- new claims or acquisition channels are added
- launch moves from internal to public use

## 10. Use A Decision-Ready Assessment Format

```markdown
# Compliance Review

## Scope
- Product or process:
- Jurisdictions:
- Data or claim surfaces:

## Applicable Obligations
| Obligation | Applicability | Rationale | Owner |
|---|---|---|---|

## Current Controls
| Obligation | Current control | Evidence | Adequate? |
|---|---|---|---|

## Gaps
1. [Severity] [Gap]
   - Why it matters:
   - Required action:
   - Owner:
   - Closure evidence:

## Verdict
- Blocked | Proceed with conditions | Low current risk

## Open Questions
- ...
```

# Success Criteria

- The review is tied to the actual product or process, not generic regulations in the abstract.
- Applicability decisions are explicit and justified.
- Gaps are classified by decision impact and assigned owners.
- Major conclusions preserve evidence and rationale.
- The review is honest about where counsel or policy ownership is still required.

# Common Failure Modes

- Listing regulations without mapping them to the real workflow.
- Skipping jurisdiction and acting as though all users are under one regime.
- Treating policy existence as evidence that the implementation satisfies it.
- Merging blockers and minor follow-ups into one undifferentiated list.
- Guessing through unresolved legal interpretation instead of escalating it.
- Declaring compliance complete when the audit trail is weak or missing.

# Example Prompt

"Use talent `compliance-review` on this launch slice. Map the real workflow to the applicable obligations, classify blockers versus follow-ups, preserve the evidence trail, and flag anything that needs formal legal review instead of guessing."
