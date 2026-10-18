# Adventure evidence and limits

Research pass: 18 October 2026. This record separates execution, source inspection, retrospective testimony and interpretation. Read study.md for the reader-facing account.

## Chosen artefact

The design reference is the 350-point Crowther/Woods game. Executed: ODWY0350, Arthur O’Dwyer’s C99 port in [Quuxplusone/Advent at 142b61f37063cb00bc9037f67b19411f257099b1](https://github.com/Quuxplusone/Advent/tree/142b61f37063cb00bc9037f67b19411f257099b1/ODWY0350). The repository's root file is README, without a Markdown extension.

The port descends through Knuth’s CWEB treatment and comparisons with Woods’s source. Its author acknowledges possible discrepancies and bugs. It is not the original executable, a hardware emulator, a complete-game verification or proof of every historical release’s behaviour. System C compilation succeeded with one existing third-party warning: `advent.c:4145:9: warning: a function declaration without a prototype is deprecated in all versions of C [-Wstrict-prototypes]`. No source modification or new dependency was introduced.

WOOD0350 supplies the PDP-10 FORTRAN source/data comparison. Its advent.readme (18 March 1996) credits Alan H. Martin and a recovered LINK-10 regression-test copy. That is a preservation chain described by the archive, not an independently authenticated 1977 disk image. CROW0005 separately preserves recovered pre-expansion files; do not identify March 1977 file dates as Crowther's original composition date.

## Evidence ledger

| Claim or interpretation | Check and limit |
|---|---|
| Building objects persist as carried state | Bounded exploratory run: IN, TAKE LAMP, INVENTORY; port source object placement, carry/drop routines. This is a selected observation, not all object behaviour. |
| A locked route changes after using carried keys | Repeatable observe.py run and observations.json: failed DOWN, UNLOCK GRATE, successful DOWN. Entrance spoiler only. |
| OUT and SOUTH differ inside the building | Separate bounded run returned refusal for SOUTH and allowed OUT. Source R_HOUSE travel entries agree. No claim that direction words work this way throughout every version. |
| Parser accepts limited vocabulary/two words | ODWY0350 advent.c listen(), lookup(), streq(); vocabulary matching uses the first five characters. Not natural-language understanding. Avoid exporting this limit to The Hobbit, Level 9 or modern interactive fiction. |
| World can be represented as locations, routes, object state | Port make_loc/make_ins and object state; original FORTRAN travel/condition handling plus advent.dat location/travel tables inspected. Our diagram explains one rule, not the complete internal implementation. |
| Limited carrying and lamp power | Port holding_count >= 7; lamp_limit initialisation 330 or 1000 according to introductory instructions; clock/light handling. Original FORTRAN HOLDNG/LIMIT and lamp routines inspected. The study deliberately avoids a universal numeric limit. |
| Treasure return increases score, terminal scoring/endgame | Port score(), treasure location checks and closing logic; original FORTRAN scoring block identifies 350 total. No complete endgame playthrough claimed. |
| Random hazards, death/reincarnation | Source routines and responses inspected. No calibrated probability or successful complete recovery session claimed. |
| Crowther 1975–76; Woods expansion 1977; original already fantastical | Jerz final DHQ article, chronology and source comparisons. Distinguish dated files, family recollections and reconstructed chronology. Do not use the preprint when its wording differs. |
| Bedquilt/caving and Patricia Crowther’s survey contribution | Jerz’s interviews, records, source comparison and field visit; credit survey work without inventing Adventure co-programming. |
| Family and D&D | Attribute Crowther’s retrospective testimony through Jerz. No inferred trauma, personality or claim that one life event explains the game. |
| Research-network circulation | Jerz chronology and recovered-source discussion; selective access around institutions, not a claim of universal access or one unique distribution route. |
| BBC home adaptation and commercial support | Level 9 manual scan at mocagh.org/rainbird/colossaladv-manual.pdf. CHAIN and *TAPE identify the BBC instructions; no date inferred from hosting folder. “The Game”, “Hints”, “Implementation” explain extended endgame, postal clue and a-code/text compression. Claims are for this manual, not every 1982/1986 version. |
| Spectrum variety | CRASH 15, April 1985, Adventure Top 30 section. Colossal Adventure 23, Snowball 11, The Hobbit 17; mixed arcade/graphical/parser category, reader chart rather than market-share data. No inference that shared chart presence establishes influence. |
| Friction, invitation, trade-offs and mental imagery | Our design interpretation, supported by explicit examples. Not creator-attributed intent or measured player research. |

## Repeating the bounded run

Obtain the exact public source revision above separately; build only ODWY0350 with its existing Makefile. Run `python3 studies/adventure/observe.py /path/to/ODWY0350/advent /tmp/adventure-observations.json`. The script has a five-second timeout, checks blocked/unlocked/entered outcomes, carried objects, light and clean termination, and retains only two short critical extracts plus the complete response hash. It raises an error if the conditions are absent; an empty-output executable was used to confirm this failure path. No binary or game source is bundled.

The retained run contains 14 counted game turns and a normal exit. Command count and game-turn count differ because introductory/confirmation replies are not ordinary moves. A response hash is execution identity, not independent historical authentication.

## Rights and imagery

No explicit whole-repository licence was found covering ODWY0350. Public source availability is not permission to redistribute its code or binaries. This change includes neither. The thirteen-word response extract is used to criticise and explain the entrance rule; Adventure is credited to Will Crowther and Don Woods, with Arthur O’Dwyer credited for this modern port. No full transcript, puzzle walkthrough, borrowed image, map, audio or historical manual scan is distributed.

figures/grate-state.svg is our original schematic, with a stacked narrow-screen variant in figures/grate-state-phone.svg. Both show the same entrance rule. It is labelled as an explanation and has a text equivalent; it neither imitates a historical screen nor reproduces the cave map. A colourful editorial opening and genuine, bounded terminal captures remain a later visual pass; do not fill that gap with a fabricated historical screenshot.

## Still open

This is a substantial initial study, not a completed whole-game investigation. Run a human play/read session with unfamiliar players; test whether the descriptions explain the parser fairly. Independently examine deeper puzzle feedback, maze navigation, failure/recovery and the endgame before strengthening evaluative claims. Add proportionate, clearly identified captures where they explain play. Review original-era access/distribution sources and contemporary reception beyond the later Spectrum chart. Identify the exact Level 9 manual edition before supplying a release date or specific retail packaging claim. The Quill and The Hobbit onward links reuse reviewed Vault context; their detailed source investigations belong to those subjects. Publication and website integration remain unapproved.
