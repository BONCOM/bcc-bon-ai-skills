# AI Skills Catalog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the installed trading/investing skills with a reviewed development-focused skill set and publish a source-linked catalog of all 73 separately installed skills.

**Architecture:** Normal Agent Skills remain single physical copies under `~/.claude/skills/`, where both Claude Code and Cursor can discover them. Claude Code-only plugins use its user-scoped plugin installer. The `AI_Skills` directory contains documentation only; it does not duplicate skill packages or modify any application repository.

**Tech Stack:** Agent Skills `SKILL.md`, `skills` CLI 1.5.18, Claude Code plugin CLI, Markdown, Python 3 verification scripts.

## Global Constraints

- Remove only the 19 named directories under `~/.claude/skills/`; do not remove source repositories, portfolio data, reports, credentials, or thesis state.
- Preserve 31 Claude SEO skills, `humanizer`, 14 Superpowers skills, the nine existing development skills, and all project repositories.
- Install normal skills globally under `~/.claude/skills/` and rely on Cursor's Claude compatibility discovery path; do not create a second physical copy.
- Use `skills` CLI version 1.5.18 because Node 22.16 is below the 22.20 floor required by CLI 1.5.19.
- Install only named skills, never a repository's complete skill catalog.
- Inspect every selected `SKILL.md`, sibling scripts, declared tools, mutable network access, license, and repository status before installation.
- Skip a skill that fails inspection or installation and record the exact reason in `optional-tools.md`; do not manually copy an incomplete package.
- Keep `codeql` manually invoked; do not install or run the CodeQL CLI as part of this work.
- Install plugins through the owning application's plugin command.
- Exclude Cursor/Claude built-ins, MCP tools, bundled subagents, and virtual-environment `SKILL.md` files from the catalog.
- Do not modify files in `/Users/rramesh/Documents/Code_Projects/SEO_Audit_Tool`.
- `/Users/rramesh/Documents/Code_Projects/AI_Skills` is not a Git repository; do not initialize or create commits unless the user separately requests it.

## File Map

- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/README.md` — catalog overview, counts, discovery paths, update procedure, inclusion rules, and recovery summary.
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/development.md` — 27 development, UI, testing, security, GCP, and skill-authoring entries.
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/seo.md` — 31 SEO entries.
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/writing.md` — the `humanizer` entry.
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/superpowers.md` — the plugin and its 14 separately installed skills.
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/agent-selection.md` — routing guide using Cursor's actual agent catalog.
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/optional-tools.md` — deferred and rejected tools, reasons, and trust boundaries.
- Preserve: `/Users/rramesh/Documents/Code_Projects/AI_Skills/docs/2026-07-16-ai-skills-catalog-design.md` — approved design record.

---

### Task 1: Establish the baseline and preflight the installers

**Files:**
- Read: `/Users/rramesh/.claude/skills/**/SKILL.md`
- Read: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/*/skills/*/SKILL.md`
- Modify: none

**Interfaces:**
- Produces: verified baseline counts of 74 unique skills, 19 removable directories, and working CLI prerequisites.

- [ ] **Step 1: Confirm tool versions**

Run:

```bash
node --version
npx -y skills@1.5.18 --version
claude --version
claude plugin list --json
```

Expected:
- Node reports `v22.16.x`.
- The skills CLI reports `1.5.18`.
- Claude Code responds and plugin listing returns valid JSON.

- [ ] **Step 2: Verify every removal target exists at an allowed path**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

root = Path.home() / ".claude" / "skills"
names = """
dividend-growth-pullback-screener
economic-calendar-fetcher
exposure-coach
kanchi-dividend-review-monitor
kanchi-dividend-sop
kanchi-dividend-us-tax-accounting
macro-regime-detector
market-environment-analysis
portfolio-manager
position-sizer
scenario-analyzer
sector-analyst
stanley-druckenmiller-investment
trader-memory-core
trading-skills-navigator
us-market-bubble-detector
us-stock-analysis
value-dividend-screener
weekly-performance-digest
""".split()

for name in names:
    path = root / name
    markers = [path / "SKILL.md", path / name / "SKILL.md"]
    assert path.parent == root
    assert path.is_dir(), f"missing removal target: {path}"
    assert any(marker.is_file() for marker in markers), f"not a skill directory: {path}"

