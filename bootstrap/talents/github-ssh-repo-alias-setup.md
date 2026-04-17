---
slug: github-ssh-repo-alias-setup
title: Set per-repo GitHub SSH identity via host alias
summary: Switch a local repo to a specific GitHub SSH key alias, pin repo-local Git identity, and verify safe auth plus remote access.
tags:
  - git
  - github
  - ssh
triggers:
  - "Repo is using the wrong GitHub account, wrong SSH key, or HTTPS instead of the intended SSH alias."
inputs:
  - Local repository path.
  - Target SSH host alias from `~/.ssh/config`.
  - Target GitHub `owner/repo`.
  - Desired repo-local Git `user.name` and `user.email`.
outputs:
  - `origin` uses the intended GitHub SSH host alias.
  - Repo-local Git identity is set explicitly.
  - Live SSH auth and `git ls-remote` both succeed.
agent_behavior:
  - Inspect existing SSH and Git config before changing anything.
  - Prefer repo-local identity changes over broad global Git config edits.
  - Verify with live network checks, not just static config reads.
safety:
  - Do not print private key material or modify unrelated SSH aliases.
  - Do not silently replace global Git identity when repo-local config is sufficient.
status: active
version: 1.0.0
---

# Goal

Bind one local repo to the intended GitHub SSH identity and confirm the setup works without leaking credentials through remote URLs or broad config changes.

# Procedure

1. Inspect SSH alias config:
   - `sed -n '1,120p' ~/.ssh/config`
2. Inspect the repo's current Git state:
   - `git -C <repo> remote -v`
   - `git -C <repo> config --list --show-origin`
3. Confirm effective SSH resolution for the target alias:
   - `ssh -G <alias> | rg '^(hostname|user|identityfile|identitiesonly|forwardagent) '`
4. Point the repo remote at the alias:
   - `git -C <repo> remote set-url origin git@<alias>:<owner>/<repo>.git`
5. Set repo-local Git identity:
   - `git -C <repo> config user.name <name>`
   - `git -C <repo> config user.email <email>`
6. Verify SSH auth for the alias:
   - `ssh -T -o BatchMode=yes <alias>`
7. Verify live repo access over that remote:
   - `git -C <repo> ls-remote --heads origin`
8. Recommended hardening check:
   - confirm `IdentitiesOnly yes`
   - confirm `forwardagent no`
   - confirm private key permissions are restricted (`600`)
   - review whether the private key is passphrase-protected

# Success Criteria

- Repo `origin` uses `git@<alias>:<owner>/<repo>.git`.
- `git config --show-origin --get user.name` and `user.email` resolve to the intended repo-local identity.
- `ssh -T` authenticates as the intended GitHub account.
- `git ls-remote --heads origin` succeeds without falling back to HTTPS credentials.

# Common Failure Modes

- Updating `origin` but leaving `user.name` or `user.email` tied to the wrong GitHub identity.
- Assuming SSH alias setup is active without checking `ssh -G <alias>`.
- Using a working alias but forgetting that commit metadata still exposes `user.name` and `user.email`.
- Leaving the private key unencrypted with no passphrase, which increases local compromise blast radius.
- Editing global Git config when only one repo needed account isolation.

# Example Prompt

"Use `github-ssh-repo-alias-setup` on `/path/to/repo` with alias `github-scwlkr`, set the repo-local identity, and verify both `ssh -T` and `git ls-remote --heads origin`."
