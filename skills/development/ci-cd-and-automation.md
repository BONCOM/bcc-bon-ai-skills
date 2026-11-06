---
type: Agent Skill
title: ci-cd-and-automation
description: "Choose this for CI pipelines, quality gates, test jobs, and deployment workflows. It orders static checks, tests, builds, and releases so failures are caught early, while keeping deployment steps explicit and reviewable."
resource: "https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-10-29T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

Choose this for CI pipelines, quality gates, test jobs, and deployment workflows. It orders static checks, tests, builds, and releases so failures are caught early, while keeping deployment steps explicit and reviewable.

# When to use

Choose this for CI pipelines, quality gates, test jobs, and deployment workflows. It orders static checks, tests, builds, and releases so failures are caught early, while keeping deployment steps explicit and reviewable.

# Installed at

- `~/.claude/skills/ci-cd-and-automation/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction-only; no bundled executable scripts. Generated workflow examples may install test tools or deploy software, so review credentials, permissions, environments, and release gates before use. 2026-10-29 (`a4a21f6`, with `d3ffa3c` 2026-10-19): the rollback workflow example passes the version input through `env` instead of interpolating it into the shell script (injection hardening), the lint example uses `npm run lint -- --fix`, and the caching note says setup-node caches the package-manager cache, not `node_modules`.

# Install / update

```text
`npx -y skills@1.5.18 add addyosmani/agent-skills --skill ci-cd-and-automation -g -a claude-code -y --copy`
```

# Citations

[1] [ci-cd-and-automation source](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
