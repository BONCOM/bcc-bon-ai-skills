---
type: Agent Skill
title: google-cloud-recipe-auth
description: "Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys."
resource: "https://github.com/google/skills/blob/main/skills/cloud/google-cloud-recipe-auth/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys.

# When to use

Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys.

# Installed at

- `~/.claude/skills/google-cloud-recipe-auth/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only with no credential reader. Its documented `gcloud auth` and ADC flows affect sensitive local or cloud credentials when a user deliberately runs them.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill google-cloud-recipe-auth -g -a claude-code -y --copy`
```

# Citations

[1] [google-cloud-recipe-auth source](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-recipe-auth/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
