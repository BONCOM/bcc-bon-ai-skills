# SEO skills

These 31 skills come from the installed Claude SEO catalog. Each is counted once, even when it delegates to another SEO skill or shares scripts from the `seo` package. The two Playwright `SKILL.md` files inside `~/.claude/skills/seo/.venv/` are dependency artifacts and are not catalog entries.

## `seo`

Start here when an SEO request spans several disciplines or the right specialist is unclear. The skill detects the business type, routes work to installed specialists, and combines technical, content, schema, image, local, AI-search, and performance findings.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo/SKILL.md
- Installed at: `~/.claude/skills/seo/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Orchestrates shared Python scripts, local crawling, optional external APIs and MCP servers, and specialist subagents. The installed package contains a Python virtual environment; its two Playwright skill stubs are excluded from discovery and counting.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo -g -a claude-code -y --copy`

## `seo-ahrefs`

Ahrefs domain metrics, referring domains, backlinks, anchors, organic keywords, and Content Explorer results are the scope of this extension. It pairs paid Ahrefs evidence with `seo-backlinks` so cross-source discrepancies remain visible.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/ahrefs/skills/seo-ahrefs/SKILL.md
- Installed at: `~/.claude/skills/seo-ahrefs/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires Node 18+, an Ahrefs API token, and the official `@ahrefs/mcp` server installed by the repository extension script. Calls paid, live Ahrefs services and does not work from the skill file alone.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-ahrefs -g -a claude-code -y --copy`

## `seo-audit`

A full-site health check belongs here rather than in the single-page skill. The audit crawls up to 500 pages, detects the business type, selects always-on and conditional specialists, calculates a health score, and returns a prioritized action plan.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-audit/SKILL.md
- Installed at: `~/.claude/skills/seo-audit/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches and crawls the target site with shared Python scripts and may dispatch up to 15 specialists. Conditional checks can use Google, Moz, Bing, DataForSEO, Common Crawl, stored drift baselines, and local report files when configured.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-audit -g -a claude-code -y --copy`

## `seo-backlinks`

Referring-domain analysis, anchor distribution, toxic-link review, link gaps, new or lost links, and disavow evidence are handled here. The skill merges Common Crawl and a verification crawler with optional Moz, Bing Webmaster, Ahrefs, or DataForSEO data instead of pretending one source is complete.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-backlinks/SKILL.md
- Installed at: `~/.claude/skills/seo-backlinks/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Shared scripts can read Moz and Bing credentials, query Common Crawl, crawl backlink URLs, and call DataForSEO when its MCP is connected. Network access is intrinsic; disavow output remains a recommendation, not an automatic submission.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-backlinks -g -a claude-code -y --copy`

## `seo-bing`

Bing Webmaster link data, Microsoft Copilot citation eligibility, and IndexNow submission to participating search engines are this extension's focus. It deliberately does not describe IndexNow as a Google indexing mechanism.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/bing-webmaster/skills/seo-bing/SKILL.md
- Installed at: `~/.claude/skills/seo-bing/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires `BING_WEBMASTER_API_KEY`; URL submission also needs a published `INDEXNOW_KEY`. Shared scripts call Bing Webmaster and can submit single or batched URLs to IndexNow, which is a mutable external action.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-bing -g -a claude-code -y --copy`

## `seo-cluster`

Keyword groups based on overlapping Google top-ten results are the input to this skill's hub-and-spoke planning. It produces cluster plans, internal-link matrices, and interactive maps; content creation is optional and separate.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-cluster/SKILL.md
- Installed at: `~/.claude/skills/seo-cluster/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Uses shared scripts and live SERP data to compare result overlap, then writes planning and visualization artifacts. Optional execution delegates to `claude-blog` only if that separate tool is installed.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-cluster -g -a claude-code -y --copy`

## `seo-competitor-pages`

Comparison, alternatives, and category-roundup pages get a dedicated workflow here. It structures feature comparisons, verdict criteria, conversion paths, and supporting schema while requiring claims to be grounded in current competitor evidence.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-competitor-pages/SKILL.md
- Installed at: `~/.claude/skills/seo-competitor-pages/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches competitor pages and may use live search evidence; generated pricing and feature claims can become stale and require source review. It writes content recommendations but does not publish pages.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-competitor-pages -g -a claude-code -y --copy`

