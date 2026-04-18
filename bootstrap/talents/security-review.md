---
slug: security-review
title: Security Review
summary: Review a system through threat modeling, secure-code assessment, prioritized findings, and verification that remediations actually close the risk.
tags:
  - security
  - review
  - risk
triggers:
  - A design, implementation, or deployment surface needs security analysis before shipping or after a significant change.
  - The team needs threat modeling, secure-code review, or remediation guidance grounded in real attack paths.
inputs:
  - System architecture, code, configs, dependencies, and deployment context.
  - Access to the relevant trust boundaries, data flows, and user or service roles.
outputs:
  - Threat model, prioritized findings, and concrete remediation guidance.
  - Security verification results showing which issues were reproduced, fixed, retested, or left as residual risk.
agent_behavior:
  - Think like an attacker, then report like an engineer.
  - Prioritize by exploitability, blast radius, and business impact rather than by fear.
  - Pair every meaningful finding with a concrete remediation path.
safety:
  - Do not recommend weakening controls as a shortcut.
  - Do not present theoretical risk as confirmed exploitability without evidence.
status: active
version: 1.0.0
---

# Goal

Catch and reduce security risk early by mapping the attack surface, identifying concrete weaknesses, and verifying that remediations actually hold.

## Use It When

- A new system or major feature is being designed.
- A code path handles auth, secrets, sensitive data, payments, admin actions, uploads, or external callbacks.
- Infrastructure or CI/CD changes could widen the attack surface.
- A team wants a security-focused review before release.

## Do Not Use It When

- The task is a purely stylistic code review with no meaningful trust boundary.
- There is no access to the code, architecture, or deployment context and the only possible output would be generic advice.
- The system needs active incident coordination right now. Use `incident-response` first, then review the aftermath.

## Security Posture Rules

- All user input is hostile until validated.
- Default deny beats default allow.
- Least privilege is the baseline, not an enhancement.
- No custom crypto, secret sprawl, or trust-by-obscurity.
- A finding without remediation is incomplete.

# Procedure

## Phase 1: Reconnaissance And Threat Modeling

### 1. Map The System

Inspect:

- user roles and privilege levels
- entry points: UI, API, jobs, uploads, webhooks, CLIs
- data flows and sensitive data classes
- dependencies and third-party integrations
- deployment and CI/CD surfaces

If you cannot explain how data and authority move through the system, you are not ready to review it.

### 2. Identify Trust Boundaries

Note where control changes hands:

- internet to edge
- edge to application
- service to service
- app to database
- internal operator to privileged control plane
- CI/CD to production

Most high-severity issues live at these seams.

### 3. Build A Threat Model

Use a lightweight STRIDE-style pass when relevant:

- spoofing
- tampering
- repudiation
- information disclosure
- denial of service
- elevation of privilege

Document:

- component
- plausible attack path
- impacted asset
- current control
- missing control

The threat model should make later code review sharper, not longer.

## Phase 2: Security Assessment

### 4. Review The Highest-Risk Code Paths First

Prioritize:

- authentication and session logic
- authorization checks
- input validation and parsing
- data access and query construction
- file handling
- secrets use and exposure
- error handling and logging
- rate limiting and abuse controls

Do not burn time equally across low- and high-risk surfaces.

### 5. Audit Dependencies And Configuration

Check for:

- known vulnerable packages
- unmaintained critical dependencies
- unsafe default configs
- permissive CORS or CSP
- insecure transport or weak secret handling
- CI/CD gaps such as missing SAST, secret scanning, or artifact trust controls

Supply-chain risk counts as product risk.

### 6. Look For Business Logic Abuse, Not Just OWASP Basics

Also assess:

- workflow bypass
- race conditions
- price or quota manipulation
- privilege escalation through feature composition
- cross-tenant or cross-user data exposure
- insecure admin tooling

A system can pass textbook checks and still be easy to abuse.

## Phase 3: Findings And Remediation

### 7. Write Findings In Priority Order

For each finding include:

- severity
- affected surface
- exploit path or proof
- blast radius
- why it matters
- recommended remediation

Suggested severity scale:

- Critical
- High
- Medium
- Low
- Informational

Do not inflate severity to win attention. Credibility matters.

### 8. Prefer Concrete Fixes Over Abstract Advice

Good remediation guidance says:

- where to add validation
- which authorization check is missing
- what secret path must change
- what header, policy, or scan belongs in CI
- what test should fail before the fix and pass after

Weak guidance says "improve security around uploads."

## Phase 4: Verification

### 9. Write Or Run Security-Focused Verification

Where feasible, verify fixes with:

- failing tests or reproduction steps
- targeted attack simulations in safe conditions
- regression checks for auth, authz, validation, and headers
- pipeline scans or dependency audits

Security review is incomplete if no one proves the remediation worked.

### 10. Record Residual Risk Honestly

Not every issue will be fixed immediately.

For deferred or partially mitigated items, record:

- current exposure
- compensating controls
- owner
- deadline or revisit trigger

Untracked residual risk becomes surprise incident fuel later.

## Security Review Report Template

```markdown
## Security Review

- Scope:
- Threat model completed:
- Findings summary:
- Highest-risk issue:
- Verification run:
- Residual risks:
- Recommended next talent:
```

## Strong vs Weak Execution

Strong:

- starts with trust boundaries and attack paths
- focuses on the highest-risk surfaces first
- includes business logic abuse, not just checklist vulnerabilities
- pairs every finding with a fix path
- verifies remediations

Weak:

- produces generic secure-coding advice without reading the system
- treats every finding as equally severe
- stops at "this is risky" without describing the exploit path
- ignores CI/CD and dependency exposure
- declares a fix complete without retesting it

# Success Criteria

- A concrete threat model or equivalent boundary map exists.
- Findings are prioritized by real risk, not by volume.
- Each meaningful issue includes remediation guidance.
- Security verification demonstrates which fixes actually closed the issue.
- Residual risk is documented with ownership and revisit logic.

# Common Failure Modes

- Reviewing low-risk code first because it is easier to read.
- Treating security review as a static lint pass instead of a threat-driven exercise.
- Missing authorization and business-logic flaws because the review stops at input validation.
- Reporting vague findings without reproduction or blast radius.
- Accepting "fixed" without rerunning the relevant security checks.
- Disabling protections to make development easier and calling it temporary.

# Example Prompt

"Use `security-review` on this system change. Map the trust boundaries first, review the highest-risk code and config surfaces, prioritize findings by exploitability and blast radius, provide concrete remediations, and verify the fixes instead of assuming they worked."
