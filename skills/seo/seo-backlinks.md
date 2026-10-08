---
type: Agent Skill
title: seo-backlinks
description: "Referring-domain analysis, anchor distribution, toxic-link review, link gaps, new or lost links, and disavow evidence are handled here. The skill merges Common Crawl and a verification crawler with optional Moz, Bing Webmaster, Ahrefs, or DataForSEO data instead of pretending one source is complete."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-backlinks/SKILL.md"
tags: [seo, installed]
timestamp: 2026-10-04T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Referring-domain analysis, anchor distribution, toxic-link review, link gaps, new or lost links, and disavow evidence are handled here. The skill merges Common Crawl and a verification crawler with optional Moz, Bing Webmaster, Ahrefs, or DataForSEO data instead of pretending one source is complete.

# When to use

Referring-domain analysis, anchor distribution, toxic-link review, link gaps, new or lost links, and disavow evidence are handled here. The skill merges Common Crawl and a verification crawler with optional Moz, Bing Webmaster, Ahrefs, or DataForSEO data instead of pretending one source is complete.

# Installed at

- `~/.claude/skills/seo-backlinks/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Shared scripts can read Moz and Bing credentials, query Common Crawl, crawl backlink URLs, and call DataForSEO when its MCP is connected. Network access is intrinsic; disavow output remains a recommendation, not an automatic submission.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-backlinks -g -a claude-code -y --copy`
```

# Citations

[1] [seo-backlinks source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-backlinks/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
