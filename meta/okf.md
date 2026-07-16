---
type: Reference
title: Open Knowledge Format
description: This catalog is an OKF v0.1 knowledge bundle — markdown concepts with YAML frontmatter, indexes, logs, and cross-links.
tags: [okf, reference, format]
timestamp: 2026-07-16T00:00:00Z
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
---

This repository conforms to **Open Knowledge Format (OKF) version 0.1**.

# Bundle rules used here

| Rule | Application |
|------|-------------|
| Concept = one `.md` file | One installed skill, deferred tool, or playbook per file |
| Required `type` | `Agent Skill`, `Deferred Tool`, `Playbook`, `Overview`, `Reference`, `Archive` |
| `index.md` | Progressive disclosure at each directory |
| `log.md` | Chronological catalog changes (root) |
| Cross-links | Bundle-relative `/skills/...` paths |
| Citations | Source URLs under `# Citations` |

# How agents should read this bundle

1. Open [`/index.md`](/index.md) first — do not load every concept.
2. Descend into the relevant category index.
3. Load only the concept files needed for the task.
4. Prefer frontmatter (`type`, `tags`, `resource`) for routing; read the body for trust and install detail.

# Citations

[1] [OKF SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[2] [OKF README](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md)
