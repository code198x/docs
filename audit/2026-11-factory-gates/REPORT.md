# Can the site's checks fail?

6 November 2026. Step 1 of the [content factory plan](../../plans/2026-11-06-content-factory.md): before the factory relies on a check, prove it goes red on a planted fault.

## Bottom line

Eight checks fail as they should when a fault is planted. One of them, the frontmatter quoting check, was run by nothing; website#1398 wires it in. Four Vault scripts are reports by design and can't fail. Two of those can become gates without grandfathering anything, and that needs Steve's decision. One check, `prose-dates`, is already red on `main` with two real disagreements that nobody saw, because nothing runs it.

## Method

Website `main` at `7cdabfd97`, in scratch worktrees. Each fault was planted alone, the check run, its exit status and output recorded, and the file restored before the next. The release build used for lychee and the type check was website#1397's branch, which differs from `main` only in a comment. No fault was committed.

## Results

| Check | Runs in | Planted fault | Result |
|---|---|---|---|
| `check-vault-links` | CI, `check:release` | Link to a missing Vault entry | **Fails** (exit 1), names the link |
| `check-vault-imagery` | CI, `check:release` | Image under `public/images/vault/` with no manifest | **Fails** (exit 1), names the file |
| `check-template-whitespace` | CI, `check:release` | Line break between prose and an inline tag | **Fails** (exit 1), names file and line |
| `check-curriculum-routes` | CI, `check:release` | A module requiring a later one in its catalogue | **Fails** (exit 1), names both modules |
| `check-frontmatter-quoting` | **Nothing** (before #1398) | `\'` in a double-quoted title | **Fails** (exit 1), names file and line |
| `check:types` | `check:release` | A new type error in `src/lib/platforms.ts` | **Fails** (exit 1); the 73 accepted baseline errors still pass |
| lychee offline link check | `check:release` | Broken internal link injected into a built page | **Fails** (exit 2), names the page |
| `check-vault-frontmatter-vs-prose` | Nothing | Frontmatter year changed on an entry with a `**Released:**` line | **Fails** (exit 1), names the entry; see notes |
| `check-vault-platform-balance` | CI, `check:release` | none needed | **Report**: no failing exit; 53 entries reported on `main`, exit 0 |
| `check-vault-sources` | Nothing | Citation block removed from a dated claim | **Report**: counts 1 uncited, exit 0 |
| `check-vault-dates` | Nothing | Release year moved six years from the press record | **Report**: flags it (+6), exit 0 |
| `find-vault-duplicates` | Nothing | Exact copy of an entry under a new slug | **Report**: scores the pair 1.000 with a warning, exit 0 |

The Playwright suites in `check:release` (536 tests) and in CI were not given planted faults. They are tests of behaviour rather than content gates, and they fail routinely on regressions.

### Notes

- **`prose-dates` is red on `main`.** Two disagreements: `games/diablo` (`released: 1996` in frontmatter, 1997 in the prose) and `people/louis-castle` (`born: 1965` in frontmatter, 1964 in the prose). Each needs a source before either value is changed.
- **`prose-dates` is narrow by design.** It compares only labelled fact lines (`**Released:** 1984`, `**Born:**`, and so on): 398 facts across 553 entries. A frontmatter change on an entry whose prose says "in the summer of 1983" or "released in 1984" goes unnoticed. Within its scope it works.
- **`check-vault-sources` and `check-vault-dates` say they are reports.** `sources`: "It reports; it does not fail. Grounding is a long job and a red build helps nobody." `dates`: "a ranked list of contradictions to read, not a verdict." The `sources` reason has lapsed: on `main` every one of 1,298 dated claims is cited.
- **`check-vault-dates` needs the reference corpus.** From a scratch worktree it exits 1 because `../../reference` doesn't exist. Set `REFERENCE_CORPUS` to `reference/_tools/search.sqlite`. On `main`, games alone produce 91 flags; every flag needs a person.
- **`find-vault-duplicates` separates copies from neighbours.** A planted copy scores 1.000; the highest pair on `main` is 0.801 (Vortex Software and Costa Panayi, a company and the programmer it was built around). 199 pairs score 0.45 or more.
- **A required CI gate depends on a live external site.** `tests/asm198x-links.spec.ts`, part of the required "Browser tests" gate, fetches every mapped page on asm198x.github.io. On website#1398, a change that touches no page, it failed with a 503 from GitHub Pages; the page answered 200 minutes later, and the failed job was re-run. The same test followed redirects, so it passed links that point at Asm198x's old redirect stubs.

## Fixed

- **website#1398** runs `check-frontmatter-quoting` first in `check:content`, as its header asks. `check:content` passes on `main` and exits 1 on the planted fault.
- **website#1399** links system pages to Asm198x's current instruction pages rather than the redirect stubs, and makes the publish test refuse redirects. With the old addresses restored, the test fails with `Received: 301`.
- **website#1404** puts the player back on the eleven system pages with a hardware render (website#1401). Running `check:release` for these changes found that the hardware gallery had replaced each player stage with the render, so `check-browser-player --built` failed on `main`. CI doesn't run that step, so only the local release check could catch it. Earlier release runs in this audit missed it because their scratch worktrees symlinked `public/emulators` from another checkout instead of letting the build stage the pinned player.

## Decisions (Steve, 6 November 2026)

1. **`check-vault-sources` becomes a gate.** `--strict` fails on any uncited dated claim; `check:content` runs it. Merged in website#1400.
2. **Duplicates become a gate at 0.9, with a confirmed-distinct list.** `find-vault-duplicates.mjs --fail-at 0.9`, with `scripts/vault-distinct-pairs.json`. Steve chose new or changed entries only; website#1400 gates every pair instead, which has the same effect today and needs no change to CI's shallow checkout. Merged in website#1400.
3. **The two `prose-dates` disagreements were careful prose, not errors, and the check now runs.** Louis Castle's evidence allows 1964 or 1965, so `born` is left unstated. `released` means earliest documented public availability (docs#286), so Diablo stays 1996 and its facts line leads with it. `check:content` runs the check. Merged in website#1400.
4. **`check-vault-dates` and `check-vault-platform-balance` stay reports.** The factory's Vault line attaches their output for each batch's new entries to the review notes.
5. **The Asm198x link test retries on a server error** before failing, so another site's outage doesn't turn a correct pull request red. Merged in website#1402.
