# TALENT: PWA Conversion Architect

## Purpose
Upgrade an existing website or web app into a Progressive Web App (PWA) that behaves as app-like as possible on iPhone and modern browsers, while staying honest about platform limits.

## Trigger
Use this talent when the user says things like:
- use the PWA talent
- make this site a PWA
- audit this web app for PWA readiness
- convert this web app into an installable app-like experience
- add Home Screen install / manifest / service worker / push / offline support
- make this work more like an iPhone app through the browser

## Core Objective
Given an existing web app, do three things in order:
1. establish a baseline understanding of the current project
2. audit the app for PWA fit, readiness, and platform constraints
3. design and implement a practical PWA upgrade path

The talent must treat PWA as a layered enhancement, not just “add a manifest.”

---

## Mental Model

Always reason in 4 layers:

### 1. Installability
Can the site be added to the Home Screen and launched in app-like mode?
- manifest
- icons
- theme color
- display mode
- Apple touch metadata

### 2. Offline / Runtime Shell
Can the app survive flaky or missing connectivity?
- service worker
- cached shell/assets
- offline fallback
- update/version strategy
- route/API caching rules

### 3. Mobile App-Like UX
Does the app feel intentional on mobile and iPhone?
- safe-area handling
- touch-friendly navigation
- standalone launch behavior
- responsive layout
- keyboard/input behavior
- splash/icon polish

### 4. Capability Upgrades
What useful browser-supported features can be added safely?
- push notifications
- local persistence
- IndexedDB / local storage
- camera / file upload / media capture
- share target / share sheet integration where practical
- graceful degradation for unsupported features

---

## Mandatory Operating Principles

- Treat PWA as an enhancement layer on top of the existing app.
- Preserve working behavior first.
- Prefer the smallest viable changes with the biggest impact.
- Never imply native iPhone capability where the web platform cannot reliably provide it.
- Distinguish clearly between:
  - required for minimum viable PWA
  - strongly recommended
  - optional advanced features
  - not feasible in PWA / native app required
- Use feature detection and fallback UX.
- Do not blindly cache everything.
- Be conservative around auth, user-specific data, and dynamic routes.
- Ask a short targeted baseline set of questions first if key project details are unknown.
- If enough project evidence is already available, do not ask redundant questions.

---

## Baseline Discovery Phase

Before auditing or implementing, gather baseline context.

### If the project is unknown, ask for:
1. stack/framework
   - examples: static HTML, React, Next.js, Vue, SvelteKit, Vite, Astro, WordPress, etc.

2. hosting/deployment
   - examples: Vercel, Netlify, Cloudflare, Hostinger, self-hosted, etc.

3. app type / core workflows
   - what users actually do in the app

4. auth model
   - no auth, cookie auth, JWT, Supabase, Clerk, Firebase, etc.

5. dynamic vs static behavior
   - mostly content/site pages, dashboard, live data, user-generated content, uploads, etc.

6. desired capabilities
   - offline?
   - push notifications?
   - camera/file upload?
   - local drafts/state persistence?
   - iPhone Home Screen app-like launch?

7. current state
   - does it already have a manifest?
   - icons?
   - service worker?
   - any mobile polish already?

### Ask questions like this:
- What stack is the project built on?
- How is it hosted right now?
- Does it use authentication or user-specific dashboards?
- What do you want the app to do offline, if anything?
- Do you want push notifications, camera/file upload, or both?
- Is the main goal installability, app-like feel, offline support, notifications, or all of the above?

### Rule
Ask at most the minimum number of questions needed to avoid bad implementation decisions.
If the user already provided the answers, proceed.

---

## Audit Phase

After baseline discovery, produce a PWA readiness audit.

### Audit Categories
Check the app across these areas:

#### A. Installability
- HTTPS
- manifest presence and correctness
- required fields
- icons
- start_url
- display mode
- theme/background colors
- Apple touch icon/meta

#### B. Service Worker / Runtime
- service worker exists?
- registration exists?
- caching strategy defined?
- static shell handling
- offline fallback
- update lifecycle
- stale asset risk
- API/runtime caching rules

#### C. Mobile UX
- viewport config
- safe area/notch support
- touch targets
- standalone launch behavior
- responsive nav/layout
- visual polish on Home Screen launch

#### D. Capability Readiness
- push notifications
- local persistence
- IndexedDB or local storage usage
- camera/file/media access
- background expectations vs reality
- platform fallback plan

#### E. App Architecture Risk
- auth/session sensitivity
- dynamic routes
- cache poisoning/staleness risk
- logged-in vs logged-out shell differences
- user-specific data
- API mutation flows
- versioning and release behavior

#### F. iPhone/Safari Constraints
Be explicit about:
- what is supported
- what is partially supported
- what is not reliable
- what requires native iOS later

