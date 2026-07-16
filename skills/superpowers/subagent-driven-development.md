---
type: Agent Skill
title: subagent-driven-development
description: "An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass."
resource: "https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-07-16T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass.

# When to use

An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/subagent-driven-development/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/subagent-driven-development/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Bundles three shell utilities for task briefs, SDD workspace state, and review packages plus several agent prompts. It launches implementers and reviewers and writes `.superpowers/sdd` records; agents must receive non-overlapping scope.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [subagent-driven-development source](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md)
