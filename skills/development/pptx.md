---
type: Agent Skill
title: pptx
description: "Create, read, edit, or combine PowerPoint (.pptx) decks — slides, pitch decks, templates, speaker notes, thumbnails, and text extraction."
resource: "https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md"
tags: [development, installed, documents]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Documents
license: Proprietary
available_in: Cursor and Claude Code
---

PowerPoint create/edit/analyze workflow from Anthropic's document skills pack.

# When to use

Any `.pptx` involvement: new decks, edits, templates, speaker notes, combining/splitting, or extracting slide text — even when the extracted content will be used elsewhere.

# Installed at

- `~/.claude/skills/pptx/SKILL.md`

# Availability

Cursor and Claude Code

# License

Proprietary (Anthropic document skill terms in `LICENSE.txt`). Use governed by your Anthropic agreement; do not redistribute the skill materials outside authorized use.

# Trust notes

Official Anthropic document skill. Bundles `scripts/` (thumbnail, unpack, slide helpers) and reference guides (`editing.md`, `pptxgenjs.md`) loaded on demand. Local processing of presentation files; may use markitdown / pptxgenjs / Node tooling when creating or inspecting decks. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk.

# Install / update

```text
npx -y skills@1.5.18 add anthropics/skills --skill pptx -g -a claude-code -y --copy
```

# Related

- Sibling document skills: [`pdf`](./pdf.md), [`docx`](./docx.md), [`xlsx`](./xlsx.md)
- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [pptx source](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md)
