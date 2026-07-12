# Antigravity Setup

This repository supports Antigravity via the root `plugin.json` manifest and `skills/` directory.

## Installation

1. Clone the repo:
```bash
git clone <your-repo-url>
cd specs
```

2. Install Antigravity from the local repository according to your Antigravity CLI or workspace setup.

3. Verify that Antigravity recognizes the repo's root `plugin.json` manifest.

## How It Works

- `plugin.json` is the Antigravity plugin manifest.
- `skills/` contains the skill definitions consumed by Antigravity.
- `agents/` contains any agent personas or subagents that the plugin can expose.

## Personal Skill Installation

Antigravity-compatible tools often support a home-directory skills folder under `~/.agents/skills/`.

To install all repo skills personally:

```powershell
cd /workspace/code/specs
python -c "from pathlib import Path; import shutil; repo=Path('skills'); personal=Path.home()/'.agents'/'skills'; personal.mkdir(parents=True, exist_ok=True); 
for src in sorted(repo.iterdir()):
    if src.is_dir():
        dst = personal / src.name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
print('Installed', sum(1 for _ in personal.iterdir()), 'skills to', personal)"
```

Verify the installed skills:

```powershell
Get-ChildItem $HOME\.agents\skills -Directory | Select-Object -ExpandProperty Name
```

## Notes

- Keep `.github/copilot-instructions.md` for repository-specific guidance in GitHub Copilot.
- Use `~/.agents/skills/` for personal skills that should be available across local repositories.
- If Antigravity has a marketplace or plugin registry, register the repo via its recommended mechanism.
