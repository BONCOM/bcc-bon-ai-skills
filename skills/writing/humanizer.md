---
type: Agent Skill
title: humanizer
description: "Remove signs of AI-generated writing from text. Use when editing or reviewing text to make it sound more natural and human-written (humanizer v2.8.2)."
resource: "https://github.com/blader/humanizer/blob/main/SKILL.md"
tags: [writing, installed]
timestamp: 2026-07-16T00:00:00Z
category: writing
license: MIT
available_in: Cursor and Claude Code
upstream_version: "2.8.2"
---

Rewrites machine-sounding prose without changing meaning or intended technical voice. Based on Wikipedia’s “Signs of AI writing” guide (WikiProject AI Cleanup). Covers inflated symbolism, promotional tone, vague attribution, em-dash overuse, rule-of-three patterns, AI vocabulary, filler, and related tells; ends with a “what still sounds generated?” self-check.

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

Declares Read, Write, Edit, Grep, Glob, and AskUserQuestion; instruction-only with no bundled executable scripts or network calls. It can rewrite the user’s files, so scope the input and preserve factual claims and citations. Refreshed 2026-07-16 from upstream v2.8.2.

# Install / update

```text
npx -y skills@1.5.18 add blader/humanizer --skill humanizer -g -a claude-code -y --copy
```

# Related

- Category index: [/skills/writing/index.md](/skills/writing/index.md)

# Citations

[1] [humanizer source](https://github.com/blader/humanizer/blob/main/SKILL.md)
