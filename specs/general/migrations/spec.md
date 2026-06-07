# Migrations

Deprecation strategy, backward compatibility, phased rollout, and A/B testing conventions.

---

## 1. Principles

- **Backward compatible by default** — old clients, old data, and old config must continue to work during the migration
- **Phased rollout** — every migration has a ramp-up period; zero-day cutovers are exceptional
- **Measurable** — each phase has a success metric; roll back if the metric doesn't improve
- **Deprecation window** — old behavior is announced, documented, and removed on a published schedule

---

## 2. Deprecation Strategy

| Phase | Action | Duration |
|-------|--------|----------|
| Announce | Log deprecation warning, document in changelog | Start of deprecation |
| Soft deprecate | New behavior available behind flag; old still works | 30 days |
| Hard deprecate | Old behavior off by default; flag to re-enable | 60 days |
| Remove | Old code removed; flag removed | 90 days (or next major) |

### Deprecation Header (API)

```
Sunset: Sat, 05 Sep 2026 00:00:00 GMT
Deprecation: true
```

---

## 3. Phased Rollout Template

```markdown
## Rollout Plan: {Feature Name}

**Owner**: {name}
**Target date**: {date}

### Phase 1 — Internal (0% → 5%)
- Enable for internal team only
- Validate: {metric} improved / no regression
- Duration: 2 days

### Phase 2 — Beta (5% → 20%)
- Random user sampling
- Validate: {metric} + manual monitoring dashboards
- Duration: 5 days

### Phase 3 — Gradual (20% → 100%)
- Increase by 20% per day
- Validate: {metric} + error rate < baseline
- Duration: 4 days

### Phase 4 — Full (100%)
- Feature flag removed
- Old codepath deleted
- Monitor for 7 days post-removal

### Rollback Trigger
- Error rate increases by > 2x
- Core metric drops > 5%
- PagerDuty alert for {feature}
```

---

## 4. A/B Testing Template

```markdown
## A/B Test: {Experiment Name}

**Hypothesis**: {change} will improve {metric} by {expected impact}

**Variants**:
- Control: current behavior
- Treatment: new behavior

**Sample**: {%} of users, randomly assigned

**Duration**: {N} days or {N} events

**Success metric**: {metric} with p < 0.05 statistical significance

**Guardrails**: {metric A} must not regress, {metric B} must stay above threshold

**Decision**: Roll out to 100% if significant & positive. Revert if neutral or negative.
```

---

## 5. Backward Compatibility Rules

| Change | Compatible? | Notes |
|--------|-------------|-------|
| Add optional field | Yes | Default value for old clients |
| Add endpoint | Yes | No impact |
| Remove field | No | Deprecate first, remove in next major |
| Rename field | No | Keep old as alias or migrate in phases |
| Change field type | No | Add new field, migrate, remove old |
| Change API behavior | Maybe | Flag-controlled; old and new coexist |
| Drop DB column | No | Remove code references first, then column |

---

## 6. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Deprecation logic, flag evaluation | Language test framework | `npm test` | Any failure |
| Integration | Old and new code paths work alongside | Integration test | `npm run test:integration` | Either path broken |
| E2E | Client with old data on new code | E2E test with migration fixtures | `npm run test:migration` | Any failure |
| Rollback | Rollback from new state to old works | Testcontainers migration test | `npm run test:rollback` | Migration not reversible |

### Self-Validation

```bash
npm test && npm run test:migration && npm run test:rollback
```
