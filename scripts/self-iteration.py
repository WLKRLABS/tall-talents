#!/usr/bin/env python3
import argparse
import re
from datetime import date
from pathlib import Path


REPORT_TEMPLATE = """# Talent Self-Iteration Report

- Conversation type: {conversation_type}
- Talents activated: {talents_activated}
- Talents that should not have activated: {talents_should_not}
- Talents that should have activated: {talents_should_have}
- Evidence found: {evidence_found}
- Changes made: {changes_made}
- No-change rationale: {no_change_rationale}
"""


def slugify(value: str) -> str:
    slug = value.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "session"


def report_path(root: Path, visibility: str, session: str):
    stem = f"{date.today().isoformat()}-{slugify(session)}.md"
    if visibility == "private":
        base = root / "private" / "self-iteration"
    else:
        base = root / "reports" / "self-iteration"
    base.mkdir(parents=True, exist_ok=True)
    return base / stem


def create_report(args):
    root = Path(args.root).expanduser().resolve()
    path = report_path(root, args.visibility, args.session)
    if path.exists() and not args.force:
        raise SystemExit(f"refusing overwrite; report exists: {path}")

    content = REPORT_TEMPLATE.format(
        conversation_type=args.conversation_type,
        talents_activated=args.talents_activated,
        talents_should_not=args.talents_should_not,
        talents_should_have=args.talents_should_have,
        evidence_found=args.evidence_found,
        changes_made=args.changes_made,
        no_change_rationale=args.no_change_rationale,
    )
    path.write_text(content, encoding="utf-8")
    print(f"[ok] wrote {path}")


def changelog_path(root: Path, talent: str):
    path = root / "talents" / talent / "CHANGELOG.md"
    if not path.exists():
        raise SystemExit(f"CHANGELOG.md not found for talent package: {talent}")
    return path


def append_changelog(args):
    root = Path(args.root).expanduser().resolve()
    path = changelog_path(root, args.talent)
    title = args.title or "automatic refinement"
    entry = f"""
## {date.today().isoformat()} - {title}

- Session: {args.session}
- Change: {args.change}
- Evidence: {args.evidence}
- Effect: {args.effect}
- Oscillation check: {args.oscillation_check}
- Report: {args.report}
"""
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"[ok] appended {path}")


def recent_changelog(args):
    root = Path(args.root).expanduser().resolve()
    path = changelog_path(root, args.talent)
    headings = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            headings.append(line)
    for heading in headings[-args.limit :]:
        print(heading)


def main():
    parser = argparse.ArgumentParser(description="Small file-mechanics helpers for Tall Talents self-iteration.")
    parser.add_argument("--root", default="~/.tall-talents", help="Root path of live Tall Talents folder")
    subparsers = parser.add_subparsers(dest="command", required=True)

    report_parser = subparsers.add_parser("create-report")
    report_parser.add_argument("--session", required=True, help="Session id or timestamp")
    report_parser.add_argument("--visibility", choices=["private", "sanitized"], default="private")
    report_parser.add_argument("--conversation-type", default="unspecified")
    report_parser.add_argument("--talents-activated", default="none")
    report_parser.add_argument("--talents-should-not", default="none")
    report_parser.add_argument("--talents-should-have", default="none")
    report_parser.add_argument("--evidence-found", default="none")
    report_parser.add_argument("--changes-made", default="none")
    report_parser.add_argument("--no-change-rationale", default="none")
    report_parser.add_argument("--force", action="store_true", help="Overwrite an existing report path")
    report_parser.set_defaults(func=create_report)

    append_parser = subparsers.add_parser("append-changelog")
    append_parser.add_argument("--talent", required=True, help="Talent package slug")
    append_parser.add_argument("--session", required=True, help="Session id or timestamp")
    append_parser.add_argument("--change", required=True)
    append_parser.add_argument("--evidence", required=True)
    append_parser.add_argument("--effect", required=True)
    append_parser.add_argument("--oscillation-check", required=True)
    append_parser.add_argument("--report", required=True)
    append_parser.add_argument("--title", help="Changelog entry title")
    append_parser.set_defaults(func=append_changelog)

    recent_parser = subparsers.add_parser("recent-changelog")
    recent_parser.add_argument("--talent", required=True, help="Talent package slug")
    recent_parser.add_argument("--limit", type=int, default=5)
    recent_parser.set_defaults(func=recent_changelog)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
