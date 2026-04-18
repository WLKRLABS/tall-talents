---
slug: trend-research
title: Trend Research
summary: Bring outside-world evidence into product and strategy decisions through source-diverse market, competitor, technology, and timing analysis.
tags:
  - research
  - market
  - strategy
triggers:
  - A product, roadmap, or strategic decision needs validated external evidence rather than internal intuition.
  - A team must assess market timing, competitive movement, or emerging technology before committing resources.
inputs:
  - The decision question, time horizon, target market or domain, and any relevant product constraints.
  - Access to current external sources, competitor material, and internal context about what decision the research must inform.
outputs:
  - Trend research brief covering market signals, competitive dynamics, timing implications, and recommended action.
  - Evidence log with source diversity, confidence assessment, and known blind spots.
agent_behavior:
  - Gather current evidence from multiple source types before making strategic claims.
  - Separate weak signals, strong signals, and speculation.
  - Tie every research conclusion back to a concrete product or strategy decision.
safety:
  - Do not present stale, single-source, or anecdotal market claims as validated trend evidence.
  - Do not mistake tool vendor narratives or hype cycles for user demand.
status: active
version: 1.0.0
---

# Goal

Help teams make better bets by turning external market and technology noise into a structured, source-grounded view of what is changing, why it matters, and whether action is justified now.

## Use It When

- A product team needs outside-world evidence before starting a major initiative.
- Leadership wants to understand market timing, competitor pressure, or adoption trends.
- A roadmap debate depends on whether a trend is real, rising, peaking, or mostly hype.

## Do Not Use It When

- The question is about current users only. Use `feedback-synthesis`.
- The work is a local implementation or delivery decision with no external-market dependency.
- The requester only wants a quick opinion and does not care about evidence.

## Core Rule

Trend research is only useful if it changes a real decision. Research that does not affect product direction, timing, or risk is just polished curiosity.

# Procedure

## 1. Define The Decision And The Time Horizon

Start with:

- what decision this research will support
- what market or domain is in scope
- what time horizon matters: now, next 6 months, next year, longer
- what kind of answer is needed: go, no-go, monitor, defer, reposition

This keeps the research from turning into an endless market tour.

## 2. Build A Source-Diverse Evidence Set

Use multiple source types where possible:

- competitors and adjacent products
- analyst or industry reports
- search and social trend signals
- funding or investment movement
- community or developer discussion
- regulatory or standards changes
- technology adoption evidence

For major decisions, aim for broad source diversity rather than many copies of the same narrative.

## 3. Separate Signals By Strength

Classify evidence as:

- weak signal: interesting but early or noisy
- moderate signal: repeated across multiple credible sources
- strong signal: validated by several independent sources and visible in real market movement

This prevents early-hype evidence from being treated like established demand.

## 4. Analyze The Trend In Context

For each major signal, ask:

- what is driving it?
- who benefits if it continues?
- who is overreacting to it?
- what adoption phase is it in?
- what barriers could slow or reverse it?

Trend research without context turns into buzzword reporting.

## 5. Map Competitive And Substitution Pressure

Look at:

- direct competitors
- indirect substitutes
- new entrants
- enabling infrastructure providers
- do-nothing alternatives users still tolerate

The competitive picture should explain not just who exists, but how the decision space is changing.

## 6. Quantify The Opportunity Carefully

When relevant, estimate:

- TAM, SAM, SOM
- reachable segment size
- likely adoption window
- urgency of entry
- downside risk of delay

Treat these numbers as decision aids, not false precision. Show the method and confidence level.

## 7. Turn Research Into Actionable Recommendation

End with a recommendation such as:

- build now
- run targeted discovery
- monitor specific signals
- reposition the concept
- defer
- kill

Pair the recommendation with:

- why now or why not now
- what would change the answer
- what follow-on work should happen next

Typical next steps:

- `product-requirements` for initiative definition
- `feedback-synthesis` to validate with existing user voice
- `executive-briefing` when the main need is leadership communication

## 8. Keep A Research Evidence Log

Record:

- source
- date
- signal type
- reliability assessment
- conclusion supported

This makes future updates faster and keeps the research falsifiable.

## Trend Research Brief Template

```markdown
## Trend Research Brief

- Decision:
- Time horizon:
- Strong signals:
- Weak signals worth monitoring:
- Competitive implication:
- Timing recommendation:
- Confidence:
- Next step:
```

## Strong vs Weak Execution

Strong:

- starts from a real decision
- uses diverse, current sources
- distinguishes validated movement from hype
- ties market evidence to timing and product implications
- records confidence and blind spots

Weak:

- gathers interesting links with no decision frame
- relies on one report or one tool vendor narrative
- treats attention as adoption
- ignores competitor and substitution context
- ends with generic "the market is growing" language

# Success Criteria

- The research answers a concrete strategic or product decision.
- Evidence comes from multiple current source types.
- Signal strength and confidence are explicit.
- Competitive, timing, and adoption implications are clear.
- The result leads cleanly into a product, strategy, or delivery next step.

# Common Failure Modes

- Starting broad and never narrowing to the actual decision.
- Confusing social attention or funding hype with durable user demand.
- Overweighting one prestigious source instead of checking cross-source agreement.
- Reporting market size without showing why the team could realistically capture it.
- Treating weak signals as justification for immediate major investment.
- Ending with observations instead of a recommendation and decision trigger.

# Example Prompt

"Use `trend-research` on this market question. Define the decision and time horizon first, gather current evidence from multiple source types, separate strong signals from hype, map the competitive and timing implications, and end with a clear build, monitor, defer, or kill recommendation plus confidence notes."
