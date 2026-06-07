# Stepper

Multi-step flow progress — checkout, setup wizard, onboarding forms, multi-screen tasks.

## Variants

### Numbered Stepper

### Layout
- Horizontal bar across top of screen
- Steps: numbered circles (32×32px) connected by lines
  - **Completed**: filled `{color.primary}`, white checkmark, line solid `{color.primary}`
  - **Active**: filled `{color.primary}`, white number, pulse animation
  - **Pending**: outlined `{color.border}`, `{color.textMuted}` number, line dotted `{color.border}`
- Label below each step: `{type.caption}`, active in `{color.primary}`, others in `{color.textMuted}`
- Tappable to go back to completed steps only

### Behavior
- Each step is a separate content area below the stepper bar
- "Next" button (primary) advances step with slide-left animation
- "Back" button (ghost) goes to previous step with slide-right animation
- Content animates: current slides out, next slides in `{anim.med}` `{anim.curve}`
- "Submit" replaces "Next" on the last step
- Form validation: block "Next" if current step is invalid, show inline errors

### Dot Stepper (Compact)

### Layout
- Row of small dots (8×8px), gap 8px
- Active: `{color.primary}`, filled, 10×10px
- Completed: `{color.primary}`, filled
- Pending: `{color.border}`, filled
- No labels — used in tight spaces (onboarding full-screen)

### Behavior
- Read-only indicator (not tappable)
- Dots animate from pending → completed with a scale + color transition `{anim.fast}`

### Side Stepper (Vertical)

### Layout
- Left column: step numbers connected by vertical line
- Right column: step content
- Used on tablets or wide screens where horizontal space allows

### Accessibility
- Stepper: `progressbar` role, `aria-valuenow` = current step
- Each step: `step` role
- Animation: respect `prefers-reduced-motion`
- Keyboard: Tab between Next/Back, Enter to advance
