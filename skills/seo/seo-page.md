---
type: Agent Skill
title: seo-page
description: "One URL is the unit of work for this analysis. It checks title and heading structure, content depth, canonicals and robots directives, social metadata, schema, images, internal links, and page-level performance without turning the request into a site crawl."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-page/SKILL.md"
tags: [seo, installed]
timestamp: 2026-11-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

One URL is the unit of work for this analysis. It checks title and heading structure, content depth, canonicals and robots directives, social metadata, schema, images, internal links, and page-level performance without turning the request into a site crawl.

# When to use

One URL is the unit of work for this analysis. It checks title and heading structure, content depth, canonicals and robots directives, social metadata, schema, images, internal links, and page-level performance without turning the request into a site crawl.

# Installed at

- `~/.claude/skills/seo-page/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Fetches the requested URL and its linked assets, then runs local parsing and scoring. Performance or field-data enrichment may call other configured SEO services, but the base analysis needs no credential. v2.6.0 (2026-11-10) runs a bundled `page_checks.py` first: 47 deterministic on-page checks (title, headings, canonical/robots, document basics, images, links, URL, size, social/schema, content) returned as JSON findings with stable ids, so the model no longer counts them by hand. Works on a live URL or saved HTML.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-page -g -a claude-code -y --copy`
```

# Citations

[1] [seo-page source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-page/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
