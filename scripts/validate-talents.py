#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path
from typing import Optional

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
CHANGELOG_ENTRY_RE = re.compile(r"^##\s+\S", re.MULTILINE)


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
        if current_key and (line == "  -" or line.startswith("  - ")):
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
        return None, body

    return data, body


def package_dirs(root: Path, dirname: str):
    base = root / dirname
    if not base.exists():
        return []
    return sorted(path for path in base.iterdir() if path.is_dir())


def validate_package(path: Path, expected_status: Optional[str] = None):
    errors = []
    talent_path = path / "TALENT.md"
    changelog_path = path / "CHANGELOG.md"

    if not talent_path.exists():
        errors.append("missing TALENT.md")
        return errors, None

    if not changelog_path.exists():
        errors.append("missing CHANGELOG.md")
    else:
        changelog = changelog_path.read_text(encoding="utf-8")
        if not CHANGELOG_ENTRY_RE.search(changelog):
            errors.append("CHANGELOG.md must contain at least one ## entry")

    text = talent_path.read_text(encoding="utf-8")
    front, body = parse_front_matter(text)

    if front is None:
        errors.append("missing or invalid front matter in TALENT.md")
        return errors, None

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
        if path.name != slug:
            errors.append(f"folder name must equal slug: expected {slug}")

    status = front.get("status")
    if isinstance(status, list):
        errors.append("status must be scalar")
    elif status and status not in ALLOWED_STATUS:
        errors.append("status must be one of: active, draft, archived")
    elif expected_status and status != expected_status:
        errors.append(f"status must be {expected_status} in {path.parent.name}/")

    for heading in REQUIRED_SECTIONS:
        if heading not in body:
            errors.append(f"missing required section: {heading}")

    return errors, slug


def validate_root(root: Path):
    talents_dir = root / "talents"
    if not talents_dir.exists():
        print(f"[error] talents directory not found: {talents_dir}")
        return 1

    all_ok = True
    seen_active_slugs = {}

    single_files = sorted(talents_dir.glob("*.md"))
    for file in single_files:
        all_ok = False
        print(f"[fail] {file}")
        print("  - single-file talents are invalid; use talents/<slug>/TALENT.md")

    talent_packages = package_dirs(root, "talents")
    if not talent_packages:
        print(f"[warn] no talent packages found in {talents_dir}")

    for package in talent_packages:
        errors, slug = validate_package(package)
        if slug:
            if slug in seen_active_slugs:
                errors.append(f"duplicate active/draft slug also in {seen_active_slugs[slug]}")
            else:
                seen_active_slugs[slug] = str(package)

        if errors:
            all_ok = False
            print(f"[fail] {package}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"[pass] {package}")

    for package in package_dirs(root, "archive"):
        errors, _slug = validate_package(package, expected_status="archived")
        if errors:
            all_ok = False
            print(f"[fail] {package}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"[pass] {package}")

    if not all_ok:
        print("[result] validation failed")
        return 1

    print("[result] validation passed")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Root path of live Tall Talents folder")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    return validate_root(root)


if __name__ == "__main__":
    sys.exit(main())
