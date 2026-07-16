---
type: Deferred Tool
title: Context Mode
description: "Context exhaustion has not been measured as a recurring problem, while the plugin adds global hooks, an MCP server, subprocess execution, and local SQLite state."
resource: "https://github.com/mksglu/context-mode"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

Context exhaustion has not been measured as a recurring problem, while the plugin adds global hooks, an MCP server, subprocess execution, and local SQLite state.

# Reconsider when

Real sessions repeatedly lose necessary context and a benchmark shows that indexed retrieval preserves the details this work needs.

# Trust boundary

Hooks intercept tool activity, sandbox commands and fetched content, and record session events in per-project SQLite. Review capture scope, subprocess isolation, upgrade behavior, purge behavior, and failure recovery before installation.

# Citations

[1] [Source](https://github.com/mksglu/context-mode)
