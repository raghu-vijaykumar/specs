# State Management

Rules for managing local and global state in applications.

---

## 1. Principles

- **Minimize global state** — only cross-cutting concerns belong in global state; everything else is local
- **Immutable updates** — state is never mutated in place; always produce a new copy
- **Single source of truth** — the same data never lives in two different stores
- **Explicit data flow** — unidirectional: action → reducer → new state → re-render
- **Colocation** — state lives as close to where it's consumed as possible

---

## 2. State Tiers

| Tier | Location | Examples | Persistence |
|------|----------|----------|-------------|
| **Local** | Component/ screen scope | Form input, toggle state, accordion open/close, scroll position | None |
| **Shared** | Feature-level service/store | Current cart, selected filters, draft post | Session |
| **Global** | Application-wide store | Auth session, theme mode, locale, feature flags | Persistent |
| **Server** | Backend / API | User profile, orders, product catalog | Database |

### Decision Flow

```
Does this state need to survive a screen unmount?
  ├── No  → Local (useState, ref, local variable)
  └── Yes → Does it need to be shared across features?
              ├── No  → Shared (feature-scoped store)
              └── Yes → Global (app-wide store)
```

---

## 3. Rules

### Local State

- Default to local state — only elevate when a concrete need arises
- Never put computed/derived values in state — compute them on render or use memoization
- Form state stays local until submitted

### Shared State

- Accessed via a hook or provider scoped to the feature
- Cleared when the feature is left unless explicitly retained
- No feature accesses another feature's shared state directly — use events or global store

### Global State

- Every entry has a documented purpose and owner
- Global state changes are logged (dev mode) for debugging
- No global state that can be recomputed from server data

### Server State

- Not duplicated in local state — cache, don't copy
- Use a dedicated server-state library (TanStack Query, RTK Query, SWR) for caching, refetching, and optimistic updates
- Stale-while-revalidate as default strategy

---

## 4. Side Effects

- Side effects (API calls, localStorage, timers) are isolated from state logic
- Use a dedicated effect layer or middleware (thunk, saga, effect hook)
- Never call async functions inside reducers / state setters

---

## 5. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | State transitions (reducers, setters) | Language test framework | `npm test` | Any unexpected output |
| Unit | Side effect handlers (thunks, sagas) | Test framework + mocks | `npm test` | Any failure |
| Integration | Feature flow: action → state → UI update | Component test | `npm run test:integration` | UI does not reflect state |
| Dev validation | Immutability check | Immer / structuredClone | Lint rule | Mutable state detected |

### Self-Validation

```bash
npm test
```
