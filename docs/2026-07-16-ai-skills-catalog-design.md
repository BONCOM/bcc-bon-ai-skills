# AI Skills Catalog Design

Date: 2026-07-16

## Goal

Create a durable inventory of agent skills that were installed separately from
Cursor and Claude Code, remove the installed trading/investing suite, and add a
curated set of development skills for the stacks used across Code_Projects.

The catalog must distinguish installed skills from app-bundled capabilities,
link every entry to its source, and record enough trust and installation
information to make future updates deliberate.

## Scope

### Remove

Delete the 19 installed trading/investing skill directories under
`~/.claude/skills/`:

- `dividend-growth-pullback-screener`
- `economic-calendar-fetcher`
- `exposure-coach`
- `kanchi-dividend-review-monitor`
- `kanchi-dividend-sop`
- `kanchi-dividend-us-tax-accounting`
- `macro-regime-detector`
- `market-environment-analysis`
- `portfolio-manager`
- `position-sizer`
- `scenario-analyzer`
- `sector-analyst`
- `stanley-druckenmiller-investment`
- `trader-memory-core`
- `trading-skills-navigator`
- `us-market-bubble-detector`
- `us-stock-analysis`
- `value-dividend-screener`
- `weekly-performance-digest`

This deletion is limited to installed skill directories. It does not delete
source repositories, portfolio data, reports, credentials, or thesis state.
The catalog will retain the canonical reinstall source before deletion:
https://github.com/tradermonty/claude-trading-skills

### Preserve

- 31 Claude SEO skills from https://github.com/AgriciDaniel/claude-seo
- `humanizer` from https://github.com/blader/humanizer
- The 14 Superpowers skills from https://github.com/obra/superpowers
- The nine development skills installed on 2026-07-16
- Existing project files and repositories under `Code_Projects`

### Add

Development quality:

- `supply-chain-risk-auditor` — https://github.com/trailofbits/skills
- `security-and-hardening` — https://github.com/addyosmani/agent-skills
- `observability-and-instrumentation` — https://github.com/addyosmani/agent-skills
- `ci-cd-and-automation` — https://github.com/addyosmani/agent-skills
- `performance-optimization` — https://github.com/addyosmani/agent-skills
- `python-testing-patterns` — https://github.com/wshobson/agents
- `playwright-best-practices` —
  https://github.com/currents-dev/playwright-best-practices-skill
- `codeql` — https://github.com/trailofbits/skills

Frontend and UI:

- `vercel-composition-patterns` — https://github.com/vercel-labs/agent-skills
- `vue` — https://github.com/antfu/skills

Node.js:

- `node` — https://github.com/mcollina/skills

Google Cloud:

- `gcloud` — https://github.com/google/skills
- `google-cloud-recipe-auth` — https://github.com/google/skills
- `cloud-logging-query-generation` — https://github.com/google/skills
- `google-cloud-waf-security` — https://github.com/google/skills
- `google-cloud-waf-operational-excellence` — https://github.com/google/skills
- `google-cloud-solution-architecture` — https://github.com/google/skills

Skill development:

- `skill-creator` — install the Anthropic-verified Claude Code plugin from
  https://claude.com/plugins/skill-creator

Superpowers will also be enabled in Claude Code from the official Claude plugin
marketplace. This adds cross-client availability but does not add another
unique skill to the inventory.

## Explicitly Not Installed

- `grill-me`: overlaps Superpowers `brainstorming`.
- `claude-mem`: captures broad session history and overlaps context tooling.
- Context Mode: credible but deferred until context exhaustion is a measured
  problem; it adds global hooks, an MCP server, subprocess execution, and local
  SQLite state.
- `cloud-monitoring-metric-selection`: deferred until the Google Cloud
  Monitoring MCP is configured manually with read-only credentials; its current
  workflow otherwise edits MCP configuration automatically.
- `vite` and `vitest`: install when a project actually uses those tools.
- `shadcn`: install when a project uses shadcn registries; its workflow consumes
  mutable remote registry and documentation content.
- `tailwind-design-system`: overlaps shadcn and existing frontend guidance;
  install for a custom Tailwind v4 design-system project.
- `wcag-audit-patterns`: install only when formal WCAG 2.2 or VPAT evidence is
  required.
- Community Docker skills: reviewed options are generic or assume specialist
  agents that are unavailable in Cursor; use the installed Cloud Run and GCP
  guidance until a Docker-specific need justifies another skill.
- Community agent routers: reviewed options hardcode Claude-specific agents and
  model names that do not match Cursor's available subagent catalog.
- Retired `next-best-practices`: Vercel moved current Next.js guidance into
  version-matched bundled documentation.