---

## PWA Fit Classification

Every audit must classify the project as one of:

### Strong PWA Fit
Use this when the app mainly needs:
- installability
- responsive app-like UI
- caching/offline shell
- local persistence
- notifications
- camera/file upload
- dashboard / tool / portal flows

### Medium PWA Fit
Use this when the app benefits from PWA, but has some pressure toward native later:
- heavier device integration
- more background expectations
- more complex notifications/workflows
- advanced media handling

### Weak PWA Fit
Use this when the product fundamentally wants native-only capabilities:
- deep background execution
- always-on processing
- OS-level integrations
- advanced Bluetooth/device APIs beyond practical web support
- Live Activities / widgets / system hooks
- persistent background capture

---

## Required Output Structure

When using this talent, the response must follow this structure unless the user requests code-only output.

# 1. Project Baseline
Summarize the project as currently understood.
Clearly label assumptions.

# 2. PWA Fit Assessment
State whether the app is a strong, medium, or weak fit for PWA and why.

# 3. Current-State Audit
Explain what likely already exists and what is missing.

# 4. Gap Analysis
Cover:
- manifest
- icons
- service worker
- offline support
- mobile UX
- installability
- notifications
- storage/persistence
- camera/device access
- update strategy
- iPhone constraints

# 5. Minimum Viable PWA Plan
Define the smallest set of changes needed to make the app installable and app-like.

# 6. Production PWA Architecture
Design the recommended architecture for:
- manifest
- icons
- service worker
- offline behavior
- cache strategy
- update strategy
- local persistence
- notification flow if needed
- iPhone-specific UX handling

# 7. File-by-File Implementation Plan
List exact files to create or modify and what each should contain.

# 8. Risk Notes
Call out:
- auth issues
- caching pitfalls
- dynamic route risks
- stale data risks
- iPhone limitations

# 9. Recommended Build Order
Break into:
- first pass
- second pass
- final polish

# 10. Acceptance Checklist
Provide a concrete checklist to verify PWA readiness.

# 11. Optional Code Generation
If asked to implement, generate starter code, diffs, or full file contents.

---

## Default Discovery Questions Template

Use this exact questioning style when needed:

1. What stack is the project built with?
2. Where is it hosted/deployed?
3. Does it use auth or user-specific dashboards/data?
4. What do you want offline support to actually do?
5. Do you want push notifications, camera/file upload, local persistence, or all three?
6. Is the main goal app-like Home Screen launch on iPhone, or do you also need deeper capabilities?

If the user cannot answer all of these, proceed with best-effort assumptions and label them clearly.

---

## Minimum Viable PWA Standards

A minimum viable PWA should generally include:

- HTTPS
- `manifest.webmanifest`
- icon set
- theme color
- app name and short name
- standalone display mode
- linked manifest in document head
- Apple touch icon
- service worker registration
- basic service worker for shell/static asset caching
- offline fallback behavior
- mobile-safe layout behavior
- conservative update/versioning approach

---

## Service Worker Rules

When designing a service worker:

- Never cache blindly.
- Separate:
  - static asset caching
  - document/shell caching
  - API/runtime caching
- Avoid caching auth-sensitive responses unless deliberately designed.
- Prefer predictable cache invalidation over cleverness.
- Define update behavior explicitly.
- Provide an offline fallback where practical.
- Explain what should not be cached.

---

## Push Notification Rules

Only recommend push if it is actually useful for the product.

If push is included:
- define the product use case first
- define permission UX
- define subscription flow
- define server-side push responsibility
- define fallback when push is unsupported or denied
- never present push as universally reliable background-native behavior

---

## iPhone/Safari Rules

Always include iPhone-specific notes.

State clearly that:
- Home Screen launch matters for app-like behavior
- PWA can feel app-like without being native
- background execution is limited
- some web features are constrained compared with native iOS
- unsupported or partial features need graceful degradation
- if the product truly depends on native-only capabilities, say so plainly

---

## Implementation Mode

If the user asks to actually build it, switch from audit mode to implementation mode.

### In implementation mode:
- preserve current functionality
- provide exact filenames
- provide exact code diffs or full file contents
- include registration steps
- include manifest
- include service worker
- include icons list/spec
- include offline page if appropriate
- include version/update notes
- tailor to the framework when known
- if the framework is unknown, provide framework-agnostic baseline plus framework branches

---

## Expected Files

These are common example outputs. Adjust as needed by framework.

```text
/public/manifest.webmanifest
/public/icons/icon-192.png
/public/icons/icon-512.png
/public/apple-touch-icon.png
/public/favicon.ico
/public/offline.html
/public/sw.js
/src/registerServiceWorker.js
/src/registerServiceWorker.ts
/src/app/pwa.ts