---
slug: worktree-isolation
title: Worktree Isolation
summary: Create or confirm an isolated workspace on a dedicated branch, run setup, and prove the baseline is clean before implementation starts.
tags:
  - git
  - worktree
  - operations
triggers:
  - Substantial implementation work should not contaminate the current workspace.
  - A new branch and clean baseline are needed before executing a plan.
  - The environment may already provide an isolated linked worktree and must be detected correctly.
inputs:
  - Repo path and intended branch name.
  - Worktree location preference from repo docs or user direction.
  - Project setup and baseline verification commands.
outputs:
  - Ready isolated workspace path and branch, or an explicit statement that the current workspace is already the isolated surface.
  - Baseline setup result and clean or failing pre-work verification status.
agent_behavior:
  - Detect the current Git environment before creating anything.
  - Follow existing repo conventions for worktree location when they exist.
  - Treat baseline verification as mandatory before implementation begins.
safety:
  - Do not create nested or duplicate worktrees when the environment already provides isolation.
  - Do not use a project-local worktree directory until ignore rules are confirmed.
status: active
version: 1.0.0
---

# Goal

Start substantial work inside a clean isolated workspace, on the right branch, with setup complete and the baseline verified. This talent exists to prevent branch confusion, dirty main workspaces, and pre-existing failures from being mistaken for new regressions.

## Use It When

- starting a feature, fix, or execution batch that will touch multiple files
- the current workspace should remain clean
- a reviewed plan is about to move into implementation
- multiple workstreams must proceed in parallel without branch switching

## Do Not Use It When

- the task is read-only exploration
- the work is a tiny one-shot edit where isolation adds more risk than value
- the environment already guarantees a safe isolated workspace and no additional worktree is needed

# Procedure

## 1. Detect The Current Git Environment First

Before creating a worktree, inspect the workspace you are already in.

Minimum signals:

- `git rev-parse --git-dir`
- `git rev-parse --git-common-dir`
- `git branch --show-current`

Interpretation:

- different git-dir and git-common-dir -> you are already inside a linked worktree
- empty branch name -> detached HEAD or externally managed workspace
- normal branch and normal git-dir -> standard repo checkout

If you are already in a linked or externally managed isolated workspace, do not create a nested worktree just because the skill says "use worktrees." Treat the current workspace as the isolated surface and continue with setup and baseline verification.

## 2. Choose The Worktree Location By Precedence

When a new worktree is actually needed, choose the location in this order:

1. existing project-local `.worktrees/`
2. existing project-local `worktrees/`
3. repo instructions in `AGENTS.md`, `CLAUDE.md`, README, or equivalent local policy
4. explicit user preference
5. a configured global worktree root

If no convention exists, prefer the repo's documented policy. If none exists and the choice matters, ask once rather than guessing.

## 3. Verify Ignore Rules For Project-Local Worktrees

If the chosen location lives inside the repository, confirm Git ignores it before creation.

Why this is mandatory:

- tracked worktree directories pollute status
- accidental commits of nested checkout contents are expensive to unwind

If the directory is not ignored, fix that first or stop and surface the blocker. Do not create the worktree and "clean it up later."

## 4. Create The Branch And Worktree Deliberately

Use a dedicated branch name tied to the actual task.

Creation rules:

- one task or batch per branch
- no anonymous scratch branch names
- no reuse of a stale directory without checking what it already contains

Record:

- repo root
- branch name
- full worktree path
- whether the branch was newly created or reused

## 5. Run Project Setup Immediately

After entering the worktree, run the setup required to make it usable.

Typical detection points:

- `package.json` -> install JavaScript dependencies
- `Cargo.toml` -> build or fetch Rust dependencies
- `requirements.txt` or `pyproject.toml` -> install Python environment
- `go.mod` -> download Go modules

Also run any repo-specific bootstrap steps documented locally. The worktree is not ready just because the directory exists.

## 6. Prove A Clean Baseline Before Coding

Run a baseline verification command that tells you whether the branch starts from a known-good state.

Examples:

- test suite or targeted smoke test
- build command
- lint plus typecheck
- repo-specific doctor or validation script

If the baseline fails:

- report the failure before implementation starts
- separate pre-existing failures from future task work
- either investigate first or get explicit permission to proceed on top of a failing baseline

Do not quietly continue and then blame later failures on uncertainty.

## 7. Report The Workspace Contract

A finished setup report should include:

- workspace path
- branch name
- whether this was newly created or already isolated
- setup commands run
- baseline verification result
- any blocker or known pre-existing failure

Default format:

```markdown
## Worktree Setup
- Workspace: [full path]
- Branch: [name]
- Mode: new worktree | existing linked worktree | externally managed isolated workspace
- Setup: [commands run]
- Baseline: pass | fail
- Notes: [pre-existing failures or none]
```

## Decision Boundaries

- If the environment already gives you a linked worktree, skip creation and use it.
- If branch creation is blocked by the host environment but the workspace is already isolated, do not fight the sandbox; continue from the existing isolated path and report the constraint.
- If the baseline is failing, stop implementation until the failure is acknowledged or investigated.

## Integration Notes

- Use before `implementation-planning` moves into execution.
- Pair with `branch-finish-workflow` to close the loop after the work is done.
- Pair with `verification-gate` so setup and baseline claims are evidence-backed.

# Success Criteria

- Work begins in a clearly identified isolated workspace or a correctly detected equivalent.
- The chosen worktree location follows repo or user policy.
- Project-local worktree directories are ignored before use.
- Setup is complete enough to run the repo's baseline verification.
- Baseline status is known before implementation starts.

# Common Failure Modes

- Creating a nested worktree inside an already isolated environment.
- Guessing the worktree location instead of following repo policy.
- Skipping ignore verification for a project-local worktree directory.
- Calling the workspace ready before dependencies or bootstrap steps run.
- Starting implementation on top of a failing baseline without surfacing it.
- Reusing a stale worktree directory without checking its branch or local state.

# Example Prompt

"Use `worktree-isolation` for this repo before implementation starts. Detect whether the current workspace is already isolated, otherwise create a dedicated worktree on a task branch, run setup, verify the clean baseline, and report the workspace path and status."
