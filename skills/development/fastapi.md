---
type: Agent Skill
title: fastapi
description: "FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than olde"
resource: "https://github.com/fastapi/fastapi/blob/master/fastapi/.agents/skills/fastapi/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-11-20T00:00:00Z
category: development
group: Development quality
license: MIT
available_in: Cursor, Claude Code, Codex and Antigravity
---

FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than older FastAPI idioms.

# When to use

FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than older FastAPI idioms.

# Installed at

- `~/.claude/skills/fastapi/SKILL.md`
- `~/.agents/skills/fastapi/SKILL.md`
- `~/.gemini/config/skills/fastapi` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

MIT

# Trust notes

Instruction and reference files only; no bundled executable scripts. Examples run the local FastAPI CLI and may use project dependencies such as HTTPX, SQLModel, or Uvicorn. Since 2026-10-08 (`af889e4`) automatic OpenTelemetry exporter setup needs an explicit opt-in; 2026-10-15 (`64efa4f`) is a Ruff formatting pass on `references/dependencies.md`. 2026-11-07 (`a1c96b4`, `ed6f37b`, `afd2a57`): new `references/parameter-models.md` and `references/fastapi-cloud.md`; FastAPI Cloud (`uv run fastapi deploy`) is suggested only when the user wants a managed deployment and has not chosen a provider, and generated API clients come from the OpenAPI schema. 2026-11-14 (`fc07dde`): `Depends(max_concurrency=...)` dependency concurrency limits. Docs only. 2026-11-18 (`55ee14b`, `b0a616d`): `max_body_size` on the app, router or path operation and `form_limits` (`max_fields`, `max_files`, `max_part_size`).

# Install / update

```text
`npx -y skills@1.5.18 add fastapi/fastapi --skill fastapi -g -a claude-code -y --copy`
```

# Citations

[1] [fastapi source](https://github.com/fastapi/fastapi/blob/master/fastapi/.agents/skills/fastapi/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
