# AI Skills catalog

This directory records the agent skills installed separately from Cursor and Claude Code. It answers four practical questions: what a skill is for, where it came from, where it is installed, and what it can touch when invoked. App-bundled capabilities are outside this inventory.

The final unique count is `31 development + 31 SEO + 1 writing + 14 Superpowers = 77`.

## Catalog documents

- [README.md](README.md): scope, counts, discovery, maintenance, and recovery
- [development.md](development.md): development quality, frontend, Node.js, Google Cloud, and skill-authoring entries
- [seo.md](seo.md): all 31 installed Claude SEO skills
- [writing.md](writing.md): the installed Humanizer skill
- [superpowers.md](superpowers.md): the Superpowers plugin and its 14 unique skills
- [agent-selection.md](agent-selection.md): routing between direct tools, agents, and installed skills
- [optional-tools.md](optional-tools.md): reviewed tools that were deliberately not installed

The approved rationale and trust boundaries are in [the catalog design](docs/2026-07-16-ai-skills-catalog-design.md).

## Discovery and counting

Normal skills live under `~/.claude/skills/`. Cursor reads this Claude compatibility path, so the 17 new normal skills were not copied into a second Cursor-specific directory. Nine older development skills also have preserved copies under `~/.agents/skills/`; each duplicated name is still one unique skill and both paths are listed in its entry.

Claude Code plugins are different from normal skills. They are installed and updated by `claude plugin`, may include hooks or other components, and resolve through a versioned plugin cache. The `skill-creator` plugin is available only in Claude Code. Superpowers is installed in both clients at separate resolved cache paths, but its 14 matching names are counted once.

Cursor and Claude built-ins are supplied by the applications and are not separately installed catalog items. MCP tools are live service integrations, not skills. Bundled subagents are agent definitions, not skills. Two Playwright `SKILL.md` files inside the SEO package's `.venv` are Python dependency artifacts and are excluded.

## Update process

Treat an update as a fresh trust decision:

1. Inspect the exact source skill, sibling scripts, declared tools, mutable network access, license, and repository status.
2. For a normal skill, use the Node-compatible pinned CLI `skills@1.5.18`.
3. Install one named skill, never a repository's complete catalog.
4. Verify the installed `SKILL.md`, local path, unexpected additions, duplicate copies, and any plugin metadata.
5. Update the corresponding catalog entry with the current source, license, trust notes, command, and resolved path.

A normal installation follows this shape:

```text
npx -y skills@1.5.18 add <owner/repository> --skill <exact-name> -g -a claude-code -y --copy
```

Plugins must use the owning application's plugin command. Do not manually copy one component out of a plugin because that can omit hooks, manifests, or cleanup state.

## Removal and recovery

Remove a normal skill by deleting only its named directory under `~/.claude/skills/`. For one of the nine preserved development skills, check its catalog entry before removal because a second copy also exists under `~/.agents/skills/`. Do not delete source repositories, project data, reports, credentials, or unrelated state.

Uninstall plugins through Claude Code or Cursor, whichever owns that installation. The owning command can remove hooks and registration state that a direct cache deletion would leave behind.

The removed trading and investing suite remains recoverable from its canonical source: https://github.com/tradermonty/claude-trading-skills. Reinstall only the needed named skills after a new inspection; do not restore the whole suite by default.
