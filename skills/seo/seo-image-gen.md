---
type: Agent Skill
title: seo-image-gen
description: "An Open Graph preview, hero, product image, infographic, schema image, or thumbnail is a generation task for this extension. It maps the asset type to aspect ratio and resolution, then delegates generation through the Banana creative pipeline."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-image-gen/SKILL.md"
tags: [seo, installed]
timestamp: 2026-09-10T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

An Open Graph preview, hero, product image, infographic, schema image, or thumbnail is a generation task for this extension. It maps the asset type to aspect ratio and resolution, then delegates generation through the Banana creative pipeline.

# When to use

An Open Graph preview, hero, product image, infographic, schema image, or thumbnail is a generation task for this extension. It maps the asset type to aspect ratio and resolution, then delegates generation through the Banana creative pipeline.

# Installed at

- `~/.claude/skills/seo-image-gen/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Requires the Banana extension, nanobanana MCP server, and Gemini image-generation access. Prompts and reference material are sent to an external model, and generated image files are written locally; the audit agent does not auto-generate.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-image-gen -g -a claude-code -y --copy`
```

# Citations

[1] [seo-image-gen source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-image-gen/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
