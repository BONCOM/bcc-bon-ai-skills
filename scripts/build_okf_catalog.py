#!/usr/bin/env python3
"""Convert AI_Skills monolithic catalog markdown into an OKF v0.1 bundle."""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "archive" / "legacy-monolith"
TODAY = date.today().isoformat()


def catalog_source(name: str) -> Path:
    """Prefer archived monoliths after migration; fall back to repo root."""
    archived = LEGACY / name
    if archived.exists():
        return archived
    return ROOT / name


@dataclass
class Concept:
    slug: str
    title: str
    summary: str
    body_lines: list[str]
    category: str
    group: str = ""
    kind: str = "Agent Skill"  # or Deferred Tool, Playbook, Overview
    tags: list[str] = field(default_factory=list)
    source: str = ""
    install_paths: list[str] = field(default_factory=list)
    available_in: str = ""
    license: str = ""
    trust_notes: str = ""
    install_update: str = ""
    why_deferred: str = ""
    reconsider_when: str = ""
    trust_boundary: str = ""


SKILL_HEADING = re.compile(r"^## `([^`]+)`\s*$")
PLAIN_HEADING = re.compile(r"^## (.+)\s*$")
GROUP_HEADING = re.compile(r"^### (.+)\s*$")
BULLET = re.compile(r"^- ([^:]+):\s*(.*)$")


def parse_skill_catalog(path: Path, category: str, default_tags: list[str]) -> list[Concept]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    concepts: list[Concept] = []
    group = ""
    i = 0
    while i < len(lines):
        g = GROUP_HEADING.match(lines[i])
        if g and not lines[i].startswith("####"):
            group = g.group(1).strip()
            i += 1
            continue
        m = SKILL_HEADING.match(lines[i])
        if not m:
            i += 1
            continue
        slug = m.group(1).strip()
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        summary_lines: list[str] = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("- ") and not lines[i].startswith("#"):
            summary_lines.append(lines[i].strip())
            i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        fields: dict[str, str] = {}
        while i < len(lines):
            if lines[i].startswith("#"):
                break
            b = BULLET.match(lines[i])
            if b:
                key = b.group(1).strip().lower()
                fields[key] = b.group(2).strip()
                i += 1
                continue
            if not lines[i].strip():
                i += 1
                if fields:
                    break
                continue
            i += 1
        summary = " ".join(summary_lines).strip()
        tags = list(default_tags)
        if group:
            tags.append(re.sub(r"[^a-z0-9]+", "-", group.lower()).strip("-"))
        raw_paths = fields.get("installed at", "")
        install_paths = []
        for p in raw_paths.split(";"):
            cleaned = p.strip().strip("`").strip()
            if cleaned:
                install_paths.append(cleaned)
        concepts.append(
            Concept(
                slug=slug,
                title=slug,
                summary=summary,
                body_lines=[],
                category=category,
                group=group,
                tags=tags,
                source=fields.get("source", ""),
                install_paths=install_paths,
                available_in=fields.get("available in", ""),
                license=fields.get("license", ""),
                trust_notes=fields.get("trust notes", ""),
                install_update=fields.get("install/update", ""),
            )
        )
    return concepts


def parse_deferred(path: Path) -> list[Concept]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    concepts: list[Concept] = []
    i = 0
    # skip title
    while i < len(lines) and not lines[i].startswith("## "):
        i += 1
    while i < len(lines):
        m = SKILL_HEADING.match(lines[i]) or PLAIN_HEADING.match(lines[i])
        if not m or lines[i].startswith("###"):
            i += 1
            continue
        raw = m.group(1).strip()
        slug = raw.strip("`")
        file_slug = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")
        i += 1
        fields: dict[str, str] = {}
        while i < len(lines) and not lines[i].startswith("## "):
            b = BULLET.match(lines[i])
            if b:
                fields[b.group(1).strip().lower()] = b.group(2).strip()
            i += 1
        concepts.append(
            Concept(
                slug=file_slug,
                title=slug,
                summary=fields.get("why deferred", "Reviewed and deferred."),
                body_lines=[],
                category="deferred",
                kind="Deferred Tool",
                tags=["deferred"],
                source=fields.get("source", ""),
                why_deferred=fields.get("why deferred", ""),
                reconsider_when=fields.get("reconsider when", ""),
                trust_boundary=fields.get("trust boundary", ""),
            )
        )
    return concepts


