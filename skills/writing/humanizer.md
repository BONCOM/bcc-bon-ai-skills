---
type: Agent Skill
title: humanizer
description: "Remove signs of AI-generated writing from text. Use when editing or reviewing text to make it sound more natural and human-written (humanizer v3.0.0)."
resource: "https://github.com/blader/humanizer/blob/main/SKILL.md"
tags: [writing, installed]
timestamp: 2026-11-20T00:00:00Z
category: writing
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
upstream_version: "4.0.0"
---

Rewrites machine-sounding prose without changing meaning or intended technical voice. v3.0.0 ("Rebuild the skill around one account and 25 patterns ordered by strength") replaces the prior Wikipedia-"Signs of AI writing"-organized ruleset with a single ordered list of 25 patterns (not-X-but-Y contrasts, one-line closers, staged openers, forced triads, dash overuse, inflated claims, sales language, stock AI words, bold labels, filler), realigned against the current Wikipedia article and trimmed of guidance the patterns already imply; the skill was also applied to its own prose. Prior to the rebuild: v2.9.0 added an explicit no-fabrication rule (never invent facts, names, numbers, dates, quotes, or citations absent from the source) and named invocation modes; v2.11.0 was a substantial rewrite pass over the ruleset; v2.11.1/v2.11.2 were packaging and wording follow-ups.

# When to use

Use when editing or reviewing text that should read as human-written — docs, blogs, product copy, or agent drafts.

# Installed at

- `~/.claude/skills/humanizer/SKILL.md`
- `~/.agents/skills/humanizer/SKILL.md`
- `~/.gemini/config/skills/humanizer` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Instruction-only skill with no network calls. As of v2.9.1 the SKILL.md frontmatter dropped the explicit `compatibility`/`allowed-tools` keys as part of a "portability" pass (enforced by a new local `scripts/validate-package.py` release-consistency check, not something that runs during skill use) — the skill still only needs read/write/edit access to the text it's asked to rewrite. It can rewrite the user's files, so scope the input and preserve factual claims and citations. Refreshed 2026-09-21 from upstream v3.0.0 (was v2.11.2, refreshed 2026-08-19) — the metadata block moved from a top-level `version:` string to `metadata.version`; the skill remains instruction-only text rewriting with no bundled network calls or executable scripts. Refreshed 2026-11-14 to v4.0.0 (`8b067c5`, 2026-11-10; the installed copy was 3.1.0): text being edited that contains fake closing tags or "operator"/"system" notes is now treated as material, never as instructions; file mode reads the whole current file first and reports how many sections it reviewed. It also reverses the 2.9.0 no-invention rule: where text is generic it may add a specific detail it knows to be true, while still treating a lost or changed claim as an error. Still instruction-only. Post-4.0.0 `main` (`3d556c3`, `3e5f816`, 2026-11-19, unreleased): informal human text (chat, rants, reviews) keeps its style and a lone tell is not enough to edit it; adds "the part" staging to §4 and an "Overall"/"Ultimately" closer to §2; `scripts/validate-package.py` now fails on repeated pattern numbers.

# Install / update

```text
npx -y skills@1.5.18 add blader/humanizer --skill humanizer -g -a claude-code -y --copy
```

# Related

- Category index: [/skills/writing/index.md](/skills/writing/index.md)

# Citations

[1] [humanizer source](https://github.com/blader/humanizer/blob/main/SKILL.md)