- Karpathy behavioural guidelines: overlap `ponytail` and Superpowers.
- Sentry for AI: defer until Sentry MCP is deliberately configured.
- Extra Hookdeck provider skills: install per provider when needed.
- `n8n-skills`, Nimbalyst visual bundle, Remotion, changelog generator, and
  marketing/writing marketplace packs: deferred for YAGNI or host/MCP
  prerequisites; see `optional-tools.md`.
- `ui-ux-pro-max`: overlaps installed frontend design guidance.

## Installation Policy

- Install normal Agent Skills globally under `~/.claude/skills/`.
- Rely on Cursor's documented compatibility discovery of
  `~/.claude/skills/`; do not create another physical copy for Cursor.
- Use the reviewed `skills` CLI version 1.5.18 because the current machine runs
  Node 22.16 and CLI 1.5.19 requires Node 22.20 or newer.
- Install individual skills, never an entire repository catalog.
- Before installation, inspect each selected `SKILL.md`, bundled scripts,
  allowed tools, mutable network fetches, license, and repository status.
- Keep `codeql` manually invoked. Its skill may run project builds or download
  query packs after confirmation, and useful execution requires a separately
  installed CodeQL CLI.
- If a selected skill fails inspection or installation, skip it and record the
  reason rather than manually copying an incomplete package.
- Plugins that require hooks or configuration changes must use their documented
  installer rather than a partial file copy.

## Catalog Structure

`/Users/rramesh/Documents/Code_Projects/AI_Skills/` will contain:

- `README.md` — purpose, counts, discovery paths, update process, inclusion and
  exclusion rules, and links to the category documents.
- `development.md` — installed development, frontend, testing, security, GCP,
  and skill-authoring entries.
- `seo.md` — every separately installed SEO skill.
- `writing.md` — standalone writing/content skills.
- `superpowers.md` — the separately installed plugin and each included skill.
- `agent-selection.md` — a practical routing guide for Cursor's actual
  subagents and the installed skills.
- `optional-tools.md` — reviewed but deferred tools such as Context Mode,
  Monitoring, Vite, Vitest, shadcn, Tailwind design-system guidance, and formal
  WCAG and Docker guidance, including reasons and trust boundaries.
- `docs/2026-07-16-ai-skills-catalog-design.md` — this design record.

No trading catalog will be created after the installed suite is removed.

## Entry Format

Every installed skill entry will include:

- Exact skill name
- One-paragraph purpose
- Exact source repository or `SKILL.md` URL
- Local installation path
- Availability in Cursor, Claude Code, or both
- License when established
- Important permissions, scripts, network calls, external services, or API-key
  requirements
- Installation/update source

Copied skills present in both `~/.agents/skills/` and `~/.claude/skills/` will
be listed once with both paths. Cursor/Claude built-ins, MCP tools, bundled
subagents, and `SKILL.md` files inside virtual environments are excluded.

## Agent Selection Guide

The guide will route tasks using the capabilities actually available in Cursor:

- Narrow repository search: direct search tools
- Broad codebase exploration: `explore`
- Command-heavy investigation: `shell`
- Browser flows and UI verification: `browser-use`
- CI failure diagnosis: `ci-investigator`
- Explicit local change review: `bugbot` or `security-review`
- SEO work: the appropriate `seo-*` specialist
- Independent parallel work: Superpowers `dispatching-parallel-agents`
- Plan execution: Superpowers `executing-plans` or
  `subagent-driven-development`

It will not invent agents or model names that are unavailable in Cursor.

## Expected Inventory

Starting unique separately installed skills: 74.

- Remove 19 trading/investing skills.
- Add 17 development-stack skills.
- Add one `skill-creator` skill/plugin.
- Enabling Superpowers in Claude Code adds no new unique skill names.

Expected final unique separately installed skills: 73.

## Verification

- Confirm all 19 trading skill paths are absent.
- Confirm every selected normal skill has a readable
  `~/.claude/skills/<name>/SKILL.md`.
- Confirm the Skill Creator and Superpowers plugins are listed by Claude Code.
- Confirm Cursor can discover the new skills through its Claude compatibility
  path after reload.
- Rebuild the inventory from disk and confirm 73 unique separately installed
  skills, excluding virtual-environment artifacts and app-bundled skills.
- Validate every catalog source link and ensure no entry lacks attribution.
- Confirm no files in `SEO_Audit_Tool` were modified by installation or
  documentation work.

## Recovery

All removed trading skills remain reinstallable from their recorded source.
New normal skills can be removed by deleting only their named directories under
`~/.claude/skills/`. Plugin removal must use the owning application's plugin
uninstall command so hooks and configuration are cleaned up correctly.
