# Theme

The visual foundation — how all tokens map to actual visual output. This spec exists to document the design intent behind the tokens.

> **Note**: All values are defined in `tokens.md`. That is the single source of truth. This file explains why they exist.

## Color Philosophy
- **Primary** (deep plum → lighter indigo in dark): Trust, stability — financial, productivity, utility apps
- **Accent** (coral): Energy, action — CTAs, notifications, highlights
- **Warm neutrals**: Approachable, less clinical than true gray/white
- Dark mode: reverse luminosity while keeping the same accent energy

## Spacing Philosophy
- Base unit: 4px
- Doubles predictably (4, 8, 12, 16, 24, 32, 48)
- Typography line heights use 1.3–1.5x to align naturally to the 4px grid

## Dark Mode
- Surface colors invert: whites become near-blacks
- Primary lightens for contrast (light background needs dark primary, dark background needs light primary)
- Accent stays the same — maintains brand identity
- Shadows deepen (more opacity) to create depth on dark surfaces

## When to Add a New Token
- If a raw value appears in 3+ components, promote it to a token
- Don't over-tokenize — one-off values stay inline
- Group tokens by category: color, space, radius, type, shadow, anim
