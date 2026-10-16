---
type: Agent Skill
title: brainstorming
description: "Creative implementation and behavior changes start with this workflow. It draws out what the user wants with open questions, plays each part back, sizes the work (just do it, agree in chat, or write a design document), and gets approval before handing off to planning."
resource: "https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-10-10T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

Creative implementation and behavior changes start with this workflow. It draws out what the user wants with open questions, plays each part back, sizes the work (just do it, agree in chat, or write a design document), and gets approval before handing off to planning.

# When to use

Creative implementation and behavior changes start with this workflow. It draws out what the user wants with open questions, plays each part back, sizes the work (just do it, agree in chat, or write a design document), and gets approval before handing off to planning.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/brainstorming/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.0/skills/brainstorming/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Bundles shell and Node scripts for an optional local visual-companion server, WebSocket helper, browser launcher, and HTML frame. It also writes design documents and dispatches a builder-check subagent (`builder-check-prompt.md`, replacing the old spec-document reviewer) that reads the design as its builder and lists open questions. v7.0.0 rebuilds the skill: it asks before proposing, sizes the work only once it understands it, asks which build choices (platform, language, libraries) the user wants to own, and offers the visual companion whenever seeing beats reading. The companion server now inserts content literally (`$'`/`$&` no longer mangled). The hard approval gate before implementation stays.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [brainstorming source](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)
