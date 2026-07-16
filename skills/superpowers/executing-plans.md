---
type: Agent Skill
title: executing-plans
description: "A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow."
resource: "https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-07-16T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow.

# When to use

A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/executing-plans/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/executing-plans/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts. Following a plan can edit code, run project commands, and change Git state, so it stops on missing context, unclear instructions, or repeated verification failure.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [executing-plans source](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md)
