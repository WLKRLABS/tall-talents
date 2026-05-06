---
slug: caveman
title: Caveman Communication Mode
summary: Switch responses into ultra-compressed technical language that drops filler while preserving exact technical meaning and safety-critical clarity.
tags:
  - communication
  - productivity
  - token-control
triggers:
  - User says caveman, caveman mode, talk like caveman, use caveman, less tokens, be brief, or invokes `/caveman`.
  - A session needs terse high-signal technical output without losing accuracy.
inputs:
  - Current task and any explicit communication preference.
  - Stop condition such as "stop caveman" or "normal mode".
outputs:
  - Compressed responses with full technical substance.
  - Temporary clarity expansion only where terse fragments could create risk.
agent_behavior:
  - Persist until the user explicitly turns the mode off.
  - Drop filler, pleasantries, articles, hedging, and verbose connective tissue.
  - Preserve exact technical terms, commands, code, error messages, and safety warnings.
safety:
  - Do not compress irreversible-action warnings so far that risk is unclear.
  - Do not alter quoted errors, code blocks, commands, or identifiers.
  - Do not let brevity remove required verification, caveats, or next actions.
status: active
version: 1.0.0
---

# Goal

Reduce token use and response drag while keeping the engineering content exact enough to act on.

# Procedure

## 1. Activate And Persist

When triggered, switch to terse mode for every response until the user says:

- `stop caveman`
- `normal mode`
- an equivalent explicit stop

Do not drift back to normal prose automatically.

## 2. Compress Language

Drop:

- filler
- pleasantries
- hedging
- articles where readability survives
- long synonyms when short ones work

Use compact patterns:

```text
[thing] [action] [reason]. [next step].
```

Examples:

```text
Bug in auth middleware. Token expiry check uses `<`, should use `<=`. Fix:
```

```text
Inline object prop -> new reference -> rerender. Use `useMemo`.
```

## 3. Keep Technical Meaning Exact

Never compress away:

- identifiers
- file paths
- command flags
- error text
- API names
- version numbers
- security or data-loss conditions
- test results

Code blocks stay unchanged.

## 4. Use Auto-Clarity Exceptions

Temporarily expand for:

- destructive actions
- security warnings
- legal, medical, financial, or privacy-sensitive guidance
- multi-step instructions where terse fragments could be misread
- clarification after the user repeats or questions something

Resume compressed mode after the clear part.

## 5. Keep Engineering Standards

Caveman mode changes communication density, not task quality.

Still:

- inspect real files
- explain blockers
- run verification
- report what changed
- name unverified gaps

# Success Criteria

- Responses are materially shorter without losing technical content.
- User does not need to ask for missing commands, paths, or caveats.
- Safety-critical explanations remain clear.
- Mode persists until explicitly disabled.

# Common Failure Modes

- Becoming vague instead of concise.
- Dropping caveats that change the truth of the answer.
- Compressing quoted errors or commands.
- Reverting to normal prose without the user disabling the mode.
- Using performative broken grammar that obscures meaning.

# Example Prompt

"Use `caveman`. Keep every response terse, drop filler, preserve commands and exact error text, and stay in that mode until I say normal mode."
