---
slug: gh-pages-site-subfolder-assets
title: Fix GitHub Pages asset paths for project subfolder sites
summary: Correct broken CSS/JS/image links when a static site is served from a repo subpath on GitHub Pages.
tags:
  - github-pages
  - static-site
  - pathing
triggers:
  - "Site works locally but loses styles/scripts on GitHub Pages project URL."
inputs:
  - Repository name and final Pages URL.
  - Build output directory (for example `dist/` or `site/`).
outputs:
  - Deployed site loads assets correctly from project subpath.
  - HTML references use deterministic base path handling.
agent_behavior:
  - Treat deployment URL as source of truth for path generation.
  - Verify generated HTML, not just source templates.
safety:
  - Avoid global string replacement across unrelated files.
  - Keep local-dev path behavior intact when possible.
status: active
version: 1.0.0
---

# Goal

Ensure assets resolve correctly when hosted at `https://<user>.github.io/<repo>/` instead of domain root.

# Procedure

1. Confirm target deploy prefix (`/<repo>/`).
2. Configure site/tooling base path (examples):
   - Vite: `base: '/<repo>/'`
   - Static template: prepend `/<repo>/` to root-relative asset refs.
3. Rebuild site output.
4. Inspect generated HTML for root-relative `href="/` or `src="/` patterns that ignore subpath.
5. Deploy/re-publish `gh-pages` branch or Pages artifact.
6. Validate live page loads CSS/JS/images from `/<repo>/...`.

# Success Criteria

- Network requests for assets resolve to URLs under repo subpath.
- No 404s for primary CSS/JS/image assets.
- Local development flow remains functional.

# Common Failure Modes

- Fixing source files but not rebuild output before deploy.
- Mixing absolute root `/assets/...` paths with subfolder hosting.
- Forgetting to update SPA router basename in single-page apps.

# Example Prompt

"Apply `gh-pages-site-subfolder-assets` for repo `docs-site`, then list the exact config and generated HTML path changes."
