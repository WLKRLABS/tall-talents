---
slug: write-a-skill
title: Write An Agent Skill
summary: Create new agent skills with concise trigger metadata, progressive disclosure, bundled references, and scripts only when deterministic reuse justifies them.
tags:
  - skills
  - documentation
  - automation
triggers:
  - User wants to create, write, design, or improve an agent skill.
  - A reusable workflow should become a SKILL.md with optional references or helper scripts.
  - Existing skill instructions are too broad, too long, or missing trigger clarity.
inputs:
  - Task or domain the skill should cover.
  - Use cases, trigger phrases, expected inputs and outputs.
  - Reference material, examples, scripts, and target skill location when known.
outputs:
  - Skill folder containing `SKILL.md` and optional references, examples, or scripts.
  - Review checklist covering trigger quality, structure, size, terminology, and safety.
agent_behavior:
  - Start by clarifying the skill's task, triggers, and reusable workflow.
  - Keep SKILL.md concise and push rarely needed detail into one-level references.
  - Add scripts only for deterministic operations that would otherwise be generated repeatedly.
  - Verify the skill description is specific enough for an agent to choose it.
safety:
  - Do not include secrets, private identifiers, credentials, or time-sensitive claims.
  - Do not create broad persona wrappers without operational procedure.
  - Do not bury essential trigger information in reference files.
status: active
version: 1.0.0
---

# Goal

Turn a repeatable workflow into an agent skill that is easy for an agent to discover, load, and execute without bloating the initial context.

# Procedure

## 1. Gather Requirements

Clarify:

- task or domain the skill covers
- specific use cases
- trigger phrases and contexts
- expected inputs and outputs
- whether it needs scripts or only instructions
- reference materials to include

If the user already gave enough context, synthesize instead of interviewing.

## 2. Choose The Skill Shape

Default folder:

```text
skill-name/
  SKILL.md
  REFERENCE.md
  EXAMPLES.md
  scripts/
    helper.js
```

Only create optional files when they earn their keep.

Split content out of `SKILL.md` when:

- the main file would exceed roughly 100 lines
- advanced details are rarely needed
- distinct reference domains would distract from the main workflow

## 3. Write Discoverable Front Matter

The description is what the agent sees before loading the skill.

Requirements:

- 1024 characters or less
- first sentence says what the skill does
- second sentence says "Use when..."
- includes concrete triggers, file types, tools, or contexts
- distinguishes this skill from nearby skills

Weak:

```text
Helps with documents.
```

Strong:

```text
Extract text and tables from PDF files, fill forms, and merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

## 4. Draft SKILL.md

Use a compact main file:

```markdown
---
name: skill-name
description: [what it does]. Use when [specific triggers].
---

# Skill Name

## Quick Start

[Minimal working path.]

## Workflow

[Step-by-step procedure.]

## Advanced

See [REFERENCE.md](REFERENCE.md).
```

Write operational steps, constraints, and success criteria. Avoid persona tone, generic advice, and speculative best practices.

## 5. Add Scripts Only When They Improve Reliability

Add helper scripts when:

- the operation is deterministic
- validation or formatting needs exact handling
- the same code would otherwise be generated repeatedly
- error handling should be consistent

Do not add scripts for vague judgment, one-off work, or tool calls the agent can perform directly.

## 6. Review With A Publishability Pass

Before writing or shipping:

- remove secrets and credentials
- remove private customer data
- replace personal machine paths and private account identifiers unless intentionally public and necessary
- remove stale or time-sensitive claims
- ensure terminology is consistent
- ensure examples are concrete

## 7. Run The Skill Review Checklist

```markdown
- [ ] Description includes specific "Use when" triggers.
- [ ] SKILL.md stays concise.
- [ ] References are one level deep.
- [ ] Scripts are deterministic and justified.
- [ ] Terminology is consistent.
- [ ] No secrets or private identifiers are present.
- [ ] Workflow is operational, not persona-only.
```

# Success Criteria

- The skill is discoverable from its description alone.
- The main instructions fit in the agent's working memory.
- Extra files provide progressive disclosure instead of hiding required steps.
- Scripts are included only where they reduce repeated code generation or mistakes.
- The final artifact is safe to publish.

# Common Failure Modes

- Vague descriptions that do not tell the agent when to load the skill.
- Overlong SKILL.md files that should have references.
- Skill folders that are persona shells rather than reusable workflows.
- Adding scripts that are not deterministic.
- Including private paths, account names, credentials, or stale environment facts.

# Example Prompt

"Use `write-a-skill` to create a new skill for this workflow. Clarify the triggers and outputs, draft a concise SKILL.md with progressive references only where useful, add deterministic scripts if justified, and run the publishability checklist before writing files."
