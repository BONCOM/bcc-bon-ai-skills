---
type: Agent Skill
title: supabase
description: "Any Supabase product work should start here: Auth, RLS, Data API grants, Edge Functions, Storage, migrations, CLI, and the Supabase MCP. It requires checking current docs/changelog before implementing because APIs and config change between versions."
resource: "https://github.com/supabase/agent-skills/blob/main/skills/supabase/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-09-28T00:00:00Z
category: development
group: Google Cloud
license: MIT
available_in: Cursor and Claude Code
---

Any Supabase product work should start here: Auth, RLS, Data API grants, Edge Functions, Storage, migrations, CLI, and the Supabase MCP. It requires checking current docs/changelog before implementing because APIs and config change between versions.

# When to use

Any Supabase product work should start here: Auth, RLS, Data API grants, Edge Functions, Storage, migrations, CLI, and the Supabase MCP. It requires checking current docs/changelog before implementing because APIs and config change between versions.

# Installed at

- `~/.claude/skills/supabase/SKILL.md`
- `~/.agents/skills/supabase/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only with a security checklist and MCP troubleshooting. Later use can call the authenticated Supabase MCP, CLI, or docs fetches; it can change schemas, RLS, and auth configuration on live projects. Prefer `supabase-postgres-best-practices` for pure SQL performance review. Adds a new "Debugging" section: on any Supabase error/RLS-block/unexpected result it must fetch the upstream Monitoring and Debugging docs before diagnosing rather than working from memory; description gains matching debugging/logs triggers.

# Install / update

```text
`npx -y skills@1.5.18 add supabase/agent-skills --skill supabase -g -a claude-code -y --copy`
```

# Citations

[1] [supabase source](https://github.com/supabase/agent-skills/blob/main/skills/supabase/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
