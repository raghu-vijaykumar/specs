# Accessibility

WCAG compliance, keyboard navigation, screen reader support, and interaction patterns.

---

## 1. Principles

- **Universal by default** — accessibility is not an overlay or afterthought; every component is built accessibly from the start
- **Respect system settings** — honor `prefers-reduced-motion`, `prefers-color-scheme`, and `prefers-contrast-more`
- **Never break keyboard nav** — every interactive element is reachable and operable by keyboard alone
- **Screen reader ready** — every meaningful element has a label, role, and state; no silent UI

---

## 2. WCAG 2.1 AA Compliance

| Category | Requirement | Check |
|----------|-------------|-------|
| Perceivable | Text alternatives for non-text content | Alt text on images, labels on icons |
| Perceivable | Captions for audio/video | Subtitles on all media |
| Perceivable | Content adapts without losing meaning | Responsive layout, reflow to 320px |
| Perceivable | Color not sole differentiator | Don't rely on color alone for status/state |
| Operable | All functionality via keyboard | Tab through every interactive element |
| Operable | No keyboard traps | Focus never gets stuck |
| Operable | Enough time (no auto-logout without warning) | Warn before session timeout |
| Operable | No seizures (no flashing > 3Hz) | No auto-playing animations |
| Operable | Navigable (skip links, headings, landmarks) | Skip to content link, semantic headings |
| Understandable | Language declared | `lang` attribute on HTML |
| Understandable | Predictable behavior | Consistent navigation, no unexpected context changes |
| Understandable | Input assistance | Error suggestions, clear labels |
| Robust | Parsable (valid HTML) | No duplicate IDs, proper nesting |
| Robust | Screen reader compatible | ARIA roles where HTML semantics insufficient |

---

## 3. Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move focus forward |
| Shift+Tab | Move focus backward |
| Enter / Space | Activate focused element |
| Arrow keys (Up/Down) | Navigate within a list, menu, or radio group |
| Arrow keys (Left/Right) | Navigate within a tab panel, slider, or carousel |
| Escape | Close modal, popover, dropdown |
| Home / End | Navigate to first/last item in a list |

### Focus Management

- Focus indicator must be visible (3px minimum outline, 3:1 contrast ratio)
- Skip link at top of page: "Skip to content"
- Modal opens: focus trapped inside, closes: focus returned to trigger element
- Dynamic content: move focus to the new content (or announce it via live region)

---

## 4. Screen Reader Patterns

| Element | Attribute | Value |
|---------|-----------|-------|
| Icon button | `aria-label` | "Close", "Search", etc. |
| Loading state | `aria-busy` | `true` |
| Live content (toast) | `role="alert"` + `aria-live="assertive"` | Announce immediately |
| Dynamic region (feed) | `aria-live="polite"` | Announce when idle |
| Error messages | `aria-describedby` | Link input to its error |
| Progress bar | `role="progressbar"`, `aria-valuenow` | Current value |
| Modal | `role="dialog"`, `aria-modal="true"`, `aria-labelledby` | Title ID |
| Tab panel | `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, `aria-controls` | Full tab pattern |

---

## 5. Animation & Motion

- All animations respect `prefers-reduced-motion`
- If reduced motion: fade transitions instead of slide/scale; disable parallax and auto-scroll
- No animation exceeds 500ms for non-essential effects
- `animation-duration` references `{anim.*}` tokens

---

## 6. Contrast & Color

| Element | Minimum contrast |
|---------|-----------------|
| Normal text | 4.5:1 |
| Large text (18px+ or 14px+ bold) | 3:1 |
| UI components (focus outline, input border) | 3:1 |
| Icons / graphical objects | 3:1 |
| States (hover, active, selected) | 3:1 from background |

---

## 7. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Automated | WCAG violations, contrast, ARIA | axe-core / Lighthouse | `npx axe --exit` | Any violation |
| Keyboard | Tab order, focus trap, skip link | Playwright / manual | `npm run test:keyboard` | Focus stuck or missing |
| Screen reader | Labels, roles, live regions | VoiceOver / NVDA / TalkBack | Manual walkthrough | Element is silent or mislabeled |
| Reduced motion | Animations respect setting | Playwright (emulate) | `npm run test:motion` | Animation plays when reduced |
| Integration | Tap targets ≥ 48×48 | Playwright / custom script | `npm run test:tap-targets` | Target below minimum |

### Self-Validation

```bash
npx axe --exit && npm run test:keyboard && npm run test:tap-targets
```
