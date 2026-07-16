# Optional and deferred tools

These tools were reviewed but not installed. Each item has a concrete reconsideration trigger so the catalog does not turn a deferred idea into an implied recommendation.

## `grill-me`

- Source: https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me
- Why deferred: Its one-question-at-a-time plan interrogation overlaps the installed Superpowers `brainstorming` workflow.
- Reconsider when: A plan needs a deliberately adversarial, user-invoked interview without producing a design document.
- Trust boundary: It reads project context and can consume substantial user attention, but it has no necessary external service; the main risk is duplicated planning process and conflicting gates.

## `claude-mem`

- Source: https://github.com/thedotmack/claude-mem
- Why deferred: Broad session capture overlaps existing context and project-record mechanisms.
- Reconsider when: Repeated cross-session loss is measured and the missing information cannot be handled with scoped project notes or built-in history.
- Trust boundary: A memory plugin observes and persists conversation and tool context. Installation must account for retention, secrets, personal data, storage location, deletion, hooks, and any remote model or network processing.

## Context Mode

- Source: https://github.com/mksglu/context-mode
- Why deferred: Context exhaustion has not been measured as a recurring problem, while the plugin adds global hooks, an MCP server, subprocess execution, and local SQLite state.
- Reconsider when: Real sessions repeatedly lose necessary context and a benchmark shows that indexed retrieval preserves the details this work needs.
- Trust boundary: Hooks intercept tool activity, sandbox commands and fetched content, and record session events in per-project SQLite. Review capture scope, subprocess isolation, upgrade behavior, purge behavior, and failure recovery before installation.

## `cloud-monitoring-metric-selection`

- Source: https://github.com/google/skills/blob/main/skills/cloud/cloud-monitoring-metric-selection/SKILL.md
- Why deferred: Its intended workflow configures a Google Cloud Monitoring MCP automatically, but this environment has no manually reviewed read-only Monitoring connection.
- Reconsider when: A project needs recurring metric discovery or query construction and a read-only Monitoring MCP is already configured with a bounded project and identity.
- Trust boundary: Monitoring access exposes production telemetry and resource labels. Keep credentials read-only, confirm project scope, and do not let a skill rewrite global MCP configuration without review.

## `vite`

- Source: https://github.com/antfu/skills/blob/main/skills/vite/SKILL.md
- Why deferred: Framework-specific Vite guidance is unnecessary for repositories that do not use Vite.
- Reconsider when: A maintained project contains Vite configuration, plugins, SSR, library builds, or a Vite 8 migration.
- Trust boundary: The skill is generated reference content, but following it can change build configuration and plugin dependencies. Confirm the installed Vite version before applying migration advice.

## `vitest`

- Source: https://github.com/antfu/skills/blob/main/skills/vitest/SKILL.md
- Why deferred: The current global catalog already has general Python and Playwright testing guidance; Vitest should be added only for a project that runs it.
- Reconsider when: A maintained repository uses Vitest for unit tests, mocking, fixtures, coverage, or test filtering.
- Trust boundary: Generated framework guidance may drift from the project's Vitest major version. Test commands execute project code, and coverage or snapshot updates write artifacts.

## `shadcn`

- Source: https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md
- Why deferred: No current catalog requirement depends on shadcn registries or presets.
- Reconsider when: A project has `components.json`, uses shadcn registries, or needs `shadcn init`, component addition, preset changes, or registry debugging.
- Trust boundary: The skill allows `npx`, `pnpm dlx`, or `bunx` to run the latest shadcn CLI. Registry and documentation content are mutable, and component commands write project files, so inspect the source registry and diff.

## `tailwind-design-system`

- Source: https://github.com/wshobson/agents/blob/main/plugins/frontend-mobile-development/skills/tailwind-design-system/SKILL.md
- Why deferred: It overlaps installed frontend and composition guidance and is specifically aimed at a Tailwind v4 design-system build.
- Reconsider when: A project is standardizing Tailwind v4 tokens, themes, component variants, dark mode, or a v3-to-v4 migration.
- Trust boundary: Guidance changes CSS architecture across the application and may add component dependencies. Confirm Tailwind major version and existing design tokens before applying it.

## `wcag-audit-patterns`

- Source: https://github.com/wshobson/agents/blob/main/plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md
- Why deferred: The installed web-design review covers routine accessibility checks; this larger workflow is justified only for formal WCAG 2.2 evidence.
- Reconsider when: Work requires a criterion-level audit trail, VPAT preparation, Section 508 evidence, or a documented manual screen-reader and keyboard test.
- Trust boundary: Automated scanners cover only part of WCAG, and the skill cannot certify legal compliance. Record tool versions, manual steps, assistive technology, residual risk, and reviewer qualifications.

## Community Docker skills

- Source: https://github.com/spencerpauly/awesome-cursor-skills#infrastructure--devops
- Why deferred: Reviewed candidates were generic or depended on specialist agents not present in Cursor. Installed Cloud Run and Google Cloud guidance covers the current container deployment needs.
- Reconsider when: A project has a concrete Docker problem such as multi-stage builds, Compose orchestration, image hardening, or local container debugging that existing guidance cannot answer.
- Trust boundary: Docker instructions can build and run untrusted images, mount host paths, expose ports, read environment secrets, and modify registries. A candidate must be inspected as a named skill, not installed as a whole community catalog.

## Community agent routers

