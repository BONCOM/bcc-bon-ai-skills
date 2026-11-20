---
type: Agent Skill
title: firebase-firestore
description: "Sets up, manages, queries, and configures Cloud Firestore databases (Standard/Enterprise edition), including data modeling, security rules, indexes, and SDK integrations (Web, Python, iOS, Android, Flutter). Explicitly out of scope: Firebase Hosting, Data Connect, Auth, Storage/GCS, Crashlytics, Functions, or BigQuery — those route to sibling skills instead."
resource: "https://github.com/firebase/agent-skills/blob/main/skills/firebase-firestore/SKILL.md"
tags: [development, installed, google-cloud]
timestamp: 2026-11-03T00:00:00Z
category: development
group: Google Cloud
license: Apache-2.0
available_in: Cursor, Claude Code, Codex and Antigravity
---

Sets up, manages, queries, and configures Cloud Firestore databases (Standard/Enterprise edition), including data modeling, security rules, indexes, and SDK integrations (Web, Python, iOS, Android, Flutter). Requires identifying Standard or Enterprise edition before choosing references because supported query and data-model features differ.

# When to use

Any Firestore work — creating/listing databases, defining data models/indexes, writing SDK queries, or integrating Firestore SDKs. Does not cover Firebase Hosting, Data Connect, Auth, Storage/GCS, Crashlytics, Functions, or BigQuery.

# Installed at

- `~/.claude/skills/firebase-firestore/SKILL.md`
- `~/.agents/skills/firebase-firestore/SKILL.md`
- `~/.gemini/config/skills/firebase-firestore` (symlink to the Claude Code copy, read by Antigravity)

# Availability

Cursor, Claude Code, Codex and Antigravity

# License

Apache-2.0

# Trust notes

Instruction and reference files invoke `npx firebase-tools@latest`; authenticated commands can list or create databases and deploy rules or indexes. No credentials are bundled. Picked up a `metadata.category: Databases` frontmatter tag (repo-wide category pass); no body content changed. 2026-11-03 (`b76be96`, with `09fe6d6` 2026-10-30): the description now covers the Admin SDK and app migrations; the security-rules note requires `firebase.json` to point at `firestore.rules` and the rules to be deployed (`npx -y firebase-tools@latest deploy --only firestore:rules`) even when server routes use the Admin SDK; adds Vector Search and Full-Text Search pipeline references for the Enterprise Web SDK.

# Install / update

```text
`npx -y skills@1.5.18 add firebase/agent-skills --skill firebase-firestore -g -a claude-code -y --copy`
```

# Citations

[1] [firebase-firestore source](https://github.com/firebase/agent-skills/blob/main/skills/firebase-firestore/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
