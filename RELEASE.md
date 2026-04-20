# Release Playbook

This file is the repo-root release contract for Tall Talents.

Use it for every tagged release and especially for the `1.0.0` launch cutover.

## Preconditions

- Work from the intended checkout.
- Keep the diff intentional. Do not start a release from a repo state you do not understand.
- Confirm current mode if bootstrap or talent content changed:

```bash
python3 scripts/dev-env.py status
```

## 1. Prepare Release Metadata

1. Decide the target version.
2. Update `CHANGELOG.md`:
   - keep `## Unreleased`
   - move releasable notes into `## <version> - <YYYY-MM-DD>`
3. Update `VERSION`.
4. Run:

```bash
bash scripts/validate-versioning.sh
```

## 2. Run The Release Dry Run

Run the full repo-side proof before tagging:

```bash
bash scripts/release-dry-run.sh --github-owner <public-owner> --ref main
```

That command proves:

- local-install workflow
- remote-style workflow from this checkout
- live GitHub raw-install workflow for the chosen public owner
- bootstrap validation, rebuild, and sync
- version/changelog consistency
- tag availability for `v$(cat VERSION)`

## 3. Canonical-Home Cutover Rules

If the release changes the canonical GitHub home, do not swap docs or defaults blindly.

Cut over in this order:

1. Confirm the target repo exists publicly:

```bash
curl -fsSI https://github.com/<owner>/tall-talents
curl -fsSI https://raw.githubusercontent.com/<owner>/tall-talents/main/scripts/install.sh
```

2. Update all canonical public surfaces:
   - README badges
   - clone URL
   - raw install examples
   - star-history link
   - `scripts/install.sh` defaults
   - shipped identity examples that would look productized
3. Push the cutover commit to the target public repo.
4. Prove the live GitHub install path:

```bash
bash scripts/smoke-github-install.sh --owner <owner> --ref main
```

Do not change the public README or installer defaults to a target owner that still returns `404`.

## 4. Tag The Release

After the dry run and any canonical-home smoke both pass:

```bash
git tag "v$(cat VERSION)"
git push origin main --follow-tags
```

## 5. Launch Sign-Off

Do not call the release done until all of these are true:

- `bash scripts/validate-versioning.sh` passes
- `bash scripts/release-dry-run.sh --github-owner <public-owner> --ref main` passes
- `bash scripts/smoke-github-install.sh --owner <public-owner> --ref main` passes against the final public home
- `git diff --check` passes
- the release docs, install defaults, and public GitHub home all match

## `1.0.0` Specific Rule

Do not tag `1.0.0` until the final public home is the intended canonical owner and the GitHub-hosted install smoke has passed there.
