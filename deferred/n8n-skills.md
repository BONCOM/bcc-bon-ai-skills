---
type: Deferred Tool
title: n8n-skills
description: "Requires a configured `n8n-mcp` server and an n8n instance; neither is part of the current catalog stack."
resource: "https://github.com/czlonkowski/n8n-skills"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

Requires a configured `n8n-mcp` server and an n8n instance; neither is part of the current catalog stack.

# Reconsider when

An automation project uses n8n and `n8n-mcp` is already authenticated.

# Trust boundary

Plugin plus MCP can create and modify live workflows. Review hooks and MCP scope before install.

# Citations

[1] [Source](https://github.com/czlonkowski/n8n-skills)
