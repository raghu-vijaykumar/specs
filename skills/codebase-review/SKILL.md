---
name: codebase-review
description: Analyze existing codebases for modular design violations — oversized modules, duplicated logic, misplaced seams, and missing abstractions — then drive targeted fixes using code-design principles. Use before a refactor, as a health check, or when inheriting a legacy codebase.
---

# Codebase Review

## Overview

Scan an existing codebase for structural issues using the **code-design** vocabulary: depth, seams, service-layer separation, and extraction triggers. This is not a lint pass — it's a structural audit that looks for patterns known to cause maintenance pain, bug propagation, and low developer leverage.

Each finding maps to a targeted fix. The goal is a smaller, cleaner codebase with higher depth and less duplication.

## When to Use

- Before starting a major refactor (establish the target state)
- Inheriting or onboarding into an unfamiliar codebase
- After repeated bugs in the same area (structural causes)
- As a periodic health check on an active codebase
- When a code review surfaces the same kinds of issues across multiple PRs

**Don't use when:** The codebase is well-structured and already follows code-design principles — it would be noise.

## Analysis Dimensions

Audit each dimension independently. Findings compose into a fix plan.

### 1. Module Size Scan

Detect oversized modules that probably contain multiple concepts:

- **Grep for files > 300 lines** — manually inspect for concept mixing
- **Grep for functions > 50 lines** — likely doing too much
- **Check exports per file** — > 5 exports suggests multiple responsibilities

**What to look for:** A file named `utils.ts` with 400 lines and 12 exports is almost certainly a god module.

### 2. Duplicated Logic Scan

Find operations repeated across callers:

- **Grep for similar blocks** — same error handling pattern, same provider/SDK calls, same validation logic
- **Check bug fix propagation** — "Did we fix this in more than one place?"
- **Look for copy-paste comments** — `// same as in X`, `// copied from Y`

**What to look for:** Email sending, payment processing, file upload, auth token refresh — these are always repeated across features.

### 3. Layer Mixing Audit

Check that orchestration and service concerns aren't tangled:

- **Actions/controllers calling SDKs directly** — missing a service layer
- **Service/modules reaching into DB** — leaky abstraction
- **Domain logic in utility files** — policy decisions should live near the feature
- **Auth checks scattered** — should be in orchestrators or middleware

**What to look for:** A function in `utils/` that checks user permissions and writes to a database.

### 4. Interface Depth Check

For each public module, evaluate depth:

- Is the interface small compared to its implementation?
- Does a caller need to understand internal concepts to use it?
- Does the module pass the deletion test?
- Are there "configuration methods" that exist only to set up internal state?

**What to look for:** A class with 15 public methods where 12 are setters/config that could be constructor parameters.

### 5. Dependency Flow Audit

Check that dependency direction is correct:

- **Circular imports** — the classic red flag
- **Leaf modules importing orchestrators** — services should be imported, not importers
- **Low-level modules knowing about high-level concepts** — a `string` utility should not import from a `services/` module
- **Deep import chains** — A → B → C → D where B and C add no value (pass-through chains)

**What to look for:** `// eslint-disable-next-line import/no-cycle` — that's a circular dependency.

### 6. Naming & Cohesion Check

Check that names match what modules contain:

- A module named `helpers.ts` is almost certainly a grab bag
- A file named `index.ts` with mixed concerns
- A class name that ends in `Manager` or `Util` — often a god object
- Exported names that don't match the file name (inconsistent discoverability)

## Severity Levels

| Level | Label | Action |
|---|---|---|
| **P0** | Structural flaw | Every new feature or bug fix is harder because of this. Fix now. |
| **P1** | Pain point | Has caused bugs or slow-downs. Fix this iteration. |
| **P2** | Code smell | Not hurting yet, but violates principles. Track for next refactor. |
| **P3** | Nit | Personal preference, no measurable impact. Skip. |

## Fix Process

For each P0/P1 finding, follow the **code-design** extraction process:

1. **Understand the seam** — What is this module responsible for? What should callers depend on?
2. **Trace callers** — Who imports this? What do they actually use?
3. **Design the target interface** — What should the deep, small interface look like?
4. **Extract step by step** — Split one concept at a time, verify after each move
5. **Verify** — Typecheck, lint, tests still pass

```
Audit → Prioritize (P0–P3) → For each P0/P1:
  Understand seam → Trace callers → Design interface → Extract → Verify
```

## Fix Patterns

| Finding | Typical Fix |
|---|---|
| God module | Split into 2+ modules by seam, expose each through its own interface |
| Duplicated block | Extract to a service module with explicit params and structured return |
| Leaky service | Remove DB access from service, pass data from orchestrator |
| Pass-through chain | Delete intermediate layers, let endpoint call the leaf directly |
| Circular import | Extract shared dependency into a third module that both import |
| Missing abstraction | Introduce a service module for the repeated operation |
| Misplaced code | Move domain logic to orchestrator, move mechanics to service |
| Oversized function | Extract helper functions by step, then extract a service if steps are reusable |

## Output

The review produces:

1. **Summary** — Overall codebase health (1–2 sentences)
2. **Findings table** — Dimension, file, severity, description
3. **Fix plan** — Ordered list of P0/P1 fixes with target interface sketch
4. **Verification** — Tests, typecheck, lint must pass after each fix
5. **Residual** — P2/P3 items tracked but not actioned

## Example Finding

```
Severity: P1
Dimension: Duplicated Logic
File: src/features/orders/createOrder.ts:45, src/features/invoices/sendInvoice.ts:32
Pattern: Same email-sending block with inline HTML and SMTP config
  → Extract to src/services/email.ts with `sendEmail(params: EmailParams)` interface
  → Callers just pass { to, subject, body }
  → Fix eliminates two duplicate blocks, one seam for future email changes
```

## Verification

After each fix in the plan:

- [ ] All original behaviour preserved (tests pass)
- [ ] Module passes the deletion test
- [ ] No new circular imports
- [ ] Dependencies flow one direction
- [ ] Service functions accept explicit params
- [ ] No copy-paste remains
- [ ] Typecheck and lint pass
- [ ] New module placement matches repo conventions

## Related Skills

- **code-design** — The design principles this audit checks against
- **code-review-and-quality** — Five-axis review for PRs (use during, not instead of, this audit)
- **code-simplification** — Chesterton's Fence, Rule of 500, complexity reduction
- **performance-optimization** — Structural issues often cause perf problems; audit then profile
