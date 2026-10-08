---
type: Agent Skill
title: handoff
description: "Compact the current conversation into a handoff document for a fresh agent or session. Manual invoke only (`/handoff` or explicit request). Writes to the OS temp directory; references specs/plans by path instead of copying them."
resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md"
tags: [development, installed, workflow]
timestamp: 2026-10-08T00:00:00Z
category: development
group: Workflow and discovery
license: MIT
available_in: Cursor and Claude Code
---

Compact the live thread of a long session into a handoff document another agent (or a fresh chat) can resume from.

# When to use

Use at context limits, end of day, or deliberate handoff to another agent/worktree. Pass what the next session should focus on. Do not use for ordinary mid-task summaries when the same chat continues.

# Installed at

- `~/.claude/skills/handoff/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only plus `agents/openai.yaml` (display metadata). `disable-model-invocation: true` — agent must not auto-trigger; user invokes `/handoff` or asks explicitly. Writes the handoff file under the OS temp directory (not the workspace). Requires redacting secrets/PII before write. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk. Minor wording fix: the "suggested skills" section now says to name skills the next agent should call the Skill tool for, rather than skills to "invoke."

# Install / update

```text
npx -y skills@1.5.18 add mattpocock/skills --skill handoff -g -a claude-code -y --copy
```

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [handoff source](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md)
[2] [AI Hero handoff docs](https://aihero.dev/skills-handoff)
