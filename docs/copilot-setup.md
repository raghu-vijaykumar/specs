# GitHub Copilot Setup

This repository is built as a skill and guidance package for AI-assisted development. GitHub Copilot does not install skills the same way Claude Code or Codex plugins do. Instead, use a repo-level Copilot instructions file to guide Copilot with your project's conventions, rules, and available skill docs.

## Setup

1. Add a `.github/copilot-instructions.md` file in the repository root.
2. Keep the instructions concise and focused on project conventions, boundaries, and tooling.
3. Open the repo in GitHub Copilot Chat or GitHub Codespaces so Copilot can read the file and the repository contents.

## Recommended File

Create `.github/copilot-instructions.md` with project-level guidance such as:
- what the repo contains (`skills/`, `references/`, `specs/`)
- how to use this repo for AI-assisted workflows
- boundaries like no secrets, no production code assumptions, and no external environment changes
- formatting conventions for docs and examples

## Using the Repo with Copilot

- GitHub Copilot can reference `.github/copilot-instructions.md` when you ask it questions in a repository context.
- Use the `skills/` directory as source material: each skill is documented in `skills/<name>/SKILL.md`.
- If you want Copilot to follow a specific skill process, instruct it explicitly, e.g.:
  - "Use the `context-engineering` skill guidance in `skills/context-engineering/SKILL.md` to answer this question."

## Notes

- There is no `codex plugin marketplace add` equivalent for GitHub Copilot.
- The repo's skill definitions are documentation, not a Copilot plugin install package.
- The best experience is to keep the `.github/copilot-instructions.md` file aligned with `CLAUDE.md`, `AGENTS.md`, and the skill descriptions.
