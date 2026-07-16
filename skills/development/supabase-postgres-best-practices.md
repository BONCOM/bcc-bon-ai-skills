---
type: Agent Skill
title: supabase-postgres-best-practices
description: "Postgres query, schema, index, connection-pooling, and RLS performance work belongs here whether or not the project uses Supabase. Rules are prioritized by impact and include incorrect/correct SQL examples."
resource: "https://github.com/supabase/agent-skills/blob/main/skills/supabase-postgres-best-practices/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Google Cloud
license: MIT
available_in: Cursor and Claude Code
---

Postgres query, schema, index, connection-pooling, and RLS performance work belongs here whether or not the project uses Supabase. Rules are prioritized by impact and include incorrect/correct SQL examples.

# When to use

Postgres query, schema, index, connection-pooling, and RLS performance work belongs here whether or not the project uses Supabase. Rules are prioritized by impact and include incorrect/correct SQL examples.

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
