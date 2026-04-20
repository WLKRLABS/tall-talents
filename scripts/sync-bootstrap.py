#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path


INDEX_HEADER = ["# Tall Talents Index", "", "Active talents (sorted by slug):", ""]


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
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            current_key = key
            data[key] = val if val else []
    return data


def talent_paths(root: Path):
    talents_dir = root / "talents"
    if not talents_dir.exists():
        raise SystemExit(f"talents directory not found: {talents_dir}")

    return sorted(talents_dir.glob("*.md"))


def collect_talents(root: Path):
    talents = []
    for path in talent_paths(root):
        front = parse_front_matter(path.read_text(encoding="utf-8"))
        if not front:
            continue
        slug = front.get("slug")
        summary = str(front.get("summary", "")).strip()
        status = front.get("status")
        if slug:
            talents.append(
                {
                    "slug": slug,
                    "summary": summary,
                    "status": status,
                    "path": path,
                }
            )

    talents.sort(key=lambda item: item["slug"])
    return talents


def active_entries(talents):
    return [talent for talent in talents if talent["status"] == "active"]


def write_index(root: Path, entries):
    lines = INDEX_HEADER.copy()
    for entry in entries:
        lines.append(f"- `{entry['slug']}` — {entry['summary']}")
    (root / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def ensure_gitkeep(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")


def write_manifest(root: Path, entries):
    lines = ["README.md", "index.md"]
    lines.extend(f"talents/{entry['path'].name}" for entry in entries)
    lines.extend(["incoming/.gitkeep", "archive/.gitkeep"])
    (root / "manifest.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def mirror_talents(src_root: Path, dst_root: Path):
    src_paths = talent_paths(src_root)
    dst_talents = dst_root / "talents"
    dst_talents.mkdir(parents=True, exist_ok=True)

    expected = {path.name for path in src_paths}
    for stale in dst_talents.glob("*.md"):
        if stale.name not in expected:
            stale.unlink()

    for src in src_paths:
        shutil.copyfile(src, dst_talents / src.name)

    return len(src_paths)


def sync_once(live_root: Path, bootstrap_root: Path):
    live_readme = live_root / "README.md"
    if not live_readme.exists():
        raise SystemExit(f"README not found in live root: {live_readme}")

    talents = collect_talents(live_root)
    active = active_entries(talents)
    same_root = live_root == bootstrap_root

    live_root.mkdir(parents=True, exist_ok=True)
    bootstrap_root.mkdir(parents=True, exist_ok=True)
    ensure_gitkeep(live_root / "incoming" / ".gitkeep")
    ensure_gitkeep(live_root / "archive" / ".gitkeep")
    ensure_gitkeep(bootstrap_root / "incoming" / ".gitkeep")
    ensure_gitkeep(bootstrap_root / "archive" / ".gitkeep")

    write_index(live_root, active)

    if same_root:
        mirrored = len(talent_paths(live_root))
    else:
        shutil.copyfile(live_readme, bootstrap_root / "README.md")
        mirrored = mirror_talents(live_root, bootstrap_root)
        write_index(bootstrap_root, active)

    write_manifest(bootstrap_root, active)

    if same_root:
        print(f"[ok] derived in place: {bootstrap_root}")
    else:
        print(f"[ok] bootstrap synced: {bootstrap_root}")
    print(f"[ok] total talents mirrored: {mirrored}")
    print(f"[ok] active talents indexed: {len(active)}")
    print(f"[ok] manifest wrote: {bootstrap_root / 'manifest.txt'}")


def main():
    default_bootstrap_root = Path(__file__).resolve().parent.parent / "bootstrap"

    parser = argparse.ArgumentParser()
    parser.add_argument("--live-root", default="~/.tall-talents", help="Root path of the live Tall Talents folder")
    parser.add_argument(
        "--bootstrap-root",
        default=str(default_bootstrap_root),
        help="Bootstrap snapshot directory inside the repository",
    )
    args = parser.parse_args()

    live_root = Path(args.live_root).expanduser().resolve()
    bootstrap_root = Path(args.bootstrap_root).expanduser().resolve()
    sync_once(live_root, bootstrap_root)


if __name__ == "__main__":
    main()
