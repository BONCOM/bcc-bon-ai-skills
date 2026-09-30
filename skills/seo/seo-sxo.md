---
type: Agent Skill
title: seo-sxo
description: "A technically sound page can still target the wrong intent or page type; this skill tests that mismatch. It reads the SERP backward, derives user stories from ranked results, scores the page through several personas, and can produce a wireframe tied to observed intent."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-sxo/SKILL.md"
tags: [seo, installed]
timestamp: 2026-09-29T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

A technically sound page can still target the wrong intent or page type; this skill tests that mismatch. It reads the SERP backward, derives user stories from ranked results, scores the page through several personas, and can produce a wireframe tied to observed intent.

# When to use

A technically sound page can still target the wrong intent or page type; this skill tests that mismatch. It reads the SERP backward, derives user stories from ranked results, scores the page through several personas, and can produce a wireframe tied to observed intent.

# Installed at

- `~/.claude/skills/seo-sxo/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Fetches the target page and needs live Google SERP evidence, either through available search tools or an SEO data extension. Persona scores are heuristic and should retain cited result evidence.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-sxo -g -a claude-code -y --copy`
```

# Citations

[1] [seo-sxo source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-sxo/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
