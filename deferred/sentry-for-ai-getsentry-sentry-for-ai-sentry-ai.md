---
type: Deferred Tool
title: "Sentry for AI (`getsentry/sentry-for-ai` / `@sentry/ai`)"
description: "Installer wires a Sentry MCP and a large skill library; no active Sentry-driven debugging workflow was confirmed. Same class of deferral as `cloud-monitoring-metric-selection`."
resource: "https://docs.sentry.io/ai/agent-plugin/"
tags: [deferred]
timestamp: 2026-07-16T00:00:00Z
status: deferred
---

# Why deferred

Installer wires a Sentry MCP and a large skill library; no active Sentry-driven debugging workflow was confirmed. Same class of deferral as `cloud-monitoring-metric-selection`.

# Reconsider when

A maintained app uses Sentry in production and needs agent-assisted issue triage with a reviewed, scoped Sentry auth.

# Trust boundary

MCP access exposes production errors, stack traces, and potentially PII in event payloads. Prefer explicit MCP setup over an installer that rewrites assistant config.

# Citations

[1] [Source](https://docs.sentry.io/ai/agent-plugin/)
