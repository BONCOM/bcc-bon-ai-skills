---
type: Agent Skill
title: solutions-r2d2
description: "The Boncom Solutions team toolkit (Solutions R2-D2): takes an idea to a live Boncom Suite app, builds or checks UI against the Boncom internal apps design system, wires central auth, adds per-role practice accounts, deploys to Cloud Run on *.boncomsuite.com, ships releases, runs a doctor health check and a security scan, and enforces bcc-bon- repo naming."
resource: "https://github.com/BONCOM/bcc-bon-solutions-skills/blob/main/solutions-r2d2/SKILL.md"
tags: [boncom, installed, authored]
timestamp: 2026-10-03T00:00:00Z
category: boncom
license: Proprietary (Boncom internal)
available_in: Cursor and Claude Code
upstream_version: "2.1.0 (f7356b4)"
---

Boncom-authored, and the first in-house skill in this catalog. Renamed from `bcc-bon-solutions` to **Solutions R2-D2** in 2.0.0 (2026-09-28); call it with `/solutions-r2d2`. 2.1.0 (2026-10-03) speeds up the deep security scan with free scanners and helper agents, checks deploys before they run, keeps Dependabot and malware alerts on, flags new package versions, and follows central auth's move to Better Auth 1.7. One entry point with eight modes: **New app** (repo, golden-path scaffold, Boncom UI and entry pages, central auth, docs, doctor, deploy, ship), **Design** (build with the design system, score an app against every guideline, or copy the exact sign-in / 404 / 403 / 500 / maintenance pages), **Auth** (central auth at `auth.boncomsuite.com` by audience and stack, including the `me-profile` endpoint for job title, department and office), **Test accounts** (admin-only practice accounts per role with private sandboxes and a "Test mode" banner), **Deploy and ship** (Cloud Run resource profiles, the team Cloud Build format, Secret Manager, `deploy.sh` / `add-subdomain.sh`, version, changelog, Suite hub listing, release note), **Doctor** (read-only PASS/WARN/FAIL scorecard for a machine and an app), **Security scan** (leaked keys, open doors, risky packages, sign-in gaps; quick, latest-changes or deep), and **Repo** (`bcc-bon-*` naming, team access, stale remotes). It reads `bcc-bon-internal-app-design`, `bcc-bon-suite-deployment-tech` and `bcc-bon-boncom_suite/auth` live rather than copying them.

# When to use

Any Boncom Suite work: starting a new internal app, building or reviewing its UI, adding sign-in, deploying or redeploying to Cloud Run, publishing a release, creating a BONCOM repo, checking an app is set up the way the team ships, or checking it is safe. It loads automatically on those requests; say "solutions-r2d2" to force it.

# Installed at

- `~/.claude/skills/solutions-r2d2` (symlink to `~/Documents/Code_Projects/bcc-bon-solutions-skills/solutions-r2d2`, a clone of `BONCOM/bcc-bon-solutions-skills`)
- The repo also keeps a `bcc-bon-solutions -> solutions-r2d2` compatibility link for pre-2.0 installs.

# Availability

Cursor and Claude Code

# License

Proprietary, Boncom internal.

# Trust notes

Authored by the Solutions team. Instructions plus two scripts and one template set:
- `scripts/doctor.sh` is read-only (gcloud, gh, git, grep, find). It runs `gh api` GETs and `gcloud` reads; it changes nothing. `--self-check` tests its parsing offline; `--check-update` (run once per conversation) reports whether a newer skill version is out.
- `scripts/adherence.eslint.mjs` is an ESLint flat config that runs the design system's adherence rules with the app's own ESLint and parser; it installs and writes nothing.
- `templates/test-accounts/` is a copy of Estimate Creator code (server middleware, admin components) that the Test accounts mode copies into an app; it's meant to be dropped once that code lands on `main` upstream.

The skill's source lookup (`bcc_src`) fast-forwards clean local clones of the three BONCOM source repos, or keeps shallow clones in `~/.cache/bcc-bon/`. A deep security scan writes its output to `~/.cache/bcc-bon/security/<app>/`, never into the repo, and uses [`supply-chain-risk-auditor`](/skills/development/supply-chain-risk-auditor.md) when installed. Every action that reaches production (`deploy.sh`, `add-subdomain.sh`, `gh repo create`, renames, history rewrites, PRs in other repos) is shown first and runs only after the user says yes; registry, API-enablement and IAM changes are left to the user. The skill opens its first reply with a Star Wars-style text banner.

# Install / update

```text
cd ~/Documents/Code_Projects && gh repo clone BONCOM/bcc-bon-solutions-skills
rm -f ~/.claude/skills/bcc-bon-solutions
ln -s "$PWD/bcc-bon-solutions-skills/solutions-r2d2" ~/.claude/skills/solutions-r2d2
# update
git -C ~/Documents/Code_Projects/bcc-bon-solutions-skills pull
```

Not installed through `skills@…`; it's an internal repo, so it has no entry in `~/.agents/.skill-lock.json`. To refresh it, `git pull` the clone; the symlink picks up the new version immediately.

# Related

- Category index: [/skills/boncom/index.md](/skills/boncom/index.md)
- Design system it applies: `BONCOM/bcc-bon-internal-app-design`
- Pairs with: [`cloud-run-basics`](/skills/development/cloud-run-basics.md), [`gcloud`](/skills/development/gcloud.md), [`supply-chain-risk-auditor`](/skills/development/supply-chain-risk-auditor.md), [`better-auth-best-practices`](/skills/development/better-auth-best-practices.md)

# Citations

[1] [solutions-r2d2 source](https://github.com/BONCOM/bcc-bon-solutions-skills/blob/main/solutions-r2d2/SKILL.md)
[2] [Changelog](https://github.com/BONCOM/bcc-bon-solutions-skills/blob/main/CHANGELOG.md)
