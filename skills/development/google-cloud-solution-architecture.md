---
type: Agent Skill
title: google-cloud-solution-architecture
description: "Complex Google Cloud workloads that span products need this broader architecture process for requirement discovery, design choices, validation, and a packaged recommendation. A request about one service should go to a narrower product skill."
resource: "https://github.com/google/skills/blob/main/skills/cloud/google-cloud-solution-architecture/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Complex Google Cloud workloads that span products need this broader architecture process for requirement discovery, design choices, validation, and a packaged recommendation. A request about one service should go to a narrower product skill.

# When to use

Complex Google Cloud workloads that span products need this broader architecture process for requirement discovery, design choices, validation, and a packaged recommendation. A request about one service should go to a narrower product skill.

# Installed at

- `~/.claude/skills/google-cloud-solution-architecture/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only with reference indexes and an output template. Later use can query Google documentation through an MCP and write architecture files only after approval; live documentation is mutable.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill google-cloud-solution-architecture -g -a claude-code -y --copy`
```

# Citations

[1] [google-cloud-solution-architecture source](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-solution-architecture/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
