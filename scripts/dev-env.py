#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


STATE_FILENAME = "tall-talents-dev-env.json"
BLOCKED_IMPORT_SUFFIXES = {".key", ".log", ".pem"}


def repo_root():
    return Path(__file__).resolve().parent.parent


def bootstrap_root():
    return repo_root() / "bootstrap"


def git_dir():
    result = subprocess.run(
        ["git", "rev-parse", "--git-dir"],
        cwd=repo_root(),
        capture_output=True,
        text=True,
        check=True,
    )
    raw = result.stdout.strip()
    path = Path(raw)
    if not path.is_absolute():
        path = repo_root() / path
    return path.resolve()


def state_path():
    return git_dir() / "info" / STATE_FILENAME


def python3_path():
    path = shutil.which("python3")
    if path:
        return Path(path).resolve()
    return Path(sys.executable).resolve()


def sync_script():
    return repo_root() / "scripts" / "sync-bootstrap.py"


def privacy_scan_script():
    return repo_root() / "scripts" / "scan-talent-privacy.py"


def load_state():
    path = state_path()
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_state(payload):
    path = state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def remove_state():
    path = state_path()
    if path.exists():
        path.unlink()


def run_git_config(*args):
    return subprocess.run(
        ["git", "config", "--local", *args],
        cwd=repo_root(),
        capture_output=True,
        text=True,
    )


def current_hooks_path():
    result = run_git_config("--get", "core.hooksPath")
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def set_hooks_path(value: str):
    result = run_git_config("core.hooksPath", value)
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or "failed to set core.hooksPath")


def unset_hooks_path():
    run_git_config("--unset", "core.hooksPath")


def unique_backup_path(live_root: Path):
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = live_root.parent / f"{live_root.name}.dev-backup.{stamp}"
    index = 1
    while candidate.exists() or candidate.is_symlink():
        candidate = live_root.parent / f"{live_root.name}.dev-backup.{stamp}-{index}"
        index += 1
    return candidate


def symlinked_to(live_root: Path, target_root: Path):
    return live_root.is_symlink() and live_root.resolve() == target_root


def live_root_rejection_reason(live_root: Path):
    resolved = live_root.resolve()
    if resolved == Path("/"):
        return "filesystem root is not a safe live library"
    if resolved == Path.home().resolve():
        return "home directory is not a safe live library"
    if resolved == repo_root().resolve():
        return "repo root is not a safe live library"
    if live_root.name != ".tall-talents":
        return "live root must be named .tall-talents"
    return None


def validate_live_root(live_root: Path, force: bool):
    reason = live_root_rejection_reason(live_root)
    if not reason:
        return
    if force:
        print(f"[warn] forcing non-standard live root: {live_root} ({reason})")
        return
    raise SystemExit(f"[fail] refusing --live-root {live_root}: {reason}; pass --force-live-root to override")


def import_candidate_paths(live_root: Path):
    candidates = []
    readme = live_root / "README.md"
    if readme.exists() or readme.is_symlink():
        candidates.append(readme)

    talents_dir = live_root / "talents"
    if talents_dir.exists():
        candidates.extend(sorted(talents_dir.glob("*.md")))

    return candidates


def is_blocked_import_path(rel_path: Path):
    parts = {part.lower() for part in rel_path.parts}
    name = rel_path.name.lower()
    suffixes = {suffix.lower() for suffix in rel_path.suffixes}
    return (
        "private" in parts
        or "log" in parts
        or "logs" in parts
        or name.startswith(".env")
        or bool(suffixes & BLOCKED_IMPORT_SUFFIXES)
    )


def validate_public_import(live_root: Path):
    problems = []
    for path in import_candidate_paths(live_root):
        rel_path = path.relative_to(live_root)
        if is_blocked_import_path(rel_path):
            problems.append(f"{rel_path} matches an excluded public-import path")
        if path.is_symlink():
            problems.append(f"{rel_path} is a symlink")
        elif not path.is_file():
            problems.append(f"{rel_path} is not a regular file")

    if problems:
        detail = "\n".join(f"- {problem}" for problem in problems)
        raise SystemExit(f"[fail] --import-live refused unsafe public import candidates:\n{detail}")

    print("[ok] --import-live imports only README.md and talents/*.md; private/, .env*, logs, keys, and PEM files stay out")


def run_sync(live_root: Path, target_root: Path):
    subprocess.run(
        [
            str(python3_path()),
            str(sync_script()),
            "--live-root",
            str(live_root),
            "--bootstrap-root",
            str(target_root),
        ],
        cwd=repo_root(),
        check=True,
    )


