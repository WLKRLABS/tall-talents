---
slug: feedback-synthesis
title: Feedback Synthesis
summary: Convert raw user feedback into decision-grade evidence by collecting, normalizing, coding, quantifying, and prioritizing themes without losing the original user voice.
tags:
  - research
  - feedback
  - product
triggers:
  - Product, support, or leadership needs actionable insight from multi-channel user feedback.
  - Raw comments, tickets, interviews, reviews, or community posts must be turned into prioritized themes and recommendations.
inputs:
  - Feedback sources such as interviews, support tickets, surveys, reviews, forums, or usage-adjacent notes.
  - The product question being answered, target segment, and any known business constraints.
outputs:
  - Synthesized themes, evidence-backed priorities, and recommended actions tied to user and business impact.
  - Traceable supporting evidence including representative quotes, source mix, and confidence notes.
agent_behavior:
  - Preserve the user's meaning while reducing noise and duplication.
  - Separate volume, severity, sentiment, and business importance instead of collapsing them into one score.
  - Keep a clear chain from raw signal to recommendation.
safety:
  - Do not let a loud anecdote stand in for a pattern without labeling it as such.
  - Do not strip away the original user voice so completely that the recommendation becomes untraceable.
status: active
version: 1.0.0
---

# Goal

Turn messy, multi-source feedback into something a product team can actually decide from while preserving enough traceability that the output remains trustworthy.

## Use It When

- A team has accumulated feedback across several channels and needs synthesis.
- Product prioritization needs user evidence, not just isolated quotes.
- Leadership wants to understand pain points, request patterns, or churn signals.

## Do Not Use It When

- There is no real feedback corpus yet. In that case produce a collection plan, not fake synthesis.
- The question is about external market movement rather than existing user voice. Use `trend-research`.
- A single support ticket or interview is being reviewed in isolation.

## Core Rule

Feedback synthesis is not counting comments. It is identifying patterns, weighting them honestly, and translating them into decisions without erasing the evidence.

# Procedure

## 1. Define The Question Before Reading Everything

State what the synthesis is trying to answer:

- what pain is most urgent?
- what request patterns justify roadmap consideration?
- what is driving dissatisfaction or churn?
- how do segments differ?

Without a question, feedback synthesis becomes an unbounded summary exercise.

## 2. Gather Inputs And Record Source Quality

For each source, note:

- source type
- time window
- segment represented
- sample size or volume
- bias risk
- freshness

Examples of source types:

- interviews
- support tickets
- surveys
- reviews
- community discussion
- success or churn notes

Not all sources deserve equal weight. Record why.

## 3. Clean And Normalize The Corpus

Before coding themes:

- remove duplicates
- separate merged issues
- normalize obvious wording variants
- preserve original wording for representative quotes
- tag each item with source and segment metadata

Normalization should reduce noise, not flatten meaning.

## 4. Code Themes And Sub-Themes

Group the corpus by:

- recurring pain points
- desired outcomes
- request type
- emotional tone
- workflow stage
- affected persona or segment

Use consistent labels. If the same problem appears under five names, your synthesis will dilute it artificially.

## 5. Quantify Without Pretending To Be More Certain Than You Are

For each theme assess separately:

- frequency
- segment concentration
- severity of pain
- strategic importance
- confidence in the pattern

Volume alone is not priority. A smaller theme may matter more if it drives churn, blocks adoption, or affects a high-value segment.

## 6. Preserve Representative User Voice

Attach evidence such as:

- direct quotes
- example tickets
- recurring wording
- notable outliers

The quotes should sharpen the theme, not replace analysis. Use them to show texture, emotional intensity, or nuance that scoring alone would hide.

## 7. Translate Themes Into Product-Relevant Recommendations

Each theme should end with a decision-grade interpretation:

- build now
- explore further
- improve docs or onboarding
- instrument and monitor
- defer
- reject

Tie the recommendation to:

- user impact
- business impact
- confidence
- likely effort or dependency surface

## 8. Flag The Limits Of The Data

State when:

- the sample is skewed
- one segment dominates the corpus
- the time window is stale
- the data is mostly request phrasing, not observed behavior
- a theme is emerging but under-evidenced

Weak evidence can still be useful, but only if labeled honestly.

## 9. Produce A Synthesis Report That Teams Can Act On

Include:

- top themes
- affected segments
- evidence summary
- representative quotes
- confidence
- recommendation
- unresolved questions

This output should plug directly into `product-requirements` or `sprint-prioritization`.

## Feedback Synthesis Template

```markdown
## Feedback Theme

- Theme:
- Sources:
- Affected segment:
- Frequency:
- Severity:
- Representative quote:
- Recommendation:
- Confidence:
```

## Strong vs Weak Execution

Strong:

- defines the decision question first
- records source quality
- separates frequency from importance
- preserves representative voice
- turns themes into explicit recommendations

Weak:

- dumps quotes into buckets with no weighting
- treats all channels as equally reliable
- lets loud anecdotes dominate the output
- strips away evidence until the conclusions look unsupported
- ends with "interesting insights" instead of decisions

# Success Criteria

- Raw feedback was normalized and coded into clear themes.
- The output preserves traceability from recommendation back to evidence.
- Priority reflects severity, segment impact, and business context, not just volume.
- Confidence and limitations are visible.
- The synthesis is usable by product and delivery teams as decision input.

# Common Failure Modes

- Starting synthesis without a decision question.
- Letting duplicate feedback inflate importance.
- Collapsing sentiment, volume, and business impact into one vague priority label.
- Overgeneralizing from a small or biased sample.
- Using quotes as decoration instead of evidence.
- Ending with themes but no product interpretation or next step.

# Example Prompt

"Use `feedback-synthesis` on this multi-channel feedback corpus. Define the decision question first, normalize and code the feedback, separate frequency from severity and business importance, preserve representative quotes, and end with evidence-backed recommendations plus confidence notes."
