---
type: Agent Skill
title: supply-chain-risk-auditor
description: "Dependency takeover risk is the reason to reach for this skill before a security review. It checks maintenance activity, maintainer concentration, package popularity, and risky capabilities, then writes a focused report; it is not a substitute for a vulnerability or license scanner."
resource: "https://github.com/trailofbits/skills/blob/main/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Development quality
license: CC-BY-SA-4.0
available_in: Cursor and Claude Code
---

Dependency takeover risk is the reason to reach for this skill before a security review. It checks maintenance activity, maintainer concentration, package popularity, and risky capabilities, then writes a focused report; it is not a substitute for a vulnerability or license scanner.

# When to use

Dependency takeover risk is the reason to reach for this skill before a security review. It checks maintenance activity, maintainer concentration, package popularity, and risky capabilities, then writes a focused report; it is not a substitute for a vulnerability or license scanner.

# Installed at

- `~/.claude/skills/supply-chain-risk-auditor/SKILL.md`

# Availability

Cursor and Claude Code

# License

CC-BY-SA-4.0

# Trust notes

Declares Read, Write, Bash, Glob, and Grep; may use authenticated `gh` network calls against public GitHub metadata and writes an audit report. No bundled downloader.

# Install / update

```text
`npx -y skills@1.5.18 add trailofbits/skills --skill supply-chain-risk-auditor -g -a claude-code -y --copy`
```

# Citations

[1] [supply-chain-risk-auditor source](https://github.com/trailofbits/skills/blob/main/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
