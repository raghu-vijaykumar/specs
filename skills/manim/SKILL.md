---
name: manim
description: |
  Use when creating animations with Manim (Mathematical Animation Engine).
  Covers code organization, styling, 7 scene type templates with animation
  patterns, pacing, and validation. Diagrams should match the draw-io skill's
  visual language.
---

# Manim Skill

## 1. Principles

- **Clarity over flash** — every animation serves understanding. If a movement doesn't explain something, remove it.
- **Consistent pacing** — same animation type has the same duration everywhere.
- **Text readable at target resolution** — render at final resolution and verify every label is legible.
- **Match diagram visual language** — colors, layout, and hierarchy match the draw-io skill for the same diagram type.

---

## 2. Color Palette

### Semantic Colors

| Token | Usage | Manim Constant | Hex |
|-------|-------|---------------|-----|
| `{primary}` | Main action, active state, brand | `BLUE_C` | `#0066CC` |
| `{secondary}` | Secondary elements, less emphasis | `PURPLE_C` | `#7B2D8E` |
| `{success}` | OK, healthy, complete | `GREEN_C` | `#008A27` |
| `{warning}` | Degraded, needs attention | `YELLOW_C` | `#E6A800` |
| `{error}` | Failure, blocked, critical | `RED_C` | `#CC0000` |
| `{info}` | Informational, neutral | `TEAL_C` | `#008080` |
| `{neutral}` | Container backgrounds, borders | `GREY_C` | `#808080` |
| `{text}` | All label text | `WHITE` (dark bg) | `#FFFFFF` |
| `{background}` | Canvas background | `BLACK` | `#000000` |

### Light Background Variant

For light-background scenes (slides, print):

| Token | Manim Constant | Hex |
|-------|---------------|-----|
| `{text-light}` | `BLACK` | `#000000` |
| `{bg-light}` | `WHITE` | `#FFFFFF` |

### Cloud Provider Colors

| Provider | Manim Constant | Hex |
|----------|---------------|-----|
| AWS | `ORANGE` | `#FF9900` |
| GCP | `BLUE_D` | `#1A56DB` |
| Azure | `BLUE_B` | `#0078D4` |
| Kubernetes | `BLUE_E` | `#1E3A8A` |

### Usage Rules

- Text on colored fills: white text for colors darker than `GREY_C`, dark text (`BLACK`) for lighter fills.
- Stroke width: 2–4px. Thicker (4px) for primary elements, thinner (2px) for secondary.
- Fill opacity: 0.8 for solid elements, 0.3–0.5 for container backgrounds.

---

## 3. Code Organization

### File Structure

```python
# scenes/architecture.py

from manim import *
from constants import *   # shared colors, fonts, durations

class ArchitectureScene(Scene):
    def construct(self):
        self.add_title()
        self.add_tiers()
        self.add_services()
        self.add_connections()
        self.wait(1)
```

### Constants File (`constants.py`)

```python
# Colors (light background variant shown)
PRIMARY = BLUE_C
SECONDARY = PURPLE_C
SUCCESS = GREEN_C
WARNING = YELLOW_C
ERROR = RED_C
INFO = TEAL_C
NEUTRAL = GREY_C
CLOUD_AWS = ORANGE

# Font defaults
FONT_FAMILY = "Sans"
TITLE_SIZE = 36
HEADING_SIZE = 28
LABEL_SIZE = 24
SMALL_SIZE = 18

# Durations (seconds)
BOX_FADE_IN = 0.5
ARROW_GROW = 0.3
TEXT_WRITE = 0.4
WAIT_SHORT = 0.3
WAIT_MEDIUM = 1.0
WAIT_LONG = 2.0

# Layout
FRAME_WIDTH = config.frame_width
FRAME_HEIGHT = config.frame_height
```

### Rules

- One file per scene. One scene class per file.
- `construct()` is the only entry point — no external methods called before it.
- Constants at top or in a separate `constants.py`.
- Helper methods for reusable mobjects (service boxes, database icons, arrows).
- All coordinates relative to `config.frame_width/height` — no hardcoded pixel values.

---

## 4. Styling Guidelines

### Element Types

