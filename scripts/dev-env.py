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
            run_sync(live_root, bootstrap)

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
        help="Import the current live library into bootstrap before linking dev mode",
    )

    subparsers.add_parser("uninstall")

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--live-root", help="Root path of the live Tall Talents folder")

    args = parser.parse_args()

    if args.command == "install":
        live_root = Path(args.live_root).expanduser()
        install(live_root, args.import_live)
    elif args.command == "uninstall":
        uninstall()
    else:
        live_root = Path(args.live_root).expanduser() if args.live_root else None
        status(live_root)


if __name__ == "__main__":
    main()
