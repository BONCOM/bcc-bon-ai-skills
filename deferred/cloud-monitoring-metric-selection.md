---
type: Deferred Tool
title: cloud-monitoring-metric-selection
description: "Its intended workflow configures a Google Cloud Monitoring MCP automatically, but this environment has no manually reviewed read-only Monitoring connection."
resource: "https://github.com/google/skills/blob/main/skills/cloud/cloud-monitoring-metric-selection/SKILL.md"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

Its intended workflow configures a Google Cloud Monitoring MCP automatically, but this environment has no manually reviewed read-only Monitoring connection.

# Reconsider when

A project needs recurring metric discovery or query construction and a read-only Monitoring MCP is already configured with a bounded project and identity.

# Trust boundary

Monitoring access exposes production telemetry and resource labels. Keep credentials read-only, confirm project scope, and do not let a skill rewrite global MCP configuration without review.

# Citations

[1] [Source](https://github.com/google/skills/blob/main/skills/cloud/cloud-monitoring-metric-selection/SKILL.md)
