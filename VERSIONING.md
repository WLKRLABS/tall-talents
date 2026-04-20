# Versioning

Tall Talents uses SemVer for the repository contract, shipped bootstrap snapshot, and release tags.

## Source Of Truth

- `VERSION` is the current repository version.
- `CHANGELOG.md` tracks `Unreleased` work plus released versions.
- Git tags use the form `vX.Y.Z`.

## Rules

1. Keep `VERSION` in plain `X.Y.Z` format with no prefix.
2. Keep `CHANGELOG.md` in this order:
   - `## Unreleased`
   - latest released version at the top
   - older released versions below it
3. Do not tag a release until:
   - `bash scripts/validate-versioning.sh` passes
   - `bash scripts/release-dry-run.sh --github-owner <owner> --ref <ref>` passes
4. Treat canonical-home moves as release work, not a docs-only cleanup:
   - update README badges, clone URLs, raw install examples, and star-history links
   - update `scripts/install.sh` default GitHub bases
   - rerun the live GitHub install smoke against the final public home before tagging
5. `1.0.0` is reserved for the first release where the public GitHub home, raw installer, docs, and release playbook all agree and pass verification.

## Required Commands

```bash
bash scripts/validate-versioning.sh
bash scripts/release-dry-run.sh --github-owner <owner> --ref main
```

The canonical public home is now `WLKRLABS/tall-talents`. Do not point release docs or installer defaults anywhere else unless the same public smoke passes there first.
