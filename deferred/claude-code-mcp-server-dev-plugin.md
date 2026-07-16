---
type: Deferred Tool
title: "Claude Code `mcp-server-dev` plugin"
description: "Cross-client MCP authoring is covered by the installed `mcp-builder` normal skill. This plugin (`build-mcp-server`, `build-mcp-app`, `build-mcpb`) is Claude Code marketplace packaging and would duplicate catalog surface."
resource: "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

Cross-client MCP authoring is covered by the installed `mcp-builder` normal skill. This plugin (`build-mcp-server`, `build-mcp-app`, `build-mcpb`) is Claude Code marketplace packaging and would duplicate catalog surface.

# Reconsider when

Claude Code-only work needs MCP Apps UI widgets or MCPB bundling that `mcp-builder` does not cover.

# Trust boundary

Plugin install can add Claude Code commands and skills outside the `~/.claude/skills/` normal-skill path; review plugin contents before enabling.

# Citations

[1] [Source](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev)
