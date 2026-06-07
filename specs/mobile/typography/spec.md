# Typography & Accessibility

The type system — hierarchy, readability, and text scaling.

## Type Scale

| Style | Token | Size | Weight | Line H | Usage |
|-------|-------|------|--------|--------|-------|
| Display | `{type.display}` | 32px | Bold | 1.2 | Hero titles |
| Heading 1 | `{type.h1}` | 24px | Bold | 1.3 | Screen titles |
| Heading 2 | `{type.h2}` | 20px | SemiBold | 1.3 | Section headers |
| Heading 3 | `{type.h3}` | 18px | SemiBold | 1.4 | Card titles |
| Body | `{type.body}` | 16px | Regular | 1.5 | Default body |
| Body Small | `{type.bodySm}` | 14px | Regular | 1.5 | Secondary text |
| Caption | `{type.caption}` | 12px | Regular | 1.4 | Labels, timestamps |
| Button | `{type.button}` | 16px | SemiBold | 1.0 | Button labels |
| Overline | `{type.overline}` | 11px | Bold | 1.2 | Badges, uppercase |

## Font Family
- iOS: SF Pro
- Android: Roboto
- Fallback: system default

## Accessibility — Text Scaling
- All components respect system font size
- Test at every level: -2, -1, 0 (default), +1, +2, +3
- Layout must not break at maximum scale
- Minimum contrast: 4.5:1 body, 3:1 large text (18px+)

## Line Length
- Optimal: 45–75 characters per line
- Max width on wide screens: 600px for readable text

## Weight Usage
- Bold (700): display, headings, emphasis
- SemiBold (600): subheadings, buttons, active nav
- Regular (400): body text, inputs, passive elements
