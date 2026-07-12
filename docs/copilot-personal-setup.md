# GitHub Copilot Personal Skill Setup

This repo can be used with GitHub Copilot both as a workspace-level skill package and as a personal skill library.

## Personal skill setup

GitHub Copilot supports personal skills in the home directory:

- `~/.copilot/skills/`
- `~/.agents/skills/`

Each skill should be a directory containing a `SKILL.md` file.

### Install all repo skills personally

To make the skills available across all your local repos, copy the repo's `skills/` directories into your personal Copilot skills folder:

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

### Verify personal installation

Check the personal skill directory and list installed skills:

```powershell
Get-ChildItem $HOME\.copilot\skills -Directory | Select-Object -ExpandProperty Name
```

If you want to install only one skill instead of all skills, copy its folder only.

## Project-level skill setup

For repository-specific skills, place skill directories under one of these locations in the repo:

- `.github/skills/`
- `.claude/skills/`
- `.agents/skills/`

This makes the skill available only when Copilot is working in that repository.

## Notes

- Personal skills are the correct way to share your repo skills across all local projects.
- This is the supported path for GitHub Copilot cloud agent skill discovery.
- Copying files into the internal VS Code Copilot extension folder is not supported and may break on updates.
- Keep `.github/copilot-instructions.md` in each repo for project-specific guidance.
