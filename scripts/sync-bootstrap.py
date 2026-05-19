#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path


INDEX_HEADER = ["# Tall Talents Index", "", "Active talents (sorted by slug):", ""]
BLOCKED_PACKAGE_PARTS = {"private", "log", "logs"}
BLOCKED_PACKAGE_SUFFIXES = {".key", ".log", ".pem"}


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


def talent_packages(root: Path):
    talents_dir = root / "talents"
    if not talents_dir.exists():
        raise SystemExit(f"talents directory not found: {talents_dir}")

    single_files = sorted(talents_dir.glob("*.md"))
    if single_files:
        detail = "\n".join(f"- {path}" for path in single_files)
        raise SystemExit(f"single-file talents are invalid after package migration:\n{detail}")

    return sorted(path for path in talents_dir.iterdir() if path.is_dir())


def collect_talents(root: Path):
    talents = []
    for package in talent_packages(root):
        talent_path = package / "TALENT.md"
        if not talent_path.exists():
            continue
        front = parse_front_matter(talent_path.read_text(encoding="utf-8"))
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
                    "package": package,
                    "entry": talent_path,
                }
            )

    talents.sort(key=lambda item: item["slug"])
    return talents


def active_entries(talents):
    return [talent for talent in talents if talent["status"] == "active"]


def write_index(root: Path, entries):
    lines = INDEX_HEADER.copy()
    for entry in entries:
        path = f"talents/{entry['slug']}/TALENT.md"
        lines.append(f"- `{entry['slug']}` — {entry['summary']} Path: `{path}`")
    (root / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def ensure_gitkeep(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")


def is_manifest_safe_package_file(package_root: Path, path: Path):
    rel = path.relative_to(package_root)
    parts = [part.lower() for part in rel.parts]
    name = rel.name.lower()
    suffixes = {suffix.lower() for suffix in rel.suffixes}
    return (
        not name.startswith(".env")
        and not any(part.startswith(".") for part in parts)
        and not any(part in BLOCKED_PACKAGE_PARTS for part in parts)
        and not bool(suffixes & BLOCKED_PACKAGE_SUFFIXES)
    )


def package_manifest_files(root: Path, entry):
    package_root = entry["package"]
    rel_files = []
    for path in sorted(p for p in package_root.rglob("*") if p.is_file()):
        if not is_manifest_safe_package_file(package_root, path):
            raise SystemExit(f"unsafe active package file refused for manifest: {path}")
        rel_files.append(path.relative_to(root).as_posix())
    return rel_files


def write_manifest(root: Path, entries):
    lines = ["README.md", "index.md"]
    for entry in entries:
        lines.extend(package_manifest_files(root, entry))
    lines.extend(
        [
            "incoming/.gitkeep",
            "archive/.gitkeep",
            "reports/self-iteration/.gitkeep",
        ]
    )
    (root / "manifest.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def mirror_tree(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    if src.exists():
        shutil.copytree(src, dst)
    else:
        dst.mkdir(parents=True, exist_ok=True)


def mirror_public_dirs(src_root: Path, dst_root: Path):
    mirror_tree(src_root / "talents", dst_root / "talents")
    mirror_tree(src_root / "archive", dst_root / "archive")
    mirror_tree(src_root / "incoming", dst_root / "incoming")
    if (src_root / "reports").exists():
        mirror_tree(src_root / "reports", dst_root / "reports")
    else:
        (dst_root / "reports" / "self-iteration").mkdir(parents=True, exist_ok=True)


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
    ensure_gitkeep(live_root / "reports" / "self-iteration" / ".gitkeep")
    ensure_gitkeep(bootstrap_root / "incoming" / ".gitkeep")
    ensure_gitkeep(bootstrap_root / "archive" / ".gitkeep")
    ensure_gitkeep(bootstrap_root / "reports" / "self-iteration" / ".gitkeep")

    write_index(live_root, active)

    if same_root:
        mirrored = len(talent_packages(live_root))
        manifest_entries = active
    else:
        shutil.copyfile(live_readme, bootstrap_root / "README.md")
        mirror_public_dirs(live_root, bootstrap_root)
        bootstrap_talents = collect_talents(bootstrap_root)
        bootstrap_active = active_entries(bootstrap_talents)
        mirrored = len(talent_packages(bootstrap_root))
        write_index(bootstrap_root, bootstrap_active)
        manifest_entries = bootstrap_active

    write_manifest(bootstrap_root, manifest_entries)

    if same_root:
        print(f"[ok] derived in place: {bootstrap_root}")
    else:
        print(f"[ok] bootstrap synced: {bootstrap_root}")
    print(f"[ok] total talent packages mirrored: {mirrored}")
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
