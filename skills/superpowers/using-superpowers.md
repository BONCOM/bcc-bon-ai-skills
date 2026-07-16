---
type: Agent Skill
title: using-superpowers
description: "This is the session-level routing rule for the library. It requires checking applicable skills before responding or acting, orders process skills before implementation guidance, and exempts dispatched task subagents so their supplied task brief remains authoritative."
resource: "https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-07-16T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

This is the session-level routing rule for the library. It requires checking applicable skills before responding or acting, orders process skills before implementation guidance, and exempts dispatched task subagents so their supplied task brief remains authoritative.

# When to use

This is the session-level routing rule for the library. It requires checking applicable skills before responding or acting, orders process skills before implementation guidance, and exempts dispatched task subagents so their supplied task brief remains authoritative.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/using-superpowers/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/using-superpowers/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only with platform reference files. The plugin's `SessionStart` hook loads Superpowers context on startup, clear, and compact events; the hook runs synchronously but adds no MCP or agent component.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [using-superpowers source](https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md)
