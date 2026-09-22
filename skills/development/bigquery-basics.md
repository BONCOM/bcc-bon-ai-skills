---
type: Agent Skill
title: bigquery-basics
description: "BigQuery datasets, tables, views, jobs, SQL queries, and basic ingestion belong here. Use it when the work is the BigQuery resource model or `bq`/client-library operations rather than BQML or pandas-style BigFrames."
resource: "https://github.com/google/skills/blob/main/skills/cloud/bigquery-basics/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-09-21T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

BigQuery datasets, tables, views, jobs, SQL queries, and basic ingestion belong here. Use it when the work is the BigQuery resource model or `bq`/client-library operations rather than BQML or pandas-style BigFrames.

# When to use

BigQuery datasets, tables, views, jobs, SQL queries, and basic ingestion belong here. Use it when the work is the BigQuery resource model or `bq`/client-library operations rather than BQML or pandas-style BigFrames.

# Installed at

- `~/.claude/skills/bigquery-basics/SKILL.md`
- `~/.agents/skills/bigquery-basics/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction and Markdown references only (CLI, clients, MCP, Terraform, IAM, Change History via `APPENDS`/`CHANGES`, and now continuous queries). Later use runs authenticated `gcloud`/`bq` or BigQuery MCP against live projects and can create or query datasets; keep project and location explicit. Sibling `bigquery-ai-ml` was deferred until BQML work appears.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill bigquery-basics -g -a claude-code -y --copy`
```

# Citations

[1] [bigquery-basics source](https://github.com/google/skills/blob/main/skills/cloud/bigquery-basics/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
