---
type: Agent Skill
title: frontend-design-review
description: "Review and create distinctive, production-grade frontend interfaces with high design quality and design system compliance. Evaluates using three pillars: frictionless insight-to-action, quality craft, and trustworthy building."
resource: "https://github.com/microsoft/skills/blob/main/.github/skills/frontend-design-review/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-07-22T00:00:00Z
category: development
group: Frontend and UI
license: MIT
available_in: Cursor and Claude Code
---

Two modes: review existing UI against design-system compliance and a three-pillar quality framework (frictionless insight-to-action, quality craft, trustworthy building) — PR reviews, accessibility audits, component reviews, theme testing — or create distinctive new interfaces that avoid generic "AI slop" aesthetics. Explicitly excludes backend, database, infra/DevOps, and pure business-logic work. Complements [`frontend-design`](/skills/development/frontend-design.md) (creation-focused) rather than duplicating it; credits Anthropic's `frontend-design` skill as a creative-principles inspiration in its own frontmatter.

# When to use

Reviewing or building frontend UI where design quality, accessibility, or design-system compliance matters — not for backend, database, or infra work.

# Installed at

- `~/.claude/skills/frontend-design-review/SKILL.md`
- `~/.agents/skills/frontend-design-review/SKILL.md`

# Availability

Cursor and Claude Code (Cursor reads the same `~/.claude/skills/` path — no separate Cursor-native cache entry exists or is needed for this skill).

# License

MIT (repo-wide)

# Trust notes

Instruction-only; no bundled scripts, no network calls beyond two attribution links in the frontmatter/body. `microsoft/skills` is the verified Microsoft org account — 2.8k stars / 315 forks over ~6 months, consistent organic growth for an org repo (not the inflated-star pattern seen in several unrelated single-author "token optimizer" repos evaluated the same day). The parent repo is otherwise mostly Azure SDK skills not relevant to this catalog's GCP/Vercel/Supabase-centric stack; only this one skill was installed. Snyk: Low Risk, Socket: 0 alerts, Gen: Safe. Verified local `SKILL.md` byte-matches upstream.

# Install / update

```text
npx -y skills@1.5.18 add microsoft/skills --skill frontend-design-review -g -a claude-code -y --copy
```

# Citations

[1] [frontend-design-review source](https://github.com/microsoft/skills/blob/main/.github/skills/frontend-design-review/SKILL.md)

# Related

- [`frontend-design`](/skills/development/frontend-design.md) — creation-focused counterpart
- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
