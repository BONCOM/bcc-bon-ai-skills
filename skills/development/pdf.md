---
type: Agent Skill
title: pdf
description: "Create, read, merge, split, rotate, watermark, encrypt, form-fill, OCR, or otherwise manipulate PDF files. Trigger on any .pdf deliverable or PDF-processing request."
resource: "https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md"
tags: [development, installed, documents]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Documents
license: Proprietary
available_in: Cursor and Claude Code
---

PDF create/edit/extract workflow from Anthropic's document skills pack (pypdf and bundled helper scripts).

# When to use

Any task involving `.pdf` files: extract text/tables, merge/split, rotate, watermarks, form fill, encrypt/decrypt, images, or OCR on scans.

# Installed at

- `~/.claude/skills/pdf/SKILL.md`

# Availability

Cursor and Claude Code

# License

Proprietary (Anthropic document skill terms in `LICENSE.txt`). Use governed by your Anthropic agreement; do not redistribute the skill materials outside authorized use.

# Trust notes

Official Anthropic document skill. Bundles local Python scripts under `scripts/` for forms, validation images, and PDF transforms — they process user-supplied files on the local machine and may pull in Python PDF/image dependencies when run. Skills.sh: Gen Safe, Socket 0 alerts, Snyk High Risk (script surface). Prefer reading `forms.md` / `reference.md` on demand rather than loading everything upfront.

# Install / update

```text
npx -y skills@1.5.18 add anthropics/skills --skill pdf -g -a claude-code -y --copy
```

# Related

- Sibling document skills: [`docx`](./docx.md), [`pptx`](./pptx.md), [`xlsx`](./xlsx.md)
- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [pdf source](https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md)
