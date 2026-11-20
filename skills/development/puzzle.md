---
type: Agent Skill
title: puzzle
description: "Design grid and logic puzzle rules, solver-checked levels, reliable undo, difficulty progression, and helpful hints. Keep the board state separate from its visual animation."
resource: "https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/genres/puzzle/SKILL.md"
tags: [development, installed, game-ux]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Game UX
license: Apache-2.0
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Design grid and logic puzzle rules, solver-checked levels, reliable undo, difficulty progression, and helpful hints. Keep the board state separate from its visual animation.

# Installed at

- `~/.claude/skills/puzzle/SKILL.md`
- `~/.agents/skills/puzzle/SKILL.md`
- `~/.gemini/config/skills/puzzle/SKILL.md`

# Trust notes

Markdown and reference examples. Apply solver and undo checks that suit the game rules. Use original mechanics, content, and assets for new games.

License Apache-2.0. Installed files match the reviewed upstream revision `c6ca6c41c8`.

# Install or update

```bash
npx -y skills@1.5.18 add gamedev-skills/awesome-gamedev-agent-skills --skill puzzle -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/puzzle ~/.gemini/config/skills/puzzle  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/genres/puzzle/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
