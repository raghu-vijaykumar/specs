# Security

Security patterns, rules, and validation gates for all code.

---

## 1. Principles

- **Defense in depth** — validate at every layer (input, API, service, DB), not just the edge.
- **Fail closed** — on error, deny access by default. Never default to allow.
- **Least privilege** — code should request only the permissions and data it needs.
- **No secrets in code** — API keys, tokens, passwords never appear in source. Use environment variables or a secret manager.
- **Dependency hygiene** — regularly scan and update dependencies. Pin major versions, allow minor/patch.

---

## 2. Rules by Layer

### Input Validation

| Rule | Detail |
|------|--------|
| Reject early | Validate at the API boundary — malformed input never reaches services |
| Type coercion | Always coerce and validate types; never trust string input |
| Length limits | Max lengths on all string fields (title, description, name, email) |
| Character allowlists | Prefer allowlist over denylist for special characters |
| SQL injection | Parameterized queries only, no string concatenation |
| XSS | Sanitize output, not input — encode on render, not on store |

### Authentication & Authorization

| Rule | Detail |
|------|--------|
| Auth on every endpoint | No unauthenticated endpoints except explicitly whitelisted (login, signup, health) |
| Role checks | Every mutation checks the caller's role; default-deny |
| Token expiry | Access tokens: 15 min max. Refresh tokens: 7 days with rotation |
| Rate limiting | Per-user, per-IP, per-endpoint tiers. Login: aggressive. Read: moderate |
| Session invalidation | Password change, logout, or suspicious activity invalidates all sessions |

### Data Storage

| Rule | Detail |
|------|--------|
| Encryption at rest | PII, credentials, tokens encrypted at rest (AES-256) |
| Encryption in transit | TLS 1.2+ for all external communication |
| Secrets | Use a vault/secret manager (Vault, AWS Secrets Manager, env vars with `.env` in `.gitignore`) |
| Audit log | All mutations of sensitive data logged: who, what, when, from where |

### Dependencies

| Rule | Detail |
|------|--------|
| Regular audit | `npm audit` / `pip-audit` / `cargo audit` / equivalent runs in CI |
| No unmaintained deps | Check for abandonment before adding any dependency |
| Lockfile | Commit lockfile; pin major versions |

---

## 3. Common Vulnerabilities (OWASP Top 10)

| # | Vulnerability | Mitigation |
|---|---------------|------------|
| 1 | Broken access control | Role/permission check on every endpoint |
| 2 | Cryptographic failures | Use modern algorithms (AES-256, bcrypt/argon2); no homegrown crypto |
| 3 | Injection | Parameterized queries, ORM, input sanitization; no eval() |
| 4 | Insecure design | Threat modeling at design phase; rate limiting, quota enforcement |
| 5 | Security misconfiguration | Minimal surface; remove debug endpoints; secure defaults |
| 6 | Vulnerable components | Dependency audit in CI; update policy (CVSS > 7 = 7 days) |
| 7 | Auth failures | MFA support; account lockout after N failures; no weak passwords |
| 8 | Data integrity failures | Signed tokens (JWT), CSP headers for web |
| 9 | Logging failures | Structured logging; no secrets in logs; monitoring alert on anomaly |
| 10 | SSRF | Allowlist outbound destinations; validate redirects |

---

## 4. Secret Management

```bash
# Never commit these files
.env
*.key
*.pem
service-account.json
credentials.json
secrets.*
```

- Use environment variables at runtime
- Use a vault for secrets at rest (HashiCorp Vault, AWS Secrets Manager)
- For local dev: `.env` file (gitignored), loaded by the application
- Rotate secrets on a schedule; always rotate on suspected leak

---

## 5. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Auth logic, token validation, role checks | Language test framework | `npm test` | Any failure |
| Integration | Endpoint auth bypass attempts | Supertest / pytest client | `npm run test:integration` | Any unauthorized request succeeds |
| SAST | Static analysis for vulnerabilities | SonarQube / CodeQL / Semgrep | `semgrep --config=auto .` | Any finding |
| Dependency | Known vulnerabilities in deps | `npm audit` / `pip-audit` | `npm audit` | High/critical severity found |
| Secret scan | Committed secrets | truffleHog / git-secrets | `trufflehog filesystem .` | Any secret found |

### Self-Validation

```bash
npm audit && semgrep --config=auto . && trufflehog filesystem --no-verification .
```

Expected: No high/critical vulnerabilities, no SAST findings, no secrets.
