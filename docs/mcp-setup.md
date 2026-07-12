# MCP Server Setup

This guide covers setting up the MCP servers configured in this repo: GitHub, Filesystem, and Brave Search.

## Prerequisites

- [Node.js](https://nodejs.org/) 20+ (for npx-based servers)
- For **OpenCode**: config is in `opencode.json` (auto-detected)
- For **Codex CLI**: config is in `.codex/config.toml` (project-scoped, auto-detected when running in this directory)

---

## Servers

### GitHub

Provides access to issues, PRs, code search, and repository management.

**Auth:** OAuth-based. On first use, both OpenCode and Codex will prompt you to authenticate via your browser.

```bash
# OpenCode: trigger auth manually
opencode mcp auth github

# Codex: trigger auth manually
codex mcp login github
```

---

### Filesystem

Provides read/write access to allowed directories on your machine.

**Allowed directories (configured):**
- `C:\workspace` — workspace root
- `C:\Users\Raghu` — user home

No auth needed — runs locally via `npx`.

---

### Brave Search

Provides web and local search capabilities.

**Setup:**
1. Get a free API key at https://brave.com/search/api/ (2,000 queries/month included)
2. Set the environment variable:

```bash
# Windows PowerShell
$env:BRAVE_API_KEY = "your-key-here"

# Or set permanently
[System.Environment]::SetEnvironmentVariable('BRAVE_API_KEY', 'your-key-here', 'User')
```

3. Update the placeholder in `opencode.json` and `.codex/config.toml` with your key, or rely on the environment variable.

---

## Verification

### OpenCode
```bash
opencode mcp list        # Show all servers and their status
opencode mcp debug github  # Test connectivity for a specific server
```

### Codex CLI
```bash
codex mcp list           # Show all servers with auth status
```

---

## Usage

Once configured, the MCP tools are automatically available to the LLM alongside built-in tools. You can reference them in prompts:

- "Search the web for latest React patterns" → uses `brave-search`
- "List open issues in this repo" → uses `github`
- "Read my notes file from ~/Documents" → uses `filesystem`
