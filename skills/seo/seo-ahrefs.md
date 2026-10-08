---
type: Agent Skill
title: seo-ahrefs
description: "Ahrefs domain metrics, referring domains, backlinks, anchors, organic keywords, and Content Explorer results are the scope of this extension. It pairs paid Ahrefs evidence with `seo-backlinks` so cross-source discrepancies remain visible."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/ahrefs/skills/seo-ahrefs/SKILL.md"
tags: [seo, installed]
timestamp: 2026-10-04T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Ahrefs domain metrics, referring domains, backlinks, anchors, organic keywords, and Content Explorer results are the scope of this extension. It pairs paid Ahrefs evidence with `seo-backlinks` so cross-source discrepancies remain visible.

# When to use

Ahrefs domain metrics, referring domains, backlinks, anchors, organic keywords, and Content Explorer results are the scope of this extension. It pairs paid Ahrefs evidence with `seo-backlinks` so cross-source discrepancies remain visible.

# Installed at

- `~/.claude/skills/seo-ahrefs/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Requires Node 18+, an Ahrefs API token, and the official `@ahrefs/mcp` server installed by the repository extension script. Calls paid, live Ahrefs services and does not work from the skill file alone.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-ahrefs -g -a claude-code -y --copy`
```

# Citations

[1] [seo-ahrefs source](https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/ahrefs/skills/seo-ahrefs/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
