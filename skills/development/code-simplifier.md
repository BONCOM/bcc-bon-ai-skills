---
type: Agent Skill
title: code-simplifier
description: "Claude Code agent that simplifies recently modified code for clarity and maintainability while preserving exact behavior. Prefer after a logical chunk of implementation, not as a broad rewrite."
resource: "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier"
tags: [development, installed, skill-development]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Skill development
license: Apache-2.0
available_in: Claude Code
---

Official Anthropic Claude Code plugin: a `code-simplifier` agent that refines recently touched code for clarity without changing functionality.

# When to use

After a logical chunk of code is written, or when the user asks to simplify/polish recent changes without behavior changes. Prefer over community marketplace "code-simplifier" skills (some fail Gen Trust Hub).

# Installed at

- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/code-simplifier/1.0.0/agents/code-simplifier.md`

# Availability

Claude Code (plugin). Not a normal `SKILL.md` for Cursor.

# License

Apache-2.0

# Trust notes

Official Anthropic plugin from `claude-plugins-official`. Agent prompt only (no bundled installer scripts, hooks, or MCP). Spawns via Claude Code's Task/agent machinery with model preference `opus` in the agent frontmatter. Community clones on skills.sh were skipped (e.g. simonwong Gen Trust Hub Fail).

# Install / update

```text
claude plugin install code-simplifier@claude-plugins-official --scope user
```

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
- Related plugin: [`skill-creator`](./skill-creator.md)

# Citations

[1] [code-simplifier plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier)
