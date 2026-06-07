# Design Tokens — Single Source of Truth

Change a value here → every component using that token updates automatically.

## Mode System

Every UI exists in one of three modes:

| Mode | Behavior |
|------|----------|
| **System** | Follows the device setting. Picks `Light` values when the device is in light mode, `Dark` values when in dark mode. **Default for all apps.** |
| **Light** | Forces light appearance. Uses `Light` column for all color tokens. |
| **Dark** | Forces dark appearance. Uses `Dark` column for all color tokens. |

Components never hardcode a color. They reference `{color.*}` and the active mode resolves the right value.

## Color

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `{color.primary}` | `#2D2B55` | `#7B79C2` | Primary actions, active states |
| `{color.primaryLight}` | `#5B59A0` | `#9D9BD6` | Hover, subtle primary backgrounds |
| `{color.accent}` | `#FF6B6B` | `#FF6B6B` | Emphasis, alerts, CTAs |
| `{color.accentAlt}` | `#FFB347` | `#FFB347` | Warm accents, ratings |
| `{color.surface}` | `#FFFFFF` | `#1C1C2E` | Card backgrounds, sheets |
| `{color.surfaceAlt}` | `#F8F7F4` | `#252538` | Secondary surfaces, input backgrounds |
| `{color.background}` | `#F5F3F0` | `#14141F` | Page backgrounds |
| `{color.text}` | `#1A1A2E` | `#F0EFED` | Primary text |
| `{color.textMuted}` | `#8E8E9A` | `#8E8E9A` | Secondary text, placeholders |
| `{color.border}` | `#E8E6E1` | `#2E2E42` | Dividers, input borders |
| `{color.error}` | `#E74C3C` | `#FF6B6B` | Error states |
| `{color.success}` | `#27AE60` | `#2ECC71` | Success states |

## Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `{space.xs}` | 4px | Tight inner padding |
| `{space.sm}` | 8px | Inner padding, small gaps |
| `{space.md}` | 12px | Standard padding, gaps |
| `{space.lg}` | 16px | Section padding, card margins |
| `{space.xl}` | 24px | Large sections |
| `{space.xxl}` | 32px | Page margins, major sections |
| `{space.xxxl}` | 48px | Top-level page padding |

Spacing does not change between modes — it's identical in light and dark.

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `{radius.sm}` | 8px | Inputs, small elements |
| `{radius.md}` | 14px | Cards, sheets, containers |
| `{radius.lg}` | 20px | Modal sheets, large overlays |
| `{radius.pill}` | 999px | Tags, badges, pills |

Radius does not change between modes.

## Typography

| Token | Size | Weight | Line H | Usage |
|-------|------|--------|--------|-------|
| `{type.display}` | 32px | Bold (700) | 1.2 | Hero titles |
| `{type.h1}` | 24px | Bold (700) | 1.3 | Screen titles |
| `{type.h2}` | 20px | SemiBold (600) | 1.3 | Section headers |
| `{type.h3}` | 18px | SemiBold (600) | 1.4 | Card titles |
| `{type.body}` | 16px | Regular (400) | 1.5 | Default body |
| `{type.bodySm}` | 14px | Regular (400) | 1.5 | Secondary text |
| `{type.caption}` | 12px | Regular (400) | 1.4 | Labels, timestamps |
| `{type.button}` | 16px | SemiBold (600) | 1.0 | Button labels |
| `{type.overline}` | 11px | Bold (700) | 1.2 | Badges, overlines |

Typography does not change between modes (sizes stay the same, only the `{color.text}` resolves differently).

## Shadows

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `{shadow.1}` | `0 2px 8px rgba(0,0,0,0.08)` | `0 2px 8px rgba(0,0,0,0.25)` | Cards, subtle depth |
| `{shadow.2}` | `0 4px 16px rgba(0,0,0,0.12)` | `0 4px 16px rgba(0,0,0,0.30)` | Sheets, elevated elements |
| `{shadow.3}` | `0 8px 24px rgba(0,0,0,0.16)` | `0 8px 24px rgba(0,0,0,0.36)` | Modals, overlays |

Shadows are deeper in dark mode to create visible depth on dark surfaces.

## Animation

| Token | Value | Usage |
|-------|-------|-------|
| `{anim.fast}` | 200ms | Micro-interactions, state changes |
| `{anim.med}` | 300ms | Entrance, transitions |
| `{anim.slow}` | 500ms | Large transitions, page changes |
| `{anim.curve}` | ease-out cubic | Default easing |

Animation does not change between modes.

## Icon

| Token | Value |
|-------|-------|
| `{icon.stroke}` | 2px |
| `{icon.size}` | 24×24px grid |

## Scrim

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `{scrim.sheet}` | black 40% | black 50% | Behind bottom sheets |
| `{scrim.dialog}` | black 50% | black 60% | Behind dialogs, modals |

Scrim is slightly more opaque in dark mode to separate layers.

## Accessible Tap Target

| Token | Value |
|-------|-------|
| `{target.min}` | 48×48px |
