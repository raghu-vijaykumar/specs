---
name: draw-io
description: |
  Use when creating or editing diagrams in draw.io / diagrams.net.
  Covers layout, colors, typography, connectors, layers, and 7 diagram
  type templates. Validates .drawio files for common issues.
---

# Draw.io Skill

## 1. General Principles

- **Clarity over decoration** — every element serves understanding. Remove anything that doesn't.
- **One concept per diagram** — if a diagram tries to explain multiple things, split it.
- **Consistent visual language** — same shape = same meaning everywhere in the file.
- **Legibility at target export size** — zoom to intended export size and verify every label is readable.

---

## 2. Color Palette

### Semantic Colors

| Token | Usage | Hex (Light) | Hex (Dark) |
|-------|-------|-------------|------------|
| `{primary}` | Main action, active state, brand | `#3B82F6` | `#60A5FA` |
| `{secondary}` | Secondary elements, less emphasis | `#8B5CF6` | `#A78BFA` |
| `{success}` | OK, healthy, complete | `#22C55E` | `#4ADE80` |
| `{warning}` | Degraded, needs attention | `#F59E0B` | `#FBBF24` |
| `{error}` | Failure, blocked, critical | `#EF4444` | `#F87171` |
| `{info}` | Informational, neutral | `#06B6D4` | `#22D3EE` |
| `{neutral}` | Container backgrounds, grid lines | `#F3F4F6` / `#D1D5DB` | `#1F2937` / `#4B5563` |
| `{text}` | All label text | `#111827` | `#F9FAFB` |
| `{background}` | Canvas background | `#FFFFFF` | `#111827` |

### Cloud Provider Colors

| Provider | Token | Hex |
|----------|-------|-----|
| AWS | `{cloud-aws}` | `#FF9900` |
| GCP | `{cloud-gcp}` | `#4285F4` |
| Azure | `{cloud-azure}` | `#0078D4` |
| Kubernetes | `{cloud-k8s}` | `#326CE5` |
| Generic service | `{cloud-generic}` | `#6B7280` |

### Usage Rules

- Fill: use semantic or cloud colors at 100% opacity.
- Stroke: same color as fill or darker variant. Stroke width 2px minimum.
- Text on colored fills: white (`#FFFFFF`) for colors darker than `#6B7280`, dark text (`#111827`) for lighter fills.
- Background grids: `{neutral}` at 40% opacity. Never pure black grid lines.
- Arrows: `{text}` color at 70% opacity. Thicker arrows for primary data flow (3px), thinner for secondary (1.5px).

---

## 3. Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Diagram title | Helvetica / Arial / Open Sans | 16pt | Bold |
| Section heading | Same | 14pt | Semi-bold |
| Component/entity label | Same | 11pt | Normal |
| Connector label | Same | 10pt | Normal (italic optional) |
| Annotation / note | Same | 9pt | Light |

- Minimum readable size: **11pt** (exceptions: 10pt for connector labels, 9pt for notes at 100% zoom).
- No text overflow outside containers — resize the box or abbreviate.
- Consistent alignment: center-align inside boxes, left-align for notes.
- One font family throughout the file. No mixing serif and sans-serif.

---

## 4. Layout Rules

- **No overlapping boxes** — every container and its children are disjoint. Use auto-layout or manual snap-to-grid.
- **Uniform spacing** — minimum 20px gap between unrelated elements, 10px between related elements.
- **Alignment grid** — snap to 10px grid. Vertically align sibling boxes. Horizontally align peer tiers.
- **Equal padding** — 15px minimum padding inside containers for their children.
- **Left-to-right, top-to-bottom** — flow direction by default. Data flows left→right, control flows top→bottom.
- **Swimlane grouping** — use swimlanes (horizontal or vertical) to separate concerns (e.g., user → frontend → API → DB).

---

## 5. Connectors

- **Routing** — orthogonal preferred. Curved only for crossing lines or feedback loops.
- **No crossing lines** — re-route manually or reorder elements to eliminate crossings.
- **Arrow direction** — every arrow points from source to target. Solid arrow = direct call / data flow. Open arrow = async / event. Dashed = return / reference / configuration.
- **Labels** — every meaningful edge gets a label. Labels in 10pt italic, centered on the edge.
- **Anchor points** — connect to specific anchor points on shapes (top/bottom/left/right), not to the shape perimeter. Fixed anchors prevent connector drift on resize.

### Connector Style Table

