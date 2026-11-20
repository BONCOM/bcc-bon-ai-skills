---
type: Agent Skill
title: seo-google
description: "Search Console, PageSpeed Insights, CrUX history, sitemap status, GA4 organic traffic, and the Indexing API are routed through this skill. It adds Google's own measurements and index state to crawler-based observations."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-google/SKILL.md"
tags: [seo, installed]
timestamp: 2026-11-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
---

Search Console, PageSpeed Insights, CrUX history, sitemap status, GA4 organic traffic, and the Indexing API are routed through this skill. It adds Google's own measurements and index state to crawler-based observations.

# When to use

Search Console, PageSpeed Insights, CrUX history, sitemap status, GA4 organic traffic, and the Indexing API are routed through this skill. It adds Google's own measurements and index state to crawler-based observations.

# Installed at

- `~/.claude/skills/seo-google/SKILL.md`
- `~/.agents/skills/seo-google/SKILL.md`
- `~/.gemini/config/skills/seo-google` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Shared scripts read configuration from `~/.config/claude-seo/google-api.json` and call Google APIs with API keys, OAuth, or service-account credentials. URL inspection and Indexing API operations have quotas; submission is a mutable external action. v2.6.1 (2026-11-14): OAuth sign-in is read-only by default, with the Indexing scope only on request (`google_auth.py --auth --indexing`). GSC and GA4 scripts take `--domain <audited-domain>`, look up that site's property from a per-site `sites` map, and refuse another site's property. v2.6.2 (2026-11-14) rewrites `references/auth-setup.md`.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-google -g -a claude-code -y --copy`
```

# Citations

[1] [seo-google source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-google/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
