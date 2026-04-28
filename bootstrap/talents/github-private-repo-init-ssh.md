---
slug: github-private-repo-init-ssh
title: Initialize a private GitHub repo with SSH alias
summary: Turn a local project folder into a private GitHub repository, commit only safe files, bind origin to a specific SSH alias, and verify live access.
tags:
  - git
  - github
  - ssh
  - repo-init
triggers:
  - "A local folder needs to become a new private GitHub repo under a specific account using SSH."
  - "The target GitHub account is selected by SSH alias instead of the globally active gh account."
inputs:
  - Local project path.
  - Target GitHub owner/repo.
  - Target SSH host alias from `~/.ssh/config`.
  - Desired repo-local Git `user.name` and `user.email`.
outputs:
  - Local repo initialized on `main`.
  - Initial commit contains only files that should be tracked.
  - Private GitHub repository exists under the target owner.
  - `origin` uses the intended SSH host alias.
  - `main` is pushed and tracks `origin/main`.
agent_behavior:
  - Inspect ignores and untracked files before staging.
  - Treat `.env`, local runtime state, dependency folders, and system files as unsafe unless the user explicitly says otherwise.
  - Use the target account token or active account deliberately when creating the GitHub repo.
  - Prefer repo-local identity settings over global Git config changes.
  - Verify privacy, branch tracking, SSH remote access, and tracked-file exclusions before reporting success.
safety:
  - Do not print tokens, private key material, or secret file contents.
  - Do not commit ignored files by force unless explicitly requested.
  - Do not switch or rewrite global Git identity when repo-local config is enough.
status: active
version: 1.0.0
---

# Goal

Initialize a local project folder as a private GitHub repository for the intended account, using a specific SSH alias for Git operations and avoiding accidental secret commits.

# Procedure

1. Inspect the local folder and ignore rules:
   - `pwd`
   - `ls -la`
   - `find . -maxdepth 2 -type f -name '.gitignore' -print -exec sed -n '1,200p' {} \;`
   - Do not print `.env` or other likely secret files.
2. Inspect SSH and GitHub account state:
   - `sed -n '1,180p' ~/.ssh/config`
   - `ssh -G <alias> | rg '^(hostname|user|identityfile|identitiesonly|forwardagent) '`
   - `ssh -T -o BatchMode=yes <alias>`
   - `gh auth status`
   - `gh repo view <owner>/<repo> --json nameWithOwner,visibility,sshUrl,url`
3. Initialize Git if needed:
   - `git init -b main`
   - `git config user.name <name>`
   - `git config user.email <email>`
4. Confirm the stage set before committing:
   - `git status --short --ignored`
   - Verify `.env`, `.DS_Store`, `node_modules/`, runtime state folders, and any intentionally ignored planning/private folders are ignored or unstaged.
5. Commit the safe initial project files:
   - `git add .`
   - `git commit -m "Initial commit"`
6. Create the private GitHub repo under the intended owner:
   - If the intended account is not the active `gh` account, use its stored token without printing it:
     - `GH_TOKEN="$(gh auth token -u <user>)" gh repo create <owner>/<repo> --private`
   - Otherwise:
     - `gh repo create <owner>/<repo> --private`
7. Bind the local repo to the SSH alias and push:
   - `git remote add origin git@<alias>:<owner>/<repo>.git`
   - `git push -u origin main`
8. Verify the result:
   - `git remote -v`
   - `git status --short --branch`
   - `git ls-remote --heads origin`
   - `gh repo view <owner>/<repo> --json nameWithOwner,visibility,sshUrl,url,defaultBranchRef`
   - `git ls-files | rg '^(\\.env|node_modules/|\\.DS_Store|<private-folder>/)' || true`

# Success Criteria

- GitHub reports the repository as `PRIVATE`.
- `origin` uses `git@<alias>:<owner>/<repo>.git`.
- `main` tracks `origin/main`.
- `git ls-remote --heads origin` succeeds over SSH.
- Repo-local Git identity resolves to the intended account metadata.
- Secret, dependency, runtime, and intentionally ignored local files are not tracked.

# Common Failure Modes

- Creating the repo with the wrong active `gh` account.
- Letting `gh repo create --source --push` set `origin` to `git@github.com:` instead of the desired SSH alias.
- Accidentally committing `.env`, `.DS_Store`, `node_modules/`, or local runtime state before reviewing `git status --ignored`.
- Setting global Git identity when only one repo needed account-specific metadata.
- Treating the `ssh -T` exit code as failure even when GitHub prints the expected successful authentication message.

# Example Prompt

"Use `github-private-repo-init-ssh` to turn this local folder into a private GitHub repo under `<owner>` using SSH alias `<alias>`. Inspect ignores before staging, keep secrets out of the commit, create the repo with the intended account, set `origin` to the alias URL, push `main`, and verify privacy plus branch tracking."
