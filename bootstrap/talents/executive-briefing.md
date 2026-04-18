---
slug: executive-briefing
title: Executive Briefing
summary: Turn validated findings into concise, quantified, decision-ready executive communication with explicit recommendations, owners, and timelines.
tags:
  - communication
  - executive
  - synthesis
triggers:
  - Research, audit, readiness, or risk findings need a short decision-ready summary.
  - Executives or stakeholders need to understand impact and action quickly.
  - A long body of analysis must be compressed without losing the decision signal.
inputs:
  - Validated findings, source evidence, and quantified data points.
  - Business context, audience, and decision needed.
  - Known gaps, uncertainties, and available owners or timelines.
outputs:
  - Concise executive brief with situation, findings, impact, recommendations, and next steps.
  - Explicit decision framing and quantified implications.
  - Transparent note of important data gaps or uncertainty.
agent_behavior:
  - Prioritize decision usefulness over completeness.
  - Quantify major claims or label them as unquantified risk.
  - Keep the brief short, ordered by business impact, and free of speculative filler.
safety:
  - Do not summarize unvalidated or weakly sourced findings as if they were settled facts.
  - Do not bury the actual decision, timeline, or owner inside narrative prose.
status: active
version: 1.0.0
---

# Goal

Produce a brief an executive can read quickly and act on confidently. This talent exists to compress complex material into a form that highlights the current situation, the most important findings, the business impact, the recommended actions, and the immediate decision path.

## Use It When

- Discovery, audit, compliance, readiness, or performance work needs executive synthesis.
- A leader needs a go, no-go, invest, defer, or fix-first decision summary.
- Stakeholders should not have to read the full source packet to understand the implications.

## Do Not Use It When

- The underlying findings are still too raw or unvalidated.
- The audience needs a detailed working document instead of a short decision brief.
- There is no actual decision, risk, or action to frame.

## Preconditions

You need validated findings, a known audience, and a decision context. A brief without a real decision boundary becomes informative but operationally useless.

# Procedure

## 1. Define The Decision And Audience First

Before drafting, identify:

- who will read this
- what they need to decide
- what timeframe matters
- what level of certainty they expect

The same evidence produces different briefs for a CEO, product lead, or engineering director. Choose the one you are actually writing for.

## 2. Review Source Material For Decision-Relevant Facts

Pull only what materially changes the decision:

- validated findings
- quantified deltas
- risk magnitude
- deadlines
- dependencies
- owners

Do not turn the brief into a miniature archive of the whole project.

## 3. Quantify Claims Wherever Possible

Every major finding should include one of:

- a metric
- a threshold comparison
- a time comparison
- a count
- a probability or confidence statement

If a point matters but cannot yet be quantified, name the gap explicitly instead of implying hard evidence exists.

## 4. Order Findings By Business Impact, Not By Research Sequence

Executives need the highest-consequence findings first:

- biggest risk
- biggest opportunity
- strongest blocker
- most leverage

Do not preserve the order in which you discovered things if that obscures what matters most.

## 5. Keep Situation, Findings, Impact, And Recommendations Distinct

Each section has a different job:

- `Situation`: what is happening now and why this matters
- `Findings`: the few most important evidence-backed insights
- `Impact`: what those findings mean financially, operationally, or strategically
- `Recommendations`: what to do next, by whom, and by when
- `Next steps`: immediate actions and the pending decision point

Collapsing these sections makes the brief harder to scan and easier to misread.

## 6. Make Recommendations Actionable

Recommendations should include:

- priority
- owner
- timeline
- expected result
- dependencies if they materially affect execution

"Improve onboarding" is not an executive recommendation. "Product and engineering to fix step-two abandonment within two weeks and re-measure conversion" is.

## 7. Preserve Integrity On Weak Data

If the evidence is incomplete:

- say what is known
- say what is uncertain
- say what decision can still be made despite the gap
- say what follow-up would reduce uncertainty fastest

This keeps the brief useful without overstating confidence.

## 8. Stay Short Enough To Read In One Pass

For a formal executive brief, keep it tightly bounded. A strong default shape is:

- situation overview: brief
- 3-5 findings
- business impact: brief
- 3-4 recommendations
- 2-3 immediate next steps

If the brief runs long, cut detail before cutting the decision signal.

## 9. Use A Repeatable Structure

```markdown
## 1. Situation Overview
- What is happening now
- Why it matters now
- Gap between current and desired state

## 2. Key Findings
- Finding 1 with quantified evidence
- Finding 2 with quantified evidence
- Finding 3 with quantified evidence

## 3. Business Impact
- Financial or operational effect
- Risk or opportunity magnitude
- Relevant time horizon

## 4. Recommendations
- [Priority] Action - Owner - Timeline - Expected result

## 5. Next Steps
- Immediate actions
- Decision point and deadline
```

## 10. Run A Brief-Specific QA Pass

Before finalizing, check:

- every material claim is sourced or clearly labeled uncertain
- the brief is ordered by impact
- the decision is obvious
- recommendations include owners and timelines
- the wording is factual rather than theatrical

If the brief sounds impressive but hides the actual choice, rewrite it.

# Success Criteria

- The brief is short, clear, and decision-ready.
- Major findings are quantified or explicitly labeled as uncertain.
- Recommendations include owners, timelines, and expected results.
- The audience can identify the key risk or opportunity within one read.
- The brief preserves factual integrity while compressing complexity.

# Common Failure Modes

- Dumping many findings without ranking them by impact.
- Writing a summary that never states the actual decision required.
- Using strong language without quantified support.
- Hiding ownership and timeline details in vague recommendations.
- Recycling analysis prose instead of rewriting for executive consumption.
- Pretending uncertainty is resolved because the brief needs confidence.

# Example Prompt

"Use talent `executive-briefing` on these validated findings. Produce a short executive brief ordered by business impact, quantify every major claim you can, surface the real decision, and give recommendations with owners and timelines."
