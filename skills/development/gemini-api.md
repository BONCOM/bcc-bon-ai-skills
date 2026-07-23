---
type: Agent Skill
title: gemini-api
description: "Gemini calls on Google Cloud Agent Platform (formerly Vertex AI) should start here: Gen AI SDK usage across languages, multimodal inputs, tools, structured output, embeddings, Live API, media generation, caching, and batch prediction. Prefer this over stale training data for model/SDK details."
resource: "https://github.com/google/skills/blob/main/skills/cloud/gemini-api/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-23T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Gemini calls on Google Cloud Agent Platform (formerly Vertex AI) should start here: Gen AI SDK usage across languages, multimodal inputs, tools, structured output, embeddings, Live API, media generation, caching, and batch prediction. Prefer this over stale training data for model/SDK details.

# When to use

Gemini calls on Google Cloud Agent Platform (formerly Vertex AI) should start here: Gen AI SDK usage across languages, multimodal inputs, tools, structured output, embeddings, Live API, media generation, caching, and batch prediction. Prefer this over stale training data for model/SDK details.

# Installed at

- `~/.claude/skills/gemini-api/SKILL.md`
- `~/.agents/skills/gemini-api/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction and reference Markdown only; requires Google Cloud credentials and Agent Platform API access when used. Directs agents to the current Gen AI SDK (`google-genai` / `@google/genai`) and away from deprecated Vertex/generativeai clients. Can incur paid inference and touch project credentials.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill gemini-api -g -a claude-code -y --copy`
```

# Citations

[1] [gemini-api source](https://github.com/google/skills/blob/main/skills/cloud/gemini-api/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
