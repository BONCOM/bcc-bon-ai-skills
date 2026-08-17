---
type: Agent Skill
title: receiving-code-review
description: "Review feedback should pass through this technical check before implementation, particularly when a suggestion is ambiguous or may not fit the codebase. The skill separates understanding from agreement, verifies the claim, and supports reasoned pushback before applying one change at a time."
resource: "https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-08-17T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

Review feedback should pass through this technical check before implementation, particularly when a suggestion is ambiguous or may not fit the codebase. The skill separates understanding from agreement, verifies the claim, and supports reasoned pushback before applying one change at a time.

# When to use

Review feedback should pass through this technical check before implementation, particularly when a suggestion is ambiguous or may not fit the codebase. The skill separates understanding from agreement, verifies the claim, and supports reasoned pushback before applying one change at a time.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/receiving-code-review/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/receiving-code-review/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts or external service. Subsequent implementation still edits and tests the reviewed code, but the skill itself adds a verification gate before those changes.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [receiving-code-review source](https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md)
