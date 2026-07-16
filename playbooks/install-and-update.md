---
type: Playbook
title: Install and update skills
description: Trust-reviewed install process for normal skills and plugins.
tags: [install, playbook, trust]
timestamp: 2026-07-16T00:00:00Z
---

Treat an update as a fresh trust decision.

1. Inspect the exact source skill, sibling scripts, declared tools, mutable network access, license, and repository status.
2. For a normal skill, use the Node-compatible pinned CLI `skills@1.5.18`.
3. Install one named skill, never a repository's complete catalog (except small official packs deliberately adopted as a set).
4. Verify the installed `SKILL.md`, local path, unexpected additions, duplicate copies, and any plugin metadata.
5. Add or update the matching OKF concept under [`/skills/`](/skills/index.md) and append [`/log.md`](/log.md).

# Normal skill install shape

```text
npx -y skills@1.5.18 add <owner/repository> --skill <exact-name> -g -a claude-code -y --copy
```

# Plugins

Plugins must use the owning application's plugin command. Do not manually copy one component out of a plugin because that can omit hooks, manifests, or cleanup state.

# Removal

Remove a normal skill by deleting only its named directory under `~/.claude/skills/`. Uninstall plugins through Claude Code or Cursor. Do not delete source repositories, project data, reports, or credentials.

# Citations

[1] [OKF specification v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
