---
slug: tdd
title: Test-Driven Development
summary: Build features or fixes one vertical slice at a time with red-green-refactor, behavior tests through public interfaces, and no horizontal test-writing pass.
tags:
  - testing
  - implementation
  - quality
triggers:
  - User asks for TDD, test-first development, red-green-refactor, or integration-style tests.
  - A feature or bug fix should be built through one verified behavior slice at a time.
  - Tests risk coupling to implementation details instead of observable behavior.
inputs:
  - Desired behavior, public interface expectations, codebase patterns, and test framework.
  - Domain glossary and ADRs when present.
  - User's priority order for behaviors to test.
outputs:
  - One behavior test failing before implementation and passing after implementation per cycle.
  - Minimal implementation for each slice.
  - Refactor pass with tests green after each step.
agent_behavior:
  - Test public behavior through real interfaces, not private methods or internal collaborators.
  - Work one test and one behavior at a time.
  - Never refactor while red.
  - Use project domain vocabulary in test names and interface names.
safety:
  - Do not write all tests first and then all implementation.
  - Do not mock internal modules the codebase controls.
  - Do not add speculative features to satisfy imagined future tests.
status: active
version: 1.0.0
---

# Goal

Deliver behavior through a disciplined red-green-refactor loop where every test describes observable behavior and survives internal refactors.

# Procedure

## 1. Plan The Public Behavior

Before code changes:

- read relevant code, `CONTEXT.md`, and ADRs
- confirm the public interface that should carry the behavior
- list behavior tests, not implementation steps
- prioritize the first thin vertical slice
- identify deep module opportunities and test seams
- get user approval when interface or behavior priority is not already specified

Ask:

```text
What should the public interface look like? Which behaviors matter most to test?
```

## 2. Write One Tracer-Bullet Test

Start with one test that confirms one end-to-end behavior through the public interface.

Good tests:

- exercise real code paths
- verify what users or callers care about
- use public APIs only
- describe what the system does
- survive internal refactors

Bad tests:

- mock internal collaborators
- assert private methods, call counts, or internal order
- verify by bypassing the interface
- describe how the implementation works

Run the test and confirm it fails for the expected reason.

## 3. Go Green Minimally

Write only enough code to pass the current test.

Rules:

- do not anticipate later tests
- do not generalize before repeated need exists
- keep implementation boring and direct
- rerun the focused test until green

## 4. Repeat Vertically

For each next behavior:

```text
RED: write one behavior test -> confirm expected failure
GREEN: implement the minimum -> confirm pass
```

Do not use a horizontal slice:

```text
Wrong: write tests 1-5, then implementation 1-5.
Right: test 1 -> implementation 1, test 2 -> implementation 2.
```

Each cycle should teach the next one.

## 5. Mock Only At System Boundaries

Mock or substitute:

- third-party APIs
- time or randomness
- filesystem when needed
- database only when a realistic test database or local stand-in is not practical

Do not mock:

- own classes
- internal modules
- code under the same control boundary

At boundaries, prefer dependency injection and specific SDK-style interfaces over generic fetchers that force conditional mock logic.

## 6. Refactor Only While Green

After behavior tests pass:

- remove duplication
- deepen shallow modules
- move logic to improve locality
- introduce value objects when primitives are carrying domain meaning
- improve interfaces so testing remains natural

Run tests after each refactor step. Keep tests on the public interface.

## Cycle Checklist

```markdown
- [ ] Test describes behavior, not implementation.
- [ ] Test uses the public interface.
- [ ] Test fails for the expected reason before code.
- [ ] Code is minimal for this test.
- [ ] Test passes after implementation.
- [ ] No speculative behavior was added.
- [ ] Refactor happened only while green.
```

# Success Criteria

- Every implementation step is driven by a failing behavior test.
- Tests are integration-style and public-interface oriented.
- Work advances through vertical tracer bullets, not horizontal batches.
- Refactors happen only after green and keep tests passing.
- The resulting tests would survive internal implementation changes.

# Common Failure Modes

- Writing tests for imagined future behavior before the first slice exists.
- Testing implementation details and locking the code against useful refactors.
- Mocking internal modules instead of testing through the real interface.
- Refactoring while red.
- Adding generality that no current test or user behavior requires.

# Example Prompt

"Use `tdd` for this feature. Confirm the public behavior and first vertical slice, write one failing behavior test, implement only enough to make it pass, repeat one slice at a time, and refactor only while green."
