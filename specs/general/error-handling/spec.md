# Error Handling

Error taxonomy, propagation patterns, user-facing messages, and recovery strategies.

---

## 1. Principles

- **Fail gracefully** — never crash the app; show a meaningful recovery path
- **Errors are typed** — throw and catch typed errors, not bare strings or `Error()` with a message
- **Every error has a code** — human-readable string (e.g., `NETWORK_TIMEOUT`, `VALIDATION_ERROR`)
- **Log, don't swallow** — caught errors are logged at the appropriate level before recovery
- **User sees actions, not errors** — a user-facing error includes what the user can do next

---

## 2. Error Taxonomy

### Error Types

```typescript
// Base interface
interface AppError {
  code: string;
  message: string;       // Technical — for developers
  userMessage: string;   // User-facing — for display
  userAction: string;    // What the user can do
  severity: 'fatal' | 'error' | 'warning' | 'info';
  recoverable: boolean;
  retryable: boolean;
  cause?: Error;
}
```

| Type | code prefix | Severity | Recoverable | Examples |
|------|-------------|----------|-------------|----------|
| Validation | `VALIDATION_` | error | Yes | `VALIDATION_REQUIRED_FIELD`, `VALIDATION_INVALID_EMAIL` |
| Network | `NETWORK_` | error/warning | Yes (retry) | `NETWORK_TIMEOUT`, `NETWORK_OFFLINE` |
| Auth | `AUTH_` | error | Yes (re-auth) | `AUTH_EXPIRED_TOKEN`, `AUTH_INSUFFICIENT_PERMISSIONS` |
| Not Found | `NOT_FOUND_` | warning | No | `NOT_FOUND_USER`, `NOT_FOUND_ORDER` |
| Conflict | `CONFLICT_` | error | Yes (refresh) | `CONFLICT_STALE_VERSION`, `CONFLICT_DUPLICATE` |
| Rate Limit | `RATE_LIMIT_` | error | Yes (backoff) | `RATE_LIMIT_EXCEEDED` |
| Internal | `INTERNAL_` | error/fatal | No | `INTERNAL_DB_ERROR`, `INTERNAL_UNEXPECTED` |

---

## 3. Propagation

### Layer Rules

| Layer | Rule |
|-------|------|
| UI | Catch typed errors, map `code` to user-facing message + action. Never show raw `Error.message` |
| Service / Use Case | Throw typed errors. Never catch and re-throw as `Error()` |
| API Handler | Return error response with `code`, `message`, `details`. Never expose stack traces |
| DB / I/O | Catch infrastructure errors, wrap in typed error with context (`code: INTERNAL_DB_ERROR`, `cause: original`) |
| Boundary (root) | Catch-all handler: log full error, show generic "Something went wrong" to user |

### Error Propagation Flow

```
DB Error → Repository wraps → Service wraps with context → 
  ├── API controller formats → JSON error response
  └── UI catches → user message + action
```

---

## 4. User-Facing Error Patterns

| Pattern | Recovery action |
|---------|----------------|
| "Couldn't load {resource}" | Retry button |
| "Connection lost" | Auto-retry with countdown; "Try again" if it fails |
| "Session expired" | "Sign in again" button → re-auth flow |
| "Something went wrong" (catch-all) | "Go to home" + "Report issue" |
| "This page doesn't exist" | "Go to home" button |
| "You don't have access" | "Request access" / "Go back" |
| "{field} is required" | Focus the field |
| "Too many requests" | "Try again in {N} seconds" |

---

## 5. Offline Patterns

| State | Behavior |
|-------|----------|
| Online | Normal operation |
| Offline (detected) | Banner: "You're offline. Changes will sync when reconnected." Queue mutations locally |
| Offline (timeout) | Show cached data if available; disable mutations that require connectivity |
| Reconnected | Sync queued mutations; dismiss banner |

---

## 6. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Every public function throws typed errors in error paths | Language test framework | `npm test` | Any path throws generic Error |
| Unit | User-facing messages are defined for every error code | Language test framework | `npm test` | Code missing userMessage |
| Integration | API returns correct error shapes | Supertest / pytest | `npm run test:integration` | Non-standard error response |
| Boundary | Catch-all handler catches everything | Integration test with forced error | `npm run test:boundary` | Unhandled exception crashes app |
| Offline | Queue + sync behavior | E2E with network condition simulation | `npm run test:e2e -- --offline` | Data lost or not synced |

### Self-Validation

```bash
npm test && npm run test:integration && npm run test:boundary
```
