# Tall Talents Plan

## Phase 1 — Contract (done in this repo)

- Define strict talent file format.
- Define status model (`active`, `draft`, `archived`).
- Define slug and filename constraints.
- Publish short strict rules.

## Phase 2 — Bootstrap (done in this repo)

- Provide initial `bootstrap/` root contents.
- Include live README, initial index, and 3 real talents.
- Include lifecycle folders (`incoming/`, `archive/`).

## Phase 3 — Enforcement (done in this repo)

- Add validator for front matter/sections/slug/status/duplicates.
- Add index rebuild script using active talents as source of truth.
- Add doctor/install scripts for reproducible setup.

## Phase 4 — Agent workflow hardening (done in this repo)

- Ship prompts for create/use/refine flows.
- Keep prompts grounded in real completed sessions.
- Prefer update-existing when overlap is high.

## Phase 5 — v1 hardening (done in this repo)

- Ensure clean CI run on macOS.
- Keep scripts small, deterministic, and dependency-light.
- Validate examples and bootstrap content stay in sync.

## v1.0.0 release gate

Release v1.0.0 only when:
- Install works on fresh macOS shell.
- Doctor passes on initialized `~/.tall-talents`.
- Validator passes on all active example talents.
- Rebuild script deterministically regenerates index.
- Documentation + rules + templates align with actual script behavior.
