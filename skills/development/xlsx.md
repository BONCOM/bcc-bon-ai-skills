---
type: Agent Skill
title: xlsx
description: "Create, read, edit, or clean spreadsheet files (.xlsx, .xlsm, .csv, .tsv) — formulas, formatting, charts, and tabular cleanup when the deliverable is a spreadsheet."
resource: "https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md"
tags: [development, installed, documents]
timestamp: 2026-07-17T00:00:00Z
category: development
group: Documents
license: Proprietary
available_in: Cursor and Claude Code
---

Spreadsheet create/edit/cleanup workflow from Anthropic's document skills pack.

# When to use

When a spreadsheet file is the primary input or output: open/fix existing workbooks, build new models, convert tabular formats, or clean messy CSV/TSV into proper sheets. Do not use when the primary deliverable is Word, HTML, a standalone script, or Google Sheets API work.

# Installed at

- `~/.claude/skills/xlsx/SKILL.md`

# Availability

Cursor and Claude Code

# License

Proprietary (Anthropic document skill terms in `LICENSE.txt`). Use governed by your Anthropic agreement; do not redistribute the skill materials outside authorized use.

# Trust notes

Official Anthropic document skill. Bundles `scripts/` (recalc and office helpers) that run locally against workbook files. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk. Formula recalculation helpers may invoke spreadsheet tooling; keep untrusted files sandboxed. Refreshed 2026-07-17 alongside the shared docx/pptx/xlsx office/ helper rewrite (no scope change for xlsx).

# Install / update

```text
npx -y skills@1.5.18 add anthropics/skills --skill xlsx -g -a claude-code -y --copy
```

# Related

- Sibling document skills: [`pdf`](./pdf.md), [`docx`](./docx.md), [`pptx`](./pptx.md)
- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [xlsx source](https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md)
