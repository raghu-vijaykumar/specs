# opensrc Setup

[opensrc](https://github.com/vercel-labs/opensrc) gives AI coding agents access to any package's source code. It resolves packages from registry APIs, shallow-clones at the correct version tag, and caches globally at `~/.opensrc/`.

## Install

```bash
npm install -g opensrc
```

The global install provides a native Rust binary — no Node.js overhead on each run.

## How It Works

1. Resolves the package to a git repository URL via registry APIs
2. Detects the installed version from lockfiles (npm) or uses latest
3. Shallow-clones the repo at the matching version tag
4. Caches in `~/.opensrc/repos/<host>/<owner>/<repo>/<version>/`
5. Tracks metadata in `~/.opensrc/sources.json`

## Usage

```bash
# Get path to source (fetches on cache miss)
opensrc path zod
opensrc path pypi:requests
opensrc path crates:serde
opensrc path facebook/react

# Read specific files using the path
cat $(opensrc path zod)/src/types.ts
rg "parse" $(opensrc path zod)

# Specific versions
opensrc path zod@3.22.0
opensrc path pypi:flask@3.0.0
opensrc path owner/repo#main

# Version resolution from lockfile
opensrc path zod --cwd /path/to/project

# Pre-fetch without printing path
opensrc fetch zod pypi:requests

# Cache management
opensrc list
opensrc list --json
opensrc remove zod
opensrc clean --npm
```

## Global AGENTS.md

Copy `docs/global-AGENTS.md` to your global config directory so all projects get opensrc support:

| Agent | Location |
|-------|----------|
| **OpenCode** | `~/.config/opencode/AGENTS.md` |
| **Claude Code** | `~/.claude/CLAUDE.md` (or `CLAUDE_GLOBAL.md` for v2.1.32+) |
| **Codex** | Reference in project `.codex/instructions.md` |

## Integration in This Repo

- **Skill:** `skills/opensrc/SKILL.md` — auto-discovered by OpenCode and Claude Code
- **MCP server:** `scripts/opensrc-mcp-server.mjs` — registered in `opencode.json` and `.codex/config.toml`
- **Agent instructions:** Referenced in `AGENTS.md` and `CLAUDE.md`
