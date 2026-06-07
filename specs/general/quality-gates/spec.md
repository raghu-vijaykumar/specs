# Quality Gates

A spec is not complete until it defines how its implementation will be tested and validated. This spec establishes the principle and provides templates for every code type.

---

## 1. Principle

**No spec is complete without a Testing & Validation section.**

Every implementation spec must document:

- **What** must be tested (units, integrations, side effects)
- **How** each layer is validated (tool, command, framework)
- **How to self-validate** — the exact command(s) a developer (or AI agent) runs to confirm the implementation is correct
- **Failure criteria** — what constitutes a failure (e.g., any test fails, coverage drops below threshold, lint warning)

Until all validation paths pass, the spec is considered **incomplete / in progress**.

---

## 2. Validation Requirements by Code Type

### API / Service Layer

| Layer | Requirement | Tooling |
|-------|-------------|---------|
| Unit | Handler/service logic in isolation (mocked I/O) | pytest / JUnit / Jest |
| Integration | Real DB, network, or file system | Testcontainers / Docker Compose |
| Contract | Request/response schema validation | OpenAPI validator / Zod / Pydantic |
| E2E | Full endpoint testing | Postman / Newman / Supertest |

### UI / Screen Layer

| Layer | Requirement | Tooling |
|-------|-------------|---------|
| Unit | State mutations, reducer/controller logic | Jest / JUnit / XCTest |
| Widget | Render + interaction (tap, scroll) | Flutter test / Compose test / SwiftUI preview |
| Accessibility | Labels, roles, focus order, contrast | Axe / Accessibility Scanner / VoiceOver |
| Visual | Snapshot regression (optional) | Storybook / Percy / Pixelmatch |

### Data Layer (DB, Cache, File Store)

| Layer | Requirement | Tooling |
|-------|-------------|---------|
| Unit | Query builder, migration logic | Language test framework |
| Integration | Real DB read/write with test fixtures | Testcontainers / SQLite in-memory |
| Migration | Up/down rollback round-trip | Flyway / Alembic / Room |
| Contract | Schema matches spec | Prisma / TypeORM schema check |

### Business Logic / Domain Layer

| Layer | Requirement | Tooling |
|-------|-------------|---------|
| Unit | Pure logic: calculations, transformations, validations | Language test framework |
| Integration | Composition of multiple services | Service test with real or fake collaborators |
| Property | Invariant testing (random inputs) | QuickCheck / fast-check |

---

## 3. Spec Template Section

Every implementation spec must include this section. Copy-paste the relevant table:

```markdown
## Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit   | <what the unit tests cover> | <test framework> | `npm test -- --coverage` | Any failure |
| Integration | <what integration tests cover> | <framework> | `docker compose up -d && npm run test:integration` | Any failure |
| Contract | <what contract covers> | <validator> | `npx openapi validate openapi.yaml` | Validation error |

### Self-Validation

```bash
# One-shot: run every gate
<single command that runs all of the above>

# Expected output
All tests passed. Coverage >= 80%. No lint warnings.
```
```

---

## 4. Completion Gate

Before a spec file is marked **final**:

- [ ] Testing & Validation section exists in the spec
- [ ] Every row in the section has a command that can be run headlessly
- [ ] At minimum, **unit tests** are defined for every new public function/class
- [ ] **Integration tests** are defined for any I/O boundary (API, DB, file system, network)
- [ ] All commands have been run and produce passing results
- [ ] Coverage meets or exceeds threshold defined in section
- [ ] Lint/format command passes without warnings
- [ ] Doc validator passes (see `specs/general/doc-sync/spec.md` § Validation)
- [ ] Source map is updated

---

## 5. Self-Validation of This Spec

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Audit | Every spec in repo has a Testing & Validation section | grep / shell | `specs/general/quality-gates/audit.ps1` | Any spec missing the section |

> **Note**: The audit script must be created and passing before this spec itself is considered final.
