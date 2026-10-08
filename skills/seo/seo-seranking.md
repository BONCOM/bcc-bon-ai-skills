---
type: Agent Skill
title: seo-seranking
description: "SE Ranking supplies live AI Share of Voice across ChatGPT, Gemini, Perplexity, Google AI Overviews, and AI Mode, along with SERP, backlink, and competitor data. This skill reports each platform separately with sample-size context."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/seranking/skills/seo-seranking/SKILL.md"
tags: [seo, installed]
timestamp: 2026-10-04T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

SE Ranking supplies live AI Share of Voice across ChatGPT, Gemini, Perplexity, Google AI Overviews, and AI Mode, along with SERP, backlink, and competitor data. This skill reports each platform separately with sample-size context.

# When to use

SE Ranking supplies live AI Share of Voice across ChatGPT, Gemini, Perplexity, Google AI Overviews, and AI Mode, along with SERP, backlink, and competitor data. This skill reports each platform separately with sample-size context.

# Installed at

- `~/.claude/skills/seo-seranking/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Requires `SERANKING_API_KEY` and the SE Ranking extension. Live REST calls send brand, prompt, keyword, or domain inputs to a paid vendor and consume its quota.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-seranking -g -a claude-code -y --copy`
```

# Citations

[1] [seo-seranking source](https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/seranking/skills/seo-seranking/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
