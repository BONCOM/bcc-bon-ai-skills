# Agent selection

Use the narrowest capability that can finish the task. A skill supplies domain instructions; an agent gets a separate context and can perform a bounded workstream. They are not interchangeable.

## Routing policy

- Narrow repository lookup -> direct Glob, rg, and ReadFile tools
- Broad codebase exploration -> `explore`
- Command-heavy work -> `shell`
- Browser flows and UI verification -> `browser-use`
- One failed PR check -> `ci-investigator`
- Explicit local change review -> `bugbot`
- Explicit security review -> `security-review`
- SEO task -> the narrowest matching `seo-*` specialist
- Supabase product/Auth/RLS/MCP work -> `supabase`; pure Postgres performance -> `supabase-postgres-best-practices`
- Webhook handlers -> `webhook-handler-patterns`; Stripe events -> `stripe-webhooks`
- Independent workstreams -> `dispatching-parallel-agents`
- Approved implementation plan -> `subagent-driven-development` or `executing-plans`

## Rules

Prefer direct tools over an agent for narrow work. Reading a known file, finding one symbol, or running one command does not need a separate agent context.

Never invent an unavailable agent or model name. Choose only from the agent and model catalogs exposed by the current client session; if the requested option is absent, report that plainly.

Use `explore` when the answer requires tracing several code areas or naming conventions. Use `shell` when command execution is the work rather than a small verification step.

Reserve `bugbot` and `security-review` for explicit user requests. A normal implementation review should use the project's usual reviewer or `requesting-code-review`, not silently substitute one of these specialized reviewers.

For SEO, start with the specific installed skill: `seo-schema` for structured data, `seo-hreflang` for international targeting, `seo-google` for Google API evidence, or another exact match. Use the broad `seo` skill only for multi-discipline work or uncertain routing.

Parallelize only independent work. If tasks edit the same files, depend on the same mutable service, or need the result of an earlier task, keep them sequential.
