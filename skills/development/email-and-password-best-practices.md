---
type: Agent Skill
title: email-and-password-best-practices
description: "Email/password auth with Better Auth: verification, password reset, password policies, and hashing customization."
resource: "https://github.com/better-auth/skills/blob/main/better-auth/emailAndPassword/SKILL.md"
tags: [development, installed, auth-better-auth]
timestamp: 2026-09-01T00:00:00Z
category: development
group: Auth (Better Auth)
license: Not declared on the repository (official Better Auth publisher)
available_in: Cursor and Claude Code
---

Email/password auth with Better Auth: verification, password reset, password policies, and hashing customization.

# When to use

Email/password auth with Better Auth: verification, password reset, password policies, and hashing customization.

# Installed at

- `~/.claude/skills/email-and-password-best-practices/SKILL.md`
- `~/.agents/skills/email-and-password-best-practices/SKILL.md`

# Availability

Cursor and Claude Code

# License

Not declared on the repository (official Better Auth publisher)

# Trust notes

Instruction-only; affects credential flows and may require email provider credentials. Do not weaken hashing or skip verification without an explicit product decision.

# Install / update

```text
`npx -y skills@1.5.18 add better-auth/skills --skill email-and-password-best-practices -g -a claude-code -y --copy`
```

# Citations

[1] [email-and-password-best-practices source](https://github.com/better-auth/skills/blob/main/better-auth/emailAndPassword/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
