---
type: Agent Skill
title: codeql
description: "An explicit CodeQL request is required before using this skill, whether the task is building a database, running a suite, adding data-extension models, or processing SARIF. It checks database extraction quality before treating a scan as valid and treats zero findings as a result that still needs val"
resource: "https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/codeql/SKILL.md"
tags: [development, installed, development-quality]
timestamp: 2026-08-19T00:00:00Z
category: development
group: Development quality
license: CC-BY-SA-4.0
available_in: Cursor and Claude Code
---

An explicit CodeQL request is required before using this skill, whether the task is building a database, running a suite, adding data-extension models, or processing SARIF. It checks database extraction quality before treating a scan as valid and treats zero findings as a result that still needs validation.

# When to use

An explicit CodeQL request is required before using this skill, whether the task is building a database, running a suite, adding data-extension models, or processing SARIF. It checks database extraction quality before treating a scan as valid and treats zero findings as a result that still needs validation.

# Installed at

- `~/.claude/skills/codeql/SKILL.md`

# Availability

Cursor and Claude Code

# License

CC-BY-SA-4.0

# Trust notes

Declares Bash, Read, Write, Edit, Glob, Grep, and task tools. It requires a separately installed CodeQL CLI, may run project builds or resolve query packs, and writes databases, logs, extensions, and SARIF; keep it manually invoked. Guard scripts and their tests were reworked to be real (not stubbed) checks — `check_db_quality.py`, `find_databases.sh`, `verify_query_suite.py`, and 9 accompanying test files were all updated. Refreshed 2026-08-19: build-fixes/quality-assessment references now run analysed-project pip installs under documented `allow-legacy-python` exceptions (the shims otherwise push `uv run`), and the sibling `sarif-parsing` skill's tool-selection table switched to `uv run --with` invocations.

# Install / update

```text
`npx -y skills@1.5.18 add trailofbits/skills --skill codeql -g -a claude-code -y --copy`
```

# Citations

[1] [codeql source](https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/codeql/SKILL.md)

# Related

- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)
- Category index: [/skills/development/index.md](/skills/development/index.md)