| Element | Type | Style |
|---------|------|-------|
| Service box | `RoundedRectangle` | `corner_radius=0.15`, fill=`PRIMARY`, stroke=`PRIMARY`, stroke_width=4 |
| Database | Custom `VGroup` of cylinder | `Circle` + `Rectangle` + `Ellipse` at bottom |
| Container | `RoundedRectangle` | `corner_radius=0.2`, fill=color at 0.3 opacity, dashed stroke |
| Arrow | `Arrow` or `CurvedArrow` | `stroke_width=3`, `tip_length=0.2` |
| Label | `Text` | `font=FONT_FAMILY`, `font_size=LABEL_SIZE` |
| Dashed line | `DashedLine` | `stroke_width=2`, `dash_length=0.1` |

### Layout Helpers

```python
def service_box(label: str, color=PRIMARY, width=1.2, height=0.6):
    box = RoundedRectangle(
        corner_radius=0.15,
        width=width,
        height=height,
        fill_color=color,
        fill_opacity=0.8,
        stroke_color=color,
        stroke_width=4,
    )
    text = Text(label, font=FONT_FAMILY, font_size=LABEL_SIZE, color=WHITE)
    return VGroup(box, text).arrange(IN, buff=0)

def container_box(label: str, width=6, height=4, color=NEUTRAL):
    box = RoundedRectangle(
        corner_radius=0.2,
        width=width,
        height=height,
        fill_color=color,
        fill_opacity=0.3,
        stroke_color=color,
        stroke_width=2,
        stroke_opacity=0.6,
    )
    text = Text(label, font=FONT_FAMILY, font_size=HEADING_SIZE, color=color)
    text.to_corner(UL, buff=0.3).next_to(box.get_top(), DOWN, buff=0.3)
    return VGroup(box, text)
```

---

## 5. Scene Type Templates

### 5a. Data Flow Animation

```
Elements animate in by layer:
  1. External entities fade in (top of scene)
  2. Processes fade in below (middle)
  3. Data stores fade in below processes (bottom)
  4. Trust boundary draws as dashed line
  5. Data flow arrows animate one by one
  6. Data packets (small circles) move along arrow paths
```

```python
class DataFlowScene(Scene):
    def construct(self):
        # Step 1: external entities
        external = service_box("External Entity", color=PRIMARY)
        external.to_edge(UP)
        self.play(FadeIn(external, scale=0.8))

        # Step 2: processes
        process = service_box("Process", color=NEUTRAL)
        process.next_to(external, DOWN, buff=1)
        self.play(FadeIn(process, scale=0.8))

        # Step 3: data stores
        datastore = service_box("Data Store", color=INFO)
        datastore.next_to(process, DOWN, buff=1)
        self.play(FadeIn(datastore, scale=0.8))

        # Step 4: trust boundary
        boundary = DashedLine(
            start=LEFT * 4, end=RIGHT * 4, stroke_width=2, color=WARNING
        ).next_to(datastore, DOWN, buff=0.5)
        self.play(Create(boundary))

        # Step 5: arrows
        arrow = Arrow(
            process.get_top(), external.get_bottom(),
            stroke_width=3, color=TEXT_COLOR, buff=0.2
        )
        self.play(GrowArrow(arrow))

        # Step 6: data packet
        packet = Dot(color=PRIMARY, radius=0.08)
        packet.move_to(arrow.get_start())
        self.play(MoveAlongPath(packet, arrow, run_time=1.5))
        self.wait(1)
```

### 5b. Sequence Animation

```
  1. Lifelines draw top-down as dashed lines
  2. Activation boxes appear on lifelines
  3. Messages animate one by one:
     - Sync: solid arrow grows from source to target
     - Async: open arrow grows, dashed return
  4. Combined fragment box draws at end
  5. Note or annotation fades in
```

