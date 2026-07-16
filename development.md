# Development skills

This catalog covers installed development skills. Normal skills are shared by Cursor and Claude Code through the Claude compatibility path. The Skill Creator entry is a Claude Code plugin component.

### Development quality

## `supply-chain-risk-auditor`

Dependency takeover risk is the reason to reach for this skill before a security review. It checks maintenance activity, maintainer concentration, package popularity, and risky capabilities, then writes a focused report; it is not a substitute for a vulnerability or license scanner.

- Source: https://github.com/trailofbits/skills/blob/main/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md
- Installed at: `~/.claude/skills/supply-chain-risk-auditor/SKILL.md`
- Available in: Cursor and Claude Code
- License: CC-BY-SA-4.0
- Trust notes: Declares Read, Write, Bash, Glob, and Grep; may use authenticated `gh` network calls against public GitHub metadata and writes an audit report. No bundled downloader.
- Install/update: `npx -y skills@1.5.18 add trailofbits/skills --skill supply-chain-risk-auditor -g -a claude-code -y --copy`

## `security-and-hardening`

Security-sensitive code belongs under this skill when it accepts untrusted input, handles authentication or sessions, stores private data, or calls an external service. The workflow starts with trust boundaries and a short threat model, then applies concrete controls for validation, authorization, secrets, uploads, webhooks, and data handling.

- Source: https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md
- Installed at: `~/.claude/skills/security-and-hardening/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts. Its examples mention package-manager audits and external security services, but the package does not call them automatically.
- Install/update: `npx -y skills@1.5.18 add addyosmani/agent-skills --skill security-and-hardening -g -a claude-code -y --copy`

## `webhook-handler-patterns`

Webhook receivers that need the verify → parse → handle-idempotently sequence, framework-specific raw-body handling, retries, or error-code conventions belong here. Use it with Next.js, Express, or FastAPI handlers before adding provider-specific skills.

- Source: https://github.com/hookdeck/webhook-skills/blob/main/skills/webhook-handler-patterns/SKILL.md
- Installed at: `~/.claude/skills/webhook-handler-patterns/SKILL.md`; `~/.agents/skills/webhook-handler-patterns/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction and Markdown references; no bundled executable installer. Examples may suggest local tunnels such as Hookdeck CLI; those are deliberate network tools when run. Complements `security-and-hardening` rather than replacing it.
- Install/update: `npx -y skills@1.5.18 add hookdeck/webhook-skills --skill webhook-handler-patterns -g -a claude-code -y --copy`

## `stripe-webhooks`

Stripe payment, subscription, and invoice webhook setup belongs here: signature verification with the raw body, common event types, and framework examples. Pair with `webhook-handler-patterns` for idempotency and retries; use the Stripe MCP for live account operations.

- Source: https://github.com/hookdeck/webhook-skills/blob/main/skills/stripe-webhooks/SKILL.md
- Installed at: `~/.claude/skills/stripe-webhooks/SKILL.md`; `~/.agents/skills/stripe-webhooks/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction, references, and runnable Express/Next.js/FastAPI examples. Generated handlers touch secrets (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`) and payment event data; keep secrets out of clients and verify signatures before parsing.
- Install/update: `npx -y skills@1.5.18 add hookdeck/webhook-skills --skill stripe-webhooks -g -a claude-code -y --copy`

## `observability-and-instrumentation`

Production endpoints, jobs, queues, retries, and service integrations need this skill when current telemetry cannot explain failures. It defines operational questions first and then chooses logs, metrics, traces, and alerts that answer those questions without leaking secrets or personal data.

- Source: https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md
- Installed at: `~/.claude/skills/observability-and-instrumentation/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts. It documents telemetry vendors and integrations but makes no network connection itself.
- Install/update: `npx -y skills@1.5.18 add addyosmani/agent-skills --skill observability-and-instrumentation -g -a claude-code -y --copy`

## `ci-cd-and-automation`

Choose this for CI pipelines, quality gates, test jobs, and deployment workflows. It orders static checks, tests, builds, and releases so failures are caught early, while keeping deployment steps explicit and reviewable.

- Source: https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md
- Installed at: `~/.claude/skills/ci-cd-and-automation/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts. Generated workflow examples may install test tools or deploy software, so review credentials, permissions, environments, and release gates before use.
- Install/update: `npx -y skills@1.5.18 add addyosmani/agent-skills --skill ci-cd-and-automation -g -a claude-code -y --copy`

