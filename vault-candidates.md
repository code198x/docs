# Vault candidate backlog

[The structured backlog](vault-candidates.csv) holds proposed subjects, why they might help readers and the existing entries that should link to them. It is the single candidate list. A row is a possibility to assess, not a commissioned article or a public stub. Initial candidates need triage; their names, categories and reasons are proposals, not verified historical claims.

## Fields

| Field | Meaning |
|---|---|
| `id` | Stable identifier, such as `VC-0001`. Allocate the next unused number; never renumber or reuse an ID. It is not an article slug. |
| `subject` | Proposed subject name. Different subjects may share a name; check the category and reason. |
| `category` | Proposed Vault category. Confirm it during triage. |
| `scope` | Semicolon-separated scope axes the subject belongs to: `region:<slug>` for where it was made or used (`region:ussr`, `region:japan`, `region:east-germany`) and `period:<decade>` for when (`period:1960s`). Set during triage; leave blank when neither says anything useful. |
| `status` | One of the states below. |
| `why` | The existing reason to consider this subject. Verify it before promoting the candidate. |
| `link_from` | Semicolon-separated referring sources: existing Vault paths (`category/slug`), or `candidate:VC-0001` for a planned source identified by its existing candidate ID. Lessons record what they want in their own `wants` frontmatter instead (see below). These record intended backlinks, not links that already exist. |
| `triage_notes` | Scope, checks for existing coverage and aliases, source leads, relevant lessons and the reasoning behind a triage decision. |
| `covered_by` | Semicolon-separated paths of existing Vault entries that cover the subject, required for `covered` and `published`. |
| `issue` | The canonical `code198x/website` issue URL once the candidate is ready and an issue exists. Blank until then. |
| `blocked_by` | For `blocked` only: the issue in a family tool repository the entry waits on, such as an Emu198x issue for a machine it can't yet capture. See [blocked work](content-candidates.md#blocked-work). |

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
| `blocked` | The work can't go on until a family tool changes. Name the tool issue in `blocked_by` and say what is waiting in the notes. |
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

The checker validates the entire CSV, including planned source IDs, before displaying a filtered list. It sorts displayed candidates by demand, with ID as the tie-breaker: each lesson that wants the candidate counts 3, each existing Vault entry in `link_from` 1, and a planned candidate nothing. Lesson wants are only counted with `--website`. `--website` optionally checks every existing-page reference against a website checkout; point it at the checkout you are actually using. It recognises Vault collection MDX files and concrete Game Study `index.astro` pages. It does not infer arbitrary pages from dynamic routes or assess prose, historical claims, aliases, issue state or a successful production build.

Run the checker's regression tests with `PYTHONDONTWRITEBYTECODE=1 python3.13 -m unittest discover -s scripts -p 'test_*.py'`. They exercise malformed records, duplicate identities, incomplete status changes and filtering that must not hide invalid rows.

## What lessons want

A lesson lists the Vault pages it would link to for depth but can't yet, in its frontmatter: `wants: [VC-0123, games/example]`. A want is a candidate ID, or the path of an existing entry still awaiting review. The website rejects any other form, and its `check-lesson-wants.mjs` fails when a wanted entry doesn't exist. Wants live in the lessons, so dropping one drops the demand; nothing here is stored or deleted.

With `--website`, the checker counts each lesson that wants a candidate in its demand, and fails if a lesson wants a candidate ID that isn't in this backlog. `--wanted-reviews` lists the entries lessons want in two groups: unreviewed entries, which are review demand, and reviewed entries a lesson still only wants. The website only warns about the second group, so a review batch isn't blocked by lessons it never touched; the factory's link pass turns them into links.

```sh
python3.13 scripts/check_vault_candidates.py --website ../website --wanted-reviews --limit 20
```

## Expand from an entry

`scripts/expand_vault_entry.py` proposes candidates related to one existing entry, from three sources: names its prose emphasises that have no entry yet, its neighbours in the knowledge graph (publishers, developers, games and people, with the magazine or catalogue record for each), and existing candidates it names whose `link_from` lacks it. It never creates entries. A name that matches more than one graph identity of the same type, nearly matches something that already exists, or has no known category comes back as a question, not a proposal.

```sh
python3.13 scripts/expand_vault_entry.py companies/ultimate --website ../website
python3.13 scripts/expand_vault_entry.py companies/ultimate --website ../website --apply
```

With `--apply` it appends the new candidates (`needs-triage`, citing the entry in `link_from`) and the `link_from` additions, then revalidates the backlog and leaves the file unchanged if anything is invalid. Review the result as a pull request. The graph lives in the umbrella's `reference/` library, so the step runs locally; without it, pass `--no-graph` and only the prose and the queue are used.

## Lanes for world computing and early subjects

Demand alone mirrors what the Vault already covers, which leans towards British and American machines of the 1980s. Two lanes keep the scope axes in view:

- **world:** any `region:` other than `region:us` or `region:uk`. The lane takes regions in turn, each region's candidates in demand order, so one well-covered region (Japan has the most) can't fill it. A candidate with two world regions stands in the first listed.
- **early:** `period:1950s` or `period:1960s`, in demand order.