## `seo-content`

Content quality, readability, thin-content, and E-E-A-T reviews should use this skill. It applies Google's Who/How/Why test, checks experience and authorship evidence, and scores whether passages are clear enough to cite in search and AI answers.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-content/SKILL.md
- Installed at: `~/.claude/skills/seo-content/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches the target page and uses local reference criteria and scoring scripts. It may consult mutable Google Search documentation; no API key is required for the base review.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-content -g -a claude-code -y --copy`

## `seo-content-brief`

Writers can use this output as an evidence-based brief for a new page or as a targeted improvement plan for an existing one. It compares current results, scores content gaps, allocates section lengths, sets keyword placement guidance, and chooses a page-type template.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-content-brief/SKILL.md
- Installed at: `~/.claude/skills/seo-content-brief/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches an existing page and competitor or SERP context, then writes a brief. Live result data and suggested keyword densities are planning inputs, not guarantees of ranking.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-content-brief -g -a claude-code -y --copy`

## `seo-dataforseo`

Live SERPs, keyword volume and intent, backlinks, business listings, competitor data, image results, and measured AI mentions come from this extension. It routes among the DataForSEO MCP modules and labels the returned evidence as live vendor data.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-dataforseo/SKILL.md
- Installed at: `~/.claude/skills/seo-dataforseo/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires the DataForSEO extension, MCP server, and paid credentials. Its 79+ tools make live billable API calls across SERP, backlink, content, merchant, and AI-visibility endpoints.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-dataforseo -g -a claude-code -y --copy`

## `seo-drift`

A known-good page baseline lets this skill detect SEO regressions after content or deployment changes. It compares titles, canonicals, robots directives, headings, schema, links, and other critical elements, then keeps a local comparison history.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-drift/SKILL.md
- Installed at: `~/.claude/skills/seo-drift/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches target pages and writes baseline and history state through shared scripts. Stored snapshots may contain page metadata and content-derived values; treat the baseline directory as project data.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-drift -g -a claude-code -y --copy`

## `seo-ecommerce`

Product-page SEO, Product schema, marketplace visibility, pricing comparisons, and Shopping or Amazon keyword gaps are handled here. The base mode audits the page directly; richer market analysis is added only when the DataForSEO Merchant API is available.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-ecommerce/SKILL.md
- Installed at: `~/.claude/skills/seo-ecommerce/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Base checks fetch product pages and validate markup. Shopping, Amazon, pricing, and gap commands use paid DataForSEO Merchant endpoints and therefore create live network calls and possible API charges.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-ecommerce -g -a claude-code -y --copy`

## `seo-firecrawl`

Choose Firecrawl when an audit needs JavaScript-rendered scraping, URL discovery, a site map, broken-link coverage, or a larger crawl than the base fetcher can provide. This extension exposes crawl, map, scrape, and in-site search operations.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/firecrawl/skills/seo-firecrawl/SKILL.md
- Installed at: `~/.claude/skills/seo-firecrawl/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires the Firecrawl extension, MCP server, and service credentials. Calls an external crawling service that sends target URLs and retrieved page content outside the local machine.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-firecrawl -g -a claude-code -y --copy`

## `seo-flow`

The FLOW method and its stage-specific evidence prompts live in this skill. It selects from the Find, Leverage, Optimize, Win, and Local prompt sets so the analysis starts from a defined decision question instead of a broad SEO request.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-flow/SKILL.md
- Installed at: `~/.claude/skills/seo-flow/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction and prompt-library content; no required executable or API. The embedded FLOW prompt material is separately attributed CC-BY-4.0 in the skill.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-flow -g -a claude-code -y --copy`

## `seo-geo`

AI Overviews, ChatGPT search, Perplexity, and similar answer surfaces are the focus of this visibility review. It checks crawler access, brand mentions, `llms.txt`, passage citability, and platform signals while treating Google's GEO guidance as ordinary SEO fundamentals where the primary source says so.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-geo/SKILL.md
- Installed at: `~/.claude/skills/seo-geo/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches the audited site, robots files, and public documentation; optional brand-visibility evidence may come from other configured vendor skills. No base API key is required.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-geo -g -a claude-code -y --copy`

## `seo-google`

