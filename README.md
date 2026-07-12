# App Specs

Framework-agnostic design and architecture specs — reusable as a starting point for any project. Packaged as AI-agent skills for use with Claude Code, Codex, OpenCode, and other coding agents.

## Quick Install

```bash
# Universal (works with 70+ agents)
npx skills add <your-repo-url>

# Or install natively (see docs below)
```

## Native Setup

| Agent | Command / Setup | Docs |
|-------|-----------------|------|
| **Claude Code** | `/plugin marketplace add <repo-url>` | [`docs/claude-setup.md`](docs/claude-setup.md) |
| **OpenAI Codex** | `codex plugin marketplace add <repo-url>` | [`docs/codex-setup.md`](docs/codex-setup.md) |
| **OpenCode** | Clone repo + `AGENTS.md` auto-discovery | [`docs/opencode-setup.md`](docs/opencode-setup.md) |

## All 30 Skills

### Define — Clarify what to build
| Skill | Description |
|-------|-------------|
| [`spec-driven-development`](skills/spec-driven-development/SKILL.md) | Write a PRD covering objectives, commands, structure, code style, testing, and boundaries before any code |
| [`idea-refine`](skills/idea-refine/SKILL.md) | Structured divergent/convergent thinking to turn vague ideas into concrete proposals |
| [`interview-me`](skills/interview-me/SKILL.md) | One-question-at-a-time interview to extract requirements |

### Plan — Break it down
| Skill | Description |
|-------|-------------|
| [`planning-and-task-breakdown`](skills/planning-and-task-breakdown/SKILL.md) | Decompose specs into small, verifiable tasks with acceptance criteria |

### Build — Write the code
| Skill | Description |
|-------|-------------|
| [`incremental-implementation`](skills/incremental-implementation/SKILL.md) | Thin vertical slices: implement, test, verify, commit |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Red-Green-Refactor, test pyramid, DAMP over DRY |
| [`context-engineering`](skills/context-engineering/SKILL.md) | Feed agents the right information at the right time |
| [`source-driven-development`](skills/source-driven-development/SKILL.md) | Ground every framework decision in official documentation |
| [`doubt-driven-development`](skills/doubt-driven-development/SKILL.md) | Adversarial fresh-context review of non-trivial decisions |
| [`frontend-ui-engineering`](skills/frontend-ui-engineering/SKILL.md) | Component architecture, design systems, state management, WCAG 2.1 AA |
| [`api-and-interface-design`](skills/api-and-interface-design/SKILL.md) | Contract-first design, error semantics, boundary validation |
| [`code-design`](skills/code-design/SKILL.md) | Design deep, modular architecture; small interfaces, focused implementations, clean seams |
| [`improve-codebase-architecture`](skills/improve-codebase-architecture/SKILL.md) | Scan for architectural friction, surface deepening opportunities, and report them before drilling into one candidate |

### Verify — Prove it works
| Skill | Description |
|-------|-------------|
| [`browser-testing-with-devtools`](skills/browser-testing-with-devtools/SKILL.md) | Chrome DevTools MCP for live runtime data |
| [`debugging-and-error-recovery`](skills/debugging-and-error-recovery/SKILL.md) | Five-step triage: reproduce, localize, reduce, fix, guard |

### Review — Quality gates before merge
| Skill | Description |
|-------|-------------|
| [`code-review-and-quality`](skills/code-review-and-quality/SKILL.md) | Five-axis review, change sizing, severity labels |
| [`code-simplification`](skills/code-simplification/SKILL.md) | Chesterton's Fence, Rule of 500, complexity reduction |
| [`security-and-hardening`](skills/security-and-hardening/SKILL.md) | OWASP Top 10 prevention, auth patterns, dependency auditing |
| [`performance-optimization`](skills/performance-optimization/SKILL.md) | Measure-first approach, Core Web Vitals, profiling |
| [`codebase-review`](skills/codebase-review/SKILL.md) | Audit existing codebases for modular design violations (oversized modules, duplication, layer mixing) and drive fixes |

### Ship — Deploy with confidence
| Skill | Description |
|-------|-------------|
| [`git-workflow-and-versioning`](skills/git-workflow-and-versioning/SKILL.md) | Trunk-based development, atomic commits |
| [`ci-cd-and-automation`](skills/ci-cd-and-automation/SKILL.md) | Shift Left, feature flags, quality gate pipelines |
| [`deprecation-and-migration`](skills/deprecation-and-migration/SKILL.md) | Code-as-liability mindset, migration patterns |
| [`documentation-and-adrs`](skills/documentation-and-adrs/SKILL.md) | Architecture Decision Records, API docs |
| [`observability-and-instrumentation`](skills/observability-and-instrumentation/SKILL.md) | Structured logging, RED metrics, OpenTelemetry |
| [`shipping-and-launch`](skills/shipping-and-launch/SKILL.md) | Pre-launch checklists, staged rollouts, rollback procedures |

### Custom
| Skill | Description |
|-------|-------------|
| [`code-review`](skills/code-review/SKILL.md) | Multi-aspect code review with 8 parallel subagents |
| [`draw-io`](skills/draw-io/SKILL.md) | Diagram creation: layout, colors, connectors, 7 template types, validation |
| [`manim`](skills/manim/SKILL.md) | Animation creation: 7 scene templates, pacing, styling, validation |
| [`opensrc`](skills/opensrc/SKILL.md) | Fetch dependency source code for deeper implementation context |

### Meta
| Skill | Description |
|-------|-------------|
| [`using-agent-skills`](skills/using-agent-skills/SKILL.md) | Maps incoming work to the right skill workflow, defines shared operating rules |

