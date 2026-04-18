---
slug: design-before-build
title: Design Before Build
summary: Require context discovery, option analysis, written design review, and explicit approval before any implementation starts.
tags:
  - planning
  - design
  - specification
triggers:
  - New features, behavior changes, or greenfield work with multiple plausible approaches.
  - Requests that feel simple but still change behavior, architecture, or user expectations.
inputs:
  - User goal, constraints, and success criteria.
  - Current project context such as files, docs, recent changes, and existing patterns.
outputs:
  - Approved design with clear scope, architecture, failure handling, and verification approach.
  - Written spec path and an explicit handoff into implementation planning.
agent_behavior:
  - Explore the real project state before proposing solutions.
  - Ask one clarifying question at a time until the decision boundary is concrete.
  - Present multiple viable approaches with a recommendation before settling on a design.
safety:
  - Do not start implementation, scaffolding, or code edits before the design is presented and approved.
  - Do not let placeholders, contradictions, or hidden scope creep survive into the written spec.
status: active
version: 1.0.0
---

# Goal

Produce an approved, implementation-ready design before any coding begins. This talent exists to prevent premature implementation, hidden assumptions, and "simple change" rationalizations that create rework later.

## Use It When

- The task introduces or changes behavior.
- The request is ambiguous, multi-step, or system-affecting.
- Multiple architectures, data flows, or UX patterns are plausible.
- Another agent or future session may need to execute the work from the written spec.

## Do Not Use It When

- The work is purely read-only analysis.
- The task is a mechanical formatting change with no behavior or structural impact.
- The user already provided an approved design and the real need is execution planning. In that case, move to `implementation-planning`.

## Required Operating Boundary

Design comes before implementation every time. A short design is fine for a small change. Skipping the design is not.

# Procedure

## 1. Explore The Existing Context First

Read the actual project state before asking for decisions:

- inspect the relevant code, docs, recent changes, and existing patterns
- identify whether the work touches one subsystem or several
- note any constraints the design must respect, including architecture, user preferences, rollout limits, and verification surface

Do not improvise a design from the request alone. The design must fit the current system, not a generic imagined one.

## 2. Run An Early Scope Gate

Before refining details, decide whether the request is small enough for one design artifact:

- if the request spans multiple independent subsystems, decompose it first
- define the sub-projects, their ordering, and the smallest first slice worth designing
- keep each design bounded enough that one implementation plan can execute it cleanly

A design that bundles unrelated work is already failing.

## 3. Clarify One Question At A Time

Use a tight question loop to remove ambiguity:

- ask one question per turn
- prefer questions that collapse major uncertainty: purpose, constraints, success criteria, non-goals, rollout shape
- use multiple-choice framing when it reduces ambiguity faster
- stop asking once additional answers are no longer changing the design

Do not dump a questionnaire. Do not ask implementation-detail questions before the product or system boundary is clear.

## 4. Produce Options Before Choosing

Present 2-3 credible approaches with trade-offs and a recommendation:

- lead with the recommended option
- explain why it fits the current codebase and stated constraints
- name what is gained, what is deferred, and what risk each option carries
- remove approaches that add unrequested complexity

This step is mandatory because it exposes assumptions and prevents a false sense that there was only one obvious solution.

## 5. Present The Design In Reviewable Sections

Once the direction is clear, present the design in sections sized to the problem:

- architecture and system boundaries
- major components or files
- data flow or state flow
- error handling and recovery behavior
- testing and verification approach
- rollout or migration constraints if relevant

Scale each section to the real complexity. Straightforward changes can use concise sections. Nuanced work needs deeper treatment. After each major section, pause for confirmation or correction instead of monologuing past disagreement.

## 6. Write The Spec

After the direction is approved in principle, write the design to a durable spec file. Default to a repo-local docs path unless the project has a different convention.

The written spec should contain:

- objective and non-goals
- exact scope boundary
- chosen approach and rejected alternatives
- file and component responsibilities
- behavior details, edge cases, and failure handling
- testing strategy
- explicit open questions only if they are truly blocked on outside input

Treat the spec as the contract between design and planning. If the design only exists in chat, it is not ready for planning.

## 7. Review The Written Spec Before Handoff

Run two review passes before planning begins.

### Self-Review Checklist

Fix issues inline before involving anyone else:

- placeholder scan: remove `TBD`, `TODO`, vague "handle appropriately" language, and hidden assumptions
- internal consistency: ensure behavior, architecture, and testing do not contradict each other
- scope check: confirm the design is still small enough for one implementation plan
- ambiguity check: rewrite anything that could be interpreted in multiple incompatible ways
- YAGNI check: remove features that were not requested and are not required to satisfy the goal

### Independent Spec Review Loop

Run a second-pass review using a fresh reviewer when available. The review should check:

- completeness
- coverage of edge cases and integration points
- consistency
- clarity
- unnecessary scope or over-engineering

Use a simple verdict format:

```markdown
## Spec Review

**Status:** Approved | Issues Found

**Issues (if any):**
- [Section]: [issue] - [why it matters]

**Recommendations (advisory):**
- [non-blocking improvement]
```

If issues are found, revise the spec and review again. If the same disagreement survives repeated review, surface the decision explicitly instead of silently splitting the difference.

## 8. Get Explicit Approval Before Planning

After the spec is clean, ask for explicit approval of the written spec. Do not move into implementation planning until that approval exists. If the user requests edits, make them and re-run the review loop.

## 9. Hand Off To Planning, Not Code

The terminal state of this talent is a reviewed, approved spec and a clear transition into `implementation-planning`. Do not blur the phases by starting code "while the plan is obvious."

# Success Criteria

- The design is grounded in the existing project rather than imagined from scratch.
- Scope is bounded tightly enough to produce one execution-ready implementation plan.
- The user has seen alternatives, understands the recommendation, and explicitly approved the design.
- A written spec exists at a concrete path and survives self-review plus a second review pass.
- No implementation work started before the design gate was cleared.

# Common Failure Modes

- Calling the task too simple for design and skipping straight to code.
- Asking a large batch of questions instead of resolving the biggest uncertainty first.
- Treating the first plausible approach as the only approach.
- Writing a spec that still contains placeholders, contradictions, or hidden scope growth.
- Letting planning or implementation begin before the written design is approved.
- Producing a design that is really an implementation checklist. That belongs in `implementation-planning`, not here.

# Example Prompt

"Use talent `design-before-build` for this feature request. Inspect the repo first, clarify one question at a time, present 2-3 approaches with a recommendation, write the approved spec, run a spec review pass, and stop at the planning handoff."
