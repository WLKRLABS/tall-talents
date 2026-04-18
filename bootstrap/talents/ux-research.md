---
slug: ux-research
title: UX Research
summary: Gather and synthesize user-behavior evidence so design and product decisions are driven by observed reality rather than internal intuition.
tags:
  - design
  - research
  - usability
triggers:
  - A user-facing decision needs evidence before design or implementation changes.
  - Usability problems, journey friction, or unmet needs must be understood rather than guessed at.
  - A redesign, workflow change, or feature prioritization effort depends on user behavior insight.
inputs:
  - Research question, decision to inform, and target user or workflow.
  - Existing product surface, analytics, interviews, support signals, or prototypes.
  - Recruiting path or explicit constraint that no direct users are available.
outputs:
  - Research plan, evidence set, findings, and prioritized recommendations.
  - Clear distinction between observation, interpretation, and proposed change.
  - Confidence level and remaining evidence gaps.
agent_behavior:
  - Start with the decision that the research must support.
  - Separate observed behavior from design recommendations.
  - Prefer direct evidence over persona theater or internal opinion.
safety:
  - Do not invent users, motivations, or journey pain points without evidence.
  - Do not present heuristic review or internal opinion as if it were primary user research.
status: active
version: 1.0.0
---

# Goal

Reduce design and product guesswork by producing credible user evidence. This talent exists to show what users are trying to do, where they fail or hesitate, and which changes are most justified by observed behavior.

## Use It When

- A user-facing workflow is being designed, revised, or debugged.
- A team needs evidence before prioritizing interface changes.
- Existing feedback is noisy and needs structured interpretation around actual tasks.

## Do Not Use It When

- The work is purely backend or operational with no user-facing decision at stake.
- The question is already answered by a recent, still-relevant research artifact.
- The request is only to design the implementation structure after the problem is already understood.

## Preconditions

You need a concrete decision to inform. "Learn more about users" is too vague. Better prompts sound like: "Why do new users abandon step two?" or "Which task is breaking down in checkout on mobile?"

# Procedure

## 1. Frame The Research Around A Real Decision

Begin with:

- the product or UX decision that needs evidence
- the user task or journey under study
- the riskiest assumptions currently being made
- what a successful outcome would clarify

Research without a decision boundary becomes a pile of anecdotes.

## 2. Choose The Right Method Instead Of Defaulting To One

Pick methods based on what needs to be learned:

- interviews for motivations, language, and task context
- usability tests for observed task breakdowns
- surveys for lightweight directional quantification
- analytics review for behavior at scale
- heuristic review only when direct user access is not possible

If you must fall back to heuristic review or internal proxies, label the confidence drop explicitly.

## 3. Define Participants And Sampling Logic

Write down:

- who counts as an in-scope user
- relevant segments
- sample size and why it is enough for the current decision
- exclusion criteria that prevent misleading results

Do not create personas first and then recruit to match the fiction. Recruit from the actual problem space.

## 4. Prepare The Study To Reduce Bias

For interviews or usability work, create:

- a moderation guide
- realistic task scenarios
- success criteria per task
- note-taking structure
- consent and recording plan where applicable

Questions should uncover behavior, not coach the participant toward your preferred answer.

## 5. Collect Evidence In A Structured Way

During execution, capture:

- direct quotes
- task success or failure
- error patterns
- hesitation points
- workarounds
- emotional signals where they materially affect the task
- relevant analytics or behavioral traces

Do not summarize mid-session into premature conclusions. Capture the raw signal first.

## 6. Separate Observation From Interpretation

When synthesizing, keep three layers distinct:

- `Observation`: what the participant did or said
- `Interpretation`: what pattern that suggests
- `Recommendation`: what change is most justified by the pattern

Collapsing these into one sentence makes weak research sound stronger than it is.

## 7. Synthesize By Frequency, Severity, And Decision Impact

Organize findings around:

- how often the issue appears
- how much it blocks or degrades the task
- which user segments it affects
- how directly it influences the decision you set out to make

One vivid quote may be useful, but one quote is not a durable priority on its own.

## 8. Only Create Personas Or Journey Maps When The Evidence Supports Them

These artifacts are useful only if they compress real evidence. If you lack enough data, do not manufacture them for presentation polish.

When justified, keep them grounded in:

- observed goals
- repeated constraints
- recurring behaviors
- evidence sources and sample size

## 9. Turn Findings Into Decision-Ready Recommendations

Recommendations should be:

- clearly tied to evidence
- scoped to the actual problem
- prioritized by user impact and confidence
- explicit about what still needs validation

Avoid recommendations that silently expand the product or redesign the whole experience unless the evidence truly points there.

## 10. Report Confidence And Gaps Honestly

The final artifact should say:

- what is strongly supported
- what is directional but weakly supported
- what remains unknown
- what follow-up research would most reduce uncertainty

This keeps the research useful instead of falsely authoritative.

## 11. Use A Deliverable Structure That Preserves Evidence

```markdown
# UX Research Findings

## Decision To Inform
- Product or UX decision:
- Workflow studied:
- Key assumptions tested:

## Methods And Participants
- Methods:
- Sample:
- Evidence sources:
- Confidence limits:

## Findings
1. [Finding]
   - Observation:
   - Evidence:
   - Impact on task:
   - Confidence:

## Recommendations
1. [Priority] [Action]
   - Supported by:
   - Expected user impact:
   - Follow-up validation:

## Open Questions
- ...
```

# Success Criteria

- The research starts from a real decision, not generic curiosity.
- Methods match the question instead of being chosen by habit.
- Observations, interpretations, and recommendations stay distinct.
- Findings are prioritized by impact and evidence strength.
- The report states confidence and gaps plainly.

# Common Failure Modes

- Starting with personas or solutions instead of the decision to inform.
- Asking leading questions that produce agreement instead of insight.
- Treating a heuristic review as equivalent to direct user evidence.
- Converting one vivid anecdote into a global product priority.
- Writing recommendations that are detached from the evidence.
- Hiding weak confidence behind polished slides or research jargon.

# Example Prompt

"Use talent `ux-research` to understand why this user flow is underperforming. Define the decision first, choose the right methods, keep observations separate from recommendations, and return a findings report with explicit confidence levels."