Search Console, PageSpeed Insights, CrUX history, sitemap status, GA4 organic traffic, and the Indexing API are routed through this skill. It adds Google's own measurements and index state to crawler-based observations.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-google/SKILL.md
- Installed at: `~/.claude/skills/seo-google/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Shared scripts read configuration from `~/.config/claude-seo/google-api.json` and call Google APIs with API keys, OAuth, or service-account credentials. URL inspection and Indexing API operations have quotas; submission is a mutable external action.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-google -g -a claude-code -y --copy`

## `seo-hreflang`

International targeting across HTML, HTTP headers, or XML sitemaps gets a focused audit and generator here. The checks cover language and region codes, self references, reciprocal return links, canonical alignment, and the single `x-default` fallback.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-hreflang/SKILL.md
- Installed at: `~/.claude/skills/seo-hreflang/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches all language variants needed to validate bidirectional relationships and may generate markup or sitemap snippets. It does not publish those changes.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-hreflang -g -a claude-code -y --copy`

## `seo-image-gen`

An Open Graph preview, hero, product image, infographic, schema image, or thumbnail is a generation task for this extension. It maps the asset type to aspect ratio and resolution, then delegates generation through the Banana creative pipeline.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-image-gen/SKILL.md
- Installed at: `~/.claude/skills/seo-image-gen/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires the Banana extension, nanobanana MCP server, and Gemini image-generation access. Prompts and reference material are sent to an external model, and generated image files are written locally; the audit agent does not auto-generate.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-image-gen -g -a claude-code -y --copy`

## `seo-images`

Existing image assets can be checked for alt text, dimensions, formats, responsive sources, lazy loading, CLS risk, file size, metadata, and search visibility. The same skill can plan or run WebP/AVIF conversion and IPTC/XMP updates when local files are supplied.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-images/SKILL.md
- Installed at: `~/.claude/skills/seo-images/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches pages and image URLs; file-optimization scripts can rewrite local image files and metadata, so preserve originals. Image SERP ranking checks use DataForSEO only when that paid extension is connected.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-images -g -a claude-code -y --copy`

## `seo-local`

Website-level local SEO belongs here: business-type detection, NAP consistency, citations, reviews, location pages, local schema, service areas, and multi-location structure. Checks adjust for brick-and-mortar, service-area, and hybrid businesses and for the detected industry.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-local/SKILL.md
- Installed at: `~/.claude/skills/seo-local/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches the business site and public citation or review evidence. API-based map and profile checks belong to `seo-maps`; this skill does not edit a Google Business Profile.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-local -g -a claude-code -y --copy`

## `seo-maps`

Maps-platform evidence is separate from the on-page work in `seo-local`. This skill supports geo-grid rank scans, GBP audits, review velocity, cross-platform NAP checks, competitor-radius mapping, Share of Local Voice, and LocalBusiness schema derived from API data.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-maps/SKILL.md
- Installed at: `~/.claude/skills/seo-maps/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Free checks call Overpass and Geoapify; advanced tiers use paid DataForSEO MCP and optional Google Maps API credentials. Geo-grid scans and review lookups are live external requests with vendor quotas.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-maps -g -a claude-code -y --copy`

## `seo-page`

One URL is the unit of work for this analysis. It checks title and heading structure, content depth, canonicals and robots directives, social metadata, schema, images, internal links, and page-level performance without turning the request into a site crawl.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-page/SKILL.md
- Installed at: `~/.claude/skills/seo-page/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches the requested URL and its linked assets, then runs local parsing and scoring. Performance or field-data enrichment may call other configured SEO services, but the base analysis needs no credential.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-page -g -a claude-code -y --copy`

## `seo-plan`

SEO strategy for a new or existing site is different from an issue audit, and this skill handles that planning work. It captures goals and constraints, reviews competitors, designs information architecture and internal links, and turns industry templates into a phased roadmap.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-plan/SKILL.md
- Installed at: `~/.claude/skills/seo-plan/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches the current site and competitor evidence when URLs are supplied and writes planning output. Keyword and authority estimates depend on whichever live-data extensions are configured.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-plan -g -a claude-code -y --copy`

## `seo-profound`

