---
type: Agent Skill
title: writing-plans
description: "An approved design or multi-step requirement becomes an implementation handoff through this skill. It maps file responsibilities, splits work into independently reviewable tasks, records the decisions an implementer needs (signatures, test assertions, spec values), and saves the plan under `docs/superpowers/plans`."
resource: "https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-10-10T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

An approved design or multi-step requirement becomes an implementation handoff through this skill. It maps file responsibilities, splits work into independently reviewable tasks, records the decisions an implementer needs (signatures, test assertions, spec values), and saves the plan under `docs/superpowers/plans`.

# When to use

An approved design or multi-step requirement becomes an implementation handoff through this skill. It maps file responsibilities, splits work into independently reviewable tasks, records the decisions an implementer needs (signatures, test assertions, spec values), and saves the plan under `docs/superpowers/plans`.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/writing-plans/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.0/skills/writing-plans/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only. It reads project context and writes a plan; it does not implement the planned code. v6.3.0 adds a required "Spec" field pointing to the design doc. v6.4.2 makes plans record decisions rather than transcribe code (bodies only where signatures and spec values don't determine the algorithm), adds a self-review check on plan length versus spec, and drops the unused `plan-document-reviewer-prompt.md`.

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [writing-plans source](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md)
