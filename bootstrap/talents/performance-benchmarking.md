---
slug: performance-benchmarking
title: Performance Benchmarking
summary: Establish baselines, run realistic performance tests, analyze bottlenecks statistically, and report pass or fail against explicit targets.
tags:
  - quality
  - performance
  - benchmarking
triggers:
  - Performance, scalability, or capacity is a release concern or active problem.
  - A system needs load, stress, endurance, or user-perceived performance evaluation.
  - Optimization work is being proposed and needs a baseline first.
inputs:
  - Critical user journeys, workloads, or services to test.
  - Performance targets, budgets, or explicit statement that they are missing.
  - Test environment details, instrumentation access, and traffic assumptions.
outputs:
  - Baseline and benchmark results with percentile-based metrics.
  - Bottleneck analysis across client, service, database, and dependency layers.
  - Optimization priorities and final pass, fail, or needs-target-definition verdict.
agent_behavior:
  - Baseline before recommending changes.
  - Use realistic load models and statistical interpretation.
  - Keep user-perceived performance and system-side metrics connected.
safety:
  - Do not optimize blindly without measuring the current state first.
  - Do not claim compliance with a performance target that was never explicitly defined.
status: active
version: 1.0.0
---

# Goal

Measure whether a system meets its actual performance expectations and explain why it does or does not. This talent exists to replace anecdotal speed claims with disciplined benchmarking and defensible bottleneck analysis.

## Use It When

- Performance is part of the acceptance bar.
- Capacity planning, release hardening, or a speed regression investigation is in scope.
- A team is about to optimize and needs to know where the time or load really goes.

## Do Not Use It When

- The task is strictly API correctness without broader performance questions.
- The environment is so artificial that results would be misleading and no caveat can make them useful.
- No one can define what "fast enough" means and the only honest result is target-definition work.

## Preconditions

You need the system under test, a representative environment or clear caveat about the environment, and explicit targets or an explicit record that targets are missing. Missing targets are not a nuisance; they are a benchmark finding.

# Procedure

## 1. Define The Performance Question Precisely

Start with the business or engineering question:

- which journeys, endpoints, jobs, or pages matter
- which traffic pattern matters
- what threshold matters
- what failure looks like

Useful questions:

- Can this handle expected peak load?
- Which tier causes the current slowdown?
- Did the recent change regress user-perceived speed?

## 2. Establish Targets Or Record Their Absence

Collect the actual expectations:

- latency budget
- throughput target
- error-rate tolerance
- Core Web Vitals budget for UI work
- queue, batch, or background-job throughput expectations
- recovery expectations after overload

If no target exists, continue with measurement but return `needs target definition` as part of the verdict.

## 3. Capture A Baseline Before Any Optimization

Measure the current system first:

- steady-state latency
- percentile distribution
- throughput
- error rate
- resource utilization
- dependency timings

Never skip the baseline. Without it, later claims about improvement or regression are weak.

## 4. Model Realistic Load And Behavior

Build a load model that resembles real usage:

- expected concurrent users or requests
- traffic bursts and quiet periods
- read/write ratio
- key journey mix
- think time where relevant
- mobile, network, and device constraints for frontend work

Synthetic load that ignores real behavior often benchmarks the wrong thing.

## 5. Run Multiple Test Families

Choose the relevant mix:

- `load`: expected sustained traffic
- `stress`: beyond expected load to find breaking points
- `spike`: sudden jumps in traffic or events
- `endurance`: long-running stability and leak detection
- `frontend`: page-level and interaction-level user-perceived performance

Not every system needs every test family, but every chosen family needs a clear rationale.

## 6. Measure With Statistical Discipline

Report at least:

- P50, P95, and P99 latency when request timing matters
- throughput over time
- error rate
- saturation indicators such as CPU, memory, queue depth, DB pool, or rate-limit events
- before versus after comparisons if tuning work happened

Do not hide behind averages. Averages flatten the exact tail behavior that users feel first.

## 7. Connect Symptoms To Bottlenecks

Move from measurement to explanation:

- client-side rendering or asset bottleneck
- application-layer hot path
- database query or lock contention
- cache miss or invalidation pattern
- external dependency latency
- network or infrastructure constraint

A benchmark is incomplete if it shows the failure without investigating the likely cause.

## 8. Keep User-Perceived Performance In Scope

For user-facing systems, report technical speed and perceived speed together:

- initial render or content visibility
- interactivity delay
- layout stability
- long-task or jank indicators
- slow or degraded mobile behavior

A fast API paired with a sluggish interface is still a performance problem.

## 9. Produce Optimization Recommendations Only After Measurement

Recommendations should be ordered by:

- impact on the measured bottleneck
- effort to implement
- confidence level
- cost implications
- operational risk

Each recommendation should say what metric it is expected to improve. If you cannot connect the recommendation to a measured problem, it does not belong in the report.

## 10. Validate Improvements With Before And After Evidence

If optimizations were made:

- re-run the relevant benchmark
- compare against the same target and load model
- state whether the change moved the bottleneck or merely displaced it

Do not claim improvement based on intuition or a single quick rerun.

## 11. Return A Decision-Ready Report

Use a report structure like this:

```markdown
# Performance Benchmark Report

## Scope
- System or journey:
- Environment:
- Targets:
- Load model:

## Results
- Baseline:
- Load:
- Stress:
- Endurance:
- Frontend:

## Bottleneck Analysis
- Primary constraint:
- Secondary constraints:
- Confidence:

## Recommendations
1. [Priority] [Change]
   - Expected metric impact:
   - Effort:
   - Risk:

## Verdict
- PASS | FAIL | NEEDS TARGET DEFINITION
```

# Success Criteria

- The benchmark starts from a documented baseline.
- Tests reflect a stated load model instead of arbitrary traffic.
- Results use percentiles and error rates, not averages alone.
- The report distinguishes measurement, diagnosis, and recommendation.
- Any pass or fail claim is tied to explicit targets or an explicit note that no target exists.

# Common Failure Modes

- Tuning before baseline measurement.
- Running unrealistic synthetic traffic and treating it as representative.
- Reporting only average latency.
- Ignoring resource saturation and dependency behavior while chasing application code first.
- Claiming success because the system survived one short run.
- Offering optimization advice that is not tied to measured bottlenecks.

# Example Prompt

"Use talent `performance-benchmarking` on this system. Define the target and load model first, baseline the current state, run the relevant benchmark families, analyze the bottlenecks statistically, and return a pass or fail verdict with prioritized improvements."
