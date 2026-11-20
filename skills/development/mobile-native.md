---
type: Agent Skill
title: mobile-native
description: "Review a web app on phones for safe areas, input zoom, viewport sizing, tap feedback, hover behavior, and scrolling. Verify the affected flow on a real device where available."
resource: "https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/mobile-native/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Frontend and UI
license: MIT
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Review a web app on phones for safe areas, input zoom, viewport sizing, tap feedback, hover behavior, and scrolling. Verify the affected flow on a real device where available.

# Installed at

- `~/.claude/skills/mobile-native/SKILL.md`
- `~/.agents/skills/mobile-native/SKILL.md`
- `~/.gemini/config/skills/mobile-native/SKILL.md`

# Trust notes

Markdown only. CSS advice is specific to the browser behavior under review.

License MIT. Installed files match the reviewed upstream revision `64eb3deb9a`.

# Install or update

```bash
npx -y skills@1.5.18 add emilkowalski/skills --skill mobile-native -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/mobile-native ~/.gemini/config/skills/mobile-native  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/mobile-native/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
