---
type: Playbook
title: Agent selection
description: Route work to the narrowest skill, agent, or direct tool.
tags: [routing, playbook]
timestamp: 2026-07-16T00:00:00Z
---

Use the narrowest capability that can finish the task. A **skill** supplies domain instructions; an **agent** gets a separate context and can run a bounded workstream; **direct tools** (Glob, rg, Read) handle narrow lookups. They are not interchangeable.

Never invent an unavailable agent or model name. Choose only from the agent and model catalogs exposed in the current client session; if the requested option is absent, say so plainly.

## Agents and tools

- Narrow repository lookup (one file, one symbol, one command) -> direct Glob, rg, and Read tools
- Broad codebase exploration -> `explore`
- Command-heavy work (git, builds, long shell) -> `shell`
- GitHub PRs, issues, CI status, releases, `gh` ops -> `gh` (not for commit/push — use commit rules)
- Browser flows and UI verification -> browser MCP / tools available in-session (e.g. `cursor-ide-browser`); do not assume a `browser-use` agent exists
- One failed PR check -> `ci-investigator`
- Explicit local change review -> `bugbot` (only when the user asks)
- Explicit security review -> `security-review` (only when the user asks)
- Independent workstreams -> `dispatching-parallel-agents`
- Approved implementation plan -> `subagent-driven-development` or `executing-plans`
- Creative feature / behavior change before coding -> Superpowers `brainstorming`
- Normal implementation review -> `requesting-code-review` (not Bugbot/security-review unless requested)

## Skills by domain

Prefer the specialist. Use a broad skill only when the task spans disciplines or the specialist is unclear.

### SEO and writing

- SEO -> narrowest matching `seo-*` (`seo-schema`, `seo-hreflang`, `seo-google`, `seo-geo`, `seo-technical`, …)
- Multi-discipline SEO or unclear routing -> `seo`
- Humanize AI-sounding prose -> `humanizer`

### Documents and session workflow

- PDF files -> `pdf`
- Word `.docx` -> `docx`
- PowerPoint `.pptx` / decks -> `pptx`
- Spreadsheets (`.xlsx` / `.csv` as deliverable) -> `xlsx`
- Discover/install a skill from skills.sh -> `find-skills` (still run trust review before adopting)
- End-of-session / cross-agent resume doc -> `handoff` (manual `/handoff`)
- Ultra-brief caveman replies -> `caveman` (opt-in; say "normal mode" to exit)

### Auth and payments

- Better Auth setup / scaffold -> `better-auth-best-practices` or `create-auth`
- Better Auth hardening -> `better-auth-security-best-practices`
- Email/password -> `email-and-password-best-practices`
- Orgs / RBAC -> `organization-best-practices`
- 2FA / MFA -> `two-factor-authentication-best-practices`
- Webhook handlers (any provider) -> `webhook-handler-patterns`
- Stripe webhooks -> `stripe-webhooks`

### Data and backends

- Supabase product / Auth / RLS / MCP -> `supabase`
- Pure Postgres performance -> `supabase-postgres-best-practices`
- BigQuery datasets / SQL / jobs -> `bigquery-basics`
- FastAPI -> `fastapi`
- Firebase Firestore -> `firebase-firestore`
- Node.js runtime / APIs -> `node`

### Google Cloud

- `gcloud` CLI usage -> `gcloud`
- Cloud Run -> `cloud-run-basics`
- Auth / identity recipe -> `google-cloud-recipe-auth`
- Cloud Logging LQL -> `cloud-logging-query-generation`
- WAF security / ops reviews -> `google-cloud-waf-security` / `google-cloud-waf-operational-excellence`
- Multi-product architecture -> `google-cloud-solution-architecture`
- GA4 Data API -> `google-analytics-data-api-basics`

### AI APIs and MCP

- Gemini on Vertex / Agent Platform -> `gemini-api`
- Claude / Anthropic SDK -> `claude-api`
- Building an MCP server -> `mcp-builder`
- Authoring a skill (Claude Code plugin) -> `skill-creator`
- Simplify recently written code without behavior change (Claude Code) -> `code-simplifier`

### Frontend

- Distinctive UI / visual design -> `frontend-design`
- React / Next performance patterns -> `vercel-react-best-practices`
- React composition at scale -> `vercel-composition-patterns`
- Vue -> `vue`
- Web Interface Guidelines review -> `web-design-guidelines`

### Quality, security, and testing

- Threat model / hardening at trust boundaries -> `security-and-hardening`
- Dependency takeover risk -> `supply-chain-risk-auditor`
- Explicit CodeQL workflow -> `codeql` (manual; needs CodeQL CLI)
- Observability / instrumentation design -> `observability-and-instrumentation`
- CI/CD pipelines -> `ci-cd-and-automation`
- Measured performance work -> `performance-optimization`
- Playwright tests -> `playwright-best-practices`; Playwright CLI -> `playwright-cli`
- Python / pytest -> `python-testing-patterns`

## Rules

1. Prefer direct tools over an agent for narrow work.
2. Prefer a specialist skill over a broad suite skill.
3. Reserve `bugbot` and `security-review` for explicit user requests.
4. Parallelize only independent work (no shared mutable files or services).
5. If two skills could apply, pick the one that matches the primary artifact (e.g. RLS policy -> `supabase`, not generic security).

# Related

- Skills index: [/skills/index.md](/skills/index.md)
- Deferred tools: [/deferred/index.md](/deferred/index.md)
- Catalog overview: [/meta/catalog-overview.md](/meta/catalog-overview.md)
