---
type: Agent Skill
title: organization-best-practices
description: "Multi-tenant organizations via Better Auth's organization plugin: members, invitations, custom roles/permissions, teams, and RBAC."
resource: "https://github.com/better-auth/skills/blob/main/better-auth/organization/SKILL.md"
tags: [development, installed, auth-better-auth]
timestamp: 2026-09-01T00:00:00Z
category: development
group: Auth (Better Auth)
license: Not declared on the repository (official Better Auth publisher)
available_in: Cursor and Claude Code
---

Multi-tenant organizations via Better Auth's organization plugin: members, invitations, custom roles/permissions, teams, and RBAC.

# When to use

Multi-tenant organizations via Better Auth's organization plugin: members, invitations, custom roles/permissions, teams, and RBAC.

# Installed at

- `~/.claude/skills/organization-best-practices/SKILL.md`
- `~/.agents/skills/organization-best-practices/SKILL.md`

# Availability

Cursor and Claude Code

# License

Not declared on the repository (official Better Auth publisher)

# Trust notes

Instruction-only; schema and authorization changes for org membership. Misconfigured roles can widen access — verify RBAC against the product model.

# Install / update

```text
`npx -y skills@1.5.18 add better-auth/skills --skill organization-best-practices -g -a claude-code -y --copy`
```

# Citations

[1] [organization-best-practices source](https://github.com/better-auth/skills/blob/main/better-auth/organization/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
