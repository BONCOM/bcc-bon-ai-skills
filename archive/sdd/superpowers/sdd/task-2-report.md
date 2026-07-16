---
type: Archive
title: task 2 report
description: Legacy catalog or SDD artifact retained for history; prefer live OKF concepts under /skills/.
tags: [archive, legacy]
timestamp: 2026-07-16T00:00:00Z
---

# Task 2 — normal skill security/trust inspection

**Status:** `DONE_WITH_CONCERNS`  
**Inspection date:** 2026-07-16  
**Scope:** The 17 exact allowlisted normal skills only. No skill was installed, no plugin state was changed, no CodeQL command was run, and no project repository was modified.

## Method

1. Ran every prescribed `npx -y skills@1.5.18 add <repo> --list` command sequentially.
2. Shallow-cloned each of the eight source repositories to the one `mktemp` review directory, inspected the selected `SKILL.md` files, enumerated their sibling files, reviewed every sibling executable (the two Node example files), and searched selected package content for executable-download and credential/network indicators.
3. Recorded repository root license, latest shallow-clone commit, and clean clone status.
4. Removed the review directory using a path-guarded deletion and verified absence.

`addyosmani/agent-skills` has an additional `.opencode/skills` mirror for its four selected names. SHA-1 comparisons showed each mirror is byte-identical to the canonical `skills/` path, so this is not an ambiguous behavioral duplicate.

## Step 1 — prescribed listing results

| Sequential command | Result |
|---|---|
| `npx -y skills@1.5.18 add trailofbits/skills --list` | Exit 0; 75 skills. Listed `supply-chain-risk-auditor` and `codeql`. |
| `npx -y skills@1.5.18 add addyosmani/agent-skills --list` | Exit 0; 24 skills. Listed `security-and-hardening`, `observability-and-instrumentation`, `ci-cd-and-automation`, and `performance-optimization`. |
| `npx -y skills@1.5.18 add wshobson/agents --list` | Exit 0; 175 skills. Listed `python-testing-patterns`. |
| `npx -y skills@1.5.18 add currents-dev/playwright-best-practices-skill --list` | Exit 0; one skill. Listed `playwright-best-practices`. |
| `npx -y skills@1.5.18 add vercel-labs/agent-skills --list` | Exit 0; nine skills. Listed `vercel-composition-patterns`. |
| `npx -y skills@1.5.18 add antfu/skills --list` | Exit 0; 19 skills. Listed `vue`. |
| `npx -y skills@1.5.18 add mcollina/skills --list` | Exit 0; 11 skills. Listed `node`. |
| `npx -y skills@1.5.18 add google/skills --list` | Exit 0; 78 skills. Listed `gcloud`, `google-cloud-recipe-auth`, `cloud-logging-query-generation`, `google-cloud-waf-security`, `google-cloud-waf-operational-excellence`, and `google-cloud-solution-architecture`. |

## Step 3 — inspection decisions

“No declared tools” means the front matter did not declare an `allowed-tools` field. Commands and network activity below are capabilities documented for a later, explicit use of the skill; none occurred during this inspection.

