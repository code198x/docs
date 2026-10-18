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

No explicit whole-repository licence was found covering ODWY0350. Public source availability is not permission to redistribute its code or binaries. This change includes neither. The thirteen-word response extract is used to criticise and explain the entrance rule; Adventure is credited to Will Crowther and Don Woods, with Arthur O’Dwyer credited for this modern port. No full transcript, complete-game walkthrough, borrowed image, map, audio or historical manual scan is distributed.

figures/grate-state.svg is our original schematic, with a stacked narrow-screen variant in figures/grate-state-phone.svg. Both show the same entrance rule. It is labelled as an explanation and has a text equivalent; it neither imitates a historical screen nor reproduces the cave map. A colourful editorial opening and genuine, bounded terminal captures remain a later visual pass; do not fill that gap with a fabricated historical screenshot.

## Current review limits

Selected parser, puzzle, maze, time and recovery encounters have now been executed as recorded below. A human reading/play session, complete endgame execution, original-hardware/configuration validation, proportionate terminal captures and exact Level 9 manual issue identification remain open. No historical reviewed flag, publication or website integration is approved by these checks.

## Comprehensive expansion: execution and interpretation

The first draft's entrance-only evidence has been extended. [check-encounters.py](check-encounters.py) executes thirteen fresh-process encounters and checks seventeen outcomes, retaining [commands, counts and response hashes](deep-observations.json). Each response is limited to 65,536 bytes and three seconds; every process is reaped, including failure paths. The supplied native executable is still ODWY0350 at the original pinned revision, without SAVE_AND_RESTORE. No third-party source modification or dependency is needed. Reproduce with `python3 studies/adventure/check-encounters.py /path/to/ODWY0350/advent /tmp/adventure-deep-observations.json`.

The new run covers incomplete requests, noun-first dialogue, reversed word order, a noun alias, native save unavailability, bird/cage/rod conditions, snake removal and newly available travel, reversible bridge state, gold affecting a return route, reincarnation and lamp recovery, a marked maze self-loop, and nearby dropped keys satisfying the grate rule. It compares otherwise identical sessions for unknown-word, inventory and three-word rejection costs. The opening instructions and quit/reincarnation confirmations are not counted as ordinary commands in the game’s final turn total.

| Expanded claim | Exact source/observation boundary |
|---|---|
| Partial commands persist across prompts; noun-first forms work | Parser encounter and simulate_an_adventure’s verb/obj preservation and shift_words. Not a claim that arbitrary multi-clause grammar is supported. |
| Aliases and five-character lookup | build_vocabulary, lookup, streq; TAKE LANTERN reaches an already-carried object. Five-character matching does not mean arbitrary abbreviations work. |
| Three-word input differs between port and preserved FORTRAN | Native listen rejects extra words; original GETIN packs/extracts first and second words and has no identical length-rejection branch. The study explicitly limits the free rejection result to the tested port. |
| Unknown words and inventory consume a turn; long-form rejection does not | Four independent fresh sessions return 4, 5, 5 and 4 turns respectively, with the same starting/ending actions. This is an outcome comparison, not a count copied from the input array. |
| Lamp consumes power before vocabulary lookup | Port pre_parse/check_clocks_and_lamp and FORTRAN around TURNS=TURNS+1/LIMIT=LIMIT-1. Turn result is executed; internal lamp decrement is source-inspected, not independently memory-instrumented. |
| Not every subsystem advances identically on every input | Port control flow separates the outer movement/hostile-character path from inner command parsing. Do not describe one universal post-command world tick. |
| Bird capture requires a cage and absence of carried rod | Two runs establish distinct refusals and successful capture after dropping the rod. Inventory confirms the bird, not merely the already-carried cage. take_bird_or_cage corroborates. |
| Releasing bird changes snake/route state | Selected south route refuses before and reaches jewellery chamber after. Not a complete lower-cave walkthrough. |
| Rod toggles bridge | Same encounter creates bridge, crosses, removes it; attempt_wave and FISSURE prop. |
| Gold affects upward travel | Same encounter refuses upward travel while gold is carried, allows it once dropped. R_EMIST conditional route corroborates. |
| Marking a maze room reveals a self-loop | Dropped food remains in the NORTH result; R_LIKE1 maps N to itself. The original illustration does not reproduce the maze or an escape route. |
| Nearby keys suffice, including dropped keys | Executed unlock with dropped keys; attempt_open_or_close uses here(KEYS, loc), not only toting. Earlier carried-keys illustrations remain sufficient examples rather than necessary-condition claims. |
| Reincarnation changes inventory | Executed death/acceptance/empty inventory and lamp recovery at road. kill_the_player places other objects at the last safe place and extinguishes carried lamp; the selected run only exercises its lamp case. |
| Score and hints | score, say_score, offer and hints table. Seeing/depositing treasure, survival, later phases, hint costs and magazine-location bonus are source-inspected. No exhaustive maximum-score victory claimed. |
| Closing depends on treasure discovery, clock and qualifying location | tally, spot_treasure, clock1/clock2, check_clocks_and_lamp, close_the_cave and attempt_blast. Do not substitute “all treasure returned triggers the ending”. No endgame execution claimed. |
| Object relationships are partly special-case | carry/drop, take_bird_or_cage, bottle contents and object base/place/prop. Original simplified tables and richer-parser diagrams are explanations, not literal copies of either source's structures. |

