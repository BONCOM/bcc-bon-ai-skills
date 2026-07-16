---
type: Agent Skill
title: better-auth-best-practices
description: "Better Auth server/client setup, database adapters, sessions, plugins, env vars (`BETTER_AUTH_SECRET`, `BETTER_AUTH_URL`), and CLI migrate/generate workflows belong here."
resource: "https://github.com/better-auth/skills/blob/main/better-auth/best-practices/SKILL.md"
tags: [development, installed, auth-better-auth]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Auth (Better Auth)
license: Not declared on the repository (official Better Auth publisher)
available_in: Cursor and Claude Code
---

Better Auth server/client setup, database adapters, sessions, plugins, env vars (`BETTER_AUTH_SECRET`, `BETTER_AUTH_URL`), and CLI migrate/generate workflows belong here.

# When to use

Better Auth server/client setup, database adapters, sessions, plugins, env vars (`BETTER_AUTH_SECRET`, `BETTER_AUTH_URL`), and CLI migrate/generate workflows belong here.

# Installed at

- `~/.claude/skills/better-auth-best-practices/SKILL.md`
- `~/.agents/skills/better-auth-best-practices/SKILL.md`

# Availability

Cursor and Claude Code

# License

Not declared on the repository (official Better Auth publisher)

# Trust notes

Instruction-only; directs agents to current docs and `@better-auth/cli`. Later use can install packages, write `auth.ts`/route handlers, run migrations, and touch auth secrets. Complements general `security-and-hardening`.

# Install / update

```text
`npx -y skills@1.5.18 add better-auth/skills --skill better-auth-best-practices -g -a claude-code -y --copy`
```

# Citations

[1] [better-auth-best-practices source](https://github.com/better-auth/skills/blob/main/better-auth/best-practices/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
