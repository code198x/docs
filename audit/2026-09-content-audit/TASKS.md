# Code198x website content audit — tasks

Started 2026-09-23. Scope: the whole site as it stands in the website working tree (uncommitted changes included). Output: findings only, no site edits. Facts are spot-checked against primary sources, weighted towards the CRASH! Live Spectrum path.

Criteria come from [PROJECT.md](../../PROJECT.md), [writing voice](../../specifications/writing-voice.md), [unit](../../specifications/unit.md), [Vault](../../specifications/vault.md) and [website](../../website.md).

Findings go in [REPORT.md](REPORT.md). Raw data (inventory, check output) sits alongside.

## 0. Set-up

- [x] Agree scope, output and location with Steve
- [x] Read the charter and specifications that define the standard
- [x] Record the website revision and working-tree state being audited

## 1. Inventory

- [x] Content inventory: every content file with collection, route, title, description, dates, draft state, provenance flags, word count and last Git change (`inventory.csv`)
- [x] Built-route inventory from `dist/`: every page the site actually emits
- [x] Reconcile the two: content without a route, routes without content, stray files in content folders
- [x] Summary counts by section and collection

## 2. Technical and structural checks

- [x] Unit tests and production build (build runs the route and Vault checks) — pass; separate scratch build, 2,468 pages
- [x] Existing Vault checks: links, sources, dates, prose-vs-frontmatter dates, duplicates, platform balance, imagery
- [x] Internal link check across the built site (broken links, links to redirects)
- [x] Orphan pages: built pages nothing links to
- [x] Redirects: every redirect target resolves
- [x] Page metadata: missing, duplicate, over-long or boilerplate titles and descriptions
- [x] Draft and future-dated content; RSS feed against what is live
- [x] Images: missing files, missing or weak alt text
- [x] Accessibility: compare against the recorded baseline

## 3. Content quality

- [x] Provenance: `ai_generated` and `reviewed` counts by collection and section
- [x] Thin and stub pages (word-count outliers per collection)
- [x] Production artefacts: TODOs, placeholders, prompt residue, editorial-history notes, correction banners
- [x] Private-source leaks: local paths and collection identifiers
- [x] House style: British spelling, “program”, banned words (“simply”, “obviously”)
- [x] Unsupported superlatives and origin claims (“first”, “invented”, “only”)
- [x] Prose lint (Vale) as an advisory pass
- [x] Duplicate and overlapping entries

## 4. Accuracy and currency

- [x] Status claims: landing pages, About, Start Here and track pages against catalogues and authored lessons
- [x] Support-surface wording on system pages (Emu198x / Code198x / Asm198x kept distinct)
- [x] Stale or time-bound language (“coming soon”, “this year”, dated plans)
- [x] Fact spot-check: sample weighted towards the Spectrum path, checked against primary sources
- [x] Citations: do substantive claims carry checkable sources?

## 5. Structure, navigation and coverage

- [x] Navigation and hub pages: labels, routes, starting points
- [x] Curriculum sequence integrity: catalogue order, unit numbering, gaps, retired content
- [x] Vault coverage against the scope axes (period, geography, form factor)
- [x] Out-of-period entries: Vault and timeline items after 2005 (added — 71 Vault, 10 timeline)
- [x] Editorial feeds (What’s New, From the Metal, Field Notes): currency and cadence

## 6. Report

- [x] Write REPORT.md: summary, findings ranked by severity, evidence, suggested owner
- [x] Review the report against this checklist; note anything skipped and why

## Added during the audit

- [x] Stray files in content folders: `systems/node_modules`, `systems/.astro`, tracked `vault/search.sqlite`, `UNIT-BREAKDOWN.md` planning notes
- [x] Vault `sources:` notes: do they render publicly? Several name local library paths and editorial history
- [x] Manufacturer YAML `# TODO: verify` dates and placeholder coordinates
- [x] Vault platform identifiers: synonyms and ids outside the systems collection (added)
- [x] Live RSS feed links and legacy URLs (added)
