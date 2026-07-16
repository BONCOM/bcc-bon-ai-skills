---
type: Agent Skill
title: find-skills
description: "Discover and install agent skills from skills.sh when the user asks how to do X, whether a skill exists for X, or wants to extend agent capabilities. Searches the registry, checks install counts and source reputation, then offers install commands."
resource: "https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md"
tags: [development, installed, workflow]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Workflow and discovery
license: Unspecified
available_in: Cursor and Claude Code
---

Discover and install agent skills from the open skills ecosystem (skills.sh / `npx skills`) when the task might already exist as a packaged skill.

# When to use

Use when the user asks "how do I do X", "find a skill for X", "is there a skill that can…", or wants to extend agent capabilities with an installable skill rather than inventing a one-off workflow.

# Installed at

- `~/.claude/skills/find-skills/SKILL.md`

# Availability

Cursor and Claude Code

# License

Unspecified in the vercel-labs/skills source repository (no LICENSE file on the skill path). Treat as third-party; prefer official publishers when recommending installs.

# Trust notes

Instruction-only skill. During use it runs `npx skills find` / `npx skills add`, which clones GitHub sources and writes into skill directories. Skills.sh: Gen Safe, Socket 0 alerts, Snyk Med Risk. Do not install candidates without a trust pass (install count, publisher, and audit badges). Still follow Boncom [`install-and-update`](/playbooks/install-and-update.md) before adopting anything globally.

# Install / update

```text
npx -y skills@1.5.18 add vercel-labs/skills --skill find-skills -g -a claude-code -y --copy
```

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Install playbook: [/playbooks/install-and-update.md](/playbooks/install-and-update.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)

# Citations

[1] [find-skills source](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md)