```python
class SequenceScene(Scene):
    def construct(self):
        client = Text("Client", font=FONT_FAMILY, font_size=LABEL_SIZE).to_edge(UL)
        service = Text("Service", font=FONT_FAMILY, font_size=LABEL_SIZE).shift(RIGHT * 3)
        db = Text("DB", font=FONT_FAMILY, font_size=LABEL_SIZE).shift(RIGHT * 6)

        # Lifelines
        for obj in [client, service, db]:
            line = DashedLine(
                obj.get_bottom(), obj.get_bottom() + DOWN * 3,
                stroke_width=2, color=NEUTRAL
            )
            self.play(Create(line), run_time=0.3)

        # Messages
        arrow_sync = Arrow(
            client.get_bottom(), service.get_bottom(),
            stroke_width=3, color=TEXT_COLOR, buff=0.2
        )
        label = Text("request(data)", font=FONT_FAMILY, font_size=SMALL_SIZE)
        label.next_to(arrow_sync, UP, buff=0.1)
        self.play(GrowArrow(arrow_sync), Write(label))
        self.wait(WAIT_SHORT)

        arrow_async = Arrow(
            service.get_bottom(), db.get_bottom(),
            stroke_width=3, color=TEXT_COLOR, buff=0.2
        )
        label2 = Text("query", font=FONT_FAMILY, font_size=SMALL_SIZE)
        label2.next_to(arrow_async, UP, buff=0.1)
        self.play(GrowArrow(arrow_async), Write(label2))

        # Return
        ret = DashedLine(
            db.get_bottom(), service.get_bottom(),
            stroke_width=2, color=NEUTRAL
        )
        self.play(Create(ret))

        # Fragment
        frag = RoundedRectangle(
            corner_radius=0.1, width=2, height=1.5,
            stroke_color=INFO, stroke_width=2
        )
        frag.next_to(client, DOWN, buff=1).shift(RIGHT * 1.5)
        frag_label = Text("alt [success]", font=FONT_FAMILY, font_size=SMALL_SIZE, color=INFO)
        frag_label.next_to(frag, UP, buff=0.1)
        self.play(Create(frag), Write(frag_label))

        self.wait(1)
```

### 5c. Architecture Animation

```
  1. Presentation tier container fades in (top)
  2. UI services fade in inside container
  3. API tier container fades in below
  4. API services fade in inside container
  5. Data tier container fades in below
  6. Databases fade in inside container
  7. Inter-tier connections draw as arrows
  8. Labels appear on each arrow
```

```python
class ArchitectureScene(Scene):
    def construct(self):
        # Tiers, top to bottom
        tiers_data = [
            ("Presentation", [("Web App", PRIMARY), ("Mobile", PRIMARY)], 3),
            ("API", [("Gateway", SECONDARY), ("Orders", SECONDARY)], 3),
            ("Data", [("Orders DB", INFO)], 2),
        ]
        y_start = FRAME_HEIGHT / 2 - 1
        spacing = 2.5
        tier_boxes = []

        for i, (tier_name, services, _) in enumerate(tiers_data):
            y_pos = y_start - i * spacing
            tier = container_box(tier_name, width=8, height=1.5, color=NEUTRAL)
            tier.move_to(UP * y_pos)
            self.play(FadeIn(tier, scale=0.9))

            for j, (svc_name, color) in enumerate(services):
                svc = service_box(svc_name, color=color)
                svc.next_to(tier, DOWN, buff=0.2).shift(RIGHT * (j - (len(services) - 1) / 2) * 1.5)
                self.play(FadeIn(svc, scale=0.8))
                tier_boxes.append(svc)
            tier_boxes.append(tier)

        # Connections between tiers
        for i in range(len(tier_boxes) - 1):
            arrow = Arrow(
                tier_boxes[i].get_bottom(),
                tier_boxes[i + 1].get_top(),
                stroke_width=2, color=TEXT_COLOR
            )
            self.play(GrowArrow(arrow), run_time=0.3)

        self.wait(1)
```

### 5d. Class Diagram Animation

```
  1. Class boxes draw row-by-row (name → attributes → methods)
  2. Relationship lines grow from source to target
  3. Multiplicity labels write at ends
  4. Stereotypes fade in on class header
```

