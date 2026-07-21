---
type: Agent Skill
title: seo-firecrawl
description: "Choose Firecrawl when an audit needs JavaScript-rendered scraping, URL discovery, a site map, broken-link coverage, or a larger crawl than the base fetcher can provide. This extension exposes crawl, map, scrape, and in-site search operations."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/firecrawl/skills/seo-firecrawl/SKILL.md"
tags: [seo, installed]
timestamp: 2026-07-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Choose Firecrawl when an audit needs JavaScript-rendered scraping, URL discovery, a site map, broken-link coverage, or a larger crawl than the base fetcher can provide. This extension exposes crawl, map, scrape, and in-site search operations.

# When to use

Choose Firecrawl when an audit needs JavaScript-rendered scraping, URL discovery, a site map, broken-link coverage, or a larger crawl than the base fetcher can provide. This extension exposes crawl, map, scrape, and in-site search operations.

# Installed at

- `~/.claude/skills/seo-firecrawl/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Requires the Firecrawl extension, MCP server, and service credentials. Calls an external crawling service that sends target URLs and retrieved page content outside the local machine.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-firecrawl -g -a claude-code -y --copy`
```

# Citations

[1] [seo-firecrawl source](https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/firecrawl/skills/seo-firecrawl/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
