---
type: Agent Skill
title: make-interfaces-feel-better
description: "Polish a rendered interface by checking optical alignment, icon weights, button hit areas, type wrapping, layered surfaces, and hover, focus, pressed, loading, and empty states."
resource: "https://github.com/jakubkrehel/make-interfaces-feel-better/blob/6d9f2f1df10e8ce2ae1708598a73b0506fb98794/skills/make-interfaces-feel-better/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Frontend and UI
license: MIT
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Polish a rendered interface by checking optical alignment, icon weights, button hit areas, type wrapping, layered surfaces, and hover, focus, pressed, loading, and empty states.

# Installed at

- `~/.claude/skills/make-interfaces-feel-better/SKILL.md`
- `~/.agents/skills/make-interfaces-feel-better/SKILL.md`
- `~/.gemini/config/skills/make-interfaces-feel-better/SKILL.md`

# Trust notes

Markdown and display metadata only. Apply changes through the project's existing component and token system. Use rendered states to confirm the improvement.

License MIT. Installed files match the reviewed upstream revision `6d9f2f1df1`.

# Install or update

```bash
npx -y skills@1.5.18 add jakubkrehel/make-interfaces-feel-better --skill make-interfaces-feel-better -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/make-interfaces-feel-better ~/.gemini/config/skills/make-interfaces-feel-better  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/jakubkrehel/make-interfaces-feel-better/blob/6d9f2f1df10e8ce2ae1708598a73b0506fb98794/skills/make-interfaces-feel-better/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
