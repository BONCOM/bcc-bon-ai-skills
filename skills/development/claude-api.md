---
type: Agent Skill
title: claude-api
description: "Claude and Anthropic SDK work should start with this reference, including model IDs, pricing, streaming, tool use, caching, tokens, and migrations. It routes to language-specific material and live official sources, and it avoids inserting Anthropic code into a project that uses another provider."
resource: "https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md"
tags: [development, installed, skill-development]
timestamp: 2026-10-09T00:00:00Z
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

Bundles documentation and examples, not an executable installer. Recommended implementations call the Anthropic API and require user-supplied credentials; live-source fallbacks use WebFetch. Managed Agents section substantially expanded (August launch wave): multi-agent orchestration patterns, expanded API reference/events/tools/scheduled-deployments coverage. Adds a new `shared/prompt-audit.md` reference (219 lines) and a prompt-audit subcommand. 2026-10-09 (`9d63080`, `dbd4588`): Claude Haiku 5.5 is now the current Haiku, Managed Agents and preserved-thinking fixes, dynamic workflows, and new Managed Agents quickstarts under `shared/managed-agents-quickstarts/`. Also bundles `shared/preserved-thinking-migration/drop_block_probe.py`, a dependency-free diagnostic (stdlib `http.client`, credentials from the environment) that only sends live API requests when the user runs it with `--yes`; nothing runs automatically.

# Install / update

```text
`npx -y skills@1.5.18 add anthropics/skills --skill claude-api -g -a claude-code -y --copy`
```

# Citations

[1] [claude-api source](https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
