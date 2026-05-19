---
slug: release-cut-and-publish
title: Release Cut And Publish
summary: Harden repo-controlled release gaps, cut a versioned release through the repo's own scripts, push the branch and tag, and verify the published GitHub release end to end.
tags:
  - release
  - versioning
  - github
  - deployment
triggers:
  - The user asks to take a repo all the way to a shipped version such as `v1.0.0`.
  - A project is close to release but still has repo-controlled blockers in packaging, installer behavior, docs, CI, or release automation.
  - The task requires more than readiness judgment and must finish with a pushed tag and verified GitHub release.
inputs:
  - Repository with a version source of truth, changelog, and script-backed release flow.
  - GitHub auth and push access for the target remote.
  - Exact target version and intended release assets.
outputs:
  - Repo-controlled release blockers fixed or support boundaries narrowed honestly before the cut.
  - Release-prep commit, annotated tag, pushed branch and tag, and successful GitHub release workflow.
  - Published GitHub release with the intended assets, release notes, and local version/install verification.
agent_behavior:
  - Fix repo-controlled release blockers before bumping the version.
  - Prefer the repository's own prepare, package, verify, tag, and install scripts over ad hoc commands.
  - Narrow unsupported claims explicitly instead of faking distribution, signing, or platform support.
safety:
  - Do not tag or push if validation, packaging, or release verification fails.
  - Do not claim notarization, universal support, or release trust properties that the repo does not actually prove.
  - Do not bump `VERSION` outside the release-prep path unless the repo's release process explicitly requires it.
status: active
version: 1.0.0
---

# Goal

Take a repository from "close to releasable" to an actually shipped versioned release by closing repo-controlled gaps first, then executing the full prepare, verify, tag, push, and publish loop with evidence at each step.

# Procedure

1. Inspect the release boundary before changing anything:
   - confirm the current branch and worktree are clean enough for release work
   - read the repo's versioning policy, changelog rules, release scripts, and release workflow
   - confirm the target version, release assets, and remote push destination
2. Audit repo-controlled blockers that would make the release dishonest or unstable:
   - installer pinned to `main` instead of a versioned release
   - release assets missing checksums or install verification
   - CI only proving raw builds instead of packaged release artifacts
   - stale pre-release docs, placeholder support claims, or versioning guidance that contradict the intended release
3. Fix those blockers before the cut:
   - harden installer, packaging, verification, CI, workflow, and docs
   - if a property cannot be made true in-repo, narrow the documented support boundary instead of pretending
   - add or update changelog entries for the release-worthy user-visible changes
4. Run the repo's pre-release validation on the unreleased tree:
   - versioning validation
   - smoke/build/tests
   - package and verify release artifacts
   - installer verification when the repo ships an installer
5. Commit the release-hardening work separately if it is distinct from release prep.
6. Run the repo-native release prep command for the target version and include install/update if the repo uses it.
7. Verify the prepared release candidate:
   - built artifact version matches the target version
   - installed local version matches the target version
   - intended release assets exist
   - release notes match the changelog section
8. Commit the release prep as `release: vX.Y.Z`, create the annotated tag with the repo script, and push the branch and tag.
9. Watch the GitHub release workflow to completion and verify the published release contains the intended assets and notes.

# Success Criteria

- The repository is not just "ready"; the release commit, tag, push, and published GitHub release all exist.
- Repo-controlled blockers were either fixed or converted into explicit support limits before the version cut.
- Packaged release artifacts and installer behavior are verified against the target version.
- GitHub release assets and notes match the actual release intent.
- The final state is evidence-backed: clean local repo, pushed tag, successful workflow, and published release URL.

# Common Failure Modes

- Jumping straight to `vX.Y.Z` without first fixing installer, packaging, docs, or CI gaps that make the release misleading.
- Using ad hoc release commands instead of the repository's own prepare/tag scripts and drifting from the documented flow.
- Letting remote install behavior fall back to a moving branch head instead of the matching release version.
- Claiming support properties such as notarization or universal binaries because they are desirable, not because the repo proves them.
- Bumping the version and tagging before the packaged release has been verified locally.
- Stopping after tag push without verifying the GitHub release workflow and published assets.

# Example Prompt

"Use `release-cut-and-publish` to take this repo to `v1.0.0`. Fix repo-controlled release blockers first, then run the repo's release-prep flow, verify the artifacts and installed version, push the release commit and tag, and confirm the published GitHub release URL and assets."
