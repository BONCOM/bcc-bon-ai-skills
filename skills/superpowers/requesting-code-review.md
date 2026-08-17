---
type: Agent Skill
title: requesting-code-review
description: "A completed plan task, major feature, or pending merge is the point to request this review. The skill gives a fresh reviewer precise requirements and a bounded Git range rather than the author's full session history, then classifies findings by severity."
resource: "https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-08-17T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

A completed plan task, major feature, or pending merge is the point to request this review. The skill gives a fresh reviewer precise requirements and a bounded Git range rather than the author's full session history, then classifies findings by severity.

# When to use

A completed plan task, major feature, or pending merge is the point to request this review. The skill gives a fresh reviewer precise requirements and a bounded Git range rather than the author's full session history, then classifies findings by severity.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/requesting-code-review/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/requesting-code-review/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Bundles a reviewer prompt, reads Git SHAs, and dispatches a general-purpose subagent. It does not post to a remote review service or modify a pull request by itself. v6.3.0 updates the bundled `code-reviewer.md` prompt (SKILL.md itself unchanged).

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [requesting-code-review source](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md)