def yaml_escape(value: str) -> str:
    if value == "":
        return '""'
    if any(c in value for c in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", ">", "'", '"', "%", "@", "`", "\n"]):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return value


def write_skill_concept(path: Path, c: Concept) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tags = ", ".join(yaml_escape(t) for t in c.tags)
    fm = [
        "---",
        f"type: {c.kind}",
        f"title: {yaml_escape(c.title)}",
        f"description: {yaml_escape(c.summary[:300] if c.summary else c.title)}",
    ]
    if c.source:
        fm.append(f"resource: {yaml_escape(c.source)}")
    fm.append(f"tags: [{tags}]")
    fm.append(f"timestamp: {TODAY}T00:00:00Z")
    fm.append(f"category: {yaml_escape(c.category)}")
    if c.group:
        fm.append(f"group: {yaml_escape(c.group)}")
    if c.license:
        fm.append(f"license: {yaml_escape(c.license)}")
    if c.available_in:
        fm.append(f"available_in: {yaml_escape(c.available_in)}")
    fm.append("---")
    body = [
        "",
        c.summary,
        "",
        "# When to use",
        "",
        c.summary,
        "",
    ]
    if c.install_paths:
        body += ["# Installed at", ""]
        for p in c.install_paths:
            body.append(f"- `{p}`")
        body.append("")
    if c.available_in:
        body += ["# Availability", "", c.available_in, ""]
    if c.license:
        body += ["# License", "", c.license, ""]
    if c.trust_notes:
        body += ["# Trust notes", "", c.trust_notes, ""]
    if c.install_update:
        body += ["# Install / update", "", "```text", c.install_update, "```", ""]
    if c.source:
        body += [
            "# Citations",
            "",
            f"[1] [{c.title} source]({c.source})",
            "",
        ]
    related = []
    if c.category == "development":
        related.append("- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)")
        related.append("- Category index: [/skills/development/index.md](/skills/development/index.md)")
    elif c.category == "seo":
        related.append("- Routing: [/playbooks/agent-selection.md](/playbooks/agent-selection.md)")
        related.append("- Category index: [/skills/seo/index.md](/skills/seo/index.md)")
    if related:
        body += ["# Related", ""] + related + [""]
    path.write_text("\n".join(fm + body), encoding="utf-8")


def write_deferred_concept(path: Path, c: Concept) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = [
        "---",
        "type: Deferred Tool",
        f"title: {yaml_escape(c.title)}",
        f"description: {yaml_escape(c.summary[:300])}",
    ]
    if c.source:
        fm.append(f"resource: {yaml_escape(c.source)}")
    fm += [
        "tags: [deferred]",
        f"timestamp: {TODAY}T00:00:00Z",
        "status: deferred",
        "---",
        "",
        "# Why deferred",
        "",
        c.why_deferred or c.summary,
        "",
        "# Reconsider when",
        "",
        c.reconsider_when or "Not specified.",
        "",
        "# Trust boundary",
        "",
        c.trust_boundary or "Not specified.",
        "",
    ]
    if c.source:
        fm += [
            "# Citations",
            "",
            f"[1] [Source]({c.source})",
            "",
        ]
    path.write_text("\n".join(fm), encoding="utf-8")


def write_index(path: Path, title: str, sections: dict[str, list[tuple[str, str, str]]], okf_version: str | None = None) -> None:
    """sections: heading -> list of (rel_link, title, description)"""
    path.parent.mkdir(parents=True, exist_ok=True)
    parts: list[str] = []
    if okf_version:
        parts += ["---", f'okf_version: "{okf_version}"', "---", ""]
    parts.append(f"# {title}")
    parts.append("")
    for heading, items in sections.items():
        parts.append(f"# {heading}")
        parts.append("")
        for link, title_, desc in items:
            parts.append(f"* [{title_}]({link}) - {desc}")
        parts.append("")
    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    skills_dev = parse_skill_catalog(catalog_source("development.md"), "development", ["development", "installed"])
    skills_seo = parse_skill_catalog(catalog_source("seo.md"), "seo", ["seo", "installed"])
    skills_writing = parse_skill_catalog(catalog_source("writing.md"), "writing", ["writing", "installed"])
    skills_super = parse_skill_catalog(
        catalog_source("superpowers.md"), "superpowers", ["superpowers", "installed", "plugin"]
    )
    deferred = parse_deferred(catalog_source("optional-tools.md"))

    # wipe generated trees (keep scripts/, .git, docs design sources briefly)
    for d in ["skills", "deferred", "playbooks", "meta"]:
        p = ROOT / d
        if p.exists():
            shutil.rmtree(p)

    # write skill concepts
    for c in skills_dev:
        write_skill_concept(ROOT / "skills" / "development" / f"{c.slug}.md", c)
    for c in skills_seo:
        write_skill_concept(ROOT / "skills" / "seo" / f"{c.slug}.md", c)
    for c in skills_writing:
        write_skill_concept(ROOT / "skills" / "writing" / f"{c.slug}.md", c)
    for c in skills_super:
        write_skill_concept(ROOT / "skills" / "superpowers" / f"{c.slug}.md", c)
    for c in deferred:
        write_deferred_concept(ROOT / "deferred" / f"{c.slug}.md", c)

    # development subgroup indexes
    by_group: dict[str, list[Concept]] = {}
    for c in skills_dev:
        by_group.setdefault(c.group or "General", []).append(c)
    write_index(
        ROOT / "skills" / "development" / "index.md",
        "Development skills",
        {
            g: [(f"./{x.slug}.md", x.title, x.summary[:160] or x.title) for x in items]
            for g, items in by_group.items()
        },
    )
    write_index(
        ROOT / "skills" / "seo" / "index.md",
        "SEO skills",
        {
            "Installed SEO skills": [
                (f"./{c.slug}.md", c.title, c.summary[:160] or c.title) for c in skills_seo
            ]
        },
    )
    write_index(
        ROOT / "skills" / "writing" / "index.md",
        "Writing skills",
        {
            "Installed writing skills": [
                (f"./{c.slug}.md", c.title, c.summary[:160] or c.title) for c in skills_writing
            ]
        },
    )
    write_index(
        ROOT / "skills" / "superpowers" / "index.md",
        "Superpowers skills",
        {
            "Installed Superpowers skills": [
                (f"./{c.slug}.md", c.title, c.summary[:160] or c.title) for c in skills_super
            ]
        },
    )
    write_index(
        ROOT / "skills" / "index.md",
        "Installed skills",
        {
            "Categories": [
                ("./development/", "Development", f"{len(skills_dev)} skills — quality, auth, frontend, Node, GCP, MCP"),
                ("./seo/", "SEO", f"{len(skills_seo)} skills — Claude SEO catalog"),
                ("./writing/", "Writing", f"{len(skills_writing)} skills"),
                ("./superpowers/", "Superpowers", f"{len(skills_super)} skills — counted once across clients"),
            ]
        },
    )
    write_index(
        ROOT / "deferred" / "index.md",
        "Deferred tools",
        {
            "Reviewed but not installed": [
                (f"./{c.slug}.md", c.title, c.summary[:160] or c.title) for c in deferred
            ]
        },
    )

    # playbooks
    routing_path = catalog_source("agent-selection.md")
    if not routing_path.exists():
        routing_path = ROOT / "playbooks" / "agent-selection.md"
    routing = routing_path.read_text(encoding="utf-8")
    routing_body = re.sub(r"^---[\s\S]*?---\s*", "", routing, count=1)
    routing_body = re.sub(r"^# .+\n+", "", routing_body, count=1)
    (ROOT / "playbooks").mkdir(parents=True, exist_ok=True)
    (ROOT / "playbooks" / "agent-selection.md").write_text(
        "\n".join(
            [
                "---",
                "type: Playbook",
                "title: Agent selection",
                "description: Route work to the narrowest skill, agent, or direct tool.",
                "tags: [routing, playbook]",
                f"timestamp: {TODAY}T00:00:00Z",
                "---",
                "",
                routing_body.strip(),
                "",
                "# Related",
                "",
                "- Skills index: [/skills/index.md](/skills/index.md)",
                "- Deferred tools: [/deferred/index.md](/deferred/index.md)",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (ROOT / "playbooks" / "install-and-update.md").write_text(
        f"""---
type: Playbook
title: Install and update skills
description: Trust-reviewed install process for normal skills and plugins.
tags: [install, playbook, trust]
timestamp: {TODAY}T00:00:00Z
---

Treat an update as a fresh trust decision.

1. Inspect the exact source skill, sibling scripts, declared tools, mutable network access, license, and repository status.
2. For a normal skill, use the Node-compatible pinned CLI `skills@1.5.18`.
3. Install one named skill, never a repository's complete catalog (except small official packs deliberately adopted as a set).
4. Verify the installed `SKILL.md`, local path, unexpected additions, duplicate copies, and any plugin metadata.
5. Add or update the matching OKF concept under [`/skills/`](/skills/index.md) and append [`/log.md`](/log.md).

# Normal skill install shape

```text
npx -y skills@1.5.18 add <owner/repository> --skill <exact-name> -g -a claude-code -y --copy
```

# Plugins

Plugins must use the owning application's plugin command. Do not manually copy one component out of a plugin because that can omit hooks, manifests, or cleanup state.

# Removal

Remove a normal skill by deleting only its named directory under `~/.claude/skills/`. Uninstall plugins through Claude Code or Cursor. Do not delete source repositories, project data, reports, or credentials.

# Citations

[1] [OKF specification v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
""",
        encoding="utf-8",
    )
    write_index(
        ROOT / "playbooks" / "index.md",
        "Playbooks",
        {
            "Operations": [
                ("./agent-selection.md", "Agent selection", "Route to the narrowest skill or agent"),
                ("./install-and-update.md", "Install and update", "Trust-reviewed install, verify, catalog"),
            ]
        },
    )

    # meta / overview concept
    (ROOT / "meta").mkdir(parents=True, exist_ok=True)
    total = len(skills_dev) + len(skills_seo) + len(skills_writing) + len(skills_super)
    (ROOT / "meta" / "catalog-overview.md").write_text(
        f"""---
type: Overview
title: Boncom AI Skills catalog
description: OKF inventory of Cursor/Claude agent skills — sources, trust notes, install paths, routing, and deferred tools.
tags: [overview, catalog]
timestamp: {TODAY}T00:00:00Z
okf_bundle: boncom-ai-skills
counts:
  development: {len(skills_dev)}
  seo: {len(skills_seo)}
  writing: {len(skills_writing)}
  superpowers: {len(skills_super)}
  total_unique: {total}
  deferred: {len(deferred)}
---

This repository is an **Open Knowledge Format (OKF) v0.1** knowledge bundle for Boncom agent skills installed outside app-bundled capabilities.

# Counts

| Category | Unique skills |
|----------|---------------|
| Development | {len(skills_dev)} |
| SEO | {len(skills_seo)} |
| Writing | {len(skills_writing)} |
| Superpowers | {len(skills_super)} |
| **Total unique** | **{total}** |
| Deferred (not installed) | {len(deferred)} |

# How to navigate

1. Start at the root [`/index.md`](/index.md) for progressive disclosure.
2. Open a category under [`/skills/`](/skills/index.md).
3. Read one concept file per skill (frontmatter for routing; body for trust and install).
4. Use [`/playbooks/agent-selection.md`](/playbooks/agent-selection.md) to choose skill vs agent vs direct tools.
5. Check [`/deferred/`](/deferred/index.md) before proposing new installs.

# Discovery paths

- Normal skills: `~/.claude/skills/` (Cursor reads this Claude compatibility path).
- Superpowers: separate Cursor and Claude Code plugin cache paths; 14 names counted once.
- Skill Creator: Claude Code plugin only.

# Out of scope

Cursor/Claude built-ins, live MCP servers, and bundled subagents are not catalog concepts unless separately installed as skills.

# Citations

[1] [Open Knowledge Format SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[2] [BONCOM/boncom-ai-skills](https://github.com/BONCOM/boncom-ai-skills)
""",
        encoding="utf-8",
    )

    # convert design doc
    design_src = ROOT / "docs" / "2026-07-16-ai-skills-catalog-design.md"
    if design_src.exists():
        design_body = design_src.read_text(encoding="utf-8")
        design_body = re.sub(r"^# .+\n+", "", design_body, count=1)
        (ROOT / "meta" / "catalog-design.md").write_text(
            f"""---
type: Reference
title: AI Skills catalog design
description: Original design goals, scope, installation policy, and trust boundaries for the Boncom skills catalog.
tags: [design, reference]
timestamp: 2026-07-16T00:00:00Z
resource: https://github.com/BONCOM/boncom-ai-skills
---

{design_body.strip()}
""",
            encoding="utf-8",
        )

    write_index(
        ROOT / "meta" / "index.md",
        "Meta",
        {
            "Catalog": [
                ("./catalog-overview.md", "Catalog overview", "Counts, scope, discovery"),
                ("./catalog-design.md", "Catalog design", "Original design and policy"),
            ]
        },
    )

    # root index + log
    write_index(
        ROOT / "index.md",
        "Boncom AI Skills (OKF bundle)",
        {
            "Start here": [
                ("./meta/catalog-overview.md", "Catalog overview", "Counts, scope, and how to navigate"),
                ("./playbooks/agent-selection.md", "Agent selection", "Route skills vs agents vs direct tools"),
                ("./playbooks/install-and-update.md", "Install and update", "Trust-reviewed install process"),
            ],
            "Knowledge": [
                ("./skills/", "Installed skills", f"{total} unique skills across development, SEO, writing, Superpowers"),
                ("./deferred/", "Deferred tools", f"{len(deferred)} reviewed, not installed"),
                ("./meta/", "Meta", "Overview and design references"),
                ("./playbooks/", "Playbooks", "Routing and maintenance"),
            ],
            "History": [
                ("./log.md", "Update log", "Chronological catalog changes"),
            ],
        },
        okf_version="0.1",
    )

    (ROOT / "log.md").write_text(
        f"""# Catalog Update Log

## {TODAY}
* **Update**: Migrated catalog to Open Knowledge Format (OKF) v0.1 — one concept per skill, directory indexes, and this log.
* **Creation**: Added Better Auth pack (6 skills), `bigquery-basics`, `gemini-api`, `mcp-builder`, Supabase, and Hookdeck webhook skills to the inventory.
* **Update**: Documented deferred tools including Karpathy, Sentry for AI, n8n, ui-ux-pro-max, Remotion, and writing/marketing marketplace packs.

## 2026-07-16
* **Initialization**: Created Boncom AI Skills catalog and private GitHub repository `BONCOM/boncom-ai-skills`.
* **Creation**: Established development, SEO, writing, and Superpowers inventories with trust notes and install commands.
""",
        encoding="utf-8",
    )

    # GitHub README as Overview concept (required frontmatter for OKF conformance)
    (ROOT / "README.md").write_text(
        f"""---
type: Overview
title: Boncom AI Skills
description: OKF v0.1 inventory of Cursor/Claude agent skills for Boncom — sources, trust, install, routing, deferred tools.
tags: [overview, github]
timestamp: {TODAY}T00:00:00Z
---

# Boncom AI Skills

This repository is an **[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)** knowledge bundle.

**{total} unique installed skills** ({len(skills_dev)} development + {len(skills_seo)} SEO + {len(skills_writing)} writing + {len(skills_super)} Superpowers), plus {len(deferred)} deferred tools.

## Start here

1. [`index.md`](index.md) — progressive disclosure entry point
2. [`meta/catalog-overview.md`](meta/catalog-overview.md) — counts and scope
3. [`playbooks/agent-selection.md`](playbooks/agent-selection.md) — routing
4. [`skills/`](skills/) — one concept file per installed skill
5. [`deferred/`](deferred/) — reviewed but not installed
6. [`log.md`](log.md) — change history

## What a concept contains

Each skill concept has YAML frontmatter (`type`, `title`, `description`, `resource`, `tags`, …) and a structured body: when to use, install paths, license, trust notes, install command, and citations.

## Maintenance

See [`playbooks/install-and-update.md`](playbooks/install-and-update.md). Regenerate from legacy monoliths (if present) with:

```bash
python3 scripts/build_okf_catalog.py
```

# Citations

[1] [OKF SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[2] [GitHub: BONCOM/boncom-ai-skills](https://github.com/BONCOM/boncom-ai-skills)
""",
        encoding="utf-8",
    )

    print(
        f"OKF bundle written: dev={len(skills_dev)} seo={len(skills_seo)} "
        f"writing={len(skills_writing)} superpowers={len(skills_super)} "
        f"deferred={len(deferred)} total={total}"
    )


if __name__ == "__main__":
    main()
