---
type: Agent Skill
title: security-and-hardening
description: "Security-sensitive code belongs under this skill when it accepts untrusted input, handles authentication or sessions, stores private data, or calls an external service. The workflow starts with trust boundaries and a short threat model, then applies concrete controls for validation, authorization, s"
resource: "https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-08-17T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

Security-sensitive code belongs under this skill when it accepts untrusted input, handles authentication or sessions, stores private data, or calls an external service. The workflow starts with trust boundaries and a short threat model, then applies concrete controls for validation, authorization, secrets, uploads, webhooks, and data handling.

# When to use

Security-sensitive code belongs under this skill when it accepts untrusted input, handles authentication or sessions, stores private data, or calls an external service. The workflow starts with trust boundaries and a short threat model, then applies concrete controls for validation, authorization, secrets, uploads, webhooks, and data handling.

# Installed at

- `~/.claude/skills/security-and-hardening/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts. Its examples mention package-manager audits and external security services, but the package does not call them automatically. Fixed a broken relative link to `references/` (was resolving one directory too shallow). Adds a new "Data Privacy & Compliance" section distinguishing security ("can an attacker read it") from privacy ("should we hold it at all") and widens the trigger description to cover GDPR/CCPA-relevant work.

# Install / update

```text
`npx -y skills@1.5.18 add addyosmani/agent-skills --skill security-and-hardening -g -a claude-code -y --copy`
```

# Citations

[1] [security-and-hardening source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
