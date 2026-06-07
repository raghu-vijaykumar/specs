# Buttons

Triggers for actions — primary calls to action, secondary options, ghost actions, and icon-only.

## Variants

### Primary Button
- Fill: `{color.primary}`, text: `{color.surface}`
- Radius: `{radius.sm}`, height: 48px
- Padding: `{space.xl}` horizontal
- Label: `{type.button}`
- Press: scale 0.97 `{anim.fast}`
- Entrance: fade-up `{anim.med}`

### Secondary Button
- Border: 1.5px `{color.primary}`, text: `{color.primary}`
- Fill transparent
- Same sizing as primary

### Ghost Button
- No fill, no border
- Text: `{color.primary}`
- Same sizing as primary
- Press: subtle background `{color.primary}` at 10% opacity

### Icon Button
- Circle: 48×48px (`{target.min}`)
- Surface: `{color.surfaceAlt}`, shadow: `{shadow.1}`
- Icon: 24×24px, `{color.text}`
- Press: scale 0.92 `{anim.fast}`

### Floating Action Button (FAB)
- Circle: 56×56px
- Surface: `{color.primary}`, icon: `{color.surface}`
- Shadow: `{shadow.3}`
- Positioned bottom-right, 16px from edges
- Entrance: scale 0→1 with bounce

### Link Button
- No styling, just `{type.body}` in `{color.primary}`
- Underline on press
- Min tap target: `{target.min}`

## States
All buttons: default, pressed, disabled (opacity 0.4), loading (spinner replaces label)

## Layout
- Full-width buttons: stretch to container
- Inline buttons: wrap content
- Button groups: 8px gap between siblings

## Accessibility
- All buttons: `button` role
- Loading state: `aria-busy="true"`
- Icon buttons: always have tooltip/label
