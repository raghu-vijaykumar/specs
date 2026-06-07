# Documentation & Design Sync

A process spec for keeping code, documentation comments, and design documents in sync automatically. Designed for AI-assisted development — the AI agent follows these rules without being prompted.

---

## 1. Purpose

Every project has three artifacts that must stay consistent:

```
Design Docs (intent, why)
     ↕  sync
Code (implementation, how)
     ↕  sync
Doc Comments (API reference, usage)
```

When any one changes, the other two update. No manual prompting required.

---

## 2. Documentation Generation

### Per-Language Rules

| Language | Doc Format | Validator | Coverage Target |
|----------|-----------|-----------|-----------------|
| Java | JavaDocs (`/** ... */`) | Checkstyle (JavadocStyle + JavadocMethod) | All public classes, methods, fields |
| Dart | DartDoc (`///`) | `dart doc` + linter rules | All public API |
| Python | Docstrings (`""" ... """`) | pydocstyle, ruff | All public modules, classes, functions |
| TypeScript | JSDoc (`/** ... */`) | ESLint `jsdoc` plugin | All exported declarations |
| Kotlin | KDoc (`/** ... */`) | detekt, diktat | All public API |
| Swift | Markdown comments (`///`) | SwiftLint | All public API |
| Go | Doc comments (`// FunctionName`) | `go vet`, `golint` | All exported names |

### What Every Doc Comment Must Include

```
1. What — what this class/function does (one-line summary)
2. Why — why it exists (when was it added, what problem it solves)
3. Parameters — @param for each (Java), [param] (Dart), :param (Python)
4. Returns — @return / Returns:
5. Throws — @throws / Throws: for unchecked exceptions
6. Example — @example or ```code block``` for non-trivial usage
```

### Doc Comment Template (language-agnostic)

```
/// [Brief one-line description]
///
/// [Extended description — why this exists, edge cases, constraints.]
///
/// [param] name — description
/// [returns] description
/// [throws] ErrorType — when it happens
///
/// [example]
/// ```code
/// usage example
/// ```
```

### When to Write Docs
- **New code**: docs are written at the same time as the code
- **Modified code**: if the signature or behavior changes, docs update
- **No doc changes needed**: refactors that don't change public API surface

---

## 3. Design Doc Structure

### Folder

Every project has a `design/` folder at the root:

```
design/
  README.md                  # Index / table of contents
  architecture.md            # Overall system design
  data-model.md              # Database schema, entities
  api-design.md              # API contracts, endpoints
  ui-component-map.md        # How UI specs map to code files
  decisions.md               # Architecture Decision Records (ADRs)
  source-map.md              # Maps design sections → source files
```

### Source Map (`design/source-map.md`)

The source map is the bidirectional link between design and code:

```markdown
# Source Map

## Architecture
| Design Section | Source Location |
|---------------|-----------------|
| Auth flow | `lib/features/auth/` |
| Payment processing | `lib/features/checkout/` |
| Offline queue | `lib/shared/services/offline_queue.dart` |

## Data Model
| Entity | Class | File |
|--------|-------|------|
| User | `User` | `lib/shared/models/user.dart` |
| Order | `Order` | `lib/shared/models/order.dart` |

## API
| Endpoint | Handler | File |
|----------|---------|------|
| `POST /auth/login` | `LoginHandler` | `lib/features/auth/api/login_handler.dart` |
| `GET /products` | `ProductListHandler` | `lib/features/products/api/product_list_handler.dart` |
```

### When the Source Map Updates
- **New file added** → add entry to source map
- **File renamed/moved** → update source map entry
- **Class renamed** → update source map entry
- **Design section changes** → flag all mapped source files as needing review

---

## 4. Bidirectional Sync Rules

### Rule 1: Code Change → Design Doc Check
When a public API changes (new class, new method, signature change):

1. Check if any `design/` file references this class/function
2. If yes, update the design doc to match the new behavior
3. If no, evaluate whether a design doc entry should be added
4. Always update the source map if file locations changed

### Rule 2: Design Doc Change → Code Flag
When a design doc is modified:

1. Scan the source map for affected files
2. For each affected file, check if the code still matches the design
3. If mismatch: add a `// TODO(doc-sync): update to match design v2` comment
4. If the design introduces new entities/endpoints: create stub files with doc comments

### Rule 3: New Feature → All Three
When a new feature is added:

