---
type: Agent Skill
title: seo-bing
description: "Bing Webmaster link data, Microsoft Copilot citation eligibility, and IndexNow submission to participating search engines are this extension's focus. It deliberately does not describe IndexNow as a Google indexing mechanism."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/bing-webmaster/skills/seo-bing/SKILL.md"
tags: [seo, installed]
timestamp: 2026-10-04T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Bing Webmaster link data, Microsoft Copilot citation eligibility, and IndexNow submission to participating search engines are this extension's focus. It deliberately does not describe IndexNow as a Google indexing mechanism.

# When to use

Bing Webmaster link data, Microsoft Copilot citation eligibility, and IndexNow submission to participating search engines are this extension's focus. It deliberately does not describe IndexNow as a Google indexing mechanism.

# Installed at

- `~/.claude/skills/seo-bing/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Requires `BING_WEBMASTER_API_KEY`; URL submission also needs a published `INDEXNOW_KEY`. Shared scripts call Bing Webmaster and can submit single or batched URLs to IndexNow, which is a mutable external action.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-bing -g -a claude-code -y --copy`
```

# Citations

[1] [seo-bing source](https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/bing-webmaster/skills/seo-bing/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
