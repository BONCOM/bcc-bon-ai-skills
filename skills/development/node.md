---
type: Agent Skill
title: node
description: "Node.js backend work gets targeted guidance here, especially for Node 22 native TypeScript type stripping, module resolution, async control flow, streams, shutdown, logging, profiling, caching, and flaky tests. It supplies a compatible `tsconfig` direction and avoids syntax that Node's runtime canno"
resource: "https://github.com/mcollina/skills/blob/main/skills/node/SKILL.md"
tags: [development, installed, node-js]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Node.js
license: MIT
available_in: Cursor and Claude Code
---

Node.js backend work gets targeted guidance here, especially for Node 22 native TypeScript type stripping, module resolution, async control flow, streams, shutdown, logging, profiling, caching, and flaky tests. It supplies a compatible `tsconfig` direction and avoids syntax that Node's runtime cannot strip.

# When to use

Node.js backend work gets targeted guidance here, especially for Node 22 native TypeScript type stripping, module resolution, async control flow, streams, shutdown, logging, profiling, caching, and flaky tests. It supplies a compatible `tsconfig` direction and avoids syntax that Node's runtime cannot strip.

# Installed at

- `~/.claude/skills/node/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Includes two inspected TypeScript examples. One opens a demonstration HTTP server on `0.0.0.0:3000` only when run directly; its test uses a random localhost port. Other references mention npm, npx, and fetch.

# Install / update

```text
`npx -y skills@1.5.18 add mcollina/skills --skill node -g -a claude-code -y --copy`
```

# Citations

[1] [node source](https://github.com/mcollina/skills/blob/main/skills/node/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
