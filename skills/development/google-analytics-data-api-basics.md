---
type: Agent Skill
title: google-analytics-data-api-basics
description: "GA4 reporting through the Analytics Data API is the scope: API enablement, compatible dimensions and metrics, and v1beta report construction. The skill covers property-scoped reporting, metadata checks, pagination, date ranges, and client-library requests instead of relying on the Analytics UI."
resource: "https://github.com/google/skills/blob/main/skills/analytics/google-analytics-data-api-basics/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

GA4 reporting through the Analytics Data API is the scope: API enablement, compatible dimensions and metrics, and v1beta report construction. The skill covers property-scoped reporting, metadata checks, pagination, date ranges, and client-library requests instead of relying on the Analytics UI.

# When to use

GA4 reporting through the Analytics Data API is the scope: API enablement, compatible dimensions and metrics, and v1beta report construction. The skill covers property-scoped reporting, metadata checks, pagination, date ranges, and client-library requests instead of relying on the Analytics UI.

# Installed at

- `~/.claude/skills/google-analytics-data-api-basics/SKILL.md`
- `~/.agents/skills/google-analytics-data-api-basics/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only; examples use authenticated `gcloud` and the Google Analytics Data API, which require a Cloud project, GA4 property access, API enablement, and network calls.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill google-analytics-data-api-basics -g -a claude-code -y --copy`
```

# Citations

[1] [google-analytics-data-api-basics source](https://github.com/google/skills/blob/main/skills/analytics/google-analytics-data-api-basics/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