```python
class ClassDiagramScene(Scene):
    def construct(self):
        # Build a class box row by row
        header = Rectangle(width=3, height=0.5, fill_color=PRIMARY, fill_opacity=0.8)
        name_text = Text("PaymentMethod", font=FONT_FAMILY, font_size=LABEL_SIZE, color=WHITE)
        name_text.move_to(header)
        self.play(FadeIn(header), Write(name_text))

        attr_box = Rectangle(width=3, height=0.8, fill_color=NEUTRAL, fill_opacity=0.3)
        attr_box.next_to(header, DOWN, buff=0)
        attr_text = Text("- id: UUID\n- amount: Decimal", font=FONT_FAMILY, font_size=SMALL_SIZE)
        attr_text.move_to(attr_box)
        self.play(FadeIn(attr_box), Write(attr_text))

        method_box = Rectangle(width=3, height=0.8)
        method_box.next_to(attr_box, DOWN, buff=0)
        method_text = Text("+ process()\n# refund()", font=FONT_FAMILY, font_size=SMALL_SIZE)
        method_text.move_to(method_box)
        self.play(FadeIn(method_box), Write(method_text))

        # Inheritance arrow
        child = header.copy().next_to(header, LEFT * 3)
        child_text = Text("CreditCard", font=FONT_FAMILY, font_size=LABEL_SIZE)
        child_text.move_to(child)
        self.play(FadeIn(child), Write(child_text))

        inherit_arrow = Arrow(
            child.get_top() + UP * 0.1, header.get_bottom() + DOWN * 0.1,
            stroke_width=3, color=TEXT_COLOR
        )
        self.play(GrowArrow(inherit_arrow))

        self.wait(1)
```

### 5e. Entity / ERD Animation

```
  1. Entity boxes draw with header (name), then PK/FK attributes
  2. Relationship lines grow with crow's foot at many end
  3. Cardinality labels appear
```

```python
class ERDScene(Scene):
    def construct(self):
        users = VGroup()
        header = Rectangle(width=3, height=0.5, fill_color=PRIMARY, fill_opacity=0.8)
        title = Text("users", font=FONT_FAMILY, font_size=LABEL_SIZE, color=WHITE).move_to(header)
        attrs = Rectangle(width=3, height=1, fill_color=NEUTRAL, fill_opacity=0.3)
        attrs.next_to(header, DOWN, buff=0)
        attr_text = Text("PK id\nemail\nname", font=FONT_FAMILY, font_size=SMALL_SIZE).move_to(attrs)
        users.add(header, title, attrs, attr_text)
        users.to_edge(LEFT)

        orders = users.copy().to_edge(RIGHT)
        orders[1] = Text("orders", font=FONT_FAMILY, font_size=LABEL_SIZE, color=WHITE).move_to(orders[0])
        orders[3] = Text("PK id\nFK user_id\ntotal", font=FONT_FAMILY, font_size=SMALL_SIZE).move_to(orders[2])

        self.play(FadeIn(users), FadeIn(orders))

        # One-to-many arrow
        line = Line(
            users[0].get_right(), orders[0].get_left(),
            stroke_width=2, color=TEXT_COLOR
        )
        # Crow's foot at orders side
        foot1 = Line(UP * 0.2 + RIGHT * 0.15, ORIGIN, stroke_width=2, color=TEXT_COLOR)
        foot2 = Line(DOWN * 0.2 + RIGHT * 0.15, ORIGIN, stroke_width=2, color=TEXT_COLOR)
        foot1.move_to(line.get_end())
        foot2.move_to(line.get_end())

        one_label = Text("1", font=FONT_FAMILY, font_size=LABEL_SIZE).next_to(line, UP, buff=0.1)
        many_label = Text("*", font=FONT_FAMILY, font_size=LABEL_SIZE).next_to(line, DOWN, buff=0.1)

        self.play(Create(line), Create(foot1), Create(foot2), Write(one_label), Write(many_label))
        self.wait(1)
```

### 5f. Network Topology Animation

```
  1. Region/AZ containers fade in as large dashed boxes
  2. VPC boxes fade in inside region
  3. Subnet boxes fade in inside VPC
  4. Resource icons place inside subnets (DrawBorderThenFill)
  5. Security groups draw as dashed boundaries
  6. Traffic arrows animate with protocol labels
```

