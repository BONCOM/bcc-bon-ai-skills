---
type: Agent Skill
title: seo-maps
description: "Maps-platform evidence is separate from the on-page work in `seo-local`. This skill supports geo-grid rank scans, GBP audits, review velocity, cross-platform NAP checks, competitor-radius mapping, Share of Local Voice, and LocalBusiness schema derived from API data."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-maps/SKILL.md"
tags: [seo, installed]
timestamp: 2026-11-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
---

Maps-platform evidence is separate from the on-page work in `seo-local`. This skill supports geo-grid rank scans, GBP audits, review velocity, cross-platform NAP checks, competitor-radius mapping, Share of Local Voice, and LocalBusiness schema derived from API data.

# When to use

Maps-platform evidence is separate from the on-page work in `seo-local`. This skill supports geo-grid rank scans, GBP audits, review velocity, cross-platform NAP checks, competitor-radius mapping, Share of Local Voice, and LocalBusiness schema derived from API data.

# Installed at

- `~/.claude/skills/seo-maps/SKILL.md`
- `~/.agents/skills/seo-maps/SKILL.md`
- `~/.gemini/config/skills/seo-maps` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Free checks call Overpass and Geoapify; advanced tiers use paid DataForSEO MCP and optional Google Maps API credentials. Geo-grid scans and review lookups are live external requests with vendor quotas. v2.6.2 (2026-11-14): subagents have no MCP tools, so paid DataForSEO maps data must be fetched first and passed in.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-maps -g -a claude-code -y --copy`
```

# Citations

[1] [seo-maps source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-maps/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
