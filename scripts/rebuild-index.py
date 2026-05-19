#!/usr/bin/env python3
import argparse
from pathlib import Path


def parse_front_matter(text: str):
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None

    data = {}
    current_key = None
    for raw in lines[1:end]:
        line = raw.rstrip()
        if not line.strip():
            continue
        if current_key and (line == "  -" or line.startswith("  - ")):
            data.setdefault(current_key, []).append(line[4:].strip())
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            current_key = k
            data[k] = v if v else []
    return data


def talent_packages(root: Path):
    talents_dir = root / "talents"
    if not talents_dir.exists():
        raise SystemExit(f"talents directory not found: {talents_dir}")
    return sorted(path for path in talents_dir.iterdir() if path.is_dir())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Root path of live Tall Talents folder")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    index_path = root / "index.md"

    entries = []
    for package in talent_packages(root):
        talent_path = package / "TALENT.md"
        if not talent_path.exists():
            continue
        front = parse_front_matter(talent_path.read_text(encoding="utf-8"))
        if not front:
            continue
        if front.get("status") != "active":
            continue
        slug = front.get("slug")
        summary = str(front.get("summary", "")).strip()
        if slug:
            entries.append((slug, summary, f"talents/{slug}/TALENT.md"))

    entries.sort(key=lambda x: x[0])

    lines = ["# Tall Talents Index", "", "Active talents (sorted by slug):", ""]
    for slug, summary, path in entries:
        lines.append(f"- `{slug}` — {summary} Path: `{path}`")

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[ok] wrote {index_path}")
    print(f"[ok] active talents indexed: {len(entries)}")


if __name__ == "__main__":
    main()
