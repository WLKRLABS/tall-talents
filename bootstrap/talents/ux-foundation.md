---
slug: ux-foundation
title: UX Foundation
summary: Translate approved scope and user evidence into implementation-ready interface structure, component boundaries, and interaction rules before polish work begins.
tags:
  - design
  - ux
  - foundation
triggers:
  - A frontend or product surface needs structural guidance before implementation.
  - Approved scope exists, but layout, hierarchy, states, and component boundaries are still too fuzzy for clean build work.
  - A team needs developer-ready interface foundations instead of moodboard-level direction.
inputs:
  - Approved scope, product goals, and any existing UX research.
  - Current interface patterns, technical constraints, and accessibility requirements.
  - Primary user tasks and content hierarchy.
outputs:
  - UX foundation document covering information architecture, layout rules, component families, state model, and implementation guidance.
  - Clear structural constraints for frontend implementation.
  - Explicit UX risks, assumptions, and deferred polish work.
agent_behavior:
  - Structure before polish and boundaries before decoration.
  - Carry research signals into layout and interaction decisions.
  - Optimize for implementer clarity as much as for user coherence.
safety:
  - Do not invent a full redesign when the need is only a structural foundation.
  - Do not assume features such as theming, animation, or design-system breadth unless the scope supports them.
status: active
version: 1.0.0
---

# Goal

Create the interface foundation that implementers can build against confidently. This talent exists to turn product intent and research into clear structure: page hierarchy, component families, state handling, responsive rules, accessibility baseline, and interaction expectations.

## Use It When

- The product direction is known, but the interface structure is not yet build-ready.
- Frontend work risks fragmentation because layout and component boundaries are still ambiguous.
- A major UI slice needs coherent foundations before detailed implementation.

## Do Not Use It When

- The work is a tiny visual tweak on an already-established system.
- The problem is still at the discovery stage and user needs are not yet understood.
- The task is pure engineering implementation of an already-documented UI foundation.

## Preconditions

You need approved scope. If the underlying product or UX decision is still unsettled, return to research or design approval first. A shaky premise produces a polished but unstable foundation.

# Procedure

## 1. Ingest The Inputs That Should Drive Structure

Collect the sources that matter:

- approved product or design scope
- user research findings, if available
- existing design-system or codebase constraints
- accessibility requirements
- performance constraints for the surface

Foundations that ignore real constraints become expensive to unwind later.

## 2. Define The Primary User Tasks And Page Hierarchy

Before drawing components, specify:

- the primary jobs the user needs to complete
- the order in which information should be revealed
- which content is primary, secondary, and supporting
- which actions must remain visible at each stage

This becomes the information architecture, not just a sitemap.

## 3. Establish Layout And Navigation Rules

Document the structural rules that should hold across the surface:

- page shells and major regions
- container widths and breakpoint behavior
- navigation model
- content density expectations
- recurring layout patterns

Layout rules should reduce implementer decision fatigue rather than create another interpretive layer.

## 4. Define Component Families And Boundaries

List the component families needed for the scope:

- content display components
- action components
- navigation components
- feedback and status components
- input components

For each family, specify:

- responsibility
- required states
- composition rules
- what it must not absorb from adjacent components

This prevents a "component" from quietly becoming a page-specific catch-all.

## 5. Define The State Model Up Front

For important surfaces, specify the states the interface must represent:

- empty
- loading
- success
- error
- permission-restricted
- partial or degraded data

State design is part of the foundation. If it is skipped, implementation will invent it inconsistently.

## 6. Set Responsive, Accessibility, And Performance Baselines

The foundation should state:

- how the layout adapts across key breakpoints
- keyboard and focus expectations
- semantic and labeling expectations
- minimum contrast and readability standards
- performance-sensitive UI constraints such as media loading or heavy animation use

Do not assume dark mode, advanced motion, or extensive theming unless the product truly requires them. Define only what the scope justifies.

## 7. Specify Interaction Patterns, Not Just Static Layout

Document the interaction rules users rely on:

- what opens, closes, expands, submits, or navigates
- where feedback appears
- how validation behaves
- what happens after success, cancel, retry, or failure
- how state persistence or preference persistence should work, if relevant

Static mockups without interaction rules push the hardest decisions downstream into code.

## 8. Produce An Implementer-Facing Handoff

The final artifact should be build-oriented:

- file or module responsibilities if known
- component inventory
- state requirements
- layout rules
- responsive constraints
- open risks and deferred polish work

The handoff should reduce ambiguity, not amplify it with abstract design language.

## 9. Separate Foundation Work From Styling Ambition

Keep the boundary clear:

- foundation defines structure, states, and rules
- later design or implementation passes may define visual refinement

This prevents foundational docs from bloating into full brand systems or speculative redesign manifests.

## 10. Review The Foundation Against Scope And Research

Before handoff, verify:

- every major user task is supported by the structure
- every critical state is accounted for
- no major research finding is contradicted
- no unrequested feature or system was added
- the document is specific enough for implementers to follow

## 11. Use A Practical Output Structure

```markdown
# UX Foundation

## Scope
- Surface:
- Primary user tasks:
- Inputs used:

## Information Architecture
- Page hierarchy:
- Navigation model:
- Content priorities:

## Layout Rules
- Shell:
- Regions:
- Breakpoints:

## Component Families
- Family:
  - Responsibility:
  - Required states:
  - Notes:

## Accessibility And Performance Baseline
- Accessibility:
- Performance:

## Interaction Rules
- ...

## Implementation Notes
- Risks:
- Deferred polish:
```

# Success Criteria

- The foundation turns approved scope into build-ready structure.
- Layout, component, and state decisions are explicit enough to reduce implementation drift.
- Accessibility and responsive behavior are part of the foundation, not an afterthought.
- The document stays within structural scope instead of becoming a decorative redesign brief.
- Implementers can tell what to build first and what constraints must hold.

# Common Failure Modes

- Jumping into styling before the task hierarchy and state model are clear.
- Creating component names without defining responsibilities or states.
- Treating responsive behavior as a later implementation detail.
- Assuming major features such as theming or animation without scope support.
- Writing design language so abstract that implementers still have to invent structure.
- Quietly redesigning the product while claiming to define only the foundation.

# Example Prompt

"Use talent `ux-foundation` on this approved interface scope. Turn the user tasks and constraints into page hierarchy, component boundaries, states, and responsive rules that frontend implementation can follow without guessing."
