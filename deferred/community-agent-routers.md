---
type: Deferred Tool
title: Community agent routers
description: "Reviewed routers assumed Claude-specific subagents and model aliases that did not match Cursor's available catalog."
resource: "https://github.com/wshobson/agents"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

Reviewed routers assumed Claude-specific subagents and model aliases that did not match Cursor's available catalog.

# Reconsider when

A router discovers the live client agent and model inventory rather than embedding names, and its fallback behavior is tested in Cursor.

# Trust boundary

Routers can silently widen scope, choose expensive models, or dispatch agents that mutate shared files. Require an allowlist, explicit unavailable-agent handling, bounded concurrency, and no invented model names.

# Citations

[1] [Source](https://github.com/wshobson/agents)
