# M.U.L.E. — evidence, interpretation and limits

19 October 2026. Original Atari design and documented C64 control differences are distinguished from later products. Atari setup and the later C64 computer demonstration have separate evidence records. The C64 pass verifies first-round development, production and an auction transaction; full-match and human multiplayer experience remain unverified.

## Rules and original documents

Read the original Electronic Arts player's guide, copyright 1983, preserved as twenty-page scan; also cross-read the later Ariolasoft Atari UK manual (copyright 1985, distinct XL/XE notes) and original C64 command summary. The study follows development, food/time, energy/production, terrain, resource roles, unit-at-a-time auctions, Beginner protections, Standard land/robot supply and Tournament crystite/collusion. Main analysis and numerical bargaining examples are ours, not extracted matches or a validated economic simulation.

- Beginner prevents selling below the critical level. The “sell tomorrow's turn” scenario explicitly applies beyond those protections; do not teach it as possible in every mode.
- Original manual printed p.10: store begins with 16 M.U.L.E.s; new robots require two smithore and a turn. This is not an immediate recipe usable by a settler. Printed p.11 distinguishes unbounded player asks from screen scaling; do not equate vertical position with a universal fixed currency scale.
- C64 reference card: up to two people can use keyboard pairs in shared action, development uses an available joystick; collusion requires synchronised input. Its printed credits use Allen Watson, whereas participant interviews use Alan. Keep source spelling visible without inventing two people.
- Food/energy spoilage in the reference card is part of carry-forward accounting; don't apply it to gross production in an invented example. No precise spoilage calculation is presented as a measured match.
- Net worth includes money, land and goods, not just cash. The colony result and individual standings are not interchangeable scores.
- Character handicap and low-wealth tie advantages are documented choices. They are not evidence that every match is close, that a real economy works this way or that any participant has a particular political belief.

Anderson's Creative Computing December 1983 review read in full, including modes, cooperative/competitive play, review response and the complaint about removing Atari joystick ports. Antic January 1985 interview read; use contemporary names in document titles and her later name/pronouns in our prose. C64 computer opponents and input arrangement are not assumed identical to original Atari behaviour.

Original package PDF rendered and inspected, including front, comic machine backstory, maker photo/liner notes and printed credits on scanned panel 5: package art Lou Beach, photography Allen Say, package design Dennis McVey, liner notes Jeffrey Goodby, producer Joe Ybarra. Package's staged family players, jokes and fictional robot backstory are not real participants or institutional history. `source-identities.json` records document hashes; no full scans distributed.

## People, sources and heritage

Read Hague/Bunten's 1997 interview through the identified 2015 transcription mirror. The original dadgum link did not resolve. Treat it as later participant testimony: earlier auction design, Heinlein inspiration, collaborators, reported sales and cancelled work. No verbatim personal-family or medical disclosure is imported merely because it is available. Avoid exclusive priority claims and contemporary-day statements about rights based on a 1990s interview.

Read Schiller's 2023 combined team interviews, the separate family and remake-developer interviews, and Dieffenbach's 2024 edited Glover account. These are original participant interviews hosted by a community site, not database entries and not independent witnesses to one another's recollections. Limit the team recollection use to testing/production/port work; original credits supply the baseline roles. Preserve uncertainty about individual ideas and completion dates rather than choose the neatest anecdote.

Glover's own account supports the earlier sequencer tune, four voices, disco bass and regret about a missing C64 counterpoint. No score or audio reproduced. Specific song resemblance is not proof of influence. His later recollection of missing initial credits does not override the extant C64 card's explicit music credit.

The Strong finding aid was read through its public PDF text access; a direct download returned 403. It establishes the collection description and some access restrictions, not that we inspected the underlying design sheets. No restricted records or images used. Bunten's sales figure is attributed to her interview, not treated as an audited platform sales ledger.

