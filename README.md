---
type: Overview
title: Boncom AI Skills
description: OKF v0.1 inventory of Cursor/Claude agent skills for Boncom — sources, trust, install, routing, deferred tools.
tags: [overview, github]
timestamp: 2026-07-16T20:45:36-06:00
---

<div align="center">

# Boncom AI Skills

**Trusted Cursor & Claude agent skills for Boncom** — cataloged, reviewed, and ready to route.

[![Skills](https://img.shields.io/badge/skills-95-111827?style=for-the-badge)](#skill-inventory)
[![Repos](https://img.shields.io/badge/repos-23-2563eb?style=for-the-badge)](#source-repositories)
[![OKF](https://img.shields.io/badge/OKF-v0.1-059669?style=for-the-badge)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[![License](https://img.shields.io/badge/catalog-private-6b7280?style=for-the-badge)](https://github.com/BONCOM/boncom-ai-skills)

**Maintained by [Rishi Ramesh](https://github.com/rramesh)**

`Last updated: 2026-07-16 20:45:36 MDT`

</div>

---

## Why this exists

Agents get better when they load the **narrowest skill** for the job — not a pile of generic prompts. This repo is the Boncom inventory: every installed skill has a source, trust notes, install path, and routing guidance.

| | Count |
|---|---:|
| Development | 49 |
| SEO | 31 |
| Writing | 1 |
| Superpowers | 14 |
| **Total unique** | **95** |
| Deferred (reviewed, not installed) | 23 |
| Source repositories | 23 |

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

Each concept file includes YAML frontmatter plus when-to-use, install paths, license, trust notes, and citations.

## Source repositories

One row per upstream GitHub repo. Expand a repo below for skill names, descriptions, and per-skill upstream dates.

| Repository | Skills | Last skill update | Repo activity |
|---|---:|---|---|
| [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) | 31 | 2026-06-12 | 2026-07-06 |
| [`obra/superpowers`](https://github.com/obra/superpowers) | 14 | 2026-06-30 | 2026-07-17 |
| [`google/skills`](https://github.com/google/skills) | 10 | 2026-07-16 | 2026-07-17 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 7 | 2026-07-01 | 2026-07-16 |
| [`better-auth/skills`](https://github.com/better-auth/skills) | 6 | 2026-07-11 | 2026-07-11 |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 4 | 2026-07-11 | 2026-07-16 |
| [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | 3 | 2026-04-14 | 2026-07-07 |
| [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official) | 2 | 2026-04-23 | 2026-07-17 |
| [`hookdeck/webhook-skills`](https://github.com/hookdeck/webhook-skills) | 2 | 2026-05-11 | 2026-07-09 |
| [`supabase/agent-skills`](https://github.com/supabase/agent-skills) | 2 | 2026-07-10 | 2026-07-14 |
| [`trailofbits/skills`](https://github.com/trailofbits/skills) | 2 | 2026-04-28 | 2026-07-15 |
| [`antfu/skills`](https://github.com/antfu/skills) | 1 | 2026-01-31 | 2026-06-23 |
| [`blader/humanizer`](https://github.com/blader/humanizer) | 1 | 2026-06-29 | 2026-06-29 |
| [`currents-dev/playwright-best-practices-skill`](https://github.com/currents-dev/playwright-best-practices-skill) | 1 | 2026-03-13 | 2026-03-13 |
| [`fastapi/fastapi`](https://github.com/fastapi/fastapi) | 1 | 2026-06-25 | 2026-07-16 |
| [`firebase/agent-skills`](https://github.com/firebase/agent-skills) | 1 | 2026-06-22 | 2026-07-01 |
| [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman) | 1 | 2026-07-03 | 2026-07-03 |
| [`mattpocock/skills`](https://github.com/mattpocock/skills) | 1 | 2026-07-08 | 2026-07-16 |
| [`mcollina/skills`](https://github.com/mcollina/skills) | 1 | 2026-03-13 | 2026-07-16 |
| [`microsoft/playwright-cli`](https://github.com/microsoft/playwright-cli) | 1 | 2026-07-09 | 2026-07-15 |
| [`paulnsorensen/skillz-that-grillz`](https://github.com/paulnsorensen/skillz-that-grillz) | 1 | 2026-05-27 | 2026-07-16 |
| [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | 1 | 2026-07-10 | 2026-07-16 |
| [`wshobson/agents`](https://github.com/wshobson/agents) | 1 | 2026-05-22 | 2026-07-16 |

### Skill inventory

<details>
<summary><strong><a href="https://github.com/AgriciDaniel/claude-seo">AgriciDaniel/claude-seo</a></strong> · **31** skills · skills updated `2026-06-12` · repo `2026-07-06`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`seo`](skills/seo/seo.md) | Start here when an SEO request spans several disciplines or the right specialist is unclear. The skill detects the business type, routes work to installed specialists, and combines technical, content, schema, image, local, AI-search, and performance findings. | 2026-06-12 |
| [`seo-ahrefs`](skills/seo/seo-ahrefs.md) | Ahrefs domain metrics, referring domains, backlinks, anchors, organic keywords, and Content Explorer results are the scope of this extension. It pairs paid Ahrefs evidence with `seo-backlinks` so cross-source discrepancies remain visible. | 2026-06-12 |
| [`seo-audit`](skills/seo/seo-audit.md) | A full-site health check belongs here rather than in the single-page skill. The audit crawls up to 500 pages, detects the business type, selects always-on and conditional specialists, calculates a health score, and returns a prioritized action plan. | 2026-06-12 |
| [`seo-backlinks`](skills/seo/seo-backlinks.md) | Referring-domain analysis, anchor distribution, toxic-link review, link gaps, new or lost links, and disavow evidence are handled here. The skill merges Common Crawl and a verification crawler with optional Moz, Bing Webmaster, Ahrefs, or DataForSEO data instead of pretending one source is complete. | 2026-06-12 |
| [`seo-bing`](skills/seo/seo-bing.md) | Bing Webmaster link data, Microsoft Copilot citation eligibility, and IndexNow submission to participating search engines are this extension's focus. It deliberately does not describe IndexNow as a Google indexing mechanism. | 2026-06-12 |
| [`seo-cluster`](skills/seo/seo-cluster.md) | Keyword groups based on overlapping Google top-ten results are the input to this skill's hub-and-spoke planning. It produces cluster plans, internal-link matrices, and interactive maps; content creation is optional and separate. | 2026-06-12 |
| [`seo-competitor-pages`](skills/seo/seo-competitor-pages.md) | Comparison, alternatives, and category-roundup pages get a dedicated workflow here. It structures feature comparisons, verdict criteria, conversion paths, and supporting schema while requiring claims to be grounded in current competitor evidence. | 2026-06-12 |
| [`seo-content`](skills/seo/seo-content.md) | Content quality, readability, thin-content, and E-E-A-T reviews should use this skill. It applies Google's Who/How/Why test, checks experience and authorship evidence, and scores whether passages are clear enough to cite in search and AI answers. | 2026-06-12 |
| [`seo-content-brief`](skills/seo/seo-content-brief.md) | Writers can use this output as an evidence-based brief for a new page or as a targeted improvement plan for an existing one. It compares current results, scores content gaps, allocates section lengths, sets keyword placement guidance, and chooses a page-type template. | 2026-06-12 |
| [`seo-dataforseo`](skills/seo/seo-dataforseo.md) | Live SERPs, keyword volume and intent, backlinks, business listings, competitor data, image results, and measured AI mentions come from this extension. It routes among the DataForSEO MCP modules and labels the returned evidence as live vendor data. | 2026-06-12 |
| [`seo-drift`](skills/seo/seo-drift.md) | A known-good page baseline lets this skill detect SEO regressions after content or deployment changes. It compares titles, canonicals, robots directives, headings, schema, links, and other critical elements, then keeps a local comparison history. | 2026-06-12 |
| [`seo-ecommerce`](skills/seo/seo-ecommerce.md) | Product-page SEO, Product schema, marketplace visibility, pricing comparisons, and Shopping or Amazon keyword gaps are handled here. The base mode audits the page directly; richer market analysis is added only when the DataForSEO Merchant API is available. | 2026-06-12 |
| [`seo-firecrawl`](skills/seo/seo-firecrawl.md) | Choose Firecrawl when an audit needs JavaScript-rendered scraping, URL discovery, a site map, broken-link coverage, or a larger crawl than the base fetcher can provide. This extension exposes crawl, map, scrape, and in-site search operations. | 2026-06-12 |
| [`seo-flow`](skills/seo/seo-flow.md) | The FLOW method and its stage-specific evidence prompts live in this skill. It selects from the Find, Leverage, Optimize, Win, and Local prompt sets so the analysis starts from a defined decision question instead of a broad SEO request. | 2026-06-12 |
| [`seo-geo`](skills/seo/seo-geo.md) | AI Overviews, ChatGPT search, Perplexity, and similar answer surfaces are the focus of this visibility review. It checks crawler access, brand mentions, `llms.txt`, passage citability, and platform signals while treating Google's GEO guidance as ordinary SEO fundamentals where the primary source says so. | 2026-06-12 |
| [`seo-google`](skills/seo/seo-google.md) | Search Console, PageSpeed Insights, CrUX history, sitemap status, GA4 organic traffic, and the Indexing API are routed through this skill. It adds Google's own measurements and index state to crawler-based observations. | 2026-06-12 |
| [`seo-hreflang`](skills/seo/seo-hreflang.md) | International targeting across HTML, HTTP headers, or XML sitemaps gets a focused audit and generator here. The checks cover language and region codes, self references, reciprocal return links, canonical alignment, and the single `x-default` fallback. | 2026-06-12 |
| [`seo-image-gen`](skills/seo/seo-image-gen.md) | An Open Graph preview, hero, product image, infographic, schema image, or thumbnail is a generation task for this extension. It maps the asset type to aspect ratio and resolution, then delegates generation through the Banana creative pipeline. | 2026-06-12 |
| [`seo-images`](skills/seo/seo-images.md) | Existing image assets can be checked for alt text, dimensions, formats, responsive sources, lazy loading, CLS risk, file size, metadata, and search visibility. The same skill can plan or run WebP/AVIF conversion and IPTC/XMP updates when local files are supplied. | 2026-06-12 |
| [`seo-local`](skills/seo/seo-local.md) | Website-level local SEO belongs here: business-type detection, NAP consistency, citations, reviews, location pages, local schema, service areas, and multi-location structure. Checks adjust for brick-and-mortar, service-area, and hybrid businesses and for the detected industry. | 2026-06-12 |
| [`seo-maps`](skills/seo/seo-maps.md) | Maps-platform evidence is separate from the on-page work in `seo-local`. This skill supports geo-grid rank scans, GBP audits, review velocity, cross-platform NAP checks, competitor-radius mapping, Share of Local Voice, and LocalBusiness schema derived from API data. | 2026-06-12 |
| [`seo-page`](skills/seo/seo-page.md) | One URL is the unit of work for this analysis. It checks title and heading structure, content depth, canonicals and robots directives, social metadata, schema, images, internal links, and page-level performance without turning the request into a site crawl. | 2026-06-12 |
| [`seo-plan`](skills/seo/seo-plan.md) | SEO strategy for a new or existing site is different from an issue audit, and this skill handles that planning work. It captures goals and constraints, reviews competitors, designs information architecture and internal links, and turns industry templates into a phased roadmap. | 2026-06-12 |
| [`seo-profound`](skills/seo/seo-profound.md) | Time-series brand citation rates, prompt coverage, co-cited competitors, and spike or drop alerts across ChatGPT and Perplexity come from Profound. The extension complements point-in-time vendor checks by making weekly and monthly citation trends the primary evidence. | 2026-06-12 |
| [`seo-programmatic`](skills/seo/seo-programmatic.md) | Pages generated at scale from CSV, JSON, an API, or a database need this planning and audit process. It evaluates record uniqueness and freshness, designs URL and template rules, automates internal-link planning, and sets thin-content and index-bloat gates before rollout. | 2026-06-12 |
| [`seo-schema`](skills/seo/seo-schema.md) | Schema.org detection, validation, and generation are grouped in this skill, with JSON-LD as the preferred format. It checks required properties, data types, absolute URLs, dates, deprecated types, and current Google rich-result support before proposing code. | 2026-06-12 |
| [`seo-seranking`](skills/seo/seo-seranking.md) | SE Ranking supplies live AI Share of Voice across ChatGPT, Gemini, Perplexity, Google AI Overviews, and AI Mode, along with SERP, backlink, and competitor data. This skill reports each platform separately with sample-size context. | 2026-06-12 |
| [`seo-sitemap`](skills/seo/seo-sitemap.md) | XML sitemap validation and generation share this workflow. It checks protocol limits, status codes, canonical and noindex conflicts, `lastmod`, robots references, redirects, and missing crawled pages, and can generate a split sitemap plan. | 2026-06-12 |
| [`seo-sxo`](skills/seo/seo-sxo.md) | A technically sound page can still target the wrong intent or page type; this skill tests that mismatch. It reads the SERP backward, derives user stories from ranked results, scores the page through several personas, and can produce a wireframe tied to observed intent. | 2026-06-12 |
| [`seo-technical`](skills/seo/seo-technical.md) | Crawlability, indexability, URL structure, mobile behavior, security headers, JavaScript rendering, structured data, Core Web Vitals, and IndexNow checks form this technical audit. The skill keeps those findings separate from content strategy and records which crawler or protocol each rule affects. | 2026-06-12 |
| [`seo-unlighthouse`](skills/seo/seo-unlighthouse.md) | A local multi-page Lighthouse sweep is useful when PageSpeed quota, CI repeatability, or broad regression coverage matters. This wrapper runs Unlighthouse against a capped route set and aggregates median performance, accessibility, best-practice, and SEO scores. | 2026-06-12 |

</details>

<details>
<summary><strong><a href="https://github.com/obra/superpowers">obra/superpowers</a></strong> · **14** skills · skills updated `2026-06-30` · repo `2026-07-17`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`brainstorming`](skills/superpowers/brainstorming.md) | Creative implementation and behavior changes start with this design workflow. It explores the current project, asks one focused question at a time, compares approaches, gets approval on a written design, and only then hands the work to planning. | 2026-06-16 |
| [`dispatching-parallel-agents`](skills/superpowers/dispatching-parallel-agents.md) | Two or more tasks with separate state, separate causes, and no ordering dependency can be dispatched through this skill. It assigns one isolated agent per problem with deliberately scoped context, then reconciles the independent results in the parent session. | 2026-06-16 |
| [`executing-plans`](skills/superpowers/executing-plans.md) | A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow. | 2026-06-30 |
| [`finishing-a-development-branch`](skills/superpowers/finishing-a-development-branch.md) | Branch integration is the final step after implementation and tests are complete. This skill freshly verifies tests, detects whether the workspace is a normal checkout or managed worktree, presents merge, PR, keep, or cleanup choices, and executes only the selected path. | 2026-06-16 |
| [`receiving-code-review`](skills/superpowers/receiving-code-review.md) | Review feedback should pass through this technical check before implementation, particularly when a suggestion is ambiguous or may not fit the codebase. The skill separates understanding from agreement, verifies the claim, and supports reasoned pushback before applying one change at a time. | 2026-06-16 |
| [`requesting-code-review`](skills/superpowers/requesting-code-review.md) | A completed plan task, major feature, or pending merge is the point to request this review. The skill gives a fresh reviewer precise requirements and a bounded Git range rather than the author's full session history, then classifies findings by severity. | 2026-06-16 |
| [`subagent-driven-development`](skills/superpowers/subagent-driven-development.md) | An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass. | 2026-06-18 |
| [`systematic-debugging`](skills/superpowers/systematic-debugging.md) | Bugs, test failures, build errors, integration issues, and unexplained performance problems all start with root-cause investigation here. The skill gathers evidence, traces the failure to its source, tests one hypothesis at a time, and revisits the model after repeated failed fixes. | 2026-06-16 |
| [`test-driven-development`](skills/superpowers/test-driven-development.md) | Implementation code for a feature, bug fix, refactor, or behavior change follows the test in this workflow. It requires a focused failure for the expected reason, the minimum code to pass, a fresh full verification, and cleanup only after the green state is established. | 2026-06-16 |
| [`using-git-worktrees`](skills/superpowers/using-git-worktrees.md) | Plan execution and isolated feature work can use this worktree setup. It first detects managed worktrees and submodules, prefers the platform's native isolation, and falls back to Git only after checking location, ignore rules, branch state, and project setup. | 2026-06-16 |
| [`using-superpowers`](skills/superpowers/using-superpowers.md) | This is the session-level routing rule for the library. It requires checking applicable skills before responding or acting, orders process skills before implementation guidance, and exempts dispatched task subagents so their supplied task brief remains authoritative. | 2026-06-30 |
| [`verification-before-completion`](skills/superpowers/verification-before-completion.md) | Completion, fix, pass, and merge-readiness claims need this evidence gate. It identifies the command that proves the claim, runs it fresh and in full, reads the result and exit status, and reports the actual state when evidence disagrees. | 2025-10-17 |
| [`writing-plans`](skills/superpowers/writing-plans.md) | An approved design or multi-step requirement becomes an implementation handoff through this skill. It maps file responsibilities, splits work into independently reviewable tasks, specifies exact edits and tests, and saves the plan under `docs/superpowers/plans`. | 2026-06-16 |
| [`writing-skills`](skills/superpowers/writing-skills.md) | Agent skill authoring, revision, and verification use pressure tests here rather than prose review alone. The workflow captures baseline failures, writes the smallest instruction that changes behavior, reruns scenarios, and closes newly observed loopholes. | 2026-06-30 |

</details>

<details>
<summary><strong><a href="https://github.com/google/skills">google/skills</a></strong> · **10** skills · skills updated `2026-07-16` · repo `2026-07-17`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`bigquery-basics`](skills/development/bigquery-basics.md) | BigQuery datasets, tables, views, jobs, SQL queries, and basic ingestion belong here. Use it when the work is the BigQuery resource model or `bq`/client-library operations rather than BQML or pandas-style BigFrames. | 2026-06-24 |
| [`cloud-logging-query-generation`](skills/development/cloud-logging-query-generation.md) | Turn to this skill when a debugging question needs a Google Cloud Logging Query Language expression. It checks service-specific monitored resource types, uses strict quoting and boolean syntax, and returns query text only; it is not for SQL or Spanner data. | 2026-07-13 |
| [`cloud-run-basics`](skills/development/cloud-run-basics.md) | Cloud Run services, finite jobs, and always-on worker pools each have a different lifecycle, which this skill makes explicit. It explains which resource type fits the workload and provides `gcloud` flows for image and source deployments rather than treating every container as an HTTP service. | 2026-07-16 |
| [`gcloud`](skills/development/gcloud.md) | Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. It requires command help validation, explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations. | 2026-06-24 |
| [`gemini-api`](skills/development/gemini-api.md) | Gemini calls on Google Cloud Agent Platform (formerly Vertex AI) should start here: Gen AI SDK usage across languages, multimodal inputs, tools, structured output, embeddings, Live API, media generation, caching, and batch prediction. Prefer this over stale training data for model/SDK details. | 2026-06-24 |
| [`google-analytics-data-api-basics`](skills/development/google-analytics-data-api-basics.md) | GA4 reporting through the Analytics Data API is the scope: API enablement, compatible dimensions and metrics, and v1beta report construction. The skill covers property-scoped reporting, metadata checks, pagination, date ranges, and client-library requests instead of relying on the Analytics UI. | 2026-07-08 |
| [`google-cloud-recipe-auth`](skills/development/google-cloud-recipe-auth.md) | Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys. | 2026-06-24 |
| [`google-cloud-solution-architecture`](skills/development/google-cloud-solution-architecture.md) | Complex Google Cloud workloads that span products need this broader architecture process for requirement discovery, design choices, validation, and a packaged recommendation. A request about one service should go to a narrower product skill. | 2026-07-10 |
| [`google-cloud-waf-operational-excellence`](skills/development/google-cloud-waf-operational-excellence.md) | Operational reviews of a Google Cloud workload belong here. The skill covers readiness criteria, release practice, monitoring, incident handling, and continuous improvement using the Operational Excellence pillar rather than product-specific setup instructions. | 2026-06-24 |
| [`google-cloud-waf-security`](skills/development/google-cloud-waf-security.md) | Security-pillar reviews of Google Cloud workloads are its job. The skill turns workload details into requirements and recommendations for identity, network boundaries, data protection, threat defense, privacy, and operations. | 2026-06-24 |

</details>

<details>
<summary><strong><a href="https://github.com/anthropics/skills">anthropics/skills</a></strong> · **7** skills · skills updated `2026-07-01` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`claude-api`](skills/development/claude-api.md) | Claude and Anthropic SDK work should start with this reference, including model IDs, pricing, streaming, tool use, caching, tokens, and migrations. It routes to language-specific material and live official sources, and it avoids inserting Anthropic code into a project that uses another provider. | 2026-07-01 |
| [`docx`](skills/development/docx.md) | Create, read, edit, or manipulate Word (.docx) documents — professional formatting, tracked changes, comments, templates, find-and-replace, and image insertion. | 2026-02-25 |
| [`frontend-design`](skills/development/frontend-design.md) | New interfaces that need a visual direction, and existing ones that feel generic, are the target. The skill grounds typography, palette, layout, motion, and copy in the product subject, requires a design pass before code, and includes responsive, focus, and reduced-motion checks. | 2026-06-09 |
| [`mcp-builder`](skills/development/mcp-builder.md) | Building or redesigning MCP servers (Python FastMCP or Node/TypeScript SDK) belongs here: research → tool design → implementation → evaluation. It is the MCP counterpart to `skill-creator` and is installed as a normal skill so Cursor and Claude Code both see it. | 2025-12-01 |
| [`pdf`](skills/development/pdf.md) | Create, read, merge, split, rotate, watermark, encrypt, form-fill, OCR, or otherwise manipulate PDF files. Trigger on any .pdf deliverable or PDF-processing request. | 2026-02-04 |
| [`pptx`](skills/development/pptx.md) | Create, read, edit, or combine PowerPoint (.pptx) decks — slides, pitch decks, templates, speaker notes, thumbnails, and text extraction. | 2026-02-04 |
| [`xlsx`](skills/development/xlsx.md) | Create, read, edit, or clean spreadsheet files (.xlsx, .xlsm, .csv, .tsv) — formulas, formatting, charts, and tabular cleanup when the deliverable is a spreadsheet. | 2026-02-04 |

</details>

<details>
<summary><strong><a href="https://github.com/better-auth/skills">better-auth/skills</a></strong> · **6** skills · skills updated `2026-07-11` · repo `2026-07-11`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`better-auth-best-practices`](skills/development/better-auth-best-practices.md) | Better Auth server/client setup, database adapters, sessions, plugins, env vars (`BETTER_AUTH_SECRET`, `BETTER_AUTH_URL`), and CLI migrate/generate workflows belong here. | 2026-07-11 |
| [`better-auth-security-best-practices`](skills/development/better-auth-security-best-practices.md) | Hardening an existing Better Auth deployment: rate limiting, secrets, CSRF, trusted origins, session/cookie security, OAuth token encryption, IP tracking, and audit logging. | 2026-07-10 |
| [`create-auth`](skills/development/create-auth.md) | Scaffolding login/sign-up into a TypeScript/JavaScript app with Better Auth — framework detection, adapters, route handlers, OAuth providers, and auth UI pages. | 2026-07-11 |
| [`email-and-password-best-practices`](skills/development/email-and-password-best-practices.md) | Email/password auth with Better Auth: verification, password reset, password policies, and hashing customization. | 2026-03-02 |
| [`organization-best-practices`](skills/development/organization-best-practices.md) | Multi-tenant organizations via Better Auth's organization plugin: members, invitations, custom roles/permissions, teams, and RBAC. | 2026-07-11 |
| [`two-factor-authentication-best-practices`](skills/development/two-factor-authentication-best-practices.md) | Better Auth `twoFactor` plugin: TOTP, email/SMS OTP, backup codes, trusted devices, and 2FA sign-in flows. | 2026-07-11 |

</details>

<details>
<summary><strong><a href="https://github.com/addyosmani/agent-skills">addyosmani/agent-skills</a></strong> · **4** skills · skills updated `2026-07-11` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`ci-cd-and-automation`](skills/development/ci-cd-and-automation.md) | Choose this for CI pipelines, quality gates, test jobs, and deployment workflows. It orders static checks, tests, builds, and releases so failures are caught early, while keeping deployment steps explicit and reviewable. | 2026-03-31 |
| [`observability-and-instrumentation`](skills/development/observability-and-instrumentation.md) | Production endpoints, jobs, queues, retries, and service integrations need this skill when current telemetry cannot explain failures. It defines operational questions first and then chooses logs, metrics, traces, and alerts that answer those questions without leaking secrets or personal data. | 2026-06-11 |
| [`performance-optimization`](skills/development/performance-optimization.md) | Measured slowness, regressions, Core Web Vitals failures, slow database access, and explicit latency budgets are its trigger. The workflow requires a baseline and profile before changes, then targets the observed frontend, backend, query, or database bottleneck and measures again. | 2026-07-07 |
| [`security-and-hardening`](skills/development/security-and-hardening.md) | Security-sensitive code belongs under this skill when it accepts untrusted input, handles authentication or sessions, stores private data, or calls an external service. The workflow starts with trust boundaries and a short threat model, then applies concrete controls for validation, authorization, secrets, uploads, webhooks, and data handling. | 2026-07-11 |

</details>

<details>
<summary><strong><a href="https://github.com/vercel-labs/agent-skills">vercel-labs/agent-skills</a></strong> · **3** skills · skills updated `2026-04-14` · repo `2026-07-07`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`vercel-composition-patterns`](skills/development/vercel-composition-patterns.md) | Boolean-prop sprawl or an inflexible component API is the signal for this skill. It favors explicit variants, compound components, context interfaces, lifted state, and React 19 patterns that keep implementation details replaceable. | 2026-01-28 |
| [`vercel-react-best-practices`](skills/development/vercel-react-best-practices.md) | React and Next.js work should consult these rules when render cost, bundle size, data fetching, or server/client boundaries matter. The 70 installed rules prioritize async waterfalls and bundle waste before lower-impact rendering and JavaScript refinements. | 2026-04-14 |
| [`web-design-guidelines`](skills/development/web-design-guidelines.md) | File-based UI, accessibility, UX, and design reviews can use this focused checker. It fetches Vercel's current Web Interface Guidelines, checks the requested files against those rules, and returns terse `file:line` findings rather than redesigning the page. | 2026-01-16 |

</details>

<details>
<summary><strong><a href="https://github.com/anthropics/claude-plugins-official">anthropics/claude-plugins-official</a></strong> · **2** skills · skills updated `2026-04-23` · repo `2026-07-17`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`code-simplifier`](skills/development/code-simplifier.md) | Claude Code agent that simplifies recently modified code for clarity and maintainability while preserving exact behavior. Prefer after a logical chunk of implementation, not as a broad rewrite. | 2026-02-20 |
| [`skill-creator`](skills/development/skill-creator.md) | Skill authoring and evaluation in Claude Code are the purpose of this plugin. It can create or revise a skill, design realistic trigger and output evaluations, compare controlled runs, inspect benchmark variance, improve the description, and package the result. | 2026-04-23 |

</details>

<details>
<summary><strong><a href="https://github.com/hookdeck/webhook-skills">hookdeck/webhook-skills</a></strong> · **2** skills · skills updated `2026-05-11` · repo `2026-07-09`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`stripe-webhooks`](skills/development/stripe-webhooks.md) | Stripe payment, subscription, and invoice webhook setup belongs here: signature verification with the raw body, common event types, and framework examples. Pair with `webhook-handler-patterns` for idempotency and retries; use the Stripe MCP for live account operations. | 2026-05-11 |
| [`webhook-handler-patterns`](skills/development/webhook-handler-patterns.md) | Webhook receivers that need the verify → parse → handle-idempotently sequence, framework-specific raw-body handling, retries, or error-code conventions belong here. Use it with Next.js, Express, or FastAPI handlers before adding provider-specific skills. | 2026-02-06 |

</details>

<details>
<summary><strong><a href="https://github.com/supabase/agent-skills">supabase/agent-skills</a></strong> · **2** skills · skills updated `2026-07-10` · repo `2026-07-14`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`supabase`](skills/development/supabase.md) | Any Supabase product work should start here: Auth, RLS, Data API grants, Edge Functions, Storage, migrations, CLI, and the Supabase MCP. It requires checking current docs/changelog before implementing because APIs and config change between versions. | 2026-07-10 |
| [`supabase-postgres-best-practices`](skills/development/supabase-postgres-best-practices.md) | Postgres query, schema, index, connection-pooling, and RLS performance work belongs here whether or not the project uses Supabase. Rules are prioritized by impact and include incorrect/correct SQL examples. | 2026-04-05 |

</details>

<details>
<summary><strong><a href="https://github.com/trailofbits/skills">trailofbits/skills</a></strong> · **2** skills · skills updated `2026-04-28` · repo `2026-07-15`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`codeql`](skills/development/codeql.md) | An explicit CodeQL request is required before using this skill, whether the task is building a database, running a suite, adding data-extension models, or processing SARIF. It checks database extraction quality before treating a scan as valid and treats zero findings as a result that still needs validation. | 2026-04-28 |
| [`supply-chain-risk-auditor`](skills/development/supply-chain-risk-auditor.md) | Dependency takeover risk is the reason to reach for this skill before a security review. It checks maintenance activity, maintainer concentration, package popularity, and risky capabilities, then writes a focused report; it is not a substitute for a vulnerability or license scanner. | 2026-04-28 |

</details>

<details>
<summary><strong><a href="https://github.com/antfu/skills">antfu/skills</a></strong> · **1** skill · skills updated `2026-01-31` · repo `2026-06-23`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`vue`](skills/development/vue.md) | Vue 3.5 single-file components, Composition API code, `<script setup>` macros, reactivity, watchers, composables, and built-in components such as Teleport or Suspense are covered here. The installed guidance prefers TypeScript, `<script setup lang="ts">`, and shallow reactivity when deep tracking is unnecessary. | 2026-01-31 |

</details>

<details>
<summary><strong><a href="https://github.com/blader/humanizer">blader/humanizer</a></strong> · **1** skill · skills updated `2026-06-29` · repo `2026-06-29`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`humanizer`](skills/writing/humanizer.md) | Remove signs of AI-generated writing from text. Use when editing or reviewing text to make it sound more natural and human-written (humanizer v2.8.2). | 2026-06-29 |

</details>

<details>
<summary><strong><a href="https://github.com/currents-dev/playwright-best-practices-skill">currents-dev/playwright-best-practices-skill</a></strong> · **1** skill · skills updated `2026-03-13` · repo `2026-03-13`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`playwright-best-practices`](skills/development/playwright-best-practices.md) | Playwright test design and maintenance are covered in depth: reliable locators, fixtures, page objects, authentication, API mocking, visual checks, CI, accessibility, security, performance, and hard-to-test browser behavior. Its reference set is broad enough to route a specific test problem without loading every topic. | 2026-03-13 |

</details>

<details>
<summary><strong><a href="https://github.com/fastapi/fastapi">fastapi/fastapi</a></strong> · **1** skill · skills updated `2026-06-25` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`fastapi`](skills/development/fastapi.md) | FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than older FastAPI idioms. | 2026-06-25 |

</details>

<details>
<summary><strong><a href="https://github.com/firebase/agent-skills">firebase/agent-skills</a></strong> · **1** skill · skills updated `2026-06-22` · repo `2026-07-01`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`firebase-firestore`](skills/development/firebase-firestore.md) | Any Firestore work should start here, including database discovery, edition selection, schema design, indexes, security rules, and client queries. The skill requires identifying Standard or Enterprise edition before choosing references because supported query and data-model features differ. | 2026-06-22 |

</details>

<details>
<summary><strong><a href="https://github.com/JuliusBrussee/caveman">JuliusBrussee/caveman</a></strong> · **1** skill · skills updated `2026-07-03` · repo `2026-07-03`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`caveman`](skills/development/caveman.md) | Ultra-compressed communication mode — cuts narration while keeping technical facts, code, commands, and errors exact. Intensity levels: lite, full, ultra (plus wenyan variants). Invoke with /caveman or 'talk like caveman'; say 'normal mode' to exit. | 2026-07-03 |

</details>

<details>
<summary><strong><a href="https://github.com/mattpocock/skills">mattpocock/skills</a></strong> · **1** skill · skills updated `2026-07-08` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`handoff`](skills/development/handoff.md) | Compact the current conversation into a handoff document for a fresh agent or session. Manual invoke only (`/handoff` or explicit request). Writes to the OS temp directory; references specs/plans by path instead of copying them. | 2026-07-08 |

</details>

<details>
<summary><strong><a href="https://github.com/mcollina/skills">mcollina/skills</a></strong> · **1** skill · skills updated `2026-03-13` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`node`](skills/development/node.md) | Node.js backend work gets targeted guidance here, especially for Node 22 native TypeScript type stripping, module resolution, async control flow, streams, shutdown, logging, profiling, caching, and flaky tests. It supplies a compatible `tsconfig` direction and avoids syntax that Node's runtime cannot strip. | 2026-03-13 |

</details>

<details>
<summary><strong><a href="https://github.com/microsoft/playwright-cli">microsoft/playwright-cli</a></strong> · **1** skill · skills updated `2026-07-09` · repo `2026-07-15`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`playwright-cli`](skills/development/playwright-cli.md) | Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow. | 2026-07-09 |

</details>

<details>
<summary><strong><a href="https://github.com/paulnsorensen/skillz-that-grillz">paulnsorensen/skillz-that-grillz</a></strong> · **1** skill · skills updated `2026-05-27` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`gh`](skills/development/gh.md) | GitHub operations via the gh CLI — PRs, issues, CI checks, releases, workflow runs, code search, repo and label management. Does not commit or push. | 2026-05-27 |

</details>

<details>
<summary><strong><a href="https://github.com/vercel-labs/skills">vercel-labs/skills</a></strong> · **1** skill · skills updated `2026-07-10` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`find-skills`](skills/development/find-skills.md) | Discover and install agent skills from skills.sh when the user asks how to do X, whether a skill exists for X, or wants to extend agent capabilities. Searches the registry, checks install counts and source reputation, then offers install commands. | 2026-07-10 |

</details>

<details>
<summary><strong><a href="https://github.com/wshobson/agents">wshobson/agents</a></strong> · **1** skill · skills updated `2026-05-22` · repo `2026-07-16`</summary>

| Skill | Description | Updated |
|---|---|---|
| [`python-testing-patterns`](skills/development/python-testing-patterns.md) | Python test work with pytest is the focus here, including fixtures, parametrization, mocks, async code, database tests, and integration coverage. The skill helps select the right test boundary and leaves runnable examples instead of broad testing advice. | 2026-05-22 |

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

- GitHub: [@rramesh](https://github.com/rramesh)
- Org repo: [BONCOM/boncom-ai-skills](https://github.com/BONCOM/boncom-ai-skills)

---

<div align="center">

[OKF SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) · Built for Cursor + Claude Code

</div>
