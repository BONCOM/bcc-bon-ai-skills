---
type: Agent Skill
title: mcp-builder
description: "Building or redesigning MCP servers (Python FastMCP or Node/TypeScript SDK) belongs here: research → tool design → implementation → evaluation. It is the MCP counterpart to `skill-creator` and is installed as a normal skill so Cursor and Claude Code both see it."
resource: "https://github.com/anthropics/skills/blob/main/skills/mcp-builder/SKILL.md"
tags: [development, installed, skill-development]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Skill development
license: Apache-2.0
available_in: Cursor and Claude Code
---

Building or redesigning MCP servers (Python FastMCP or Node/TypeScript SDK) belongs here: research → tool design → implementation → evaluation. It is the MCP counterpart to `skill-creator` and is installed as a normal skill so Cursor and Claude Code both see it.

# When to use

Building or redesigning MCP servers (Python FastMCP or Node/TypeScript SDK) belongs here: research → tool design → implementation → evaluation. It is the MCP counterpart to `skill-creator` and is installed as a normal skill so Cursor and Claude Code both see it.

# Installed at

- `~/.claude/skills/mcp-builder/SKILL.md`
- `~/.agents/skills/mcp-builder/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction plus `reference/` guides and `scripts/` (`evaluation.py`, `connections.py`) that can call the Anthropic API and connect to a candidate MCP server when deliberately run. Fetches live MCP protocol and SDK docs during use. Not the Claude Code-only `mcp-server-dev` plugin (deferred; different packaging).

# Install / update

```text
`npx -y skills@1.5.18 add anthropics/skills --skill mcp-builder -g -a claude-code -y --copy`
```

# Citations

[1] [mcp-builder source](https://github.com/anthropics/skills/blob/main/skills/mcp-builder/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
