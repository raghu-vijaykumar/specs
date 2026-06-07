# Media

Displaying and interacting with images, videos, and galleries.

## Image Viewer

### Purpose
Full-screen viewing of a single image with zoom and pan.

### Layout
- Full screen, black background (always, even in light mode)
- Image centered, scaled to fit on open
- Close button: top-left, 44×44px, white with 20% dark background circle
- Optional caption bar: bottom, fading overlay `{type.caption}` white

### Gestures

| Gesture | Action |
|---------|--------|
| Single tap | Toggle UI overlay (close button, caption) |
| Double tap | Zoom to 2× centered on tap point |
| Pinch | Zoom in/out, 1× to 5× range |
| Drag (zoomed) | Pan the image |
| Drag (at 1×) | Swipe down to dismiss (pull-to-dismiss with opacity fade) |
| Swipe left/right | Next/previous image (if in a gallery) |

### Behavior
- Initial scale: fit within screen (fit within bounds)
- Max scale: 5×
- Double-tap zooms to 2×, double-tap again returns to 1×
- Pull down to dismiss: image follows finger, background fades, release below 30% threshold dismisses

### Accessibility
- Close: `button` role, label "Close image"
- Image: `image` role with description from caption
- Zoom: announce current zoom level

---

## Gallery Grid

### Purpose
Thumbnail grid of images — photo library, product images, user media.

### Layout
- 3-column grid (customizable), no gap between items
- Each cell: square crop, 1:1 aspect ratio
- Thumbnail fills cell, center-cropped
- Optional overlay: play button icon (for videos), selection checkbox, duration badge

### Selection Mode
- Long-press an item to enter selection mode
- Checkmark appears on selected items (top-right circle, `{color.primary}`)
- Selection count in app bar
- Select All / Deselect All actions

### Behavior
- Tap: open Image Viewer at that index
- Smooth scroll (not paginated)
- Lazy load images as they scroll into view
- Placeholder: skeleton loader matching cell size (`{color.surfaceAlt}`)

### Accessibility
- Grid: `list` role with `grid` orientation
- Each cell: `button` role, label from metadata
- Selection state: `aria-selected`

---

## Video Player (Minimal)

### Purpose
Play video content — feed videos, tutorials, profile videos.

### Layout
- Aspect ratio: 16:9, full-width
- Centered play button overlay (64×64px, white circle with 30% dark bg)
- Controls bar (shown on tap, auto-hide after 3s):
  - Play/Pause, scrubber, time counter, full-screen toggle, volume
- Scrubbing: current time / total time, `{type.caption}` white
- Bottom gradient overlay for readability on light video content

### States
- **Loading**: spinner centered
- **Error**: "Video unavailable" centered, retry button
- **Completed**: replay button replaces play

### Accessibility
- Player: `application` role
- Play/Pause: `button` role, announces state
- Scrubber: `slider` role
- Captions/subtitles support (if available)
