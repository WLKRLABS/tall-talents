---
slug: supabase-hosted-auth-email-repair
title: Supabase Hosted Auth Email Login Repair
summary: Repair hosted Supabase email/password login after CLI config pushes disable the email provider while signup remains disabled.
tags:
  - supabase
  - auth
  - debugging
  - devops
triggers:
  - A hosted Supabase app returns "Email logins are disabled" from password login.
  - Supabase CLI config was pushed with signup disabled and manually created Auth users cannot sign in.
inputs:
  - Linked Supabase project ref.
  - Local `.env` with Supabase URL and keys, without printing secret values.
  - Access to the Supabase CLI login token or dashboard.
outputs:
  - Email/password provider enabled.
  - Public signup remains disabled.
  - Required application profile row exists for the approved Auth user.
agent_behavior:
  - Treat provider enablement, signup policy, and app authorization profile as separate checks.
  - Verify with Management API or a password-login probe before claiming the issue is fixed.
safety:
  - Do not print Supabase access tokens, anon keys, service role keys, or user passwords.
  - Do not enable public signup as a shortcut for fixing existing-user login.
status: active
version: 1.0.0
---

# Goal

Restore password login for approved users on a hosted Supabase project without reopening public signup or weakening the app's authorization model.

## Use It When

- Password login fails with `Email logins are disabled`.
- A user exists in Supabase Auth but cannot sign in.
- The project uses manually approved users plus app-owned profile or role rows.
- `supabase config push` was recently used to disable signup.

## Procedure

1. Confirm the exact symptom:
   - Capture the login error text.
   - Verify the app is pointed at the intended Supabase project ref.

2. Inspect local config:
   - In `supabase/config.toml`, keep `[auth] enable_signup = false` to block public signup.
   - Keep `[auth.email] enable_signup = true` so hosted email/password login stays enabled.
   - Add a short comment if needed so future agents do not flip the email provider off again.

3. Inspect remote hosted Auth config:
   - Use the Management API or dashboard to verify:
     - `external_email_enabled` is `true`
     - `disable_signup` is `true`
   - If using a CLI token from local keychain, decode it inside the shell and never print it.

4. Push or patch the minimal Auth config:
   - Prefer `supabase config push --yes` after fixing local `config.toml`.
   - If needed, patch only `external_email_enabled = true` through the Management API.
   - Do not change SMTP, invite, OAuth, MFA, or signup settings unless they are part of the observed failure.

5. Verify provider behavior:
   - Run a password login probe with the real email and an intentionally wrong password.
   - Success criterion: the error changes to `Invalid login credentials`, not `Email logins are disabled`.

6. Verify app authorization:
   - List Auth users through the service-role Admin API without printing secrets.
   - Insert or upsert the app profile row for the approved user with the intended role.
   - For first-owner setup, use `owner`; otherwise preserve the requested role.

7. Report clearly:
   - State provider enabled.
   - State public signup remains disabled.
   - State which app profile role was prepared, without exposing secrets or passwords.

## Success Criteria

- Hosted Auth reports `external_email_enabled = true`.
- Hosted Auth reports `disable_signup = true`.
- Password-login probe no longer returns `Email logins are disabled`.
- The approved Auth user has the app-level authorization row required by the codebase.

## Common Failure Modes

- Setting `[auth.email] enable_signup = false` and accidentally disabling hosted email/password login.
- Enabling public signup just to make login work.
- Fixing Supabase Auth but forgetting the app's `profiles` or role table.
- Testing only from the browser after stale URL query parameters still show an old error.

## Example Prompt

"Use `supabase-hosted-auth-email-repair` on this project. Keep public signup disabled, restore email/password login, verify the provider with a wrong-password probe, and make sure the approved Auth user has the required app profile row."
