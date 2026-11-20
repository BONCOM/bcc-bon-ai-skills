---
type: Agent Skill
title: playwright-cli
description: "Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow."
resource: "https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-11-20T00:00:00Z
category: development
group: Frontend and UI
license: Apache-2.0
available_in: Cursor, Claude Code, Codex and Antigravity
---

Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow.

# When to use

Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow.

# Installed at

- `~/.claude/skills/playwright-cli/SKILL.md`
- `~/.agents/skills/playwright-cli/SKILL.md`
- `~/.gemini/config/skills/playwright-cli` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

Apache-2.0

# Trust notes

Declares Bash access for `playwright-cli`, `npx`, and `npm`. Commands can browse external sites, preserve browser state, capture page content, and write screenshots or traces; confirm the target and data boundary first. 2026-11-05 (`745fbc7`, with `faf6bc5` 2026-10-31, Playwright rolls to 1.65/1.66 alpha): adds `mousewheel` and `tab-new --isolated-context` examples, `cookie-delete --domain`, a clearer `--raw` description (keeps errors and the snapshot), and tracing examples that `open` then `goto`. Documentation only. 2026-11-18 (`a33d9e0`, Playwright 1.66 alpha): attach to the user's own browser profile through the Playwright Extension with named, coloured sessions and `detach --close-tabs`; `npx playwright cli` needs Playwright 1.59+. Treat attaching to the user's profile as using their signed-in sessions.

# Install / update

```text
`npx -y skills@1.5.18 add microsoft/playwright-cli --skill playwright-cli -g -a claude-code -y --copy`
```

# Citations

[1] [playwright-cli source](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
