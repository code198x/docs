# The Vault

The Vault is our encyclopaedia of people, companies, systems, hardware, software, games, culture and related subjects in the project's period, and beyond where needed to explain them. It gives fuller context room to breathe while lessons retain enough explanation for the immediate task.

## Organisation

| Type | URL Pattern | Purpose |
|------|-------------|---------|
| People | `/vault/people/{slug}` | Programmers, artists, musicians, designers |
| Companies | `/vault/companies/{slug}` | Studios, publishers, hardware manufacturers |
| Groups | `/vault/groups/{slug}` | Scene collectives, demo groups, informal organisations |
| Games | `/vault/games/{slug}` | Notable games referenced in curriculum |
| Demos | `/vault/demos/{slug}` | Demo scene productions and digital art showcases |
| Genres | `/vault/genres/{slug}` | Game genres, subgenres, and design movements |
| Techniques | `/vault/techniques/{slug}` | Programming techniques and approaches |
| Tools | `/vault/tools/{slug}` | Development tools, trackers, databases, archives |
| Emulators | `/vault/emulators/{slug}` | Emulation software preserving vintage platforms |
| Hardware | `/vault/hardware/{slug}` | Chips and components (SID, VIC-II, PPU) |
| Systems | `/vault/systems/{slug}` | Platforms (C64, Spectrum, Amiga, NES) |
| Culture | `/vault/culture/{slug}` | Movements and cultural context |
| Events | `/vault/events/{slug}` | Demo parties, LAN events, conferences |
| Magazines | `/vault/magazines/{slug}` | Gaming press, computing magazines, fanzines |
| Books | `/vault/books/{slug}` | Books about gaming, programming, computing history |
| Phenomena | `/vault/phenomena/{slug}` | Cultural phenomena, industry events, defining moments |
| Distribution | `/vault/distribution/{slug}` | Software distribution methods (shareware, cover tapes) |
| Communities | `/vault/communities/{slug}` | Subcultures and communities (demo scene, modding) |


Use the existing category and canonical entry when one fits. A new entry should answer a useful question or support a meaningful curriculum connection, not merely increase a count.

## Entry contract

The website's `src/content.config.ts` is authoritative for accepted fields. Every entry requires `title`, `subtitle`, `summary`, `category`, `ai_generated` and `reviewed`; tags default to an empty array and platforms are optional. Use existing platform identifiers consistently.

Set provenance honestly. `ai_generated` records machine-written prose; `reviewed` records a person checking and signing off the claims. These are independent. Do not mark an entry reviewed because an automated check passed.

| Category | Start Field | End Field | Display Label | Example |
|----------|-------------|-----------|---------------|---------|
| People | `born` | `died` | Lived | `born: 1960` (alive) |
| Companies | `founded` | `dissolved` | Active | `founded: 1987`, `dissolved: 2001` |
| Groups | `founded` | `dissolved` | Active | `founded: 1987` (still active) |
| Games | `released` | — | Released | `released: 1993` |
| Demos | `released` | — | Released | `released: 1993` |
| Genres | `emerged` | `ended` | Era | `emerged: 1980` (ongoing) |
| Techniques | `originated` | `deprecated` | Used | `originated: 1980` (still used) |
| Tools | `released` | — | Released | `released: 1987` |
| Emulators | `released` | — | Released | `released: 1997` |
| Culture | `emerged` | `ended` | Period | `emerged: 1985`, `ended: 1995` |
| Events | `emerged` | `ended` | Held | `emerged: 1992` (ongoing) |
| Magazines | `founded` | `dissolved` | Published | `founded: 1984`, `dissolved: 1992` |
| Books | `released` | — | Published | `released: 2003` |
| Phenomena | `emerged` | `ended` | Period | `emerged: 1983`, `ended: 1985` |
| Distribution | `emerged` | `ended` | Era | `emerged: 1980` (ongoing) |
| Communities | `emerged` | `ended` | Active | `emerged: 1985` (ongoing) |
| Hardware/Systems | `introduced` | `discontinued` | Produced | `introduced: 1982`, `discontinued: 1994` |


