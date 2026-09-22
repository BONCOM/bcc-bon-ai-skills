---
type: Agent Skill
title: two-factor-authentication-best-practices
description: "Better Auth `twoFactor` plugin: TOTP, email/SMS OTP, backup codes, trusted devices, and 2FA sign-in flows."
resource: "https://github.com/better-auth/skills/blob/main/better-auth/twoFactor/SKILL.md"
tags: [development, installed, auth-better-auth]
timestamp: 2026-09-01T00:00:00Z
category: development
group: Auth (Better Auth)
license: Not declared on the repository (official Better Auth publisher)
available_in: Cursor and Claude Code
---

Better Auth `twoFactor` plugin: TOTP, email/SMS OTP, backup codes, trusted devices, and 2FA sign-in flows.

# When to use

Better Auth `twoFactor` plugin: TOTP, email/SMS OTP, backup codes, trusted devices, and 2FA sign-in flows.

# Installed at

- `~/.claude/skills/two-factor-authentication-best-practices/SKILL.md`
- `~/.agents/skills/two-factor-authentication-best-practices/SKILL.md`

# Availability

Cursor and Claude Code

# License

Not declared on the repository (official Better Auth publisher)

# Trust notes

Instruction-only; involves MFA secrets and recovery codes. SMS/email OTP needs a messaging provider; keep backup-code handling out of logs and clients.

# Install / update

```text
`npx -y skills@1.5.18 add better-auth/skills --skill two-factor-authentication-best-practices -g -a claude-code -y --copy`
```

# Citations

[1] [two-factor-authentication-best-practices source](https://github.com/better-auth/skills/blob/main/better-auth/twoFactor/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
