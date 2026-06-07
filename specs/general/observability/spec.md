# Observability

Logging, metrics, tracing, and alerting conventions for all services.

---

## 1. Principles

- **Structured everywhere** — all telemetry is machine-parseable; no free-text logging for operational data
- **No PII in telemetry** — logs, metrics, and traces never contain personally identifiable information
- **Correlation by default** — every operation carries a trace ID that links logs, metrics, and traces
- **Actionable alerts** — every alert has a runbook; if it fires and nobody acts, it's noise

---

## 2. Logging

### Levels

| Level | When | Example |
|-------|------|---------|
| ERROR | Something is broken and needs human attention | DB connection lost, payment failed |
| WARN | Something unexpected but non-critical | Rate limit approaching, retry attempt |
| INFO | Major lifecycle events | User signup, order placed, deploy complete |
| DEBUG | Detailed flow for development | Every function entry/exit, API payload |
| TRACE | Full request-level detail | SQL queries, external API calls, timing |

### Structured Format (JSON)

```json
{
  "timestamp": "2026-06-07T13:00:00.000Z",
  "level": "ERROR",
  "message": "Payment gateway timeout",
  "service": "checkout-service",
  "trace_id": "trc_abc123",
  "user_id": "usr_456",
  "duration_ms": 30500,
  "error": {
    "type": "GatewayTimeout",
    "code": "TIMEOUT",
    "stack": "..."
  }
}
```

### What Not to Log

- Passwords, tokens, secrets
- Full credit card numbers (log last 4 only)
- Raw request/response bodies of PII-containing endpoints
- Stack traces for expected errors (validation, 404)

---

## 3. Metrics

| Metric | Type | What It Measures |
|--------|------|------------------|
| Request rate | Counter | Requests per second per endpoint |
| Error rate | Counter | 5xx / 4xx per endpoint |
| Latency | Histogram | p50, p95, p99 response time |
| Active users | Gauge | Concurrent sessions |
| Queue depth | Gauge | Pending jobs in worker queues |
| DB pool | Gauge | Active/idle/waiting connections |
| Cache hit rate | Counter | Cache hits vs misses |
| Memory / CPU | Gauge | Per-service resource usage |

---

## 4. Tracing

- Trace every request end-to-end (frontend → API → service → DB)
- Include trace ID in HTTP response headers (`X-Trace-Id`)
- Spans for every external call (DB, cache, third-party API)
- Tag spans with: `service`, `operation`, `user_id` (if non-PII), `error`

---

## 5. Alerting Rules

| Condition | Severity | Response |
|-----------|----------|----------|
| Error rate > 5% for 5 min | Critical | Page on-call |
| p95 latency > 2s for 10 min | Warning | Investigate next business day |
| Disk > 85% | Warning | Add capacity |
| Any ERROR log from payment service | Critical | Page on-call |
| Cert expires in < 7 days | Warning | Renew |

---

## 6. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Log format, PII scrubber, level filtering | Language test framework | `npm test` | Any failure |
| Integration | Trace ID propagation, structured log output | Integration test | `npm run test:integration` | Missing or malformed traces |
| Audit | Logs scanned for PII patterns | Custom script / grep | `rg "(password\|secret\|ssn)" logs/` | Any match |
| Alert | Alert conditions fire correctly | Smoke test | `npm run test:smoke` | Alert didn't fire |

### Self-Validation

```bash
npm test && npm run test:integration && rg "(password|secret)" logs/ 2>/dev/null || echo "No PII in logs"
```
