---
type: Agent Skill
title: gcloud
description: "Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. It requires command help validation, explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations."
resource: "https://github.com/google/skills/blob/main/skills/cloud/gcloud/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. It requires command help validation, explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations.

# When to use

Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. It requires command help validation, explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations.

# Installed at

- `~/.claude/skills/gcloud/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only, but later use operates the authenticated Google Cloud CLI against live resources. It may read active configuration and make network calls; its safeguards forbid autonomous high-risk changes.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill gcloud -g -a claude-code -y --copy`
```

# Citations

[1] [gcloud source](https://github.com/google/skills/blob/main/skills/cloud/gcloud/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
