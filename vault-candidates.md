# Vault candidate backlog

[The structured backlog](vault-candidates.csv) holds proposed subjects, why they might help readers and the existing entries that should link to them. It is the single candidate list. A row is a possibility to assess, not a commissioned article or a public stub. Initial candidates need triage; their names, categories and reasons are proposals, not verified historical claims.

## Fields

| Field | Meaning |
|---|---|
| `id` | Stable identifier, such as `VC-0001`. Allocate the next unused number; never renumber or reuse an ID. It is not an article slug. |
| `subject` | Proposed subject name. Different subjects may share a name; check the category and reason. |
| `category` | Proposed Vault category. Confirm it during triage. |
| `status` | One of the states below. |
| `why` | The existing reason to consider this subject. Verify it before promoting the candidate. |
| `link_from` | Semicolon-separated referring sources: existing Vault paths (`category/slug`), or `candidate:VC-0001` for a planned source identified by its existing candidate ID. These record intended backlinks, not links that already exist. |
| `triage_notes` | Scope, checks for existing coverage and aliases, source leads, relevant lessons and the reasoning behind a triage decision. |
| `covered_by` | Semicolon-separated paths of existing Vault entries that cover the subject, required for `covered` and `published`. |
| `issue` | The canonical `code198x/website` issue URL once the candidate is ready and an issue exists. Blank until then. |

Use a CSV-aware editor or Python's `csv` module. Quotes and commas in names and reasons must survive editing. Keep the header and field order. Add new candidates to the CSV with the next ID and `needs-triage`; do not add a second list here. Keep resolved records and their IDs so later reviews can recognise subjects already assessed.

For an unwritten referring entry, use its stable candidate identity rather than a proposed URL. For example, `candidate:VC-2826` identifies the women's computing theme as a planned source. The referenced record must exist and cannot be the referring candidate itself. Keep any earlier proposed path in `triage_notes` for context; a candidate reference does not reserve a URL or establish publication. Once the referring entry is published, check its actual path and replace the candidate reference with that path.

Candidate references are allowed only in `link_from`. `covered_by` always names actual entry paths: another candidate is not evidence that coverage exists.

## Triage and status

| Status | Meaning and required evidence |
|---|---|
| `needs-triage` | Scope and existing coverage have not yet been checked. No issue is created at this stage. |
| `ready` | The subject earns a distinct article. Notes record its scope, a check of existing entries and aliases, useful source leads and the benefit to readers. It can now receive a writing issue. |
| `in-progress` | Writing has started against the linked issue. Retain the triage notes. |
| `covered` | Existing coverage already serves the reader. Record the entry paths and explain the match; arrange any missing backlinks through the existing issue workflow. |
| `published` | The finished entry and required backlinks are published and verified. Record the entry path and retain the issue link. |
| `deferred` | A decision has been made to leave this subject for later. Record why and what would justify reconsidering it. |

Read the referring entries before deciding what the candidate means. Check existing titles, aliases, redirects and relevant sections, not just matching filenames. A matching name is a prompt to inspect coverage; it is not enough to merge or discard a candidate. Likewise, an absent match does not prove an article is missing.

Prioritise candidates that answer a concrete question in a published lesson or help readers of several existing entries. Referring-entry counts help find those candidates; they do not establish importance or readiness. Check the sources and write the scope before setting `ready`. For a combined row, decide whether it needs one article, several, or an existing section. If splitting it, retain the original ID with a note pointing to the new IDs.

Do not remove a row because an automated scan no longer finds its subject. The website's `node scripts/vault-candidates.mjs` is a discovery aid; its output is not a replacement for this backlog. See [the Vault specification](specifications/vault.md#reviewing-existing-entries) for the evidence and publication standard.

## Open an issue when ready

Writing issues belong in `code198x/website`, which owns the articles. The CSV owns candidate identity and triage; the issue owns the writing task. Record the issue URL in the CSV as soon as it exists and update both when work starts or is published.

Before creating an issue, inspect `issue` and search **open and closed** website issues for the candidate ID, name and aliases. Reuse an existing issue where it covers the same work. A closed issue may establish that the subject is already covered; inspect its outcome before opening another. Do not retry an uncertain creation until you have searched for the first result.

Use a title such as `Write the Vault entry for <subject> (VC-0001)`. Use the existing `enhancement` and `area:curriculum` labels, adding an existing `system:` label only when the task is specific to that machine family. Do not create a new label taxonomy or a bulk issue for every untriaged row.

Copy this outline into the issue and replace the placeholders with the triage findings:

```markdown
Candidate: VC-0001 — <subject>
Backlog: https://github.com/code198x/docs/blob/main/vault-candidates.csv

## Reader need and scope
<Who needs this, what the article explains, and its boundaries.>

## Existing coverage checked
<Entry titles, aliases, sections and related open or closed issues inspected;
why this deserves a separate article.>

## Source leads
<Checkable primary sources where available; note gaps and secondary fallbacks.>

## Backlinks
<Links to each referring article or lesson that should gain a useful link.>

## Completion
- [ ] Write and source the article under the Vault specification.
- [ ] Add the agreed backlinks; verify links, sources and rendered pages.
- [ ] Supply the evidence report and obtain human sign-off for reviewed status.
- [ ] Verify publication, then record the published path and status in the backlog.
```

## Validate and inspect

Run from this repository with Python 3.13 or later; no third-party packages are required:

```sh
python3.13 scripts/check_vault_candidates.py
python3.13 scripts/check_vault_candidates.py --status needs-triage --category hardware --limit 20
python3.13 scripts/check_vault_candidates.py --website ../website --limit 20
```

The checker validates the entire CSV, including planned source IDs, before displaying a filtered list. It sorts displayed candidates by the number of distinct referring sources, with ID as the tie-breaker. `--website` optionally checks every existing-page reference against a website checkout; point it at the checkout you are actually using. It recognises Vault collection MDX files and concrete Game Study `index.astro` pages. It does not infer arbitrary pages from dynamic routes or assess prose, historical claims, aliases, issue state or a successful production build.

Run the checker's regression tests with `PYTHONDONTWRITEBYTECODE=1 python3.13 -m unittest discover -s scripts -p 'test_*.py'`. They exercise malformed records, duplicate identities, incomplete status changes and filtering that must not hide invalid rows.

## Existing scope notes

The *Your Sinclair* Smash Tapes and *Sinclair User* Megatape fit better as sections of `distribution/cover-tapes` than as entries.

Graftgold's 16-bit games (*Paradroid 90*, *Fire & Ice*, *Uridium 2*) fit better as a section of `companies/graftgold`, and Gilsoft's The Illustrator as a section of `companies/gilsoft` or `tools/the-quill`.
