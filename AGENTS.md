# Agent Instructions

This repository provides design and architecture specs that skills and agents can use as reference material. The specs describe UI components, design tokens, architecture patterns, and cross-cutting concerns.

## Available Skills

### Define
- `spec-driven-development` — Write a PRD covering objectives, commands, structure, code style, testing, and boundaries before any code
- `idea-refine` — Structured divergent/convergent thinking to turn vague ideas into concrete proposals
- `interview-me` — One-question-at-a-time interview to extract requirements

### Plan
- `planning-and-task-breakdown` — Decompose specs into small, verifiable tasks with acceptance criteria

### Build
- `incremental-implementation` — Thin vertical slices: implement, test, verify, commit
- `test-driven-development` — Red-Green-Refactor, test pyramid, DAMP over DRY
- `context-engineering` — Feed agents the right information at the right time
- `source-driven-development` — Ground every framework decision in official documentation
- `doubt-driven-development` — Adversarial fresh-context review of non-trivial decisions
- `frontend-ui-engineering` — Component architecture, design systems, state management, WCAG 2.1 AA
- `api-and-interface-design` — Contract-first design, error semantics, boundary validation
- `code-design` — Design deep, modular architecture; small interfaces with focused implementations at clean seams
- `improve-codebase-architecture` — Scan for architectural friction, surface deepening opportunities, and present them as an HTML report

### Verify
- `browser-testing-with-devtools` — Chrome DevTools MCP for live runtime data
- `debugging-and-error-recovery` — Five-step triage: reproduce, localize, reduce, fix, guard

### Review
- `code-review-and-quality` — Five-axis review, change sizing, severity labels
- `code-simplification` — Chesterton's Fence, Rule of 500, complexity reduction
- `security-and-hardening` — OWASP Top 10 prevention, auth patterns, dependency auditing
- `performance-optimization` — Measure-first approach, Core Web Vitals, profiling
- `codebase-review` — Audit existing codebases for modular design violations (oversized modules, duplication, layer mixing) and drive fixes

### Ship
- `git-workflow-and-versioning` — Trunk-based development, atomic commits
- `ci-cd-and-automation` — Shift Left, feature flags, quality gate pipelines
- `deprecation-and-migration` — Code-as-liability mindset, migration patterns
- `documentation-and-adrs` — Architecture Decision Records, API docs
- `observability-and-instrumentation` — Structured logging, RED metrics, OpenTelemetry
- `shipping-and-launch` — Pre-launch checklists, staged rollouts, rollback procedures

### Custom
- `code-review` (custom) — Multi-aspect code review with 8 parallel subagents (style, security, performance, error handling, testing quality, architecture, documentation, accessibility)
- `draw-io` (custom) — Diagram creation: layout, colors, connectors, 7 template types, validation
- `manim` (custom) — Animation creation: 7 scene templates, pacing, styling, validation
- `opensrc` — Fetch dependency source code to give AI agents deeper implementation context (requires `npm install -g opensrc`)

### Meta
- `using-agent-skills` — Maps incoming work to the right skill workflow, defines shared operating rules

## Agent Personas
- `code-reviewer` — Senior Staff Engineer (five-axis code review)
- `test-engineer` — QA Specialist (test strategy, coverage analysis)
- `security-auditor` — Security Engineer (vulnerability detection, OWASP)
- `web-performance-auditor` — Web Performance Engineer (Core Web Vitals audit)

## References

Quick-reference material in `references/`:
- `constitution.md` — Design principles and governance
- `accessibility-checklist.md` — WCAG 2.1 AA checklist with patterns and testing tools
- `security-checklist.md` — Pre-commit checks, auth, input validation, OWASP Top 10
- `performance-checklist.md` — Core Web Vitals targets, frontend/backend checklists
- `quality-gates.md` — Testing and validation requirements
- `definition-of-done.md` — Project-wide standing bar every change must clear
- `testing-patterns.md` — Test structure, naming, mocking, anti-patterns
- `observability-checklist.md` — Structured logging, RED metrics, alerting, pre-launch gate
- `orchestration-patterns.md` — Multi-persona orchestration patterns and anti-patterns
- `design-tokens.md` — Color, spacing, radius, animation tokens
- `accessibility-standards.md` — WCAG compliance reference
- `security-guidelines.md` — Security patterns and OWASP reference

Full component and architecture specs are in `specs/`.

## MCP Servers

This project configures MCP servers for agent use:
- `github` — Issues, PRs, code search, repository management (OAuth)
- `filesystem` — Read/write access to workspace and home directories (local)
- `brave-search` — Web and local search (requires `BRAVE_API_KEY` env var)
- `opensrc` — Fetch dependency source code path; use with Read tool to inspect library internals

## Rules

- Always check if a relevant skill exists before implementing
- If a skill applies, use it
- Reference specs for design decisions and component patterns
- Never skip verification gates defined in `references/quality-gates.md`
- When you need to understand how a library works internally, use `opensrc` skill or MCP tool to fetch and read its source code

## Default Workflow for Spec-Driven Development
- For any non-trivial task, start with `spec-driven-development` unless the request is still unclear.
- If the request is vague or underspecified, first use `interview-me` and `idea-refine`.
- Once a spec exists or is updated, automatically move to `planning-and-task-breakdown`.
- Once planning is available, automatically use `context-engineering` and `incremental-implementation`.
- For any behavioral change, bug fix, or logic work, automatically include `test-driven-development`.
- For UI or browser-facing work, include `browser-testing-with-devtools`.
- Before merge or handoff, run `code-review-and-quality` and add specialist review skills only when the task domain requires them.