## `performance-optimization`

Measured slowness, regressions, Core Web Vitals failures, slow database access, and explicit latency budgets are its trigger. The workflow requires a baseline and profile before changes, then targets the observed frontend, backend, query, or database bottleneck and measures again.

- Source: https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md
- Installed at: `~/.claude/skills/performance-optimization/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts. Examples refer to Lighthouse, CrUX, real-user monitoring, and optional `npx` profilers, which can create network traffic when deliberately run.
- Install/update: `npx -y skills@1.5.18 add addyosmani/agent-skills --skill performance-optimization -g -a claude-code -y --copy`

## `python-testing-patterns`

Python test work with pytest is the focus here, including fixtures, parametrization, mocks, async code, database tests, and integration coverage. The skill helps select the right test boundary and leaves runnable examples instead of broad testing advice.

- Source: https://github.com/wshobson/agents/blob/main/plugins/python-development/skills/python-testing-patterns/SKILL.md
- Installed at: `~/.claude/skills/python-testing-patterns/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only with Markdown references; no bundled executable scripts. Examples may ask to install pytest plugins or project test dependencies.
- Install/update: `npx -y skills@1.5.18 add wshobson/agents --skill python-testing-patterns -g -a claude-code -y --copy`

## `playwright-best-practices`

Playwright test design and maintenance are covered in depth: reliable locators, fixtures, page objects, authentication, API mocking, visual checks, CI, accessibility, security, performance, and hard-to-test browser behavior. Its reference set is broad enough to route a specific test problem without loading every topic.

- Source: https://github.com/currents-dev/playwright-best-practices-skill/blob/main/SKILL.md
- Installed at: `~/.claude/skills/playwright-best-practices/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Bundles Markdown references and a validation workflow, not runtime scripts. Following examples can open browsers, contact test services, use environment credentials, or update snapshots, so set the target and test-data boundary first.
- Install/update: `npx -y skills@1.5.18 add currents-dev/playwright-best-practices-skill --skill playwright-best-practices -g -a claude-code -y --copy`

## `codeql`

An explicit CodeQL request is required before using this skill, whether the task is building a database, running a suite, adding data-extension models, or processing SARIF. It checks database extraction quality before treating a scan as valid and treats zero findings as a result that still needs validation.

- Source: https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/codeql/SKILL.md
- Installed at: `~/.claude/skills/codeql/SKILL.md`
- Available in: Cursor and Claude Code
- License: CC-BY-SA-4.0
- Trust notes: Declares Bash, Read, Write, Edit, Glob, Grep, and task tools. It requires a separately installed CodeQL CLI, may run project builds or resolve query packs, and writes databases, logs, extensions, and SARIF; keep it manually invoked.
- Install/update: `npx -y skills@1.5.18 add trailofbits/skills --skill codeql -g -a claude-code -y --copy`

## `fastapi`

FastAPI implementation and review work should consult this skill for routes, Pydantic models, dependencies, response models, SSE, byte streams, and bundled frontend delivery. It points to current framework conventions such as `Annotated` dependencies and return-type response schemas rather than older FastAPI idioms.

- Source: https://github.com/fastapi/fastapi/blob/master/fastapi/.agents/skills/fastapi/SKILL.md
- Installed at: `~/.claude/skills/fastapi/SKILL.md`; `~/.agents/skills/fastapi/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction and reference files only; no bundled executable scripts. Examples run the local FastAPI CLI and may use project dependencies such as HTTPX, SQLModel, or Uvicorn.
- Install/update: `npx -y skills@1.5.18 add fastapi/fastapi --skill fastapi -g -a claude-code -y --copy`

### Frontend and UI

## `frontend-design`

New interfaces that need a visual direction, and existing ones that feel generic, are the target. The skill grounds typography, palette, layout, motion, and copy in the product subject, requires a design pass before code, and includes responsive, focus, and reduced-motion checks.

