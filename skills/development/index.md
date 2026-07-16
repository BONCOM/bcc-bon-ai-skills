# Development skills

# Development quality

* [supply-chain-risk-auditor](./supply-chain-risk-auditor.md) - Dependency takeover risk is the reason to reach for this skill before a security review. It checks maintenance activity, maintainer concentration, package popul
* [security-and-hardening](./security-and-hardening.md) - Security-sensitive code belongs under this skill when it accepts untrusted input, handles authentication or sessions, stores private data, or calls an external 
* [webhook-handler-patterns](./webhook-handler-patterns.md) - Webhook receivers that need the verify → parse → handle-idempotently sequence, framework-specific raw-body handling, retries, or error-code conventions belong h
* [stripe-webhooks](./stripe-webhooks.md) - Stripe payment, subscription, and invoice webhook setup belongs here: signature verification with the raw body, common event types, and framework examples. Pair
* [observability-and-instrumentation](./observability-and-instrumentation.md) - Production endpoints, jobs, queues, retries, and service integrations need this skill when current telemetry cannot explain failures. It defines operational que
* [ci-cd-and-automation](./ci-cd-and-automation.md) - Choose this for CI pipelines, quality gates, test jobs, and deployment workflows. It orders static checks, tests, builds, and releases so failures are caught ea
* [performance-optimization](./performance-optimization.md) - Measured slowness, regressions, Core Web Vitals failures, slow database access, and explicit latency budgets are its trigger. The workflow requires a baseline a
* [python-testing-patterns](./python-testing-patterns.md) - Python test work with pytest is the focus here, including fixtures, parametrization, mocks, async code, database tests, and integration coverage. The skill help
* [playwright-best-practices](./playwright-best-practices.md) - Playwright test design and maintenance are covered in depth: reliable locators, fixtures, page objects, authentication, API mocking, visual checks, CI, accessib
* [codeql](./codeql.md) - An explicit CodeQL request is required before using this skill, whether the task is building a database, running a suite, adding data-extension models, or proce
* [fastapi](./fastapi.md) - FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled fron

# Auth (Better Auth)

* [better-auth-best-practices](./better-auth-best-practices.md) - Better Auth server/client setup, database adapters, sessions, plugins, env vars (`BETTER_AUTH_SECRET`, `BETTER_AUTH_URL`), and CLI migrate/generate workflows be
* [create-auth](./create-auth.md) - Scaffolding login/sign-up into a TypeScript/JavaScript app with Better Auth — framework detection, adapters, route handlers, OAuth providers, and auth UI pages.
* [better-auth-security-best-practices](./better-auth-security-best-practices.md) - Hardening an existing Better Auth deployment: rate limiting, secrets, CSRF, trusted origins, session/cookie security, OAuth token encryption, IP tracking, and a
* [email-and-password-best-practices](./email-and-password-best-practices.md) - Email/password auth with Better Auth: verification, password reset, password policies, and hashing customization.
* [organization-best-practices](./organization-best-practices.md) - Multi-tenant organizations via Better Auth's organization plugin: members, invitations, custom roles/permissions, teams, and RBAC.
* [two-factor-authentication-best-practices](./two-factor-authentication-best-practices.md) - Better Auth `twoFactor` plugin: TOTP, email/SMS OTP, backup codes, trusted devices, and 2FA sign-in flows.

# Frontend and UI

* [frontend-design](./frontend-design.md) - New interfaces that need a visual direction, and existing ones that feel generic, are the target. The skill grounds typography, palette, layout, motion, and cop
* [vercel-react-best-practices](./vercel-react-best-practices.md) - React and Next.js work should consult these rules when render cost, bundle size, data fetching, or server/client boundaries matter. The 70 installed rules prior
* [vercel-composition-patterns](./vercel-composition-patterns.md) - Boolean-prop sprawl or an inflexible component API is the signal for this skill. It favors explicit variants, compound components, context interfaces, lifted st
* [vue](./vue.md) - Vue 3.5 single-file components, Composition API code, `<script setup>` macros, reactivity, watchers, composables, and built-in components such as Teleport or Su
* [web-design-guidelines](./web-design-guidelines.md) - File-based UI, accessibility, UX, and design reviews can use this focused checker. It fetches Vercel's current Web Interface Guidelines, checks the requested fi
* [playwright-cli](./playwright-cli.md) - Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and p

# Node.js

* [node](./node.md) - Node.js backend work gets targeted guidance here, especially for Node 22 native TypeScript type stripping, module resolution, async control flow, streams, shutd

# Google Cloud

* [bigquery-basics](./bigquery-basics.md) - BigQuery datasets, tables, views, jobs, SQL queries, and basic ingestion belong here. Use it when the work is the BigQuery resource model or `bq`/client-library
* [gemini-api](./gemini-api.md) - Gemini calls on Google Cloud Agent Platform (formerly Vertex AI) should start here: Gen AI SDK usage across languages, multimodal inputs, tools, structured outp
* [cloud-run-basics](./cloud-run-basics.md) - Cloud Run services, finite jobs, and always-on worker pools each have a different lifecycle, which this skill makes explicit. It explains which resource type fi
* [firebase-firestore](./firebase-firestore.md) - Any Firestore work should start here, including database discovery, edition selection, schema design, indexes, security rules, and client queries. The skill req
* [supabase](./supabase.md) - Any Supabase product work should start here: Auth, RLS, Data API grants, Edge Functions, Storage, migrations, CLI, and the Supabase MCP. It requires checking cu
* [supabase-postgres-best-practices](./supabase-postgres-best-practices.md) - Postgres query, schema, index, connection-pooling, and RLS performance work belongs here whether or not the project uses Supabase. Rules are prioritized by impa
* [google-analytics-data-api-basics](./google-analytics-data-api-basics.md) - GA4 reporting through the Analytics Data API is the scope: API enablement, compatible dimensions and metrics, and v1beta report construction. The skill covers p
* [gcloud](./gcloud.md) - Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. It requires command help validation, explicit project a
* [google-cloud-recipe-auth](./google-cloud-recipe-auth.md) - Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authoriz
* [cloud-logging-query-generation](./cloud-logging-query-generation.md) - Turn to this skill when a debugging question needs a Google Cloud Logging Query Language expression. It checks service-specific monitored resource types, uses s
* [google-cloud-waf-security](./google-cloud-waf-security.md) - Security-pillar reviews of Google Cloud workloads are its job. The skill turns workload details into requirements and recommendations for identity, network boun
* [google-cloud-waf-operational-excellence](./google-cloud-waf-operational-excellence.md) - Operational reviews of a Google Cloud workload belong here. The skill covers readiness criteria, release practice, monitoring, incident handling, and continuous
* [google-cloud-solution-architecture](./google-cloud-solution-architecture.md) - Complex Google Cloud workloads that span products need this broader architecture process for requirement discovery, design choices, validation, and a packaged r

# Skill development

* [claude-api](./claude-api.md) - Claude and Anthropic SDK work should start with this reference, including model IDs, pricing, streaming, tool use, caching, tokens, and migrations. It routes to
* [mcp-builder](./mcp-builder.md) - Building or redesigning MCP servers (Python FastMCP or Node/TypeScript SDK) belongs here: research → tool design → implementation → evaluation. It is the MCP co
* [skill-creator](./skill-creator.md) - Skill authoring and evaluation in Claude Code are the purpose of this plugin. It can create or revise a skill, design realistic trigger and output evaluations,
