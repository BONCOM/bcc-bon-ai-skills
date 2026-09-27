---
type: Agent Skill
title: bcc-bon-solutions
description: "The Boncom Solutions team toolkit: takes an idea to a live Boncom Suite app, builds or checks UI against the Boncom internal apps design system, wires central auth, deploys to Cloud Run on *.boncomsuite.com, ships releases, runs a doctor health check, and enforces bcc-bon- repo naming."
resource: "https://github.com/BONCOM/bcc-bon-solutions-skills/blob/main/bcc-bon-solutions/SKILL.md"
tags: [boncom, installed, authored]
timestamp: 2026-09-27T00:00:00Z
category: boncom
license: Proprietary (Boncom internal)
available_in: Cursor and Claude Code
upstream_version: "fa37f10"
---

Boncom-authored, and the first in-house skill in this catalog. One entry point with six modes: **New app** (repo, golden-path scaffold, Boncom UI and entry pages, central auth, docs, doctor, deploy, ship), **Design** (build with the design system, score an app against every guideline, or copy the exact sign-in / 404 / 403 / 500 / maintenance pages), **Auth** (central auth at `auth.boncomsuite.com` by audience and stack), **Deploy and ship** (Cloud Run resource profiles, the team Cloud Build format, Secret Manager, `deploy.sh` / `add-subdomain.sh`, version, changelog, Suite hub listing, release note), **Doctor** (read-only PASS/WARN/FAIL scorecard for a machine and an app), and **Repo** (`bcc-bon-*` naming, team access, stale remotes). It reads `bcc-bon-internal-app-design`, `bcc-bon-suite-deployment-tech` and `bcc-bon-boncom_suite/auth` live rather than copying them.

# When to use

Any Boncom Suite work: starting a new internal app, building or reviewing its UI, adding sign-in, deploying or redeploying to Cloud Run, publishing a release, creating a BONCOM repo, or checking that an app is set up the way the team ships. It loads automatically on those requests; say "bcc-bon-solutions" to force it.

# Installed at

- `~/.claude/skills/bcc-bon-solutions` (symlink to a clone of `BONCOM/bcc-bon-solutions-skills`)

# Availability

Cursor and Claude Code

# License

Proprietary, Boncom internal.

# Trust notes

Authored by the Solutions team; no third-party code. Instructions plus two scripts:
- `scripts/doctor.sh` is read-only (gcloud, gh, git, grep, find). It runs `gh api` GETs and `gcloud` reads; it changes nothing. `--self-check` tests its parsing offline.
- `scripts/adherence.eslint.mjs` is an ESLint flat config that runs the design system's adherence rules with the app's own ESLint and parser; it installs and writes nothing.

The skill's source lookup clones the three BONCOM source repos into `~/.cache/bcc-bon/` when there's no local checkout, and fast-forwards clean local clones. Every action that reaches production (`deploy.sh`, `add-subdomain.sh`, `gh repo create`, renames, PRs in other repos) is shown first and runs only after the user says yes; registry, IAM and API changes are left to the user.

# Install / update

```text
cd ~/Documents/Code_Projects && gh repo clone BONCOM/bcc-bon-solutions-skills
ln -s "$PWD/bcc-bon-solutions-skills/bcc-bon-solutions" ~/.claude/skills/bcc-bon-solutions
# update
git -C ~/Documents/Code_Projects/bcc-bon-solutions-skills pull
```

Not installed through `skills@…`; it's an internal repo.

# Related

- Category index: [/skills/boncom/index.md](/skills/boncom/index.md)
- Design system it applies: `BONCOM/bcc-bon-internal-app-design`
- Pairs with: [`cloud-run-basics`](/skills/development/cloud-run-basics.md), [`gcloud`](/skills/development/gcloud.md), [`better-auth-best-practices`](/skills/development/better-auth-best-practices.md), [`claude-api`](/skills/development/claude-api.md)

# Citations

[1] [bcc-bon-solutions source](https://github.com/BONCOM/bcc-bon-solutions-skills/blob/main/bcc-bon-solutions/SKILL.md)
