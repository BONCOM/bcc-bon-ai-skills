---
type: Agent Skill
title: playwright-best-practices
description: "Playwright test design and maintenance are covered in depth: reliable locators, fixtures, page objects, authentication, API mocking, visual checks, CI, accessibility, security, performance, and hard-to-test browser behavior. Its reference set is broad enough to route a specific test problem without "
resource: "https://github.com/currents-dev/playwright-best-practices-skill/blob/main/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-11-08T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
---

Playwright test design and maintenance are covered in depth: reliable locators, fixtures, page objects, authentication, API mocking, visual checks, CI, accessibility, security, performance, and hard-to-test browser behavior. Its reference set is broad enough to route a specific test problem without loading every topic.

# When to use

Playwright test design and maintenance are covered in depth: reliable locators, fixtures, page objects, authentication, API mocking, visual checks, CI, accessibility, security, performance, and hard-to-test browser behavior. Its reference set is broad enough to route a specific test problem without loading every topic.

# Installed at

- `~/.claude/skills/playwright-best-practices/SKILL.md`
- `~/.agents/skills/playwright-best-practices/SKILL.md`
- `~/.gemini/config/skills/playwright-best-practices` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Bundles Markdown references and a validation workflow, not runtime scripts. Following examples can open browsers, contact test services, use environment credentials, or update snapshots, so set the target and test-data boundary first. 2026-11-08 (`8ce85b0`, `0b75b58`): reference paths and Playwright API examples corrected across 29 reference files, keyboard shortcuts tested without a prior click, and a Browser Executable Missing section (`npx playwright install --dry-run`, install only the browsers the tests use). Docs only.

# Install / update

```text
`npx -y skills@1.5.18 add currents-dev/playwright-best-practices-skill --skill playwright-best-practices -g -a claude-code -y --copy`
```

# Citations

[1] [playwright-best-practices source](https://github.com/currents-dev/playwright-best-practices-skill/blob/main/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