### Source handling for the expansion

- Original preserved FORTRAN/data and modern port remain the gameplay evidence. Crowther chronology/caving/family and collaboration use Jerz’s final DHQ research article. A creator’s remembered circumstance is not asserted to cause a particular puzzle.
- P. David Lebling, Marc S. Blank and Timothy A. Anderson, “Zork: A Computerized Fantasy Simulation Game”, IEEE Computer 12.4 (April 1979), pp. 51–59: original design paper consulted through the IF Archive transcription in articles.zip (IEEE). Web-rendered transcription was readable; the direct university PDF timed out and no university PDF verification is claimed. Use for the bounded Zork comparison, not to assign later Zork features to Adventure.
- Inform Designer’s Manual fourth edition, §§26, 30–33: original later engine documentation for descriptions, grammar, object matching, scope and recovery from parser trouble. Our generic PUT/KEY/BOX example and stage diagram are original explanatory material, not accepted Adventure input or an exact universal execution order.
- Tim Anderson/Stu Galley, “The History of Zork”, New Zork Times, 1985: attributed retrospective account of influence and development. Do not repeat industry-productivity jokes as statistics.
- Dave Lebling, “They’re Never Satisfied”, New Zork Times, Fall 1984, p. 2: primary practitioner account of testing, including fictional consistency and writing alongside crashes. Not evidence that our study has had human play-testing.
- Graham Nelson, The Craft of Adventure, second edition (1995), “Bill of Player’s Rights”: later design criticism, not a universal historical law or current legal source. The study does not repeat the document’s old copyright advice.
- Microsoft Adventure, IBM Program Instructions, First Edition June 1981: visually inspected scanned spreads, title credit and printed pp. 2–3, 6–7. The title credits Gordon Letwin; printed p. 7 specifies 32K user memory, monitor, one drive and its own operating system. Printed pp. 22–23 were subsequently visually inspected: write-protect tab removal, SAVE, two numbered cave images, overwrite warning and numbered restore at loading. Their operation is documented, not executed here. No claim that this bootable edition is an ordinary DOS program.
- Level 9 BBC manual: loading commands identify BBC; “The Game”, “Hints” and “Implementation” establish larger ending, postal help, A-code and text compression. Undated scan issue remains uncertain; no date is taken from the host’s rainbird folder.
- The Quill manual at mocagh.org/miscgame/quill-manual.pdf is **Oric-1/Atmos Serial A, 1985**, not the original Spectrum manual. Its title page was visually inspected: Graeme Yeandle; Oric version by Tim Gilberts. Introduction and table/event/condition sections support the bounded authoring-system discussion. Spectrum origin and onward coverage reuse the existing reviewed Vault entry; no Oric feature is silently dated to 1983 Spectrum.
- CRASH 15 remains the mixed reader-chart example. It is not sales evidence or proof that each listed game descends directly from Adventure.

### Illustration and spoiler boundaries

Three original explanatory subjects now have wide and stacked phone variants: entrance state, a generic richer-parser flow, and a marker making a self-loop recognisable. Each has a title, text alternative and caption; none is a capture, borrowed illustration, actual cave map or game-code reproduction. The study’s optional worked-puzzle disclosures cover selected early/middle encounters. The ending’s structure is described from source without its winning input sequence. No complete cave map, full transcript or solution is published.

The longer study is not presented as a completed human review. Remaining independent work includes human reading/play, original-hardware/configuration validation, a complete endgame play session, exact Level 9 issue identification and proportionate native terminal captures. These limits do not defer the explanations that can already be supported by the selected execution and source.

The expanded authoring section also uses Scott Adams, “Pirate’s Adventure”, BYTE 5.12 (December 1980), printed p. 192 introduction and Program Notes, with continuation/listings through p. 212. The printed opening page was visually checked against the issue scan. It establishes his attributed experience of the 350-point Adventure, choosing original games, interpreter/data reuse, the 16K Level II BASIC TRS-80 product and Alexis Adams’s scenario ideas. This is a creator account, not an independent verification of every remembered time or a chronology of all editions. Incidental family anecdotes, program listings and the game’s full solution are not reproduced. BYTE is already covered by magazines/byte; Scott Adams/Adventure International remain VC-0717. Alexis’s contribution can be covered within that existing combined scope without a duplicate candidate.

Contemporary reception now includes Bob Liddil’s “Microsoft Adventure”, BYTE 5.12 (December 1980), printed pp. 264/266. The first printed review page was visually inspected: TRS-80, 32K and one drive; $29.95; presentation/shorthand/prose discussion; editorial Crowther/Woods credit note signed GW. Page 266 supplies packaging/documentation and save comments. The reviewer’s disk-text explanation is attributed, not asserted as our independent implementation test. Keep this edition distinct from the June 1981 IBM manual. One review is not a sales or universal-reception claim.
