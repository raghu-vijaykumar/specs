# Dialogs

Overlay boxes for confirmations, alerts, and focused tasks.

## Variants

### Alert Dialog
- Centered card: `{color.surface}`, radius `{radius.md}`, `{shadow.3}`
- Width: 85% of screen, max 400px
- Padding: `{space.xl}` all sides
- Icon at top (48px, `{color.accent}` for warnings, `{color.primary}` for info)
- Title: `{type.h3}`, body: `{type.body}` `{color.textMuted}`
- Buttons at bottom: Primary + Ghost, right-aligned, 8px gap
- Entrance: scale 0.9→1 + fade, `{anim.med}` `{anim.curve}`
- Scrim: `{scrim.dialog}`

### Confirmation Dialog
- Same as alert but with two explicit actions:
  - Cancel (ghost button, left)
  - Confirm (primary button, right, could be `{color.error}` for destructive)
- Dismiss: tap scrim (cancel) or explicit button

### Input Dialog
- Dialog with a text field inside
- Used for quick data entry (rename, prompt)
- Submit button disabled until input is valid

### Full-Screen Dialog
- Slides up like a page, covers full screen
- Top bar: close button left, title center, action right
- Content fills remaining space
- Used for: create/edit flows, pickers
- Entrance: slide up from bottom `{anim.slow}` `{anim.curve}`

## Accessibility
- All dialogs: `dialog` role
- Focus trapped inside dialog
- Dismiss on Escape key
- First actionable element auto-focused
