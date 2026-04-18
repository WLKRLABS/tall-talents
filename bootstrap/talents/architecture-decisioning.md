---
slug: architecture-decisioning
title: Architecture Decisioning
summary: Produce domain-first architecture decisions with explicit trade-offs, ADRs, operational implications, and a clear evolution path.
tags:
  - architecture
  - design
  - systems
triggers:
  - A project needs a material system-level decision about boundaries, patterns, data flows, or operational shape.
  - Multiple architectural approaches are viable and the trade-offs need to be made explicit before implementation.
inputs:
  - Problem statement, quality attributes, operational constraints, and current system context.
  - Relevant code, infrastructure definitions, and domain knowledge from the surrounding system.
outputs:
  - Architecture decision record and supporting rationale covering context, options, chosen approach, and consequences.
  - Clear guidance for service boundaries, data shape, API patterns, and operational concerns affected by the decision.
agent_behavior:
  - Start from domain boundaries and failure modes before choosing technology.
  - Present multiple viable options with trade-offs, not a single asserted answer.
  - Prefer maintainable, reversible decisions over theoretically impressive ones.
safety:
  - Do not recommend architecture that the current team cannot realistically operate.
  - Do not hide costs, lost flexibility, or operational burden behind generic best-practice language.
status: active
version: 1.0.0
---

# Goal

Make system-shaping decisions in a way that is explicit, reviewable, and durable enough to guide implementation without drifting into architecture theater.

## Use It When

- The team must choose between architectural patterns or boundary options.
- A change affects domain decomposition, data ownership, API shape, or system operations.
- The cost of choosing wrong is high enough that a documented decision is warranted.

## Do Not Use It When

- The work is a local bug fix or a routine implementation detail.
- The decision has already been made and the need is execution planning.
- The discussion is still at product scope and has not yet become a technical architecture question.

## Core Principles

- Domain first, technology second.
- Trade-offs over slogans.
- Reversibility over false optimality.
- Documentation of decisions, not just diagrams.
- Operational reality counts as architecture, not cleanup.

# Procedure

## 1. Clarify The Decision Boundary

State the decision in one sentence:

- what must be decided
- what is in scope
- what is explicitly out of scope
- what deadline or delivery pressure exists

Architecture work bloats quickly when the boundary is not named up front.

## 2. Discover The Domain Before Naming The Pattern

Map the domain surface:

- core entities and invariants
- important commands and events
- bounded contexts or natural modules
- ownership boundaries
- upstream and downstream relationships

If the domain is still fuzzy, do not jump to microservices, CQRS, or event-driven designs just because they sound strong.

## 3. Surface The Quality Attributes That Actually Matter

Name the forces competing in this decision:

- scalability
- reliability
- security
- maintainability
- observability
- latency
- consistency
- team autonomy
- cost
- reversibility

Not every decision optimizes every attribute. State which ones matter most and why.

## 4. Generate Real Options

Present at least two credible options and usually three when the decision is substantial.

Examples:

- modular monolith vs microservices
- synchronous API orchestration vs event-driven workflow
- CRUD model vs CQRS split
- shared database vs domain-owned data stores

For each option, state:

- when it works well
- what it makes easier
- what it makes harder
- what operational burden it adds
- what assumptions must stay true for it to keep working

## 5. Evaluate With Team And System Reality, Not Purity

Assess each option against:

- current team size and skills
- deployment maturity
- observability maturity
- rollback complexity
- data migration complexity
- incident response burden
- expected growth horizon

The best architecture is not the most sophisticated one. It is the one that survives contact with the team's actual operating constraints.

## 6. Write The ADR

Every material architecture choice should produce a short ADR:

```markdown
# ADR-00X: [Decision]

## Status
Proposed | Accepted | Deprecated | Superseded

## Context
- problem being solved
- relevant constraints
- forces in tension

## Options Considered
- option A
- option B
- option C

## Decision
- chosen approach
- why it won

## Consequences
- what becomes easier
- what becomes harder
- follow-on work required
```

Keep the ADR concrete. It should explain why this decision was made for this system, not read like a reusable blog post.

## 7. Expand The Decision Into A Buildable Shape

Where relevant, define:

- service or module boundaries
- data ownership and schema responsibilities
- interface patterns and contracts
- deployment or runtime assumptions
- reliability mechanisms
- observability requirements
- security implications

If the decision affects APIs, storage, or operations, that detail belongs in the architecture package, not in someone's head.

## 8. Name Failure Modes And Evolution Paths

Ask:

- what breaks this architecture first?
- what assumptions are most likely to stop being true?
- how would we migrate if growth or product shape changes?
- what signals would tell us to revisit the decision?

This keeps the architecture honest and prevents one-time decisions from hardening into dogma.

## 9. Review The Decision For Over-Architecture

Run an explicit check:

- is this complexity required now?
- does the team have the operational maturity to run it?
- is there a simpler option that satisfies the current need?
- are we paying cost today for speculative future scale?

If the answer points toward restraint, choose restraint and document why.

## 10. Hand Off Clearly

Close with:

- the chosen architecture direction
- exact artifacts created
- open follow-up decisions, if any
- implementation implications
- related talents to use next

Typical handoff targets:

- `security-review` for threat modeling and control validation
- `implementation-planning` for concrete delivery work
- `workflow-mapping` if the hardest part is flow complexity rather than system shape

## Strong vs Weak Execution

Strong:

- starts from domain and constraints
- names the trade-offs plainly
- produces an ADR
- includes data, API, and operational implications
- chooses what the team can actually run

Weak:

- starts with the technology pattern
- hides trade-offs behind "best practice"
- optimizes for elegance over reversibility
- ignores operational cost
- produces diagrams without decisions

# Success Criteria

- The decision boundary is explicit and bounded.
- Multiple viable options were compared with honest trade-offs.
- The chosen architecture is documented in an ADR.
- The output covers operational and data consequences, not just component names.
- The recommendation is maintainable and reversible in the current team context.

# Common Failure Modes

- Choosing a pattern before understanding the domain.
- Treating scalability as the only quality attribute that matters.
- Recommending microservices or event-driven architecture without the operational maturity to support them.
- Documenting the chosen design without recording rejected options and consequences.
- Making a "future-proof" choice that adds immediate cost for speculative benefit.
- Ignoring security and observability implications until later implementation phases.

# Example Prompt

"Use `architecture-decisioning` for this system choice. Map the domain first, surface the real quality attributes in tension, compare at least two viable options, write an ADR with consequences, and end with the implementation implications of the chosen approach."
