---
type: Agent Skill
title: using-git-worktrees
description: "Plan execution and isolated feature work can use this worktree setup. It first detects managed worktrees and submodules, prefers the platform's native isolation, and falls back to Git only after checking location, ignore rules, branch state, and project setup."
resource: "https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-07-16T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

Plan execution and isolated feature work can use this worktree setup. It first detects managed worktrees and submodules, prefers the platform's native isolation, and falls back to Git only after checking location, ignore rules, branch state, and project setup.

# When to use

Plan execution and isolated feature work can use this worktree setup. It first detects managed worktrees and submodules, prefers the platform's native isolation, and falls back to Git only after checking location, ignore rules, branch state, and project setup.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/using-git-worktrees/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/using-git-worktrees/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only, but it runs Git commands and can create a branch, directory, and linked worktree. It asks for consent when no isolation preference exists and avoids nesting a worktree inside an already managed worktree.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [using-git-worktrees source](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md)
