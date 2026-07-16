---
type: Agent Skill
title: gh
description: "GitHub operations via the gh CLI — PRs, issues, CI checks, releases, workflow runs, code search, repo and label management. Does not commit or push."
resource: "https://github.com/paulnsorensen/skillz-that-grillz/blob/main/skills/gh/SKILL.md"
tags: [development, installed, github]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

Day-to-day GitHub work through the `gh` CLI: pull requests, issues, CI/workflow status, releases, repo/label management, and code search. Uses `gh --jq` / `--template` and `--body-file` for PR/issue bodies. Treats local `git` as read-only (status/diff/log); does not stage, commit, or push.

# When to use

Use when creating or managing PRs, checking CI, working issues/releases, or other `gh` tasks. Prefer existing Cursor commit/PR user rules for commits and pushes. Prefer Superpowers review skills for code-quality review.

# Installed at

- `~/.claude/skills/gh/SKILL.md`
- `~/.agents/skills/gh/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction plus `references/` (jq recipes, troubleshooting, automation, extras). No bundled installer scripts. Later use runs authenticated `gh` against GitHub and can create/merge PRs, edit issues, trigger workflows, and change repo settings — confirm destructive actions. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Med Risk.

# Install / update

```text
npx -y skills@1.5.18 add paulnsorensen/skillz-that-grillz --skill gh -g -a claude-code -y --copy
```

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
- Boncom team grant on new repos: local Cursor rule / skill `boncom-new-repo-team-access`

# Citations

[1] [gh skill source](https://github.com/paulnsorensen/skillz-that-grillz/blob/main/skills/gh/SKILL.md)
