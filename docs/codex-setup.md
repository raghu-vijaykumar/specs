# Codex Setup

This guide explains how to use this spec repository with OpenAI Codex CLI (v0.122+).

## Overview

This repository is a [Codex plugin](https://developers.openai.com/codex/plugins/build). The `skills/` directory is consumed by Codex through `.codex-plugin/plugin.json`.

## Install (one command)

```bash
codex plugin marketplace add <your-repo-url>
```

Or from a local clone:

```bash
codex plugin marketplace add /path/to/clone
```

> Requires Codex CLI v0.122 or later.

Codex clones the repo into `~/.codex/plugins/specs/`, registers the marketplace in `~/.codex/config.toml`, and makes all skills available. Restart Codex if it's already running.

## Usage

After install, invoke a skill in Codex chat with `@`:

### Define
- `@spec-driven-development` — Write a PRD before any code
- `@idea-refine` — Turn vague ideas into concrete proposals
- `@interview-me` — One-question-at-a-time requirements interview

### Plan
- `@planning-and-task-breakdown` — Decompose specs into verifiable tasks

### Build
- `@incremental-implementation` — Thin vertical slices
- `@test-driven-development` — Red-Green-Refactor
- `@context-engineering` — Feed agents the right context
- `@source-driven-development` — Ground decisions in docs
- `@doubt-driven-development` — Adversarial review
- `@frontend-ui-engineering` — Component architecture, WCAG
- `@api-and-interface-design` — Contract-first design
- `@improve-codebase-architecture` — Surface deepening opportunities and present an HTML review

### Verify
- `@browser-testing-with-devtools` — Live runtime data
- `@debugging-and-error-recovery` — Five-step triage

### Review
- `@code-review-and-quality` — Five-axis review
- `@code-simplification` — Reduce complexity
- `@security-and-hardening` — OWASP Top 10
- `@performance-optimization` — Core Web Vitals

### Ship
- `@git-workflow-and-versioning` — Atomic commits
- `@ci-cd-and-automation` — Pipeline quality gates
- `@deprecation-and-migration` — Migration patterns
- `@documentation-and-adrs` — ADRs and API docs
- `@observability-and-instrumentation` — RED metrics
- `@shipping-and-launch` — Staged rollouts

### Custom
- `@code-review` — 8-axis review with parallel subagents
- `@draw-io` — Diagram creation
- `@manim` — Animation creation

### Meta
- `@using-agent-skills` — Discover which skill applies

## How It Works

- `.codex-plugin/plugin.json` — Codex plugin manifest pointing `skills` at `./skills/`
- `.agents/plugins/marketplace.json` — Marketplace registration entry
- `skills/<name>/SKILL.md` — Skill definitions with `name` + `description` frontmatter
- `agents/` — 4 specialist agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor)
- `references/` and `specs/` — Available as supplementary context
