---
slug: setup-matt-pocock-skills
title: Set Up Engineering Skill Context
summary: Scaffold the repo-local agent-skill configuration for issue trackers, triage labels, and domain docs before engineering workflow skills consume it.
tags:
  - setup
  - agents
  - workflow
triggers:
  - User wants to set up Matt Pocock engineering skills in a repo.
  - Skills such as to-issues, to-prd, triage, diagnose, tdd, improve-codebase-architecture, or zoom-out lack issue tracker, labels, or domain-doc context.
  - A repo needs AGENTS.md or CLAUDE.md agent-skill configuration plus docs/agents/*.md.
inputs:
  - Current repo files, git remote, AGENTS.md or CLAUDE.md, domain docs, and issue tracker preference.
  - User decisions for tracker, triage label vocabulary, and single-context or multi-context domain layout.
outputs:
  - Updated `## Agent skills` block in the existing agent instruction file.
  - `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and `docs/agents/domain.md`.
  - Clear note of which engineering skills now consume the setup.
agent_behavior:
  - Explore before asking and do not assume the repo uses GitHub.
  - Ask the three setup decisions one at a time.
  - Update an existing `## Agent skills` block in place instead of appending duplicates.
  - Prefer editing CLAUDE.md when it exists, otherwise AGENTS.md.
safety:
  - Do not create AGENTS.md when CLAUDE.md already exists, or vice versa.
  - Do not invent label names or issue tracker behavior when the user has not confirmed them.
  - Do not overwrite surrounding user-authored instructions.
status: active
version: 1.0.0
---

# Goal

Prepare a repository so engineering workflow talents and skills share the same issue tracker, triage vocabulary, and domain-documentation layout.

# Procedure

## 1. Explore Existing Repo State

Inspect before asking:

- `git remote -v` and `.git/config`
- root `CLAUDE.md` and `AGENTS.md`
- existing `## Agent skills` blocks
- root `CONTEXT.md` and `CONTEXT-MAP.md`
- root and context-local `docs/adr/`
- existing `docs/agents/`
- `.scratch/` or other local issue conventions

Summarize what exists and what is missing.

## 2. Decide Issue Tracker

Explain that skills such as `to-issues`, `to-prd`, and `triage` need to know where issues live.

Default:

- GitHub when a GitHub remote exists
- GitLab when a GitLab remote exists
- local markdown when no remote exists or the user prefers local work

Supported options:

- GitHub - use GitHub Issues and `gh`
- GitLab - use GitLab Issues and `glab`
- local markdown - write issues under a repo-local scratch path
- other - record the user's described workflow as prose

Ask this decision first and wait for the answer.

## 3. Decide Triage Label Vocabulary

Explain that `triage` uses canonical roles but the tracker may use different label strings.

Canonical state roles:

- `needs-triage`
- `needs-info`
- `ready-for-agent`
- `ready-for-human`
- `wontfix`

Default label string equals role name unless the user maps it differently.

Ask this decision second and wait for the answer.

## 4. Decide Domain Docs Layout

Explain that `diagnose`, `tdd`, `triage`, `zoom-out`, and `improve-codebase-architecture` use domain docs and ADRs to avoid renaming concepts casually.

Supported layouts:

- single-context - root `CONTEXT.md` plus root `docs/adr/`
- multi-context - root `CONTEXT-MAP.md` pointing to context-specific `CONTEXT.md` and ADR locations

Ask this decision third and wait for the answer.

## 5. Draft Before Writing

Show the user:

- the exact `## Agent skills` block
- `docs/agents/issue-tracker.md`
- `docs/agents/triage-labels.md`
- `docs/agents/domain.md`

Let the user correct it before files are written.

## 6. Write To The Existing Instruction Surface

Choose the instruction file:

- if `CLAUDE.md` exists, edit it
- else if `AGENTS.md` exists, edit it
- if neither exists, ask which one to create

If an `## Agent skills` block exists, replace only that block. Preserve surrounding instructions.

Block shape:

```markdown
## Agent skills

### Issue tracker

[one-line summary]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary]. See `docs/agents/triage-labels.md`.

### Domain docs

[single-context or multi-context summary]. See `docs/agents/domain.md`.
```

Then write the three `docs/agents/*.md` files.

## 7. Close With Consumer List

Report that the setup is complete and name the skills that will read the files:

- `to-issues`
- `to-prd`
- `triage`
- `diagnose`
- `tdd`
- `improve-codebase-architecture`
- `zoom-out`

# Success Criteria

- Existing repo conventions are inspected before setup decisions.
- The user confirms tracker, label vocabulary, and domain-doc layout.
- Only the correct agent instruction file is edited.
- Existing `## Agent skills` block is updated in place.
- `docs/agents` files match the chosen setup and can be edited directly later.

# Common Failure Modes

- Assuming GitHub because it is common.
- Dumping all setup questions at once.
- Creating both AGENTS.md and CLAUDE.md.
- Appending a duplicate `## Agent skills` block.
- Creating labels or tracker workflows the user did not confirm.

# Example Prompt

"Use `setup-matt-pocock-skills` in this repo. Inspect remotes and agent docs first, ask me the issue tracker, triage labels, and domain-doc layout decisions one at a time, then update the existing instruction file and `docs/agents` docs."
