---
type: Agent Skill
title: api-and-interface-design
description: "Design contracts across Next.js, Express, FastAPI, and shared modules. Review compatibility, boundary validation, stable errors, and how existing callers will handle a change."
resource: "https://github.com/addyosmani/agent-skills/blob/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/api-and-interface-design/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Development quality
license: MIT
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Design contracts across Next.js, Express, FastAPI, and shared modules. Review compatibility, boundary validation, stable errors, and how existing callers will handle a change.

# Installed at

- `~/.claude/skills/api-and-interface-design/SKILL.md`
- `~/.agents/skills/api-and-interface-design/SKILL.md`
- `~/.gemini/config/skills/api-and-interface-design/SKILL.md`

# Trust notes

Markdown only. Examples inform implementation while the Suite's documented identity, permissions, and service contracts govern Boncom integrations.

License MIT. Installed files match the reviewed upstream revision `8c99fa36d9`.

# Install or update

```bash
npx -y skills@1.5.18 add addyosmani/agent-skills --skill api-and-interface-design -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/api-and-interface-design ~/.gemini/config/skills/api-and-interface-design  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/addyosmani/agent-skills/blob/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/api-and-interface-design/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
