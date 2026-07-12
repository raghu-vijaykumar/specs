---
name: code-design
description: Design deep, modular architecture — small interfaces with focused implementations placed at clean seams, extracted when repetition appears. Use when designing new modules, refactoring oversized files, extracting reusable logic, or deciding where a piece of code belongs.
---

# Code Design

## Overview

Design **deep modules** — a lot of behaviour behind a small, well-named interface, placed at the right architectural layer. This produces **leverage** for callers (one capability reused across N sites) and **locality** for maintainers (change in one place, fix everywhere).

Everything in this skill is framework-agnostic. Module placement rules are discovered from the repo itself — conventions, directory structure, and existing patterns.

## When to Use

- Designing a new module or component
- A file has grown too large for one concept (>200–300 lines)
- Same logic repeated across 2+ callers
- Copy-pasting operational blocks between files
- A bug fix in one path doesn't propagate to others doing the same thing
- Adding a new feature that shares mechanics with existing flows
- Before and during any significant refactor

**Don't use when:** Logic is truly domain-specific and used by only one caller. Small one-off scripts or configuration files don't need this.

## Vocabulary

Use these terms consistently:

| Term | Meaning |
|---|---|
| **Module** | Anything with an interface and an implementation. A function, class, file, or folder. Deliberately scale-agnostic. |
| **Interface** | Everything a caller must know to use the module — type signature, invariants, ordering constraints, error modes, config, perf. |
| **Implementation** | What's inside the module. The body of code that callers never touch. |
| **Depth** | Behaviour per unit of interface. A module is **deep** when a small interface exposes lots of capability. |
| **Seam** | A place where you can alter behaviour without editing in that place (Michael Feathers). Where the interface lives. |
| **Leverage** | What callers get from depth — one implementation serves N callers. |
| **Locality** | What maintainers get — change, bugs, and knowledge concentrate in one place. |
| **Seam** | Where a module's interface lives. Distinct from "boundary" (DDD overloaded). |

## Deep vs Shallow

**Deep module** — small interface, large implementation:
```
  ┌─────────────────────┐
  │   Small Interface   │   Few methods, simple params
  ├─────────────────────┤
  │                     │
  │  Deep Implementation│   Complex logic hidden
  │                     │
  └─────────────────────┘
```

**Shallow module** — large interface, thin implementation (avoid):
```
  ┌─────────────────────────────────┐
  │       Large Interface           │   Many methods, complex params
  ├─────────────────────────────────┤
  │  Thin Implementation            │   Just passes through
  └─────────────────────────────────┘
```

When designing an interface, ask:
- Can I reduce the number of methods / exports?
- Can I simplify the parameters?
- Can I hide more complexity inside?

## Core Principles

### 1. The Deletion Test
Imagine deleting the module entirely. If complexity vanishes, it was a pass-through. If complexity reappears scattered across N callers, the module is earning its keep.

### 2. Extract on 2+ Use Sites
One caller with an adapter means a **hypothetical** seam. Two callers means a **real** one. Don't introduce a module unless something actually varies across it.

### 3. Interface is the Test Surface
Callers and tests cross the same seam. If you need to test *past* the interface, the module is probably the wrong shape.

### 4. Accept Dependencies, Don't Create Them
```typescript
// Good — testable
function processOrder(order, paymentGateway) {}

// Bad — hidden dependency, hard to test
function processOrder(order) {
  const gateway = new StripeGateway();
}
```

### 5. Return Results, Don't Produce Side Effects
```typescript
// Good — testable
function calculateDiscount(cart): Discount {}

// Hard to test — mutates input
function applyDiscount(cart): void {
  cart.total -= discount;
}
```

## Service Layer Architecture

Two-layer separation that emerges naturally from the extraction rules:

