---
type: Agent Skill
title: animation-performance
description: "Diagnose dropped frames in transitions, overlays, or gameplay effects. Measure paint, compositing, and main-thread work with a recording before changing motion."
resource: "https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/animation-performance/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Frontend and UI
license: MIT
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Diagnose dropped frames in transitions, overlays, or gameplay effects. Measure paint, compositing, and main-thread work with a recording before changing motion.

# Installed at

- `~/.claude/skills/animation-performance/SKILL.md`
- `~/.agents/skills/animation-performance/SKILL.md`
- `~/.gemini/config/skills/animation-performance/SKILL.md`

# Trust notes

Markdown only. A browser performance recording and real-device checks supply the evidence.

License MIT. Installed files match the reviewed upstream revision `64eb3deb9a`.

# Install or update

```bash
npx -y skills@1.5.18 add emilkowalski/skills --skill animation-performance -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/animation-performance ~/.gemini/config/skills/animation-performance  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/animation-performance/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