| Flow type | Line style | Arrow | Width | Example |
|-----------|------------|-------|-------|---------|
| Synchronous call | Solid | Closed arrow (→) | 2px | API request |
| Asynchronous / event | Solid | Open arrow (⇢) | 2px | Message queue |
| Return / response | Dashed | Open arrow (⇢) | 1.5px | HTTP response |
| Data flow | Solid | Closed arrow (→) | 2px | Query result |
| Reference / config | Dotted | None | 1px | Config injection |
| Replication | Dashed | Both or none | 1.5px | DB sync |
| Failover | Solid bold | Closed arrow (→) | 3px | DR failover path |

---

## 6. Layers

- **One concern per layer**: `Background`, `Grid`, `Tiers`, `Services`, `Connectors`, `Labels`, `Notes`, `Annotations`.
- **Layer naming**: `{diagram-type}/{z-index:02}/{concern}` e.g., `sequence/01/lifelines`, `sequence/02/messages`.
- **Lock layers** after finishing to prevent accidental moves.
- **Hide helper layers** before export (grid, notes, draft shapes).

---

## 7. Diagram Type Templates

### 7a. Data Flow Diagram (DFD)

```
┌──────────────────────────────────────────────────┐
│                ╔════════════╗                     │
│                ║  External  ║──────────┐          │
│                ║  Entity    ║          │          │
│                ╚════════════╝          │          │
│                                        ▼          │
│               ┌─────────────────────────┐         │
│               │     Process 1           │         │
│               │  (rounded rect, bold)   │         │
│               └────┬─────────┬──────────┘         │
│                     │         │                    │
│                     ▼         ▼                    │
│      ┌────────────┐         ┌────────────┐        │
│      │ Data Store │         │ Data Store │        │
│      │ (open rect)│         │ (open rect)│        │
│      └────────────┘         └────────────┘        │
│   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─         │
│   Trust boundary (dashed line, {warning})         │
└──────────────────────────────────────────────────┘
```

| Element | Shape | Color |
|---------|-------|-------|
| External entity | Rectangle, sharp corners | `{primary}` |
| Process | Rounded rectangle (rx=8) | `{neutral}` fill, `{text}` border |
| Data store | Rectangle, open right side (use custom shape or two overlapping rects) | `{info}` |
| Data flow | Solid arrow, labeled | `{text}` at 70% |
| Trust boundary | Dashed line, 1.5px | `{warning}` |

### 7b. Sequence Diagram

```
┌─────────────────────────────────────────────────────┐
│  ┌──────┐    ┌──────────┐    ┌──────────┐           │
│  │Client│    │  Service │    │    DB    │           │
│  └──┬───┘    └────┬─────┘    └────┬─────┘           │
│     │             │               │                  │
│     │  ──────→    │               │   sync call      │
│     │             │  ──────→      │   sync call      │
│     │             │  ← ─ ─ ─ ─    │   return         │
│     │  ← ─ ─ ─ ─  │               │   return         │
│     │             │               │                  │
│     │  ⇢ ⇢ ⇢ ⇢   │               │   async event    │
│     │             │               │                  │
│     │◄──────►     │               │   alt fragment   │
│     │  [success]  │               │                  │
│     │◄──────►     │               │   else fragment  │
│     │  [failure]  │               │                  │
│     │             │               │                  │
└─────────────────────────────────────────────────────┘
```

| Element | Shape | Color |
|---------|-------|-------|
| Lifeline | Dashed vertical line | `{neutral}` |
| Activation bar | Thin rectangle on lifeline | `{primary}` |
| Sync message | Solid arrow, filled head | `{text}` |
| Async message | Solid line, open arrow head | `{text}` |
| Return message | Dashed line, open arrow | `{text}` |
| Combined fragment | Rectangle with label compartment at top-left | `{info}` border |

### 7c. Architecture Diagram

```
┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
│  Presentation Tier                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │  Web App │  │  Mobile  │  │  Admin   │    │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
│       │             │             │           │
├─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ┼─ ─ ─ ─ ─ ─ ┼─ ─ ─ ─ ─ ┤
│  API Tier (https)   │             │           │
│       │             │             │           │
│       └─────────────┼─────────────┘           │
│                     ▼                         │
│            ┌──────────────────┐               │
│            │   API Gateway    │               │
│            └────────┬─────────┘               │
│                     │                         │
│    ┌────────────────┼────────────────┐        │
│    ▼                ▼                ▼        │
│ ┌────────┐    ┌──────────┐    ┌──────────┐    │
│ │ Auth   │    │Product   │    │ Order    │    │
│ │Service │    │Service   │    │ Service  │    │
│ └────────┘    └────┬─────┘    └────┬─────┘    │
│                    │               │           │
│               ┌────▼─────┐    ┌───▼──────┐    │
│               │Products  │    │ Orders   │    │
│               │ DB       │    │ DB       │    │
│               └──────────┘    └──────────┘    │
├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┤
│  Data Tier                                    │
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
```

