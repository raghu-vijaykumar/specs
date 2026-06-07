# Cards

Containers for grouping related content. Used across profiles, item previews, actions, and media.

## Variants

### Elevated Card
- Surface: `{color.surface}`
- Shadow: `{shadow.1}`
- Radius: `{radius.md}`
- Padding: `{space.lg}` body, `{space.xl}` horizontal
- Entrance: fade-up `{anim.med}` `{anim.curve}`, offset 20px

### Flat Card
- Surface: `{color.surface}`
- Border: 1px `{color.border}`
- Radius: `{radius.md}`
- No shadow — use on colored backgrounds

### Tappable Card
- Either elevated or flat base
- Press feedback: scale 0.97, `{anim.fast}` `{anim.curve}`
- Min tap target: `{target.min}`
- Trailing chevron when navigable

### Action Card
- Card body + full-width action button at bottom
- Button: surface `{color.primary}`, text `{color.surface}`, radius matches card bottom
- Staggered entrance: card `{anim.med}`, button `+100ms`

### Media Card
- Header image region (16:9 ratio recommended)
- Gradient overlay: transparent → black at 50% opacity, bottom 40% of image
- Title/subtitle overlaid on gradient
- Image top corners match `{radius.md}`, bottom corners flat

### Row Card
- Compact: leading slot → middle content → trailing slot
- Leading: 48×48px (icon, avatar, or initials)
- Middle: title `{type.body}` + subtitle `{type.bodySm}` `{color.textMuted}`
- Trailing: chevron, toggle, or action icon
- Flat style, no shadow

## Behaviors
- Swipe-to-dismiss on row cards
- Long-press reorder (where applicable)

## Accessibility
- Tappable cards: `button` role
- Non-tappable: `group` role
- Min tap target: `{target.min}`