```python
class NetworkTopologyScene(Scene):
    def construct(self):
        region = container_box("AWS Region: us-east-1", width=10, height=6, color=CLOUD_AWS)
        region.move_to(ORIGIN)
        self.play(FadeIn(region, scale=0.95))

        vpc = container_box("VPC 10.0.0.0/16", width=8, height=4.5, color=SUCCESS)
        vpc.move_to(region)
        self.play(FadeIn(vpc, scale=0.95))

        pub_subnet = container_box("Public Subnet 10.0.1.0/24", width=7, height=1.5, color=INFO)
        pub_subnet.next_to(vpc, UP, buff=0.5)
        self.play(FadeIn(pub_subnet))

        priv_subnet = container_box("Private Subnet 10.0.2.0/24", width=7, height=1.5, color=INFO)
        priv_subnet.next_to(vpc, DOWN, buff=0.5)
        self.play(FadeIn(priv_subnet))

        # Resources
        alb = service_box("ALB", color=CLOUD_AWS)
        alb.move_to(pub_subnet)
        self.play(DrawBorderThenFill(alb))

        ec2 = service_box("EC2", color=CLOUD_AWS)
        ec2.move_to(priv_subnet).shift(LEFT * 1.5)
        rds = service_box("RDS", color=INFO)
        rds.move_to(priv_subnet).shift(RIGHT * 1.5)
        self.play(DrawBorderThenFill(ec2), DrawBorderThenFill(rds))

        # Security group
        sg = container_box("SG: web-sg", width=3, height=1.5, color=WARNING)
        sg.next_to(vpc, RIGHT, buff=0.5)
        self.play(FadeIn(sg))

        # Traffic arrows
        arrow = Arrow(alb.get_bottom(), ec2.get_top(), stroke_width=3, color=TEXT_COLOR)
        label = Text("HTTP :80", font=FONT_FAMILY, font_size=SMALL_SIZE).next_to(arrow, LEFT, buff=0.1)
        self.play(GrowArrow(arrow), Write(label))

        self.wait(1)
```

### 5g. HA / DR Animation

```
  1. Primary region container fades in left (bold border, glow effect)
  2. Standby region container fades in right (dimmed, normal border)
  3. Active resource glows, standby resource is dimmed
  4. Replication link draws as dashed double-headed arrow
  5. RTO/RPO badges appear in each region
  6. Failover animation: glow transfers from primary to standby
```

```python
class HADRScene(Scene):
    def construct(self):
        primary = container_box("Primary Region\nus-east-1", width=5, height=4, color=SUCCESS)
        primary.to_edge(LEFT, buff=0.5)
        # Add glow effect (surrounding rectangle with low opacity)
        glow = SurroundingRectangle(primary, color=SUCCESS, fill_opacity=0.05, stroke_opacity=0.5)
        self.play(FadeIn(primary), FadeIn(glow))

        standby = container_box("Secondary Region\nus-west-2", width=5, height=4, color=NEUTRAL)
        standby.to_edge(RIGHT, buff=0.5)
        standby.set_opacity(0.6)
        self.play(FadeIn(standby))

        # Active/Standby labels
        active_label = Text("[ACTIVE]", font=FONT_FAMILY, font_size=LABEL_SIZE, color=SUCCESS)
        active_label.next_to(primary, DOWN, buff=0.3)
        standby_label = Text("[STANDBY]", font=FONT_FAMILY, font_size=LABEL_SIZE, color=NEUTRAL)
        standby_label.next_to(standby, DOWN, buff=0.3)
        self.play(Write(active_label), Write(standby_label))

        # Replication link
        rep = DashedLine(
            primary.get_right(), standby.get_left(),
            stroke_width=2, color=INFO
        )
        rep_label = Text("sync (5 min RPO)", font=FONT_FAMILY, font_size=SMALL_SIZE, color=INFO)
        rep_label.next_to(rep, UP, buff=0.1)
        self.play(Create(rep), Write(rep_label))

        # RTO/RPO badges
        for region, pos in [(primary, LEFT), (standby, RIGHT)]:
            rto = RoundedRectangle(corner_radius=0.1, width=2, height=0.4, fill_color=INFO, fill_opacity=0.8, stroke_width=0)
            rto_text = Text("RTO: 15 min", font=FONT_FAMILY, font_size=SMALL_SIZE, color=WHITE).move_to(rto)
            rto_group = VGroup(rto, rto_text)
            rto_group.next_to(region, pos, buff=0.3)
            self.play(FadeIn(rto_group))

        # Failover animation
        self.play(
            glow.animate.set_stroke(color=WARNING, opacity=0.3).set_fill(color=WARNING, opacity=0.05),
            standby.animate.set_opacity(1.0),
            active_label.animate.set_color(NEUTRAL),
            standby_label.animate.set_color(SUCCESS).set_text("[ACTIVE]"),
            run_time=2
        )

        failover_arrow = Arrow(
            primary.get_right(), standby.get_left(),
            stroke_width=4, color=WARNING
        )
        failover_label = Text("FAILOVER", font=FONT_FAMILY, font_size=SMALL_SIZE, color=WARNING)
        failover_label.next_to(failover_arrow, DOWN, buff=0.1)
        self.play(GrowArrow(failover_arrow), Write(failover_label))

        self.wait(1)
```