Later-product overview cross-read with family testimony and the relevant creator/publisher pages. Publisher's current board-game listing identifies Heikki Harju and the tabletop game; full primary rules download was not retrieved cleanly, so no precise tabletop procedure, player-count comparison, completeness claim or current price is used. The point about administering a model at a table is our design question. M.U.L.E. Online's Atari/C64 combination is Dieffenbach's statement of his approach, not a verification of all his code.

## Execution and capture limits

Fresh Emu198x native headless runner, unchanged source revision 6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c, release build without UI; explicit 16 KiB Atari OS revision 2, BASIC disabled, NTSC 800XL. Held US-labelled 1983 ATR identity/hashes recorded in captures/manifest.json. Label alone does not authenticate untouched retail media.

The final interactive attempt selected one human Beginner game, chose a colour/species, and reached a roster of three computer Mechtrons and one human Gollumer. The included image is the Gollumer setup screen. A later attempt stalls/loses display after the transition towards the colony; zero-human demonstration likewise failed later in startup. Whether media, compatibility or emulation accounts for that is not established. This does not prove the historical game has that fault. Stop this capture route rather than alter the game or emulator to create apparently working evidence.

The earlier native C64 PRG startup failure was traced to the direct importer omitting the KERNAL load-end pointer required by the unpacker. The correction is merged in emu198x/emu198x#1839; the Atari display transition remains separately tracked in #1838. The initial failed C64 probe is not evidence of a general keyboard defect.

### C64 follow-up, 19 October

Rebuilt the merged source `b5f8fe59cea181e4232c0caf9b5917994f8c5414` as a native headless release runner without changing emulator or game code. Genuine C64 firmware, PRG and companion D64 identities are recorded in `captures/c64-manifest.json`. Direct PRG import now reaches the title; the game still needs its companion disk for the later load. Without a mounted disk it reports a loading error. Adding the matching held disk and allowing the loading interval reaches the colony. This is a configuration observation, not proof of untouched retail image authenticity.

The zero-human Beginner computer demonstration accepts F5 player-count changes and F7 start. Initial rapid presses before the menu had settled missed selections; the retained successful schedule begins from an inspected menu and allows 90 released frames between presses. The game’s own command summary documents the zero-human demonstration and joystick fire for accelerating computer turns. All button presses in the retained schedule are released.

The first development round, an acid-rain event, first production, smithore status, buyer/seller declaration and a live auction are visible. Two computer sellers initially ask 80. Later both ask 50; one recorded exchange raises the purple seller’s cash from 927 to 977 and shows one unit traded. These observations support the paired auction frames. They do not validate every economy rule, the whole match or human negotiation. The store’s market role is also described in the original manual.

Four full native 416×288 PNG frames are copied without cropping, scaling, interpolation or retouching. The article labels them as C64 computer-demonstration captures and retains the Atari species-selection image. No borrowed gameplay imagery is included.

`observations.json` preserves both the original Atari setup schedule and the successful C64 continuation schedules, with private paths removed. State filenames describe local checkpoints; the save states themselves, commercial program and disk bytes, firmware and full recordings are not distributed. Original diagrams still explain invented layouts and prices rather than pretending to be captured transactions.

## Images, voice and publication

The package front is the study's only published-artwork reproduction, proportionally reduced to 308×313 (96,404 pixels). It accompanies direct package/marketing criticism. Source/artist/credit/transform/hash and rights basis recorded in advertising/manifest.json. Archive hosting is not an open licence; prose licensing does not replace artwork rights. No additional package portrait, manual-page crop or advert is included. Other portrait/design-note leads stay in the shared imagery shortlist.

Original generated header depicts an imagined colony, not historical concept art. Original SVGs have phone compositions. The website reuses approved editorial components and noindex/unreviewed state, not a new layout or promised curriculum game. Whole-game breadth remains an editorial approach, not a claim that every port or sequel was played. Owner historical, voice and publication review remain open.
