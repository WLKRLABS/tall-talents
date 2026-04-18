---
slug: incident-response
title: Incident Response
summary: Turn a production incident into a structured response with severity classification, role assignment, time-boxed investigation, stable communication, and follow-through after recovery.
tags:
  - operations
  - incidents
  - reliability
triggers:
  - A production issue, outage, severe degradation, data integrity concern, or security event is actively affecting users or business operations.
  - The team needs a repeatable response system instead of ad hoc troubleshooting under pressure.
inputs:
  - Incident symptoms, affected surfaces, monitoring signals, and the current operational context.
  - Access to responders, runbooks, dashboards, and communication channels.
outputs:
  - Active incident command structure, mitigation and verification record, and stakeholder updates during the incident.
  - Post-incident timeline, root-cause analysis, and action items with owners and deadlines.
agent_behavior:
  - Stabilize first, analyze deeply second.
  - Assign explicit roles and keep communication cadence predictable.
  - Stay blameless while remaining strict about follow-through.
safety:
  - Do not skip severity classification, ownership, or timeline logging.
  - Do not call an incident resolved without metric-based verification and a monitoring period.
status: active
version: 1.0.0
---

# Goal

Replace panic and improvisation with a response model that reduces time to mitigation, keeps stakeholders informed, and converts outages into durable reliability improvements.

## Use It When

- Users are actively affected by production failure or major degradation.
- A security or data-integrity issue may be unfolding.
- A service issue requires cross-functional coordination under time pressure.

## Do Not Use It When

- The issue is a routine low-severity bug with no active user impact.
- The work is a post-release hardening review rather than a live incident.
- The real need is proactive operational automation. Use `devops-automation` for that.

## Incident Law

During an active incident:

- classify
- assign roles
- stabilize
- verify
- communicate
- then perform deeper root-cause work

If the service is still bleeding, do not let abstract diagnosis replace mitigation.

# Procedure

## 1. Detect, Confirm, And Declare

On the first credible signal:

- validate this is a real incident and not a false positive
- state the affected service or user-facing symptom
- classify initial severity
- open the incident channel, thread, or timeline

Default to over-clarity. Hidden incidents waste the first critical minutes.

## 2. Assign Roles Before The Response Fragments

At minimum assign:

- Incident Commander
- Technical Lead
- Communications Lead
- Scribe

One person can cover multiple roles in a smaller team, but the roles still need to exist explicitly.

Without role assignment, everyone starts troubleshooting and no one owns the timeline or the decisions.

## 3. Classify Severity And Set Cadence

Use a simple severity model such as:

- SEV1: full outage, data loss risk, security breach, or large-scale user impact
- SEV2: major degradation or key feature unavailable
- SEV3: partial degradation with workaround
- SEV4: low-impact operational issue

Severity determines:

- who gets paged
- update cadence
- escalation path
- acceptable response time

If impact grows or uncertainty worsens, upgrade severity quickly rather than protecting pride.

## 4. Build A Real-Time Timeline

Log:

- when the incident started or was first observed
- when it was declared
- every meaningful hypothesis
- every mitigation step
- every user-impact update
- when metrics recovered

The incident timeline is a core artifact, not clerical overhead. If it is missing, the post-mortem will be weak and the organization will relearn the same outage badly.

## 5. Time-Box Investigation Paths

Use short hypothesis loops:

- choose the most likely path
- gather evidence quickly
- if unconfirmed after the agreed window, pivot or escalate

Time-boxing prevents long, confident dead ends.

For high-severity incidents, a 15-minute hypothesis window is a good default unless the current path is clearly yielding evidence.

## 6. Mitigate Before Pursuing Perfect Understanding

Common mitigation options:

- rollback a recent deploy
- restart or fail over a bad component
- scale up capacity
- disable a feature flag
- activate a fallback or cache
- isolate the failing dependency

Choose the action that reduces user harm fastest while preserving safety.

Root cause can continue after the system is stable.

## 7. Verify Recovery With Metrics, Not Vibes

Before declaring resolution, confirm:

- user-facing function works
- error rates returned to baseline or acceptable bounds
- latency or throughput recovered
- no new alerts are cascading
- the fix holds for a monitoring period

Use a defined watch period after mitigation. "Looks fine now" is not enough.

## 8. Communicate On A Fixed Rhythm

Stakeholders should know:

- current status: investigating, identified, mitigating, monitoring, resolved
- impact
- what is being done
- when the next update will arrive

Send updates on the cadence implied by severity even if the update is "no change, still investigating."

Silence is interpreted as loss of control.

## 9. Close The Active Incident Deliberately

When the system is stable:

- announce resolution
- summarize impact and duration
- capture known remaining risk
- schedule the post-mortem within 48 hours

Do not let "we will write this up later" become the quiet end of the incident.

## 10. Run A Blameless Post-Mortem With Follow-Through

The post-mortem should include:

- executive summary
- impact
- timeline
- root cause and contributing factors
- what worked
- what failed
- action items with owner, priority, and due date

Use a systemic frame:

- what guardrail was missing?
- what signal failed to page soon enough?
- what documentation or ownership gap increased blast radius?

Action items without owners or deadlines do not count.

## Incident Command Template

```markdown
## Incident Status

- Severity:
- Incident Commander:
- Technical Lead:
- Communications Lead:
- Scribe:
- Current status:
- User impact:
- Next update at:
```

## Strong vs Weak Execution

Strong:

- declares and classifies early
- assigns roles immediately
- mitigates user harm before chasing perfect explanation
- verifies recovery with metrics
- runs the post-mortem quickly and tracks actions to closure

Weak:

- lets everyone troubleshoot without command structure
- delays severity classification to avoid escalation
- confuses "identified a possible cause" with "service recovered"
- stops communicating when there is no new information
- writes a post-mortem with no deadlines, owners, or follow-through

# Success Criteria

- The incident had an explicit command structure and severity level.
- Investigation and mitigation were documented in a real-time timeline.
- Stakeholders received predictable updates during the incident.
- Resolution was verified with observable recovery signals and a monitoring window.
- A blameless post-mortem was produced with owned action items.

# Common Failure Modes

- Skipping declaration because the team hopes the issue will clear quickly.
- Diving into technical debugging before assigning ownership and communication roles.
- Spending too long on one hypothesis during a high-severity outage.
- Declaring resolution before metrics and user impact actually normalize.
- Letting the post-mortem drift beyond the point where accurate recall is still easy.
- Failing to complete action items, which guarantees repeat incidents.

# Example Prompt

"Use `incident-response` for this outage. Classify severity, assign incident roles, run time-boxed investigation with mitigation-first thinking, send fixed-cadence updates, verify recovery with metrics, and finish with a post-mortem that includes owned action items."
