---
type: Agent Skill
title: seo-content
description: "Content quality, readability, thin-content, and E-E-A-T reviews should use this skill. It applies Google's Who/How/Why test, checks experience and authorship evidence, and scores whether passages are clear enough to cite in search and AI answers."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-content/SKILL.md"
tags: [seo, installed]
timestamp: 2026-11-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
---

Content quality, readability, thin-content, and E-E-A-T reviews should use this skill. It applies Google's Who/How/Why test, checks experience and authorship evidence, and scores whether passages are clear enough to cite in search and AI answers.

# When to use

Content quality, readability, thin-content, and E-E-A-T reviews should use this skill. It applies Google's Who/How/Why test, checks experience and authorship evidence, and scores whether passages are clear enough to cite in search and AI answers.

# Installed at

- `~/.claude/skills/seo-content/SKILL.md`
- `~/.agents/skills/seo-content/SKILL.md`
- `~/.gemini/config/skills/seo-content` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Fetches the target page and uses local reference criteria and scoring scripts. It may consult mutable Google Search documentation; no API key is required for the base review.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-content -g -a claude-code -y --copy`
```

# Citations

[1] [seo-content source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-content/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
