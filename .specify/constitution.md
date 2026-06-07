# Constitution — Mobile UI Component Spec

## Purpose
A reusable, tech-agnostic UI component spec system. Defines what to build, not how. Copy these specs into any new project — the implementing developer or AI agent translates them into the target framework.

## Design Principles

### 1. Component-Themed, Not Screen-Tied
Components grouped by UI pattern (cards, inputs, navigation), not by screen (login, settings). Any app composes patterns as needed.

### 2. Token-First
All values reference design tokens `{token.name}`. The single source of truth is `specs/general/tokens.md`. Change one file → everything updates.

### 3. Three-Mode System — System, Light, Dark
Every color and shadow token has a **Light** and **Dark** value. The **System** mode follows the device setting and picks the right column automatically. Components never hardcode a color — they reference `{color.*}` and the active mode resolves it.

| Mode | Behavior |
|------|----------|
| System | Follows device. Default. Picks Light or Dark column. |
| Light | Forces light palette. |
| Dark | Forces dark palette. |

### 4. Custom Visual Identity
- No generic icon fonts. Icons are hand-crafted (described in `specs/mobile/icons/spec.md`, refined one-by-one).
- Rounded corners, soft shadows, generous whitespace.
- Warm, muted color palette.

### 5. Animation-Native
Every component has built-in entrance animation and press micro-interaction. Durations reference `{anim.*}` tokens.

### 6. Accessibility-First
- Text scales with system font size.
- Min 48×48px tap targets.
- Every spec includes an accessibility section with roles and labels.

### 7. Framework-Agnostic
Specs describe what the user sees and how it behaves, not which framework API to call.

## Governance
- All values must use `{token.*}` references — no raw values except in `tokens.md`.
- Every component must specify behavior in all three modes (system, light, dark).
- Every component must define entrance animation and press feedback.
- New tokens: if a raw value appears in 3+ components, promote it to `tokens.md`.

### 8. Quality-Gated [NEW]
Every implementation spec must include a **Testing & Validation** section defining how its code will be tested and what commands verify correctness. Without passing quality gates, a spec is marked **in progress**, not final. See `specs/general/quality-gates/spec.md`.
