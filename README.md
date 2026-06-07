# App Spec Template

Framework-agnostic design and architecture specs — reusable as a starting point for any project.

## Structure

```
.specify/constitution.md   — Design principles & governance rules
specs/
├── mobile/                — Mobile UI component specs
│   ├── bottom_sheets/     — Standard, modal, expandable, floating action row
│   ├── buttons/           — Primary, secondary, ghost, icon, FAB, link
│   ├── cards/             — Elevated, flat, tappable, action, media, row
│   ├── dialogs/           — Alert, confirm, input, full-screen
│   ├── feedback/          — Snackbar, spinner, skeleton, empty/error state, badge, progress
│   ├── icons/             — 18 custom icon designs (all draft)
│   ├── inputs/            — Text field, search, toggle, segmented control, slider, checkbox, radio
│   ├── lists/             — Simple, grouped, swipeable, avatar, chip, divider
│   ├── media/             — Image viewer, gallery grid, video player
│   ├── navigation/        — Bottom nav, top tabs, floating indicator/icons
│   ├── pickers/           — Date picker, time picker, bottom sheet picker
│   ├── stepper/           — Numbered, dot (compact), side (vertical)
│   ├── themes/            — Design philosophy behind tokens
│   └── typography/        — 9-level type scale, font family, text scaling
└── general/               — Platform-agnostic / cross-cutting specs
    ├── architecture/      — Project structure, screen templates, nav map, data flow, error handling, build pipeline
    ├── doc-sync/          — Doc generation per language, source map, bidirectional sync rules, AI agent instructions
    ├── legal/             — Privacy policy, ToS, licenses, cookie consent, data export, accessibility statement
    └── quality-gates/     — Testing & validation requirements per code type; completion gate template
    ├── system/            — Onboarding, force update, maintenance, permissions, about, splash
    └── tokens.md          — Single source of truth for all design tokens (Light + Dark columns)
```

## Key Concepts

- **Token-based design** — All specs reference `{token.*}` values from `tokens.md`; change one file and everything updates.
- **Three-mode system** — System (follows device), Light, Dark. Color/shadow tokens have Light and Dark columns; spacing, radius, typography, animation stay identical.
- **Animation-native** — Every component has built-in entrance animation + press micro-interaction.
- **Accessibility-first** — Min 48×48px tap targets, roles/labels in every spec.
- **AI agent ready** — Doc-sync spec includes agent instructions for automatic doc generation, source map maintenance, and validation (AGENTS.md).

## Usage

1. Copy the `specs/` folder into your new project
2. Adapt `tokens.md` to your brand colors, spacing, and radii
3. Delete unused component specs
4. Create `design/` folder with `source-map.md`
5. Copy AI agent instructions from `specs/general/doc-sync/spec.md` §6 into `AGENTS.md`
6. Add the language-appropriate doc validator to your build system

## Principles

See `.specify/constitution.md` for the full set of design principles and governance rules.
