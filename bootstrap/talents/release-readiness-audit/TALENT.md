---
slug: release-readiness-audit
title: Release Readiness Audit
summary: Judge ship readiness with a skeptical evidence-first audit that defaults to needs work until user journeys, quality gates, and release risks are actually proven.
tags:
  - release
  - audit
  - quality
triggers:
  - The user asks whether something is ready to ship, production-ready, or safe to launch.
  - A release candidate, hardening pass, or final go or no-go review is in scope.
  - A system needs a final verdict backed by more than one verification signal.
inputs:
  - Exact release scope, spec, or acceptance criteria.
  - Fresh evidence across user journeys, tests, performance, security, compliance, and operations as applicable.
  - Known issue list, build artifacts, and release environment details.
outputs:
  - Ready, Needs Work, or Not Ready verdict with evidence-backed rationale.
  - Prioritized issue list, missing proof list, and next iteration targets.
agent_behavior:
  - Default to skepticism until evidence proves readiness.
  - Cross-check claims against real artifacts and complete user journeys.
  - Separate fixable release issues from deeper architectural blockers.
safety:
  - Do not issue a ready verdict without overwhelming evidence for the actual release surface.
  - Do not confuse one green command or one passing subsystem with full release readiness.
status: active
version: 1.0.0
---

# Goal

Make the final shipping decision evidence-based instead of hopeful. This talent exists because release readiness is not a synonym for "build passes" or "most features seem done." A real release audit verifies complete user journeys, required quality gates, and the risks that matter for the actual release.

## Use It When

- a user asks "is this ready to ship"
- a release candidate is under review
- a final hardening pass is needed
- go or no-go must be decided before deployment or announcement

## Do Not Use It When

- the work is obviously incomplete and not at a release boundary
- the need is a narrow single-claim verification rather than a multi-signal readiness judgment; use `verification-gate`

# Procedure

## 1. Set The Audit Boundary Up Front

Define what "release" means for this audit:

- exact artifact, service, branch, or environment in scope
- target users or operators
- release-specific requirements, spec, or checklist
- must-have signals such as performance, security, compliance, or operational readiness

If the release boundary is vague, the verdict will be vague. Lock it first.

## 2. Start From A Skeptical Default

The default verdict is `Needs Work` until proven otherwise.

Why:

- first-pass implementations often need more hardening
- local success often hides integration or distribution gaps
- release decisions fail when optimism outruns evidence

Do not treat skepticism as negativity. It is the job of the gate.

## 3. Collect Fresh Evidence Across The Real Release Surface

The exact mix depends on the product, but the audit should gather the evidence categories that actually matter:

- critical user journeys
- functional regression or acceptance tests
- build and packaging status
- performance under realistic load or usage
- security and permissions checks
- compliance or policy checks when relevant
- operational readiness: deployability, monitoring, rollback, backups, recovery, or installability

Evidence must be fresh and tied to the current release candidate, not copied from an older run.

## 4. Cross-Check Claims Against The Exact Spec

Quote the requirement source directly for release-critical claims.

For each material requirement:

- what the spec or release checklist says
- what artifact, command, or observed behavior proves it
- whether the proof fully matches, partially matches, or fails

This is where missing requirements surface even when most tests are green.

## 5. Validate Complete User Journeys, Not Isolated Features

A release is about the whole experience reaching the user successfully.

Check:

- primary happy paths end to end
- important failure or recovery paths
- cross-device, cross-platform, or cross-environment consistency when applicable
- critical operator flows if operators are part of the release surface

A product can have passing units and still fail the release because the complete journey is broken.

## 6. Aggregate Findings By Severity And Type

Classify issues so the verdict is defensible.

### Critical

Blocks release.

Examples:

- broken core user journey
- security vulnerability
- missing required release artifact
- spec requirement clearly absent
- operational or recovery gap that makes deployment unsafe

### High

May still block release depending on risk tolerance, but at minimum prevents a clean ready verdict.

Examples:

- inconsistent behavior across major supported environments
- high-risk missing test coverage
- material performance shortfall
- compliance evidence missing

### Medium

Should be fixed soon but may not independently block the release if the rest of the surface is strong and the risk is explicit.

## 7. Choose The Verdict Deliberately

Use exactly one of these:

### Ready

Use only when the release surface has overwhelming evidence behind it.

This is rare on the first pass and should feel hard-earned.

### Needs Work

Use when the system is close enough to harden but still has specific fixable issues or missing proof.

This is the expected outcome when hardening discovers real but tractable gaps.

### Not Ready

Use when the blockers are fundamental enough that the work must return to earlier design, architecture, or foundational phases.

Examples:

- structural product gap against the spec
- unsafe architecture for the intended release
- missing foundational systems required for launch

## 8. Produce A Fix-Or-Ship Packet

Default report structure:

```markdown
## Release Readiness Audit
- Release target: [artifact, environment, or version]
- Verdict: Ready | Needs Work | Not Ready

### Evidence Reviewed
- [command, report, artifact, or journey]

### Requirement Coverage
- [requirement] - [pass | partial | fail] - [evidence]

### Findings
- [Critical] ...
- [High] ...
- [Medium] ...

### Missing Proof
- [signal not yet verified]

### Next Action
- [ship]
- [fix list and re-audit]
- [return to earlier phase]
```

For `Needs Work`, include:

- exact fix list
- evidence required for the next pass
- whether 1 or more additional revision cycles are expected

For `Not Ready`, include:

- which earlier phase or design decision must be revisited
- why hardening alone will not solve it

## 9. Keep The Gate Honest

Rules:

- one green subsystem does not prove release readiness
- a local build does not prove deployment, installability, or distribution trust
- old screenshots, old load tests, or old compliance notes do not prove the current candidate
- if the evidence package is incomplete, the verdict cannot be `Ready`

## Integration Notes

- Use `verification-gate` for every individual success claim inside the audit.
- Use `visual-evidence-qa`, `api-validation`, `performance-benchmarking`, or `compliance-review` to gather stronger evidence before the final verdict when those surfaces matter.
- Use `handoff-contracts` when a release gate package must be passed to another owner or phase.

# Success Criteria

- The verdict is tied to the actual release boundary and current evidence.
- Critical user journeys and required release signals are checked end to end.
- The report distinguishes fixable hardening issues from deeper foundational blockers.
- A ready verdict is rare and well-supported rather than casual.
- A needs-work verdict comes with a concrete next iteration path.

# Common Failure Modes

- Treating passing tests as a substitute for release readiness.
- Auditing isolated features instead of complete user journeys.
- Reusing stale evidence from an older candidate.
- Calling something ready without security, performance, operational, or compliance proof when those are in scope.
- Hiding missing proof behind an upbeat summary.
- Using "needs work" for issues that are actually architectural and should be called `Not Ready`.

# Example Prompt

"Use `release-readiness-audit` on this release candidate. Default to skepticism, audit the exact release surface with fresh evidence, validate the critical journeys and requirements, then return a Ready, Needs Work, or Not Ready verdict with the missing proof and fix list called out explicitly."
