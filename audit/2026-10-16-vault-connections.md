# Vault connections and reading paths — 16 October 2026

The Vault already connects subjects extensively, but its most deliberate discovery routes cover a small part of that material. We should repair a few concrete editorial gaps and publish two short paths through existing reviewed articles before commissioning more content or building a broader discovery system.

## Scope and evidence

Source baseline: [website main at 7412570](https://github.com/code198x/website/tree/7412570891a79c0485b3d894cefd4cf74eb924eb). The source checkout had no tracked modifications. This audit changes no website article or interface. The current [Vault specification](../specifications/vault.md#presentation-and-discovery) deliberately calls for curated features, a complete subject directory and title search; these remain the starting point.

Separately, the public site was inspected with Chromium at 1440 × 1000 and 390 × 1000 on 16 October 2026, completing at 16:19 UTC. The eight routes checked at both widths were the Vault contents; Culture, People and Techniques category pages; Xenon 2; Jack Tramiel; Manami Matsumae; and Software Crossed What Machines Could Not. All sixteen page loads returned HTTP 200. Their observed discovery surfaces agree with the source observations below; this does not establish the deployed commit ID.

The link inventory scanned all MDX entries under `src/content/vault`, parsed their YAML frontmatter, and extracted literal Markdown and HTML links to `/vault/`. It excluded fenced code and `<Sources>` blocks, removed fragments/queries and trailing slashes, and counted each source–destination pair once where the destination exists. It includes prose and See also links. It does not expand components, resolve redirects, or count generated navigation, lesson links or citation-only links. Counts describe this source scan rather than all possible ways to reach an article.

| Measure | Result | Interpretation |
|---|---:|---|
| Vault entries | 1,485 | All carry `reviewed: true`; this audit does not repeat their historical fact-checking |
| Distinct directed authored body links to existing entries | 15,248 | Considerable existing connection work |
| Directed edges with a reverse edge | 7,562 | Asymmetry is not itself a defect |
| Entries without an outgoing body link to an existing entry | 0 | Every scanned article offers an authored onward link |
| Entries without an incoming authored body link | 29 | Still accessible through directories/search and potentially other surfaces |
| Source articles with a configured Follow connections panel | 3 | Commando, SID and Colour Clash |

## What already works

- The contents page presents the Commando music trail: Rob Hubbard and the SID lead into arpeggios and HVSC. Its four explained edges are checked against real authored links. The resolver rejects missing/unreviewed promoted entries, repeated or disconnected nodes, unsupported edges and empty explanations.
- Colour Clash supplies a separate illustrated feature and three article connections. Four additional discoveries offer Tetris, Gunpei Yokoi, ProTracker and the Demo Scene.
- Techniques has three question-led starting cards, about colour clash, chords from one voice and software scrolling. These are entry points, rather than full multi-step itineraries.
- Xenon 2 already links David Whittaker and the Bitmap Brothers; the surrounding articles connect game publishing, soundtrack conversion and Renegade. We should expose this coverage rather than duplicate it.
- “When the Record Companies Sold Software” already covers the earlier record-business/software-publishing phase. It has incoming body links from Ariolasoft, Electronic Arts, Virgin Games and Reading the Charts. It is useful related context for later pop/game connections, with the distinct periods and relationships explained.
- Soviet Computing, Spectrum Clones, Brazilian Market Reserve, Brazilian Gaming, C64 Across Borders and Magazines Across Borders already form substantial regional coverage. Tramiel and Baer already have biographies covering their documented experiences. A lack of a broader itinerary does not mean those subjects are unwritten.

## Verified gaps

| Finding | Evidence at the baseline | Reader consequence |
|---|---|---|
| Named contributor has no link | `companies/atari.mdx:60` names Dona Bailey but does not link her existing biography | Readers following the Centipede credit cannot follow her name |
| Composer contributions are not surfaced from the games | Neither `games/mega-man.mdx` nor `games/shovel-knight.mdx` links Manami Matsumae; her biography has zero incoming body links | Existing sourced material about her work is harder to encounter from familiar games |
| A cross-border theme lacks incoming body links | `culture/software-crossed-what-machines-could-not.mdx` links PAPERsoft, Bajtek and Magazines Across Borders; none links back | Readers encounter examples without an obvious route to the connecting theme |
| A major machine does not lead to its regional account | `systems/commodore-64.mdx` does not link `culture/the-c64-across-borders.mdx` | Readers starting with the machine can miss how ownership and access differed across countries |
| Explicit paths concentrate on techniques | `vault-reading-paths.ts` supplies only the three Techniques questions; category rendering gates these to Techniques | Culture and People rely on directories rather than comparable guided starts |
| Article arrival loses wider incoming context | `[...slug].astro` renders configured edges from two small trails; `backlinks.ts` indexes unit pages only | An article does not generally reveal which other Vault articles discuss it |

The Matsumae repair requires fresh source checking before changing credits. Her biography cites the original Mega Man interview and the Shovel Knight soundtrack's two guest pieces. Preserve Jake Kaufman's principal score credit and do not transfer a first-game credit to Mega Man 2. The audit establishes a discovery/coverage gap, not a completed historical correction.

## Live discovery observations

The contents page's subject directory was expanded at 1440px and collapsed at 390px, as the specification permits. The music trail and feature remained visible in the mobile page. None of the sixteen checked pages had horizontal document overflow. Screenshots of the contents and Tramiel pages were captured at both widths; the mobile contents capture was visually inspected. This is a bounded navigation check, not a full accessibility audit.

The Culture and People pages had no question-led cards; Techniques showed all three. The four sampled articles had no configured Follow connections panel. Their sidebars displayed Details and Keep exploring, with no incoming Vault reading list. These observations concern the inspected routes; source inspection supplies the wider configuration count.

At both widths, the contents search returned Dona Bailey (one title), Soviet Computing (one title), and four titles for “music”: Beeper Music, Interrupt-Driven Music, Music Games and Tracker Music. “Bomb the Bass” and “Betty Boo” returned no matching titles. The interface accurately says “Search article titles”. This is intentional title search, not a broken full-text search. Explained editorial routes can reveal connections that a title query cannot.

## Small first tranche and tracking

Repair the four bounded editorial gaps first. Publish two short paths using existing reviewed articles: music/games/publishing and machines/software crossing borders. Select a small main sequence with optional branches, and explain each actual relationship. Do not require all suggested articles in one long itinerary.

Reuse [#781](https://github.com/code198x/website/issues/781) for the women's contributions theme and its reading route, under [#780](https://github.com/code198x/website/issues/780). That work already covers integration, discrimination and recognition; a second theme commission would duplicate it. Existing women in games and music should connect naturally to that route as the initial biographies appear.

Incoming article suggestions are a separate proposal. Decide whether a few curated selections or a bounded list of actual authored incoming links helps readers enough to justify implementation. Do not infer causation, personal motivations or historical relationships from tags or co-occurrence. A reciprocal link is not compulsory, and a new graph service is not a prerequisite for the editorial tranche.

The current design remains in place. New categories, a global navigation redesign, automatic semantic links and full-text search are not adopted by this audit. Unwritten film, music and geopolitical candidates remain in the candidate backlog, not broken links or prerequisites for these paths.

## Tracked issues

- [#796 — discovery tracker](https://github.com/code198x/website/issues/796) owns three native child issues.
- [#797 — bounded editorial repairs](https://github.com/code198x/website/issues/797) is the first delivery step.
- [#798 — two initial reading paths](https://github.com/code198x/website/issues/798) uses existing reviewed coverage.
- [#799 — incoming reading suggestions](https://github.com/code198x/website/issues/799) is an idea requiring a design decision before implementation.

Titles, open state, reciprocal parent references and all three native child relationships were read back after creation.

## Verification

- `node scripts/check-vault-links.mjs`: 25,972 references across `src/`, 1,485 entries and 187 redirects; all resolve. This checks destinations, not whether a missing link would be useful.
- Focused Vitest run for `src/lib/vault-features.test.ts`: all eight tests passed. Rejection cases exercise missing/unreviewed selections, invalid imagery and unsupported/disconnected/repeated/unexplained trail edges; the checks can fail on invalid data.
- Scoped Impeccable detector on the Vault index and explorer component returned an empty finding list. This supplementary scan does not validate editorial relationships.
- Live page and search checks are described above. No website build or publication is claimed, because this change records an audit and tracking only.
- Existing open and closed website issues were searched for Vault, reading-path and cross-link work. Closed #246 addressed resolving shipped lesson references; closed #369 addressed techniques grounding. Neither is an open owner for these discovery gaps. Existing #781 is reused for women's history.

## Entries with no incoming authored body link in this scan

These 29 IDs are investigation leads, not a bulk repair queue or a list of unreachable pages:

```text
companies/americana
companies/cascade-games
companies/durell
companies/natsume
companies/vulcan-software
culture/arcade-to-console
culture/moon-logic
culture/software-crossed-what-machines-could-not
culture/uk-gaming-boom
events/chaos-constructions
games/jackal
games/links-awakening
games/little-nemo
games/punch-out
games/reversi
games/snake-rattle-n-roll
games/snake
games/splatterhouse
games/suikoden
games/sunset-riders
hardware/d-sub-connector
people/brian-howarth
people/gargaj
people/manabu-takemura
people/manami-matsumae
people/neil-baldwin
phenomena/rpg-golden-age
software/aseprite
techniques/twister
```
