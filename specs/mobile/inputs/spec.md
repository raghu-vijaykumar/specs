# Inputs

Form controls for data entry — auth, profiles, settings, checkout, search.

## Variants

### Text Field
- Outlined container, radius `{radius.sm}`
- Padding: `{space.lg}` horizontal, `{space.md}` vertical
- Border: 1.5px `{color.border}` → `{color.primary}` on focus → `{color.error}` on error
- Label floats above on focus, animates `{anim.fast}` `{anim.curve}`
- Leading icon slot (24×24px, `{color.textMuted}` → `{color.primary}` on focus)
- Trailing clear button when text present
- Error message slides in below, `{type.caption}` `{color.error}`
- Disabled: opacity 0.5

### Search Field
- Text field variant with search icon leading
- Cancel button appears on focus, slides in `{anim.fast}`
- Debounced 300ms onChange

### Toggle / Switch
- Track: 44×24px, radius `{radius.pill}`
- Thumb: 20×20px circle
- On: track `{color.primary}`, thumb `{color.surface}`
- Off: track `{color.border}`, thumb `{color.surface}`
- Thumb animates `{anim.fast}` `{anim.curve}`
- Optional label beside using `{type.body}`

### Segmented Control
- 2–4 segments in pill container, radius `{radius.sm}` height 40px
- Active: fill `{color.primary}`, text `{color.surface}`, `{type.button}`
- Inactive: transparent, text `{color.textMuted}`, `{type.body}`
- Highlight slides between segments `{anim.med}` `{anim.curve}`

### Slider
- Track: 4px tall, radius `{radius.pill}`
- Active track: `{color.primary}`, inactive: `{color.border}`
- Thumb: 28px circle, `{color.primary}`, shadow `{shadow.2}`
- Value label appears above thumb on drag, animates `{anim.fast}`
- Optional discrete steps with snap

### Checkbox
- Box: 22×22px, radius `{radius.sm}`
- Unchecked: border 2px `{color.border}`, fill transparent
- Checked: fill `{color.primary}`, checkmark `{color.surface}`
- Animates `{anim.fast}` `{anim.curve}`
- Label beside using `{type.body}`

### Radio Button
- Circle: 22×22px
- Unselected: border 2px `{color.border}`
- Selected: border `{color.primary}`, inner dot 10px `{color.primary}`
- Animate dot scale `{anim.fast}`

### Search Bar
- Text field variant with search icon leading, clear button trailing
- Rounded pill container: `{radius.pill}`, background `{color.surfaceAlt}`
- On focus: expands full width, cancel button appears (slide-in)
- Debounced 300ms onChange for API calls
- Below the bar: **suggestion chips** (recent searches, trending) and **autocomplete dropdown**

### Autocomplete Dropdown
- Appears below search bar when input length ≥ 2 characters
- `{color.surface}`, `{radius.sm}`, `{shadow.2}`
- Items: icon + text, `{space.lg}` padding, divider between
- Highlight matching text in `{color.primary}`
- "No results" item at bottom if empty
- Dismiss: tap outside, press Escape, or clear input

### Filter Chips
- Horizontally scrollable row below search bar
- Chips: `{radius.pill}`, `{color.surfaceAlt}`, `{type.caption}`
- Active chip: `{color.primary}` fill, white text
- Tappable to toggle, multi-select allowed
- "Clear All" link at the end

## States
All inputs: default, focused, hovered, active, error, disabled

## Accessibility
- Min tap target: `{target.min}`
- Toggle: `switch` role
- Slider: `adjustable` role
- All labels linked via semantics
- Search: `search` role, results announced