- Source: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- Installed at: `~/.claude/skills/frontend-design/SKILL.md`; `~/.agents/skills/frontend-design/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction-only; no bundled executable scripts. It may recommend screenshots for visual review but does not itself open a browser or fetch assets.
- Install/update: `npx -y skills@1.5.18 add anthropics/skills --skill frontend-design -g -a claude-code -y --copy`

## `vercel-react-best-practices`

React and Next.js work should consult these rules when render cost, bundle size, data fetching, or server/client boundaries matter. The 70 installed rules prioritize async waterfalls and bundle waste before lower-impact rendering and JavaScript refinements.

- Source: https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md
- Installed at: `~/.claude/skills/vercel-react-best-practices/SKILL.md`; `~/.agents/skills/vercel-react-best-practices/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only with compiled and per-rule Markdown references; no bundled executable scripts or required network service.
- Install/update: `npx -y skills@1.5.18 add vercel-labs/agent-skills --skill vercel-react-best-practices -g -a claude-code -y --copy`

## `vercel-composition-patterns`

Boolean-prop sprawl or an inflexible component API is the signal for this skill. It favors explicit variants, compound components, context interfaces, lifted state, and React 19 patterns that keep implementation details replaceable.

- Source: https://github.com/vercel-labs/agent-skills/blob/main/skills/composition-patterns/SKILL.md
- Installed at: `~/.claude/skills/vercel-composition-patterns/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only with Markdown rules and metadata; no bundled executable scripts or network requirements. The license is declared in the skill even though the repository has no root license file.
- Install/update: `npx -y skills@1.5.18 add vercel-labs/agent-skills --skill vercel-composition-patterns -g -a claude-code -y --copy`

## `vue`

Vue 3.5 single-file components, Composition API code, `<script setup>` macros, reactivity, watchers, composables, and built-in components such as Teleport or Suspense are covered here. The installed guidance prefers TypeScript, `<script setup lang="ts">`, and shallow reactivity when deep tracking is unnecessary.

- Source: https://github.com/antfu/skills/blob/main/skills/vue/SKILL.md
- Installed at: `~/.claude/skills/vue/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Generated instruction content and Markdown references only; no bundled executable scripts. The source is derived from Vue documentation, but the installed package performs no network fetch.
- Install/update: `npx -y skills@1.5.18 add antfu/skills --skill vue -g -a claude-code -y --copy`

## `web-design-guidelines`

File-based UI, accessibility, UX, and design reviews can use this focused checker. It fetches Vercel's current Web Interface Guidelines, checks the requested files against those rules, and returns terse `file:line` findings rather than redesigning the page.

- Source: https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md
- Installed at: `~/.claude/skills/web-design-guidelines/SKILL.md`; `~/.agents/skills/web-design-guidelines/SKILL.md`
- Available in: Cursor and Claude Code
- License: Not stated in the skill repository
- Trust notes: Instruction-only, but every review fetches mutable guidance from `raw.githubusercontent.com/vercel-labs/web-interface-guidelines`; review source changes if results shift.
- Install/update: `npx -y skills@1.5.18 add vercel-labs/agent-skills --skill web-design-guidelines -g -a claude-code -y --copy`

## `playwright-cli`

Browser navigation, form interaction, screenshots, page snapshots, and test generation are exposed through the Playwright CLI. Compact snapshot references and persistent browser sessions make it a good fit when shell-based browser control is preferable to an MCP workflow.

- Source: https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md
- Installed at: `~/.claude/skills/playwright-cli/SKILL.md`; `~/.agents/skills/playwright-cli/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Declares Bash access for `playwright-cli`, `npx`, and `npm`. Commands can browse external sites, preserve browser state, capture page content, and write screenshots or traces; confirm the target and data boundary first.
- Install/update: `npx -y skills@1.5.18 add microsoft/playwright-cli --skill playwright-cli -g -a claude-code -y --copy`

### Node.js

## `node`

Node.js backend work gets targeted guidance here, especially for Node 22 native TypeScript type stripping, module resolution, async control flow, streams, shutdown, logging, profiling, caching, and flaky tests. It supplies a compatible `tsconfig` direction and avoids syntax that Node's runtime cannot strip.

- Source: https://github.com/mcollina/skills/blob/main/skills/node/SKILL.md
- Installed at: `~/.claude/skills/node/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Includes two inspected TypeScript examples. One opens a demonstration HTTP server on `0.0.0.0:3000` only when run directly; its test uses a random localhost port. Other references mention npm, npx, and fetch.
- Install/update: `npx -y skills@1.5.18 add mcollina/skills --skill node -g -a claude-code -y --copy`

### Google Cloud

## `cloud-run-basics`

Cloud Run services, finite jobs, and always-on worker pools each have a different lifecycle, which this skill makes explicit. It explains which resource type fits the workload and provides `gcloud` flows for image and source deployments rather than treating every container as an HTTP service.

