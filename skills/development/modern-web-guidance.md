---
type: Agent Skill
title: modern-web-guidance
description: "Look up browser support and fallbacks for responsive layouts, dialogs, forms, CSS motion, typography, and other native web features."
resource: "https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Frontend and UI
license: Apache-2.0
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Look up browser support and fallbacks for responsive layouts, dialogs, forms, CSS motion, typography, and other native web features.

# Installed at

- `~/.claude/skills/modern-web-guidance/SKILL.md`
- `~/.agents/skills/modern-web-guidance/SKILL.md`
- `~/.gemini/config/skills/modern-web-guidance/SKILL.md`

# Trust notes

Markdown guides. The upstream search and retrieval workflow uses the companion npm CLI on demand. Use generic web-platform queries. The upstream trigger covers a wide range of frontend work. The catalog routes it to compatibility and native web platform questions.

License Apache-2.0. Installed files match the reviewed upstream revision `64a6d708f5`.

# Install or update

```bash
npx -y skills@1.5.18 add GoogleChrome/modern-web-guidance --skill modern-web-guidance -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/modern-web-guidance ~/.gemini/config/skills/modern-web-guidance  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/skills/modern-web-guidance/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
