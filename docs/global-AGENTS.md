# Global AGENTS.md — OpenCode / Claude Code / Codex

Copy this file to your global agent config directory:

| Agent | Location |
|-------|----------|
| **OpenCode** | `~/.config/opencode/AGENTS.md` |
| **Claude Code** | `~/.claude/CLAUDE.md` (or `CLAUDE_GLOBAL.md` for Claude Code v2.1.32+) |
| **Codex** | Instruction via `.codex/instructions.md` in each project |

---

## opensrc — Source Code Fetching

**Prerequisite:** `npm install -g opensrc`

`opensrc` fetches dependency source code so agents can read implementations, not just types. It resolves packages from registry APIs, shallow-clones at the correct version tag, and caches globally at `~/.opensrc/`.

### Usage with agents

```bash
# Get path to a package's source (fetches on cache miss)
opensrc path zod                       # npm (default)
opensrc path pypi:requests             # PyPI
opensrc path crates:serde              # crates.io
opensrc path facebook/react            # GitHub repo

# Read specific files from a package
cat $(opensrc path zod)/src/types.ts
rg "parse" $(opensrc path zod)

# Fetch source without printing path
opensrc fetch zod pypi:requests
```

### When to use opensrc

- When you need to understand internal behavior that types don't reveal
- When debugging unexpected library behavior
- When you want to learn patterns from well-known implementations
- When verifying how a function handles edge cases

Don't fetch source for simple API usage questions that docs or types can answer.

### Cache management

```bash
~/.opensrc/                   # Cache location (override: OPENSRC_HOME)
opensrc list                  # Show cached sources
opensrc remove zod            # Remove a package
opensrc clean --npm           # Clean npm packages only
```

---

## Core Rules for All Projects

1. **Always use available skills** — Check AGENTS.md for relevant skills before implementing
2. **Prefer opensrc over docs** — When you need to understand library internals, fetch source directly
3. **Never skip verification** — Run tests after changes, validate before committing
4. **Use MCP servers** when appropriate — GitHub, Filesystem, Brave Search are available
