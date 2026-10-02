---
type: Agent Skill
title: fastapi
description: "FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than olde"
resource: "https://github.com/fastapi/fastapi/blob/master/fastapi/.agents/skills/fastapi/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-10-02T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor and Claude Code
---

FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than older FastAPI idioms.

# When to use

FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than older FastAPI idioms.

# Installed at

- `~/.claude/skills/fastapi/SKILL.md`
- `~/.agents/skills/fastapi/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Instruction and reference files only; no bundled executable scripts. Examples run the local FastAPI CLI and may use project dependencies such as HTTPX, SQLModel, or Uvicorn.

# Install / update

```text
`npx -y skills@1.5.18 add fastapi/fastapi --skill fastapi -g -a claude-code -y --copy`
```

# Citations

[1] [fastapi source](https://github.com/fastapi/fastapi/blob/master/fastapi/.agents/skills/fastapi/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
