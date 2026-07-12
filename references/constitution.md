# Constitution — Design Principles & Governance

## Purpose
A reusable, tech-agnostic UI component spec system. Defines what to build, not how.

## Principles

### 1. Component-Themed, Not Screen-Tied
Components grouped by UI pattern (cards, inputs, navigation), not by screen (login, settings).

### 2. Token-First
All values reference design tokens `{token.name}`. Single source of truth: `specs/general/tokens.md`.

### 3. Three-Mode System — System, Light, Dark
Every color and shadow token has Light and Dark values. System mode follows device setting.

### 4. Custom Visual Identity
- No generic icon fonts. Hand-crafted icons described in `specs/mobile/icons/`.
- Rounded corners, soft shadows, generous whitespace.
- Warm, muted color palette.

### 5. Animation-Native
Every component has built-in entrance animation and press micro-interaction.

### 6. Accessibility-First
- Text scales with system font size.
- Min 48×48px tap targets.
- Every spec includes an accessibility section.

### 7. Framework-Agnostic
Specs describe what the user sees and how it behaves, not which framework API to call.

### 8. Quality-Gated
Every implementation spec must include a Testing & Validation section.

## Governance
- All values must use `{token.*}` references — no raw values except in `tokens.md`.
- Every component must specify behavior in all three modes.
- Every component must define entrance animation and press feedback.
- New tokens: if a raw value appears in 3+ components, promote it to `tokens.md`.