Dates must have evidence. Omit or use the schema's nullable field when unknown; do not invent a beginning or end to make a timeline neat. Additional structured fields, including publishers and hardware relationships, must match the actual schema and distinguish an entity from its parent organisation.

## Writing and evidence

Start with what the subject is and why it matters here. Let the structure follow the material: short entries need not repeat a long template, and a complex subject may need several focused sections. Use useful images and sound where rights, provenance and technical quality allow. Captions explain what the reader can learn from them.

Cite checkable evidence next to substantive claims: title, author or organisation, edition/date, page or section, and a public link when available. Name original sources directly. Never expose private collections, local source paths or internal library identifiers in public content or repositories.

Distinguish documented facts, recollections, allegations, disputed accounts and interpretation. Do not invent motives, dialogue or convenient origin stories. Check claims of priority and credit collaborations. Treat harmful conduct honestly, proportionately and in age-appropriate language; neither technical achievement nor historical context excuses it. See [Writing voice](writing-voice.md).

A dispute, allegation, lawsuit or falling-out between named people or companies needs at least two independent sources. One party's own account, however clearly attributed, is not enough on its own: keep only what a second source confirms.

An entry is about its subject, not about Code198x. Do not describe how the subject shapes the curriculum, calibrates a game, informs the project's voice or appears in a brief, and do not name a module whose place in the course is undecided. A plain link to a published lesson that uses the subject is fine; see [Connections and review](#connections-and-review).

Corrections belong in the corrected text. Git and the pull request explain the change; the reader does not need an editorial history appended to every entry.

## Connections and review

Link selectively to related Vault entries, fuller conceptual explanations and lessons that use the subject. A technique entry gives context; a Pattern Library entry gives an adaptable implementation. Avoid reproducing either inside the other.

Before publication check sources, dates, names, internal links, image rights and alt text, and the actual rendered page. Use the website's existing Vault validation scripts for schema, links, dates, source and imagery checks as applicable. Automated checks support editorial review; they cannot establish historical truth.

## Reviewing existing entries

Every existing entry was machine-written and is unreviewed. An unreviewed entry stays published with its "Not yet fact-checked" footer, but is excluded from search indexing and the sitemap until it is reviewed. Links to it keep working.

Review in batches of about ten entries, in priority order: the Spectrum and UK entries a CRASH! Live visitor meets first, then entries linked from published lessons, then the rest by category.

For each entry, an agent checks the frontmatter dates and every substantive claim. Evidence comes from period magazines, manuals and datasheets first, cited by publication, issue or edition, and page. A public web source is a fallback where no period source exists, and is marked as secondary. The agent corrects wrong claims, removes or qualifies unsupported ones, cites what it verified, and replaces any reference to a private collection with a statement about the public sources. It records each claim's verdict in an evidence report.

The review also makes the entry worth reading. Much of the machine-written prose is accurate but dry: generic summary, lists of facts and repeated conclusions. Rewrite it where it reads flat. Open with why the subject mattered and what is surprising about it; prefer concrete, sourced detail (figures, names, what a period magazine actually said, what the thing was like to use) to general statements; use active voice and varied sentences; tell the story the evidence supports. Engaging is not the same as hyped: no unsupported superlatives, aphorisms, rhetorical questions or punchline endings, and every added detail is verified and cited like any other claim.

Each batch is one pull request whose description carries the evidence report. The owner's approval of that pull request is the person's sign-off: the pull request sets `reviewed: true` on the entries it covers. An agent's check alone never sets it.

While reviewing, add any subject an entry mentions but the Vault lacks to [the candidates list](../vault-candidates.md), with the entries that should link to it.

Merge entries that duplicate each other, with redirects. Other cuts, including out-of-period entries, are a separate decision.
