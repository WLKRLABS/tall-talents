---
slug: branch-finish-workflow
title: Finish open worktrees into the integration branch safely
summary: Inspect all open worktrees, separate real local edits from stale branch drift, commit each true delta, and fast-forward the integration branch without losing on-disk work.
tags:
  - git
  - worktree
  - branch
  - integration
triggers:
  - "User asks to finish, merge, or clean up multiple open Git worktrees."
  - "A repo has dirty feature worktrees whose branch tips may already be merged into the integration branch."
inputs:
  - Repo root and integration branch, usually `main`.
  - `git worktree list --porcelain` output.
  - Per-worktree `git status --short` and recent commit context.
outputs:
  - Every real on-disk change is either committed intentionally or explicitly left alone.
  - The integration branch contains the finished work.
  - Already-merged open worktrees are either confirmed clean or fast-forwarded to the integrated tip.
agent_behavior:
  - Inspect every worktree before deciding what needs a commit.
  - Distinguish stale branch drift from actual local edits before staging anything.
  - Prefer fast-forward merges when the finished branch is already linear on top of the integration branch.
safety:
  - Do not discard local changes unless you proved they are only stale branch drift created by branch normalization.
  - Do not assume editor buffers that are not on disk are available to commit.
  - Do not run concurrent write-heavy Git commands against the same shared repo metadata.
status: active
version: 1.0.0
---

# Goal

Finish all open worktrees into the integration branch without losing real work, accidentally recommitting already-merged history, or turning stale branch state into fake "new" changes.

## Use It When

- Multiple worktrees are open and the user wants everything committed and merged.
- At least one dirty worktree sits on a branch that may already be merged into `main`.
- Untracked files in one worktree could block merges from another.

## Do Not Use It When

- The worktrees represent intentionally separate efforts that should not be integrated together.
- Conflicts between branches change behavior and require product or design decisions.
- The repo is already in the middle of an unresolved merge, rebase, or cherry-pick. Resolve that state first.

# Procedure

## 1. Inventory The Real Worktree State

Read the actual repo state first:

- `git worktree list --porcelain`
- `git status --short` in the main worktree
- `git status --short` in each open worktree
- recent branch context such as `git log --oneline --decorate -5` or `git branch -vv`

Do not assume that every open worktree still has unique work. Some branches may already be merged and only left open locally.

## 2. Classify Each Worktree Before Editing Anything

For each worktree, decide which bucket it belongs to:

- clean and already merged: no commit needed
- dirty with real local changes: commit required
- dirty only because the branch base is stale relative to `main`: normalize first, then re-evaluate

This classification step prevents committing stale versions of files that only differ because the branch is old.

## 3. Check For Merge Blockers In The Integration Branch

Inspect the integration branch worktree for untracked files that would block incoming file additions.

If the integration branch already has real on-disk work, commit that first when it is part of the requested finish pass. This reduces collision risk and makes later worktree merges cleaner.

## 4. Normalize Stale Merged Branches Without Losing Local Files

When a dirty feature worktree sits on a branch whose tip is already merged into `main`, move the branch baseline up to `main` while preserving the working tree.

After normalization:

- re-check status
- discard only the diffs that were revealed solely because the old branch carried stale file versions
- keep any files that were already locally modified or untracked before normalization

The proof matters: if a file was not dirty before normalization, do not suddenly treat its stale content as a user edit.

## 5. Commit Each Real Delta With Intentional Scope

Commit the remaining per-worktree changes in the smallest honest units:

- main worktree on-disk changes that genuinely belong on the integration branch
- feature-worktree-only files or edits that still exist after branch normalization

Use commit messages that describe the actual delta, not the whole repo history.

## 6. Merge The Finished Branch Into The Integration Branch

Prefer a fast-forward merge when the finished branch is directly ahead of the integration branch:

- `git merge --ff-only <branch>`

If stateful Git commands appear hung inside an agent exec environment, retry them in a PTY before assuming repo corruption. Do not start low-level recovery while the command path itself is the real issue.

## 7. Bring Other Open Worktrees Up To The Integrated Tip

For clean worktrees whose branches were already merged earlier, fast-forward them to the new integration-branch tip when the goal is "finish all open worktrees" rather than merely land one branch.

This leaves the open worktree set aligned on the same finished commit instead of preserving stale local branch tips for no reason.

## 8. Verify The Final State

Run the repo-specific verification that matches the surfaces changed during the finish pass.

At minimum verify:

- the intended commits exist
- branch refs for the finished worktrees point at the integrated commit
- required repo validation hooks or scripts pass
- the user-facing changed files are present in the integrated worktree

If editor buffers were never written to disk, report that limitation explicitly instead of pretending they were committed.

# Success Criteria

- Every actual on-disk change was either committed intentionally or explicitly identified as stale branch drift and left out.
- `main` or the chosen integration branch contains the finished work.
- Open worktree branches that should now be aligned point to the integrated commit.
- No stale branch file versions were committed as fake new work.

# Common Failure Modes

- Committing a whole dirty worktree without checking whether most of the diff is just the branch being behind `main`.
- Letting an untracked file in `main` block a merge from a feature worktree.
- Treating a file that only became dirty after normalization as if it were a real user edit.
- Running concurrent merge, status, or ref-updating commands against the same shared worktree repo and then misdiagnosing the resulting hangs.
- Claiming unsaved editor buffers were committed when they never existed on disk.

# Example Prompt

"Use `branch-finish-workflow` on this repo. Inspect every open worktree, commit the real remaining deltas, merge them into `main`, and leave the open worktree refs aligned on the finished commit without losing local on-disk work."
