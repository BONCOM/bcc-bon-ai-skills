---
type: Agent Skill
title: dispatching-parallel-agents
description: "Two or more tasks with separate state, separate causes, and no ordering dependency can be dispatched through this skill. It assigns one isolated agent per problem with deliberately scoped context, then reconciles the independent results in the parent session."
resource: "https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-07-24T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

Two or more tasks with separate state, separate causes, and no ordering dependency can be dispatched through this skill. It assigns one isolated agent per problem with deliberately scoped context, then reconciles the independent results in the parent session.

# When to use

Two or more tasks with separate state, separate causes, and no ordering dependency can be dispatched through this skill. It assigns one isolated agent per problem with deliberately scoped context, then reconciles the independent results in the parent session.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/dispatching-parallel-agents/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.2.0/skills/dispatching-parallel-agents/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts. It can launch several subagents concurrently, so tasks must not share files, mutable services, or a working directory where simultaneous edits would conflict.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [dispatching-parallel-agents source](https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md)
