---
type: Agent Skill
title: performance-optimization
description: "Measured slowness, regressions, Core Web Vitals failures, slow database access, and explicit latency budgets are its trigger. The workflow requires a baseline and profile before changes, then targets the observed frontend, backend, query, or database bottleneck and measures again."
resource: "https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

Measured slowness, regressions, Core Web Vitals failures, slow database access, and explicit latency budgets are its trigger. The workflow requires a baseline and profile before changes, then targets the observed frontend, backend, query, or database bottleneck and measures again.

# When to use

Measured slowness, regressions, Core Web Vitals failures, slow database access, and explicit latency budgets are its trigger. The workflow requires a baseline and profile before changes, then targets the observed frontend, backend, query, or database bottleneck and measures again.

# Installed at

- `~/.claude/skills/performance-optimization/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts. Examples refer to Lighthouse, CrUX, real-user monitoring, and optional `npx` profilers, which can create network traffic when deliberately run.

# Install / update

```text
`npx -y skills@1.5.18 add addyosmani/agent-skills --skill performance-optimization -g -a claude-code -y --copy`
```

# Citations

[1] [performance-optimization source](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
