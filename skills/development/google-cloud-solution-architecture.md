---
type: Agent Skill
title: google-cloud-solution-architecture
description: "Complex, multi-product Google Cloud workloads need this interactive requirement-discovery and architecture process to reach a packaged design recommendation. Route single-service or narrowly-scoped requests to a product-specific or google-cloud-recipe-* skill instead."
resource: "https://github.com/google/skills/blob/main/skills/cloud/google-cloud-solution-architecture/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-08-10T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Complex, multi-product Google Cloud workloads need this interactive requirement-discovery and architecture process to reach a packaged design recommendation. Route single-service or narrowly-scoped requests to a product-specific or google-cloud-recipe-* skill instead.

# When to use

Complex, multi-product Google Cloud workloads need this interactive requirement-discovery and architecture process to reach a packaged design recommendation. Route single-service or narrowly-scoped requests to a product-specific or google-cloud-recipe-* skill instead.

# Installed at

- `~/.claude/skills/google-cloud-solution-architecture/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction-only with reference indexes and an output template. Later use can query Google documentation through an MCP and write architecture files only after approval; live documentation is mutable. Now adds an explicit guardrail against autonomous execution of generated scripts/code — Phase 3 validation must be handed to the user to run (or dry-run only with explicit permission) rather than executed directly.

# Install / update

```text
`npx -y skills@1.5.18 add google/skills --skill google-cloud-solution-architecture -g -a claude-code -y --copy`
```

# Citations

[1] [google-cloud-solution-architecture source](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-solution-architecture/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
