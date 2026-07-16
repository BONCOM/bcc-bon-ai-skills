---
type: Agent Skill
title: skill-creator
description: "Skill authoring and evaluation in Claude Code are the purpose of this plugin. It can create or revise a skill, design realistic trigger and output evaluations, compare controlled runs, inspect benchmark variance, improve the description, and package the result."
resource: "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator"
tags: [development, installed, skill-development]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Skill development
license: Apache-2.0
available_in: Claude Code
---

Skill authoring and evaluation in Claude Code are the purpose of this plugin. It can create or revise a skill, design realistic trigger and output evaluations, compare controlled runs, inspect benchmark variance, improve the description, and package the result.

# When to use

Skill authoring and evaluation in Claude Code are the purpose of this plugin. It can create or revise a skill, design realistic trigger and output evaluations, compare controlled runs, inspect benchmark variance, improve the description, and package the result.

# Installed at

- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/skill-creator/61414f8881f6/skills/skill-creator/SKILL.md`

# Availability

Claude Code

# License

Apache-2.0

# Trust notes

Bundles eight Python scripts, three evaluator-agent prompts, an HTML review UI, and packaging utilities. Evaluation and description optimization can spawn subagents, run the `claude` CLI, open a local viewer, and write benchmark workspaces; no hooks or MCP servers are installed.

# Install / update

```text
`claude plugin install skill-creator@claude-plugins-official --scope user`
```

# Citations

[1] [skill-creator source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
