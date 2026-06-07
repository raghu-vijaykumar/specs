# Pickers

Date, time, and option pickers — used in forms, filters, scheduling, and profile screens.

## Date Picker

### Purpose
Select a single date (birthday, appointment), date range (booking), or month/year (credit card).

### Layout — Inline Calendar
- Full month grid: 7 columns (Su Mo Tu ...), 6 rows max
- Header: month/year label center, `<` `>` arrows for navigation
- Days: 40×40px tappable circles
  - Today: outlined border `{color.primary}`
  - Selected: filled `{color.primary}`, white text
  - In-range (range mode): `{color.primary}` at 15% opacity
  - Disabled (past/future): `{color.textMuted}` at 40% opacity
- Swipe horizontally to switch months (optional, `{anim.med}`)
- Jump to "Today" button below calendar

### Layout — Compact / Text Mode
- Read-only field showing selected date
- On tap: opens a bottom sheet with the inline calendar
- Also acceptable: platform-native date picker as fallback

### Variants

| Variant | Behavior |
|---------|----------|
| **Single** | Pick one date. Confirm button. |
| **Range** | Pick start + end. Selected range highlighted. Min/max nights enforced. |
| **Month/Year** | Scrollable month list + year list side by side. Used for credit card expiry. |

### Accessibility
- Calendar: `grid` role, days are `gridcell`
- Header arrows: `button` role
- Selected date announced on change
- Keyboard: arrow keys navigate days

---

## Time Picker

### Purpose
Select a time (hour + minute, optionally AM/PM or 24h).

### Layout — Analog (Wheel)
- Two scrollable columns: hours (1–12 or 0–23) and minutes (00–59)
- AM/PM toggle column when in 12h mode
- Each column: 5 visible items, infinite scroll, snap to center
- Selected value: `{type.h1}` `{color.primary}`, others: `{type.body}` `{color.textMuted}`
- Confirmation bar at bottom: Cancel | OK

### Layout — Digital (Input)
- Two text fields: HH and MM, with colon between
- Auto-tab from HH to MM on 2 characters
- AM/PM toggle button beside fields
- Validates on submit: hours 1–12 (or 0–23), minutes 0–59

### Accessibility
- Wheel: `listbox` role, items are `option`
- Digital fields: standard text input semantics
- Time announced on change

---

## Bottom Sheet Picker (Generic)

### Purpose
Pick from a list of options — country, currency, language, category.

### Layout
- Modal bottom sheet (`{radius.lg}`)
- Title: `{type.h3}`, close button top-right
- Search bar at top for long lists
- Scrollable list of options
- Selected item: checkmark `{color.primary}` on the right
- Grouped options: sticky section headers

### Accessibility
- Sheet: `dialog` role, `aria-label` matches title
- List: `listbox` role
- Selected: `aria-selected="true"`