- Source: https://github.com/google/skills/blob/main/skills/cloud/cloud-run-basics/SKILL.md
- Installed at: `~/.claude/skills/cloud-run-basics/SKILL.md`; `~/.agents/skills/cloud-run-basics/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction-only; commands use authenticated `gcloud`, enable APIs, build images, and create or update Cloud Run resources. Confirm project, region, billing, and resource name before execution.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill cloud-run-basics -g -a claude-code -y --copy`

## `firebase-firestore`

Any Firestore work should start here, including database discovery, edition selection, schema design, indexes, security rules, and client queries. The skill requires identifying Standard or Enterprise edition before choosing references because supported query and data-model features differ.

- Source: https://github.com/firebase/agent-skills/blob/main/skills/firebase-firestore/SKILL.md
- Installed at: `~/.claude/skills/firebase-firestore/SKILL.md`; `~/.agents/skills/firebase-firestore/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction and reference files invoke `npx firebase-tools@latest`; authenticated commands can list or create databases and deploy rules or indexes. No credentials are bundled.
- Install/update: `npx -y skills@1.5.18 add firebase/agent-skills --skill firebase-firestore -g -a claude-code -y --copy`

## `supabase`

Any Supabase product work should start here: Auth, RLS, Data API grants, Edge Functions, Storage, migrations, CLI, and the Supabase MCP. It requires checking current docs/changelog before implementing because APIs and config change between versions.

- Source: https://github.com/supabase/agent-skills/blob/main/skills/supabase/SKILL.md
- Installed at: `~/.claude/skills/supabase/SKILL.md`; `~/.agents/skills/supabase/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only with a security checklist and MCP troubleshooting. Later use can call the authenticated Supabase MCP, CLI, or docs fetches; it can change schemas, RLS, and auth configuration on live projects. Prefer `supabase-postgres-best-practices` for pure SQL performance review.
- Install/update: `npx -y skills@1.5.18 add supabase/agent-skills --skill supabase -g -a claude-code -y --copy`

## `supabase-postgres-best-practices`

Postgres query, schema, index, connection-pooling, and RLS performance work belongs here whether or not the project uses Supabase. Rules are prioritized by impact and include incorrect/correct SQL examples.

