---
type: Overview
title: Boncom AI Skills
description: OKF v0.1 inventory of Cursor/Claude agent skills for Boncom — sources, trust, install, routing, deferred tools.
tags: [overview, github]
timestamp: 2026-07-16T00:00:00Z
---

# Boncom AI Skills

This repository is an **[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)** knowledge bundle.

**95 unique installed skills** (49 development + 31 SEO + 1 writing + 14 Superpowers), plus 23 deferred tools.

## Start here

1. [`index.md`](index.md) — progressive disclosure entry point
2. [`meta/catalog-overview.md`](meta/catalog-overview.md) — counts and scope
3. [`playbooks/agent-selection.md`](playbooks/agent-selection.md) — routing
4. [`skills/`](skills/) — one concept file per installed skill
5. [`deferred/`](deferred/) — reviewed but not installed
6. [`log.md`](log.md) — change history

## What a concept contains

Each skill concept has YAML frontmatter (`type`, `title`, `description`, `resource`, `tags`, …) and a structured body: when to use, install paths, license, trust notes, install command, and citations.

## Maintenance

See [`playbooks/install-and-update.md`](playbooks/install-and-update.md). Regenerate from legacy monoliths (if present) with:

```bash
python3 scripts/build_okf_catalog.py
```

# Citations

[1] [OKF SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[2] [GitHub: BONCOM/boncom-ai-skills](https://github.com/BONCOM/boncom-ai-skills)
