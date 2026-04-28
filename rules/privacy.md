# Privacy Rule

Talents can be personal in origin, but committed talents must be publishable.

Do not commit:

- secrets, tokens, API keys, passwords, service-role values, private keys, or session cookies
- private URLs, internal hostnames, customer data, or private repo names unless they are intentionally public and necessary
- personal machine paths, personal emails, account names, or project names when a placeholder would preserve the workflow
- copied logs that include credentials, auth headers, reset links, or access tokens

Prefer placeholders:

- `<project-root>`
- `<user-home>`
- `<github-owner>`
- `<repo-name>`
- `<provider-token>`
- `<customer-name>`

If private context is useful to the owner but not safe to publish, keep it in `~/.tall-talents/private/` or another local-only note. Convert that context into sanitized operational steps before moving anything into `~/.tall-talents/talents/`.
