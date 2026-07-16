---
type: Agent Skill
title: web-design-guidelines
description: "File-based UI, accessibility, UX, and design reviews can use this focused checker. It fetches Vercel's current Web Interface Guidelines, checks the requested files against those rules, and returns terse `file:line` findings rather than redesigning the page."
resource: "https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Frontend and UI
license: Not stated in the skill repository
available_in: Cursor and Claude Code
---

File-based UI, accessibility, UX, and design reviews can use this focused checker. It fetches Vercel's current Web Interface Guidelines, checks the requested files against those rules, and returns terse `file:line` findings rather than redesigning the page.

# When to use

File-based UI, accessibility, UX, and design reviews can use this focused checker. It fetches Vercel's current Web Interface Guidelines, checks the requested files against those rules, and returns terse `file:line` findings rather than redesigning the page.

# Installed at

- `~/.claude/skills/web-design-guidelines/SKILL.md`
- `~/.agents/skills/web-design-guidelines/SKILL.md`

# Availability

Cursor and Claude Code

# License

Not stated in the skill repository

# Trust notes

Instruction-only, but every review fetches mutable guidance from `raw.githubusercontent.com/vercel-labs/web-interface-guidelines`; review source changes if results shift.

# Install / update

```text
`npx -y skills@1.5.18 add vercel-labs/agent-skills --skill web-design-guidelines -g -a claude-code -y --copy`
```

# Citations

[1] [web-design-guidelines source](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
