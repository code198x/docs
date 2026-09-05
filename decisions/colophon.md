# Decision: the colophon

A page saying what this site is made of and who made it. People are derived; the rest is authored.

## The decision

`/colophon` credits four things: the **people** who have contributed, the **typefaces** the site sets its text in, the **tools** it is built with, and a pointer to how its **sources** are handled.

It is not a contributors list with a page around it. A colophon traditionally states how a thing was made, and this project has unusually good material for one — three libre typefaces, a family of assemblers and emulators it wrote itself, and a reference library with recorded provenance.

## People are derived, never hand-kept

Contributor names come from git history across the organisation's repositories, written to a committed file by a script and read by the build. Nobody types a name into a list.

**Why not fetch at build time.** The site deploys from a daily cron on a date gate. A GitHub API call inside that build adds a network dependency and a rate limit to an unattended publish, and the failure is quiet in the worst way: a rate-limited fetch renders an *empty* colophon rather than failing the build. The same reasoning that keeps heavy build steps out of the scheduled deploy applies here with more force, because the failure is invisible.

**Why not hand-keep it.** A second copy of who contributed is only ever as fresh as the last person who remembered both — the failure [state-lives-in-catalogues.md](state-lives-in-catalogues.md) exists to prevent. A hand-kept credits list goes stale the first time someone contributes during a busy week, and a missing name is a worse failure than a missing page.

So: a scheduled workflow regenerates the file and opens a pull request. A new contributor appearing is something to see and merge, not something that happens silently.

## Which repositories count

`website`, `docs`, `code-samples`, `scripts`, and the four retired `*-dev` repositories.

The retired ones are included deliberately. They hold real work that really happened, and dropping them because the containers were retired would erase contributions rather than archive them.

Excluded: `.github` (organisation configuration, not the project) and `substack-drafts` (drafts, not published work).

## No counts, and no ordering by volume

Names appear alphabetically. No commit counts, no ranking, no "top contributor".

A Vault entry and a corrected typo are both one commit. Any number makes that comparison visible, and it is the wrong comparison — it measures the shape of someone's git history rather than what they gave. It would also turn the page into a leaderboard, which is a poor fit for a project whose contribute page says in as many words that you will not get equity.

## Tools and typefaces are authored, not derived

The opposite rule to people, and deliberately so.

Deriving the tools list from `package.json` would print 189 packages, most of which are transitive and none of which anyone chose. The list worth reading is the handful that shaped the site — an editorial statement, which is exactly the kind of thing a human should write and keep. It changes when a decision changes, not on its own.

The typefaces are Literata, JetBrains Mono and Nebula Sans, all under the SIL Open Font Licence, whose texts already ship in `public/fonts/`. The colophon links those licence files rather than restating them.

## Sources are pointed at, not restated

[`/standards`](../../website/src/pages/standards.astro) already answers "how we know what we claim" — sourcing, proof levels, attribution, and the disclosure that drafting help does not make a claim true. The colophon links it. Restating any of it would create the second copy this project keeps ruling out.

## Drift triggers

- Typing a contributor's name into a file by hand, for any reason, including "just this once until the script runs".
- Adding a commit count, a ranking, a "since" date used as seniority, or a most-active section.
- Moving the contributor fetch into the site build.
- Deriving the tools list from the dependency tree.
- Restating the sourcing methodology here instead of linking `/standards`.
- Dropping the retired `*-dev` repositories from the scan because they are no longer active.

## Relates to

- [state-lives-in-catalogues.md](state-lives-in-catalogues.md) — why the people list is derived.
- [the-project-is-free-and-non-commercial.md](../../../decisions/the-project-is-free-and-non-commercial.md) — why the page offers recognition rather than reward.
