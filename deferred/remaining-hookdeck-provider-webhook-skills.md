---
type: Deferred Tool
title: Remaining Hookdeck provider webhook skills
description: "Only `webhook-handler-patterns` and `stripe-webhooks` were installed (Stripe MCP is present). The other ~55 provider skills add catalog noise until that provider is in use."
resource: "https://github.com/hookdeck/webhook-skills"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

Only `webhook-handler-patterns` and `stripe-webhooks` were installed (Stripe MCP is present). The other ~55 provider skills add catalog noise until that provider is in use.

# Reconsider when

Implementing Shopify, Clerk, Resend, GitHub, or another listed provider webhook in a maintained app.

# Trust boundary

Provider skills include signature verification and example handlers that touch secrets and inbound event data. Install one named skill at a time.

# Citations

[1] [Source](https://github.com/hookdeck/webhook-skills)
