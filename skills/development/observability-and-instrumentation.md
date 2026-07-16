---
type: Agent Skill
title: observability-and-instrumentation
description: "Production endpoints, jobs, queues, retries, and service integrations need this skill when current telemetry cannot explain failures. It defines operational questions first and then chooses logs, metrics, traces, and alerts that answer those questions without leaking secrets or personal data."
resource: "https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

Production endpoints, jobs, queues, retries, and service integrations need this skill when current telemetry cannot explain failures. It defines operational questions first and then chooses logs, metrics, traces, and alerts that answer those questions without leaking secrets or personal data.

# When to use

Production endpoints, jobs, queues, retries, and service integrations need this skill when current telemetry cannot explain failures. It defines operational questions first and then chooses logs, metrics, traces, and alerts that answer those questions without leaking secrets or personal data.

# Installed at

- `~/.claude/skills/observability-and-instrumentation/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts. It documents telemetry vendors and integrations but makes no network connection itself.

# Install / update

```text
`npx -y skills@1.5.18 add addyosmani/agent-skills --skill observability-and-instrumentation -g -a claude-code -y --copy`
```

# Citations

[1] [observability-and-instrumentation source](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