Time-series brand citation rates, prompt coverage, co-cited competitors, and spike or drop alerts across ChatGPT and Perplexity come from Profound. The extension complements point-in-time vendor checks by making weekly and monthly citation trends the primary evidence.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/profound/skills/seo-profound/SKILL.md
- Installed at: `~/.claude/skills/seo-profound/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires `PROFOUND_API_KEY` and the Profound extension. Calls a paid external API for tracked prompts and brand-mention history; brand and prompt sets leave the local environment.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-profound -g -a claude-code -y --copy`

## `seo-programmatic`

Pages generated at scale from CSV, JSON, an API, or a database need this planning and audit process. It evaluates record uniqueness and freshness, designs URL and template rules, automates internal-link planning, and sets thin-content and index-bloat gates before rollout.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-programmatic/SKILL.md
- Installed at: `~/.claude/skills/seo-programmatic/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: May read local datasets or inspect supplied API and database shapes. It produces an architecture or audit and does not bulk-publish pages; credentials for live data sources remain project-specific.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-programmatic -g -a claude-code -y --copy`

## `seo-schema`

Schema.org detection, validation, and generation are grouped in this skill, with JSON-LD as the preferred format. It checks required properties, data types, absolute URLs, dates, deprecated types, and current Google rich-result support before proposing code.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-schema/SKILL.md
- Installed at: `~/.claude/skills/seo-schema/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches page source and may consult mutable Schema.org and Google rich-result documentation. Generated JSON-LD is output for review and is not injected into the target site.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-schema -g -a claude-code -y --copy`

## `seo-seranking`

SE Ranking supplies live AI Share of Voice across ChatGPT, Gemini, Perplexity, Google AI Overviews, and AI Mode, along with SERP, backlink, and competitor data. This skill reports each platform separately with sample-size context.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/seranking/skills/seo-seranking/SKILL.md
- Installed at: `~/.claude/skills/seo-seranking/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires `SERANKING_API_KEY` and the SE Ranking extension. Live REST calls send brand, prompt, keyword, or domain inputs to a paid vendor and consume its quota.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-seranking -g -a claude-code -y --copy`

## `seo-sitemap`

XML sitemap validation and generation share this workflow. It checks protocol limits, status codes, canonical and noindex conflicts, `lastmod`, robots references, redirects, and missing crawled pages, and can generate a split sitemap plan.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-sitemap/SKILL.md
- Installed at: `~/.claude/skills/seo-sitemap/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches sitemap files and sampled URLs and may crawl the site for comparison. Generated XML is local output; the skill does not upload or submit it to search engines.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-sitemap -g -a claude-code -y --copy`

## `seo-sxo`

A technically sound page can still target the wrong intent or page type; this skill tests that mismatch. It reads the SERP backward, derives user stories from ranked results, scores the page through several personas, and can produce a wireframe tied to observed intent.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-sxo/SKILL.md
- Installed at: `~/.claude/skills/seo-sxo/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Fetches the target page and needs live Google SERP evidence, either through available search tools or an SEO data extension. Persona scores are heuristic and should retain cited result evidence.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-sxo -g -a claude-code -y --copy`

## `seo-technical`

Crawlability, indexability, URL structure, mobile behavior, security headers, JavaScript rendering, structured data, Core Web Vitals, and IndexNow checks form this technical audit. The skill keeps those findings separate from content strategy and records which crawler or protocol each rule affects.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-technical/SKILL.md
- Installed at: `~/.claude/skills/seo-technical/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Crawls public URLs, headers, robots files, sitemaps, and rendered pages through shared scripts. Field performance data and IndexNow submission require separate configured services; the base audit does not submit changes.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-technical -g -a claude-code -y --copy`

## `seo-unlighthouse`

A local multi-page Lighthouse sweep is useful when PageSpeed quota, CI repeatability, or broad regression coverage matters. This wrapper runs Unlighthouse against a capped route set and aggregates median performance, accessibility, best-practice, and SEO scores.

- Source: https://github.com/AgriciDaniel/claude-seo/blob/main/extensions/unlighthouse/skills/seo-unlighthouse/SKILL.md
- Installed at: `~/.claude/skills/seo-unlighthouse/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Requires Node 18+ and `unlighthouse-cli`; the shared wrapper performs URL safety checks, starts browser processes, crawls the site, and writes JSON and HTML reports. No API key is needed.
- Install/update: `npx -y skills@1.5.18 add AgriciDaniel/claude-seo --skill seo-unlighthouse -g -a claude-code -y --copy`
