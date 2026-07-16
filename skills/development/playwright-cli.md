---
type: Agent Skill
title: playwright-cli
description: "Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow."
resource: "https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Frontend and UI
license: Apache-2.0
available_in: Cursor and Claude Code
---

Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow.

# When to use

Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow.

# Installed at

- `~/.claude/skills/playwright-cli/SKILL.md`
- `~/.agents/skills/playwright-cli/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Declares Bash access for `playwright-cli`, `npx`, and `npm`. Commands can browse external sites, preserve browser state, capture page content, and write screenshots or traces; confirm the target and data boundary first.

# Install / update

```text
`npx -y skills@1.5.18 add microsoft/playwright-cli --skill playwright-cli -g -a claude-code -y --copy`
```

# Citations

[1] [playwright-cli source](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
