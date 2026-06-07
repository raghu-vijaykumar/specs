# PII Handling

Rules for identifying, storing, displaying, logging, and deleting personally identifiable information.

---

## 1. What Counts as PII

| Category | Examples |
|----------|----------|
| Identity | Name, email, phone, address, government ID (SSN, passport, driver's license) |
| Biometric | Faceprint, fingerprint, voiceprint |
| Financial | Credit card number, bank account, income, credit score |
| Health | Medical records, insurance ID, genetic data |
| Digital | IP address, device ID, precise location, cookies/identifiers used for tracking |
| Behavioral | Browsing history, purchase history, app usage patterns (if tied to an identifier) |

---

## 2. Rules

### Storage

- **Encrypt at rest** — all PII fields encrypted with AES-256
- **Minimize** — store only what the feature needs; no "collect everything" patterns
- **Separate** — PII in a separate table/collection from operational data where possible
- **Retention limit** — every PII field has a TTL or explicit deletion trigger (account deletion, legal expiry)
- **No raw PII in logs** — log a correlation ID, not the data itself

### Display

- **Mask by default** — `ra***@example.com`, `****-****-****-1234`
- **Full reveal** — only on explicit user action (tap "show") and session-authenticated
- **Never in URLs** — PII goes in request body or headers, never query params
- **Never in titles/notifications** — push notifications reference content, not the data

### API / Transfer

- **TLS 1.2+** — all PII in transit
- **No PII in response bodies** unless the endpoint is explicitly for that data
- **Audit log** — every PII read/mutation logged (who, when, what field)
- **Third-party** — PII sent to third parties requires explicit user consent per service

### Deletion

- **Right to delete** — expose a `DELETE /user/data` endpoint that clears all PII within 30 days
- **Soft delete** — mark deleted_at; hard purge after retention period
- **Cascade** — deleting a user deletes or anonymizes all associated PII

---

## 3. Data Flow Checklist

When adding a new feature that touches PII:

- [ ] Is this field really necessary? Can we use a pseudonymized ID instead?
- [ ] Is the field encrypted at rest?
- [ ] Is the field masked in UI by default?
- [ ] Is the field excluded from logs?
- [ ] Is the field excluded from API responses unless explicitly requested?
- [ ] Does the field have a retention/deletion policy?
- [ ] Is the field covered by the audit log?

---

## 4. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | PII masking, encryption/decryption, retention logic | Language test framework | `npm test` | Any failure |
| Integration | API responses do not leak PII in non-PII endpoints | Supertest / pytest | `npm run test:integration` | Any PII in unexpected response |
| Audit | Logs are scanned for PII patterns | Custom regex / grepp | `rg "(email\|ssn\|credit.card)" logs/` | Any match |
| E2E | Account deletion cascades to all PII | E2E test suite | `npm run test:e2e` | Deleted PII still accessible |

### Self-Validation

```bash
npm test && npm run test:integration && rg "(email|ssn|credit.card)" logs/ 2>/dev/null || echo "No PII in logs"
```
