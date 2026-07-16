---
type: Agent Skill
title: stripe-webhooks
description: "Stripe payment, subscription, and invoice webhook setup belongs here: signature verification with the raw body, common event types, and framework examples. Pair with `webhook-handler-patterns` for idempotency and retries; use the Stripe MCP for live account operations."
resource: "https://github.com/hookdeck/webhook-skills/blob/main/skills/stripe-webhooks/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

Stripe payment, subscription, and invoice webhook setup belongs here: signature verification with the raw body, common event types, and framework examples. Pair with `webhook-handler-patterns` for idempotency and retries; use the Stripe MCP for live account operations.

# When to use

Stripe payment, subscription, and invoice webhook setup belongs here: signature verification with the raw body, common event types, and framework examples. Pair with `webhook-handler-patterns` for idempotency and retries; use the Stripe MCP for live account operations.

# Installed at

- `~/.claude/skills/stripe-webhooks/SKILL.md`
- `~/.agents/skills/stripe-webhooks/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction, references, and runnable Express/Next.js/FastAPI examples. Generated handlers touch secrets (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`) and payment event data; keep secrets out of clients and verify signatures before parsing.

# Install / update

```text
`npx -y skills@1.5.18 add hookdeck/webhook-skills --skill stripe-webhooks -g -a claude-code -y --copy`
```

# Citations

[1] [stripe-webhooks source](https://github.com/hookdeck/webhook-skills/blob/main/skills/stripe-webhooks/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
