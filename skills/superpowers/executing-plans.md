---
type: Agent Skill
title: executing-plans
description: "A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow."
resource: "https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-11-03T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow.

# When to use

A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/executing-plans/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.2/skills/executing-plans/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

v6.4.1 rebuilds it as Native (inline) execution and bundles two shell helpers (`scripts/task-start`, `scripts/task-done`) that keep the SDD-style ledger and test log; it now runs the whole plan and then dispatches one whole-branch review instead of pausing every few tasks. Following a plan can edit code, run project commands, and change Git state, so it stops on missing context, unclear instructions, or repeated verification failure. v7.0.0 fixes `task-done` so a task whose passing test prints nothing is still recorded. v7.0.2: the `task-start`/`task-done` helpers and `sdd-workspace` are run by absolute path from the working tree being executed, and pick the repository through the new shared `sdd-repo` helper (the plan file's location never chooses it); the example workflow was dropped.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [executing-plans source](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md)
