---
type: Agent Skill
title: seo-images
description: "Existing image assets can be checked for alt text, dimensions, formats, responsive sources, lazy loading, CLS risk, file size, metadata, and search visibility. The same skill can plan or run WebP/AVIF conversion and IPTC/XMP updates when local files are supplied."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-images/SKILL.md"
tags: [seo, installed]
timestamp: 2026-11-20T00:00:00Z
category: seo
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
---

Existing image assets can be checked for alt text, dimensions, formats, responsive sources, lazy loading, CLS risk, file size, metadata, and search visibility. The same skill can plan or run WebP/AVIF conversion and IPTC/XMP updates when local files are supplied.

# When to use

Existing image assets can be checked for alt text, dimensions, formats, responsive sources, lazy loading, CLS risk, file size, metadata, and search visibility. The same skill can plan or run WebP/AVIF conversion and IPTC/XMP updates when local files are supplied.

# Installed at

- `~/.claude/skills/seo-images/SKILL.md`
- `~/.agents/skills/seo-images/SKILL.md`
- `~/.gemini/config/skills/seo-images` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Fetches pages and image URLs; file-optimization scripts can rewrite local image files and metadata, so preserve originals. Image SERP ranking checks use DataForSEO only when that paid extension is connected. v2.6.0: `parse_html.py --probe-images` fetches each image with a browser `Accept` header and reports the format actually served, so WebP/AVIF served from a `.jpg` URL is no longer flagged for conversion.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-images -g -a claude-code -y --copy`
```

# Citations

[1] [seo-images source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-images/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
