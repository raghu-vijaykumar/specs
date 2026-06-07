# API Design

Conventions for REST and GraphQL API design across all services.

---

## 1. Principles

- **Consistent URL structure** — predictable paths, same patterns everywhere
- **Backward compatibility** — additive changes only within a version; breaking changes require a new version
- **Idempotency** — PUT, DELETE, and safe methods produce the same result on repeated calls
- **Self-describing** — every response includes enough context for the client to understand it without out-of-band knowledge

---

## 2. URL Structure (REST)

```
/{version}/{resource}
/{version}/{resource}/{id}
/{version}/{resource}/{id}/{subresource}
```

### Conventions

| Pattern | Example | Method |
|---------|---------|--------|
| List | `GET /v1/users` | GET |
| Read | `GET /v1/users/{id}` | GET |
| Create | `POST /v1/users` | POST |
| Replace | `PUT /v1/users/{id}` | PUT (full resource) |
| Partial update | `PATCH /v1/users/{id}` | PATCH (delta only) |
| Delete | `DELETE /v1/users/{id}` | DELETE |
| Subresource list | `GET /v1/users/{id}/orders` | GET |
| Action | `POST /v1/orders/{id}/cancel` | POST (non-CRUD actions, verb at end) |
| Bulk | `POST /v1/users/bulk` | POST (with array body) |

### Naming Rules

- **Plural nouns** for resources (`/users`, not `/user`)
- **kebab-case** for multi-word resources (`/order-items`)
- **Lowercase** throughout
- **No verbs** in resource names — verbs are HTTP methods or action suffixes
- **Version as prefix** (`/v1/`) — header-based versioning discouraged

---

## 3. Request / Response Shape

### Success Response

```json
{
  "data": { ... },
  "meta": {
    "request_id": "req_abc123"
  }
}
```

### List Response (with pagination)

```json
{
  "data": [ ... ],
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 142,
    "total_pages": 8
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      { "field": "email", "code": "required", "message": "Email is required" }
    ],
    "request_id": "req_abc123"
  }
}
```

### HTTP Status Codes

| Code | When |
|------|------|
| 200 | Success (GET, PUT, PATCH) |
| 201 | Created (POST) |
| 204 | No Content (DELETE, successful POST without body) |
| 400 | Bad Request (validation error, malformed input) |
| 401 | Unauthenticated (missing/invalid credentials) |
| 403 | Forbidden (authenticated but not authorized) |
| 404 | Not Found |
| 409 | Conflict (duplicate, stale version) |
| 422 | Unprocessable Entity (semantic error) |
| 429 | Rate Limited |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## 4. Pagination

- **Cursor-based** preferred for real-time / infinite scroll feeds
- **Offset-based** for admin panels and jump-to-page interfaces
- Default `per_page`: 20. Max: 100.
- Pagination metadata always included in list responses

---

## 5. Versioning

- **URL-prefix versioning**: `/v1/`, `/v2/`
- Minimum support window: **6 months** for old versions
- Deprecation header on old versions: `Sunset: Sat, 1 Jan 2027 00:00:00 GMT`
- Changelog maintained per version

---

## 6. Idempotency

- POST mutations should support an `Idempotency-Key` header
- Idempotency keys expire after 24 hours
- Same key + same request returns original result (not a duplicate)

---

## 7. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Request validation, response serialization | Language test framework | `npm test` | Any failure |
| Integration | Endpoints return correct status codes and shapes | Supertest / pytest | `npm run test:integration` | Status code ≠ expected |
| Contract | OpenAPI/Swagger schema validation | Spectral / Zod | `npx spectral lint openapi.yaml` | Validation error |
| E2E | Full request-response flow | Newman / Supertest | `npm run test:e2e` | End-to-end failure |
| Idempotency | Repeated POST with same key returns same result | Integration test | `npm run test:integration` | Duplicate or inconsistent |

### Self-Validation

```bash
npx spectral lint openapi.yaml && npm test && npm run test:integration
```
