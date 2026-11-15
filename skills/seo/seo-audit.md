---
type: Agent Skill
title: seo-audit
description: "A full-site health check belongs here rather than in the single-page skill. The audit crawls up to 500 pages, detects the business type, selects always-on and conditional specialists, calculates a health score, and returns a prioritized action plan."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-audit/SKILL.md"
tags: [seo, installed]
timestamp: 2026-11-14T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

A full-site health check belongs here rather than in the single-page skill. The audit crawls up to 500 pages, detects the business type, selects always-on and conditional specialists, calculates a health score, and returns a prioritized action plan.

# When to use

A full-site health check belongs here rather than in the single-page skill. The audit crawls up to 500 pages, detects the business type, selects always-on and conditional specialists, calculates a health score, and returns a prioritized action plan.

# Installed at

- `~/.claude/skills/seo-audit/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Fetches and crawls the target site with shared Python scripts and may dispatch up to 15 specialists. Conditional checks can use Google, Moz, Bing, DataForSEO, Common Crawl, stored drift baselines, and local report files when configured. v2.6.1 (2026-11-14): headless Chromium runs sandboxed wherever the host allows it; when it cannot, the report says once that the page was rendered without the sandbox, and the agent never sets the sandbox override variables itself.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-audit -g -a claude-code -y --copy`
```

# Citations

[1] [seo-audit source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-audit/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
