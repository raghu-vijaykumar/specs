# Design Tokens Reference

## Mode System
| Mode | Behavior |
|------|----------|
| **System** | Follows device setting (default) |
| **Light** | Forces light palette |
| **Dark** | Forces dark palette |

Components never hardcode a color. They reference `{color.*}` and the active mode resolves the value.

## Color Tokens

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `{color.primary}` | `#2D2B55` | `#7B79C2` | Primary actions, active states |
| `{color.primaryLight}` | `#5B59A0` | `#9D9BD6` | Hover, subtle primary backgrounds |
| `{color.accent}` | `#FF6B6B` | `#FF6B6B` | Emphasis, alerts, CTAs |
| `{color.accentAlt}` | `#FFB347` | `#FFB347` | Warm accents, ratings |
| `{color.surface}` | `#FFFFFF` | `#1C1C2E` | Card backgrounds, sheets |
| `{color.surfaceAlt}` | `#F8F7F4` | `#252538` | Secondary surfaces |
| `{color.background}` | `#F5F3F0` | `#14141F` | Page backgrounds |
| `{color.text}` | `#1A1A2E` | `#F0EFED` | Primary text |
| `{color.textMuted}` | `#8E8E9A` | `#8E8E9A` | Secondary text, placeholders |
| `{color.border}` | `#E8E6E1` | `#2E2E42` | Dividers, input borders |
| `{color.error}` | `#E74C3C` | `#FF6B6B` | Error states |
| `{color.success}` | `#27AE60` | `#2ECC71` | Success states |

## Spacing Tokens
| Token | Value | Usage |
|-------|-------|-------|
| `{space.xs}` | 4px | Tight inner padding |
| `{space.sm}` | 8px | Inner padding, small gaps |
| `{space.md}` | 12px | Standard padding, gaps |
| `{space.lg}` | 16px | Section padding, card padding |
| `{space.xl}` | 24px | Screen margins, large gaps |
| `{space.xxl}` | 32px | Section spacing |

## Radius Tokens
| Token | Value | Usage |
|-------|-------|-------|
| `{radius.sm}` | 4px | Checkboxes, small elements |
| `{radius.md}` | 8px | Buttons, inputs, cards |
| `{radius.lg}` | 12px | Dialogs, sheets, modals |
| `{radius.xl}` | 16px | Large containers |
| `{radius.full}` | 999px | Pills, chips, avatars |

## Animation Tokens
| Token | Value | Usage |
|-------|-------|-------|
| `{anim.fast}` | 100ms | Micro-interactions, press feedback |
| `{anim.normal}` | 250ms | Transitions, entrance animations |
| `{anim.slow}` | 400ms | Page transitions, emphasis animations |
| `{anim.easeOut}` | cubic-bezier(0, 0, 0.2, 1) | Standard easing |
| `{anim.easeInOut}` | cubic-bezier(0.4, 0, 0.2, 1) | Entrance/exit |
