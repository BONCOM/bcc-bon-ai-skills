---
type: Agent Skill
title: pptx
description: "Create, read, edit, or combine PowerPoint (.pptx, .potx) decks — slides, pitch decks, templates, speaker notes, thumbnails, and text extraction."
resource: "https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md"
tags: [development, installed, documents]
timestamp: 2026-11-20T00:00:00Z
category: development
group: Documents
license: Apache-2.0
available_in: Cursor, Claude Code, Codex and Antigravity
---

PowerPoint create/edit/analyze workflow from Anthropic's document skills pack.

# When to use

Any `.pptx` / `.potx` involvement: new decks, edits, templates, speaker notes, combining/splitting, or extracting slide text — even when the extracted content will be used elsewhere.

# Installed at

- `~/.claude/skills/pptx/SKILL.md`
- `~/.agents/skills/pptx/SKILL.md`
- `~/.gemini/config/skills/pptx` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

Apache-2.0 (since `2c5958e`, 2026-11-06; previously proprietary)

# Trust notes

Official Anthropic document skill. Bundles `scripts/` (thumbnail, unpack, slide helpers) and reference guides (`editing.md`, `pptxgenjs.md`) loaded on demand. Local processing of presentation files; may use markitdown / pptxgenjs / Node tooling when creating or inspecting decks. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk. 2026-07-17 upstream refresh added `.potx` template support and shares the same office/ helper rewrite as the docx and xlsx skills. 2026-11-14 (`1780c5e`): moved to the Apache 2.0 license (`2c5958e`, 2026-11-06). New decks are built as structured decks by default (theme, layouts, named placeholders, sections, scheme colors). Two new local scripts: `scripts/slide_text.py` (python-pptx text dump, replaces `markitdown`) and `scripts/apply_theme.js` (rewrites the deck's theme colors after `pres.writeFile()`, loads jszip from beside pptxgenjs and never from the working directory). Adds deck content-and-flow guidance and required content and visual QA. No network calls. 2026-11-16 (`e4bb5d9`): `scripts/office/soffice.py` renders PDFs and images from a temp copy whose non-web external `.rels` links are cut to `about:blank`, `validate.py` checks the original also unpacks safely, and editing unpacks with Python `zipfile` instead of `unzip` (which restores symlinks) and repacks with `zip -y`. I read both scripts: local only, no network calls.

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
