---
slug: repo-onboarding-map
title: Repo Onboarding Map
summary: Build a facts-only orientation or zoom-out map of an unfamiliar repo, subsystem, module graph, or caller chain by reading code and stating exactly what was inspected.
tags:
  - research
  - onboarding
  - codebase
triggers:
  - A user asks what a repo does, where to start, or what owns a behavior.
  - User says "zoom out" because they do not know a section of code well and need the broader module/caller map.
  - A new engineer or agent needs fast orientation before making changes.
  - Repository structure, entry points, and boundaries must be explained without drifting into redesign.
inputs:
  - Repository tree and relevant source files.
  - Specific subsystem or behavior questions when present.
  - Available manifests, entry points, routers, commands, and config files.
  - Domain glossary and ADRs when the repo provides them.
outputs:
  - One-line summary, five-minute explanation, and deep dive.
  - Explicit list of files inspected, modules and callers mapped, and boundaries traced.
agent_behavior:
  - State only facts grounded in inspected code.
  - Follow real request, event, command, or data paths through the system.
  - Use the project's domain glossary vocabulary when it exists.
  - Be explicit about what was not inspected or what remains partial.
safety:
  - Do not turn onboarding output into a code review, redesign, or implementation plan.
  - Do not state ownership or behavior that cannot be tied to inspected files.
status: active
version: 1.1.0
---

# Goal

Shorten time-to-understanding for an unfamiliar codebase by producing a high-signal orientation map grounded in actual files and execution paths. This talent exists to replace vague repo summaries with traceable, read-only understanding.

## Use It When

- onboarding into a new repo
- answering "where should I start"
- identifying which files own a behavior
- mapping structure before design, planning, or debugging work

## Do Not Use It When

- the user wants recommendations or code changes rather than orientation
- the output is supposed to judge quality, propose refactors, or choose an architecture

# Procedure

## 1. Inventory The Repo Surface

Start with the top-level structure and framework signals:

- manifests and lockfiles
- build or runtime config
- top-level directories
- app, package, service, library, or monorepo markers

Goal:

- determine what kind of repo this is
- identify which directories actually contain code
- avoid spending time on generated, cached, or non-executable surfaces unless they affect startup

## 2. Identify The True Entry Points

Find the smallest set of files that explain how the system starts or how the requested behavior enters the codebase.

Common entry classes:

- CLI main files and command registration
- web server bootstrap and routers
- framework app initializers
- package exports
- workers, schedulers, cron tasks, and background jobs

Do not guess. Tie every claimed entry point to a real file.

## 3. Trace Concrete Execution Paths

For each requested area, follow the path end to end:

- where input enters
- where validation happens
- where orchestration happens
- where core logic lives
- where persistence or external I/O happens
- how the result returns

Name the files involved in order. If the path forks, say where it forks and why.

## 4. Map Boundaries And Responsibilities

Separate the system into real seams visible in code:

- presentation or interface layer
- application or orchestration layer
- domain logic
- persistence or external integration layer
- cross-cutting concerns such as config, auth, logging, jobs

Also note confusing spots that matter for onboarding:

- modules whose names mislead about their real role
- duplicate abstractions
- files that look important but are generated or thin wrappers

State these as code-grounded observations, not judgments.

## 4A. Zoom-Out Mode

When the user asks to "zoom out" from an unfamiliar section of code, keep the scope narrower than a full repo onboarding map:

- identify the current file, module, function, or behavior being discussed
- go one layer up and list relevant callers, owners, adapters, and downstream effects
- explain how the area fits into the larger domain using `CONTEXT.md` vocabulary when present
- include the files that would be the next best reads for deeper understanding
- avoid recommendations unless the user explicitly asks for next actions

Default zoom-out output:

```markdown
## Zoom-Out Map
- Current area:
- What calls it:
- What it calls:
- Domain role:
- Important adjacent modules:
- Why this area matters:
- Files inspected:
- Best next files to read:
```

## 5. Keep The Output Strictly Factual

This talent is read-only and explanation-only.

Do not:

- recommend changes
- evaluate whether the code is good or bad
- suggest a better architecture
- sneak in review findings

If the user later wants design, planning, debugging, or implementation advice, switch talents after the orientation map is done.

## 6. Be Honest About Coverage

State exactly what was inspected and what was not.

If you only traced one subsystem:

- say that clearly
- list the files inspected
- avoid implying full-repo understanding

Partial but honest maps are more useful than broad but invented ones.

## 7. Return Three Levels Of Understanding

Default output shape:

```markdown
# Codebase Orientation Map

## 1-Line Summary
[one sentence stating what this codebase is]

## 5-Minute Explanation
- Primary tasks in code: [...]
- Primary inputs: [...]
- Primary outputs: [...]
- Key files: [...]
- Main code paths: [...]

## Deep Dive
- Type: [...]
- Primary runtime(s): [...]
- Entry points:
  - `[path]`: [why it matters]
- Top-level structure:
  - `[path]`: [purpose]
- Key boundaries:
  - Presentation: [...]
  - Application: [...]
  - Persistence or external I/O: [...]
- Detailed code flows:
  1. `[entry]` -> `[router]` -> `[service]` -> `[storage or external call]` -> `[output]`
- Files inspected:
  - `[path]`
- Files not inspected:
  - `[path or "not exhaustive"]`
```

## Decision Boundaries

- If the repo is too large to map completely in one pass, narrow the question and say so.
- If multiple runtimes or packages exist, explain their relationships before diving deep into one of them.
- If the user asks "where should I start," answer with the first concrete files to read, based on traced entry points, not personal preference.

## Integration Notes

- Use before `design-before-build` when the current system is not yet understood.
- Use before `implementation-planning` when the file map is still fuzzy.
- Use before `systematic-debugging` when the failing behavior's ownership is unknown.

# Success Criteria

- The orientation map is grounded in inspected code.
- Entry points and code paths point to real files.
- The output helps a new engineer understand the repo quickly without over-claiming coverage.
- The answer stays descriptive and read-only.
- Files inspected and not inspected are stated clearly.

# Common Failure Modes

- Describing a repo from filenames alone without tracing code paths.
- Turning the map into a design critique or refactor plan.
- Claiming full understanding after reading one subsystem.
- Mixing inferred intent with observed behavior.
- Omitting the inspected-file list and hiding the actual coverage.

# Example Prompt

"Use `repo-onboarding-map` on this repository. Build a facts-only orientation map from the real code, show the entry points and main paths, and state exactly which files you inspected."
