---
slug: game-live-preview-workspace
title: Game Live Preview Workspace
summary: Start the local game dev server and open the in-app browser preview before game UI or asset work so Codex and the playable surface stay side by side.
tags:
  - games
  - frontend
  - browser
  - workflow
triggers:
  - The user starts work on a browser-playable game, canvas game, PWA game, or visual asset integration task.
  - The user wants Codex and a live browser preview open together while iterating on game UI, animation, assets, or interactions.
  - A game task will benefit from hot reload, screenshots, or immediate visual confirmation.
inputs:
  - Current repository path and package/runtime files.
  - Available local dev command, such as npm run dev, pnpm dev, bun run dev, or a repo-specific preview command.
  - Browser Use or equivalent in-app browser capability for opening localhost.
outputs:
  - Running local dev server with the active URL identified.
  - In-app browser opened to the correct localhost URL.
  - Short working note describing the live-preview loop and any manual refresh caveats.
agent_behavior:
  - Prefer live preview setup before making visual or game-asset edits.
  - Keep the dev server running while the game/UI work continues.
  - Use screenshots and console checks after meaningful visual changes.
safety:
  - Do not assume the port; read the dev server output and open the actual URL.
  - Do not use macOS open or an external browser when an in-app browser plugin is available for localhost.
  - Do not kill unrelated user processes to free a port unless the user explicitly approves.
status: active
version: 1.0.0
---

# Goal

Make game and visual-asset work collaborative by putting the live playable surface next to Codex at the start of the session. The aim is a tight loop: edit assets or UI, let the dev server update, inspect the actual browser view, then tune with evidence.

## Use It When

- Working on a browser game, canvas game, PWA game, WebGL game, or game-like interactive UI.
- Integrating sprites, backgrounds, music, sound effects, animation timing, HUDs, controls, or responsive game layout.
- The user says they want to watch changes live, work side by side, or see the app in real time.
- A visual change would otherwise be judged from code instead of a rendered game surface.

## Do Not Use It When

- The task is backend-only, docs-only, CLI-only, or a quick informational answer.
- The project has no local browser-rendered surface.
- The user explicitly asks not to run a dev server or not to open a browser.
- Opening the app would require logging into an unrelated third-party account or transmitting sensitive data.

# Procedure

## 1. Identify The Local Game Runtime

Inspect the repo before starting anything:

- `pwd`
- `package.json`, `vite.config.*`, `next.config.*`, `bun.lock*`, `pnpm-lock.yaml`, `yarn.lock`, or equivalent runtime signals
- README run commands when present
- existing terminal sessions if a dev server may already be running

Find the real command instead of guessing. Common candidates:

```text
npm run dev
pnpm dev
bun run dev
yarn dev
```

If dependencies are missing and the repo has a lockfile, install them with the repo's package manager unless the user asked not to.

## 2. Start Or Reuse The Dev Server

Run the dev server in a long-running terminal session.

Rules:

- Prefer binding to localhost or `127.0.0.1` when the framework supports it.
- If the requested/default port is occupied, let the framework choose another port or use the next safe local port.
- Read the server output and capture the exact local URL.
- Keep the session ID or terminal context available for later shutdown/status checks.
- Do not end the final response while a server is accidentally half-started or failing.

If a server is already running for this repo, reuse it when the URL is clear.

## 3. Open The In-App Browser To The Actual URL

Use the Browser Use in-app browser when available.

Required behavior:

- Open the exact URL from server output, usually `http://127.0.0.1:<port>/` or `http://localhost:<port>/`.
- Name the browser session with the project or task.
- Take an initial screenshot so the current surface is known.
- If navigation fails, check the dev server terminal before changing ports or commands.

Do not satisfy this step with `open http://...` or an external browser unless the in-app browser is unavailable and the user accepts the fallback.

## 4. Establish The Live Iteration Loop

Tell the user the active URL and the update behavior:

- code and CSS changes usually hot reload
- files under `public/` may need a browser refresh when the filename stays the same
- generated assets should be saved into the runtime path before previewing
- the dev server should stay running while work continues

During implementation:

- after meaningful UI, animation, or asset changes, refresh if needed
- capture a screenshot or DOM/console check before judging the result
- keep the user's visible browser state in mind when explaining what changed

## 5. Verify Before Calling Visual Work Done

For game/UI work, do a small visual sanity check:

- current browser screenshot
- browser console warning/error check when available
- at least one critical interaction if the change affects controls, audio, animation, menus, or gameplay

Use `visual-evidence-qa` for deeper acceptance review. This talent only guarantees the live workspace and tight preview loop.

## 6. Close Or Leave Running Intentionally

At closeout, state whether the dev server is still running.

Default:

- leave it running if the user is actively working alongside Codex
- stop it only when the user asks or when the task clearly ends and the server is no longer useful

# Success Criteria

- The correct local game URL is open in the in-app browser.
- Codex has a running dev server session or has confirmed an existing server.
- The user can see live game/UI changes while Codex works.
- The agent knows when to hot reload versus explicitly refresh.
- Visual claims are backed by the browser view, not by source-code inspection alone.

# Common Failure Modes

- Opening the wrong port or a stale localhost tab.
- Starting a second dev server when the repo already has one running.
- Using an external browser even though the in-app browser is available.
- Forgetting that `public/` asset replacement may need a browser refresh.
- Calling a sprite, background, or UI change done without checking the rendered game.
- Killing a user-owned process just to free a port.

# Example Prompt

"Use `game-live-preview-workspace` for this game UI pass. Start the repo's dev server, open the in-app browser to the actual localhost URL, keep it running while editing assets, and verify changes with a screenshot."
