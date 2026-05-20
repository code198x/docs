# Lesson References Catalogue

A live inventory of vault entries, pattern library entries, and external references linked from curriculum lessons. Updated as units are written. See [revamp.md](revamp.md) for the cross-referencing discipline that drives this catalogue.

## Why this exists

Two jobs:

1. **Drives vault completeness.** When a Shadowkeep unit links to `/vault/games/atic-atac`, that page must exist (or be on the to-write list). The catalogue surfaces the gap.
2. **Surfaces reuse.** When five units link to `attribute-clash`, that entry deserves real care.

The catalogue is the operational link between lesson work and vault/pattern work.

## How to use

When writing a unit, log every vault / pattern / cross-curriculum reference here under the appropriate section. Mark `[x]` if the target exists and is at quality bar; `[~]` if it exists but needs review; `[ ]` if it doesn't exist yet.

When sweeping the vault for completeness, work the unchecked entries.

## Format

```
- [status] target-path — Linked from: <list of units>. Notes.
```

Status:
- `[x]` exists, at quality bar
- `[~]` exists, needs review or expansion
- `[ ]` doesn't exist yet — must be written

---

## Spectrum — Vault references

Status as of 2026-05-15 (post Shadowkeep U1-U6 ship + retrofit pass + vault sweep).

**Vault sweep completed 2026-05-15** — 18 Spectrum entries reviewed and brought to October-launch bar (~14,000 words of new/rewritten content). See list at bottom of this file.

### Games

- `[~]` `/vault/games/atic-atac` — Linked from: **Shadowkeep U4, U5**. Cited as Shadowkeep's primary inspiration and pace reference. AI-generated, ~390 words, marked `reviewed: false` — needs editorial pass.
- `[~]` `/vault/games/sabre-wulf` — Linked from: **Shadowkeep U4**. Cited alongside Atic Atac for movement pacing. AI-generated, ~363 words, needs review.
- `[~]` `/vault/games/knight-lore` — Not yet linked from Shadowkeep U1–6 (likely Phase 2 Arc 2+ when scale grows). Exists, needs review.
- `[~]` `/vault/games/manic-miner` — Not linked from U1–6 yet; will be from Unit 7 (beeper title theme). Exists, needs review.
- `[~]` `/vault/games/jet-set-willy` — Not linked yet; potential reference in Unit 7 or later. Exists, needs review.

### Systems and Hardware

- `[~]` `/vault/systems/zx-spectrum` — Linked from: **Shadowkeep U1**. Foundational entry. AI-generated, ~255 words, `reviewed: false`. **High-priority for review pass.**
- `[x]` `/vault/hardware/z80` — Linked from: **Shadowkeep U1**. CPU reference. **Reviewed 2026-05-15 round 3.**
- `[x]` `/vault/hardware/ula` — Linked from: **Shadowkeep U4**. **Reviewed 2026-05-15 round 3.**
- `[ ]` `/vault/hardware/zx-spectrum-next` — Mentioned in U1, U2, U3, U4 ("Spectrum Next") but not currently linked. Decide whether to create or just leave as plain mention.
- `[ ]` `/vault/hardware/spectrum-keyboard` — Mentioned in U4 (keyboard scan via port `$FE`) but currently links to `/vault/hardware/ula` instead. Decide whether this rates its own entry.

### Techniques

