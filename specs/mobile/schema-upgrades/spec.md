# In-App Schema Upgrades

Patterns for local database migrations when the app schema changes across versions.

---

## 1. Principles

- **Forward-only** — migrations apply in ascending order. Never roll back a migration; roll forward with a fix migration.
- **Idempotent** — every migration is safe to run twice. Use `IF NOT EXISTS`, `CREATE TABLE IF NOT EXISTS`, `ALTER TABLE ... IF NOT EXISTS`, or version checks.
- **No data loss by default** — destructive migrations (column drop, table drop) must be explicitly flagged and reviewed.
- **Version pinned in code** — the current schema version is a constant in the codebase, not inferred from the database.
- **User is never blocked permanently** — if a migration fails, the app degrades gracefully rather than crashing on launch.

---

## 2. Version Management

### Schema Version Storage

```sql
-- Stored in a metadata table
CREATE TABLE IF NOT EXISTS _schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT (datetime('now'))
);
```

| Platform | Storage Mechanism |
|----------|------------------|
| SQLite (direct) | `_schema_version` table |
| Room (Android) | `room_master_table` (auto-managed) |
| Core Data (iOS) | Model version hash in `.xcdatamodeld` |
| Realm | Schema version integer on `RealmConfiguration` |
| Hive / ObjectBox | Internal version number |
| Drift (Flutter) | `_db_version` table (auto-managed) |

### Version Constant

```dart
// lib/shared/db/schema_version.dart
const int SCHEMA_VERSION = 7;
```

- Bump on every PR that changes the schema.
- Never re-use a version number.
- The version constant is the source of truth — if it mismatches the DB, migrations run.

---

## 3. Migration Strategy

### Migration File Convention

```
lib/shared/db/migrations/
├── migration_001_create_users.sql
├── migration_002_add_email_index.sql
├── migration_003_add_profile_table.sql
├── migration_004_add_stripe_customer_id.sql
├── migration_005_rename_status_column.sql
└── migration_006_add_notifications_table.sql
```

| Pattern | Example | Rule |
|---------|---------|------|
| SQL (raw) | `migration_001_desc.sql` | One file per version |
| Flutter (Drift) | `migration_001.dart` in `onUpgrade` | Nested `onUpgrade` calls |
| Android (Room) | Auto-detected from `RoomDatabase.Callback` | `Migration(1, 2)` objects |
| iOS (Core Data) | `Mapping Model` or lightweight migration | `.xcmappingmodel` |
| Realm | `migrationBlock` on `RealmConfiguration` | Version bump + block |

### Migration Runner Pseudocode

```dart
Future<void> runMigrations(Database db, int currentVersion, int targetVersion) async {
  for (int v = currentVersion + 1; v <= targetVersion; v++) {
    await db.execute(await loadMigration(v));
    await db.execute('INSERT INTO _schema_version (version) VALUES ($v)');
  }
}
```

- Migrations run inside a transaction. If any migration fails, the entire upgrade rolls back.
- Each migration is logged to `_schema_version` *after* it succeeds.

---

## 4. Migration Types

| Type | Description | When to use |
|------|-------------|-------------|
| **Additive** | New table, column, or index. No existing data is affected. | Default. Safe, always preferred. |
| **Non-destructive modify** | Add nullable column with default, rename via add + copy + drop, change constraint with temp table | When schema shape changes but data is preserved. |
| **Seed / backfill** | Populate new column from existing data (nullable → NOT NULL after backfill) | After adding a non-nullable column. Two-step: add nullable, backfill, alter to NOT NULL. |
| **Destructive** | Drop table, drop column with data loss | Only when the data is genuinely unused or replaced. Must be reviewed. |

### Destructive Migration Rule

```markdown
## Destructive Migration Checklist

- [ ] Data being dropped is confirmed unused (grep codebase for all references)
- [ ] Data has been exported/backed up if needed
- [ ] Migration has a corresponding UI change that removes the feature
- [ ] Reviewed by at least one other developer
- [ ] Flagged in release notes
```

