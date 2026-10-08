---
type: Agent Skill
title: seo-drift
description: "A known-good page baseline lets this skill detect SEO regressions after content or deployment changes. It compares titles, canonicals, robots directives, headings, schema, links, and other critical elements, then keeps a local comparison history."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-drift/SKILL.md"
tags: [seo, installed]
timestamp: 2026-10-04T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

A known-good page baseline lets this skill detect SEO regressions after content or deployment changes. It compares titles, canonicals, robots directives, headings, schema, links, and other critical elements, then keeps a local comparison history.

# When to use

A known-good page baseline lets this skill detect SEO regressions after content or deployment changes. It compares titles, canonicals, robots directives, headings, schema, links, and other critical elements, then keeps a local comparison history.

# Installed at

- `~/.claude/skills/seo-drift/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Fetches target pages and writes baseline and history state through shared scripts. Stored snapshots may contain page metadata and content-derived values; treat the baseline directory as project data.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-drift -g -a claude-code -y --copy`
```

# Citations

[1] [seo-drift source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-drift/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
