# Lists

Arranging content in vertical stacks — settings, contacts, feeds, results.

## Variants

### Simple List Item
- Height: 48px (`{target.min}`) or auto if multi-line
- Padding: `{space.lg}` horizontal, `{space.md}` vertical
- Leading icon: 24×24px, `{color.textMuted}`
- Title: `{type.body}`
- Trailing: chevron, badge, or toggle
- Divider between items: 1px `{color.border}` with `{space.lg}` left inset

### Grouped List
- Section with header label: `{type.caption}` `{color.textMuted}`, padding `{space.md}` horizontal `{space.sm}` vertical
- Items below with rounded container: `{radius.md}` `{color.surface}`
- Items inside share top/bottom borders (no outer border radius on inner items)

### Swipeable List Item
- Simple list item that can be swiped left
- Reveals action buttons behind (delete red, edit gray, etc.)
- Action buttons: 72px wide, labeled, colored
- Snaps open/closed

### Avatar List Item
- Leading: 44×44px circle, initials or image
- Initials: 2 letters, `{type.button}` `{color.surface}`, background `{color.primaryLight}`
- Content: title + subtitle stacked
- Used in: contacts, messages, comments

### Chip / Tag
- Small pill: height 32px, `{radius.pill}`
- Surface: `{color.surfaceAlt}`, text: `{type.caption}` `{color.text}`
- Padding: `{space.sm}` horizontal
- Optional trailing X to dismiss, show on hover
- Optional leading dot for status (8px circle)
- Wrap in a flex row, 8px gap

### Divider
- 1px `{color.border}`
- Full or inset (with `{space.lg}` left margin)
- Optional label in center: `{type.caption}` `{color.textMuted}`

## Accessibility
- List: `list` role
- Items: `listitem` role
- Swipeable: announce available actions
- Chips: `button` role if tappable, `status` role if static