def run_privacy_scan(target_root: Path):
    subprocess.run(
        [str(python3_path()), str(privacy_scan_script()), "--root", str(target_root)],
        cwd=repo_root(),
        check=True,
    )


def install(live_root: Path, import_live: bool):
    bootstrap = bootstrap_root().resolve()
    state = load_state() or {}
    backup_path = None

    existing_hooks = current_hooks_path()
    previous_hooks = state.get("previous_hooks_path")
    if existing_hooks != ".githooks":
        previous_hooks = existing_hooks

    if symlinked_to(live_root, bootstrap):
        backup_path = state.get("backup_path")
        print(f"[ok] live root already points at repo bootstrap: {live_root}")
    else:
        if import_live and (live_root.exists() or live_root.is_symlink()):
            validate_public_import(live_root)
            run_sync(live_root, bootstrap)
            run_privacy_scan(bootstrap)

        if live_root.exists() or live_root.is_symlink():
            backup = unique_backup_path(live_root)
            live_root.rename(backup)
            backup_path = str(backup)
            print(f"[ok] backed up prior live root: {backup}")

        live_root.parent.mkdir(parents=True, exist_ok=True)
        live_root.symlink_to(bootstrap, target_is_directory=True)
        print(f"[ok] linked live root to repo bootstrap: {live_root} -> {bootstrap}")

    set_hooks_path(".githooks")
    write_state(
        {
            "live_root": str(live_root),
            "bootstrap_root": str(bootstrap),
            "backup_path": backup_path,
            "previous_hooks_path": previous_hooks,
            "mode": "repo-live",
        }
    )

    print("[ok] repo-local hooksPath set to .githooks")
    print("[ok] derived files will refresh on commit via .githooks/pre-commit")


def uninstall():
    state = load_state()
    if not state:
        print("[ok] dev mode not installed for this repo")
        return

    live_root = Path(state["live_root"]).expanduser()
    bootstrap = Path(state["bootstrap_root"]).expanduser().resolve()
    backup_path = state.get("backup_path")

    if symlinked_to(live_root, bootstrap):
        live_root.unlink()
        print(f"[ok] removed live-root link: {live_root}")

    if backup_path:
        backup = Path(backup_path).expanduser()
        if backup.exists() or backup.is_symlink():
            backup.rename(live_root)
            print(f"[ok] restored previous live root: {live_root}")

    previous_hooks = state.get("previous_hooks_path")
    if previous_hooks:
        set_hooks_path(previous_hooks)
        print(f"[ok] restored prior core.hooksPath: {previous_hooks}")
    else:
        unset_hooks_path()
        print("[ok] cleared repo-local core.hooksPath")

    remove_state()


def status(live_root: Optional[Path]):
    bootstrap = bootstrap_root().resolve()
    state = load_state()
    if state and live_root is None:
        live_root = Path(state["live_root"]).expanduser()
    elif live_root is None:
        live_root = Path("~/.tall-talents").expanduser()
    hooks = current_hooks_path()
    linked = symlinked_to(live_root, bootstrap)

    print(f"live_root: {live_root}")
    print(f"bootstrap_root: {bootstrap}")
    print(f"linked: {'yes' if linked else 'no'}")
    print(f"core.hooksPath: {hooks or '(unset)'}")
    if state:
        print(f"state_file: {state_path()}")
        print(f"backup_path: {state.get('backup_path') or '(none)'}")
    else:
        print("state_file: (missing)")


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser("install")
    install_parser.add_argument("--live-root", default="~/.tall-talents", help="Root path of the live Tall Talents folder")
    install_parser.add_argument(
        "--import-live",
        action="store_true",
        help="Import reviewed public live-library files into bootstrap before linking dev mode",
    )
    install_parser.add_argument(
        "--confirm-public-import",
        action="store_true",
        help="Confirm that --import-live content has been reviewed for public bootstrap import",
    )
    install_parser.add_argument(
        "--force-live-root",
        action="store_true",
        help="Allow a non-standard --live-root after explicit review",
    )

    subparsers.add_parser("uninstall")

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--live-root", help="Root path of the live Tall Talents folder")

    args = parser.parse_args()

    if args.command == "install":
        live_root = Path(args.live_root).expanduser()
        validate_live_root(live_root, args.force_live_root)
        if args.import_live and not args.confirm_public_import:
            raise SystemExit("[fail] --import-live requires --confirm-public-import after reviewing live files for public import")
        install(live_root, args.import_live)
    elif args.command == "uninstall":
        uninstall()
    else:
        live_root = Path(args.live_root).expanduser() if args.live_root else None
        status(live_root)


if __name__ == "__main__":
    main()
