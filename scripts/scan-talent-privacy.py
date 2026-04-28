#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional


TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".py",
    ".sh",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".env",
}

SECRET_PATTERNS = [
    ("private key block", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"(?<![A-Za-z0-9_])(github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,})(?![A-Za-z0-9_])")),
    ("OpenAI-style API key", re.compile(r"(?<![A-Za-z0-9])sk-(?:proj-)?[A-Za-z0-9_-]{20,}")),
    ("Slack token", re.compile(r"(?<![A-Za-z0-9])xox[baprs]-[A-Za-z0-9-]{20,}")),
    ("AWS access key id", re.compile(r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])")),
    ("Google API key", re.compile(r"(?<![A-Za-z0-9])AIza[0-9A-Za-z_-]{35}")),
    ("SendGrid API key", re.compile(r"(?<![A-Za-z0-9])SG\.[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}")),
    ("Stripe live secret key", re.compile(r"(?<![A-Za-z0-9])(?:sk|rk)_live_[0-9A-Za-z]{16,}")),
    ("Discord bot token", re.compile(r"(?<![A-Za-z0-9_-])[MN][A-Za-z0-9]{23}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27}(?![A-Za-z0-9_-])")),
]

SENSITIVE_ASSIGNMENT_RE = re.compile(
    r"\b([A-Z0-9_]*(?:TOKEN|SECRET|PASSWORD|PASS|PRIVATE_KEY|API_KEY|SERVICE_ROLE|ACCESS_KEY)[A-Z0-9_]*)\b"
    r"\s*[:=]\s*[\"']?([^\"'`\s]+)",
    re.IGNORECASE,
)

PERSONAL_PATTERNS = [
    ("personal home path", re.compile(r"/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+")),
    ("email address", re.compile(r"(?<![A-Za-z0-9._%+-])(?!(?:git|noreply)@github\.com\b)[A-Za-z0-9._%+-]+@(?!example\.com\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
]

PLACEHOLDER_MARKERS = (
    "<",
    "$",
    "${",
    "your_",
    "your-",
    "example",
    "placeholder",
    "replace",
    "redacted",
    "changeme",
    "xxxxx",
    "***",
    "...",
)


def is_text_file(path: Path) -> bool:
    if path.name.startswith(".env"):
        return True
    if path.name in {"manifest.txt", "README.md", "index.md"}:
        return True
    return path.suffix in TEXT_EXTENSIONS


def looks_like_placeholder(value: str) -> bool:
    clean = value.strip().strip("\"'").strip()
    lower = clean.lower()

    if not clean:
        return True

    if clean.startswith("$("):
        return True

    return any(marker in lower for marker in PLACEHOLDER_MARKERS)


def collect_files(root: Optional[Path], paths: List[str]) -> List[Path]:
    files: List[Path] = []

    if root is not None:
        talents_dir = root / "talents"
        if talents_dir.exists():
            files.extend(sorted(talents_dir.glob("*.md")))
        for rel in ("README.md", "index.md", "manifest.txt"):
            candidate = root / rel
            if candidate.exists():
                files.append(candidate)

    for raw in paths:
        path = Path(raw).expanduser()
        if path.is_dir():
            files.extend(sorted(p for p in path.rglob("*") if p.is_file()))
        elif path.exists():
            files.append(path)

    unique = []
    seen = set()
    for path in files:
        resolved = path.resolve()
        if resolved in seen or not path.is_file() or not is_text_file(path):
            continue
        seen.add(resolved)
        unique.append(path)

    return unique


def scan_file(path: Path):
    failures = []
    warnings = []

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return failures, warnings

    for line_no, line in enumerate(lines, start=1):
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(line):
                failures.append((path, line_no, label))

        for match in SENSITIVE_ASSIGNMENT_RE.finditer(line):
            name = match.group(1)
            value = match.group(2)
            if len(value.strip("\"'")) >= 12 and not looks_like_placeholder(value):
                failures.append((path, line_no, f"sensitive assignment: {name}"))

        for label, pattern in PERSONAL_PATTERNS:
            if pattern.search(line):
                warnings.append((path, line_no, label))

    return failures, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan Tall Talents markdown for obvious secrets and publishability risks.")
    parser.add_argument("--root", help="Tall Talents root to scan, for example ~/.tall-talents or bootstrap")
    parser.add_argument("--paths", nargs="*", default=[], help="Additional files or directories to scan")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve() if args.root else None
    files = collect_files(root, args.paths)

    if not files:
        print("[warn] no files found to scan")
        return 0

    all_failures = []
    all_warnings = []

    for file in files:
        failures, warnings = scan_file(file)
        all_failures.extend(failures)
        all_warnings.extend(warnings)

    for path, line_no, label in all_warnings:
        print(f"[warn] {path}:{line_no}: personal identifier to review: {label}")

    for path, line_no, label in all_failures:
        print(f"[fail] {path}:{line_no}: high-confidence secret risk: {label}")

    if all_failures:
        print("[result] privacy scan failed")
        return 1

    print(f"[result] privacy scan passed ({len(files)} files, {len(all_warnings)} warnings)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
