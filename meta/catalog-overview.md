---
type: Overview
title: Boncom AI Skills catalog
description: OKF inventory of Cursor/Claude agent skills — sources, trust notes, install paths, routing, and deferred tools.
tags: [overview, catalog]
timestamp: 2026-07-16T00:00:00Z
okf_bundle: boncom-ai-skills
counts:
  development: 41
  seo: 31
  writing: 1
  superpowers: 14
  total_unique: 87
  deferred: 23
---

This repository is an **Open Knowledge Format (OKF) v0.1** knowledge bundle for Boncom agent skills installed outside app-bundled capabilities.

# Counts

| Category | Unique skills |
|----------|---------------|
| Development | 41 |
| SEO | 31 |
| Writing | 1 |
| Superpowers | 14 |
| **Total unique** | **87** |
| Deferred (not installed) | 23 |

# How to navigate

1. Start at the root [`/index.md`](/index.md) for progressive disclosure.
2. Open a category under [`/skills/`](/skills/index.md).
3. Read one concept file per skill (frontmatter for routing; body for trust and install).
4. Use [`/playbooks/agent-selection.md`](/playbooks/agent-selection.md) to choose skill vs agent vs direct tools.
5. Check [`/deferred/`](/deferred/index.md) before proposing new installs.

# Discovery paths

- Normal skills: `~/.claude/skills/` (Cursor reads this Claude compatibility path).
- Superpowers: separate Cursor and Claude Code plugin cache paths; 14 names counted once.
- Skill Creator: Claude Code plugin only.

# Out of scope

Cursor/Claude built-ins, live MCP servers, and bundled subagents are not catalog concepts unless separately installed as skills.

# Citations

[1] [Open Knowledge Format SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[2] [BONCOM/boncom-ai-skills](https://github.com/BONCOM/boncom-ai-skills)