- Source: https://github.com/wshobson/agents
- Why deferred: Reviewed routers assumed Claude-specific subagents and model aliases that did not match Cursor's available catalog.
- Reconsider when: A router discovers the live client agent and model inventory rather than embedding names, and its fallback behavior is tested in Cursor.
- Trust boundary: Routers can silently widen scope, choose expensive models, or dispatch agents that mutate shared files. Require an allowlist, explicit unavailable-agent handling, bounded concurrency, and no invented model names.

## Retired `next-best-practices`

- Source: https://github.com/vercel-labs/next-skills
- Why deferred: Vercel retired the standalone skill. Current Next.js guidance now ships as version-matched bundled documentation and agent rules generated by `next dev`.
- Reconsider when: Do not reinstall the retired skill. For an older Next.js release, use the documented `npx @next/codemod@canary agents-md` path or upgrade to a release that bundles the docs.
- Trust boundary: Framework advice must match the installed Next.js version. Prefer local `node_modules/next/dist/docs/` and generated `AGENTS.md` over a stale global copy.

## Karpathy behavioural guidelines (`andrej-karpathy-skills`)

- Source: https://github.com/forrestchang/andrej-karpathy-skills
- Why deferred: The four principles (think before coding, simplicity, surgical changes, goal-driven execution) already overlap the workspace `ponytail` rule and Superpowers TDD/verification skills. It is a `CLAUDE.md`/plugin policy file, not a domain skill.
- Reconsider when: A Claude Code-only project wants the plugin form without the Cursor `ponytail` rule, or measured over-editing persists after those rules.
- Trust boundary: Low; instruction-only. Installing it globally can fight existing laziness/surgical-edit rules if both are loaded.

## Sentry for AI (`getsentry/sentry-for-ai` / `@sentry/ai`)

- Source: https://docs.sentry.io/ai/agent-plugin/
- Why deferred: Installer wires a Sentry MCP and a large skill library; no active Sentry-driven debugging workflow was confirmed. Same class of deferral as `cloud-monitoring-metric-selection`.
- Reconsider when: A maintained app uses Sentry in production and needs agent-assisted issue triage with a reviewed, scoped Sentry auth.
- Trust boundary: MCP access exposes production errors, stack traces, and potentially PII in event payloads. Prefer explicit MCP setup over an installer that rewrites assistant config.

## Remaining Hookdeck provider webhook skills

- Source: https://github.com/hookdeck/webhook-skills
- Why deferred: Only `webhook-handler-patterns` and `stripe-webhooks` were installed (Stripe MCP is present). The other ~55 provider skills add catalog noise until that provider is in use.
- Reconsider when: Implementing Shopify, Clerk, Resend, GitHub, or another listed provider webhook in a maintained app.
- Trust boundary: Provider skills include signature verification and example handlers that touch secrets and inbound event data. Install one named skill at a time.

## `n8n-skills`

- Source: https://github.com/czlonkowski/n8n-skills
- Why deferred: Requires a configured `n8n-mcp` server and an n8n instance; neither is part of the current catalog stack.
- Reconsider when: An automation project uses n8n and `n8n-mcp` is already authenticated.
- Trust boundary: Plugin plus MCP can create and modify live workflows. Review hooks and MCP scope before install.

## `ui-ux-pro-max`

- Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Why deferred: Overlaps installed `frontend-design` and `web-design-guidelines`, plus existing frontend design user rules. Large style/palette databases add context cost for marginal gain.
- Reconsider when: A greenfield branding exercise needs searchable style/palette/font databases beyond the current design skills.
- Trust boundary: CLI installer writes skill assets from GitHub releases; prefer pinned/offline install and review generated files.

## Nimbalyst visual skills bundle

- Source: https://nimbalyst.com/skills/
- Why deferred: Skills target Nimbalyst editors (mockup/excalidraw/datamodel). They are not useful as standalone Cursor skills without that workspace.
- Reconsider when: The Nimbalyst app is adopted for visual mockups or ERDs.
- Trust boundary: Bundle is tied to a host application; evaluate the host separately from the skill markdown.

## Writing and marketing community skills

- Sources: Blog Writer / Writing Assistant (aiskill.market), `thesethrose/marketing-mode`, Blotato social relay, YouTube transcript, competitor ad analysis
- Why deferred: Writing needs are already covered by `humanizer` plus the SEO content skills. Marketing-mode is broad and mediocre for pure writing; social/YouTube/ad skills are adjacent, not core to the current catalog.
- Reconsider when: A recurring content workflow needs a specialist (long-form voice, social grader, ad-library analysis) that `humanizer` and `seo-content` cannot cover.
- Trust boundary: Marketplace and social skills often pull remote content or require third-party APIs. Inspect each named skill before install; do not install a whole marketing bundle.

## `remotion-best-practices`

- Source: https://github.com/remotion-dev/skills
- Why deferred: No maintained Remotion/programmatic-video project is active. Install at first Remotion scaffold, not prophylactically.
- Reconsider when: A project adds Remotion or starts generating video with React compositions.
- Trust boundary: Official Remotion guidance; render commands can be CPU/GPU heavy and write media artifacts.

## `changelog-generator`

- Source: community copies such as composiohq/awesome-claude-skills
- Why deferred: Thin wrapper over `git log` plus Keep a Changelog formatting; one audited Gen Trust Hub failure was observed on a popular listing. Not worth a global skill until release-note volume justifies it.
- Reconsider when: Multiple apps need the same user-facing changelog voice and a single inspected source passes trust review.
- Trust boundary: Reads git history and can write `CHANGELOG.md`. Prefer a named, inspected skill over an entire awesome-skills dump.
