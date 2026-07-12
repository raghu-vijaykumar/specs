# OpenCode Setup

This guide explains how to use this spec repository with OpenCode.

## Overview

OpenCode uses agent-driven skill execution via `AGENTS.md` and the built-in `skill` tool. Skills are auto-discovered from the `skills/` directory.

## Installation

1. Clone the repo:
```bash
git clone <your-repo-url>
```

2. Open the project in OpenCode.

3. Ensure these files are present:
- `AGENTS.md` (root) — agent instructions
- `skills/` directory — skill definitions
- `references/` directory — reference checklists

No additional installation required.

## How It Works

### Skill Discovery
All skills live in `skills/<name>/SKILL.md`. The agent reads `AGENTS.md` to understand which skills apply.

### Available Skills
- `code-review` — Multi-aspect code review with 8 parallel subagents
- `draw-io` — Diagram creation with 7 template types
- `manim` — Animation creation with 7 scene templates
- `improve-codebase-architecture` — Architecture review that surfaces deepening opportunities as an HTML report

### References
The `references/` folder contains quick-reference material:
- `constitution.md` — Design principles and governance
- `accessibility-standards.md` — WCAG 2.1 AA checklist
- `security-guidelines.md` — Security patterns and OWASP reference
- `quality-gates.md` — Testing and validation requirements
- `design-tokens.md` — Color, spacing, radius, animation tokens

Full specs are in `specs/` for detailed component and architecture documentation.

## Usage

Just use natural language — the agent will automatically invoke relevant skills:

- "Review this code" → `code-review`
- "Create a diagram" → `draw-io`  
- "Create an animation" → `manim`

Reference material is loaded on demand when the agent needs it.

## Summary

OpenCode integration combines:
- Structured skills (`skills/`)
- Reference material (`references/`)
- Agent rules (`AGENTS.md`)
- Full specs (`specs/`)
