---
type: Agent Skill
title: subagent-driven-development
description: "An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass."
resource: "https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-11-03T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass.

# When to use

An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/subagent-driven-development/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.2/skills/subagent-driven-development/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Bundles three shell utilities for task briefs, SDD workspace state, and review packages plus several agent prompts. It launches implementers and reviewers and writes `.superpowers/sdd` records; agents must receive non-overlapping scope. v6.3.0 narrows the stop conditions to four named triggers (irreversible/destructive op, security-sensitive action, out-of-worktree side effect, plan defect) and requires every other ambiguity be resolved by a logged ruling rather than a check-in. v7.0.0: `sdd-workspace` no longer overwrites a repo's own `.superpowers/sdd/.gitignore` and keeps plan markers repo-relative on Windows Git Bash. v7.0.1 splits the long-form guidance into `references/` (batching, preflight, fix loop, final review, resuming, handling reports, cannot-verify) so it survives compaction; v7.0.2 adds the `sdd-repo` script, a single source of truth for which working tree the scripts act in, which stops outside a repository instead of guessing from the plan path, and fixes the `review-package`, `sdd-workspace` and `task-brief` helpers.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [subagent-driven-development source](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md)
