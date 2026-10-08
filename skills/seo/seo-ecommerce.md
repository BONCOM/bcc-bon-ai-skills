---
type: Agent Skill
title: seo-ecommerce
description: "Product-page SEO, Product schema, marketplace visibility, pricing comparisons, and Shopping or Amazon keyword gaps are handled here. The base mode audits the page directly; richer market analysis is added only when the DataForSEO Merchant API is available."
resource: "https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-ecommerce/SKILL.md"
tags: [seo, installed]
timestamp: 2026-10-04T00:00:00Z
category: seo
license: MIT
available_in: Cursor and Claude Code
---

Product-page SEO, Product schema, marketplace visibility, pricing comparisons, and Shopping or Amazon keyword gaps are handled here. The base mode audits the page directly; richer market analysis is added only when the DataForSEO Merchant API is available.

# When to use

Product-page SEO, Product schema, marketplace visibility, pricing comparisons, and Shopping or Amazon keyword gaps are handled here. The base mode audits the page directly; richer market analysis is added only when the DataForSEO Merchant API is available.

# Installed at

- `~/.claude/skills/seo-ecommerce/SKILL.md`

# Availability

Cursor and Claude Code

# License

MIT

# Trust notes

Base checks fetch product pages and validate markup. Shopping, Amazon, pricing, and gap commands use paid DataForSEO Merchant endpoints and therefore create live network calls and possible API charges.

# Install / update

```text
`npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-ecommerce -g -a claude-code -y --copy`
```

# Citations

[1] [seo-ecommerce source](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-ecommerce/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/seo/index.md](/skills/seo/index.md)
