# Feedback

Communicating system state — loading, empty, error, confirmations, progress.

## Variants

### Snackbar / Toast
- Pill: `{radius.pill}`, background dark (near-black), text `{color.surface}`
- Padding: `{space.md}` `{space.lg}`
- Entrance: slide up + fade `{anim.med}`
- Exit: fade out `{anim.fast}`
- Auto-dismiss: 3s (configurable)
- Swipe to dismiss
- Leading icon (24px), message (`{type.body}`), optional action label (`{color.accent}`)
- Stacked when multiple appear

### Loading Spinner
- Two styles:
  - **Pulsing dots**: 3 dots, staggered scale animation, 1.2s loop
  - **Rotating ring**: arc sweep, 1.2s loop
- Sizes: small (20px), large (40px)
- Color: `{color.primary}` default
- Full-page: centered, large. Inline: beside text, small.

### Skeleton Loader
- Placeholder shimmer for unloaded content
- Base: `{color.surfaceAlt}`, highlight: white (light) or `{color.surfaceAlt}` +30% lightness
- Shimmer: left-to-right gradient sweep, 1.5s loop
- Shapes: rounded rect matching the content shape
- Card skeleton: header rect + 2 body lines
- Text skeleton: single line matching `{type.body}` height

### Empty State
- Centered layout: icon/illustration (64px), title (`{type.h2}`), subtitle (`{type.body}` `{color.textMuted}`)
- Optional CTA button (primary)
- Fade-up entrance as a group `{anim.med}`

### Error State
- Same layout as empty but:
  - Error icon in `{color.error}`
  - Shake animation on first appear (translate x ±8px, 3 cycles, `{anim.fast}`)
  - "Retry" button (primary)
  - Optional expandable error detail

### Badge
- Small pill: min height 16px, padding `{space.sm}` horizontal
- Colors: `{color.error}` for alerts, `{color.textMuted}` for counts
- Text: `{type.overline}` `{color.surface}`
- Scale bounce when count changes `{anim.fast}`
- Positioned top-right of parent, offset +4px

### Progress Bar
- Track: 4px tall, full width, `{color.border}` background
- Fill: `{color.primary}`, radius `{radius.pill}`
- Animate fill width `{anim.med}`
- Optional determinate (percentage) or indeterminate (pulsing)

## Accessibility
- Snackbar: `status` role
- Loading: `progressbar` role
- Error: `alert` role
- Badge: `status` role if dynamic
