# Navigation

Moving between sections — bottom bars, tabs, floating indicators.

## Variants

### Bottom Navigation Bar
- Height: 64px + safe area, `{color.surface}`, top border 1px `{color.border}`
- 4–5 items distributed evenly
- Active item: filled pill `{color.primary}` at 15% opacity, icon+label in `{color.primary}`
- Inactive: icon in `{color.textMuted}`, label hidden or muted
- Pill slides between items `{anim.fast}` `{anim.curve}`
- Badge support: red dot top-right (12px diameter)
- Page transition: slide horizontal matching direction

### Top Tabs
- Horizontal scrollable row
- Active tab: `{color.primary}`, 3px underline indicator
- Inactive: `{color.textMuted}`
- Indicator slides position + animates width `{anim.med}` `{anim.curve}`
- Padding per tab: `{space.md}` horizontal, `{space.sm}` vertical
- Connected to swipeable `PageView`

### Floating Action Indicator
- Pill: `{radius.pill}`, `{color.primary}`, `{shadow.2}`
- Shows contextual count: "3 new", "Cart (2)"
- Entrance: scale bounce 0→1
- Positioned above bottom nav or bottom-right
- Tappable, navigates to relevant section

### Floating Icons
- Row of 1–4 circular icons, 48×48px each
- Surface: `{color.surface}`, `{shadow.2}`, radius 50%
- Gap: `{space.sm}` between
- Idle animation: ±3px y floating, 2s period, sine wave
- Press: scale pulse, then navigate
- Opposite the FAB position

## Accessibility
- Bottom nav items: `tab` role, `aria-selected`
- Floating icons: `button` role
- All items have accessibility labels
