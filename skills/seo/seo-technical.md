---
type: Agent Skill
title: seo-technical
description: "Crawlability, indexability, URL structure, mobile behavior, security headers, JavaScript rendering, structured data, Core Web Vitals, and IndexNow checks form this technical audit. The skill keeps those findings separate from content strategy and records which crawler or protocol each rule affects."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-technical/SKILL.md"
tags: [seo, installed]
timestamp: 2026-11-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
---

Crawlability, indexability, URL structure, mobile behavior, security headers, JavaScript rendering, structured data, Core Web Vitals, and IndexNow checks form this technical audit. The skill keeps those findings separate from content strategy and records which crawler or protocol each rule affects.

# When to use

Crawlability, indexability, URL structure, mobile behavior, security headers, JavaScript rendering, structured data, Core Web Vitals, and IndexNow checks form this technical audit. The skill keeps those findings separate from content strategy and records which crawler or protocol each rule affects.

# Installed at

- `~/.claude/skills/seo-technical/SKILL.md`
- `~/.agents/skills/seo-technical/SKILL.md`
- `~/.gemini/config/skills/seo-technical` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Crawls public URLs, headers, robots files, sitemaps, and rendered pages through shared scripts. Field performance data and IndexNow submission require separate configured services; the base audit does not submit changes. v2.5.0 (2026-10-22) adds a read-only server-stack CVE exposure check (`references/stack-cve-exposure.md`, currently the 2026-10-21 PHP critical-RCE advisory): it reads only headers and markup from the normal response, never fuzzes or sends payloads, and asks whether the user owns the site before requesting any other path. v2.6.2 (2026-11-14) can trust a named local sandbox proxy through `CLAUDE_SEO_TRUSTED_PROXIES`; audit targets, redirects and rendered-page requests must still be public, and link-local and cloud metadata addresses stay refused.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-technical -g -a claude-code -y --copy`
```

# Citations

[1] [seo-technical source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-technical/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
