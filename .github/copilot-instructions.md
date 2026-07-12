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
