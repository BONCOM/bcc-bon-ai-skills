---
type: Agent Skill
title: claude-api
description: "Claude and Anthropic SDK work should start with this reference, including model IDs, pricing, streaming, tool use, caching, tokens, and migrations. It routes to language-specific material and live official sources, and it avoids inserting Anthropic code into a project that uses another provider."
resource: "https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md"
tags: [development, installed, skill-development]
timestamp: 2026-07-27T00:00:00Z
category: development
group: Skill development
license: Apache-2.0
available_in: Cursor and Claude Code
---

Claude and Anthropic SDK work should start with this reference, including model IDs, pricing, streaming, tool use, caching, tokens, and migrations. It routes to language-specific material and live official sources, and it avoids inserting Anthropic code into a project that uses another provider.

# When to use

Claude and Anthropic SDK work should start with this reference, including model IDs, pricing, streaming, tool use, caching, tokens, and migrations. It routes to language-specific material and live official sources, and it avoids inserting Anthropic code into a project that uses another provider.

# Installed at

- `~/.claude/skills/claude-api/SKILL.md`
- `~/.agents/skills/claude-api/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Bundles documentation and examples, not an executable installer. Recommended implementations call the Anthropic API and require user-supplied credentials; live-source fallbacks use WebFetch.

# Install / update

```text
`npx -y skills@1.5.18 add anthropics/skills --skill claude-api -g -a claude-code -y --copy`
```

# Citations

[1] [claude-api source](https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
