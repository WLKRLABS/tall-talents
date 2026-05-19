#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="~/.tall-talents", help="Root path of live Tall Talents folder")
    parser.add_argument("--title", required=True, help="Talent title")
    parser.add_argument("--summary", required=True, help="Talent summary")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    talents_dir = root / "talents"
    talents_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(args.title)
    if not slug:
        raise SystemExit("generated slug is empty; provide a title with letters or numbers")

    package_dir = talents_dir / slug
    if package_dir.exists():
        raise SystemExit(f"refusing overwrite; package exists: {package_dir}")

    package_dir.mkdir(parents=True)
    talent_path = package_dir / "TALENT.md"
    changelog_path = package_dir / "CHANGELOG.md"

    content = f"""---
slug: {slug}
title: {args.title}
summary: {args.summary}
tags:
  - replace-with-tag
triggers:
  - Describe when this talent should be used.
inputs:
  - List the concrete inputs this workflow needs.
outputs:
  - List the concrete artifacts or outcomes this workflow produces.
agent_behavior:
  - Describe the execution rules the agent should follow.
safety:
  - Capture the main guardrail or failure to avoid.
  - Do not include secrets, private identifiers, or owner-only context in the committed talent.
status: draft
version: 1.0.0
---

# Goal

Describe the outcome this talent is meant to achieve.

# Procedure

1. Replace this placeholder with the first concrete step.

# Success Criteria

- Replace with the measurable definition of done.

# Common Failure Modes

- Replace with the most likely way this workflow can go wrong.

# Example Prompt

"Use `{slug}` for [task], then report exact commands/files changed."
"""
    changelog = """# Changelog

## Unreleased - draft created

- Session: create-talent.py
- Change: Created package scaffold.
- Evidence: User or agent requested a new draft talent package.
- Effect: Provides a validator-clean starting point for authoring.
- Oscillation check: Initial package entry; no prior change exists to undo.
"""

    talent_path.write_text(content, encoding="utf-8")
    changelog_path.write_text(changelog, encoding="utf-8")
    print(f"[ok] created {package_dir}")


if __name__ == "__main__":
    main()
