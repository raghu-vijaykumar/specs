# Claude Code Instructions

This repository contains framework-agnostic design and architecture specs, plus 27 agent skills and 4 agent personas.

## Skills by Phase

**Define:** spec-driven-development, idea-refine, interview-me
**Plan:** planning-and-task-breakdown
**Build:** incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design
**Verify:** browser-testing-with-devtools, debugging-and-error-recovery
**Review:** code-review-and-quality, code-simplification, security-and-hardening, performance-optimization
**Ship:** git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, observability-and-instrumentation, shipping-and-launch
**Custom:** code-review (8-axis review), draw-io (diagrams), manim (animations), opensrc (source code fetching)
**Meta:** using-agent-skills

## Agent Personas
- `code-reviewer` — Five-axis code review
- `test-engineer` — Test strategy and coverage
- `security-auditor` — Vulnerability detection
- `web-performance-auditor` — Core Web Vitals audit

## Default Workflow for Spec-Driven Development
- For any non-trivial task, start with `spec-driven-development` unless the request is still unclear.
- If the request is vague or underspecified, first use `interview-me` and `idea-refine`.
- Once a spec exists or is updated, automatically move to `planning-and-task-breakdown`.
- Once planning is available, automatically use `context-engineering` and `incremental-implementation`.
- For any behavioral change, bug fix, or logic work, automatically include `test-driven-development`.
- For UI or browser-facing work, include `browser-testing-with-devtools`.
- Before merge or handoff, run `code-review-and-quality` and add specialist review skills only when the task domain requires them.
- New skills should be added by phase and documented in the canonical workflow, so downstream agents can auto-select them without explicit prompting.

## opensrc

Fetch dependency source code for deeper implementation context. Requires `npm install -g opensrc`.

```bash
opensrc path zod                     # get path to zod source
cat $(opensrc path zod)/src/types.ts # read a specific file
rg "parse" $(opensrc path zod)       # search within source
```

## References
- `references/constitution.md` — Design principles
- `references/accessibility-checklist.md` — WCAG 2.1 AA checklist
- `references/security-checklist.md` — Security quick reference
- `references/performance-checklist.md` — Performance quick reference
- `references/quality-gates.md` — Testing & validation requirements
- `references/definition-of-done.md` — Standing quality bar

Full specs in `specs/` for detailed component and architecture documentation.
