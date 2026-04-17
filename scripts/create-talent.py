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

    path = talents_dir / f"{slug}.md"
    if path.exists():
        raise SystemExit(f"refusing overwrite; file exists: {path}")

    content = f"""---
slug: {slug}
title: {args.title}
summary: {args.summary}
tags:
  -
triggers:
  -
inputs:
  -
outputs:
  -
agent_behavior:
  -
safety:
  -
status: draft
version: 1.0.0
---

# Goal


# Procedure

1. 

# Success Criteria

- 

# Common Failure Modes

- 

# Example Prompt

\"Use `{slug}` for [task], then report exact commands/files changed.\"
"""
    path.write_text(content, encoding="utf-8")
    print(f"[ok] created {path}")


if __name__ == "__main__":
    main()