```sh
python3.13 scripts/check_vault_candidates.py --status needs-triage --lane world --limit 20
python3.13 scripts/check_vault_candidates.py --status needs-triage --lane early --limit 20
```

A batch takes at least a third of its subjects from these lanes whenever they hold candidates, and the rest from the overall ranking. Old machines come first in both, then their era (see [Run a batch](#run-a-batch)). Lanes only see candidates whose `scope` is set, so triage records it.

Every candidate's `scope` was backfilled on 6 November 2026 by a model pass over each row's subject, reason and notes, with instructions to leave a field blank rather than guess. 99 rows were left empty. These are prioritisation hints, not checked facts: triage confirms or corrects a candidate's scope along with the rest of the record.

## Run a batch

The `vault-batch` workflow ([`workflows/vault-batch.js`](workflows/vault-batch.js)) runs the whole batch process and ends in two draft pull requests for review. It runs in Claude Code on the machine that holds the primary-source library, because the research reads that library; a hosted runner can't.

In Claude Code, type `/vault-batch` or ask it to "run the vault-batch workflow". With no arguments it takes ten candidates from the ranking: at least a third from the lanes, taken in turn, and the rest by demand. Throughout, the machines of the 1980s and earlier (`systems` and `hardware` with a `period:` of the 1950s to the 1980s) come first, then everything else from those decades, and only then later subjects. That keeps batches on the project's centre: by demand alone, well-linked modern consoles and studios would lead. Within the world lane, regions still take turns at each of those steps. Name your own list instead with `ids`, or change the number with `size`:

```text
run the vault-batch workflow
run the vault-batch workflow with size 5
run the vault-batch workflow with ids VC-0018 VC-0931 VC-0936
```

To see which candidates the ranking would choose, without starting anything:

```sh
python3.13 scripts/next_vault_batch.py --website ../website --size 10
```

The workflow works in two new worktrees (`docs-batch-<slug>` and `website-batch-<slug>` beside the main checkouts) and never touches the main checkouts. For each candidate, one agent triages it and gathers claim-level evidence, a second writes the entry, and a third, which didn't write it, removes or qualifies anything the sources don't support. One agent then adds the incoming links, opens or reuses the writing issues, updates the queue rows and records the evidence in the website's `docs/reviews/<slug>/`.

Then `scripts/vault_batch_gates.py` runs every gate and the batch stops on any failure, before anything is committed. It checks that:

- nothing the batch adds, in either repository, names a private path: the local library's folders, the knowledge graph or a path on this machine. Both repositories are public, so this runs before anything is pushed, and the workflow also scans its writing issues, commit messages and PR descriptions with `--scan` before creating them;
- triage covers exactly the batch, and the queue rows agree with it;
- each draft is new, marked `ai_generated: true`, unreviewed unless approved (see below), and has an incoming link;
- every claim has a source, and a claim with only one is marked single-sourced;
- existing entries changed only by gaining Vault links, and nothing outside the Vault changed;
- a broken link planted in a draft makes the link check fail, and removing it makes it pass;
- the website's full release check passes, and the built drafts are `noindex` and absent from the sitemap.

To approve a batch, say so in conversation, naming the entries you approve (or the whole batch). The agent that applies it sets `reviewed: true` on those entries in the batch's own pull request and records your approval in the review directory as `approval.json`:

```json
{"approved_by": "Steve Hill", "date": "2026-11-07", "how": "in conversation", "entries": ["systems/magnavox-odyssey"]}
```

CI then requires exactly the approved entries to be reviewed and indexed, and every other draft to stay unreviewed and hidden. The workflow's own gate run passes `--drafts-only`, which fails if any approval exists: an agent never approves its own batch. Publication is still verified after the merge, as before.

If the gates fail, the worktrees stay for you to fix. Resume the run with the same arguments plus `attempt: 2`: the earlier stages come back from the resume cache and only the gates and the pull requests run again. You can also run the gates by hand from the docs worktree (see the script's help). Website CI runs them too, without the release check, on any pull request that adds a `docs/reviews/<slug>/triage.json`, so a batch made outside the workflow is checked as well. It reads the queue from the docs branch with the same name as the website branch, or from main if there isn't one. Approval and publication stay with a person: a batch's entries are unreviewed until then.

To start the workflow by name, link it into the Claude Code workflows folder of the directory you work from once (it is ignored by Git there):

```sh
mkdir -p ~/Projects/198x/.claude/workflows
ln -s ~/Projects/198x/Code198x/docs/workflows/vault-batch.js ~/Projects/198x/.claude/workflows/
```

## Existing scope notes

The *Your Sinclair* Smash Tapes and *Sinclair User* Megatape fit better as sections of `distribution/cover-tapes` than as entries.

Graftgold's 16-bit games (*Paradroid 90*, *Fire & Ice*, *Uridium 2*) fit better as a section of `companies/graftgold`, and Gilsoft's The Illustrator as a section of `companies/gilsoft` or `tools/the-quill`.
