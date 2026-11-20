---
type: Agent Skill
title: game-ui-ux
description: "Design and verify game HUDs, menus, controls, and pause overlays. Check focus, touch and controller navigation, safe areas, and whether important information survives narrow screens."
resource: "https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-ui-ux/SKILL.md"
tags: [development, installed, game-ux]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Game UX
license: Apache-2.0
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Design and verify game HUDs, menus, controls, and pause overlays. Check focus, touch and controller navigation, safe areas, and whether important information survives narrow screens.

# Installed at

- `~/.claude/skills/game-ui-ux/SKILL.md`
- `~/.agents/skills/game-ui-ux/SKILL.md`
- `~/.gemini/config/skills/game-ui-ux/SKILL.md`

# Trust notes

Markdown and examples for multiple engines. Use the project's existing engine and UI stack.

License Apache-2.0. Installed files match the reviewed upstream revision `c6ca6c41c8`.

# Install or update

```bash
npx -y skills@1.5.18 add gamedev-skills/awesome-gamedev-agent-skills --skill game-ui-ux -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/game-ui-ux ~/.gemini/config/skills/game-ui-ux  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-ui-ux/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
