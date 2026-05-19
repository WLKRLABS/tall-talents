---
slug: pwa-conversion-architect
title: PWA Conversion Architect
summary: Audit an existing web app for honest PWA fit, then design or implement the smallest viable upgrade path with explicit iPhone and browser constraints.
tags:
  - pwa
  - web
  - mobile
  - architecture
triggers:
  - The user asks to make a site or web app installable, offline-capable, or more app-like on iPhone or modern browsers.
  - The task involves manifest, service worker, Home Screen installability, push, offline support, or PWA readiness auditing.
  - A project needs a reality-check on whether PWA is sufficient or native capabilities are actually required.
inputs:
  - Framework or stack, deployment target, and the current app architecture.
  - Current installability state such as manifest, icons, service worker, and mobile UX behavior.
  - Product requirements for offline behavior, notifications, persistence, camera or file access, and auth-sensitive flows.
outputs:
  - Honest PWA fit classification with explicit platform constraints.
  - Gap analysis and minimum viable PWA plan with exact file targets.
  - If implementation is requested, source-grounded code changes plus verification notes.
agent_behavior:
  - Treat PWA as a layered enhancement to the existing app, not a manifest-only checkbox.
  - Preserve working behavior first and prefer the smallest viable changes with the biggest user impact.
  - Separate minimum viable PWA requirements from strongly recommended upgrades, optional enhancements, and native-only needs.
safety:
  - Do not imply native iPhone capabilities where the web platform is partial, fragile, or unsupported.
  - Do not cache auth-sensitive or user-specific responses blindly.
  - Do not recommend push notifications or offline mutations without defining the product behavior and fallback path.
status: active
version: 1.0.0
---

# Goal

Turn an existing website or web app into the strongest honest PWA version of itself by auditing fit first, then defining or implementing a practical upgrade path for installability, offline behavior, mobile UX, and browser-supported capabilities.

# Procedure

## 1. Build The Baseline From Real Project Evidence

Inspect the codebase and deployed behavior before making recommendations.

Capture:

- framework or stack
- hosting or deployment target
- app type and core workflows
- auth model and user-specific data surfaces
- dynamic versus static routes
- current manifest, icons, service worker, and mobile polish
- desired capabilities such as offline support, push, camera, file upload, or local persistence

If those facts are not visible from the repo or runtime, ask only the minimum number of targeted questions needed to avoid bad implementation decisions.

Default questions:

1. What stack is the project built with?
2. Where is it hosted or deployed?
3. Does it use auth or user-specific dashboards or data?
4. What should offline support actually do?
5. Do you want push notifications, camera or file upload, local persistence, or all three?
6. Is the main goal Home Screen app-like launch on iPhone, or are deeper capabilities required?

## 2. Audit The App Across The Required PWA Surfaces

Evaluate the app in these categories:

- Installability: HTTPS, manifest presence, required fields, icons, `start_url`, display mode, theme or background color, and Apple touch metadata.
- Runtime shell and offline behavior: service worker presence, registration, caching strategy, offline fallback, update lifecycle, stale asset risk, and API or route caching boundaries.
- Mobile app-like UX: viewport setup, safe-area handling, touch targets, responsive layout, standalone launch behavior, and Home Screen polish.
- Capability readiness: push notifications, local persistence, IndexedDB or local storage, camera or file access, and graceful degradation for unsupported features.
- Architecture risk: auth sensitivity, dynamic routes, logged-in versus logged-out shells, mutation flows, and stale-data or cache-poisoning risk.
- iPhone and Safari constraints: what is supported, partially supported, unreliable, or effectively native-only.

## 3. Classify PWA Fit Honestly

Classify the project as one of:

- Strong PWA fit: installability, responsive app-like UX, local persistence, dashboard or tool flows, conservative offline shell, notifications, or camera/file upload are enough.
- Medium PWA fit: PWA helps materially, but heavier device integration, complex notifications, or more demanding background behavior may still create native pressure later.
- Weak PWA fit: the product fundamentally depends on native-only capabilities such as deep background execution, system hooks, advanced device APIs, or OS-level integrations that the web cannot reliably provide.

State the classification plainly and explain why.

## 4. Define The Minimum Viable PWA Scope

Identify the smallest change set that makes the app honestly installable and app-like.

Minimum viable scope usually includes:

- `manifest.webmanifest`
- icon set and Apple touch icon
- linked manifest and theme metadata
- standalone display mode
- service worker registration
- basic shell or static-asset caching
- offline fallback when appropriate
- safe mobile layout behavior
- explicit update strategy

Keep this separate from optional advanced work such as push, background sync, aggressive offline data handling, or share targets.

## 5. Design The Production PWA Architecture

For a production-ready plan, specify:

- manifest shape and icon inventory
- exact service worker responsibilities
- what should and should not be cached
- offline behavior for static content, shells, routes, and API data
- cache invalidation and update strategy
- local persistence design
- push notification flow if actually useful
- iPhone-specific launch, safe-area, and fallback handling
- exact files to create or modify

When the framework is known, tailor the architecture to that stack instead of giving generic advice.

## 6. Implement Only When Requested

If the user asks for implementation:

- preserve current functionality first
- patch exact filenames
- add manifest, icons spec, service worker, registration, and offline assets as needed
- keep caching conservative around auth, dynamic routes, and mutations
- use feature detection and fallback UX for partial browser support
- verify the changed runtime behavior after the final edit

## 7. Report In A Decision-Ready Shape

Unless the user explicitly wants code-only output, report in this order:

1. Project Baseline
2. PWA Fit Assessment
3. Current-State Audit
4. Gap Analysis
5. Minimum Viable PWA Plan
6. Production PWA Architecture
7. File-by-File Implementation Plan
8. Risk Notes
9. Recommended Build Order
10. Acceptance Checklist
11. Optional Code Generation

# Success Criteria

- The project receives an explicit strong, medium, or weak PWA fit classification tied to real evidence.
- Minimum viable PWA requirements are separated cleanly from optional enhancements and native-only needs.
- Service worker and caching guidance are conservative, explicit, and safe around auth and dynamic data.
- iPhone and Safari limitations are called out plainly instead of being glossed over.
- If implementation is requested, the file-by-file plan or patch preserves existing behavior and includes verification.

# Common Failure Modes

- Treating PWA as just adding a manifest and icons.
- Blindly caching everything, including auth-sensitive or user-specific responses.
- Claiming native-like iPhone behavior for features that Safari or Home Screen PWAs do not reliably support.
- Recommending push notifications without defining the product use case, permission UX, and fallback path.
- Skipping update strategy and leaving users stuck on stale assets or shells.
- Mixing minimum viable installability work with advanced capability upgrades until the scope becomes unclear.

# Example Prompt

"Use `pwa-conversion-architect` to audit this web app for PWA fit, tell me whether it is a strong, medium, or weak candidate, and then give me the smallest honest implementation plan with exact files, caching boundaries, and iPhone-specific constraints."
