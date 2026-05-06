---
slug: improve-codebase-architecture
title: Improve Codebase Architecture
summary: Find deepening opportunities in a codebase by using domain language, ADRs, module depth, seams, adapters, leverage, and locality.
tags:
  - architecture
  - refactoring
  - codebase
triggers:
  - User wants to improve architecture, find refactoring opportunities, or make code more testable.
  - A codebase has tightly coupled modules, shallow pass-through layers, or weak test seams.
  - User wants code to become easier for agents and humans to navigate.
inputs:
  - Relevant code, tests, CONTEXT.md, CONTEXT-MAP.md, and docs/adr.
  - User's area of concern or permission to scan for architecture friction.
  - Existing failures, testing pain, or navigation pain when available.
outputs:
  - Numbered deepening opportunities with files, problem, solution, and benefits.
  - Chosen candidate design discussion, context updates, and optional ADRs.
  - Interface exploration when the user asks to design a deepened module.
agent_behavior:
  - Use the vocabulary Module, Interface, Implementation, Depth, Seam, Adapter, Leverage, and Locality exactly.
  - Read domain docs and ADRs before proposing candidates.
  - Present candidates before proposing concrete interfaces.
  - Ask which candidate to explore before entering design detail.
safety:
  - Do not relitigate ADRs unless real friction justifies reopening the decision.
  - Do not introduce a seam unless at least two adapters or a clear variation point justify it.
  - Do not keep old shallow-module tests once deeper interface tests replace them.
status: active
version: 1.0.0
---

# Goal

Surface architecture improvements that make code easier to understand, test, and change by turning shallow modules into deeper modules with better seams.

# Procedure

## 1. Load Domain And Decision Context

Read the project's domain vocabulary and decisions first:

- `CONTEXT-MAP.md` if present
- applicable `CONTEXT.md`
- applicable `docs/adr/`
- nearby tests and code paths

Use project domain terms for product concepts and the architecture vocabulary in this talent for code structure.

## 2. Use The Architecture Vocabulary Precisely

Use these terms exactly:

- **Module** - anything with an interface and an implementation
- **Interface** - everything callers must know: types, invariants, ordering, error modes, configuration, and performance characteristics
- **Implementation** - code inside the module
- **Depth** - leverage at the interface
- **Seam** - where an interface lives and behavior can vary
- **Adapter** - concrete thing satisfying an interface at a seam
- **Leverage** - what callers get from depth
- **Locality** - what maintainers get from depth

Avoid substituting overloaded words such as component, service, API, or boundary when the exact concept is module, interface, or seam.

## 3. Explore For Friction

Look for places where understanding or changing one concept requires too much bouncing:

- shallow modules whose interface is nearly as complex as the implementation
- pass-through modules that fail the deletion test
- pure functions extracted only for testability while real bugs live in orchestration
- tightly coupled modules that leak knowledge across seams
- areas with weak or missing tests because the current interface is wrong

Deletion test:

```text
If deleting the module makes complexity vanish, it was not earning its keep.
If deleting it spreads complexity across callers, it was hiding useful complexity.
```

## 4. Present Deepening Candidates First

Return a numbered list before proposing interfaces.

For each candidate include:

- **Files** - modules involved
- **Problem** - architecture friction in terms of depth, seam, leverage, or locality
- **Solution** - plain-English change
- **Benefits** - how locality, leverage, and tests improve
- **ADR conflicts** - only when an existing ADR would be contradicted and real friction justifies reopening it

Ask: "Which of these would you like to explore?"

## 5. Classify Dependencies For The Chosen Candidate

Dependency category determines test strategy:

- in-process - deepen directly and test through the new interface
- local-substitutable - use a local test stand-in such as in-memory storage or PGLite
- remote but owned - define a port at the seam and use production plus test adapters
- true external - inject a port and test with a mock adapter

One adapter means a hypothetical seam. Two adapters means a real seam.

## 6. Run The Grilling Loop

For the chosen candidate, clarify:

- what concept the deepened module owns
- which complexity sits behind the interface
- where the seam belongs
- which callers should know less after the refactor
- which tests should survive and which shallow tests should be deleted

If a new domain term is resolved, update `CONTEXT.md` using `grill-with-docs` discipline. If the user rejects a candidate for a durable, non-obvious reason, offer an ADR so future reviews do not re-suggest it.

## 7. Explore Interfaces Only When Asked

If the user wants interface design, use a "design it twice" pattern:

- frame constraints and dependency categories
- generate multiple materially different interfaces
- compare by depth, locality, seam placement, and adapter strategy
- recommend one interface or a hybrid

Interface output should include invariants, ordering, error modes, and usage examples, not just method names.

# Success Criteria

- Suggestions are grounded in real code, CONTEXT.md vocabulary, and ADR awareness.
- Candidates explain friction using depth, leverage, locality, and seam placement.
- No concrete interface is proposed before the user chooses a candidate.
- Testing strategy moves toward behavior through the deepened interface.
- ADR conflicts and durable rejected decisions are handled explicitly.

# Common Failure Modes

- Listing generic refactors instead of code-grounded deepening opportunities.
- Calling every boundary a seam without a real variation point.
- Proposing interfaces too early.
- Keeping old shallow tests that duplicate or fight the deeper interface tests.
- Ignoring domain terms and naming modules after implementation artifacts.

# Example Prompt

"Use `improve-codebase-architecture` on this area. Read CONTEXT.md and ADRs, inspect the code, find deepening opportunities using the module/interface/seam vocabulary, present candidates first, and wait for me to pick one before designing interfaces."
