---
slug: repo-talent-acquisition-pass
title: Acquire reusable talents from external repositories
summary: Scan external repositories for durable workflows, normalize them into Tall Talents candidates, merge overlaps, and produce a prioritized port plan with source traceability.
tags:
  - research
  - synthesis
  - talent-library
triggers:
  - "User asks to mine one or more repos for reusable talents, workflows, or operating patterns."
  - "Need a source-grounded port plan that converts agents, skills, or playbooks into standalone Tall Talents."
inputs:
  - Repository URLs or local paths.
  - Scope filters such as coding, product, design, security, or operations.
  - Acceptance criteria for what counts as durable versus gimmicky.
outputs:
  - Repo inventory with relevant source files identified.
  - Candidate talent list with traceable source artifacts.
  - Deduped final talent set with prioritization, rejection log, and machine-readable export.
agent_behavior:
  - Inventory both repos before proposing candidates.
  - Read enough source to understand the operating pattern, not just the file name.
  - Merge duplicates aggressively and prefer durable workflows over persona wrappers.
safety:
  - Do not port gimmicks, branding, or repo-specific conventions as if they were reusable talents.
  - Do not infer a talent from a folder or title alone without reading the underlying source.
status: active
version: 1.0.0
---

# Goal

Convert external agent/skill repositories into a Tall Talents-ready acquisition plan grounded in actual source material and hard cuts.

# Procedure

1. Inventory each source repo:
   - count files and directories
   - identify relevant folders such as skills, agents, strategy docs, playbooks, runbooks, and templates
   - ignore obviously irrelevant integration wrappers and boilerplate
2. Extract a broad candidate set:
   - read relevant source files
   - capture the reusable capability beneath each agent, skill, or workflow
   - aim broad first, then normalize
3. Normalize every candidate into a common shape:
   - slug
   - name
   - category
   - source repo and files
   - original names
   - summary
   - why it matters
   - port strategy
   - overlap group
4. Deduplicate aggressively:
   - merge near-duplicates
   - reject narrow or gimmicky items
   - prefer stronger operating models when multiple repos cover similar ground
5. Prioritize the final set:
   - rank by leverage, reuse frequency, implementation simplicity, and complementarity
   - keep a rejection log for discarded or folded candidates
6. Produce deliverables:
   - executive summary
   - final talent table
   - per-talent dossiers
   - recommended Tall Talents folder plan
   - implementation queue
   - rejection log
   - machine-readable JSON

# Success Criteria

- Final talents are traceable to exact source files.
- Overlap is merged rather than repeated.
- Weak, niche, or branding-heavy candidates are explicitly rejected.
- Output is actionable enough to drive actual Tall Talents implementation.

# Common Failure Modes

- Listing repo folders instead of extracting the capability underneath them.
- Porting persona wrappers without the underlying workflow, checklist, or quality gate.
- Treating duplicates from two repos as two final talents instead of one merged talent.
- Accepting tool- or brand-specific conventions as universal operating patterns.

# Example Prompt

"Use `repo-talent-acquisition-pass` to scan these two repos, identify the best reusable Talents for Tall Talents, merge overlaps, reject weak candidates, and return both a report and machine-readable JSON."

