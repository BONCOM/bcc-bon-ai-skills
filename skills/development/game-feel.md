---
type: Agent Skill
title: game-feel
description: "Tune interaction feedback for selecting, succeeding, failing, and finishing a game action. Set feedback intensity, preserve input responsiveness, and validate it in playtests."
resource: "https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-feel/SKILL.md"
tags: [development, installed, game-ux]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Game UX
license: Apache-2.0
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Tune interaction feedback for selecting, succeeding, failing, and finishing a game action. Set feedback intensity, preserve input responsiveness, and validate it in playtests.

# Installed at

- `~/.claude/skills/game-feel/SKILL.md`
- `~/.agents/skills/game-feel/SKILL.md`
- `~/.gemini/config/skills/game-feel/SKILL.md`

# Trust notes

Markdown and engine-specific reference examples. Honor reduced motion and keep visual feedback nonessential to understanding game state.

License Apache-2.0. Installed files match the reviewed upstream revision `c6ca6c41c8`.

# Install or update

```bash
npx -y skills@1.5.18 add gamedev-skills/awesome-gamedev-agent-skills --skill game-feel -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/game-feel ~/.gemini/config/skills/game-feel  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-feel/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
