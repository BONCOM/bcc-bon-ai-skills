---
type: Agent Skill
title: firebase-firestore
description: "Any Firestore work should start here, including database discovery, edition selection, schema design, indexes, security rules, and client queries. The skill requires identifying Standard or Enterprise edition before choosing references because supported query and data-model features differ."
resource: "https://github.com/firebase/agent-skills/blob/main/skills/firebase-firestore/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-07-16T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor and Claude Code
---

Any Firestore work should start here, including database discovery, edition selection, schema design, indexes, security rules, and client queries. The skill requires identifying Standard or Enterprise edition before choosing references because supported query and data-model features differ.

# When to use

Any Firestore work should start here, including database discovery, edition selection, schema design, indexes, security rules, and client queries. The skill requires identifying Standard or Enterprise edition before choosing references because supported query and data-model features differ.

# Installed at

- `~/.claude/skills/firebase-firestore/SKILL.md`
- `~/.agents/skills/firebase-firestore/SKILL.md`

# Availability

Cursor and Claude Code

# License

Apache-2.0

# Trust notes

Instruction and reference files invoke `npx firebase-tools@latest`; authenticated commands can list or create databases and deploy rules or indexes. No credentials are bundled.

# Install / update

```text
`npx -y skills@1.5.18 add firebase/agent-skills --skill firebase-firestore -g -a claude-code -y --copy`
```

# Citations

[1] [firebase-firestore source](https://github.com/firebase/agent-skills/blob/main/skills/firebase-firestore/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
