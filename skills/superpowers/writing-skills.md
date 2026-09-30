---
type: Agent Skill
title: writing-skills
description: "Agent skill authoring, revision, and verification use pressure tests here rather than prose review alone. The workflow captures baseline failures, writes the smallest instruction that changes behavior, reruns scenarios, and closes newly observed loopholes."
resource: "https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md"
tags: [superpowers, installed, plugin]
timestamp: 2026-09-19T00:00:00Z
category: superpowers
license: MIT
available_in: Cursor and Claude Code
---

Agent skill authoring, revision, and verification use pressure tests here rather than prose review alone. The workflow captures baseline failures, writes the smallest instruction that changes behavior, reruns scenarios, and closes newly observed loopholes.

# When to use

Agent skill authoring, revision, and verification use pressure tests here rather than prose review alone. The workflow captures baseline failures, writes the smallest instruction that changes behavior, reruns scenarios, and closes newly observed loopholes.

# Installed at

- `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/writing-skills/SKILL.md`
- `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/writing-skills/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Bundles a Node graph renderer, DOT examples, references, and test prompts. Its verification method dispatches subagents for baseline and with-skill pressure scenarios and can write rendered process graphs. v6.3.0 updates the bundled `render-graphs.js` renderer (SKILL.md itself unchanged).

# Install / update

```text
`claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
```

# Citations

[1] [writing-skills source](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md)
