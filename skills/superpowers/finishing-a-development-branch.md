---
type: Agent Skill
title: finishing-a-development-branch
description: "Branch integration is the final step after implementation and tests are complete. This skill freshly verifies tests, detects whether the workspace is a normal checkout or managed worktree, presents merge, PR, keep, or cleanup choices, and executes only the selected path."
resource: "https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-08-17T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

Branch integration is the final step after implementation and tests are complete. This skill freshly verifies tests, detects whether the workspace is a normal checkout or managed worktree, presents merge, PR, keep, or cleanup choices, and executes only the selected path.

# When to use

Branch integration is the final step after implementation and tests are complete. This skill freshly verifies tests, detects whether the workspace is a normal checkout or managed worktree, presents merge, PR, keep, or cleanup choices, and executes only the selected path.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/finishing-a-development-branch/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.3.0/skills/finishing-a-development-branch/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only, but it runs tests and Git inspection and can merge branches, create a PR, remove a worktree, or delete a branch after the user chooses. Cleanup is not automatic. v6.3.0 adds an explicit refusal path when worktree removal is blocked by modified/untracked files: never force-remove, show the human partner what's at stake and ask.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [finishing-a-development-branch source](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md)
