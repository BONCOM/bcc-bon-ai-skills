---
type: Agent Skill
title: cloud-logging-query-generation
description: "Turn to this skill when a debugging question needs a Google Cloud Logging Query Language expression. It checks service-specific monitored resource types, uses strict quoting and boolean syntax, and returns query text only; it is not for SQL or Spanner data."
resource: "https://github.com/google/skills/blob/main/skills/cloud/cloud-logging-query-generation/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-10-19T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Turn to this skill when a debugging question needs a Google Cloud Logging Query Language expression. It checks service-specific monitored resource types, uses strict quoting and boolean syntax, and returns query text only; it is not for SQL or Spanner data.

# When to use

Turn to this skill when a debugging question needs a Google Cloud Logging Query Language expression. It checks service-specific monitored resource types, uses strict quoting and boolean syntax, and returns query text only; it is not for SQL or Spanner data.

# Installed at

- `~/.claude/skills/cloud-logging-query-generation/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only with 22 Markdown service references, including a new dedicated Audit Logs reference (`protoPayload` schema, log-type routing across Admin Activity/Data Access/System Event/Policy Denied). It generates LQL but does not authenticate to or query Cloud Logging. 2026-10-19 (`a342dc5`, v1.0.2) adds a usage-attribution block and `references/attribution.md`: agent-run `gcloud` commands get an inline `CLOUDSDK_METRICS_REQUEST_ATTRIBUTION` prefix and direct HTTP/MCP calls a `User-Agent` suffix naming only the skill and version (no user data, never in generated code, dropped if the user opts out).

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill cloud-logging-query-generation -g -a claude-code -y --copy`
```

# Citations

[1] [cloud-logging-query-generation source](https://github.com/google/skills/blob/main/skills/cloud/cloud-logging-query-generation/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
