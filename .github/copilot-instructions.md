# GitHub Copilot Instructions

## Project Overview
- This repository contains reusable AI-assisted development guides, skills, and specs.
- Core content is in `skills/`, `references/`, and `specs/`.

## Guidance for Copilot
- Use `skills/<name>/SKILL.md` as the canonical description of each skill.
- Treat `references/` and `specs/` as supporting context, not executable code.
- Keep output concise, clear, and aligned with repository conventions.

## Conventions
- Use headings, bullets, and examples in Markdown.
- Reference file paths with backticks like `skills/context-engineering/SKILL.md`.
- Do not add secrets, credentials, or deployment-specific configuration.

## Boundaries
- Do not assume a production runtime or external environment unless explicitly stated.
- Do not modify files outside the repo without explicit permission.
- Do not invent a new plugin system for Copilot; use the provided docs and instructions.

## Preferred Workflow
- For process questions, reference the relevant skill doc.
- For installation or setup questions, explain that Copilot uses `.github/copilot-instructions.md` rather than a plugin install command.
- Keep recommendations aligned with the existing `README.md` and `docs/` guides.

## Auto-Injection Policy for Spec-Driven Development
- Treat `spec-driven-development` as the default entry skill for any non-trivial task that has unclear or evolving requirements.
- If the request is vague or underspecified, first use `interview-me` and `idea-refine`.
- Once a spec exists or is updated, automatically move to `planning-and-task-breakdown`.
- Once planning is available, automatically use `context-engineering` and `incremental-implementation`.
- For any behavior change, bug fix, or logic work, automatically include `test-driven-development`.
- For UI or browser-facing work, include `browser-testing-with-devtools`.
- If implementation fails or behavior is unexpected, use `debugging-and-error-recovery`.
- Before merge or handoff, run `code-review-and-quality` and add specialist review skills only when the task domain requires them.
- Add `security-and-hardening`, `performance-optimization`, `git-workflow-and-versioning`, and `documentation-and-adrs` at the appropriate stage rather than as a generic catch-all.

## How Skills Are Selected
- Treat this policy as the canonical routing logic for downstream agents.
- The agent should auto-select the next skill by task phase, not by waiting for the user to name it.
- Use `skills/using-agent-skills/SKILL.md` as the meta-skill for discovery and phase mapping.
- When adding a new skill, update this policy and the canonical phase map in `specs/AGENTS.md`, `specs/CLAUDE.md`, `docs/global-AGENTS.md`, and `skills/using-agent-skills/SKILL.md`.

## Default Skill Chain
1. `interview-me` / `idea-refine` when the request is unclear.
2. `spec-driven-development` for the initial spec.
3. `planning-and-task-breakdown` for task decomposition.
4. `context-engineering` and `incremental-implementation` for execution.
5. `test-driven-development` for behavior changes and bug fixes.
6. `browser-testing-with-devtools` for UI verification when relevant.
7. `code-review-and-quality` before merge or handoff.