## Agent Personas

| Agent | Role | Perspective |
|-------|------|-------------|
| [`code-reviewer`](agents/code-reviewer.md) | Senior Staff Engineer | Five-axis code review |
| [`test-engineer`](agents/test-engineer.md) | QA Specialist | Test strategy, coverage analysis |
| [`security-auditor`](agents/security-auditor.md) | Security Engineer | Vulnerability detection, OWASP |
| [`web-performance-auditor`](agents/web-performance-auditor.md) | Web Performance Engineer | Core Web Vitals audit |

## References

Quick-reference material in [`references/`](references/):

| Reference | Covers |
|-----------|--------|
| [`constitution.md`](references/constitution.md) | Design principles and governance |
| [`accessibility-checklist.md`](references/accessibility-checklist.md) | WCAG 2.1 AA checklist with patterns and testing tools |
| [`security-checklist.md`](references/security-checklist.md) | Pre-commit checks, auth, input validation, OWASP Top 10 |
| [`performance-checklist.md`](references/performance-checklist.md) | Core Web Vitals targets, frontend/backend checklists |
| [`quality-gates.md`](references/quality-gates.md) | Testing and validation requirements |
| [`definition-of-done.md`](references/definition-of-done.md) | Project-wide standing bar every change must clear |
| [`testing-patterns.md`](references/testing-patterns.md) | Test structure, naming, mocking, anti-patterns |
| [`observability-checklist.md`](references/observability-checklist.md) | Structured logging, RED metrics, alerting, pre-launch gate |
| [`orchestration-patterns.md`](references/orchestration-patterns.md) | Multi-persona orchestration patterns and anti-patterns |
| [`design-tokens.md`](references/design-tokens.md) | Color, spacing, radius, animation tokens |
| [`accessibility-standards.md`](references/accessibility-standards.md) | WCAG compliance reference |
| [`security-guidelines.md`](references/security-guidelines.md) | Security patterns and OWASP reference |

## Specs

Full component and architecture specs in [`specs/`](specs/):

### Mobile UI Components
| Category | Components |
|----------|------------|
| Bottom Sheets | Standard, modal, expandable, floating action row |
| Buttons | Primary, secondary, ghost, icon, FAB, link |
| Cards | Elevated, flat, tappable, action, media, row |
| Dialogs | Alert, confirm, input, full-screen |
| Feedback | Snackbar, spinner, skeleton, empty/error state, badge, progress |
| Icons | 18 custom icon designs |
| Inputs | Text field, search, toggle, segmented control, slider, checkbox, radio |
| Lists | Simple, grouped, swipeable, avatar, chip, divider |
| Media | Image viewer, gallery grid, video player |
| Navigation | Bottom nav, top tabs, floating indicator/icons |
| Pickers | Date picker, time picker, bottom sheet picker |
| Schema Upgrades | In-app DB migrations |
| Stepper | Numbered, dot (compact), side (vertical) |
| Themes | Design philosophy behind tokens |
| Typography | 9-level type scale, font family, text scaling |
| Localization | i18n: string extraction, locale fallback, RTL, dynamic sizing |

### Cross-Cutting (General)
Architecture, doc-sync, legal, quality-gates, security, PII handling, API design, data modeling, state management, observability, performance, CI/CD, migrations, error handling, accessibility, system flows, and design tokens.

## Key Concepts

- **Token-based design** — All specs reference `{token.*}` values from `tokens.md`; change one file and everything updates.
- **Three-mode system** — System (follows device), Light, Dark.
- **Animation-native** — Every component has built-in entrance animation + press micro-interaction.
- **Accessibility-first** — Min 48×48px tap targets, roles/labels in every spec.
- **AI agent ready** — Skills auto-discover for Claude Code, Codex, OpenCode.

## Project Structure

```
.
├── skills/                # 30 AI agent skills
│   ├── spec-driven-development/
│   ├── incremental-implementation/
│   ├── test-driven-development/
│   └── ...
├── agents/                # 4 specialist agent personas
├── references/            # 12 quick-reference checklists
├── specs/                 # Full design & architecture specs
│   ├── mobile/            # Mobile UI component specs
│   └── general/           # Cross-cutting specs
├── hooks/                 # Session lifecycle hooks
├── docs/                  # Setup guides per agent
├── .codex-plugin/         # Codex plugin manifest
├── .claude-plugin/        # Claude plugin manifest
├── opencode.json          # OpenCode project config (MCP servers)
├── .codex/                # Codex project config (MCP servers)
├── AGENTS.md              # OpenCode agent instructions
├── CLAUDE.md              # Claude Code project instructions
└── plugin.json            # Antigravity plugin manifest
```

## Usage

1. Copy the `specs/` folder into your new project
2. Adapt `tokens.md` to your brand colors, spacing, and radii
3. Delete unused component specs
4. Use the included skills via your preferred AI agent

## MCP Servers

This project includes pre-configured MCP servers for both [OpenCode](opencode.json) and [Codex](.codex/config.toml):

| Server | Type | Purpose | Auth |
|--------|------|---------|------|
| **GitHub** | Remote | Issues, PRs, code search | OAuth |
| **Filesystem** | Local (npx) | Read/write workspace files | None |
| **Brave Search** | Local (npx) | Web search | `BRAVE_API_KEY` env var |
| **opensrc** | Local (MCP) | Fetch dependency source code | `npm install -g opensrc` |

See [`docs/mcp-setup.md`](docs/mcp-setup.md) and [`docs/opensrc-setup.md`](docs/opensrc-setup.md) for setup instructions.
