---
type: Agent Skill
title: seo-schema
description: "Schema.org detection, validation, and generation are grouped in this skill, with JSON-LD as the preferred format. It checks required properties, data types, absolute URLs, dates, deprecated types, and current Google rich-result support before proposing code."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-schema/SKILL.md"
tags: [seo, installed]
timestamp: 2026-10-04T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Schema.org detection, validation, and generation are grouped in this skill, with JSON-LD as the preferred format. It checks required properties, data types, absolute URLs, dates, deprecated types, and current Google rich-result support before proposing code.

# When to use

Schema.org detection, validation, and generation are grouped in this skill, with JSON-LD as the preferred format. It checks required properties, data types, absolute URLs, dates, deprecated types, and current Google rich-result support before proposing code.

# Installed at

- `~/.claude/skills/seo-schema/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Fetches page source and may consult mutable Schema.org and Google rich-result documentation. Generated JSON-LD is output for review and is not injected into the target site.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-schema -g -a claude-code -y --copy`
```

# Citations

[1] [seo-schema source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-schema/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
