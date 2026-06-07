# Data Modeling

Conventions for database schemas, entities, and migrations.

---

## 1. Principles

- **Audit trail** — every record knows when it was created, updated, and (optionally) deleted
- **Soft delete** — destructive operations are reversible via soft delete
- **Immutable history** — mutations append; they don't destroy the prior state (event sourcing where critical)
- **Naming consistency** — predictable names make the schema self-documenting

---

## 2. Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Tables | snake_case, plural | `users`, `order_items` |
| Columns | snake_case, singular | `first_name`, `created_at` |
| Primary key | `id` (UUID preferred over auto-increment) | `id UUID PRIMARY KEY` |
| Foreign key | `{table}_id` | `user_id`, `order_id` |
| Join tables | `{table1}_{table2}` | `users_roles` |
| Indexes | `idx_{table}_{column}` | `idx_users_email` |
| Unique constraints | `uq_{table}_{column}` | `uq_users_email` |

---

## 3. Required Audit Fields

Every table MUST include:

```sql
id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
updated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
deleted_at    TIMESTAMPTZ  -- NULL = active, set = soft-deleted
```

- `created_at` — set once on insert, never modified
- `updated_at` — updated on every mutation (use a trigger or ORM hook)
- `deleted_at` — NULL = active; filter with `WHERE deleted_at IS NULL` in all queries unless explicitly querying deleted

---

## 4. Migrations

| Rule | Detail |
|------|--------|
| One direction | Forwards only. Backward compatibility handled by code, not rollback migration |
| Idempotent | `UP` migration should be safe to run twice (`IF NOT EXISTS`) |
| Small steps | One logical change per migration file |
| Naming | `{timestamp}_{description}.sql` — sorted by time, self-documenting |
| Review | All migrations reviewed like code; no `ALTER` in production without review |

### Migration File Template

```sql
-- migration/20260101_add_stripe_customer_id_to_users.sql

ALTER TABLE users
  ADD COLUMN IF NOT EXISTS stripe_customer_id VARCHAR(255);
CREATE INDEX IF NOT EXISTS idx_users_stripe_customer_id ON users(stripe_customer_id);
```

---

## 5. Indexing Strategy

| Index type | When | Example |
|------------|------|---------|
| Primary key | Every table | `PRIMARY KEY (id)` |
| Foreign key | Every FK column | `INDEX (user_id)` |
| Unique | Every natural unique constraint | `UNIQUE (email)` WHERE `deleted_at IS NULL` |
| Composite | Multi-column query patterns | `INDEX (status, created_at)` |
| Partial | Filtered queries on large tables | `INDEX ON users(email) WHERE deleted_at IS NULL` |

---

## 6. Type Conventions

| Concept | Type | Notes |
|---------|------|-------|
| IDs | UUID | v4, generated at application level |
| Timestamps | `TIMESTAMPTZ` | Always with timezone |
| Money | `DECIMAL(12,2)` or integer cents | Integer avoids floating-point errors |
| Status | `VARCHAR(32)` or ENUM | ENUM if fixed set; VARCHAR if extensible |
| Text | `VARCHAR(255)` for short, `TEXT` for long | Always with max length |
| JSON | `JSONB` | Only for unstructured/schema-less data |
| Booleans | `BOOLEAN` | Never integer 0/1 |

---

## 7. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Model validation, constraints, serialization | Language test framework | `npm test` | Any failure |
| Migration | Up migration runs cleanly forward | Testcontainers / Docker | `npm run test:migrations` | Migration error |
| Integration | CRUD operations on real DB | Testcontainers / Docker | `npm run test:integration` | Any query failure |
| Schema | Generated schema matches spec | Prisma / TypeORM / SQLX check | `npm run schema:check` | Drift from spec |

### Self-Validation

```bash
npm run test:migrations && npm test && npm run schema:check
```
