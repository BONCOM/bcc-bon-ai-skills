---
type: Deferred Tool
title: shadcn
description: No current catalog requirement depends on shadcn registries or presets.
resource: "https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

No current catalog requirement depends on shadcn registries or presets.

# Reconsider when

A project has `components.json`, uses shadcn registries, or needs `shadcn init`, component addition, preset changes, or registry debugging.

# Trust boundary

The skill allows `npx`, `pnpm dlx`, or `bunx` to run the latest shadcn CLI. Registry and documentation content are mutable, and component commands write project files, so inspect the source registry and diff.

# Citations

[1] [Source](https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md)
