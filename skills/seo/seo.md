---
type: Agent Skill
title: seo
description: "Start here when an SEO request spans several disciplines or the right specialist is unclear. The skill detects the business type, routes work to installed specialists, and combines technical, content, schema, image, local, AI-search, and performance findings."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo/SKILL.md"
tags: [seo, installed]
timestamp: 2026-09-10T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Start here when an SEO request spans several disciplines or the right specialist is unclear. The skill detects the business type, routes work to installed specialists, and combines technical, content, schema, image, local, AI-search, and performance findings.

# When to use

Start here when an SEO request spans several disciplines or the right specialist is unclear. The skill detects the business type, routes work to installed specialists, and combines technical, content, schema, image, local, AI-search, and performance findings.

# Installed at

- `~/.claude/skills/seo/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Orchestrates shared Python scripts, local crawling, optional external APIs and MCP servers, and specialist subagents. The installed package contains a Python virtual environment; its two Playwright skill stubs are excluded from discovery and counting.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo -g -a claude-code -y --copy`
```

# Citations

[1] [seo source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
