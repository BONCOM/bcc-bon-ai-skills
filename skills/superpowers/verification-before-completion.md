---
type: Agent Skill
title: verification-before-completion
description: "Completion, fix, pass, and merge-readiness claims need this evidence gate. It identifies the command that proves the claim, runs it fresh and in full, reads the result and exit status, and reports the actual state when evidence disagrees."
resource: "https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-07-16T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

Completion, fix, pass, and merge-readiness claims need this evidence gate. It identifies the command that proves the claim, runs it fresh and in full, reads the result and exit status, and reports the actual state when evidence disagrees.

# When to use

Completion, fix, pass, and merge-readiness claims need this evidence gate. It identifies the command that proves the claim, runs it fresh and in full, reads the result and exit status, and reports the actual state when evidence disagrees.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/verification-before-completion/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/verification-before-completion/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts. It runs project-specific verification commands and reads their complete output but does not define a universal test runner.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [verification-before-completion source](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)
