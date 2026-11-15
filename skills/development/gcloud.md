---
type: Agent Skill
title: gcloud
description: "Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. Mandates `gcloud help <leaf_command>` validation before proposing or running any command or plan (parent-group help doesn't count, web search is forbidden as a syntax fallback), plus explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations."
resource: "https://github.com/google/skills/blob/main/skills/cloud/gcloud/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-11-12T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. Mandates `gcloud help <leaf_command>` validation before proposing or running any command or plan (parent-group help doesn't count, web search is forbidden as a syntax fallback), plus explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations.

# When to use

Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. Mandates `gcloud help <leaf_command>` validation before proposing or running any command or plan (parent-group help doesn't count, web search is forbidden as a syntax fallback), plus explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations.

# Installed at

- `~/.claude/skills/gcloud/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only, but later use operates the authenticated Google Cloud CLI against live resources. It may read active configuration and make network calls; its safeguards forbid autonomous high-risk changes. `--validate-only` is now accepted alongside `--dry-run` as a Step 2/3 preview mechanism, and the trigger description now also covers answering questions about gcloud syntax/flags, not just command execution. 2026-10-19 (`a342dc5`, v1.0.1) adds a usage-attribution block and `references/attribution.md`: agent-run `gcloud` commands get an inline `CLOUDSDK_METRICS_REQUEST_ATTRIBUTION` prefix and direct HTTP/MCP calls a `User-Agent` suffix naming only the skill and version (no user data, never in generated code, dropped if the user opts out). 2026-10-26 (`ae55fb6`, `b027a20` 2026-10-23, v1.0.3): adds a No Proactive `gcloud` CLI Installation rule (never install the CLI or components without the user's explicit yes, then stop and wait) and a multi-skill attribution precedence rule (a loaded product-specific skill's `skill:<name>` tag wins over `skill:gcloud`). 2026-11-12 (`db25e83`, v1.0.4): the mandatory `gcloud help` check is skipped when the prompt supplies help output, says syntax is validated, or says not to execute anything (then no `run_command` at all, references read directly); operations are `gcloud <GROUP> operations describe`; the WIF link points at the new Authenticate page; MCP guidance covers folder queries.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill gcloud -g -a claude-code -y --copy`
```

# Citations

[1] [gcloud source](https://github.com/google/skills/blob/main/skills/cloud/gcloud/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
