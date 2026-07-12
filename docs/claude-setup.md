# Claude Code Setup

This guide explains how to use this spec repository with Claude Code.

## Installation

### Plugin install (recommended)
```bash
/plugin marketplace add <your-repo-url>
/plugin install specs@<your-plugin-name>
```

If SSH keys aren't set up, use HTTPS:
```bash
/plugin marketplace add https://github.com/<user>/<repo>.git
/plugin install specs@<your-plugin-name>
```

Because this repository includes `.claude-plugin/plugin.json`, Claude Code can install it as a plugin from your repo and make the skills available across workspaces that use the same Claude environment.

### Local install
```bash
git clone <your-repo-url>
claude --plugin-dir /path/to/repo
```

## Usage

Skills auto-discover from `skills/`. Reference material in `references/` and full specs in `specs/` are available as context.

### Available Skills
- `code-review` — Multi-aspect code review with 8 parallel subagents
- `draw-io` — Diagram creation
- `manim` — Animation creation

### References
- `constitution.md` — Design principles and governance
- `accessibility-standards.md` — WCAG 2.1 AA checklist
- `security-guidelines.md` — Security patterns and OWASP reference
- `quality-gates.md` — Testing and validation requirements
- `design-tokens.md` — Color, spacing, radius, animation tokens

Full specs are in `specs/` for detailed component and architecture documentation.
