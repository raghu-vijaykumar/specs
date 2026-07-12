---
name: improve-codebase-architecture
description: Scan a codebase for architectural friction, surface deepening opportunities, and present them as an HTML report before drilling into one candidate. Use when modules feel shallow, tightly coupled, or hard to extend.
---

# Improve Codebase Architecture

## Overview

This skill helps you identify where a codebase is structurally painful and where a small refactor could create more leverage and locality. The goal is not to churn the codebase, but to surface a few high-value opportunities that make future work easier to reason about, test, and evolve.

Use it when a system feels hard to navigate, when bugs appear in the same area repeatedly, or when a module seems like it is doing too much while exposing too little real capability.

## When to Use

- A feature is hard to add because the relevant logic is spread across many shallow modules
- A module has a large interface but little real behaviour behind it
- A change requires touching many places to fix one issue
- Repeated logic is copied in multiple flows
- Tests are awkward because the seam is unclear or the module is too coupled
- The codebase is unfamiliar and you want a guided architecture review before refactoring

Do not use this skill for a simple bug fix, a one-off script, or a case where the existing structure is already clear and healthy.

## Core Vocabulary

Use these terms consistently:

- Module — any unit with an interface and an implementation
- Interface — what callers must know to use the module
- Implementation — the internal behaviour hidden behind the interface
- Depth — lots of real behaviour behind a small interface
- Seam — the place where behaviour can change without editing everywhere
- Leverage — one implementation reused across many callers
- Locality — change and knowledge stay concentrated in one place

## Process

### 1. Gather context first

Read any project glossary, domain notes, or ADRs before proposing architecture changes. The best architecture suggestions use the repo’s own terminology and respect prior decisions.

Use the existing context-engineering workflow to collect the right context before exploring the code.

### 2. Explore for structural friction

Look for places where the codebase shows one or more of these patterns:

- Many small modules that must be coordinated just to understand one concept
- Shallow modules that mostly pass through calls without owning real behaviour
- Logic that is repeated across multiple callers and is hard to update consistently
- Tight coupling across seams that makes tests awkward and changes risky
- Modules that are hard to test because the interface does not expose the right boundary

Treat the deletion test as a guide: if removing a module would just move complexity around, it is probably shallow; if removing it would make the codebase less coherent, it is likely earning its keep.

### 3. Present candidates as an HTML report

Create a self-contained HTML report in the system temp directory and open it for the user. Use a fresh filename such as:

- architecture-review-<timestamp>.html

The report should be visual and structured. For each candidate, include:

- Files or modules involved
- The friction in the current architecture
- A plain-English proposal for a deeper seam or module shape
- The likely benefits in terms of leverage, locality, and testability
- A before/after sketch of the architecture idea
- A recommendation strength: Strong, Worth exploring, or Speculative

End the report with a top recommendation: which candidate to tackle first and why.

### 4. Drill into one candidate

Once the user chooses a candidate, work through it with the same discipline as a real design review:

- Clarify the problem in concrete terms
- Identify the current seam and why it feels weak
- Determine what should live behind the seam versus what should stay at the caller level
- Sketch a deeper module shape, not just a rename or a wrapper
- Call out what tests would become easier once the seam is improved

If the candidate conflicts with an existing ADR, only raise it when the friction is strong enough to justify reopening the decision.

## Design Principles to Apply

Use the repo’s architecture vocabulary and principles from the existing design skills:

- Prefer a small interface with meaningful behaviour behind it
- Extract only when the same responsibility is truly repeated or shared
- Keep domain policy near the caller or feature that owns it
- Move shared operational mechanics into a deeper module when that reduces duplication
- Make the seam explicit so tests can target the right boundary

## Output Shape

The outcome of this skill should be:

1. A short summary of the architectural friction you found
2. A ranked set of candidates with the most leverage
3. A visual HTML report that the user can inspect
4. A focused follow-up plan for the candidate they choose

## Related Skills

- code-design — Use for the underlying vocabulary and module-shaping principles
- codebase-review — Use for a broader structural audit of an existing codebase
- context-engineering — Use to gather the right context before proposing changes
- debugging-and-error-recovery — Use when the friction is tied to a specific broken path or regression
