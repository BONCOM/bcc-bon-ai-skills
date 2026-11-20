---
type: Agent Skill
title: google-cloud-recipe-auth
description: "Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys."
resource: "https://github.com/google/skills/blob/main/skills/cloud/google-cloud-recipe-auth/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-11-20T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor, Claude Code, Codex and Antigravity
---

Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys.

# When to use

Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys.

# Installed at

- `~/.claude/skills/google-cloud-recipe-auth/SKILL.md`
- `~/.agents/skills/google-cloud-recipe-auth/SKILL.md`
- `~/.gemini/config/skills/google-cloud-recipe-auth` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

Apache-2.0

# Trust notes

Instruction-only with no credential reader. Its documented `gcloud auth` and ADC flows affect sensitive local or cloud credentials when a user deliberately runs them. 2026-10-09 (`4b940dd`): Google Cloud product naming standardized; the description now names Identity and Access Management (IAM) explicitly. No change to guidance. 2026-10-19 (`a342dc5`, v1.0.2) adds a usage-attribution block and `references/attribution.md`: agent-run `gcloud` commands get an inline `CLOUDSDK_METRICS_REQUEST_ATTRIBUTION` prefix and direct HTTP/MCP calls a `User-Agent` suffix naming only the skill and version (no user data, never in generated code, dropped if the user opts out). 2026-11-20 (`16b4164`): updated Express Mode link.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill google-cloud-recipe-auth -g -a claude-code -y --copy`
```

# Citations

[1] [google-cloud-recipe-auth source](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-recipe-auth/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
