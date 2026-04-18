---
slug: visual-evidence-qa
title: Visual Evidence QA
summary: Validate visual and interaction quality through captured evidence, honest inspection, and issue reporting tied to exact screenshots or recordings.
tags:
  - quality
  - qa
  - visual
triggers:
  - UI, responsive, theming, or interaction work needs a credible QA pass.
  - Someone is claiming a visual surface is done, polished, or production ready.
  - A release or review depends on what users can actually see and do.
inputs:
  - Running build, preview, or artifact to inspect.
  - Spec, acceptance criteria, or exact UI expectations.
  - A capture method for screenshots, recordings, or comparable visual evidence.
outputs:
  - Evidence set covering the tested flows and states.
  - Issue list tied to specific proof and severity.
  - Honest verdict describing current quality and re-test needs.
agent_behavior:
  - Capture evidence before forming conclusions.
  - Describe what is actually visible and reproducible, not what seems intended.
  - Default to skepticism when work is being rated too highly without proof.
safety:
  - Do not approve a visual surface without fresh evidence from the current build.
  - Do not invent missing requirements or excuse visible defects with design speculation.
status: active
version: 1.0.0
---

# Goal

Make visual QA evidence-first. This talent exists to stop fantasy approvals, catch visible regressions early, and force quality claims to rest on what the interface actually shows across real states and devices.

## Use It When

- The work has a visible UI or interaction surface.
- Responsive behavior, theming, forms, navigation, or state handling matter.
- A reviewer needs proof rather than narrative.

## Do Not Use It When

- The work is purely backend, infrastructure, or CLI with no meaningful visual surface.
- The artifact cannot be rendered or exercised yet.
- The real task is product design direction rather than verification of an implemented surface.

## Preconditions

You need a current build, the acceptance source, and a workable capture path. If you cannot capture the surface you are supposed to approve, the correct verdict is not approval.

# Procedure

## 1. Start With The Acceptance Source

Before opening the UI, collect the exact expectations:

- quote the relevant spec or acceptance criteria
- identify the flows and states that matter most
- note device, theme, or accessibility requirements that are explicitly in scope

The QA pass should compare implementation to the real requirement, not to a vague sense of polish.

## 2. Capture Evidence Before Interpreting It

Generate or collect evidence first:

- desktop view
- tablet view if the surface is responsive
- mobile view if the surface is responsive
- light and dark theme only if theming is part of the implemented or required behavior
- empty, loading, error, and success states where relevant
- before/after interaction captures for anything collapsible, modal, navigational, or stateful

If the surface has error handling, capture the error state. If it has validation, capture invalid input as well as successful input.

## 3. Inspect With Your Eyes, Not With Intent

Review the evidence and document exactly what is visible:

- layout alignment
- spacing rhythm
- typography hierarchy
- truncation or overflow
- contrast and readability
- broken states
- missing affordances
- visibly incorrect interaction outcomes

Do not rewrite the interface in your head. Describe what shipped, not what the implementer likely meant.

## 4. Exercise The Critical Interactions

At minimum, test the interactions that change state or route the user:

- navigation and routing
- menu open/close behavior
- forms: empty, filled, invalid, submitted
- dialogs and drawers
- accordions or expandable regions
- hover, focus, and keyboard-visible states when relevant
- retry, dismiss, cancel, and back behaviors

For each interaction, keep proof of the starting state and the resulting state.

## 5. Compare Evidence Against The Requirement Line By Line

For each important requirement, record one of:

- `MATCHES`: evidence clearly shows the behavior or visual condition
- `PARTIAL`: the intent is visible but incomplete or inconsistent
- `MISSING`: the requirement is not present
- `REGRESSION`: the interface fails or visibly breaks

This prevents vague verdicts like "mostly there" from hiding specific misses.

## 6. Create Evidence-Tied Findings

Every issue should include:

- what is wrong
- where it appears
- why it matters
- proof reference
- severity

Useful severities:

- `Critical`: blocks task completion or breaks a primary flow
- `High`: major mismatch, strong usability damage, or obvious release risk
- `Medium`: meaningful polish or consistency issue that should be fixed soon
- `Low`: minor but real defect worth tracking

## 7. Use Honest Rating Discipline

Default to caution on first-pass work. A clean run with zero issues is rare and requires extra scrutiny. If you find no issues, say why the surface appears low-risk and what evidence supports that judgment.

Do not use inflated language:

- no "premium" or "production ready" without proof
- no perfect scores for obviously early work
- no approval because the implementation effort seems high

## 8. Decide The Verdict

The QA verdict should be one of:

- `PASS`: acceptance criteria met and remaining issues are explicitly minor
- `FAIL`: defects block acceptance or trust in the surface
- `RETEST REQUIRED`: fixes landed, but evidence is stale or incomplete

If evidence is inconclusive, fail or require re-test. Ambiguity is not a pass.

## 9. Return A Fixable Report

The report should help the implementer act immediately:

```markdown
# Visual QA Report

## Scope
- Surface tested:
- Build or URL:
- Acceptance source:

## Evidence Reviewed
- Desktop:
- Tablet:
- Mobile:
- State captures:

## Requirement Comparison
- MATCHES:
- PARTIAL:
- MISSING:
- REGRESSIONS:

## Findings
1. [Severity] Issue
   - Evidence:
   - Expected:
   - Actual:
   - Why it matters:

## Verdict
- PASS | FAIL | RETEST REQUIRED

## Next Action
- Fix list:
- Re-test scope:
```

## 10. Re-Test Only The Current Build

After fixes, capture fresh evidence. Do not carry forward approval from an older run. A re-test should verify:

- the reported issues are actually fixed
- the fix did not create new visual or interaction regressions
- the original acceptance source is now satisfied

# Success Criteria

- Visual claims are tied to fresh, reviewable evidence.
- The report distinguishes observed reality from assumed intent.
- Major flows and relevant states are exercised, not just screenshot once-over views.
- Findings are actionable because each one points to exact proof and impact.
- Approval, if given, is evidence-backed and narrow enough to trust.

# Common Failure Modes

- Approving based on a narrative description instead of a current capture.
- Looking only at the happy path and skipping validation, error, loading, or responsive states.
- Writing generic comments like "spacing feels off" without evidence or consequence.
- Treating inconclusive results as a soft pass.
- Inflating ratings because the work seems difficult or the submitter is confident.
- Comparing against a remembered design instead of the actual acceptance source.

# Example Prompt

"Use talent `visual-evidence-qa` on this UI change. Capture the current surface first, compare it against the exact acceptance criteria, tie every issue to proof, and give a pass/fail verdict only if the evidence supports it."
