---
type: Agent Skill
title: seo-unlighthouse
description: "A local multi-page Lighthouse sweep is useful when PageSpeed quota, CI repeatability, or broad regression coverage matters. This wrapper runs Unlighthouse against a capped route set and aggregates median performance, accessibility, best-practice, and SEO scores."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/unlighthouse/skills/seo-unlighthouse/SKILL.md"
tags: [seo, installed]
timestamp: 2026-09-29T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

A local multi-page Lighthouse sweep is useful when PageSpeed quota, CI repeatability, or broad regression coverage matters. This wrapper runs Unlighthouse against a capped route set and aggregates median performance, accessibility, best-practice, and SEO scores.

# When to use

A local multi-page Lighthouse sweep is useful when PageSpeed quota, CI repeatability, or broad regression coverage matters. This wrapper runs Unlighthouse against a capped route set and aggregates median performance, accessibility, best-practice, and SEO scores.

# Installed at

- `~/.claude/skills/seo-unlighthouse/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Requires Node 18+ and `unlighthouse-cli`; the shared wrapper performs URL safety checks, starts browser processes, crawls the site, and writes JSON and HTML reports. No API key is needed.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-unlighthouse -g -a claude-code -y --copy`
```

# Citations

[1] [seo-unlighthouse source](https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/unlighthouse/skills/seo-unlighthouse/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
