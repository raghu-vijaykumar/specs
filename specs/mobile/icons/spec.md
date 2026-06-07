# Custom Icons

Hand-crafted icon set. No third-party icon fonts. Each icon is defined by shape description, then refined into code one at a time.

## Design Rules
- Grid: `{icon.size}` (24×24px)
- Stroke: `{icon.stroke}` (2px)
- Line cap: round
- Line join: round
- Style: outlined with rounded terminals
- Padding: 2px internal inset

## Status Tracking
- `draft` — shape described, not yet implemented
- `refined` — implemented and visually approved

## Catalog

### Navigation

| Icon | Description | Status |
|------|-------------|--------|
| `home` | House outline, roof peak centered, walls 80% height | draft |
| `search` | Magnifying glass at 45°, circle left, handle right | draft |
| `profile` | Circle head top-center, shoulders curve below | draft |
| `settings` | Gear: outer circle with teeth, inner circle | draft |
| `back` | Chevron pointing left | draft |
| `chevronRight` | Chevron pointing right | draft |

### Actions

| Icon | Description | Status |
|------|-------------|--------|
| `plus` | Cross with rounded ends | draft |
| `close` | X with rounded ends at 45° | draft |
| `edit` | Pencil at 45°, tip bottom-left | draft |
| `delete` | Trash can: body + lid + vertical lines inside | draft |
| `share` | Connected dots with upward arrow | draft |
| `more` | Three horizontal dots | draft |

### Status

| Icon | Description | Status |
|------|-------------|--------|
| `check` | Checkmark, thick, 45° angle | draft |
| `alert` | Triangle with exclamation | draft |
| `info` | Circle with lowercase "i" | draft |
| `heart` | Two symmetrical curves meeting at bottom point | draft |
| `star` | 5-point star, straight edges | draft |

### Media

| Icon | Description | Status |
|------|-------------|--------|
| `camera` | Rounded rect body + lens circle + flash dot | draft |
| `image` | Landscape with mountain + sun circles | draft |
| `play` | Equilateral triangle pointing right | draft |

## Adding a New Icon
1. Add shape description to the catalog
2. Mark as `draft`
3. Implement as code
4. Review visually, adjust stroke/proportions
5. Mark as `refined`
