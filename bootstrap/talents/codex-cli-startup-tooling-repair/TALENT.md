---
slug: codex-cli-startup-tooling-repair
title: Codex CLI Startup Tooling Repair
summary: Repair Codex CLI startup warnings and verify Browser plus Computer Use availability from the real local config without overstating backend readiness.
tags:
  - codex
  - tooling
  - debugging
  - mcp
triggers:
  - Codex prints startup warnings about invalid skills, skipped skills, plugins, MCP servers, or local tooling.
  - User asks to make Browser, in-app browser, or Computer Use available from CLI Codex.
  - A Codex config path points at a stale plugin bundle or versioned app path.
inputs:
  - User-provided Codex startup output or warning text.
  - Access to the local `~/.codex` directory and Codex CLI.
outputs:
  - Minimal config or skill fix.
  - Fresh proof that skill frontmatter parses, Codex starts without the reported warning, and requested tools are visible, enabled, or honestly blocked.
agent_behavior:
  - Start from the exact warning text and inspect the named files before editing.
  - Treat Browser and Computer Use as separate surfaces: Browser may be plugin/skill based, while Computer Use should appear as an MCP server.
  - Prefer validating current local state over reinstalling global tooling.
safety:
  - Do not print secrets from `auth.json`, environment files, or config values.
  - Do not reinstall or delete plugin bundles before proving a config or syntax fix is insufficient.
status: active
version: 1.0.0
---

# Goal

Keep CLI Codex clean at startup and ready to use the local Browser and Computer Use surfaces without turning a small config repair into a full reinstall.

## Procedure

1. Capture the failing startup behavior.
   - Run or inspect the exact command the user used.
   - Record the warning path, line number, plugin name, or MCP server name.

2. Inspect local config safely.
   - Check `~/.codex/config.toml`, plugin cache directories, and the named skill file.
   - Redact token-like values if printing config output.
   - For stale versioned paths, compare the configured path with the installed plugin bundle.

3. Fix the minimum surface.
   - For invalid `SKILL.md` frontmatter, repair only the YAML frontmatter.
   - For stale Computer Use paths, update the path to the installed bundle that `codex mcp list` uses.
   - Do not rewrite unrelated skills, plugins, or project trust entries.

4. Verify skill loading.
   - Parse all local skill frontmatter with a YAML parser.
   - Run a short Codex startup cycle and confirm the reported skipped-skill warning is gone.

5. Verify Browser availability.
   - Confirm `codex features list` reports `browser_use`, `browser_use_external`, and `in_app_browser` as true.
   - Confirm `codex debug prompt-input` lists the Browser plugin and `browser-use:browser` skill for an in-app browser prompt.
   - Confirm `node_repl` is available as an enabled MCP server when Browser automation needs the Browser client runtime.
   - If missing, add the bundled Node REPL server and trust the exact local Browser client hash:
     - `codex mcp add node_repl --env NODE_REPL_TRUSTED_BROWSER_CLIENT_SHA256S=<sha256 of browser-client.mjs> --env NODE_REPL_BROWSER_CLIENT_MARKETPLACE_NAME=openai-bundled -- /Applications/Codex.app/Contents/Resources/node_repl`
   - Verify `node_repl/js` with a harmless `console.log` proof, then verify Browser runtime bootstrap with `setupAtlasRuntime({ globals: globalThis })`.
   - Verify actual browser controllability separately with `await agent.browsers.list()` or `await agent.browsers.get("iab")`.
   - If Codex.app owns `/tmp/codex-browser-use/*.sock` but Browser still returns `BROWSERS=[]`, treat that as a real backend attachment failure, not proof of readiness. The Browser client filters in-app browser backends by the current Codex session metadata, so a socket can exist while the active CLI turn still cannot attach to it.
   - When using `codex debug app-server send-message-v2`, note the reported thread source. A thread sourced from another host surface such as `vscode` may have Browser plugin visibility while still lacking an attachable `iab` backend.
   - Do not require Browser to appear in `codex mcp list`; it can be exposed as a plugin/skill surface rather than a standalone MCP server.
   - Do not claim Browser can manipulate pages if the Browser runtime returns `BROWSERS=[]` or cannot connect to `iab`.

6. Verify Computer Use availability.
   - Confirm `computer_use` is true in `codex features list`.
   - Confirm `codex mcp list` includes an enabled `computer-use` server.
   - If the current session exposes Computer Use tools, run a harmless read-only call such as listing apps.

## Success Criteria

- The originally reported startup warning no longer appears.
- All local skill frontmatter parses.
- CLI Codex reaches the Ready state.
- Browser is model-visible through the plugin/skill prompt context.
- `node_repl/js` can bootstrap the Browser runtime, or the exact missing capability is reported.
- Actual Browser page manipulation is only considered proven after a real backend appears in `agent.browsers.list()` and a page action succeeds through that backend.
- Computer Use is enabled as an MCP server and points at an installed executable.

## Common Failure Modes

- Quoting YAML descriptions only after a colon has already broken plain-scalar parsing.
- Updating one Computer Use path while leaving another stale versioned path in `config.toml`.
- Treating the absence of Browser in `codex mcp list` as failure even when it is present as a Browser plugin and skill.
- Treating Browser plugin visibility or successful `setupAtlasRuntime` bootstrap as proof that an `iab` backend is connected.
- Treating a live `/tmp/codex-browser-use/*.sock` socket as proof that the current CLI session can attach to the in-app browser.
- Counting a shell, fetch, DOM replay, standalone Playwright, or Computer Use action as Browser Use proof.
- Claiming tool readiness from config alone without a fresh Codex startup or debug prompt check.

## Example Prompt

"Use talent `codex-cli-startup-tooling-repair` on this Codex startup warning. Inspect the exact warning and local config first, make the smallest safe config or skill repair, and verify Browser plus Computer Use availability without exposing secrets."
