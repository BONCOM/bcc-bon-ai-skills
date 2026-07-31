---
type: Agent Skill
title: supabase-postgres-best-practices
description: "Postgres best practices maintained by Supabase, for Postgres running anywhere — not just Supabase projects. Covers schema/migration design, RLS policies and their tests, indexes, triggers, database functions, queues (pg_cron, pgmq), pgvector search, pg_restore/data imports, and diagnosing slow queries, locking, bloat, or cross-tenant data leaks."
resource: "https://github.com/supabase/agent-skills/blob/main/skills/supabase-postgres-best-practices/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-30T00:00:00Z
category: development
group: Google Cloud
license: MIT
available_in: Cursor and Claude Code
---

Postgres best practices maintained by Supabase, for Postgres running anywhere — not just Supabase projects. Covers schema/migration design, RLS policies and their tests, indexes, triggers, database functions, queues (pg_cron, pgmq), pgvector search, pg_restore/data imports, and diagnosing slow queries, locking, bloat, or cross-tenant data leaks.

# When to use

Load before writing or changing anything that lives in a Postgres database: table/column creation or alteration, schema design, migrations and declarative schema files, RLS policies and their tests, indexes, triggers, database functions, queues (pg_cron, pgmq), pgvector/semantic search, and pg_restore or data imports. Also load when diagnosing slow queries, high CPU, timeouts, EXPLAIN plans, connection exhaustion, locking, bloat, or rows visible to the wrong tenant — even for a one-column change or a single query.

# Installed at

- `~/.claude/skills/supabase-postgres-best-practices/SKILL.md`
- `~/.agents/skills/supabase-postgres-best-practices/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction and reference Markdown only; no bundled executable installer. Applying the rules can change schemas, indexes, and RLS policies on a live database when the agent has MCP or CLI access.

# Install / update

```text
`npx -y skills@1.5.18 add supabase/agent-skills --skill supabase-postgres-best-practices -g -a claude-code -y --copy`
```

# Citations

[1] [supabase-postgres-best-practices source](https://github.com/supabase/agent-skills/blob/main/skills/supabase-postgres-best-practices/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