1. **Check for existing design doc** covering this feature (search `design/` for relevant sections)
2. **If found**: update the existing design doc section to reflect any changes
3. **If not found**: create a new design doc file `design/features/<feature-name>.md` covering:
   - **Purpose** — what this feature does and why
   - **Entities** — new data models, classes, or types
   - **API surface** — public functions, endpoints, events
   - **Dependencies** — what existing systems it touches
   - **Source map** — which files implement it
4. Add source map entries linking new files to the new design doc
5. Implement code with doc comments
6. Verify docs compile (dart doc, javadoc, etc.)

### Rule 4: New Source Files Without Design Mapping
When new source files are created (not part of an existing feature):

1. Scan all files in the change set
2. For each file, check `design/source-map.md` to see if it's mapped to any design section
3. **If mapped**: follow Rule 1 or Rule 3 depending on scope
4. **If unmapped**: the code represents functionality not yet documented at the design level
   - Infer the feature boundary: group unmapped files by their purpose
   - Create `design/features/<inferred-feature-name>.md` documenting:
     - What the code does
     - Why it exists (inferred from usage, imports, naming)
     - Key classes and their roles
     - How it connects to the rest of the system
   - Add source map entries for all new files
   - Add a note: `> **Auto-generated**: this design doc was created from unmapped source files. Review for accuracy.`
5. Run validation to confirm all new code is now documented at both the design and API level

### Rule 5: Validation Gate
Before marking any task as complete:

1. Doc comments exist on all new public API
2. Linter/checkstyle passes for doc rules
3. Source map is up to date
4. Design docs reference the new code
5. `dart doc` / `javadoc` / equivalent compiles without warnings

---

## 5. Validation

### Per-Language Validators

| Language | Doc Validator | How to Run |
|----------|-------------|------------|
| Java | Checkstyle | `mvn checkstyle:check` or `gradle checkstyleMain` |
| Dart | `dart doc` | `dart doc --validate-links .` |
| Python | pydocstyle | `pydocstyle src/` |
| TypeScript | eslint-plugin-jsdoc | `npx eslint --rule 'jsdoc/require-jsdoc: error'` |
| Kotlin | diktat | `diktatCheck` |
| Go | `go vet` | `go vet ./...` |

### Validation Rules (language-agnostic)

- **No undocumented public API**: every public class, method, field, function must have a doc comment
- **No stale docs**: if the signature changes, the doc must update
- **No broken links**: doc links to other classes/files must resolve
- **No missing params**: every parameter must have a `@param` or equivalent
- **No missing returns**: every non-void method must have `@return` or equivalent
- **No placeholder docs**: no `// TODO: write docs` or empty doc blocks

---

## 6. AI Agent Integration

### Agent Instructions (copy into AGENTS.md or .specify/constitution.md)

```
## Documentation & Design Sync

When writing or modifying code, you MUST:

1. **Write doc comments** for every new public class, method, field, or function.
   Use the correct format for the language (JavaDocs, DartDoc, JSDoc, etc.).
   See specs/doc-sync/spec.md for templates.

2. **Update existing docs** when you change a public API signature or behavior.
   Never leave a doc comment that contradicts the code.

3. **Maintain the source map** at design/source-map.md.
   - When you add a file, add it to the source map.
   - When you rename/move a file, update the source map.
   - When you add a class, check if it belongs to an existing design doc section.

4. **Check design docs** when implementing a feature.
   - If a design doc exists for what you're building, follow it.
   - If the design doc conflicts with what makes sense, flag it with a comment.
   - If no design doc exists for the feature, create one.

5. **Auto-create design docs for unmapped code**.
   - When you create source files that aren't covered by any design doc or source map entry, treat this as a new feature.
   - Infer the feature boundary from the files' purpose, naming, and imports.
   - Create `design/features/<feature-name>.md` documenting purpose, entities, API surface, and dependencies.
   - Update `design/source-map.md` with entries for all new files.
   - Add a note: `> **Auto-generated**: review for accuracy.`

6. **Run validation** before completing any task:
   - Run the language's doc validator (checkstyle, dart doc, etc.)
   - Fix all doc warnings/errors
   - Verify the source map is current
   - Confirm every new file is mapped to a design doc (either existing or newly created)

7. **Never require a prompt** for any of the above.
   This is automatic, just like writing compilable code. If you generate code, you also generate the corresponding design doc and source map entries.
```

### Project Setup Checklist

When initializing a new project with this spec:

1. Create `design/` folder with template files
2. Create `design/source-map.md` (even if empty)
3. Configure the doc validator in the build system
4. Add the Agent Instructions to AGENTS.md
5. Run the validator once to establish a clean baseline
