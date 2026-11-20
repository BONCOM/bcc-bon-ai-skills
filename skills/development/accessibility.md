---
type: Agent Skill
title: accessibility
description: "Audit rendered UI for WCAG 2.2 issues with Lighthouse or axe, an accessibility-tree snapshot, and a keyboard walkthrough. Re-run the checks after remediation."
resource: "https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/skills/accessibility/SKILL.md"
tags: [development, installed, frontend-and-ui]
timestamp: 2026-11-20T14:45:10-07:00
category: development
group: Frontend and UI
license: MIT
available_in: Claude Code, Gemini CLI, Codex, and Antigravity
---

# When to use

Audit rendered UI for WCAG 2.2 issues with Lighthouse or axe, an accessibility-tree snapshot, and a keyboard walkthrough. Re-run the checks after remediation.

# Installed at

- `~/.claude/skills/accessibility/SKILL.md`
- `~/.agents/skills/accessibility/SKILL.md`
- `~/.gemini/config/skills/accessibility/SKILL.md`

# Trust notes

Markdown and WCAG references. Live checks use existing browser tooling or optional Lighthouse and axe commands. Automated results cover a subset of accessibility barriers.

License MIT. Installed files match the reviewed upstream revision `afa8da9421`.

# Install or update

```bash
npx -y skills@1.5.18 add addyosmani/web-quality-skills --skill accessibility -g -a claude-code gemini-cli codex -y --copy
ln -s ~/.claude/skills/accessibility ~/.gemini/config/skills/accessibility  # First install on Antigravity
```

# Sources

- [Upstream SKILL.md](https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/skills/accessibility/SKILL.md)
- [Routing playbook](/playbooks/agent-selection.md)