| Skill | Canonical source path | License | Scripts / executable code | Tools, network, and API requirements | Maintenance evidence | Decision | Rationale |
|---|---|---|---|---|---|---|---|
| `supply-chain-risk-auditor` | `trailofbits__skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md` | CC BY-SA 4.0 | No executable code; template, SVG, and display YAML only | Declares `Read Write Bash Glob Grep`; requires `gh` to query public GitHub metadata and writes a workspace report | `cfe5d7b`, 2026-06-30 | APPROVE_WITH_CONCERN | Purpose matches content and no hidden download exists. It can write a report and make authenticated `gh` requests when invoked, so use only for an explicit audit. |
| `security-and-hardening` | `addyosmani__agent-skills/skills/security-and-hardening/SKILL.md` | MIT | SKILL.md only | No declared tools; guidance references package-manager audits and external services but contains no executable downloader | `c1974de`, 2026-07-16 | APPROVE | Security guidance matches purpose; mirror is byte-identical and no code is bundled. |
| `observability-and-instrumentation` | `addyosmani__agent-skills/skills/observability-and-instrumentation/SKILL.md` | MIT | SKILL.md only | No declared tools; documents telemetry integrations but does not contact a telemetry service itself | `c1974de`, 2026-07-16 | APPROVE | Read-only guidance with explicit PII/secret-redaction advice; mirror is byte-identical. |
| `ci-cd-and-automation` | `addyosmani__agent-skills/skills/ci-cd-and-automation/SKILL.md` | MIT | SKILL.md only | No declared tools; examples can deploy or install Playwright if a user later adopts them | `c1974de`, 2026-07-16 | APPROVE_WITH_CONCERN | Matches CI/CD purpose and contains no executable package code, but generated CI can have deployment effects and must remain review-gated. Mirror is byte-identical. |
| `performance-optimization` | `addyosmani__agent-skills/skills/performance-optimization/SKILL.md` | MIT | SKILL.md only | No declared tools; examples reference Lighthouse, CrUX/RUM, and optional `npx` tools | `c1974de`, 2026-07-16 | APPROVE | Guidance-only and measurement-first; no credentials, download scripts, or hidden network behavior. Mirror is byte-identical. |
| `python-testing-patterns` | `wshobson__agents/plugins/python-development/skills/python-testing-patterns/SKILL.md` | MIT | No executable code; two Markdown references | No declared tools; examples mention optional `pip install pytest-cov`/test dependencies | `b6af371`, 2026-07-14 | APPROVE | Matches Python-testing purpose; optional dependency installation is instructional, not automatic. |
| `playwright-best-practices` | `currents-dev__playwright-best-practices-skill/SKILL.md` | MIT | No scripts; 80+ Markdown references and one validation workflow | No declared tools; reference examples can run Playwright, Docker images, Lighthouse, test APIs, and use environment-provided test credentials | `ef329e7`, 2026-03-13 | APPROVE_WITH_CONCERN | Comprehensive test guidance is in scope and has no bundled executable. Invocation can create browser/network traffic or update snapshots, so it needs an explicit target and test-data boundaries. |
| `codeql` | `trailofbits__skills/plugins/static-analysis/skills/codeql/SKILL.md` | CC BY-SA 4.0 | No executable code; Markdown workflows/references and display YAML only | Declares `Bash Read Write Edit Glob Grep` plus task/todo tools; requires separately installed CodeQL and may create analysis artifacts; references optional query packs | `cfe5d7b`, 2026-06-30 | APPROVE_MANUAL_ONLY | Purpose matches and workflows require a pre-existing CLI rather than downloading it. Preserve the plan constraint: do not install or run CodeQL automatically. |
| `vercel-composition-patterns` | `vercel-labs__agent-skills/skills/composition-patterns/SKILL.md` | MIT declared in SKILL.md; no repository-root LICENSE located | No executable code; Markdown rules, metadata, README, and AGENTS.md | No declared tools or network/API requirement | `f8a72b9`, 2026-06-10 | APPROVE_WITH_CONCERN | Guidance-only React composition content matches purpose. The declared per-skill MIT license is sufficient for this documentation-only package, but root-license absence should be rechecked on future updates. |
| `vue` | `antfu__skills/skills/vue/SKILL.md` | MIT | No executable code; generation note and three Markdown references | No declared tools; source is generated from Vue docs, but installed content performs no network action | `a74f281`, 2026-06-23 | APPROVE | Purpose and Vue 3 guidance match; no scripts or credentials. |
| `node` | `mcollina__skills/skills/node/SKILL.md` | MIT | Two inspected TypeScript example files: local HTTP graceful-shutdown example and localhost-only test; neither runs on install | No declared tools; reference examples can use npm/npx/fetch and recommend packages, but no automatic download or API key access | `879c9de`, 2026-07-16 | APPROVE_WITH_CONCERN | Bundled code is licensed and benign, but the example server listens on `0.0.0.0:3000` if deliberately executed. Use examples only under normal local-development review. |
| `gcloud` | `google__skills/skills/cloud/gcloud/SKILL.md` | Apache-2.0 | SKILL.md only | No declared tools; requires Google Cloud CLI and user authentication for later cloud actions; explicitly mandates help validation, explicit project/location, `--quiet`, dry runs, and denies autonomous IAM/delete/billing/KMS actions | `13247c7`, 2026-07-16 | APPROVE_WITH_CONCERN | High-trust control guidance matches purpose and contains strong safeguards, but it can operate on authenticated cloud resources when explicitly invoked. |
| `google-cloud-recipe-auth` | `google__skills/skills/cloud/google-cloud-recipe-auth/SKILL.md` | Apache-2.0 | SKILL.md only | No declared tools; explains `gcloud auth login`, ADC, impersonation, and service-account choices; no credential reads or commands in package | `13247c7`, 2026-07-16 | APPROVE_WITH_CONCERN | Auth guidance discourages static keys and favors short-lived or attached identities. It is advice-only but concerns sensitive credential workflows. |
| `cloud-logging-query-generation` | `google__skills/skills/cloud/cloud-logging-query-generation/SKILL.md` | Apache-2.0 | No executable code; 21 Markdown LQL/service references | No declared tools; produces LQL text only and does not query Cloud Logging itself | `13247c7`, 2026-07-16 | APPROVE | Purpose matches generated-query-only behavior; no API key, credential, or network requirement. |
| `google-cloud-waf-security` | `google__skills/skills/cloud/google-cloud-waf-security/SKILL.md` | Apache-2.0 | SKILL.md only | No declared tools; documentation grounding URLs only, no automatic fetch/action | `13247c7`, 2026-07-16 | APPROVE | Advisory Well-Architected Framework security checklist; no executable or mutable access. |
| `google-cloud-waf-operational-excellence` | `google__skills/skills/cloud/google-cloud-waf-operational-excellence/SKILL.md` | Apache-2.0 | SKILL.md only | No declared tools; documentation grounding URLs only, no automatic fetch/action | `13247c7`, 2026-07-16 | APPROVE | Advisory operations framework guidance; no executable or mutable access. |
| `google-cloud-solution-architecture` | `google__skills/skills/cloud/google-cloud-solution-architecture/SKILL.md` | Apache-2.0 | No executable code; three Markdown reference indexes and output template | No declared tools; directs later grounding via Google Developer Knowledge MCP and official docs, requires approval before validation and writing workspace files | `13247c7`, 2026-07-16 | APPROVE_WITH_CONCERN | Matches architecture-design purpose and includes approval gates. It invokes a live documentation MCP only during a later architecture task, so recommendations are mutable and must be citation-reviewed. |

