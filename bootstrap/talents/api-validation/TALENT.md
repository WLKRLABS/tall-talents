---
slug: api-validation
title: API Validation
summary: Validate APIs across contract, authentication, error handling, integration, and performance expectations with a traceable test matrix.
tags:
  - quality
  - api
  - validation
triggers:
  - A new endpoint, version, integration, or contract change must be verified.
  - API behavior is central to a feature, release, or incident review.
  - Someone claims an API is stable, secure, or ready without a structured validation pass.
inputs:
  - Endpoint inventory, routes, or API specification.
  - Auth model, expected request and response behavior, and relevant SLAs if they exist.
  - Test environment, credentials, fixtures, and dependency details.
outputs:
  - API test matrix covering functional, negative, auth, integration, and performance cases.
  - Evidence-backed findings with endpoint-level pass or fail status.
  - Clear release recommendation or residual risk statement.
agent_behavior:
  - Inventory the real API surface before choosing tests.
  - Test failure modes and abuse cases, not just successful requests.
  - Treat missing documentation, missing SLAs, or missing observability as real risks.
safety:
  - Do not declare an API validated because a few happy-path requests worked.
  - Do not invent acceptable latency, auth, or contract thresholds when the system has not defined them.
status: active
version: 1.0.0
---

# Goal

Prove whether an API is behaving correctly, safely, and predictably under the conditions that matter. This talent exists to stop superficial endpoint testing from being mistaken for true API readiness.

## Use It When

- Shipping or refactoring API endpoints.
- Validating third-party or service-to-service integrations.
- Auditing release readiness for systems with important API surfaces.

## Do Not Use It When

- The work has no meaningful API surface.
- You only need deep performance analysis for an already-known contract.
- The endpoint inventory, auth model, or environment access is so incomplete that results would be mostly guesswork.

## Preconditions

You need the real surface area: routes, versions, auth model, required payloads, error expectations, and environment access. If no SLA or contract exists, log that absence as a risk instead of silently choosing one.

# Procedure

## 1. Inventory The Actual API Surface

Start from source or authoritative docs, not memory:

- list endpoints, methods, versions, and owners
- identify auth requirements and role boundaries
- note idempotent versus non-idempotent operations
- record rate limits, quotas, or abuse controls if they exist
- identify upstream and downstream dependencies

This inventory becomes the spine of the validation matrix.

## 2. Build A Test Matrix Before Sending Requests

For each endpoint, define coverage across these categories:

- happy path behavior
- required field validation
- malformed input handling
- authentication
- authorization
- duplicate or replay behavior where relevant
- error response shape
- dependency failure handling
- documentation or example accuracy
- performance against explicit targets, if known

Do not improvise tests endpoint by endpoint in a way that leaves major categories uncovered.

## 3. Prepare A Controlled Test Environment

Before execution, confirm:

- credentials and roles are available
- test data is safe and resettable
- side effects are understood
- external integrations are either mockable or intentionally exercised
- logs, traces, or metrics can be consulted if behavior is ambiguous

APIs with destructive behavior need stricter test-data discipline than read-only endpoints.

## 4. Validate Happy Paths And Contract Shape

Run the expected successful requests first:

- verify status codes
- verify response payload shape
- verify required fields and forbidden fields
- verify persistence or side effects
- verify backward compatibility if versioning matters

The goal here is not merely "200 OK." The goal is "contract matches the intended shape and side effects."

## 5. Validate Authentication And Authorization Separately

Test authn and authz as independent concerns:

- request without credentials
- request with expired or invalid credentials
- request with valid credentials but insufficient role or scope
- cross-tenant or cross-user access attempts where relevant

Many APIs pass happy-path tests while failing on the boundary that matters most.

## 6. Test Negative Cases And Error Discipline

For each important endpoint, test:

- missing required fields
- invalid field formats
- unsupported values
- duplicate submissions where relevant
- oversized payloads where relevant
- malformed JSON or invalid encoding when appropriate

Check not only that the request fails, but that it fails in a predictable, documented, safe way.

## 7. Exercise Integration And Dependency Failure Paths

If the API touches databases, queues, other services, or third parties, validate:

- timeout handling
- partial dependency failure
- unavailable upstream services
- retry behavior
- deduplication or idempotency where repeated delivery is possible

An endpoint that only works in the fully healthy case is not fully validated.

## 8. Validate Performance Against Real Targets

If the system has explicit latency or throughput expectations, test them. If it does not, record that gap and avoid pretending the API passed a standard that was never defined.

At minimum, capture:

- percentile latency, not just averages
- error rate under representative load
- throughput at expected volume
- resource or dependency bottlenecks if visible

If performance is a primary question, hand off or pair with `performance-benchmarking`.

## 9. Verify Documentation And Executable Examples

If docs, examples, or SDK snippets exist:

- run or replay them where feasible
- confirm sample payloads still work
- confirm auth instructions match reality
- note undocumented required fields, headers, or setup steps

Documentation drift is a validation failure when other systems or teams depend on it.

## 10. Return A Traceable Endpoint-Level Verdict

Use a report structure that makes coverage and gaps obvious:

```markdown
# API Validation Report

## Scope
- Service:
- Environment:
- Endpoint count:
- SLA / contract source:

## Coverage Matrix
| Endpoint | Functional | Auth | Negative cases | Integration | Performance | Docs |
|---|---|---|---|---|---|---|

## Findings
1. [Severity] [Endpoint] - [Issue]
   - Evidence:
   - Expected:
   - Actual:
   - Risk:

## Residual Risks
- Missing SLA:
- Untested dependency:
- Environment limitation:

## Verdict
- PASS | PASS WITH RISKS | FAIL
```

## 11. Stop At The Right Boundary

This talent should end with a validated API state and a clear list of residual risks. If the next step is redesigning the contract, tuning systemic performance, or reworking architecture, say so explicitly instead of smuggling that work into the validation pass.

# Success Criteria

- Every important endpoint is covered by a visible matrix, not an implied memory list.
- Functional, auth, negative, and integration behavior are all exercised where applicable.
- Missing contracts, missing SLAs, and missing docs are reported as risks rather than ignored.
- Findings are endpoint-specific and tied to evidence.
- The final verdict distinguishes validated behavior from unvalidated assumptions.

# Common Failure Modes

- Testing only successful requests and calling the API validated.
- Confusing authentication success with correct authorization boundaries.
- Using averages instead of percentiles for latency claims.
- Ignoring dependency failures because the happy path is currently green.
- Trusting documentation examples without executing them.
- Inventing performance targets because the system never defined one.

# Example Prompt

"Use talent `api-validation` on this service change. Inventory the real endpoints first, build a matrix that includes auth, negative cases, dependency failures, and performance expectations, then return an evidence-backed verdict with explicit residual risks."
