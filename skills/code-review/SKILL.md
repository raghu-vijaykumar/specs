---
name: code-review
description: |
  Use when reviewing code changes, pull requests, or any implementation.
  Launches 8 parallel subagents — one per review aspect — then aggregates
  results into a single prioritized report.
---

# Code Review Skill

## Flow

1. Read the diff or files to review
2. Launch 8 parallel `task` subagents, each covering one aspect
3. Each subagent returns only issues found
4. Aggregate into a single review with:
   - Priority-ordered issues (P0 = blocking, P1 = should fix, P2 = nit)
   - Positives (what's done well)
   - Summary verdict (approve / changes requested with specifics)
   - Per-aspect breakdown

## Review Aspects (run in parallel)

| # | Aspect | What the subagent checks |
|---|--------|--------------------------|
| A | **Style & Conventions** | Naming, formatting, import order, language idioms, linter rules, file structure |
| B | **Security** | OWASP top 10, hardcoded secrets, injection, auth/z flaws, input validation gaps, dependency vulnerabilities |
| C | **Performance** | N+1 queries, bundle size, render loops, memory leaks, lazy loading, caching, profiling cues |
| D | **Error Handling** | Coverage of error paths, proper error types (not bare strings), user-facing messages, logging, recovery & retry |
| E | **Testing Quality** | Coverage gaps, missing test types (unit/integration/e2e), edge cases, mocking strategy, redundant tests |
| F | **Architecture & Design** | Separation of concerns, coupling, dependency direction, SOLID, patterns matching codebase conventions |
| G | **Documentation** | Doc comments on all public API, stale/misleading docs, missing param/return tags, source map truth |
| H | **Accessibility** | WCAG violations, ARIA, keyboard nav, screen reader, contrast, tap targets, reduced motion |

## Aggregated Output Format

```markdown
## Code Review Summary

**Verdict**: Changes requested

### Issues (by priority)

**P0** (2)
- Security: plaintext API key in ...
- Architecture: circular dependency between ...

**P1** (4)
- Style: mixed naming conventions in ...
- Testing: missing error-path coverage in ...

**P2** (3)
- Documentation: typo in doc comment ...

### Positives
- Error handling in PaymentService is thorough
- All public methods have doc comments
- Good separation of concerns in the checkout module

### Per-Aspect Breakdown

| Aspect | Issues | Verdict |
|--------|--------|---------|
| Style | 1 P1 | minor cleanup |
| Security | 1 P0 | blocking |
| Performance | 0 | clean |
| Error Handling | 0 | clean |
| Testing | 1 P1 | needs work |
| Architecture | 1 P0 | blocking |
| Documentation | 1 P2 | minor |
| Accessibility | 0 | clean |
```
