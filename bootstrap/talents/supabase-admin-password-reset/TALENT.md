---
slug: supabase-admin-password-reset
title: Supabase Admin Password Reset
summary: Reset an existing Supabase Auth user's password with a service-role workflow that avoids chat-secret exposure and preserves app authorization rules.
tags:
  - supabase
  - auth
  - operations
  - security
triggers:
  - A user lost the password for a dashboard backed by Supabase Auth.
  - The app has no public signup and approved users are managed manually.
  - A service-role key is available locally or in the deployment environment.
inputs:
  - Supabase project URL and service-role key, without printing secret values.
  - The approved user's email address.
  - Knowledge of the app-level profile or role table required after authentication.
outputs:
  - Existing Auth user's password is updated.
  - No password is pasted into chat, command history, or logs.
  - App-level authorization row or role is verified and reported.
agent_behavior:
  - Prefer an interactive local script or Supabase Dashboard action over asking the user to share a password.
  - Treat Auth credentials and app authorization as separate checks.
  - Keep public signup disabled unless the user's explicit goal is to change signup policy.
safety:
  - Do not print service-role keys, anon keys, access tokens, or passwords.
  - Do not create duplicate Auth users when the task is to reset an existing password.
  - Do not enable public signup as a shortcut for account recovery.
status: active
version: 1.0.0
---

# Goal

Recover access for an existing Supabase-backed admin user by changing only the Auth password and verifying that the app still authorizes that user after login.

## Use It When

- The app signs in with `supabase.auth.signInWithPassword`.
- Approved users are created manually in Supabase Auth.
- The dashboard has a separate `profiles`, roles, or membership table that gates admin access.
- The user says they lost or forgot the dashboard password.

## Procedure

1. Confirm the auth boundary:
   - Inspect the login action or route.
   - Verify whether passwords live in Supabase Auth, a local database, or another identity provider.
   - Identify the app-level authorization table and approved roles.

2. Choose the safest reset path:
   - If the user has Supabase Dashboard access, the manual path is Auth > Users > selected user > reset or change password.
   - If the repo has a service-role key, prefer a local script that prompts interactively for the new password.
   - Do not ask the user to paste the new password into chat.

3. Protect secrets:
   - Load `NEXT_PUBLIC_SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` from local environment files or the process environment.
   - Never print key values.
   - Avoid command-line password arguments because they can land in shell history.

4. Reset only the existing Auth user:
   - Look up the Auth user by email using the Admin API.
   - If no user exists, stop and report that account creation is a separate action.
   - Call `auth.admin.updateUserById(user.id, { password })`.

5. Verify app authorization:
   - Query the app's profile, membership, or role row for that Auth user ID.
   - Confirm the role can access the dashboard, such as `owner` or `admin`.
   - Warn if the user can authenticate but lacks app approval.

6. Report the operational result:
   - State that the password was updated for the email address.
   - State the app-level role check result.
   - Remind the user to sign in with the new password, without repeating the password.

## Success Criteria

- The existing Supabase Auth user is found by email.
- The password update succeeds through the Admin API or Supabase Dashboard.
- The password is not exposed in chat, logs, or shell history.
- The app-level authorization row is checked and any missing or insufficient role is reported.

## Common Failure Modes

- Resetting the Auth password but forgetting that the app requires an `owner` or `admin` profile row.
- Creating a second Auth user for the same person instead of updating the existing one.
- Enabling public signup to recover one admin account.
- Passing the password as a visible command argument or asking the user to send it in chat.

# Example Prompt

"Use `supabase-admin-password-reset` for this dashboard account recovery. Confirm the app uses Supabase Auth, reset the existing user's password through a service-role or dashboard workflow without exposing the password or key, verify the app-level admin role row, and report only the non-secret result."
