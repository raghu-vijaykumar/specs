# Bottom Sheets

Overlay panels that slide up. Used for menus, filters, confirmations, extended actions.

## Variants

### Standard Sheet
- Slides up from bottom, `{anim.med}` `{anim.curve}`
- Top radius: `{radius.lg}`
- Drag handle: 32×4px pill, `{color.border}`, centered at top
- Scrim: `{scrim.sheet}`, fades with sheet
- Height: ~50% of screen by default, content scrolls
- Dismiss: swipe down past 40% threshold or tap scrim

### Modal Sheet
- Same as standard but:
  - Scrim: `{scrim.dialog}`
  - Blocks interaction behind (hard modal)
  - Close button (X) in top-right
  - Height: ~80% of screen

### Expandable Sheet
- Three snap points: peek (80px), half (50%), full (90%)
- Starts at peek showing a preview
- Drag between snap points with spring physics
- Smooth transition between states

### Floating Action Row
- Pill: `{radius.pill}`, `{color.surface}`, `{shadow.2}`
- Contains 2–4 icon buttons, 44×44px each
- Padding: `{space.sm}` vertical, `{space.md}` horizontal
- Slides up coordinated with scroll (appears on scroll-up, hides on scroll-down)
- Used for secondary actions on content pages

## Accessibility
- Sheet: `dialog` role
- Scrim is focus-trapping for modal
- Drag handle: tappable as "collapse" button