## Network/download and credential review

- No selected package contains an executable downloader (`curl`, `wget`, package installer, or clone script) that runs as part of its package.
- The selected skills do not read local credential files. `gcloud` and the auth recipe document authentication flows; supply-chain auditing can call `gh` when deliberately used; Playwright examples can exercise configured test endpoints; CodeQL may resolve already installed packs.
- `node` contains the only selected sibling source code. The two TypeScript files were read: one starts a local demonstration HTTP server only when executed directly; its test sends requests only to a random local port.

## Step 4 — cleanup evidence

- Review directory created by `mktemp`: `/var/folders/h4/fp2jq4rn4xnfmrmscn2zbrf40000gp/T/ai-skills-review.HNI2cd`.
- Eight shallow clones completed and all were clean (`git status --porcelain` empty).
- The literal plan guard initially refused deletion because this macOS `TMPDIR` ends in `/`, while `mktemp` normalized the doubled separator in its printed path. I retained the exact printed path and normalized only the guard prefix (`${TMPDIR%/}`); its `case` still accepted only `${tmp_root}/ai-skills-review.*`.
- Guarded removal reported `removed: /var/folders/h4/fp2jq4rn4xnfmrmscn2zbrf40000gp/T/ai-skills-review.HNI2cd`; `test ! -e` succeeded.

## Self-review

- All 17 exact names were found in the required sequential listings and mapped to one canonical source path.
- All selected `SKILL.md` files were read. Every sibling file was enumerated; all sibling executable code was read. Reference trees were searched for command, download, credential, API, and network indicators.
- No rejected name was substituted. No installation, plugin mutation, Git initialization, or modification outside this report occurred.

## Concerns to carry forward

1. `codeql` is trusted for manual use only; Task 2 must not cause the CLI or its packs to be installed or run.
2. `gcloud`, `supply-chain-risk-auditor`, Playwright guidance, and generated CI can produce authenticated, network, browser, or deployment side effects only after an explicit user request and target confirmation.
3. `vercel-composition-patterns` declares MIT in its `SKILL.md`, but its repository clone lacked a root license file. This is acceptable here because the selected package contains documentation only, but should be revalidated before any future package with executable content is accepted.
