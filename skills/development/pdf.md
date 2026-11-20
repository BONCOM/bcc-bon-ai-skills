---
type: Agent Skill
title: pdf
description: "Create, read, merge, split, rotate, watermark, encrypt, form-fill, OCR, or otherwise manipulate PDF files. Trigger on any .pdf deliverable or PDF-processing request."
resource: "https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md"
tags: [development, installed, documents]
timestamp: 2026-11-14T00:00:00Z
category: development
group: Documents
license: Apache-2.0
available_in: Cursor, Claude Code, Codex and Antigravity
---

PDF create/edit/extract workflow from Anthropic's document skills pack (pypdf and bundled helper scripts).

# When to use

Any task involving `.pdf` files: extract text/tables, merge/split, rotate, watermarks, form fill, encrypt/decrypt, images, or OCR on scans.

# Installed at

- `~/.claude/skills/pdf/SKILL.md`
- `~/.agents/skills/pdf/SKILL.md`
- `~/.gemini/config/skills/pdf` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

Apache-2.0 (since `2c5958e`, 2026-11-06; previously proprietary)

# Trust notes

Official Anthropic document skill. Bundles local Python scripts under `scripts/` for forms, validation images, and PDF transforms — they process user-supplied files on the local machine and may pull in Python PDF/image dependencies when run. Skills.sh: Gen Safe, Socket 0 alerts, Snyk High Risk (script surface). Prefer reading `FORMS.md` / `REFERENCE.md` on demand rather than loading everything upfront. 2026-11-14 (`1780c5e`): moved to the Apache 2.0 license (`2c5958e`, 2026-11-06) and `forms.md`/`reference.md` renamed `FORMS.md`/`REFERENCE.md`; instructions otherwise unchanged. This was the first real upstream change since install (earlier hash differences were false positives).

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
