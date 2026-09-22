---
type: Agent Skill
title: cloud-run-basics
description: "Cloud Run services, finite jobs, and always-on worker pools each have a different lifecycle, which this skill makes explicit. It explains which resource type fits the workload and provides `gcloud` flows for image and source deployments rather than treating every container as an HTTP service."
resource: "https://github.com/google/skills/blob/main/skills/cloud/cloud-run-basics/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-09-21T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Cloud Run services, finite jobs, and always-on worker pools each have a different lifecycle, which this skill makes explicit. It explains which resource type fits the workload and provides `gcloud` flows for image and source deployments rather than treating every container as an HTTP service.

# When to use

Cloud Run services, finite jobs, and always-on worker pools each have a different lifecycle, which this skill makes explicit. It explains which resource type fits the workload and provides `gcloud` flows for image and source deployments rather than treating every container as an HTTP service.

# Installed at

- `~/.claude/skills/cloud-run-basics/SKILL.md`
- `~/.agents/skills/cloud-run-basics/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only; commands use authenticated `gcloud`, enable APIs, build images, and create or update Cloud Run resources. Confirm project, region, billing, and resource name before execution.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill cloud-run-basics -g -a claude-code -y --copy`
```

# Citations

[1] [cloud-run-basics source](https://github.com/google/skills/blob/main/skills/cloud/cloud-run-basics/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
