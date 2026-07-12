# Accessibility Standards

## Principles
- **Universal by default** — accessibility is not an afterthought
- **Respect system settings** — `prefers-reduced-motion`, `prefers-color-scheme`, `prefers-contrast-more`
- **Never break keyboard nav** — every interactive element reachable by keyboard alone
- **Screen reader ready** — every meaningful element has a label, role, and state

## WCAG 2.1 AA Quick Reference

| Category | Requirement |
|----------|-------------|
| Perceivable | Text alternatives for non-text content |
| Perceivable | Captions for audio/video |
| Perceivable | Content adapts without losing meaning (reflow to 320px) |
| Perceivable | Color not sole differentiator |
| Operable | All functionality via keyboard |
| Operable | No keyboard traps |
| Operable | Enough time (warn before session timeout) |
| Operable | No seizures (no flashing > 3Hz) |
| Operable | Navigable (skip links, headings, landmarks) |
| Understandable | Language declared on HTML |
| Understandable | Predictable behavior, consistent navigation |
| Understandable | Input assistance with error suggestions |
| Robust | Valid HTML, no duplicate IDs |
| Robust | ARIA roles where HTML semantics insufficient |

## Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move focus forward |
| Shift+Tab | Move focus backward |
| Enter/Space | Activate focused element |
| Escape | Close modal, dismiss menu |
| Arrow keys | Navigate list, tab, slider |
| Home/End | First/last item in list |

## Screen Reader Patterns

- Use native HTML semantics before ARIA
- `aria-label` on icon-only buttons
- `aria-live="polite"` for dynamic updates
- `role="alert"` for errors
- `aria-expanded` on toggle controls
- Announce toast/snackbar content

## Touch Targets
- Minimum 48×48px (44px acceptable in dense layouts)
- 8px gap between adjacent targets