| Element | Shape | Color |
|---------|-------|-------|
| Tier boundary | Large rounded rect, dashed | `{neutral}` fill at 10%, `{neutral}` border |
| Service | Rounded rect | `{primary}` for core, `{secondary}` for supporting |
| Database | Cylinder shape | `{info}` |
| External | Rectangle, sharp corners | `{cloud-generic}` |
| Communication | Solid arrow with protocol label | `{text}` |

### 7d. Class Diagram

```
┌──────────────────────┐
│    «abstract»         │
│  ┌──────────────────┐ │
│  │   PaymentMethod  │ │  ← class name (bold, centered)
│  ├──────────────────┤ │
│  │ - id: UUID      │ │  ← attributes (left-aligned)
│  │ - amount: Decimal│ │
│  ├──────────────────┤ │
│  │ + process():     │ │  ← methods (left-aligned)
│  │   Result         │ │
│  │ # refund(): void │ │
│  └──────────────────┘ │
│         ▲             │
│         │             │
│  ┌──────┴───────┐     │
│  │ CreditCard   │     │  ← inherits
│  └──────────────┘     │
│                       │
│  ┌──────────┐ ◇────── │  ← composition
│  │ Payment  │         │
│  └──────────┘         │
└──────────────────────┘
```

| Relationship | Line | Arrow |
|--------------|------|-------|
| Inheritance | Solid | Hollow triangle pointing to parent |
| Association | Solid | Regular arrow or none |
| Composition | Solid | Filled diamond at owner |
| Aggregation | Solid | Hollow diamond at owner |
| Dependency | Dashed | Open arrow pointing to dependency |

**Multiplicity**: `1`, `0..1`, `0..*`, `1..*`, `*` — placed near the target end of the relationship line.

### 7e. Entity Relationship Diagram (ERD)

```
┌───────────────────────┐
│       users           │  ← entity name (bold)
├───────────────────────┤
│ PK  id          UUID  │  ← primary key
│     email       VARCHAR│
│     name        VARCHAR│
│     created_at  TS    │
├───────────────────────┤
│   1 ────────< *       │  ← one-to-many
└───────────────────────┘
         │
         │  (crow's foot at many side)
         ▼
┌───────────────────────┐
│      orders           │
├───────────────────────┤
│ PK  id          UUID  │
│ FK  user_id     UUID  │  ← foreign key
│     total       DECIMAL│
│     status      VARCHAR│
│     created_at  TS    │
└───────────────────────┘
```

