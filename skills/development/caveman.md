---
type: Agent Skill
title: caveman
description: "Ultra-compressed communication mode — cuts narration while keeping technical facts, code, commands, and errors exact. Intensity levels: lite, full, ultra (plus wenyan variants). Invoke with /caveman or 'talk like caveman'; say 'normal mode' to exit."
resource: "https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md"
tags: [development, installed, workflow]
timestamp: 2026-08-17T00:00:00Z
category: development
group: Workflow and discovery
license: MIT
available_in: Cursor and Claude Code
---

Token-efficient reply style: drop filler, keep every technical fact. Optional intensity levels including wenyan variants.

# When to use

When the user asks for caveman mode, fewer tokens, or `/caveman`. Exit on "normal mode". Do not force this style on formal docs, legal text, or user-facing copy unless requested.

# Installed at

- `~/.claude/skills/caveman/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Installed as the single named skill only (`caveman`) — sibling skills (`caveman-commit`, `cavecrew`, etc.) and the repo's Claude Code plugin/hooks were not installed. Instruction + README; no bundled executable scripts in the skill directory. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk. Style-only; does not change how code or commands are written. Picked up a negation-safety rule (never drop not/never/no/only/except), a no-narration rule for tool calls, an explicit `off` switch, and tighter guardrails on when to preserve grammar particles vs. drop articles. Now also forbids ADDING words to sound more "caveman" (compression only, never style that grows output) and treats "open a defect"/"file a bug" the same as "open issue" — body stays normal prose since it's read by other humans.

# Install / update

```text
npx -y skills@1.5.18 add JuliusBrussee/caveman --skill caveman -g -a claude-code -y --copy
```

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [caveman source](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md)
