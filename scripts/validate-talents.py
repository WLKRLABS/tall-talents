#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "slug",
    "title",
    "summary",
    "tags",
    "triggers",
    "inputs",
    "outputs",
    "agent_behavior",
    "safety",
    "status",
    "version",
]

REQUIRED_SECTIONS = [
    "# Goal",
    "# Procedure",
    "# Success Criteria",
    "# Common Failure Modes",
    "# Example Prompt",
]

ALLOWED_STATUS = {"active", "draft", "archived"}
SLUG_RE = re.compile(r"^[a-z0-9-]+$")


def parse_front_matter(text: str):
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return None, text

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text

    front_lines = lines[1:end]
    body = "\n".join(lines[end + 1 :])

    data = {}
    current_key = None
    for raw in front_lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, []).append(line[4:].strip())
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            current_key = key
            if val:
                data[key] = val
            else:
                data[key] = []
            continue
        # invalid line
        return None, body

    return data, body


def validate_file(path: Path):
    errors = []
    text = path.read_text(encoding="utf-8")
    front, body = parse_front_matter(text)

    if front is None:
        return ["missing or invalid front matter"], None

    for field in REQUIRED_FIELDS:
        if field not in front:
            errors.append(f"missing required field: {field}")

    slug = front.get("slug")
    if isinstance(slug, list):
        errors.append("slug must be scalar")
        slug = None

    if slug:
        if not SLUG_RE.match(slug):
            errors.append("slug must match ^[a-z0-9-]+$")
        expected_name = f"{slug}.md"
        if path.name != expected_name:
            errors.append(f"filename must equal slug: expected {expected_name}")

    status = front.get("status")
    if isinstance(status, list):
        errors.append("status must be scalar")
    elif status and status not in ALLOWED_STATUS:
        errors.append("status must be one of: active, draft, archived")

    for heading in REQUIRED_SECTIONS:
        if heading not in body:
            errors.append(f"missing required section: {heading}")

    return errors, slug


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Root path of live Tall Talents folder")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    talents_dir = root / "talents"

    if not talents_dir.exists():
        print(f"[error] talents directory not found: {talents_dir}")
        return 1

    files = sorted(talents_dir.glob("*.md"))
    if not files:
        print(f"[warn] no talents found in {talents_dir}")
        return 0

    all_ok = True
    seen = {}

    for file in files:
        errors, slug = validate_file(file)
        if slug:
            if slug in seen:
                errors.append(f"duplicate slug also in {seen[slug]}")
            else:
                seen[slug] = file.name

        if errors:
            all_ok = False
            print(f"[fail] {file}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"[pass] {file}")

    if not all_ok:
        print("[result] validation failed")
        return 1

    print("[result] validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