print(f"verified {len(names)} removable skill directories")
PY
```

Expected: `verified 19 removable skill directories`.

- [ ] **Step 3: Rebuild the pre-change inventory**

Use `Glob` to enumerate top-level `SKILL.md` files in `~/.claude/skills`, explicitly excluding `seo/.venv/**`. Use `Glob` separately for the versioned Superpowers plugin directory. Confirm this composition:

```text
31 SEO + 19 trading + 9 development + 1 writing + 14 Superpowers = 74
```

If the composition differs, stop before deletion and reconcile the approved design with the actual installation.

---

### Task 2: Inspect all 17 selected normal skills

**Files:**
- Read: temporary shallow clones under the system temporary directory
- Modify: none

**Interfaces:**
- Consumes: the exact allowlist from the approved design.
- Produces: an inspection decision for every selected skill; only approved names proceed to installation.

- [ ] **Step 1: Confirm each repository exposes the selected names**

Run each command sequentially:

```bash
npx -y skills@1.5.18 add trailofbits/skills --list
npx -y skills@1.5.18 add addyosmani/agent-skills --list
npx -y skills@1.5.18 add wshobson/agents --list
npx -y skills@1.5.18 add currents-dev/playwright-best-practices-skill --list
npx -y skills@1.5.18 add vercel-labs/agent-skills --list
npx -y skills@1.5.18 add antfu/skills --list
npx -y skills@1.5.18 add mcollina/skills --list
npx -y skills@1.5.18 add google/skills --list
```

Expected: all 17 exact names from Task 4 are listed.

- [ ] **Step 2: Shallow-clone reviewed sources into an isolated temporary directory**

Run:

```bash
review_dir="$(mktemp -d "${TMPDIR:-/tmp}/ai-skills-review.XXXXXX")"
for repo in \
  trailofbits/skills \
  addyosmani/agent-skills \
  wshobson/agents \
  currents-dev/playwright-best-practices-skill \
  vercel-labs/agent-skills \
  antfu/skills \
  mcollina/skills \
  google/skills
do
  git clone --depth=1 "https://github.com/$repo.git" "$review_dir/${repo//\//__}"
done
printf '%s\n' "$review_dir"
```

Expected: eight successful clones and one printed temporary path.

- [ ] **Step 3: Inspect each selected package before installation**

For each selected name, use `rg` to locate the matching `SKILL.md`, then use `ReadFile` and `Glob` to inspect that file and sibling scripts/references:

```text
supply-chain-risk-auditor
security-and-hardening
observability-and-instrumentation
ci-cd-and-automation
performance-optimization
python-testing-patterns
playwright-best-practices
codeql
vercel-composition-patterns
vue
node
gcloud
google-cloud-recipe-auth
cloud-logging-query-generation
google-cloud-waf-security
google-cloud-waf-operational-excellence
google-cloud-solution-architecture
```

For every name, record during execution:
- unique matching `SKILL.md`;
- declared allowed tools;
- executable sibling files;
- external downloads, mutable fetches, or API-key requirements;
- repository license and recent maintenance status;
- whether its behavior matches its stated purpose.

Reject on hidden credential access, destructive default behavior, unexplained executable downloads, ambiguous duplicate names, or a missing license for bundled executable code. A rejected name is omitted from installation and documented in `optional-tools.md`, so the final count is reduced transparently rather than replaced silently.

- [ ] **Step 4: Remove temporary review clones**

Run only against the path printed by `mktemp`:

```bash
test -n "$review_dir" &&
case "$review_dir" in
  "${TMPDIR:-/tmp}"/ai-skills-review.*) rm -rf -- "$review_dir" ;;
  *) echo "refusing to remove unexpected path: $review_dir" >&2; exit 1 ;;
esac
```

Expected: the temporary review directory is absent.

---

### Task 3: Remove the 19 trading and investing skills

**Files:**
- Delete: the 19 exact directories listed in the approved design under `/Users/rramesh/.claude/skills/`
- Modify: none

**Interfaces:**
- Consumes: Task 1's verified removal allowlist.
- Produces: no installed trading/investing skill directories.

- [ ] **Step 1: Delete only verified targets**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import shutil

root = Path.home() / ".claude" / "skills"
names = """
dividend-growth-pullback-screener
economic-calendar-fetcher
exposure-coach
kanchi-dividend-review-monitor
kanchi-dividend-sop
kanchi-dividend-us-tax-accounting
macro-regime-detector
market-environment-analysis
portfolio-manager
position-sizer
scenario-analyzer
sector-analyst
stanley-druckenmiller-investment
trader-memory-core
trading-skills-navigator
us-market-bubble-detector
us-stock-analysis
value-dividend-screener
weekly-performance-digest
""".split()

for name in names:
    path = root / name
    markers = [path / "SKILL.md", path / name / "SKILL.md"]
    assert path.parent == root
    assert path.is_dir(), f"missing target: {path}"
    assert any(marker.is_file() for marker in markers), f"refusing non-skill path: {path}"
    shutil.rmtree(path)

print(f"removed {len(names)} skill directories")
PY
```

Expected: `removed 19 skill directories`.

- [ ] **Step 2: Verify removal without touching related data**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

root = Path.home() / ".claude" / "skills"
names = """
dividend-growth-pullback-screener economic-calendar-fetcher exposure-coach
kanchi-dividend-review-monitor kanchi-dividend-sop
kanchi-dividend-us-tax-accounting macro-regime-detector
market-environment-analysis portfolio-manager position-sizer scenario-analyzer
sector-analyst stanley-druckenmiller-investment trader-memory-core
trading-skills-navigator us-market-bubble-detector us-stock-analysis
value-dividend-screener weekly-performance-digest
""".split()
remaining = [str(root / name) for name in names if (root / name).exists()]
assert not remaining, remaining
print("all 19 trading skill paths are absent")
PY
```

Expected: `all 19 trading skill paths are absent`.

---

### Task 4: Install the 17 reviewed normal skills

**Files:**
- Create: `/Users/rramesh/.claude/skills/<selected-name>/`
- Modify: none outside `/Users/rramesh/.claude/skills/`

**Interfaces:**
- Consumes: Task 2's inspection approvals.
- Produces: one readable global `SKILL.md` for every approved selected name.

- [ ] **Step 1: Install each selected skill explicitly and sequentially**

Run:

```bash
npx -y skills@1.5.18 add trailofbits/skills --skill supply-chain-risk-auditor -g -a claude-code -y --copy
npx -y skills@1.5.18 add addyosmani/agent-skills --skill security-and-hardening -g -a claude-code -y --copy
npx -y skills@1.5.18 add addyosmani/agent-skills --skill observability-and-instrumentation -g -a claude-code -y --copy
npx -y skills@1.5.18 add addyosmani/agent-skills --skill ci-cd-and-automation -g -a claude-code -y --copy
npx -y skills@1.5.18 add addyosmani/agent-skills --skill performance-optimization -g -a claude-code -y --copy
npx -y skills@1.5.18 add wshobson/agents --skill python-testing-patterns -g -a claude-code -y --copy
npx -y skills@1.5.18 add currents-dev/playwright-best-practices-skill --skill playwright-best-practices -g -a claude-code -y --copy
npx -y skills@1.5.18 add trailofbits/skills --skill codeql -g -a claude-code -y --copy
npx -y skills@1.5.18 add vercel-labs/agent-skills --skill vercel-composition-patterns -g -a claude-code -y --copy
npx -y skills@1.5.18 add antfu/skills --skill vue -g -a claude-code -y --copy
npx -y skills@1.5.18 add mcollina/skills --skill node -g -a claude-code -y --copy
npx -y skills@1.5.18 add google/skills --skill gcloud -g -a claude-code -y --copy
npx -y skills@1.5.18 add google/skills --skill google-cloud-recipe-auth -g -a claude-code -y --copy
npx -y skills@1.5.18 add google/skills --skill cloud-logging-query-generation -g -a claude-code -y --copy
npx -y skills@1.5.18 add google/skills --skill google-cloud-waf-security -g -a claude-code -y --copy
npx -y skills@1.5.18 add google/skills --skill google-cloud-waf-operational-excellence -g -a claude-code -y --copy
npx -y skills@1.5.18 add google/skills --skill google-cloud-solution-architecture -g -a claude-code -y --copy
```

Expected: every command exits successfully. Do not run these commands concurrently because the shared `npx` cache previously produced `ENOTEMPTY`.

- [ ] **Step 2: Verify exact installed files**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

root = Path.home() / ".claude" / "skills"
names = """
supply-chain-risk-auditor
security-and-hardening
observability-and-instrumentation
ci-cd-and-automation
performance-optimization
python-testing-patterns
playwright-best-practices
codeql
vercel-composition-patterns
vue
node
gcloud
google-cloud-recipe-auth
cloud-logging-query-generation
google-cloud-waf-security
google-cloud-waf-operational-excellence
google-cloud-solution-architecture
""".split()

missing = [name for name in names if not (root / name / "SKILL.md").is_file()]
assert not missing, f"missing installed skills: {missing}"
print(f"verified {len(names)} installed normal skills")
PY
```

Expected: `verified 17 installed normal skills`.

---

### Task 5: Enable the two Claude Code plugins

**Files:**
- Modify: Claude Code's user-scoped plugin state
- Modify: none in project repositories

**Interfaces:**
- Produces: enabled `skill-creator` and `superpowers` plugins in Claude Code.

- [ ] **Step 1: Install from Anthropic's official marketplace**

Run:

```bash
claude plugin marketplace add anthropics/claude-plugins-official --scope user
claude plugin install skill-creator@claude-plugins-official --scope user
claude plugin install superpowers@claude-plugins-official --scope user
```

Expected: the marketplace registration succeeds or reports that the same
user-scoped marketplace is already registered, then both installations succeed
or report that the same user-scoped plugin is already installed.

- [ ] **Step 2: Verify plugin status**

Run:

```bash
claude plugin list --json
```

Expected: JSON entries for `skill-creator` and `superpowers`, each enabled at user scope. Capture the resolved installation paths and source marketplace for the catalog.

---

### Task 6: Build the seven-document catalog

**Files:**
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/README.md`
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/development.md`
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/seo.md`
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/writing.md`
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/superpowers.md`
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/agent-selection.md`
- Create: `/Users/rramesh/Documents/Code_Projects/AI_Skills/optional-tools.md`

**Interfaces:**
- Consumes: actual post-install files and plugin metadata from Tasks 4 and 5.
- Produces: a source-linked catalog containing exactly one entry per unique separately installed skill.

- [ ] **Step 1: Use one consistent entry schema**

Every installed-skill entry must use this structure with real values from the installed package and source repository:

```markdown
## `<exact-skill-name>`

<One paragraph describing when the skill should be invoked and what it contributes.>

- Source: <exact repository or SKILL.md URL>
- Installed at: `<resolved local path>`
- Available in: Cursor and Claude Code | Claude Code
- License: <verified SPDX name or "Not stated in the skill repository">
- Trust notes: <scripts, declared tools, network calls, external services, API keys, or "Instruction-only; no bundled executable scripts">
- Install/update: `<exact source and command family>`
```

Do not infer a license from popularity or ownership. Do not claim Cursor support for a Claude plugin.

- [ ] **Step 2: Write `development.md` with exactly 27 entries**

Document these nine preserved skills:

```text
claude-api
cloud-run-basics
fastapi
firebase-firestore
frontend-design
google-analytics-data-api-basics
playwright-cli
vercel-react-best-practices
web-design-guidelines
```

Document the 17 new normal skills from Task 4 and the Claude Code-only `skill-creator` plugin from Task 5. Group entries under Development Quality, Frontend and UI, Node.js, Google Cloud, and Skill Development without changing the total.

- [ ] **Step 3: Write `seo.md` with exactly 31 entries**

Document:

```text
seo
seo-ahrefs
seo-audit
seo-backlinks
seo-bing
seo-cluster
seo-competitor-pages
seo-content
seo-content-brief
seo-dataforseo
seo-drift
seo-ecommerce
seo-firecrawl
seo-flow
seo-geo
seo-google
seo-hreflang
seo-image-gen
seo-images
seo-local
seo-maps
seo-page
seo-plan
seo-profound
seo-programmatic
seo-schema
seo-seranking
seo-sitemap
seo-sxo
seo-technical
seo-unlighthouse
```

Use the canonical source `https://github.com/AgriciDaniel/claude-seo` and inspect each installed `SKILL.md` for its distinct purpose and external-service requirements. Exclude both Playwright `SKILL.md` files under `seo/.venv/`.

- [ ] **Step 4: Write `writing.md` and `superpowers.md`**

`writing.md` contains only `humanizer`, sourced from `https://github.com/blader/humanizer`.

`superpowers.md` describes the plugin once and contains entries for:

```text
brainstorming
dispatching-parallel-agents
executing-plans
finishing-a-development-branch
receiving-code-review
requesting-code-review
subagent-driven-development
systematic-debugging
test-driven-development
using-git-worktrees
using-superpowers
verification-before-completion
writing-plans
writing-skills
```

Use `https://github.com/obra/superpowers` as the canonical source. Record both Cursor's resolved versioned plugin path and Claude Code's resolved plugin path without counting the skills twice.

- [ ] **Step 5: Write `agent-selection.md`**

Include this routing policy:

```text
Narrow repository lookup -> direct Glob, rg, and ReadFile tools
Broad codebase exploration -> explore
Command-heavy work -> shell
Browser flows and UI verification -> browser-use
One failed PR check -> ci-investigator
Explicit local change review -> bugbot
Explicit security review -> security-review
SEO task -> the narrowest matching seo-* specialist
Independent workstreams -> dispatching-parallel-agents
Approved implementation plan -> subagent-driven-development or executing-plans
```

Add two rules: prefer direct tools over an agent for narrow work, and never invent an unavailable agent or model name.

- [ ] **Step 6: Write `optional-tools.md`**

Document why these were reviewed but not installed:

```text
grill-me
claude-mem
Context Mode
cloud-monitoring-metric-selection
vite
vitest
shadcn
tailwind-design-system
wcag-audit-patterns
community Docker skills
community agent routers
retired next-best-practices
```

Include the trigger that would justify reconsidering each item and the relevant trust boundary from the approved design.

- [ ] **Step 7: Write `README.md`**

Include:
- purpose and scope;
- final count formula `27 development + 31 SEO + 1 writing + 14 Superpowers = 73`;
- normal discovery path `~/.claude/skills/`;
- explanation that Cursor reads the Claude compatibility path without a second copy;
- distinction between normal skills, Claude Code plugins, built-ins, MCP tools, and bundled subagents;
- links to all seven catalog documents and the approved design;
- update process: inspect source, pin `skills@1.5.18`, install one named skill, verify, then update the catalog;
- removal/recovery instructions, including `https://github.com/tradermonty/claude-trading-skills` as the canonical reinstall source for the deleted suite.

---

### Task 7: Verify inventory, attribution, discovery, and repository isolation

**Files:**
- Read: all catalog Markdown files
- Read: installed skill and plugin paths
- Modify: catalog files only when correcting a failed check

**Interfaces:**
- Produces: evidence that the approved design is fully implemented.

- [ ] **Step 1: Run the catalog integrity check**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

catalog = Path("/Users/rramesh/Documents/Code_Projects/AI_Skills")
docs = [
    catalog / "development.md",
    catalog / "seo.md",
    catalog / "writing.md",
    catalog / "superpowers.md",
]

for path in docs:
    assert path.is_file(), f"missing catalog file: {path}"
    text = path.read_text()
    entries = re.findall(r"^## `([^`]+)`$", text, flags=re.MULTILINE)
    assert len(entries) == len(set(entries)), f"duplicate entries in {path.name}"
    for name in entries:
        section = text.split(f"## `{name}`", 1)[1].split("\n## `", 1)[0]
        for field in ("Source:", "Installed at:", "Available in:", "License:", "Trust notes:", "Install/update:"):
            assert field in section, f"{path.name}: {name} missing {field}"

counts = {
    "development.md": 27,
    "seo.md": 31,
    "writing.md": 1,
    "superpowers.md": 14,
}
actual = {}
for path in docs:
    actual[path.name] = len(re.findall(r"^## `([^`]+)`$", path.read_text(), flags=re.MULTILINE))
assert actual == counts, (actual, counts)
assert sum(actual.values()) == 73

for name in ("README.md", "agent-selection.md", "optional-tools.md"):
    assert (catalog / name).is_file(), f"missing {name}"

print("catalog contains 73 unique complete entries")
PY
```

Expected: `catalog contains 73 unique complete entries`.

- [ ] **Step 2: Validate installed normal-skill inventory**

Use `Glob` to enumerate `~/.claude/skills/**/SKILL.md`, exclude `**/.venv/**`, and confirm:
- no trading target remains;
- the nine preserved development skills remain;
- all 17 selected normal skills exist;
- all 31 SEO skills and `humanizer` remain.

Use `claude plugin list --json` to confirm `skill-creator` and `superpowers` are enabled. Confirm the Superpowers source includes all 14 cataloged skills.

- [ ] **Step 3: Validate source links**

Extract every `Source:` URL from the seven catalog files and request each unique URL once with `WebFetch`. Every source must resolve successfully. If a repository does not expose a stable per-skill URL, use its canonical repository URL consistently.

- [ ] **Step 4: Verify Cursor discovery**

Reload Cursor after installation, then ask it to enumerate globally discoverable skills or start a fresh agent session and confirm at least one unique new trigger from each category is discoverable:

```text
supply-chain-risk-auditor
vercel-composition-patterns
node
gcloud
```

Do not create physical copies under another global skill directory to force discovery.

- [ ] **Step 5: Confirm the application repository stayed untouched**

Run:

```bash
git -C "/Users/rramesh/Documents/Code_Projects/SEO_Audit_Tool" status --short
```

Expected: output exactly matches the known pre-existing status captured before execution; no `AI_Skills` work or installer artifacts appear in this repository.

- [ ] **Step 6: Run the final unfinished-marker and count scan**

Search all `AI_Skills/*.md` files for unfinished markers and stale totals:

```bash
rg -n $'\x54\x42\x44|\x54\x4f\x44\x4f|71\x20skills|72\x20skills' "/Users/rramesh/Documents/Code_Projects/AI_Skills" --glob '*.md'
```

Expected: no matches. Correct any failed check and rerun Tasks 7.1 through 7.6 before reporting completion.
