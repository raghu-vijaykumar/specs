# System Flows

Screens and flows that handle the app lifecycle — first launch, updates, errors, permissions, and meta info.

## Onboarding

### Purpose
Introduce the app to first-time users. Explain core value prop, request key permissions, and set up initial preferences.

### Layout
- Full-screen, swipeable pages (PageView or equivalent)
- Page indicator at bottom (3–4 dots max)
- Each page: illustration area (top 50%) + title + subtitle + optional action
- Last page: "Get Started" button (primary, full width)
- Skip link in top-right corner on every page

### Page Structure (recommended)
1. **Welcome** — app name, tagline, hero illustration
2. **Feature Highlight 1** — key functionality
3. **Feature Highlight 2** — differentiator
4. **Permissions** (optional) — what you'll need and why
5. **Get Started** — CTA button, Terms link

### Behavior
- Shown only on first launch (flag stored locally)
- Swipe forward only (no backward swipe, but dots are tappable)
- Skip button dismisses onboarding and jumps to the main app
- After onboarding: trigger permission requests individually (not all at once)

### Accessibility
- Page indicator: announces "Page X of Y"
- Swipe: works with keyboard navigation
- Illustrations: `aria-hidden="true"` (decorative)

---

## Force Update

### Purpose
Block the user from using an outdated, insecure, or broken app version.

### Layout
- Full-screen modal (cannot be dismissed)
- Center-aligned: icon (64px, `{color.accent}`), title (`{type.h2}`), body (`{type.body}` `{color.textMuted}`)
- "Update Now" button (primary) → opens app store
- "No Thanks" button (ghost) — only shown if update is optional, not forced

### Variants

| Severity | Behavior |
|----------|----------|
| **Optional** | Banner at top of app, can be dismissed. "A new version is available." |
| **Recommended** | Modal, can be dismissed but shows again after 3 launches. |
| **Required** | Hard modal, no dismiss. App is unusable until updated. |

### Entry Point
- Checked on app launch via version API
- Server controls min version per platform

### Accessibility
- `alert` role, announced on appear
- Focus trapped inside modal for required variant

---

## Maintenance Mode

### Purpose
App is temporarily unavailable due to server maintenance, database migration, or emergency.

### Layout
- Full screen (not a modal — replaces the app entirely)
- Centered: icon (64px, `{color.accentAlt}`), title (`{type.h2}`), body (`{type.body}`)
- Optional: estimated return time in `{type.body}` format "Back by 2:30 PM"
- No navigation, no back button, no scrim

### Behavior
- Triggered by API returning 503 with `maintenance: true` flag
- Polls server every 30s to check if maintenance is over
- When over: auto-transition back to normal app (no user action needed)

---

## Permissions

### Purpose
Request platform permissions (camera, location, notifications, photo library, etc.) with context — explain *why* before the system dialog.

### Layout
- Bottom sheet (`{radius.lg}`): icon (48px), title (`{type.h3}`), body (`{type.body}` `{color.textMuted}`)
- "Allow" button (primary) → triggers system permission dialog
- "Maybe Later" button (ghost)
- Single permission per sheet (never batch)

### Pattern
1. User triggers a feature that needs a permission (e.g., tapping camera)
2. Show the permission rationale sheet (this spec)
3. User taps "Allow" → native system permission dialog appears
4. If denied: show a different sheet explaining how to enable in Settings

### Permission Rationale Text Template

| Permission | Title | Body |
|------------|-------|------|
| Camera | "Scan & Capture" | "Take photos of documents, scan QR codes, and capture moments." |
| Location | "Your Location" | "Find nearby places, get directions, and personalize your experience." |
| Notifications | "Stay Updated" | "Get alerts for messages, updates, and important activity." |
| Photo Library | "Access Photos" | "Save images, upload profile pictures, and share media." |
| Microphone | "Record Audio" | "Record voice notes, make calls, and add audio to content." |

### Denied State Sheet
- Different tone: "Camera access is turned off. Enable it in Settings to use this feature."
- "Open Settings" button → deep links to app settings
- "Go Back" button (ghost)

### Accessibility
- Permission rationale: `alert` role
- "Allow": announces what permission will be requested

---

## About Screen

### Purpose
App metadata — version, credits, support, and links.

### Layout
- List layout (`specs/lists/spec.md` — grouped list style)
- `{color.surface}` container with `{radius.md}`
- Center-aligned header: app icon (80px), app name (`{type.h2}`), tagline (`{type.bodySm}`)

### Items (in order)
| Item | Content | Action |
|------|---------|--------|
| Version | `1.0.0 (42)` | Copy to clipboard on tap |
| Rate the App | Opens app store review | Store link |
| Share the App | Opens system share sheet | Share intent |
| Contact Support | `support@example.com` | Opens email/message |
| Privacy Policy | Link to legal page | Navigate to `legal/spec.md` |
| Terms of Service | Link to legal page | Navigate to `legal/spec.md` |
| Licenses | Link to legal page | Navigate to `legal/spec.md` (Licenses section) |
| Open Source Credits | Expandable list | See `legal/spec.md` |

### Accessibility
- Version: `button` role (tappable to copy)
- All items have `{target.min}` tap target
- Links open in-app browser where possible

---

## Splash Screen

### Purpose
Branded loading screen shown on cold start. Bridges the gap between launch and first content.

### Layout
- Full screen, centered
- App icon/logo (120px max), centered vertically
- App name below: `{type.h2}` `{color.primary}`
- Loading indicator: `{anim.fast}` delay, then the app's loading spinner at bottom
- Background: `{color.background}` (light) or `{color.surface}` (dark)
- No text other than branding
- No buttons, no interaction

### Behavior

| Phase | What happens | Duration |
|-------|-------------|----------|
| 1. Icon appears | Logo fades in + scales slightly (0.9→1.0) | `{anim.med}` |
| 2. Loading | App initializes (config, auth check, data fetch) | Variable |
| 3. Decision | If logged in → main app. If not → onboarding/auth. | Instant |
| 4. Transition | Current screen cross-fades to destination | `{anim.med}` |

- Minimum splash display: 400ms (avoids flash on fast devices)
- Maximum splash display: 5s timeout → show error state
- No "Skip" button — splash is purely a loading bridge

### Accessibility
- Icon: `aria-hidden="true"` (decorative)
- Announce: "Loading" via screen reader
- Transition: prevent sudden layout shifts
