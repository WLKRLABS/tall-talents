---
slug: to-issues
title: Turn Plans Into Issues
summary: Break a plan, spec, or PRD into independently grabbable issue-tracker tickets using thin vertical tracer-bullet slices.
tags:
  - issues
  - planning
  - delivery
triggers:
  - User wants to convert a plan, spec, PRD, or conversation into implementation issues.
  - Work needs to be split into independently grabbable tasks for humans or agents.
  - User asks for vertical-slice tickets or a GitHub issue breakdown.
inputs:
  - Source plan, spec, PRD, issue, or current conversation context.
  - Issue tracker configuration and triage label vocabulary.
  - Repo context, domain glossary, and ADRs when available.
outputs:
  - Approved vertical-slice issue breakdown.
  - Published issues in dependency order with acceptance criteria and `needs-triage` role.
agent_behavior:
  - Prefer thin vertical slices over layer-by-layer tasks.
  - Mark slices as AFK or HITL based on whether human decisions are still required.
  - Ask the user to approve granularity and dependencies before publishing.
safety:
  - Do not publish issues until the user approves the breakdown.
  - Do not close or modify a parent issue while creating child issues.
  - Do not create horizontal layer tickets such as schema-only, API-only, or UI-only unless they are independently valuable and verifiable.
status: active
version: 1.0.0
---

# Goal

Convert plans into issue-tracker work that a human or agent can pick up independently, finish, and verify without needing the entire plan in their head.

# Procedure

## 1. Gather Source Context

Use the current conversation context by default.

If the user provides an issue number, URL, or local path, fetch and read the full body and comments before drafting.

Confirm the issue tracker and triage label vocabulary exist. If not, run `setup-matt-pocock-skills` first.

## 2. Explore The Codebase When Needed

If the implementation surface is not already known:

- inspect relevant repo files
- use `CONTEXT.md` vocabulary in issue titles and descriptions
- respect ADRs in the area
- avoid file-path-heavy issue bodies unless the repo convention expects them

## 3. Draft Vertical Slices

Each issue should be a thin complete path through all layers needed for a demoable or verifiable result.

For each slice, state:

- **Title**
- **Type** - AFK or HITL
- **Blocked by**
- **User stories covered**
- **Acceptance criteria**

AFK slices can be implemented and verified without human interaction. HITL slices require decisions, design review, manual validation, external access, or judgment that should not be delegated blindly.

## 4. Quiz The User Before Publishing

Present the proposed breakdown and ask:

- does the granularity feel right?
- are dependencies correct?
- should slices be merged or split?
- are AFK and HITL labels correct?

Iterate until approved.

## 5. Publish In Dependency Order

Create blockers first so dependent tickets can reference real issue IDs.

Apply the configured `needs-triage` role to each new issue.

Use this body shape:

```markdown
## Parent

[Parent issue reference, if any.]

## What to build

[Concise end-to-end behavior for this vertical slice.]

## Acceptance criteria

- [ ] [criterion]

## Blocked by

[Issue reference or "None - can start immediately."]
```

Do not close or modify the parent issue.

## 6. Report The Published Set

Return:

- issue links or IDs
- dependency order
- AFK/HITL classification
- any follow-up triage needed

# Success Criteria

- Every issue is independently grabbable.
- Each slice is vertical, demoable, and acceptance-driven.
- Dependencies are explicit and published in order.
- User approved the breakdown before issue creation.
- Parent issues remain intact.

# Common Failure Modes

- Creating one ticket per technical layer.
- Publishing before the maintainer approves granularity.
- Making tickets too broad for one agent to finish safely.
- Omitting dependencies and forcing future agents to rediscover order.
- Modifying or closing the parent issue by accident.

# Example Prompt

"Use `to-issues` on this PRD. Read the source context, draft thin vertical AFK/HITL slices with dependencies and acceptance criteria, get my approval on the breakdown, then publish issues in dependency order with `needs-triage`."
