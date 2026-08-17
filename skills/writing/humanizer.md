---
type: Agent Skill
title: humanizer
description: "Remove signs of AI-generated writing from text. Use when editing or reviewing text to make it sound more natural and human-written (humanizer v2.11.0)."
resource: "https://github.com/blader/humanizer/blob/main/SKILL.md"
tags: [writing, installed]
timestamp: 2026-08-17T00:00:00Z
category: writing
license: MIT
available_in: Cursor and Claude Code
upstream_version: "2.11.0"
---

Rewrites machine-sounding prose without changing meaning or intended technical voice. Based on Wikipedia’s “Signs of AI writing” guide (WikiProject AI Cleanup). Covers inflated symbolism, promotional tone, vague attribution, em-dash overuse, rule-of-three patterns, AI vocabulary, filler, and related tells; ends with a “what still sounds generated?” self-check. v2.9.0 added an explicit no-fabrication rule (never invent facts, names, numbers, dates, quotes, or citations absent from the source) and named invocation modes that change what gets delivered. v2.11.0 ("Rewrite Humanizer in Plain Language") is a substantial rewrite pass over the ruleset itself, following several point releases between v2.9.1 and v2.11.0 (plugin discovery fix, qualified gated vocabulary rule, shadowboxing/editorial-scar-tissue pattern additions).

# When to use

Use when editing or reviewing text that should read as human-written — docs, blogs, product copy, or agent drafts.

# Installed at

- `~/.claude/skills/humanizer/SKILL.md`
- `~/.agents/skills/humanizer/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only skill with no network calls. As of v2.9.1 the SKILL.md frontmatter dropped the explicit `compatibility`/`allowed-tools` keys as part of a "portability" pass (enforced by a new local `scripts/validate-package.py` release-consistency check, not something that runs during skill use) — the skill still only needs read/write/edit access to the text it's asked to rewrite. It can rewrite the user's files, so scope the input and preserve factual claims and citations. Refreshed 2026-08-17 from upstream v2.11.0 (was v2.9.1).

# Install / update

```text
npx -y skills@1.5.18 add blader/humanizer --skill humanizer -g -a claude-code -y --copy
```

# Related

- Category index: [/skills/writing/index.md](/skills/writing/index.md)

# Citations

[1] [humanizer source](https://github.com/blader/humanizer/blob/main/SKILL.md)