- Source: https://github.com/supabase/agent-skills/blob/main/skills/supabase-postgres-best-practices/SKILL.md
- Installed at: `~/.claude/skills/supabase-postgres-best-practices/SKILL.md`; `~/.agents/skills/supabase-postgres-best-practices/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction and reference Markdown only; no bundled executable installer. Applying the rules can change schemas, indexes, and RLS policies on a live database when the agent has MCP or CLI access.
- Install/update: `npx -y skills@1.5.18 add supabase/agent-skills --skill supabase-postgres-best-practices -g -a claude-code -y --copy`

## `google-analytics-data-api-basics`

GA4 reporting through the Analytics Data API is the scope: API enablement, compatible dimensions and metrics, and v1beta report construction. The skill covers property-scoped reporting, metadata checks, pagination, date ranges, and client-library requests instead of relying on the Analytics UI.

- Source: https://github.com/google/skills/blob/main/skills/analytics/google-analytics-data-api-basics/SKILL.md
- Installed at: `~/.claude/skills/google-analytics-data-api-basics/SKILL.md`; `~/.agents/skills/google-analytics-data-api-basics/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction-only; examples use authenticated `gcloud` and the Google Analytics Data API, which require a Cloud project, GA4 property access, API enablement, and network calls.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill google-analytics-data-api-basics -g -a claude-code -y --copy`

## `gcloud`

Read this before any `gcloud` command for resource discovery, configuration queries, or troubleshooting. It requires command help validation, explicit project and location values, reduced output, and a denylist for destructive IAM, deletion, billing, and KMS operations.

- Source: https://github.com/google/skills/blob/main/skills/cloud/gcloud/SKILL.md
- Installed at: `~/.claude/skills/gcloud/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction-only, but later use operates the authenticated Google Cloud CLI against live resources. It may read active configuration and make network calls; its safeguards forbid autonomous high-risk changes.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill gcloud -g -a claude-code -y --copy`

## `google-cloud-recipe-auth`

Google Cloud identity choices for a developer, local script, workload, or cross-cloud service are handled here. The skill separates authentication from authorization, prefers ADC, attached identities, impersonation, and short-lived credentials, and avoids defaulting to service-account keys.

- Source: https://github.com/google/skills/blob/main/skills/cloud/google-cloud-recipe-auth/SKILL.md
- Installed at: `~/.claude/skills/google-cloud-recipe-auth/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction-only with no credential reader. Its documented `gcloud auth` and ADC flows affect sensitive local or cloud credentials when a user deliberately runs them.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill google-cloud-recipe-auth -g -a claude-code -y --copy`

## `cloud-logging-query-generation`

Turn to this skill when a debugging question needs a Google Cloud Logging Query Language expression. It checks service-specific monitored resource types, uses strict quoting and boolean syntax, and returns query text only; it is not for SQL or Spanner data.

- Source: https://github.com/google/skills/blob/main/skills/cloud/cloud-logging-query-generation/SKILL.md
- Installed at: `~/.claude/skills/cloud-logging-query-generation/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction-only with 21 Markdown service references. It generates LQL but does not authenticate to or query Cloud Logging.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill cloud-logging-query-generation -g -a claude-code -y --copy`

## `google-cloud-waf-security`

Security-pillar reviews of Google Cloud workloads are its job. The skill turns workload details into requirements and recommendations for identity, network boundaries, data protection, threat defense, privacy, and operations.

- Source: https://github.com/google/skills/blob/main/skills/cloud/google-cloud-waf-security/SKILL.md
- Installed at: `~/.claude/skills/google-cloud-waf-security/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Advisory instruction content with official documentation URLs; no bundled scripts, cloud commands, authentication, or automatic fetches.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill google-cloud-waf-security -g -a claude-code -y --copy`

## `google-cloud-waf-operational-excellence`

Operational reviews of a Google Cloud workload belong here. The skill covers readiness criteria, release practice, monitoring, incident handling, and continuous improvement using the Operational Excellence pillar rather than product-specific setup instructions.

- Source: https://github.com/google/skills/blob/main/skills/cloud/google-cloud-waf-operational-excellence/SKILL.md
- Installed at: `~/.claude/skills/google-cloud-waf-operational-excellence/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Advisory instruction content with official documentation URLs; no bundled scripts, cloud commands, authentication, or automatic fetches.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill google-cloud-waf-operational-excellence -g -a claude-code -y --copy`

## `google-cloud-solution-architecture`

Complex Google Cloud workloads that span products need this broader architecture process for requirement discovery, design choices, validation, and a packaged recommendation. A request about one service should go to a narrower product skill.

- Source: https://github.com/google/skills/blob/main/skills/cloud/google-cloud-solution-architecture/SKILL.md
- Installed at: `~/.claude/skills/google-cloud-solution-architecture/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Instruction-only with reference indexes and an output template. Later use can query Google documentation through an MCP and write architecture files only after approval; live documentation is mutable.
- Install/update: `npx -y skills@1.5.18 add google/skills --skill google-cloud-solution-architecture -g -a claude-code -y --copy`

### Skill development

## `claude-api`

Claude and Anthropic SDK work should start with this reference, including model IDs, pricing, streaming, tool use, caching, tokens, and migrations. It routes to language-specific material and live official sources, and it avoids inserting Anthropic code into a project that uses another provider.

- Source: https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md
- Installed at: `~/.claude/skills/claude-api/SKILL.md`; `~/.agents/skills/claude-api/SKILL.md`
- Available in: Cursor and Claude Code
- License: Apache-2.0
- Trust notes: Bundles documentation and examples, not an executable installer. Recommended implementations call the Anthropic API and require user-supplied credentials; live-source fallbacks use WebFetch.
- Install/update: `npx -y skills@1.5.18 add anthropics/skills --skill claude-api -g -a claude-code -y --copy`

## `skill-creator`

Skill authoring and evaluation in Claude Code are the purpose of this plugin. It can create or revise a skill, design realistic trigger and output evaluations, compare controlled runs, inspect benchmark variance, improve the description, and package the result.

- Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator
- Installed at: `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/skill-creator/61414f8881f6/skills/skill-creator/SKILL.md`
- Available in: Claude Code
- License: Apache-2.0
- Trust notes: Bundles eight Python scripts, three evaluator-agent prompts, an HTML review UI, and packaging utilities. Evaluation and description optimization can spawn subagents, run the `claude` CLI, open a local viewer, and write benchmark workspaces; no hooks or MCP servers are installed.
- Install/update: `claude plugin install skill-creator@claude-plugins-official --scope user`
