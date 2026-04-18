---
slug: product-requirements
title: Product Requirements
summary: Turn user and business need into a decision-grade opportunity assessment and PRD with explicit goals, non-goals, evidence, risks, and launch intent.
tags:
  - product
  - requirements
  - strategy
triggers:
  - A team needs to define what should be built and why before design or implementation begins.
  - Stakeholder requests, market opportunities, or user pain need to be translated into a reviewable product artifact.
inputs:
  - Problem statement, user evidence, business context, and current product constraints.
  - Access to stakeholder goals, available research, and technical dependency awareness.
outputs:
  - Opportunity assessment and PRD that define scope, success metrics, non-goals, risks, and launch intent.
  - Clear build, explore, defer, or kill recommendation with documented reasoning.
agent_behavior:
  - Lead with the problem and evidence, not the requested feature.
  - Make trade-offs and non-goals explicit before solution detail expands.
  - Align business, user, and technical reality in one artifact.
safety:
  - Do not write requirements around an unvalidated solution request without exposing the underlying problem.
  - Do not hide open questions, timeline risk, or dependency risk behind polished prose.
status: active
version: 1.0.0
---

# Goal

Define the right work before teams commit delivery effort by producing a product artifact that makes the problem, value, scope, constraints, and success conditions explicit.

## Use It When

- A feature or initiative needs definition before design or engineering begins.
- Stakeholders have proposed solutions that still need problem validation.
- A team needs a durable artifact to align engineering, design, marketing, and operations.

## Do Not Use It When

- The need is sprint-level task shaping after scope is already approved. Use `sprint-prioritization`.
- The question is still exploratory market or voice-of-customer research. Use `trend-research` or `feedback-synthesis` first if evidence is missing.
- The work is a tiny implementation detail that does not warrant a PRD-grade artifact.

## Core Rule

The feature request is not the requirement. The requirement is the problem, the desired outcome, and the conditions under which a specific solution is worth building.

# Procedure

## 1. Start With The Problem, Not The Requested Solution

Clarify:

- what pain or opportunity exists
- who experiences it
- how often it occurs
- what it costs the user or business if ignored

Ask "why" until the requested feature resolves into a real problem statement. If that never happens, the request is probably weak.

## 2. Gather Evidence Before Solution Framing

Use the strongest available inputs:

- user interviews
- support tickets
- analytics or funnel data
- churn or retention signals
- competitive pressure
- strategic company goals

If the evidence is thin, say so. Requirements written on top of unexamined assumptions are fragile from day one.

## 3. Write An Opportunity Assessment Before The Full PRD

Capture:

- why now
- evidence of user need
- business case
- rough effort signal
- options considered
- recommendation: build, explore further, defer, or kill

This is the decision gate. It prevents teams from spending PRD energy on initiatives that should not advance.

## 4. State Goals And Non-Goals Explicitly

For any initiative that survives the opportunity gate, define:

- primary goal
- supporting metrics
- baseline
- target
- measurement window
- explicit non-goals for this iteration

Non-goals are not a courtesy section. They are one of the main tools for protecting scope.

## 5. Define The User And The Job To Be Done

Document:

- primary persona or user segment
- main job to be done
- user stories or scenarios
- acceptance criteria for the core flows
- relevant edge cases and failure behavior

If a user story cannot be paired with observable success criteria, it is not ready.

## 6. Write The Solution Overview Without Pretending It Is Final Design

Describe:

- the intended product behavior
- major interaction or flow changes
- key design decisions already made
- material trade-offs and deferred elements

Do not harden speculative implementation detail into requirement text. The PRD should guide design and engineering, not impersonate them.

## 7. Add Technical And Delivery Reality Early

Include:

- dependencies
- open questions
- known risks
- regulatory or operational constraints
- launch assumptions
- rollback triggers

This is where product requirements stay honest. A product doc that ignores delivery constraints is just persuasive fiction.

## 8. Write The Launch Intent Before The Team Builds

At minimum define:

- rollout shape
- target audience
- success gates
- monitoring or anomaly thresholds
- support readiness
- rollback criteria

If launch thinking only starts at the end, important scope will show up too late.

## 9. Run The Anti-Rationalization Review

Before approval, ask:

- are we solving a validated problem or satisfying a loud request?
- did we write down what we are not building?
- is success measurable?
- are the major risks visible?
- would engineering and design know where ambiguity still exists?

If the answer is no, the requirements are not done.

## 10. End With A Clear Recommendation And Next Step

Close the artifact with:

- recommendation
- confidence level
- required sign-offs
- immediate next step

Possible next steps:

- move to `design-before-build`
- gather more evidence through `feedback-synthesis`
- validate external demand through `trend-research`
- defer with revisit conditions

## Product Requirements Review Template

```markdown
## Product Requirements Review

- Problem statement:
- Evidence quality:
- Recommendation:
- Primary metric:
- Non-goals:
- Major risks:
- Next step:
```

## Strong vs Weak Execution

Strong:

- exposes the real problem beneath feature requests
- grounds the doc in evidence
- names non-goals and trade-offs
- includes open questions and dependency risk
- gives a real build or no-build recommendation

Weak:

- writes polished solution prose without proving the need
- treats stakeholder preference as user evidence
- omits non-goals
- ignores launch and rollback thinking
- calls the document done while material unknowns stay hidden

# Success Criteria

- The artifact explains why the work matters, to whom, and under what evidence.
- Goals, metrics, and non-goals are explicit.
- Risks, dependencies, and launch assumptions are visible.
- The recommendation is clear enough to guide a build, defer, or kill decision.
- Downstream teams can use the document without inventing the product intent themselves.

# Common Failure Modes

- Starting from a feature request and never surfacing the underlying problem.
- Using weak anecdotes as if they were validated demand.
- Writing goals without baselines or measurement windows.
- Omitting non-goals, which guarantees scope creep later.
- Hiding technical or regulatory constraints until implementation starts.
- Treating the PRD as final design instead of a decision-grade product definition.

# Example Prompt

"Use `product-requirements` on this initiative. Start with the underlying problem, gather and weigh the available evidence, produce an opportunity assessment and PRD with goals and non-goals, expose the main risks and dependencies, and end with a clear build, explore, defer, or kill recommendation."
