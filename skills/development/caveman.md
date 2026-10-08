---
type: Agent Skill
title: caveman
description: "Ultra-compressed communication mode — cuts narration while keeping technical facts, code, commands, and errors exact. Intensity levels: lite, full, ultra (plus wenyan variants). Invoke with /caveman or 'talk like caveman'; say 'normal mode' to exit."
resource: "https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md"
tags: [development, installed, workflow]
timestamp: 2026-10-08T00:00:00Z
category: development
group: Workflow and discovery
license: MIT
available_in: Cursor and Claude Code
---

Token-efficient reply style: drop filler, keep every technical fact. Optional intensity levels including wenyan variants.

# When to use

When the user asks for caveman mode, fewer tokens, or `/caveman`. Exit on "normal mode". Do not force this style on formal docs, legal text, or user-facing copy unless requested.

# Installed at

- `~/.claude/skills/caveman/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Installed as the single named skill only (`caveman`) — sibling skills (`caveman-commit`, `cavecrew`, etc.) and the repo's Claude Code plugin/hooks were not installed. Instruction + README; no bundled executable scripts in the skill directory. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Low Risk. Style-only; does not change how code or commands are written. Picked up a negation-safety rule (never drop not/never/no/only/except), a no-narration rule for tool calls, an explicit `off` switch, and tighter guardrails on when to preserve grammar particles vs. drop articles. Now also forbids ADDING words to sound more "caveman" (compression only, never style that grows output) and treats "open a defect"/"file a bug" the same as "open issue" — body stays normal prose since it's read by other humans. Refreshed 2026-08-19: bundled README softened its published "65% token reduction" claim to "result depends on model and workload; no aggregate reduction or quality-equivalence claim is published" and dropped the wenyan-full "80-90% character reduction" figure — documentation wording only, no change to `SKILL.md` itself. Refreshed 2026-09-21 (upstream commits `b433570`→`8801144`, 2026-08-23 to 2026-09-08): rewrote the ruleset's framing clauses and shortened skill descriptions to fit the listing budget; added a permanent clarity register that always mixes in ASD-STE100 Simplified Technical English (one idea per sentence, ~20-word cap, active voice, one term per concept, imperative instructions, 3-word noun-cluster max — clarity wins on conflict with caveman's own compression); and added a reply-language rule (follow an explicit user/project language instruction over the dominant conversation language, apply it to every emitted line not just the final reply, and always keep code/CLI/API/error strings verbatim). The same refresh also pulled in `82d2a60` (2026-09-20), a one-line fix to the bundled `README.md`'s ultra-mode example that replaces its `→` arrows with commas — the arrows read as literal style guidance rather than as prose shorthand. Documentation example only; `SKILL.md` unchanged by that commit.

# Install / update

```text
npx -y skills@1.5.18 add JuliusBrussee/caveman --skill caveman -g -a claude-code -y --copy
```

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [caveman source](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md)