- `[x]` `/vault/techniques/udg` — Linked from: **Shadowkeep U3**. **Created 2026-05-15 in this retrofit pass.**
- `[x]` `/vault/techniques/beeper-music` — Linked from: **Shadowkeep U1, U6**; will be central to U7. **Created 2026-05-15 in this retrofit pass.**
- `[x]` `/vault/techniques/sinclair-basic` — Linked from: **Shadowkeep U3** (UDG context). **Reviewed 2026-05-15 round 4.**
- `[~]` `/vault/techniques/attribute-aware-design` — Not currently linked from U1–6 (Shadowkeep IS attribute-aware design, but the MDX doesn't link). Consider retroactive link from U5 (where collision-by-attribute is the central thesis).
- `[x]` `/vault/techniques/zx-spectrum-hardware-ports` — Likely candidate for U4 (port `$FE` deep dive) or U7 (port `$FE` bit 4 for beeper). **Reviewed 2026-05-15 round 4.**
- `[x]` `/vault/techniques/zx-spectrum-rom-disassembly` — Reference for ROM routines + sysvars (incl. corrected FRAMES at $5C78). **Reviewed 2026-05-15 round 5.**

### People

- `[~]` `/vault/people/clive-sinclair` — Not linked from U1–6 prose. Exists; foundational. Could be backlinked from system entry.
- `[~]` `/vault/people/matthew-smith` — Will be linked from Unit 7 (Manic Miner beeper precedent). Exists, needs review.
- `[x]` `/vault/people/stamper-brothers` — Lineage from Atic Atac/Sabre Wulf/Knight Lore. **Reviewed 2026-05-15 round 2.**
- `[x]` `/vault/people/tim-follin` — Beeper-music exemplar; will be linked from Unit 7. **Reviewed 2026-05-15 round 2.**
- `[x]` `/vault/people/raffaele-cecco` — Cybernoid/Stormlord author; Follin's collaborator. **Reviewed 2026-05-15 round 3.**
- `[x]` `/vault/people/andrew-braybrook` — Paradroid/Uridium author; *Zzap!64* diaries. **Reviewed 2026-05-15 round 3.**
- `[x]` `/vault/people/steve-turner` — Quazatron / Avalon; Hewson Spectrum auteur. **Created 2026-05-15 round 6.**
- `[x]` `/vault/people/oliver-twins` — Dizzy / Codemasters; bedroom-coder canon. **Reviewed 2026-05-15 round 7.**
- `[x]` `/vault/people/oliver-frey` — *CRASH* / *Zzap!64* cover artist; defined the era's visual identity. **Reviewed 2026-05-15 round 7.**
- `[x]` `/vault/people/jeff-minter` — Llamasoft; 40+ years of continuous solo authorship. **Reviewed 2026-05-15 round 9.**
- `[x]` `/vault/people/david-braben` — Co-creator of *Elite*; Frontier; Raspberry Pi. **Reviewed 2026-05-15 round 10.**
- `[x]` `/vault/people/ian-bell` — Co-creator of *Elite*; the quieter half. **Reviewed 2026-05-15 round 10.** (Fixed botched born/died frontmatter.)

### Companies

- `[~]` `/vault/companies/ultimate` — Not linked from U1–6 prose. Exists. Will be referenced from Atic Atac/Sabre Wulf entries.
- `[~]` `/vault/companies/sinclair-research` — Exists; backlinked from system entry.
- `[~]` `/vault/companies/hewson-consultants` — Not linked from U1–6; brief mentions Hewson tier. Exists.
- `[x]` `/vault/companies/gremlin-graphics` — Sheffield mid-tier publisher; Monty Mole, Lotus, Actua. **Reviewed 2026-05-15 round 8.**
- `[x]` `/vault/companies/newsfield` — *CRASH*/*Zzap!*/*Amtix!* publisher. **Reviewed 2026-05-15 round 8.**
- `[x]` `/vault/companies/psygnosis` — Liverpool 16-bit; Lemmings, Shadow of the Beast, WipEout. **Reviewed 2026-05-15 round 8.**
- `[x]` `/vault/companies/us-gold` — Birmingham; American + arcade conversions; Tiertex. **Reviewed 2026-05-15 round 8.**
- `[x]` `/vault/companies/ocean-software` — The ceiling the bedroom-coder model couldn't reach. **Reviewed 2026-05-15 round 4.**
- `[x]` `/vault/companies/melbourne-house` — Australian publisher; Hobbit / Exploding Fist / **Logan-O'Hara ROM disassembly book**. **Reviewed 2026-05-15 round 6.**
- `[x]` `/vault/companies/mastertronic` — £1.99 budget tier; the floor below the Project's bar. **Reviewed 2026-05-15 round 6.**
- `[x]` `/vault/companies/codemasters` — Darling brothers; the budget-to-AAA trajectory; Dizzy era. **Reviewed 2026-05-15 round 7.**
- `[x]` `/vault/companies/imagine-software` — Liverpool collapse 1984; *Commercial Breaks* documentary; Psygnosis lineage. **Reviewed 2026-05-15 round 7.**

### Magazines

- `[x]` `/vault/magazines/crash-magazine` — Linked from: **Shadowkeep U2** (the "Crash reviewer in 1987" line). Exists, status TBD.
- `[~]` `/vault/magazines/your-sinclair` — Not yet linked from U1–6; mentioned in writing-voice spec. Exists.
- `[x]` `/vault/magazines/sinclair-user` — Third voice anchor (technical/serious). **Reviewed 2026-05-15 round 2.**

### Culture / Phenomena

- `[x]` `/vault/culture/bedroom-coder` — Cultural foundation; referenced from system entry's "See also". **Reviewed 2026-05-15 round 2.**
- `[x]` `/vault/culture/type-in-programs` — The pedagogical model the BASIC track revives. **Reviewed 2026-05-15 round 4.** (Maps to the earlier "magazine-type-ins" placeholder.)
- `[x]` `/vault/culture/cover-tapes` — What replaced type-ins; YS Smash Tape etc. **Reviewed 2026-05-15 round 9.**
- `[x]` `/vault/culture/british-game-development` — Industry-wide context. **Reviewed 2026-05-15 round 9.**
- `[x]` `/vault/culture/liverpool-games-scene` — 1980-2012 cluster lineage. **Reviewed 2026-05-15 round 9.**
- `[x]` `/vault/culture/cambridge-games-scene` — Acorn/Elite/Frontier; technical-ambition tradition. **Reviewed 2026-05-15 round 10.**
- `[x]` `/vault/culture/dundee-games-scene` — DMA/Rockstar North; Abertay games degree. **Reviewed 2026-05-15 round 10.**
- `[x]` `/vault/culture/guildford-games-cluster` — Bullfrog/Lionhead/Hello Games/Media Molecule. **Reviewed 2026-05-15 round 10.**

---

## Spectrum — Pattern library references

(Add as units cite specific patterns)

- `[ ]` `/patterns/spectrum/attribute-checking` — Linked from: Shadowkeep U7 (Wall Collision).
- `[ ]` `/patterns/spectrum/keyboard-matrix-read` — Linked from: Shadowkeep U4.
- `[ ]` `/patterns/spectrum/beeper-tone` — Linked from: Shadowkeep U12, BASIC Bright Spark.
- `[ ]` `/patterns/spectrum/screen-bitmap-write` — Linked from: Shadowkeep U5.
- `[ ]` `/patterns/spectrum/multi-room-data-table` — Linked from: Shadowkeep U8 onwards. **Likely needs writing.**

---

## Cross-curriculum references

(Internal links between curriculum units — kept here too for sanity, especially when a unit references another in a different track)

- (To populate as content is written)

---

## Vault audit 2026-05-19 — gaps surfaced by Spectrum Assembly v0.3 / BASIC v6.4

After the Spectrum Assembly track structure decision (44 entries, 6 volumes) and the v6.4 BASIC rename pass, the curriculum now references substantially more canonical Spectrum games, people, and companies than before. Shadowkeep's per-unit refinements (read-alongside + modern-equivalent lines added 2026-05-19) cite specific canonical moments per unit, which need vault entries to resolve.

**Surveyed 2026-05-19** — current vault state checked against curriculum references. Gaps listed below by category, prioritised by curriculum visibility.

### Tier 1 — Referenced in Shadowkeep per-unit read-alongside or modern-equivalent lines

These appear in concrete prose that learners will read. Must exist at vault bar by October.

**Games — missing:**
- `[ ]` `/vault/games/hyper-light-drifter` — modern equivalent for U5 (silhouette), U7 (pixel movement), U11 (lighting), U20 (palette mood), U30 (audio mix). High frequency.
- `[ ]` `/vault/games/stardew-valley` — modern equivalent for U2 (tilesets), U9 (Y-sort).
- `[ ]` `/vault/games/deaths-door` — modern equivalent for U9 (Y-sort), U11 (lighting), U20 (palette).
- `[ ]` `/vault/games/cybernoid-ii` — referenced in U7 (pixel movement), U17 (audio layering), U30 (full audio). The existing `cybernoid.mdx` may cover this — check if Cybernoid II is its own entry needed.
- `[ ]` `/vault/games/disasterpeace-hyper-light-drifter-soundtrack` — modern equivalent for U15 (composed theme). Or roll into person-entry `disasterpeace`.

**People — missing:**
- `[ ]` `/vault/people/disasterpeace` — modern equivalent cited at U15.
- `[~]` `/vault/people/matthew-smith` — already in vault, marked needs-review per existing entry status.
- `[~]` `/vault/people/tim-follin` — already in vault, marked reviewed; status [x] above.

### Tier 2 — Referenced by Assembly track lineup traditions (Volume 1-4 games' "Tradition" columns)

Each game in the v0.3 lineup names a canonical legend and tradition. Vault must support those citations when per-game specs are written.

**Games — missing (~25):**

V1 (Rooms and Worlds):
- `[ ]` `/vault/games/saboteur-ii` — Greycoat tradition (slot 33)
- `[ ]` `/vault/games/sherlock` — The Drawn World tradition (slot 34)
- `[ ]` `/vault/games/lord-of-the-rings-spectrum` — The Drawn World tradition (slot 34)
- `[ ]` `/vault/games/pentagram` — Underlight tradition (slot 3 inspiration)
- `[ ]` `/vault/games/lords-of-midnight` — Whitewinter tradition (slot 4)
- `[ ]` `/vault/games/doomdarks-revenge` — Whitewinter tradition
- `[ ]` `/vault/games/starquake` — Underlight tradition
- `[ ]` `/vault/games/firelord` — Underlight + Embergate tradition
- `[ ]` `/vault/games/avalon` — Underlight tradition

V2 (Verticality and Gravity):
- `[ ]` `/vault/games/cauldron-ii` — The Witch's Year tradition (slot 16)
- `[ ]` `/vault/games/trapdoor` — The Goblin's Larder tradition (slot 12)
- `[ ]` `/vault/games/bombjack` — Towerfast tradition (slot 13)
- `[ ]` `/vault/games/underwurlde` — Brindlewood tradition (slot 14)

V3 (Motion and Threat):
- `[ ]` `/vault/games/zynaps` — Ironstreak tradition (slot 18)
- `[ ]` `/vault/games/light-force` — Skylash tradition (slot 19)
- `[ ]` `/vault/games/sanxion` — Skylash tradition

V4 (The Real World and the Third Dimension):
- `[ ]` `/vault/games/tornado-low-level` — Storm Bird tradition (slot 27)
- `[ ]` `/vault/games/daley-thompsons-decathlon` — Ten Trials tradition (slot 25)
- `[ ]` `/vault/games/match-day` — Cup Saturday tradition (slot 26)
- `[ ]` `/vault/games/buggy-boy` — Switchback tradition (slot 28)
- `[ ]` `/vault/games/chequered-flag` — Switchback tradition
- `[ ]` `/vault/games/driller` — Coreworks tradition (slot 30)
- `[ ]` `/vault/games/the-sentinel` — Stillwatcher tradition (slot 32)
- `[ ]` `/vault/games/3d-monster-maze` — The Long Passage tradition (slot 31)

V5 (Beyond Games — demoscene):
- `[ ]` `/vault/games/crystal-frog` — referenced for Hairline tradition
- `[ ]` `/vault/games/esi-megademo` — referenced for The Long Night tradition

V6 (Next-native — modern scene): no specific canonical games; references the modern Spectrum scene generally.

**People — missing (~9):**
- `[ ]` `/vault/people/clive-townsend` — Saboteur / Saboteur II / Durell auteur
- `[ ]` `/vault/people/mike-singleton` — Lords of Midnight / Doomdark's Revenge
- `[ ]` `/vault/people/don-priestley` — Trapdoor / Flunky / large-character-sprite style
- `[ ]` `/vault/people/malcolm-evans` — 3D Monster Maze
- `[ ]` `/vault/people/bo-jangeborg` — Fairlight (iso adventure)
- `[ ]` `/vault/people/mel-croucher` — Automata / Pi-Man / Deus Ex Machina (experimental)
- `[ ]` `/vault/people/sandy-white` — Ant Attack (early iso)
- `[ ]` `/vault/people/steve-crow` — Cybernoid / Wizard's Lair / Bubble Bus tradition
- `[ ]` `/vault/people/einar-saukas` — Modern Spectrum scene (8x1 multicolour, modern demoscene techniques)

**Companies — missing (~10):**
- `[ ]` `/vault/companies/mikro-gen` — Pyjamarama, Wally Week games
- `[ ]` `/vault/companies/palace-software` — Cauldron / Cauldron II
- `[ ]` `/vault/companies/durell-software` — Saboteur / Saboteur II / Combat Lynx
- `[ ]` `/vault/companies/digital-integration` — Tornado Low Level / Fighter Pilot
- `[ ]` `/vault/companies/incentive-software` — Freescape (Driller, Castle Master, Total Eclipse)
- `[ ]` `/vault/companies/lothlorien` — Wargames (Yankee, Arnhem, Roundheads)
- `[ ]` `/vault/companies/mirrorsoft` — Tetris Spectrum publisher
- `[ ]` `/vault/companies/cds-software` — Steve Davis Snooker, Colossus Chess
- `[ ]` `/vault/companies/bubble-bus-software` — Wizard's Lair, Starquake
- `[ ]` `/vault/companies/tehkan` — Bombjack, Pengo (arcade lineage)

### Tier 3 — Cross-curriculum (BASIC track v6.4 references)

BASIC v6.4 game names (Oracle Stone, Cipher, Locksmith, etc.) are inspired-by; they reference canonical antecedents (Magic 8-Ball toy, Hangman game tradition, Mastermind / Invicta, Battleship / Milton Bradley, Pong / Atari, Pac-Man / Namco, etc.). When per-game vault threads are written for the BASIC games, they cite these antecedents — most of which are likely already in the vault as `pac-man.mdx`, `pong.mdx`, etc. (confirmed for: asteroids, frogger, pac-man, pong, tetris). The toy antecedents (Magic 8-Ball, Hangman board game, Battleship, Mastermind) may need new entries — check pending.

### Recommended priorities

1. **Tier 1 first** (modern equivalents in Shadowkeep — 5 entries). High visibility through Shadowkeep MDX prose. October-relevant.
2. **Tier 2 V1-V2 games + people** (Shadowkeep's lineup neighbours). Most-cited canonical lineage. ~15 entries.
3. **Tier 2 V3-V4 + companies**. Lower-frequency but still required for per-game spec work. ~25 entries.
4. **V5 demoscene + V6 Next**. Specialised; can wait until those volumes enter build scope. ~5-7 entries.

**Total gap: ~50 vault entries** to bring the curriculum's citations to fully-resolved status. None block the October ship of Volume 1 BASIC or Shadowkeep Arcs 1-2 directly — Shadowkeep's per-unit references are mostly to already-existing vault entries (Atic Atac, Knight Lore, Sabre Wulf, Manic Miner, JSW, Cybernoid, Hobbit) — but the read-alongside / modern-equivalent entries do reference Hyper Light Drifter, Stardew Valley, Death's Door, Disasterpeace, none of which exist yet.

### Slug corrections noted

- Ultimate Play the Game lives at `companies/ultimate.mdx` (not `companies/ultimate-play-the-game.mdx`).
- Cybernoid II references may go to `games/cybernoid.mdx` — confirm whether sequel deserves its own entry given its distinct AY soundtrack and Tim Follin contribution.

---

## C64 — Vault references

(Populated when Cadence work resumes post-October)

---

## NES — Vault references

(Populated when Nightshade work begins post-October)

---

## Amiga — Vault references

(Populated when Exodus work resumes post-October)

---

## Maintenance notes

- **Triggered update:** any new lesson MDX written with a `/vault/` or `/patterns/` link must update this file in the same commit.
- **Sweep update:** during the Pass 3b-style vault review for October, every `[ ]` entry here is a target.
- **Quality bumps:** an entry with five-plus citations should be reviewed for promotion to flagship-tier care.

---

## 2026-05-15 vault sweep — entries reviewed

All marked `reviewed: true`, in the 400-1100 word range, with magazine-class voice.

### Round 1 — flagship entries
| Entry | Words | Notes |
|---|---|---|
| `systems/zx-spectrum` | 1060 | Foundational; linked from every Spectrum unit. |
| `games/atic-atac` | 788 | Shadowkeep's direct ancestor; linked from Shadowkeep U4, U5. |
| `games/sabre-wulf` | 720 | Linked from Shadowkeep U4. |
| `games/knight-lore` | 903 | The Filmation engine breakthrough. |
| `games/manic-miner` | 957 | Beeper-music precedent for Unit 7. |
| `games/jet-set-willy` | 859 | The POKE-patched mansion. |
| `people/matthew-smith` | 728 | Manic Miner / Jet Set Willy author. |
| `people/clive-sinclair` | 553 | Fact corrections (Sinclair Research date, sale price). |
| `companies/ultimate` | 947 | Stamper brothers' studio. |
| `techniques/udg` | 718 | **Created** — for Shadowkeep U3 link. |
| `techniques/beeper-music` | 815 | **Created** — for Unit 7 prelude. |
| `techniques/attribute-aware-design` | 1006 | Five strategies for the two-colour cell. |
| `magazines/crash-magazine` | 799 | The Project's voice anchor. |

### Round 1b — wider sweep
| Entry | Words | Notes |
|---|---|---|
| `companies/sinclair-research` | 699 | The Cambridge computer company. |
| `companies/software-projects` | 594 | **Created** — Matthew Smith's company. |
| `companies/bug-byte` | 413 | **Created** — Manic Miner's original publisher. |
| `companies/hewson-consultants` | 720 | The mid-tier full-price quality reference. |
| `magazines/your-sinclair` | 710 | The Project's voice anchor (humour register). |

### Round 2 — people, magazines, culture
| Entry | Words | Notes |
|---|---|---|
| `people/stamper-brothers` | 1000 | Ultimate → Rare lineage; 1982-2007. |
| `people/tim-follin` | 900 | Beeper composer; Unit 7 bar-setter. |
| `magazines/sinclair-user` | 700 | Third voice anchor (technical register). |
| `culture/bedroom-coder` | 1100 | The cultural figure the Project revives. |

### Round 3 — hardware and Hewson auteurs
| Entry | Words | Notes |
|---|---|---|
| `hardware/z80` | 950 | CPU foundation; linked from U1. |
| `hardware/ula` | 1100 | The chip that defines the Spectrum; linked from U4. |
| `people/raffaele-cecco` | 850 | Cybernoid/Stormlord; Unit 7 visual+audio reference. |
| `people/andrew-braybrook` | 900 | Paradroid/Uridium; *Zzap!64* diary tradition. |

### Round 4 — techniques, culture, Ocean
| Entry | Words | Notes |
|---|---|---|
| `techniques/zx-spectrum-hardware-ports` | (polish on solid existing reference) | U4 + U7 anchor. |
| `techniques/sinclair-basic` | 1000 | The BASIC-track language reference. |
| `culture/type-in-programs` | 1300 | The pedagogical model the BASIC track revives. |
| `companies/ocean-software` | 1100 | The ceiling the bedroom-coder model couldn't reach. |

### Round 5 — pedagogy, culture, ROM
| Entry | Words | Notes |
|---|---|---|
| `culture/usborne-computing-books` | 1200 | The "Usborne bar" reference for BASIC track. |
| `culture/machine-code-for-beginners` | 1200 | The BASIC→assembly tradition. |
| `culture/poke-culture` | 1200 | Memory-as-inspectable; Spectrum cultural pillar. |
| `techniques/zx-spectrum-rom-disassembly` | (polish + FRAMES sysvar fix) | Sysvars at $5C00-$5CB5; FRAMES at $5C78. |

### Round 6 — hardware, publishers, the Hewson trio
| Entry | Words | Notes |
|---|---|---|
| `hardware/multiface` | (polish on existing) | The NMI freezer behind POKE culture. |
| `companies/melbourne-house` | 1300 | Australian publisher; Hobbit/Fist + Logan-O'Hara book. |
| `companies/mastertronic` | 1400 | £1.99 budget tier; the floor the Project sits above. |
| `people/steve-turner` | 1000 | **Created** — Quazatron/Avalon; completes Hewson trio. |

### Round 7 — Dizzy era and the Liverpool collapse
| Entry | Words | Notes |
|---|---|---|
| `people/oliver-twins` | 1300 | Dizzy authors; the canonical bedroom-coder trajectory. |
| `people/oliver-frey` | 1500 | The CRASH/Zzap! cover artist; defined the era's visual identity. |
| `companies/codemasters` | 1500 | Darling brothers; £1.99 → £1.2bn EA acquisition (2021). |
| `companies/imagine-software` | 1500 | Liverpool collapse 1984; *Commercial Breaks* BBC documentary. |

### Round 8 — the British publishing landscape
| Entry | Words | Notes |
|---|---|---|
| `companies/newsfield` | 1500 | Roger Kean's Ludlow publisher; *CRASH*/*Zzap!*/*Amtix!*. |
| `companies/psygnosis` | 1700 | Liverpool 16-bit; Roger Dean, Lemmings, WipEout. |
| `companies/gremlin-graphics` | 1500 | Sheffield mid-tier; Monty Mole, Lotus trilogy. |
| `companies/us-gold` | 1500 | Birmingham; American + arcade conversions; Tiertex. |

### Round 9 — culture mop-up and Jeff Minter
| Entry | Words | Notes |
|---|---|---|
| `culture/cover-tapes` | 1600 | Late-80s magazine cassettes; killed the type-in tradition. |
| `culture/british-game-development` | 1700 | The five preconditions; regional clusters; transitions. |
| `culture/liverpool-games-scene` | 1500 | Thirty-year continuous-personnel lineage 1980-2012. |
| `people/jeff-minter` | 1700 | Llamasoft; 40+ years of continuous solo authorship. |

### Round 10 — Elite, and the remaining regional scenes
| Entry | Words | Notes |
|---|---|---|
| `people/david-braben` | 2200 | Co-creator of Elite; Frontier; Raspberry Pi co-founder. |
| `people/ian-bell` | 1500 | Co-creator of Elite; the quieter half. Frontmatter fix. |
| `culture/cambridge-games-scene` | 1700 | Acorn/Elite/Frontier; technical-ambition tradition. |
| `culture/dundee-games-scene` | 1900 | DMA Design → Rockstar North; Abertay's 1997 games degree. |
| `culture/guildford-games-cluster` | 2000 | Bullfrog/Lionhead/Hello Games/Media Molecule lineage. |
