---
type: Agent Skill
title: docx
description: "Create, read, edit, or manipulate Word (.docx) documents — professional formatting, tracked changes, comments, templates, find-and-replace, and image insertion."
resource: "https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md"
tags: [development, installed, documents]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Documents
license: Proprietary
available_in: Cursor and Claude Code
---

Word document create/edit/analyze workflow from Anthropic's document skills pack.

# When to use

Any `.docx` / Word deliverable: reports, memos, letters, templates, tracked changes, comments, or reorganization of existing Word files. Not for PDFs, spreadsheets, or Google Docs.

# Installed at

- `~/.claude/skills/docx/SKILL.md`

# Availability

Cursor and Claude Code

# License

Proprietary (Anthropic document skill terms in `LICENSE.txt`). Use governed by your Anthropic agreement; do not redistribute the skill materials outside authorized use.

# Trust notes

Official Anthropic document skill. Bundles `scripts/` (including office/LibreOffice helpers and comment/accept-changes utilities) that run locally on user documents. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk. May invoke `pandoc` or soffice conversion when the workflow requires it.

# Install / update

```text
npx -y skills@1.5.18 add anthropics/skills --skill docx -g -a claude-code -y --copy
```

# Related

- Sibling document skills: [`pdf`](./pdf.md), [`pptx`](./pptx.md), [`xlsx`](./xlsx.md)
- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [docx source](https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md)
