# Quality Gates

## Principle
**No implementation spec is complete without a Testing & Validation section.**

Every implementation spec must document:
- **What** must be tested (units, integrations, side effects)
- **How** each layer is validated (tool, command, framework)
- **How to self-validate** — exact command(s) to confirm correctness
- **Failure criteria** — what constitutes failure

Until all validation paths pass, the spec is **incomplete / in progress**.

## Validation by Code Type

### API / Service Layer
| Layer | Requirement | Tooling |
|-------|-------------|---------|
| Unit | Handler/service logic in isolation | pytest / JUnit / Jest |
| Integration | Real DB, network, or file system | Testcontainers / Docker Compose |
| Contract | Request/response schema validation | OpenAPI / Zod / Pydantic |
| E2E | Full endpoint testing | Postman / Newman / Supertest |

### UI / Screen Layer
| Layer | Requirement | Tooling |
|-------|-------------|---------|
| Unit | State mutations, reducer logic | Jest / JUnit / XCTest |
| Widget | Render + interaction | Flutter test / Compose test |
| Integration | Screen flows, navigation | Detox / Cypress / XCUITest |

### Data Layer
| Layer | Requirement | Tooling |
|-------|-------------|---------|
| Migration | Schema changes up and down | Flyway / Alembic / Prisma |
| Seed | Test data idempotent | Custom seed script |
| Query | Performance, correctness | Query analyzer / EXPLAIN |

## Definition of Done
- [ ] All tests pass (unit + integration + e2e)
- [ ] Code coverage ≥ 80% (threshold per module)
- [ ] Lint passes with zero warnings
- [ ] Type check passes
- [ ] No secrets or credentials in code
- [ ] Accessibility checked against WCAG 2.1 AA
- [ ] Error paths tested (not just happy path)
- [ ] Documentation updated
