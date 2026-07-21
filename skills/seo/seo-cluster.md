---
type: Agent Skill
title: seo-cluster
description: "Keyword groups based on overlapping Google top-ten results are the input to this skill's hub-and-spoke planning. It produces cluster plans, internal-link matrices, and interactive maps; content creation is optional and separate."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-cluster/SKILL.md"
tags: [seo, installed]
timestamp: 2026-07-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Keyword groups based on overlapping Google top-ten results are the input to this skill's hub-and-spoke planning. It produces cluster plans, internal-link matrices, and interactive maps; content creation is optional and separate.

# When to use

Keyword groups based on overlapping Google top-ten results are the input to this skill's hub-and-spoke planning. It produces cluster plans, internal-link matrices, and interactive maps; content creation is optional and separate.

# Installed at

- `~/.claude/skills/seo-cluster/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Uses shared scripts and live SERP data to compare result overlap, then writes planning and visualization artifacts. Optional execution delegates to `claude-blog` only if that separate tool is installed.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-cluster -g -a claude-code -y --copy`
```

# Citations

[1] [seo-cluster source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-cluster/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
