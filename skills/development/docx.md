---
type: Agent Skill
title: docx
description: "Create, read, edit, or manipulate Word (.docx, .dotx) documents — professional formatting, tracked changes, comments, templates, find-and-replace, and image insertion."
resource: "https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md"
tags: [development, installed, documents]
timestamp: 2026-11-20T00:00:00Z
category: development
group: Documents
license: Apache-2.0
available_in: Cursor, Claude Code, Codex and Antigravity
---

Word document create/edit/analyze workflow from Anthropic's document skills pack.

# When to use

Any `.docx` / `.dotx` Word deliverable: reports, memos, letters, templates, tracked changes, comments, or reorganization of existing Word files. Not for PDFs, spreadsheets, or Google Docs.

# Installed at

- `~/.claude/skills/docx/SKILL.md`
- `~/.agents/skills/docx/SKILL.md`
- `~/.gemini/config/skills/docx` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

Apache-2.0 (since `2c5958e`, 2026-11-06; previously proprietary)

# Trust notes

Official Anthropic document skill. Bundles `scripts/` (including office/LibreOffice helpers and comment/accept-changes utilities) that run locally on user documents. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk. May invoke `pandoc` or soffice conversion when the workflow requires it. 2026-07-17 upstream refresh rewrote the create/edit guidance around `docx-js` gotchas (page size, tables, TOC headings) and added `.dotx` template support. 2026-11-14 (`1780c5e`): moved to the Apache 2.0 license (`2c5958e`, 2026-11-06); every heading level needs its own style, ZIP folder entries are dropped before rendering and repacking uses `zip -XrD` (Word refused files with them through cloud co-editing), and the shared `scripts/office/` validators and redlining checker are rewritten. No new network or install calls; scripts still run locally on user documents. 2026-11-16 (`e4bb5d9`): `scripts/office/soffice.py` renders PDFs and images from a temp copy whose non-web external `.rels` links are cut to `about:blank`, `validate.py` checks the original also unpacks safely, and editing unpacks with Python `zipfile` instead of `unzip` (which restores symlinks) and repacks with `zip -y`. I read both scripts: local only, no network calls.

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
