---
slug: vercel-git-connect-ssh-alias
title: Connect Vercel Git when local origin uses a GitHub SSH alias
summary: Attach a Vercel project to its GitHub repository without losing a repo-local custom SSH host alias used for local pushes.
tags:
  - vercel
  - github
  - deploy
  - ssh
triggers:
  - "Vercel Git auto-deploys are missing because the local Git remote uses a custom SSH host alias."
  - "`vercel git connect` fails while parsing a non-canonical GitHub SSH alias such as `git@github-work:owner/repo.git`."
inputs:
  - Local repository path.
  - Vercel project name or linked `.vercel/project.json`.
  - Canonical GitHub repository URL.
  - Existing local SSH alias remote URL.
outputs:
  - Vercel project connected to the canonical GitHub repository.
  - Local `origin` restored to the intended SSH alias.
  - A real Git push triggers and verifies a Vercel production deployment.
agent_behavior:
  - Preserve the local SSH alias instead of replacing it permanently with HTTPS or `github.com`.
  - Treat a successful manual Vercel deploy as insufficient proof of Git auto-deploys.
  - Verify with a fresh Git-triggered deployment when a safe commit is available.
safety:
  - Do not print Vercel or GitHub tokens.
  - Do not leave `origin` on HTTPS if the repo intentionally uses a custom SSH identity alias.
  - Do not push an empty or unrelated commit just to test automation unless the user approves it.
status: active
version: 1.0.0
---

# Goal

Repair Vercel Git auto-deploys for a repo that intentionally uses a custom GitHub SSH host alias locally, while preserving that alias for future pushes.

# Procedure

1. Inspect current state:
   - `git remote -v`
   - `git status --short --branch`
   - `vercel project inspect <project>`
   - `vercel ls <project>`
2. Confirm the canonical GitHub repository URL independently:
   - `gh repo view <owner>/<repo> --json url,sshUrl,defaultBranchRef,visibility`
   - If the active `gh` account is wrong, use the intended account token without printing it.
3. Try the direct Vercel connection first:
   - `vercel git connect https://github.com/<owner>/<repo>`
4. If Vercel fails while parsing the custom SSH alias, temporarily canonicalize `origin`, connect, then restore the original remote:

```bash
original_remote="$(git remote get-url origin)"
git remote set-url origin https://github.com/<owner>/<repo>.git
vercel git connect https://github.com/<owner>/<repo>
git remote set-url origin "$original_remote"
```

5. Verify local Git state was restored:
   - `git remote -v`
   - `git ls-remote --heads origin`
6. If there is a meaningful safe change to push, commit and push it to the production branch.
7. Verify Vercel created a new Git-triggered deployment:
   - `vercel ls <project>`
   - `vercel inspect <new-deployment-url> --wait --timeout 5m`

# Success Criteria

- `vercel git connect` reports the GitHub repository as connected.
- Local `origin` still uses the intended SSH alias.
- `git ls-remote --heads origin` succeeds through the alias.
- A push to the production branch creates a new Vercel deployment.
- The new deployment reaches `Ready` and includes the expected production aliases.

# Common Failure Modes

- Assuming a manual `vercel --prod` deployment proves Git auto-deploys.
- Leaving `origin` on HTTPS after using it only as a temporary Vercel CLI workaround.
- Running Vercel commands under the wrong team or scope.
- Verifying GitHub access with the wrong active `gh` account.
- Creating noise commits solely to test deploy automation.

# Example Prompt

"Fix Vercel Git auto-deploys for this repo. Local `origin` uses `git@github-work:owner/repo.git`, and Vercel is not connected to GitHub."
