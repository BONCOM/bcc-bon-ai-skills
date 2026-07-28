---
type: Overview
title: Boncom AI Skills
description: OKF v0.1 inventory of Cursor/Claude agent skills for Boncom — sources, trust, install, routing, deferred tools.
tags: [overview, github]
timestamp: 2026-07-27T18:02:00-06:00
---

<div align="center">

# Boncom AI Skills

**Trusted Cursor & Claude agent skills for Boncom** — cataloged, reviewed, and ready to route.

[![Skills](https://img.shields.io/badge/skills-96-111827?style=for-the-badge)](#skill-inventory)
[![Repos](https://img.shields.io/badge/repos-24-2563eb?style=for-the-badge)](#source-repositories)
[![OKF](https://img.shields.io/badge/OKF-v0.1-059669?style=for-the-badge)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[![Catalog](https://img.shields.io/badge/catalog-private-6b7280?style=for-the-badge)](https://github.com/BONCOM/boncom-ai-skills)

**Maintained by [Rishi Ramesh](https://github.com/rrishi0309)**

`Last updated: 2026-07-27 18:02:00 MDT`

</div>

---

## Why this exists

Agents get better when they load the **narrowest skill** for the job — not a pile of generic prompts. This repo is the Boncom inventory: every installed skill has a source, trust notes, install path, and routing guidance.

| | Count |
|---|---:|
| Development | 50 |
| SEO | 31 |
| Writing | 1 |
| Superpowers | 14 |
| **Total unique** | **96** |
| Deferred (reviewed, not installed) | 23 |
| Source repositories | 24 |

## Quick start

| Step | Link |
|---|---|
| Progressive disclosure entry | [`index.md`](index.md) |
| Counts & scope | [`meta/catalog-overview.md`](meta/catalog-overview.md) |
| Route skill vs agent vs tools | [`playbooks/agent-selection.md`](playbooks/agent-selection.md) |
| Trust-reviewed install / update | [`playbooks/install-and-update.md`](playbooks/install-and-update.md) |
| Per-skill concepts | [`skills/`](skills/) |
| Deferred tools | [`deferred/`](deferred/) |
| Change log | [`log.md`](log.md) |

## Source repositories

One row per upstream GitHub repo. Expand a pack below for a short summary — full per-skill docs live under [`skills/`](skills/).

| Repository | Skills | Last skill update | Repo activity |
|---|---:|---|---|
| [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) | 31 | 2026-07-20 | 2026-07-20 |
| [`obra/superpowers`](https://github.com/obra/superpowers) | 14 | 2026-07-24 | 2026-07-24 |
| [`google/skills`](https://github.com/google/skills) | 10 | 2026-07-24 | 2026-07-24 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 7 | 2026-07-24 | 2026-07-24 |
| [`better-auth/skills`](https://github.com/better-auth/skills) | 6 | 2026-07-11 | 2026-07-11 |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 4 | 2026-07-11 | 2026-07-16 |
| [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | 3 | 2026-04-14 | 2026-07-07 |
| [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official) | 2 | 2026-04-23 | 2026-07-17 |
| [`hookdeck/webhook-skills`](https://github.com/hookdeck/webhook-skills) | 2 | 2026-05-11 | 2026-07-09 |
| [`supabase/agent-skills`](https://github.com/supabase/agent-skills) | 2 | 2026-07-10 | 2026-07-14 |
| [`trailofbits/skills`](https://github.com/trailofbits/skills) | 2 | 2026-04-28 | 2026-07-15 |
| [`antfu/skills`](https://github.com/antfu/skills) | 1 | 2026-01-31 | 2026-06-23 |
| [`blader/humanizer`](https://github.com/blader/humanizer) | 1 | 2026-07-22 | 2026-07-22 |
| [`currents-dev/playwright-best-practices-skill`](https://github.com/currents-dev/playwright-best-practices-skill) | 1 | 2026-07-21 | 2026-07-21 |
| [`fastapi/fastapi`](https://github.com/fastapi/fastapi) | 1 | 2026-06-25 | 2026-07-16 |
| [`firebase/agent-skills`](https://github.com/firebase/agent-skills) | 1 | 2026-06-22 | 2026-07-01 |
| [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman) | 1 | 2026-07-03 | 2026-07-03 |
| [`mattpocock/skills`](https://github.com/mattpocock/skills) | 1 | 2026-07-08 | 2026-07-16 |
| [`mcollina/skills`](https://github.com/mcollina/skills) | 1 | 2026-03-13 | 2026-07-16 |
| [`microsoft/playwright-cli`](https://github.com/microsoft/playwright-cli) | 1 | 2026-07-09 | 2026-07-15 |
| [`microsoft/skills`](https://github.com/microsoft/skills) | 1 | 2026-07-22 | 2026-07-22 |
| [`paulnsorensen/skillz-that-grillz`](https://github.com/paulnsorensen/skillz-that-grillz) | 1 | 2026-07-17 | 2026-07-17 |
| [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | 1 | 2026-07-10 | 2026-07-16 |
| [`wshobson/agents`](https://github.com/wshobson/agents) | 1 | 2026-05-22 | 2026-07-16 |

### Skill inventory

<details>
<summary><a href="https://github.com/AgriciDaniel/claude-seo"><strong>AgriciDaniel/claude-seo</strong></a> · <strong>31</strong> skills · skills updated <code>2026-07-20</code> · repo <code>2026-07-20</code></summary>

Claude SEO suite for audits, content, technical SEO, local/maps, schema, sitemaps, AI-search (GEO), and vendor extensions.

**Covers:** full-site audit, page analysis, technical SEO, content & briefs, schema, hreflang, images, local & maps, ecommerce, programmatic SEO, SXO/intent, FLOW planning, backlinks, Ahrefs/Bing/DataForSEO/Firecrawl/SE Ranking/Profound/Unlighthouse extensions

**Installed:** `seo`, `seo-ahrefs`, `seo-audit`, `seo-backlinks`, `seo-bing`, `seo-cluster`, `seo-competitor-pages`, `seo-content`, `seo-content-brief`, `seo-dataforseo`, `seo-drift`, `seo-ecommerce`, `seo-firecrawl`, `seo-flow`, `seo-geo`, `seo-google`, `seo-hreflang`, `seo-image-gen`, `seo-images`, `seo-local`, `seo-maps`, `seo-page`, `seo-plan`, `seo-profound`, `seo-programmatic`, `seo-schema`, `seo-seranking`, `seo-sitemap`, `seo-sxo`, `seo-technical`, `seo-unlighthouse`

</details>

<details>
<summary><a href="https://github.com/obra/superpowers"><strong>obra/superpowers</strong></a> · <strong>14</strong> skills · skills updated <code>2026-07-24</code> · repo <code>2026-07-24</code></summary>

End-to-end agentic engineering process: design → plan → TDD → implement → review → verify → finish the branch.

**Covers:** brainstorming, writing/executing plans, TDD, systematic debugging, parallel agents, subagent-driven development, code review, git worktrees, verification-before-completion

**Installed:** `brainstorming`, `dispatching-parallel-agents`, `executing-plans`, `finishing-a-development-branch`, `receiving-code-review`, `requesting-code-review`, `subagent-driven-development`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `using-superpowers`, `verification-before-completion`, `writing-plans`, `writing-skills`

</details>

<details>
<summary><a href="https://github.com/google/skills"><strong>google/skills</strong></a> · <strong>10</strong> skills · skills updated <code>2026-07-24</code> · repo <code>2026-07-24</code></summary>

Google Cloud product skills for common Boncom cloud work.

**Covers:** gcloud, Cloud Run, BigQuery, Gemini on Agent Platform, Cloud Logging LQL, Analytics Data API, auth recipes, WAF security & ops reviews, solution architecture

**Installed:** `bigquery-basics`, `cloud-logging-query-generation`, `cloud-run-basics`, `gcloud`, `gemini-api`, `google-analytics-data-api-basics`, `google-cloud-recipe-auth`, `google-cloud-solution-architecture`, `google-cloud-waf-operational-excellence`, `google-cloud-waf-security`

</details>

<details>
<summary><a href="https://github.com/anthropics/skills"><strong>anthropics/skills</strong></a> · <strong>7</strong> skills · skills updated <code>2026-07-24</code> · repo <code>2026-07-24</code></summary>

Official Anthropic skills for Claude/API work, UI design, MCP servers, and office documents.

**Covers:** claude-api, frontend-design, mcp-builder, pdf, docx (+ .dotx templates), pptx (+ .potx templates), xlsx

**Installed:** `claude-api`, `docx`, `frontend-design`, `mcp-builder`, `pdf`, `pptx`, `xlsx`

</details>

<details>
<summary><a href="https://github.com/better-auth/skills"><strong>better-auth/skills</strong></a> · <strong>6</strong> skills · skills updated <code>2026-07-11</code> · repo <code>2026-07-11</code></summary>

Better Auth setup, scaffolding, and hardening.

**Covers:** server/client best practices, create-auth scaffolding, security hardening, email/password, organizations/RBAC, 2FA

**Installed:** `better-auth-best-practices`, `better-auth-security-best-practices`, `create-auth`, `email-and-password-best-practices`, `organization-best-practices`, `two-factor-authentication-best-practices`

</details>

<details>
<summary><a href="https://github.com/addyosmani/agent-skills"><strong>addyosmani/agent-skills</strong></a> · <strong>4</strong> skills · skills updated <code>2026-07-11</code> · repo <code>2026-07-16</code></summary>

Production quality skills for delivery and runtime health.

**Covers:** CI/CD & automation, observability/instrumentation, performance optimization, security & hardening

**Installed:** `ci-cd-and-automation`, `observability-and-instrumentation`, `performance-optimization`, `security-and-hardening`

</details>

<details>
<summary><a href="https://github.com/vercel-labs/agent-skills"><strong>vercel-labs/agent-skills</strong></a> · <strong>3</strong> skills · skills updated <code>2026-04-14</code> · repo <code>2026-07-07</code></summary>

Vercel engineering guidance for React/Next UI quality and performance.

**Covers:** React best practices, composition patterns, Web Interface Guidelines reviews

**Installed:** `vercel-composition-patterns`, `vercel-react-best-practices`, `web-design-guidelines`

</details>

<details>
<summary><a href="https://github.com/anthropics/claude-plugins-official"><strong>anthropics/claude-plugins-official</strong></a> · <strong>2</strong> skills · skills updated <code>2026-04-23</code> · repo <code>2026-07-17</code></summary>

Official Claude Code plugins (not normal SKILL.md installs).

**Covers:** skill-creator, code-simplifier

**Installed:** `code-simplifier`, `skill-creator`

</details>

<details>
<summary><a href="https://github.com/hookdeck/webhook-skills"><strong>hookdeck/webhook-skills</strong></a> · <strong>2</strong> skills · skills updated <code>2026-05-11</code> · repo <code>2026-07-09</code></summary>

Webhook receiver patterns and Stripe-specific handlers.

**Covers:** verify → parse → idempotent handle, Stripe webhooks

**Installed:** `stripe-webhooks`, `webhook-handler-patterns`

</details>

<details>
<summary><a href="https://github.com/supabase/agent-skills"><strong>supabase/agent-skills</strong></a> · <strong>2</strong> skills · skills updated <code>2026-07-10</code> · repo <code>2026-07-14</code></summary>

Supabase product guidance plus Postgres performance rules.

**Covers:** Auth/RLS/Edge/Storage/MCP, Postgres performance & RLS

**Installed:** `supabase`, `supabase-postgres-best-practices`

</details>

<details>
<summary><a href="https://github.com/trailofbits/skills"><strong>trailofbits/skills</strong></a> · <strong>2</strong> skills · skills updated <code>2026-04-28</code> · repo <code>2026-07-15</code></summary>

Security analysis skills from Trail of Bits.

**Covers:** CodeQL workflows, supply-chain risk auditing

**Installed:** `codeql`, `supply-chain-risk-auditor`

</details>

<details>
<summary><a href="https://github.com/antfu/skills"><strong>antfu/skills</strong></a> · <strong>1</strong> skill · skills updated <code>2026-01-31</code> · repo <code>2026-06-23</code></summary>

Vue 3 / Composition API guidance.

**Covers:** Vue SFCs, script setup, reactivity, composables

**Installed:** `vue`

</details>

<details>
<summary><a href="https://github.com/blader/humanizer"><strong>blader/humanizer</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-22</code> · repo <code>2026-07-22</code></summary>

Rewrite AI-sounding prose so it reads naturally.

**Covers:** humanizer editing pass

**Installed:** `humanizer`

</details>

<details>
<summary><a href="https://github.com/currents-dev/playwright-best-practices-skill"><strong>currents-dev/playwright-best-practices-skill</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-21</code> · repo <code>2026-07-21</code></summary>

Deep Playwright test design and maintenance.

**Covers:** locators, fixtures, auth, mocking, visual/a11y/CI patterns

**Installed:** `playwright-best-practices`

</details>

<details>
<summary><a href="https://github.com/fastapi/fastapi"><strong>fastapi/fastapi</strong></a> · <strong>1</strong> skill · skills updated <code>2026-06-25</code> · repo <code>2026-07-16</code></summary>

Current FastAPI conventions for APIs and review.

**Covers:** routes, Pydantic, dependencies, SSE, response models

**Installed:** `fastapi`

</details>

<details>
<summary><a href="https://github.com/firebase/agent-skills"><strong>firebase/agent-skills</strong></a> · <strong>1</strong> skill · skills updated <code>2026-06-22</code> · repo <code>2026-07-01</code></summary>

Firestore data modeling and client/query guidance.

**Covers:** edition choice, schema, indexes, security rules, queries

**Installed:** `firebase-firestore`

</details>

<details>
<summary><a href="https://github.com/JuliusBrussee/caveman"><strong>JuliusBrussee/caveman</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-03</code> · repo <code>2026-07-03</code></summary>

Ultra-brief reply style to cut narration tokens.

**Covers:** caveman / lite / ultra modes

**Installed:** `caveman`

</details>

<details>
<summary><a href="https://github.com/mattpocock/skills"><strong>mattpocock/skills</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-08</code> · repo <code>2026-07-16</code></summary>

Session handoff documents for fresh agents.

**Covers:** manual /handoff compaction to OS temp

**Installed:** `handoff`

</details>

<details>
<summary><a href="https://github.com/mcollina/skills"><strong>mcollina/skills</strong></a> · <strong>1</strong> skill · skills updated <code>2026-03-13</code> · repo <code>2026-07-16</code></summary>

Node.js backend patterns (Node 22+).

**Covers:** native TS stripping, modules, streams, shutdown, testing flakes

**Installed:** `node`

</details>

<details>
<summary><a href="https://github.com/microsoft/playwright-cli"><strong>microsoft/playwright-cli</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-09</code> · repo <code>2026-07-15</code></summary>

Shell-driven browser automation via Playwright CLI.

**Covers:** navigate, snapshot, forms, screenshots, test generation

**Installed:** `playwright-cli`

</details>

<details>
<summary><a href="https://github.com/microsoft/skills"><strong>microsoft/skills</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-22</code> · repo <code>2026-07-22</code></summary>

Microsoft's coding-agent skill collection — mostly Azure SDK skills outside this catalog's GCP/Vercel/Supabase-centric scope; one general-purpose frontend skill adopted.

**Covers:** frontend design/PR review (three-pillar quality framework, accessibility, design-system compliance)

**Installed:** `frontend-design-review`

</details>

<details>
<summary><a href="https://github.com/paulnsorensen/skillz-that-grillz"><strong>paulnsorensen/skillz-that-grillz</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-17</code> · repo <code>2026-07-17</code></summary>

Day-to-day GitHub work through the gh CLI.

**Covers:** PR inspection/review/merge, issues, CI, releases, search (no commit/push/PR creation — repo retired its bundled commit and pr-stack skills)

**Installed:** `gh`

</details>

<details>
<summary><a href="https://github.com/vercel-labs/skills"><strong>vercel-labs/skills</strong></a> · <strong>1</strong> skill · skills updated <code>2026-07-10</code> · repo <code>2026-07-16</code></summary>

Discover and install skills from the skills.sh ecosystem.

**Covers:** find-skills registry search + install guidance

**Installed:** `find-skills`

</details>

<details>
<summary><a href="https://github.com/wshobson/agents"><strong>wshobson/agents</strong></a> · <strong>1</strong> skill · skills updated <code>2026-05-22</code> · repo <code>2026-07-16</code></summary>

Python/pytest testing patterns.

**Covers:** fixtures, parametrization, mocks, async & DB tests

**Installed:** `python-testing-patterns`

</details>

## Maintenance

Treat every install or update as a fresh trust decision. See [`playbooks/install-and-update.md`](playbooks/install-and-update.md).

```bash
# Normal skill (pinned CLI)
npx -y skills@1.5.18 add <owner/repository> --skill <exact-name> -g -a claude-code -y --copy

# Regenerate from legacy monoliths (if present)
python3 scripts/build_okf_catalog.py
```

## Maintainer

**Rishi Ramesh** — catalog design, trust review, installs, and routing for Boncom.

- GitHub: [@rrishi0309](https://github.com/rrishi0309)
- Org repo: [BONCOM/boncom-ai-skills](https://github.com/BONCOM/boncom-ai-skills)

---

<div align="center">

[OKF SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) · Built for Cursor + Claude Code

</div>