---

## 5. Handling Version Skips

Users may skip app versions. Migrations must handle `1 → 7` (not just `1 → 2`).

### Rules

- Migrations run sequentially from current DB version to target version. Every intermediate migration applies.
- No migration assumes a prior migration's side effects unless it depends on it.
- Test the scenario: install version 1 → upgrade directly to version 7.

```dart
// Correct: runs every migration in order
for (int v = dbVersion + 1; v <= SCHEMA_VERSION; v++) {
  await applyMigration(v);
}

// Wrong: assumes dbVersion == SCHEMA_VERSION - 1
applyMigration(SCHEMA_VERSION);  // skips intermediate migrations!
```

---

## 6. Migration Failure Recovery

### Behavior on Failure

1. Migration transaction rolls back — the database stays at the prior version.
2. The app launches with `SCHEMA_VERSION > dbVersion`, which triggers a retry.
3. User sees a non-blocking message: "Upgrading database…" with a progress indicator.
4. If migration fails persistently (3+ attempts), show error screen with "Contact support" and log the failure details.

```dart
enum MigrationResult { success, retryable, fatal }

Future<MigrationResult> attemptMigration() async {
  try {
    await runMigrations(db, currentVersion, SCHEMA_VERSION);
    return MigrationResult.success;
  } on SchemaMigrationException catch (e) {
    if (e.attempts < 3) return MigrationResult.retryable;
    logError(e);
    return MigrationResult.fatal;
  }
}
```

### Recovery Actions

| Failure Type | Recovery |
|-------------|----------|
| Syntax error in migration SQL | Fix in next release — migration failed safely (rolled back) |
| Constraint violation (duplicate row) | Migration needs `INSERT OR IGNORE` or dedup step |
| Disk full | Prompt user to free space and retry |
| Timeout (large dataset) | Run migration on background thread with progress callback |

---

## 7. Testing Migrations

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Each migration runs without error against an empty DB | Language test framework | `npm test` | Any SQL error |
| Integration | Migration from version N to version N+1 preserves data | Test with pre-seeded DB | `npm run test:migration` | Data loss or corruption |
| Skip | Migration 1 → 7 (skip intermediate) preserves data | DB seeded at version 1, run all migrations | `npm run test:migration-skip` | Data loss or corruption |
| Destructive | Confirm destructive migration drops expected data | Test with pre-seeded data + backup validation | `npm run test:migration-destructive` | Unexpected data loss |
| Concurrent | Migration does not block UI thread | Manual or integration test | Visual check | UI freeze > 1s |

### Test Fixture Pattern

```dart
void testMigration(int fromVersion, int toVersion) {
  final db = await createEmptyDb();
  // Seed with schema at fromVersion
  applyMigrationsUpTo(db, fromVersion);
  insertTestData(db);
  // Run target migration
  applyMigrations(db, fromVersion, toVersion);
  // Verify
  expect(await getSchemaVersion(db), toVersion);
  expect(await queryAllData(db), equals(expectedData));
}
```

---

## 8. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Each migration runs without error | Language test framework | `npm test` | Any SQL error |
| Integration | Data preserved across version upgrade | Test with pre-seeded DB | `npm run test:migration` | Data loss |
| Skip | Version skip (1→7) preserves data | DB seeded at v1, run all migrations | `npm run test:migration-skip` | Data loss |
| Destructive | Expected data is dropped, other data preserved | Seeded DB + migration | `npm run test:migration-destructive` | Unexpected data loss |
| Concurrent | UI stays responsive during migration | Profiling / integration test | `npm run test:migration-perf` | UI thread blocked > 1s |
| Idempotency | Re-running migration produces same result | Apply migration twice | `npm run test:migration-idempotent` | Error on second run |

### Self-Validation

```bash
npm test && npm run test:migration && npm run test:migration-skip && npm run test:migration-perf
```
