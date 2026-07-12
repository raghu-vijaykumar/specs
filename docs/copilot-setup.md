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

## Personal Copilot Skills

You can also install these skills personally so they are available across all your local repositories.

- Personal skills live in `~/.copilot/skills/` or `~/.agents/skills/`.
- Each skill must be a directory containing a `SKILL.md` file.
- The `~/.agents/skills/` path is also the standard home-directory skill location for Antigravity and other `.agents`-compatible tools.

### Install all repo skills personally

To make the skills available across all your local repos, copy the repo's `skills/` directories into your personal skill folder.

```powershell
cd /workspace/code/specs
python -c "from pathlib import Path; import shutil; repo=Path('skills'); personal=Path.home()/'.copilot'/'skills'; personal.mkdir(parents=True, exist_ok=True);
for src in sorted(repo.iterdir()):
    if src.is_dir():
        dst = personal / src.name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
print('Installed', sum(1 for _ in personal.iterdir()), 'skills to', personal)"
```

If you want Antigravity or `.agents`-based tools to consume the same skills, install them under `~/.agents/skills/` instead.

### Verify personal installation

```powershell
Get-ChildItem $HOME\.copilot\skills -Directory | Select-Object -ExpandProperty Name
```

or for Antigravity-compatible tools:

```powershell
Get-ChildItem $HOME\.agents\skills -Directory | Select-Object -ExpandProperty Name
```

If you want to install only one skill instead of all skills, copy its folder only.

## Notes

- There is no `codex plugin marketplace add` equivalent for GitHub Copilot.
- The repo's skill definitions are documentation, not a Copilot plugin install package.
- The best experience is to keep the `.github/copilot-instructions.md` file aligned with `CLAUDE.md`, `AGENTS.md`, and the skill descriptions.
