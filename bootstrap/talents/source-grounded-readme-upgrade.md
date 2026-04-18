---
slug: source-grounded-readme-upgrade
title: Upgrade a README into a source-grounded showcase page
summary: Turn a repository README into a high-credibility landing page by preserving what already works, surfacing verified proof, and only adding badges, graphs, support links, and brand sections that can be confirmed.
tags:
  - readme
  - documentation
  - github
  - branding
  - product
triggers:
  - "User asks to analyze, review, rewrite, or upgrade a repository README so it feels outstanding, public-facing, or more polished."
  - "Need to add badges, star history, support links, feature framing, or brand/product positioning without drifting away from the actual repo."
inputs:
  - Repository path and current README.
  - Source-of-truth repo files such as scripts, version markers, changelog, workflows, architecture docs, or templates.
  - GitHub repo metadata and any public support or brand links if they exist.
outputs:
  - Rewritten README with a stronger narrative, clearer proof, and more scannable structure.
  - Verified badges, graphs, and external links, with explicit placeholders or omissions where verification failed.
  - Brief assessment of what the original README already did well so the rewrite preserves the right strengths.
agent_behavior:
  - Inspect the actual repository and metadata before writing marketing copy.
  - Preserve the strongest parts of the existing README instead of replacing them blindly.
  - Verify every external badge, graph, support link, and brand URL before adding it.
  - Prefer concise, high-signal sections that help a GitHub visitor understand the project quickly.
safety:
  - Do not fabricate support links, star history embeds, product claims, or brand details.
  - Do not add external embeds or badges that fail verification.
  - Do not let the README become generic marketing fluff disconnected from the real repo.
  - Do not treat different README surfaces as interchangeable when a repo has both a public repo README and a bootstrap or runtime README with a different job.
status: active
version: 1.0.0
---

# Goal

Produce a README that feels like a strong public landing page while staying tightly grounded in the repository's real files, real metadata, and verified external links.

# Procedure

1. Audit what already exists:
   - read the current `README.md` start to finish
   - identify what already works: the core pitch, memorable lines, install flow, examples, structure, or product framing
   - note what is missing, weak, buried, repetitive, or visually flat
2. Gather repo truth before rewriting:
   - inspect the files that prove what the project actually is, such as `VERSION`, `CHANGELOG.md`, architecture docs, install scripts, workflows, templates, examples, and core source directories
   - list the features, commands, assets, and guarantees that the README can legitimately claim
   - confirm which README surfaces exist so repo-level messaging does not accidentally overwrite a bootstrap or runtime README with a different purpose
3. Verify public metadata and showcase elements:
   - confirm repository URL, default branch, license, homepage, workflow path, and star count through live GitHub metadata when available
   - test any badge, star-history chart, or graph URL before keeping it
   - if the user wants support links such as Buy Me a Coffee, inspect the repo, linked GitHub profile, and linked website before adding one
   - when a requested support or brand URL cannot be verified, omit it or keep an explicit placeholder instead of inventing it
4. Design the README narrative:
   - put the first screen to work with a clear identity, fast product pitch, and lightweight proof such as badges
   - order the body from high-level understanding to concrete proof: why it exists, what it does, what is included, install, usage, verification, support, brand, license
   - preserve any original line or framing that already gives the project a strong voice
5. Rewrite for clarity and credibility:
   - turn vague descriptions into sections backed by real repo artifacts
   - show features with actual shipped examples, scripts, workflows, or assets instead of generic claims
   - keep installation and usage commands runnable and easy to find
   - add showcase sections such as stars, support, or brand framing only when they strengthen understanding instead of adding noise
6. Run a README QA pass:
   - read the final markdown as a landing page, not just a diff
   - verify referenced local files exist
   - verify external badge and graph URLs resolve
   - run `git diff --check` to catch trailing whitespace and markdown hygiene issues
   - if any requested element remains unverified, mark that clearly in the README or final report

# Success Criteria

- The README explains the project clearly within the first screen and makes the repo feel credible immediately.
- Every meaningful claim is grounded in actual repository files, commands, examples, or verified GitHub metadata.
- Added badges, graphs, support links, and brand links all resolve successfully, or missing items are left explicit instead of fabricated.
- The rewrite keeps or improves the original README's best strengths instead of flattening them into a generic template.
- Markdown QA passes cleanly.

# Common Failure Modes

- Replacing a clear existing README with generic launch-copy language.
- Adding flashy badges, graphs, or donation links without verifying that they work.
- Burying the install and usage flow under philosophy or branding sections.
- Claiming features, support channels, or brand affiliations that are not evidenced in the repo.
- Treating the README as a design exercise instead of a source-grounded product document.
- Forgetting the final markdown hygiene pass and leaving trailing whitespace or broken links behind.

# Example Prompt

"Use talent `source-grounded-readme-upgrade` to audit this repo's README, preserve what already works, verify which badges and star-history embeds are real, add a support section only if the link can be confirmed, and rewrite it into a stronger public-facing README."
