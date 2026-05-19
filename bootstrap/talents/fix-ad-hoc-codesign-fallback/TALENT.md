---
slug: fix-ad-hoc-codesign-fallback
title: Fix macOS ad-hoc codesign fallback for local binaries
summary: Restore runnable macOS binaries by removing invalid signatures and applying deterministic ad-hoc signing.
tags:
  - macos
  - codesign
  - cli
triggers:
  - "Binary fails with killed: 9 or code signature invalid errors after local build or patching."
inputs:
  - Path to target binary or app bundle executable.
  - Shell access with xcode command line tools.
outputs:
  - Binary executes without immediate signature termination.
  - codesign verification passes with ad-hoc identity.
agent_behavior:
  - Prefer minimal file changes and explicit command output checks.
  - Re-sign only target artifacts, not unrelated directories.
safety:
  - Do not recursively sign unknown trees.
  - Never use identity-based signing certificates unless explicitly requested.
status: active
version: 1.0.0
---

# Goal

Make a locally built or patched macOS executable runnable again by applying a valid ad-hoc signature after clearing stale signature state.

# Procedure

1. Confirm failure mode with direct execution.
2. Inspect existing signature:
   - `codesign -dvv <binary>`
3. Remove stale signature attributes if present:
   - `codesign --remove-signature <binary>`
4. Apply ad-hoc signature:
   - `codesign --force --sign - <binary>`
5. Verify:
   - `codesign --verify --verbose=2 <binary>`
   - `spctl --assess --type execute <binary>` (best-effort signal)
6. Re-run binary and confirm normal startup.

# Success Criteria

- Target executable no longer exits immediately with signature error.
- `codesign --verify` returns success.
- Commands are limited to explicit target paths.

# Common Failure Modes

- Signing the wrapper path instead of inner executable for `.app` bundles.
- Attempting deep recursive signing and mutating unrelated binaries.
- Assuming Gatekeeper assessment must pass for local ad-hoc testing; verify actual execution first.

# Example Prompt

"Use `fix-ad-hoc-codesign-fallback` on `./dist/mytool`, show exact verification output, and stop if signature still fails."
