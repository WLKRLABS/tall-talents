---
slug: verification-gate
title: Verification Gate
summary: Block success claims until fresh commands, artifacts, and requirement checks prove the exact claim being made.
tags:
  - quality
  - verification
  - execution
triggers:
  - Before claiming work is done, fixed, passing, ready, or regression-safe.
  - Before commit, push, PR creation, handoff, or release recommendation.
  - After delegated work where the result must be verified independently.
inputs:
  - Exact claim being evaluated.
  - Repo-appropriate proving commands, artifacts, or requirement checklist.
  - Current code state and any recent changes since the last verification run.
outputs:
  - Evidence-backed status statement with fresh proof.
  - Explicit gap report when the claim is only partially proven or not proven.
agent_behavior:
  - Identify the exact claim before choosing the proof.
  - Run fresh verification after the final change, not from memory or earlier logs.
  - Narrow the claim when the evidence is narrower than the original wording.
safety:
  - Do not say done, fixed, passing, ready, or equivalent without fresh evidence.
  - Do not substitute nearby signals for the real proof required by the claim.
status: active
version: 1.0.0
---

# Goal

Prevent false completion, correctness, and readiness claims by forcing the agent to prove the exact statement it is about to make. This talent exists because code changes, green-looking logs, and optimistic language are not verification.

## Use It When

- A message would imply success, completion, readiness, or correctness.
- A bug is claimed fixed.
- A feature is claimed implemented.
- A branch is about to be finished, handed off, or merged.
- Another agent or tool reports success and that success must be trusted or rejected.

## Do Not Use It As The Primary Talent When

- The work is still in diagnosis mode and no success claim is being made yet. Use `systematic-debugging`.
- The question is a release go or no-go decision requiring multiple evidence streams. Use `release-readiness-audit`, which still applies this gate inside the audit.

# Procedure

## 1. Name The Claim Under Test

Rewrite vague status language into one testable sentence.

Examples:

- "The build succeeds."
- "The original login bug is fixed."
- "Task 3 is complete."
- "The release candidate is ready to ship."

If the claim is fuzzy, verification will be fuzzy. Tighten the claim first.

## 2. Identify The Proof Before Speaking

Decide what evidence would actually prove the claim.

Common pairings:

- Tests pass -> the exact test command output and exit code.
- Build succeeds -> the build command output and exit code.
- Bug fixed -> a repro of the original failure path that now passes.
- Requirements met -> a point-by-point checklist against the exact requirement source.
- Delegated task complete -> the actual diff plus direct verification of the changed behavior.

Use the narrowest full proof, not a proxy.

- A linter run does not prove a build.
- A passing unit test does not prove an end-to-end flow.
- A changed file does not prove a bug fix.
- A subagent saying "done" proves nothing by itself.

## 3. Run Fresh Verification After The Final Change

Verification must happen after the latest edit that could affect the claim.

- rerun the relevant command or artifact check fresh
- use the full command that proves the claim, not a shorter nearby check
- if the claim is broad, run the broad proof or narrow the claim

If the correct proof is expensive, say that explicitly and choose the strongest proof you actually ran. Never imply stronger evidence than you collected.

## 4. Read The Full Result

Do not stop at the first green-looking line.

Check:

- exit code
- total failures and skipped items
- warnings that materially weaken the claim
- the artifact path, contents, or screenshot you expected to generate
- whether a regression test fails for the right reason before the fix and passes after it when regression proof matters

Verification is not complete until the result is understood.

## 5. Cross-Check Evidence Against The Literal Claim

Ask whether the evidence proves the exact words you plan to use.

- "Build passes" requires a successful build.
- "Bug fixed" requires the original symptom path to stop failing.
- "Phase complete" requires every required item for the phase, not just one green command.
- "Agent completed the task" requires checking the real work product, not the agent's self-report.

If the proof is narrower than the claim, narrow the claim.

## 6. Report The Real Status

Use one of three outcomes.

### Proven

State the claim and the evidence together.

Examples:

- "`pytest tests/test_auth.py -q` exited 0; the targeted auth tests pass."
- "The original repro now passes under `npm test -- login-flow`; the bug is verified fixed for that path."

### Partially Proven

State exactly what is proven and what is still open.

Examples:

- "The build passes locally, but I did not run the browser smoke test."
- "The API path is verified; the release is not yet audited."

### Not Proven

State the failure or gap directly.

Examples:

- "The linter passes, but the build still fails."
- "The code changed, but I did not reproduce the original symptom yet, so I cannot claim the bug is fixed."

Do not soften an unproven result with optimism language.

## 7. Stop When The Proof Surface Is Incomplete

Do not push through the gate when:

- the proving command is unknown
- the required environment is unavailable
- the evidence is contradictory
- only partial verification was possible for a broad claim
- delegated work has not been independently checked

At that point, either:

- gather the missing evidence
- move into `systematic-debugging`
- widen into `release-readiness-audit`
- ask for the missing environment or decision

## 8. Use The Verification Note Format

Default reporting shape:

```markdown
## Verification Note
- Claim under test: [exact statement]
- Proof used: [commands, artifacts, or checklist]
- Result: Proven | Partially proven | Not proven
- Evidence:
  - [command or artifact]
  - [key outcome]
- Remaining gaps:
  - [none or explicit unverified surface]
```

## Anti-Rationalization Rules

- Ban "should", "probably", "seems", and celebratory language before proof.
- Confidence is not evidence.
- Partial verification only supports a partial claim.
- Exhaustion does not relax the gate.
- A subagent status message never replaces independent verification.
- If you do not know the proving command, finding it is part of the job.

## Integration Notes

- Use with `minimal-diff-execution` before declaring a patch done.
- Use with `code-review` before saying a reviewed chunk is safe to advance.
- Use with `branch-finish-workflow` before merge, PR, or cleanup decisions.
- Use inside `release-readiness-audit` for every readiness claim made in the audit.

# Success Criteria

- Every success claim is tied to fresh evidence.
- The evidence actually proves the literal claim being made.
- Partial proof produces a narrower claim instead of a false completion statement.
- Delegated work is independently checked before being trusted.
- Unverified gaps are reported plainly instead of being hidden behind optimistic wording.

# Common Failure Modes

- Claiming success because the code changed.
- Using a nearby green signal instead of the real proof.
- Reusing stale command output after later edits.
- Reporting a bug fixed without reproducing the original path.
- Closing a task because one check passed while other required criteria were skipped.
- Changing the wording to sound less definite while still implying success.

# Example Prompt

"Use `verification-gate` before you tell me this task is done. Name the exact claim, run the proving command or artifact check fresh, read the full result, and report what is proven, partially proven, or not proven."