| Orchestration (Caller/Action) | Service (Shared Mechanics) |
|---|---|
| Owns business rules & policy | Owns reusable operations |
| Owns state transitions | Owns provider/SDK interactions |
| Owns auth / ownership checks | Owns command execution details |
| Owns failure classification | Owns health checks / readiness |
| Owns retry / user-facing errors | Returns structured results |
| Calls service functions | Never reaches into domain state directly |

**Rule of thumb:**
- "What this business flow means" → stays in the orchestrator
- "How to do this operation reliably" → moves to a service module

## Module Placement (Learn from Repo)

Don't guess where modules go. Discover from the repo:

1. **Scan directory conventions** — `lib/`, `utils/`, `services/`, `shared/`, `helpers/`, `infra/`?
2. **Match existing patterns** — Do similar modules live in `src/domain/feature/service.ts` or `src/services/feature.ts`?
3. **Follow the dependency direction** — Services should be leaf-ward (imported by orchestrators, not vice versa)
4. **Use the local test convention** — Where are tests for similar modules? `__tests__/`, `*.test.ts`, `spec/`?

Typical placement by role (validate against repo conventions):

| Role | Usually Goes |
|---|---|
| Domain/orchestration logic | Near the feature it serves |
| Shared operational mechanics | A `services/` or `lib/` directory |
| Provider/SDK adapters | `adapters/` or `providers/` |
| Type definitions | `types/` or co-located with module |
| Utility functions | `utils/` (only if truly generic) |

## Extraction Process

When extracting shared logic from existing code:

1. Write the flow in the orchestrator first (clear behaviour)
2. Mark repeated operational chunks across callers
3. Extract **only** the repeated, non-domain chunks to a service module
4. Replace one caller → verify (typecheck, lint, test) → replace remaining callers
5. Keep domain policy in the orchestrator (auth, state transitions, error classification)
6. Re-verify: all original flows still work

```
New feature? → Write in action → See repeated ops? → Extract to service module
                                → No repetition?  → Keep in orchestrator
```

## Designing Service Functions

Design as **capability blocks**, not monoliths:

```typescript
// Good: composable, caller chooses what to use
createSandbox(...)
prepareRepo(...)
detectPackageManager(...)
installDependencies(...)
```

Each function should:
- Accept all required data as **explicit parameters** (no hidden global/DB access)
- Return **structured outputs** (not throw arbitrary errors)
- Make failure explicit (typed errors, result types, or structured error objects)
- Never reach into domain state directly (let the orchestrator decide)

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| **God module** | One huge file/function hides all control flow | Split by seam/role |
| **Leaky abstraction** | Module reaches into DB or domain state | Move data access to orchestrator or adapter |
| **Over-abstraction** | Logic used by only one caller extracted | Keep inline until caller #2 appears |
| **Inconsistent API** | Each function uses different arg/error styles | Standardize on one pattern |
| **Circular import** | Two modules import each other | Extract shared dependency into a third module |
| **Pass-through chain** | A → B → C → D where B, C, D just delegate | Remove intermediate layers, let A call D directly |
| **Magic strings / config** | Literal values sprinkled everywhere | Pull into constants or config module |

## Verification

After designing or restructuring a module, confirm:

- [ ] All original behaviour preserved (tests pass, no regressions)
- [ ] Module passes the deletion test (removing it would scatter complexity)
- [ ] Interface is smaller than implementation (depth check)
- [ ] No callers reach into implementation details (import from private paths)
- [ ] No circular imports introduced
- [ ] Dependencies flow in one direction (orchestrator → service, never service → orchestrator)
- [ ] Service functions accept explicit params (no hidden state)
- [ ] No repeated blocks remain across the extracted callers
- [ ] Typecheck and lint pass
- [ ] Placement matches repo conventions (same directory pattern as similar modules)

## Related Skills

- **codebase-review** — Scan existing codebases for modular design violations and drive fixes
- **code-review-and-quality** — Five-axis review (includes architecture axis)
- **code-simplification** — Chesterton's Fence, Rule of 500, complexity reduction
