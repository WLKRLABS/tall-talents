---
slug: devops-automation
title: DevOps Automation
summary: Build delivery and infrastructure automation that is reproducible, observable, reversible, and secure enough to run in production.
tags:
  - devops
  - infrastructure
  - automation
triggers:
  - A team needs CI/CD, infrastructure-as-code, rollout safety, monitoring, backup, or recovery automation.
  - Manual operational steps are creating reliability, speed, or security problems.
inputs:
  - Current deployment process, infrastructure shape, environments, and operational constraints.
  - Application architecture, compliance constraints, and service reliability requirements.
outputs:
  - Automated infrastructure and delivery design with rollout, rollback, observability, and recovery paths.
  - Validation evidence for the automation, including health checks, alerting, and recovery confidence.
agent_behavior:
  - Treat automation, observability, rollback, and recovery as one operating system rather than separate chores.
  - Prefer vendor-neutral patterns unless the current platform requires something specific.
  - Eliminate manual steps only when the automated replacement is actually safer and testable.
safety:
  - Do not ship pipeline or infrastructure automation without rollback and monitoring.
  - Do not encode secrets, unsafe defaults, or unreviewed production changes into the automation layer.
status: active
version: 1.0.0
---

# Goal

Create an operations baseline where infrastructure and delivery are reproducible, deployments are guarded, incidents are easier to contain, and manual toil steadily disappears instead of hiding in tribal knowledge.

## Use It When

- Deployments depend on manual shell steps or personal knowledge.
- Environments drift because infrastructure is not codified.
- Releases need consistent testing, rollout, and rollback behavior.
- Monitoring, backups, or recovery are under-specified or partially manual.

## Do Not Use It When

- The work is a one-off local development script with no operational consequence.
- The system is still at pure experimentation stage and production automation would be fiction.
- The main issue is active incident coordination rather than preventative ops design. Use `incident-response` for the live incident first.

## Operating Standard

No production automation is complete unless it addresses:

- build and deploy path
- rollback path
- observability
- secret handling
- backup and recovery
- validation of the automation itself

# Procedure

## 1. Assess The Current Operating Surface

Inventory:

- environments: local, staging, production, ephemeral previews
- current deployment steps and who performs them
- infra components and ownership
- failure history or known pain points
- security and compliance constraints

If the current system cannot be described clearly, do not start by writing pipeline YAML. Start by understanding the real operating model.

## 2. Define The Desired Delivery Flow

Specify the full path from change to production:

- source control and branch policy
- required checks
- artifact build path
- promotion model across environments
- deployment strategy: rolling, canary, blue-green, etc.
- rollback triggers and rollback operator

The deployment path must be explicit enough that a new operator could explain what happens at each gate.

## 3. Encode Infrastructure And Pipeline As Reviewable Artifacts

Prefer declarative, versioned definitions:

- infrastructure-as-code
- pipeline configs
- environment templates
- alert rules
- backup jobs
- restore procedures

Manual runbooks still matter, but they should explain the automation, not substitute for missing automation.

## 4. Build In Safety Controls From The Start

Every automated path should include:

- health checks
- deployment verification
- automatic or well-defined rollback
- secrets management
- access control
- auditability

Fast deployment without controlled rollback is just faster outage creation.

## 5. Treat Observability As A First-Class Deliverable

Define:

- what metrics matter
- what logs must exist
- what traces or correlation IDs matter
- what alerts should page vs ticket vs dashboard only
- who receives each alert

Alerting that cannot be acted on is noise. Dashboards without thresholds are decoration.

## 6. Automate Recovery, Not Just Deployment

Build or document automation for:

- backups
- restore verification
- disaster recovery steps
- restart or failover paths
- scaling policies
- degraded-mode or fallback mechanisms

A pipeline that only gets code into production is not enough. Production also needs a practiced way back out of trouble.

## 7. Validate The Automation End To End

Run checks such as:

- pipeline execution on safe changes
- deployment health verification
- rollback drill
- restore drill
- alert firing validation
- secret-injection or permission validation

If backup restore was never tested, you do not have a backup system. You have hope stored in another location.

## 8. Include Cost And Operability In The Design

Assess:

- wasteful overprovisioning
- hidden human maintenance cost
- vendor lock-in pressure
- noisy alerts or brittle deploy steps
- operational burden created by advanced tooling

Choose the simplest automation stack that reliably serves the current scale and risk profile.

## 9. Leave Behind An Operations Package

Document:

- architecture and environment map
- deployment and rollback flow
- alert and dashboard map
- backup and recovery expectations
- known limitations
- next hardening priorities

Automation without an understandable package is still fragile because only the original author knows what it is supposed to do.

## DevOps Automation Review Template

```markdown
## DevOps Automation Review

- Delivery flow defined:
- Rollback path defined:
- Monitoring and alerting in place:
- Backup and recovery validated:
- Security controls embedded:
- Remaining manual steps:
```

## Strong vs Weak Execution

Strong:

- starts with the actual operating surface
- treats deployment, rollback, monitoring, and recovery as one system
- keeps automation reviewable and versioned
- validates drills rather than assuming they will work
- balances reliability with operational simplicity

Weak:

- writes pipeline automation before understanding the environments
- automates deploys but not rollbacks
- adds dashboards with no actionable alerts
- stores secrets unsafely for convenience
- declares recovery readiness without ever testing restore

# Success Criteria

- Delivery and infrastructure flows are encoded as reviewable automation.
- Rollback, monitoring, and recovery are part of the design, not follow-up chores.
- The automation has been validated through real checks or drills.
- Security and access controls are embedded in the operating model.
- The resulting system reduces toil without introducing brittle or opaque complexity.

# Common Failure Modes

- Automating the happy path only and ignoring failure handling.
- Building environment-specific snowflakes instead of reusable definitions.
- Shipping monitoring after deployment instead of with it.
- Assuming backups are sufficient without restore verification.
- Letting manual, undocumented steps survive inside "automated" release flows.
- Choosing tool sprawl over a maintainable operating model.

# Example Prompt

"Use `devops-automation` on this delivery surface. Assess the current operating model first, define the deployment and rollback flow, codify infra and pipelines as reviewable artifacts, embed monitoring and backup/recovery, validate the automation with drills or checks, and report any remaining manual or risky steps."
