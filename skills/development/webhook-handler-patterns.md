---
type: Agent Skill
title: webhook-handler-patterns
description: "Webhook receivers that need the verify → parse → handle-idempotently sequence, framework-specific raw-body handling, retries, or error-code conventions belong here. Use it with Next.js, Express, or FastAPI handlers before adding provider-specific skills."
resource: "https://github.com/hookdeck/webhook-skills/blob/main/skills/webhook-handler-patterns/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

Webhook receivers that need the verify → parse → handle-idempotently sequence, framework-specific raw-body handling, retries, or error-code conventions belong here. Use it with Next.js, Express, or FastAPI handlers before adding provider-specific skills.

# When to use

Webhook receivers that need the verify → parse → handle-idempotently sequence, framework-specific raw-body handling, retries, or error-code conventions belong here. Use it with Next.js, Express, or FastAPI handlers before adding provider-specific skills.

# Installed at

- `~/.claude/skills/webhook-handler-patterns/SKILL.md`
- `~/.agents/skills/webhook-handler-patterns/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction and Markdown references; no bundled executable installer. Examples may suggest local tunnels such as Hookdeck CLI; those are deliberate network tools when run. Complements `security-and-hardening` rather than replacing it.

# Install / update

```text
`npx -y skills@1.5.18 add hookdeck/webhook-skills --skill webhook-handler-patterns -g -a claude-code -y --copy`
```

# Citations

[1] [webhook-handler-patterns source](https://github.com/hookdeck/webhook-skills/blob/main/skills/webhook-handler-patterns/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
