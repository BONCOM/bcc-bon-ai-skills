---
type: Agent Skill
title: better-auth-security-best-practices
description: "Hardening an existing Better Auth deployment: rate limiting, secrets, CSRF, trusted origins, session/cookie security, OAuth token encryption, IP tracking, and audit logging."
resource: "https://github.com/better-auth/skills/blob/main/security/SKILL.md"
tags: [development, installed, auth-better-auth]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Auth (Better Auth)
license: Not declared on the repository (official Better Auth publisher)
available_in: Cursor and Claude Code
---

Hardening an existing Better Auth deployment: rate limiting, secrets, CSRF, trusted origins, session/cookie security, OAuth token encryption, IP tracking, and audit logging.

# When to use

Hardening an existing Better Auth deployment: rate limiting, secrets, CSRF, trusted origins, session/cookie security, OAuth token encryption, IP tracking, and audit logging.

# Installed at

- `~/.claude/skills/better-auth-security-best-practices/SKILL.md`
- `~/.agents/skills/better-auth-security-best-practices/SKILL.md`

# Availability

Cursor and Claude Code

# License

Not declared on the repository (official Better Auth publisher)

# Trust notes

Instruction-only; changes auth security configuration and secret handling. Prefer over generic advice when the stack is Better Auth.

# Install / update

```text
`npx -y skills@1.5.18 add better-auth/skills --skill better-auth-security-best-practices -g -a claude-code -y --copy`
```

# Citations

[1] [better-auth-security-best-practices source](https://github.com/better-auth/skills/blob/main/security/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
