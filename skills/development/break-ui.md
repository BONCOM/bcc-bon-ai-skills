---
type: Agent Skill
title: break-ui
description: "Stress-test tables, forms, and content-heavy screens with realistic data at schema limits. Check long names, translated labels, empty lists, and large datasets through the existing data boundary."
resource: "https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/break-ui/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Frontend and UI
license: MIT
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Stress-test tables, forms, and content-heavy screens with realistic data at schema limits. Check long names, translated labels, empty lists, and large datasets through the existing data boundary.

# Installed at

- `~/.claude/skills/break-ui/SKILL.md`
- `~/.agents/skills/break-ui/SKILL.md`
- `~/.gemini/config/skills/break-ui/SKILL.md`

# Trust notes

Markdown and a fixture catalog. Use synthetic inputs in local fixtures or tests. The upstream preview toggle, if used, belongs in development.

License MIT. Installed files match the reviewed upstream revision `64eb3deb9a`.

# Install or update

```bash
npx -y skills@1.5.18 add emilkowalski/skills --skill break-ui -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/break-ui ~/.gemini/config/skills/break-ui  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/break-ui/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
