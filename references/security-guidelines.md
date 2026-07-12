# Security Guidelines

## Principles
- **Defense in depth** — validate at every layer (input, API, service, DB)
- **Fail closed** — on error, deny access by default
- **Least privilege** — request only the permissions and data needed
- **No secrets in code** — use env vars or secret manager
- **Dependency hygiene** — regularly scan and update

## Input Validation

| Rule | Detail |
|------|--------|
| Reject early | Validate at API boundary |
| Type coercion | Always coerce and validate types |
| Length limits | Max lengths on all string fields |
| Allowlists | Prefer allowlist over denylist for characters |
| SQL injection | Parameterized queries only |
| XSS | Sanitize output, not input |

## Authentication & Authorization

| Rule | Detail |
|------|--------|
| Auth on every endpoint | Only whitelist login, signup, health |
| Role checks | Every mutation checks role; default-deny |
| Token expiry | Access: 15 min max. Refresh: 7 days with rotation |
| Rate limiting | Per-user, per-IP, per-endpoint tiers |
| Session invalidation | On password change, logout, suspicious activity |

## Data Storage

| Rule | Detail |
|------|--------|
| Encryption at rest | AES-256 for PII and secrets |
| Encryption in transit | TLS 1.2+ for all external communication |
| No plaintext secrets | Hash with bcrypt/argon2; never log secrets |
| Audit log | All access to sensitive data logged |
| Data retention | Automatically purge after retention period |

## OWASP Top 10 (Quick Check)

| Risk | Mitigation |
|------|-----------|
| Broken Access Control | Role checks, default-deny |
| Cryptographic Failures | TLS 1.2+, AES-256, bcrypt |
| Injection | Parameterized queries, input allowlists |
| Insecure Design | Threat modeling in spec phase |
| Security Misconfiguration | Minimal attack surface, disable debug |
| Vulnerable Components | Regular dependency scanning |
| Auth Failures | MFA, rate limiting, session rotation |
| Data Integrity Failures | Signature verification on updates |
| Logging Failures | Structured audit logging |
| SSRF | URL allowlists, no open redirects |