| Notation | Meaning |
|----------|---------|
| `PK` | Primary key column |
| `FK` | Foreign key column |
| `╪` / crow's foot | Many side of relationship |
| `|` — `|` | One-to-one (single line both sides) |
| `|` — `<` | One-to-many (crow's foot at many) |
| `<` — `>` | Many-to-many (crow's foot both sides) |

### 7f. Network Topology Diagram

```
┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
│  AWS Region: us-east-1                      │
│  ┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐   │
│  │  VPC: 10.0.0.0/16                    │   │
│  │  ┌──────────────────────────────┐    │   │
│  │  │  Public Subnet 10.0.1.0/24    │    │   │
│  │  │  ┌──────┐  ┌──────┐          │    │   │
│  │  │  │  ALB │──│  NAT │          │    │   │
│  │  │  └──┬───┘  └──────┘          │    │   │
│  │  └─────┼─────────────────────────┘    │   │
│  │        │                              │   │
│  │  ┌─────▼─────────────────────────┐    │   │
│  │  │  Private Subnet 10.0.2.0/24    │    │   │
│  │  │  ┌──────┐  ┌──────┐          │    │   │
│  │  │  │  EC2 │──│  RDS │          │    │   │
│  │  │  └──────┘  └──────┘          │    │   │
│  │  └──────────────────────────────┘    │   │
│  │                                      │   │
│  │  Security Group: web-sg              │   │
│  │  ┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐   │   │
│  │  │  Inbound: 443 from 0.0.0.0/0 │   │   │
│  │  │  Outbound: 80 to 10.0.2.0/24 │   │   │
│  │  └─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘   │   │
│  └─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘   │
│                                            │
│  Traffic: Internet ──(443)──→ ALB ──(80)──→ EC2 ──(5432)──→ RDS │
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
```

| Element | Shape | Color |
|---------|-------|-------|
| Region | Large rounded rect, dashed border | `{cloud-aws}` border |
| VPC | Rounded rect inside region | `{success}` border at 50% |
| Subnet | Rounded rect inside VPC | `{info}` fill at 10% |
| Security group | Rounded rect, dashed border | `{warning}` |
| Resource (EC2, RDS, ALB) | Icon rectangle | `{cloud-aws}` |
| Traffic flow | Solid arrow with protocol:port label | `{text}` |

### 7g. HA / DR Diagram

```
┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐     ┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
│  Primary Region             │     │  Secondary Region           │
│  us-east-1                  │     │  us-west-2                  │
│                             │     │                             │
│  ┌─────────────────────┐    │     │  ┌─────────────────────┐    │
│  │  Application        │    │     │  │  Application        │    │
│  │  ┌──────┐ ┌──────┐   │    │     │  │  ┌──────┐ ┌──────┐   │    │
│  │  │  EC2 │ │  RDS │   │    │ ═══ │  │  │  EC2 │ │  RDS │   │    │
│  │  │Active│ │Primary│   │    │sync │  │  │Standby││Replica│   │    │
│  │  └──────┘ └──────┘   │    │     │  │  └──────┘ └──────┘   │    │
│  └─────────────────────┘    │     │  └─────────────────────┘    │
│                             │     │                             │
│  RTO: 15 min                │     │  RTO: 15 min                │
│  RPO: 5 min                 │     │  RPO: 5 min                 │
│                             │     │                             │
│  [ACTIVE] glow              │     │  [STANDBY] dim              │
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘     └─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘

         Failover flow: DNS update → Route53 → ALB in secondary
         ─ ─ ─ ─(failover)─ ─ ─ →   Traffic shifts to secondary
```

| Element | Shape | Color |
|---------|-------|-------|
| Active region | Rounded rect, bold border (3px) | `{success}` border, subtle glow |
| Standby region | Rounded rect, normal border (1.5px) | `{neutral}` border, dimmed fill |
| Replication link | Dashed double-headed arrow | `{info}` |
| Failover arrow | Bold solid arrow (3px) | `{warning}` |
| RTO/RPO badge | Small rounded rect inside region | `{info}` fill at 80% |
| Resource active | Rectangle with bold border | `{primary}` |
| Resource standby | Rectangle, dashed border, 50% opacity | `{neutral}` |

---

## 8. Export Settings

| Use case | Format | Scale | Border |
|----------|--------|-------|--------|
| Documentation (PDF, wiki) | SVG | 100% | 20px |
| Embedded (web, presentation) | PNG | 200% (2x) | 20px |
| Print | PDF | 100% | 30px |
| Slide deck | PNG | 150% | 15px |

- Turn off grid and page background before export.
- Selection only: select all (Ctrl+A) → right-click → "Export as..." → "Selection only".

---

## 9. Validation

### Manual Checklist

Before marking a diagram as final:

- [ ] No overlapping boxes — visually inspect or run `validate.py`
- [ ] All connectors have valid source and target — no dangling arrows
- [ ] Every connector points in the correct direction
- [ ] All text labels at minimum 11pt (10pt for connector labels)
- [ ] Consistent color palette — no out-of-palette raw colors
- [ ] Font family is consistent throughout
- [ ] Legend exists if using non-obvious colors or custom shapes
- [ ] No stray elements off-canvas
- [ ] Layers are named and locked
- [ ] Grid and helper layers hidden before export
- [ ] Export at correct resolution for target use

### Automated Validation

Run `validate.py` on any `.drawio` file:

```bash
python skills/draw-io/validate.py path/to/diagram.drawio
```

The script checks for:
- Overlapping vertex geometries
- Orphan connectors (missing source or target)
- Font sizes below minimum
- Color compliance with the defined palette
- Floating elements (cells without a container)

## 10. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Automated | `.drawio` file structure, overlaps, orphans, fonts, colors | `validate.py` | `python skills/draw-io/validate.py *.drawio` | Any structural issue reported |
| Manual | Semantic correctness, direction, labels | Visual review | — | Misleading or incorrect content |