---

## 6. Pacing & Timing

| Element type | Animation | Duration | rate_func |
|-------------|-----------|----------|-----------|
| Service box | `FadeIn(scale=0.8)` | 0.5s | `smooth` |
| Container | `FadeIn(scale=0.95)` | 0.6s | `smooth` |
| Arrow | `GrowArrow` | 0.3s | `smooth` |
| Text | `Write` | 0.4s | `smooth` |
| Dashed line | `Create` | 0.3s | `linear` |
| Data packet | `MoveAlongPath` | 1.5s | `smooth` |
| Pulse / glow | `Flash` | 0.5s | `there_and_back` |
| Failover | `Transform` / cross-fade | 2.0s | `smooth` |
| Wait (between steps) | `wait()` | 0.5–1.0s | — |
| Wait (before end) | `wait()` | 2.0s | — |

- Every `wait()` MUST have an explicit duration argument. No bare `wait()`.
- Group related elements into a single `play()` call (e.g., `self.play(Create(arrow), Write(label))`).
- Allow 1 second per 10 words for text reading time.

---

## 7. Labels & Text

- Default font size: `LABEL_SIZE = 24` for element labels, `SMALL_SIZE = 18` for connector/attribute labels.
- `Text` for labels (not `Tex`) — use `Tex` only for mathematical notation.
- Add background buffering for text readability over colored fills:

  ```python
  label = Text("Label", font=FONT_FAMILY, font_size=LABEL_SIZE)
  bg = BackgroundRectangle(label, fill_opacity=0.5, buff=0.1)
  self.add(bg, label)
  ```

- Text alignment: center-aligned inside boxes, left-aligned for notes/lists.
- All coordinates relative to `config.frame_width / height` — use `ORIGIN`, `UP`/`DOWN`/`LEFT`/`RIGHT` constants.

---

## 8. Resolution & Output

```bash
# Development (fast, low quality)
manim -pql scenes/architecture.py ArchitectureScene

# Production (high quality, 4K)
manim -pqh scenes/architecture.py ArchitectureScene --resolution 3840,2160

# Transparent background for slides
manim -pqh -t scenes/architecture.py ArchitectureScene
```

| Flag | Use |
|------|-----|
| `-pql` | Iteration / development |
| `-pqh` | Production / final render |
| `-t` | Transparent background |
| `--resolution W,H` | Custom resolution |
| `-o name.mp4` | Custom output filename |

---

## 9. Validation

### Manual Checklist

Before marking a scene as final:

- [ ] Scene runs without errors (`-pql` passes)
- [ ] All `wait()` calls have explicit duration arguments
- [ ] No mobjects overlap at any point in the animation
- [ ] No mobjects are off-screen at rest (check against `config.frame_width/height`)
- [ ] Text is readable at target export resolution
- [ ] Colors match the defined palette (no out-of-palette raw hex)
- [ ] Pacing is consistent (same element types have same durations)
- [ ] Labels don't overflow their containers
- [ ] At least one `wait()` at the end before scene finishes

### Automated Validation

Run `validate.py` on any scene file:

```bash
python skills/manim/validate.py scenes/architecture.py
```

The script checks for:
- Scene class compiles (import + instantiation check)
- Bare `wait()` calls (no duration argument)
- Off-screen absolute coordinates
- Hardcoded color hex values outside palette

## 10. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Compile | Scene imports and parses correctly | Python | `python -m py_compile scenes/scene.py` | Syntax/import error |
| Render | Scene renders without runtime error | Manim | `manim -pql scenes/scene.py SceneName` | Non-zero exit |
| Static analysis | Bare wait() calls, off-screen coords, hardcoded colors | `validate.py` | `python skills/manim/validate.py scenes/scene.py` | Any issue reported |
| Visual | No overlaps, correct layout | Manual review of rendered frame | — | Visual defect |
