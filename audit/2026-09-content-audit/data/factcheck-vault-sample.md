# Vault fact-check sample

**Date:** 2026-09-23. **Scope:** read-only spot-check of 30 of the 1,478 Vault entries (`Code198x/website/src/content/vault/`). Every Vault entry carries `ai_generated: true, reviewed: false`, so this sample estimates the error rate of unreviewed machine-written prose.

**Bottom line:** 40 of 250 checked claims (16%) are WRONG against a source, and 22 of the 30 entries contain at least one WRONG claim. Fewer than half of all claims (48%) are anything other than cleanly VERIFIED. Errors concentrate in short biographical "fast facts" and in frontmatter dates. Long sections that quote period magazines hold up well (see *Patterns*).

## Method

**Sample.** There are 30 entries in two halves.

- **UK / Spectrum-weighted (15, chosen by hand):**
  - `companies/sinclair-research`
  - `people/clive-sinclair`
  - `people/steven-vickers`
  - `systems/zx-spectrum`
  - `hardware/ula`
  - `systems/zx81`
  - `magazines/crash-magazine`
  - `people/oliver-frey`
  - `companies/ultimate`
  - `companies/rare`
  - `people/stamper-brothers`
  - `games/knight-lore`
  - `people/matthew-smith`
  - `games/manic-miner`
  - `games/jet-set-willy`

  No Richard Altwasser entry exists, so he could not be sampled.
- **Random (15):** drawn with Python `random.seed(1982); random.sample(pool, 15)`. The pool was all 1,478 `*/*.mdx` slugs, sorted, minus the UK 15. The draw returned:
  - `companies/mastertronic`
  - `companies/acornsoft`
  - `people/ian-logan`
  - `techniques/scrolling`
  - `games/dungeon-master`
  - `companies/epyx`
  - `people/roberta-williams`
  - `magazines/acorn-user`
  - `genres/western-rpg`
  - `games/hypersports`
  - `people/bob-yannes`
  - `people/ed-boon`
  - `games/supreme-commander`
  - `games/wizball`
  - `games/dig-dug`

  The seed happened to draw several UK or Acorn subjects too.

**Checks.** For each entry I checked:

- every frontmatter date field;
- between 4 and 15 substantive prose claims, weighted towards dates, prices, attributions, superlatives, quotes, anecdotes and living/dead status;
- the entry's own cited sources, where it had any.

Primary sources came first:

- **Period magazines** first: *CRASH*, *Sinclair User*, *Your Sinclair*, *Computer and Video Games*, *Personal Computer Games*, *ACE*, *Acorn User*, *Zzap!64* and others. These were searched by keyword and quoted from the issue itself.
- **Books and manuals** second, such as Chris Smith's *The ZX Spectrum ULA* and Don Thomasson's *The Ins and Outs of the TS1000 & ZX81*.
- **The web**, only where no print source turned up. These rows are marked "(web)". Wikipedia was a last resort and is flagged wherever it appears.

**Who did the checking.** Four parallel sub-agents did the checking. I compiled their results and re-checked a handful by hand: the CRASH issue 1 price, the ZX81 kit price, the ULA port wording, the ZX81 and Clive Sinclair price text, and the CRASH 51 Stamper passage.

**Verdicts.**

| Verdict | Meaning |
|---|---|
| VERIFIED | A source was read and the claim matches it. |
| WRONG | A source was read and it contradicts the claim. |
| UNSUPPORTED | No source was found; the row says where I looked. |
| IMPRECISE | Broadly right, but off in date, number or scope, or overstated. |

**Compilation adjustments.**

- **Stamper birth years (3 rows) downgraded from WRONG to UNSUPPORTED.** A sub-agent marked them WRONG on Wikipedia's dates, Chris 1958 and Tim 1961. But *CRASH* issue 51 (April 1988), p. 36, says "Chris - at 29 the younger, quieter brother". That fits the entry's Tim 1958 / Chris 1959. The two sources conflict, so the claim needs a primary birth record.
- **Hypersports chart row upgraded to WRONG.** A sub-agent marked it "IMPRECISE (one row WRONG)". The May 1986 position is contradicted outright.

**Limits.**

- **Confidence varies by source.** Web-only verdicts, mostly for Ed Boon, Supreme Commander, Epyx and Roberta Williams, are less secure than magazine-backed ones.
- **Some claims were drawn from the prose, not listed.** Claim counts per entry vary because long entries carry more checkable claims.
- **WRONG means contradicted by the cited source.** Several WRONG verdicts rest on a single source, and each row shows which one.

## Summary

| Half | Claims | Verified | Imprecise | Unsupported | Wrong | Wrong rate | Not cleanly verified |
|---|---|---|---|---|---|---|---|
| UK / Spectrum-weighted (15) | 147 | 71 | 24 | 28 | 24 | 16% | 52% |
| Random (15) | 103 | 58 | 21 | 8 | 16 | 16% | 44% |
| All 30 | 250 | 129 | 45 | 36 | 40 | 16% | 48% |

**Entries with at least one WRONG claim:** 22 of 30. That is 11 of the 15 UK entries and 11 of the 15 random entries.

**Entries with none:**

- `companies/sinclair-research`
- `companies/rare`
- `games/manic-miner`
- `games/jet-set-willy`
- `people/roberta-williams`
- `genres/western-rpg`
- `people/ed-boon`
- `games/wizball`

### Per entry

| Entry | Half | Claims | Verified | Imprecise | Unsupported | Wrong | Wrong rate |
|---|---|---|---|---|---|---|---|
| `companies/sinclair-research` | UK | 11 | 10 | 0 | 1 | 0 | 0% |
| `people/clive-sinclair` | UK | 8 | 2 | 3 | 1 | 2 | 25% |
| `people/steven-vickers` | UK | 7 | 2 | 1 | 2 | 2 | 29% |
| `systems/zx-spectrum` | UK | 7 | 2 | 2 | 1 | 2 | 29% |
| `hardware/ula` | UK | 7 | 4 | 1 | 1 | 1 | 14% |
| `systems/zx81` | UK | 7 | 3 | 1 | 2 | 1 | 14% |
| `magazines/crash-magazine` | UK | 9 | 6 | 0 | 1 | 2 | 22% |
| `people/oliver-frey` | UK | 11 | 1 | 1 | 4 | 5 | 45% |
| `companies/ultimate` | UK | 15 | 7 | 6 | 1 | 1 | 7% |
| `companies/rare` | UK | 6 | 5 | 1 | 0 | 0 | 0% |
| `people/stamper-brothers` | UK | 10 | 3 | 2 | 4 | 1 | 10% |
| `games/knight-lore` | UK | 11 | 4 | 1 | 4 | 2 | 18% |
| `people/matthew-smith` | UK | 15 | 2 | 3 | 5 | 5 | 33% |
| `games/manic-miner` | UK | 13 | 12 | 0 | 1 | 0 | 0% |
| `games/jet-set-willy` | UK | 10 | 8 | 2 | 0 | 0 | 0% |
| `companies/mastertronic` | random | 12 | 5 | 3 | 1 | 3 | 25% |
| `companies/acornsoft` | random | 10 | 5 | 2 | 2 | 1 | 10% |
| `people/ian-logan` | random | 8 | 5 | 2 | 0 | 1 | 12% |
| `techniques/scrolling` | random | 7 | 4 | 1 | 0 | 2 | 29% |
| `games/dungeon-master` | random | 6 | 3 | 2 | 0 | 1 | 17% |
| `companies/epyx` | random | 7 | 4 | 0 | 2 | 1 | 14% |
| `people/roberta-williams` | random | 5 | 3 | 2 | 0 | 0 | 0% |
| `magazines/acorn-user` | random | 5 | 3 | 0 | 0 | 2 | 40% |
| `genres/western-rpg` | random | 6 | 2 | 3 | 1 | 0 | 0% |
| `games/hypersports` | random | 6 | 2 | 2 | 0 | 2 | 33% |
| `people/bob-yannes` | random | 5 | 2 | 2 | 0 | 1 | 20% |
| `people/ed-boon` | random | 5 | 5 | 0 | 0 | 0 | 0% |
| `games/supreme-commander` | random | 5 | 4 | 0 | 0 | 1 | 20% |
| `games/wizball` | random | 8 | 6 | 0 | 2 | 0 | 0% |
| `games/dig-dug` | random | 8 | 5 | 2 | 0 | 1 | 12% |

## Patterns

- **Period-magazine sections are reliable; boilerplate fast facts are not.** The long, source-quoting sections checked out almost entirely. That covers `sinclair-research`, `manic-miner`, `jet-set-willy`, the CRASH mechanics in `crash-magazine`, the ULA timing, and the magazine quotes in `mastertronic` and `acornsoft`. The errors cluster instead in short biographical lists, "Fast facts" boxes, frontmatter dates and See-also blurbs. `people/oliver-frey` (5 WRONG) and `people/matthew-smith` (5 WRONG) are the worst entries.
- **Entries contradict each other.** Each pair below disagrees, and one side matches the primary source:
  - **ZX81 price.** `sinclair-research` gives £49.95 kit / £69.95 built, which is right. `zx81` and `clive-sinclair` get it wrong.
  - **Manic Miner release month.** `manic-miner` says August 1983 (right); `matthew-smith` says November.
  - **Alan Maton's role.** `manic-miner` says marketing manager (right); `matthew-smith` says managing director.
  - **Did the Stampers give interviews?** `ultimate` calls "reclusive" overstated. `stamper-brothers` and CRASH 51 say they gave no interviews.
  - **Mastertronic and Virgin.** `mastertronic` contradicts itself: its ACE-based section on a Virgin minority stake is at odds with its own Fast facts.
- **The entries' "This library cannot…" caveats are themselves often false.** Three warning boxes claim no evidence exists when period sources carry it:
  - **Logan's Rosetta Stone award.** SYNTAX, March 1982, reported it independently.
  - **Acorn User's Redwood handover.** Acorn User issue 20 announces it.
  - **Crammond's route into Acornsoft.** Acorn Programs, July 1984, covers it.

  A hedge is not evidence of a search.
- **A garbled scan reading became an invented anecdote.** The Mastertronic entry turns "A^i?nf X" (Agent X) into "Ant Attack 85%". It then builds a Sandy White aside on that misreading.
- **Invented biographical detail:**
  - Frey's training at the Royal College of Art, and his TV21, Look-In and Pirelli credits.
  - Frey's cover descriptions.
  - BASIC features credited to Vickers.
  - Knight Lore's werewolf mechanics.
  - Epyx's "ROXX" hardware and its "Games by gamers, for gamers" slogan.
  - Matthew Smith's "Megatree" and his "2002 Retro Gamer" interview. Retro Gamer began in 2004.
- **Superlatives without sources:**
  - "a first for the platform" (Manic Miner's music).
  - "Ultima established the template".
  - "invented the graphic adventure". The period press does call Mystery House the first graphic adventure, but Ken Williams programmed it.
  - "Britain's first home computer under £100". This is Sinclair's own advertising line.
- **Living/dead status is correct throughout.** Sinclair (d. 16 Sep 2021) and Frey (d. 2022) are both marked dead. Frey's day of death is wrong: 23 August against 21 August.
- **Private paths.**
  - No public prose contains local file-system paths.
  - `systems/zx-spectrum` puts two local working-file paths in its frontmatter sources instead of publication citations. One of them no longer resolves.
  - Whether frontmatter sources render publicly was not checked.
- **Some citations do not say what the entry claims:**
  - **The ZX81 "manual" quotes** actually come from Don Thomasson's Melbourne House book. The entry also gets that book's title wrong.
  - **The Mastertronic Bulldog quote** is cited as CRASH 41 but appears in issue 39.
  - **The Knight Lore motive** is taken from a 1998 *Arcade* paraphrase rather than from the primary source, Tim Stamper in CRASH 51.
  - **The ULA frontmatter** cites a page number (p.268) that does not match the pages in Smith's book (pp.245-246).

## Findings

The table lists WRONG rows first, then UNSUPPORTED, IMPRECISE and VERIFIED. Web sources are marked (web). Print sources are cited by title, issue, date and page. Page numbers count from the front cover of the scanned issue or book (cover = p. 1), so they can differ by a page or two from the printed folio. Abbreviations: C&VG = *Computer and Video Games*; SU = *Sinclair User*; YS = *Your Sinclair*; PCG = *Personal Computer Games*; PCN = *Personal Computer News*; Smith = Chris Smith, *The ZX Spectrum ULA: How to Design a Microcomputer* (ZX Design and Media, 2010); Thomasson = Don Thomasson, *The Ins and Outs of the TS1000 & ZX81* (Melbourne House, 1983).

| Entry | Claim | Verdict | Evidence / locator | Note |
|---|---|---|---|---|
| `vault/people/clive-sinclair.mdx` | Subtitle "The man who put Britain online" | **WRONG** | Nothing in the entry or its sources concerns networking. Sinclair made computers cheap, not online. | The subtitle is anachronistic and misleading. |
| `vault/people/clive-sinclair.mdx` | "ZX81 (1981): even cheaper at £69.95 (kit form)" | **WRONG** | C&VG issue 1, November 1981: £69.95 was the built price (p. 22); the kit was £49.95 (coupon, p. 23) | The Sinclair Research entry has it right. |
| `vault/people/steven-vickers.mdx` | "joined 1980, wrote ZX80, ZX81, and Spectrum ROMs" | **WRONG** | Smith, ch. 7: the Spectrum ROM was "Written by John Grant and Steven Vickers under contract from Nine Tiles". (web) Wikipedia: he joined Nine Tiles in 1980, which had already written the ZX80 BASIC, and he adapted it into the ZX81's 8K ROM | He was a Nine Tiles contractor, not a Sinclair employee, and he did not write the ZX80 ROM. |
| `vault/people/steven-vickers.mdx` | Sinclair BASIC had "no line numbers required in later versions", "User-defined functions and procedures" | **WRONG** | The Spectrum manual (*Sinclair ZX Spectrum BASIC Programming*, Steven Vickers, Sinclair Research, 1982), ch. 9 "Functions", documents DEF FN only. Spectrum BASIC has no procedures and needs line numbers in every version. | These are invented features. |
| `vault/systems/zx-spectrum.mdx` | See also: Clive Sinclair, "designer of the original Spectrum" | **WRONG** | *MC Microcomputer* (Italy) no. 20, June 1983, p. 47: Altwasser was "largely responsible for the hardware development", Vickers the ROM |  |
| `vault/systems/zx-spectrum.mdx` | Frontmatter sources give two local working-file paths (a Spectrum port $FE synthesis and a "Distilled at …" note) instead of publications | **WRONG** | One of the two paths does not resolve to any existing file, and neither is a publication a reader can check | These are private local paths in public frontmatter, and one of them is dead. |
| `vault/hardware/ula.mdx` | Port $FE "(any odd port with A0=0)" | **WRONG** | Smith, ch. 19, p. 216: "any port address that has A0 low ... any even numbered address" | The claim contradicts itself: a port with A0=0 is even. |
| `vault/systems/zx81.mdx` | "£69.95 (kit form) or £99.95 (assembled)" (body and Fast facts) | **WRONG** | C&VG issue 1, November 1981, p. 22 (£69.95 is the ZX81 price), coupon p. 23 (kit £49.95); SU issue 51 (June 1986), p. 47, timeline "1981 ZX81 (£69.95)" | Correct prices: £49.95 kit, £69.95 built. The frontmatter already flags prices as unverified. |
| `vault/magazines/crash-magazine.mdx` | "Cover price: £0.95 at launch" | **WRONG** | *CRASH* issue 1, February 1984, p. 5: "Single copy: 75p" |  |
| `vault/magazines/crash-magazine.mdx` | "Crash Powertape, from issue 72 (January 1990)" | **WRONG** | *CRASH* issue 65, June 1989 ("Mega Power Tape"); Power Tape mentioned in issues 65-71; *CRASH* issue 75 (April 1990), p. 8, refers to "PowerTape (back issue 67)" | The Power Tape started around issue 65 (June 1989). |
| `vault/people/oliver-frey.mdx` | "10 February 1948" (born) | **WRONG** | (web) https://downthetubes.net/in-memoriam-illustrator-and-comic-artist-oliver-frey/ and Wikipedia https://en.wikipedia.org/wiki/Oliver_Frey: born 30 June 1948, Zürich | The year is right. |
| `vault/people/oliver-frey.mdx` | "23 August 2022" (died), "aged 74" | **WRONG** | Same sources: died 21 August 2022, aged 74 | Living/dead status and age are correct; the day is wrong. |
| `vault/people/oliver-frey.mdx` | "Moved to Britain: As a teenager" | **WRONG** | (web) Wikipedia: the family moved to Britain in 1956, when he was about 8 |  |
| `vault/people/oliver-frey.mdx` | "*The Oliver Frey Artbook*, 2017, edited by Roger Kean" | **WRONG** | (web) Wikipedia: *The Fantasy Art of Oliver Frey*, Thalamus Publishing, 2006, by Roger Kean |  |
| `vault/people/oliver-frey.mdx` | "Newsfield collapsed in 1992" | **WRONG** | Europress took over CRASH from issue 94 (Dec 1991), after the missing November 1991 issue (see the crash-magazine entry) | Newsfield collapsed in late 1991. |
| `vault/companies/ultimate.mdx` | "Gunfright (1985)", "Cyberun (1985)" | **WRONG** | *CRASH* issue 24, January 1986, p. 76 (first adverts); Gunfright reviewed in *CRASH* issue 25, February 1986, p. 60; Cyberun rated in CRASH issue 28 (ratings table in *CRASH* issue 51, April 1988, p. 38) | Both are 1986 releases. |
| `vault/people/stamper-brothers.mdx` | "Killer Instinct (1994, SNES)" | **WRONG** | (web) Wikipedia, Rare: arcade debut in 1994, SNES version after that (1995) |  |
| `vault/games/knight-lore.mdx` | "CRASH gave 94% (just shy of a Smash)" | **WRONG** | *CRASH* issue 15, April 1985, p. 12: "Above 90% — a CRASH Smash" | 94% was well inside Smash range. |
| `vault/games/knight-lore.mdx` | "The castle is 49 rooms" / "The 50 rooms" | **WRONG** | PCG issue 15 (February 1985): "128 screens of 3D magic - Britain's greatest Knight Lore map"; "Doing this for all 128 screens…" | The whole "50 rooms" section is wrong. |
| `vault/people/matthew-smith.mdx` | "born in 1966 in Wallasey, Merseyside" | **WRONG** | (web, Wikipedia, last resort): born in Penge, London; the family moved to Wallasey when he was seven. PCG Mar 1984 places him in Liverpool computing | The birthplace is wrong, though he grew up in Wallasey. |
| `vault/people/matthew-smith.mdx` | "signed it to Bug-Byte for release in November" 1983 | **WRONG** | PCN, 17 August 1983: review, Bug-Byte, £5.95; C&VG issue 21 (July 1983), p. 16: "in the shops now" | On sale by August 1983. The Manic Miner entry says this itself. |
| `vault/people/matthew-smith.mdx` | "Alan Maton (Bug-Byte's former managing director)" | **WRONG** | PCG issue 03: "from despatch rider to marketing manager in a matter of months" | Contradicts the Manic Miner entry, which gets this right. |
| `vault/people/matthew-smith.mdx` | Attack of the Mutant Zombie Flesh Eating Chickens From Mars "retitled The Megatree and never released" | **WRONG** | *Retro Gamer* issue 5 (2004), p. 47: Steve Foster says it "eventually became Star Paws" | The Megatree was a separate project. |
| `vault/people/matthew-smith.mdx` | "In 2002… interviewed by Retro Gamer, working briefly at a Yorkshire software house" | **WRONG** | *Retro Gamer* issue 1 appeared in 2004. (web) Wikipedia: joined Runecraft, Dewsbury, in 1999 | Retro Gamer did not exist in 2002. The Yorkshire employer fits, but the year is 1999. |
| `vault/companies/mastertronic.mdx` | CRASH 48 index: Mastertronic catalogue runs "from Ant Attack at 85% down to 1985 at 21%" | **WRONG** | *CRASH* issue 48 (January 1988) games index, pp. 95-101: Mastertronic entries include **Knight Tyme 94%** (29/18), **Mister Magic 86%** (31/72), Kobyashi Naru 83%, Universal Hero 83%. 1985 21% (25/20) is correct | The top of the range is 94%, not 85%, so the "85 down to 21" framing is wrong. |
| `vault/companies/mastertronic.mdx` | "Ant Attack 85% issue 37… Sandy White's game, acquired rather than commissioned" | **WRONG** | The index line in *CRASH* issue 48 (January 1988), p. 95, reads in the garbled scan text "A^i?nf X Mastertronic 85% 37/117", which is **Agent X**, alphabetised under "Ag". Ant Attack appears as "Soft Solid 3D Ant Attack 85%, 1/18" (p. 100), a Quicksilva-era title | A garbled scan reading turned into an invented anecdote about Sandy White. |
| `vault/companies/mastertronic.mdx` | Oliver Twins: "Their early careers were Mastertronic titles before they moved to Codemasters" | **WRONG** | Wikipedia (web) https://en.wikipedia.org/wiki/Oliver_Twins: early games came from C&VG (Road Runner type-in), Acornsoft (Gambit), Acorn User, Interceptor, Players and Beebug, then Codemasters (Super Robin Hood). No Mastertronic title | See also: "Oliver Twins — Started at Mastertronic" repeats the error. |
| `vault/companies/acornsoft.mdx` | Aviator written "speculatively… an unsolicited year of work" | **WRONG** | *Acorn Programs*, July 1984, p. 12 (Nicole Segre interview): "Slightly more forward planning went into the creation of Aviator. Crammond discussed his idea for a flight simulator with Acornsoft and a decision was made to base the program on the Spitfire" | It was **Super Invaders** that he sent "out of the blue". |
| `vault/people/ian-logan.mdx` | Rosetta Stone Award "attested here only by Melbourne House's own advertising copy" | **WRONG** | *SYNTAX ZX80* vol. 3 no. 3, March 1982, p. 1: "IAN LOGAN WINS FIRST ANNUAL ROSETTA STONE… sponsored by Mindware Co. of Wayland, MA" | Independent news coverage exists, so the ⚠ caveat is false. The ads quoted (Sinclair User 3–5, 1982) date from 1982, not 1981. |
| `vault/techniques/scrolling.mdx` | "MMC3 IRQ… (Battletoads, Mega Man 3+)" | **WRONG** | NESdev Wiki, mapper list (https://www.nesdev.org/wiki/Mapper): Battletoads is mapper 7 **AxROM**, which has no IRQ | Mega Man 3 on MMC3 was not checked. |
| `vault/techniques/scrolling.mdx` | "Famous Spectrum software scrollers: R-Type, Cobra, Star Wars Trilogy, Cybernoid" | **WRONG** | *CRASH* issue 51, April 1988, p. 13: Cybernoid travels "through the pirates' flick-screen territory" | Cybernoid does not scroll. Star Wars Trilogy was not checked. |
| `vault/games/dungeon-master.mdx` | Spells: "Four power levels (Lo, Um, On, Ee)" | **WRONG** | *ACE* issue 30, March 1990, p. 77: "Power: LO UM ON EE PAL MON"; also *The Games Machine* (Italian edition) issue 12, September 1989, p. 72 | There are six power levels, not four. |
| `vault/companies/epyx.mdx` | "California Games II — 1990" | **WRONG** | Magazine coverage of California Games II clusters in 1992 (*Amiga Power* issue 18, October 1992, p. 78; *Amiga Joker* (Germany), October 1992, p. 32; *AmigaWorld* vol. 8 no. 11, November 1992, p. 84). Wikipedia (web) gives 1992 |  |
| `vault/magazines/acorn-user.mdx` | ended: 1999 | **WRONG** | https://en.wikipedia.org/wiki/Acorn_User (web, Wikipedia): final issue no. 267, December 2003 | 1999 appears to reflect the last issue the entry's author consulted, not the last issue published. |
| `vault/magazines/acorn-user.mdx` | "This library cannot date a clean handover" from Addison-Wesley to Redwood | **WRONG** | *Acorn User* issue 20, March 1984, p. 10: "publishing rights of Acorn User will be handed over from Addison-Wesley… to the Redwood Publishing Company after the April issue". Issue 21 (April 1984), p. 5, is "© Redwood Publishing 1984" | Period sources do date the handover. Wikipedia agrees: Redwood from April 1984. |
| `vault/games/hypersports.mdx` | "CRASH charts, 7 appearances" plus table (Oct 85 #2, Nov 85 #1, Dec 85 #2, Mar 86 #8, May 86 #22, Jun 86 #8) | **WRONG** | Oct #2: *CRASH* issue 21 (October 1985), p. 99. Nov #1: issue 22 (November 1985), p. 112 ("HOTLINE TOP 30 FOR NOV … 1 ( 2) HYPERSPORTS"). Dec #2: issue 23 (December 1985), p. 100. Mar #8: issue 26 (March 1986), p. 63. Jun #8: issue 29 (June 1986), p. 102. **May = #8, not #22**: issue 28 (May 1986), p. 70 ("TOP 30 FOR MAY … 8( 8) HYPERSPORTS Imagine") | Recorded as WRONG (agent marked "IMPRECISE (one row WRONG)"). The table has 6 rows but claims 7 appearances. CRASH actually lists it many more times: Sep 85 #16, Feb 86 #5 (issue 25, p. 93), Apr 86 #8 (issue 27, p. 62), Sep 86 #30, Dec 86 #29. Because May was #8, the "curious bounce back to #8 in June" is invented. It held #8 from March to June. |
| `vault/games/hypersports.mdx` | Decathlon "had established [the genre] a year earlier" | **WRONG** | *CRASH* issue 10, November 1984, p. 93 (Decathlon review: "The arcade original 'Track and Field' has spawned a number of Spectrum versions in this Olympics year") | Konami's own Track and Field arcade game established the waggle genre. Decathlon was one of several 1984 Spectrum games following it. The link text "Daley Thompson's Decathlon" points at /vault/people/christian-urquhart. CRASH credits the Decathlon review to "Paul Ownes & Christian Urquhart" [sic, Owens], so the link target is defensible but mislabelled. |
| `vault/people/bob-yannes.mdx` | `born: 1953` | **WRONG** | (web) https://en.wikipedia.org/wiki/Bob_Yannes and https://www.c64-wiki.com/wiki/Bob_Yannes both give "born 1957" | No print source found. The web sources (Wikipedia is a last resort) agree on 1957. |
| `vault/games/supreme-commander.mdx` | Faction table lists "Seraphim / Alien power" | **WRONG** | (web) same page: the base game has three factions (UEF, Cybran, Aeon). Seraphim were added in the *Forged Alliance* expansion (6 Nov 2007) |  |
| `vault/games/dig-dug.mdx` | Enemy points "Fygar … 300-600" | **WRONG** | Fygar scores the same as Pooka by layer (200/300/400/500) and double when pumped horizontally (400–1000): *Atari Connection* vol. 4 no. 1, March 1984, p. 31 ("blowing Fygar in a horizontal path … score twice as many points"); (web) https://history.blueskyrangers.com/instructions/digdug.html (Intellivision manual: 200 surface … 500 bottom, Fygar "DOUBLE") | The depth-multiplier table (1.5×/2×/2.5×) matches the Pooka values. "Pooka 200-500" is right. |
| `vault/companies/sinclair-research.mdx` | NEB "injected a further £19 million the following year" | **UNSUPPORTED** | SU issue 51 (June 1986), p. 47, timeline: the scan text reads "NEB injects further E l 9m"; it could read £1.9m or £19m | Check the page image before the number stands. |
| `vault/people/clive-sinclair.mdx` | "Sold over 1.5 million units" (ZX81) | **UNSUPPORTED** | No figure found in the period magazines searched. A secondary summary gives "~1.5M" with no primary locator. | The zx81 entry itself marks this as unverified. |
| `vault/people/steven-vickers.mdx` | `born: 1954` | **UNSUPPORTED** | No print source found. (web) Wikipedia https://en.wikipedia.org/wiki/Steve_Vickers_(computer_scientist) gives "born 1952 or 1953" | This is probably wrong: no source gives 1954. |
| `vault/people/steven-vickers.mdx` | "Vickers advocated for ... Keyword entry ... Syntax checking" | **UNSUPPORTED** | Nothing found. Keyword entry was already on the ZX80 (SU 51 p.47: "the now famous single keyword entry method"), before Vickers arrived. | The entry attributes a motive and a role without evidence. |
| `vault/systems/zx-spectrum.mdx` | "over five million sold" | **UNSUPPORTED** | The period sources found say about 4 million: *CRASH* issue 50, March 1988, p. 32 ("some four million Spectrums"); *CRASH* issue 52, May 1988, p. 29 | The 5 million figure is the usual retrospective one, but no source for it was found. |
| `vault/hardware/ula.mdx` | "reason the ZX Spectrum cost £125 instead of £250" | **UNSUPPORTED** | No source found | The counterfactual price is invented. |
| `vault/systems/zx81.mdx` | "Over 1.5 million sold" | **UNSUPPORTED** | No primary source found; the entry's own frontmatter flags it |  |
| `vault/systems/zx81.mdx` | "schools adopted the ZX81 in large numbers" | **UNSUPPORTED** | No source found | This is doubtful. |
| `vault/magazines/crash-magazine.mdx` | Smash = "Anything 90% or above" | **UNSUPPORTED** | No statement of the threshold found in CRASH text |  |
| `vault/people/oliver-frey.mdx` | "Died ... Ludlow, Shropshire" | **UNSUPPORTED** | Neither source gives the place of death |  |
| `vault/people/oliver-frey.mdx` | "Trained at: Royal College of Art" | **UNSUPPORTED** | (web) Wikipedia: Famous Artists School correspondence course in Switzerland | Probably invented. |
| `vault/people/oliver-frey.mdx` | TV21 / Captain Scarlet / Look-In / 2000AD; Superman storyboards; Pirelli | **UNSUPPORTED** | (web) downthetubes lists War Picture Library, Look and Learn (Trigan Empire), Eagle Dan Dare, Battle; for Superman, "comic book art for the ... opening sequence" (not storyboards) | TV21, Look-In and Pirelli look invented. |
| `vault/people/oliver-frey.mdx` | "virtually every CRASH cover from issue 1 to issue 90"; Issue 24 "Knight Lore-era"; Issue 1 "wizard / treasure cave" | **UNSUPPORTED** | Issue 1's cover credit to Frey is confirmed (*CRASH* issue 1, February 1984, p. 5), but its subject was not checked. No per-issue cover credits found for later issues. Knight Lore was reviewed in early 1985, a year before issue 24 | These cover descriptions look invented. |
| `vault/companies/ultimate.mdx` | "Tim Stamper (born 1958) and Chris Stamper (1959)" | **UNSUPPORTED** | Web: Chris b. Oct 1958, Tim b. Feb 1961 (Stamper brothers, Wikipedia, last resort). *CRASH* issue 51 (April 1988), p. 36, has "Chris - at 29", which fits a 1958 birth | Downgraded from WRONG at compilation: *CRASH* issue 51 (April 1988), p. 36, reads "Chris - at 29 the younger, quieter brother", which fits the entry (Tim older, Chris b. 1958/59); only Wikipedia gives Chris 1958 / Tim 1961. Sources conflict; needs a primary birth record. CRASH also calls Chris "the younger" brother, which conflicts with the web dates. Either way the entry's years are wrong. |
| `vault/people/stamper-brothers.mdx` | `born: 1958`; "Tim Stamper (born 1958) and Chris Stamper (born 1959)" | **UNSUPPORTED** | (web) Chris b. 1958, Tim b. 1961 (Stamper brothers, Wikipedia, last resort); *CRASH* issue 51 (April 1988), p. 36: "Chris - at 29" | Downgraded from WRONG at compilation: *CRASH* issue 51 (April 1988), p. 36, reads "Chris - at 29 the younger, quieter brother", which fits the entry (Tim older, Chris b. 1958/59); only Wikipedia gives Chris 1958 / Tim 1961. Sources conflict; needs a primary birth record. The years are swapped or wrong. A single `born` field does not suit a two-person entry. |
| `vault/people/stamper-brothers.mdx` | "two brothers from Loughborough" | **UNSUPPORTED** | Web: Chris attended Loughborough University; the family shop and first premises were in Ashby-de-la-Zouch (Wikipedia). CRASH Apr 1988 says "Based in… Ashby-de-la-Zouch… wholly owned by one family" | The Loughborough link seems to be Chris's university, not where they came from. |
| `vault/people/stamper-brothers.mdx` | "Stampers were 23 and 22" in April 1982 | **UNSUPPORTED** | By the web dates Chris was 23 and Tim 21 | Downgraded from WRONG at compilation: *CRASH* issue 51 (April 1988), p. 36, reads "Chris - at 29 the younger, quieter brother", which fits the entry (Tim older, Chris b. 1958/59); only Wikipedia gives Chris 1958 / Tim 1961. Sources conflict; needs a primary birth record.  |
| `vault/people/stamper-brothers.mdx` | Battletoads "co-developed with the Pickford brothers" | **UNSUPPORTED** | Not in the period sources searched; Wikipedia Rare gives no such credit | Probably wrong; needs a credits check. |
| `vault/games/knight-lore.mdx` | "Ultimate Play the Game's October 1984 release" | **UNSUPPORTED** | The entry's own frontmatter says Nov 1984 is the earliest dated appearance; PCG Nov 1984 news | The prose contradicts the frontmatter. |
| `vault/games/knight-lore.mdx` | Werewolf form "slower, deadlier"; puzzles that need werewolf form | **UNSUPPORTED** | Nothing in CRASH 12 or Sinclair Programs Jan 1985. Sinclair Programs describes the change as "annoying… lethal" mid-manoeuvre, with a 40-day limit | Looks invented. |
| `vault/games/knight-lore.mdx` | "roughly 6 frames per second"; "in the British Library's permanent collection" | **UNSUPPORTED** | No source found |  |
| `vault/games/knight-lore.mdx` | platforms include `commodore-64` | **UNSUPPORTED** | No C64 Knight Lore found in period magazines | Probably no official C64 version exists. |
| `vault/people/matthew-smith.mdx` | Manic Miner "sell over 250,000 copies" | **UNSUPPORTED** | Magazine searches ("Manic Miner has sold", "copies of Manic Miner") found nothing. CRASH Apr 1988 uses 250,000 for Ghostbusters instead |  |
| `vault/people/matthew-smith.mdx` | "By nineteen he was a millionaire" | **UNSUPPORTED** | PCG Mar 1984 says only "he certainly had made some money" |  |
| `vault/people/matthew-smith.mdx` | "a first for the platform" (continuous beeper music) | **UNSUPPORTED** | Only Wikipedia (web) makes the claim; no period source found | Manic Miner's own entry is more careful ("usually credited"). |
| `vault/people/matthew-smith.mdx` | "left Bug-Byte with the game's source code (per the contract's wording)" | **UNSUPPORTED** | PCG issue 03 (Feb 1984): "Matthew has taken the rights to Manic Miner with him" | Nothing supports the contract detail. |
| `vault/people/matthew-smith.mdx` | "As of the mid-2020s, Smith is alive" | **UNSUPPORTED** | No recent print source found | Not checked on the web. |
| `vault/games/manic-miner.mdx` | "Smith wrote Manic Miner in his bedroom in Wallasey" | **UNSUPPORTED** | PCG Mar 1984: written on a Tandy Model 4 (5MB hard disk), then transcribed to the Spectrum; says nothing of Wallasey | PCG also says the original idea came from Alan Maton. |
| `vault/companies/mastertronic.mdx` | "BMX Racers is reported to have passed a million" | **UNSUPPORTED** | No period-magazine hit for BMX Racers with sales figures | Reported by whom is not stated. |
| `vault/companies/acornsoft.mdx` | Crammond Retro Gamer quote ("expecting it to be published by Acornsoft… took me a year") | **UNSUPPORTED** | No match in *Retro Gamer* or any other period magazine searched (for "own enjoyment", "first experience of writing", "real-time simulator") | The quote could not be found. |
| `vault/companies/acornsoft.mdx` | Elite rank needed "around 6,400" kills (2002 retrospective) | **UNSUPPORTED** | No period-magazine hit for 6,400/6400 with Elite; the 2002 retrospective is not named or cited | The entry's own ⚠ already flags this. |
| `vault/companies/epyx.mdx` | Hardware: "ROXX — Unreleased" | **UNSUPPORTED** | No period-magazine hit linking ROXX to Epyx; not in Wikipedia's hardware list | Possibly invented. |
| `vault/companies/epyx.mdx` | Opening slogan: "Games by gamers, for gamers" | **UNSUPPORTED** | No period-magazine hit for the phrase with Epyx | Presented as Epyx's slogan with no evidence. |
| `vault/genres/western-rpg.mdx` | "Ultima established the template" | **UNSUPPORTED** | No source found that credits Ultima with setting the template (searched magazines and books). | A "first/established" superlative with no evidence. Wizardry came out the same year (1981), and mainframe CRPGs came earlier. I did not verify those earlier titles against sources, so I report the claim as unsupported rather than wrong. |
| `vault/games/wizball.mdx` | "The Games Machine at 80%" | **UNSUPPORTED** | *The Games Machine* issue 1, October 1987, p. 15, has only an Atari ST preview. No TGM Spectrum score found. |  |
| `vault/games/wizball.mdx` | "Your Sinclair 8/10" | **UNSUPPORTED** | YS issue 20, August 1987, pp. 40-41, is a pre-release write-up ("It's not quite ready yet"). No legible YS score found. YS issue 22 (October 1987), p. 15, has a reader letter mentioning "the Wizball review". |  |
| `vault/people/clive-sinclair.mdx` | "ZX80: Britain's first home computer under £100" | **IMPRECISE** | C&VG issue 1, November 1981, p. 21: Sinclair's own advert calls it the "world's first complete personal computer for under £100" | This is a manufacturer's advertising claim, not an established fact, so attribute it. |
| `vault/people/clive-sinclair.mdx` | "knighted for services to British industry in 1983" | **IMPRECISE** | SU 51: "knighted in the 1983 Birthday honours list" | The year is verified. The citation wording was not found in any source consulted. |
| `vault/people/clive-sinclair.mdx` | Sold "after the QL ... commercial failure dented ... finances" | **IMPRECISE** | SU 51 p.47: the 1985 crisis came from the market nose-dive and overstocked Spectrum Plus distributors, as well as the QL | The entry reduces a crisis with several causes to the QL alone. |
| `vault/people/steven-vickers.mdx` | "wrote the ZX Spectrum's ROM" (sole author) | **IMPRECISE** | *MC Microcomputer* (Italy) no. 20, June 1983, p. 47: Vickers "wrote most of the software contained in the ROM" | Co-written with John Grant, per Smith, ch. 7. |
| `vault/systems/zx-spectrum.mdx` | "about a third the price of a Commodore 64 at the time" | **IMPRECISE** | The C64 was not on sale in the UK in April 1982 | This compares against a machine that did not yet exist at the launch date. |
| `vault/systems/zx-spectrum.mdx` | FLASH "swaps INK and PAPER about twice a second" | **IMPRECISE** | Smith, ch. 14 (the flash counter): a swap every 16 frames, ~1.56 Hz full cycle | Close enough, but "about three swaps a second" is the accurate description. |
| `vault/hardware/ula.mdx` | Loading stripes "driven by the same bit 4 that the beeper uses" | **IMPRECISE** | Smith, ch. 19 (Figure 19-4, the border colour register): the border is bits 0-2 | The ROM loader writes the border colour through bits 0-2. Bit 4 is the speaker. |
| `vault/systems/zx81.mdx` | "Sinclair's own manual calls the 'dogsbody'"; "The manual is blunt ... 30 integrated circuits" | **IMPRECISE** | Thomasson, p. 10: this is Don Thomasson's Melbourne House book (1983), which says "the manual calls the 'dogsbody'" | "Dogsbody" is second-hand. The "blunt" quotes are Thomasson's, not Sinclair's manual. The frontmatter title "The ZX81: Its Ins and Outs" is also wrong: the book is "The Ins and Outs of the TS1000 & ZX81". |
| `vault/people/oliver-frey.mdx` | "Friday the 13th ... several Newsfield issues" | **IMPRECISE** | *CRASH* issue 24, January 1986, p. 179 (issue index): the Friday 13th "Scary cover" was CRASH 23, December 1985 | That is a single CRASH issue. |
| `vault/companies/ultimate.mdx` | `ended: 1988` / "sold the Ultimate brand to US Gold in 1988" | **IMPRECISE** | *CRASH* issue 51, April 1988, p. 36: "US Gold had won out and taken over Ultimate. The terms of the sale were obscure; the Stampers retained a majority shareholding"; the label "largely dormant since mid-1987". Wikipedia Rare (web) gives 1986 for the sale | The entry says no period source exists, but CRASH Apr 1988 has one. It also shows the Stampers kept majority control, so "sold the brand and back catalogue" overstates the deal. |
| `vault/companies/ultimate.mdx` | "trained in electronics and computer science respectively" | **IMPRECISE** | Web (Wikipedia, Stamper brothers): Chris read electronics and physics at Loughborough and left in 1981 | Nothing supports "computer science" for Tim. |
| `vault/companies/ultimate.mdx` | "Stampers did give interviews… telling Roger Kean" ("Reclusive is overstated") | **IMPRECISE** | *CRASH* issue 51, April 1988, p. 35: the Stampers "were secretive and gave no interviews"; a promised CRASH interview "never came"; Kean heard the story "a few months ago", i.e. 1987-88 after Ultimate had faded | The primary source backs the reclusive reputation for the Ultimate years. The Kean interview came in CRASH (Apr 1988), not *Arcade*; *Arcade* (issue 1, December 1998, p. 176) only retells it. |
| `vault/companies/ultimate.mdx` | Knight Lore held back; "anxious to avoid rendering all following games disappointments" | **IMPRECISE** | Primary: *CRASH* issue 51, April 1988, p. 38: Tim: "Knight Lore was finished before Sabre Wulf… if we released Knight Lore and Alien 8… we wouldn't have sold Sabre Wulf" | The quoted motive is *Arcade*'s 1998 paraphrase (*Arcade* issue 1, December 1998, p. 176). Tim's own reason was protecting Sabre Wulf's sales, and Alien 8 was held back too. |
| `vault/companies/ultimate.mdx` | CRASH: Knight Lore "the second most cloned piece of software after WordStar" | **IMPRECISE** | *CRASH* issue 51, April 1988, p. 35: "one CRASH reader has claimed it became the second-most-cloned…"; also *CRASH* issue 46, November 1987, p. 18 | CRASH gives this as a reader's claim, so it is not "CRASH's own summary". |
| `vault/companies/ultimate.mdx` | "roughly twenty titles for the ZX Spectrum" | **IMPRECISE** | *CRASH* issue 51, April 1988, p. 35: "an unbroken chain of 14 Spectrum hit games" (1983-86); its ratings table (p. 38) lists 13 | "Roughly twenty" looks high for the Spectrum. |
| `vault/companies/rare.mdx` | "Second-party developer from late 1980s" | **IMPRECISE** | (web) Wikipedia, Rare: Nintendo bought a 25% stake in 1994, later 49%, which made Rare second-party | In the late 1980s Rare was a licensed third-party NES developer. |
| `vault/people/stamper-brothers.mdx` | ran ACG "in the late 1970s and early 1980s" doing contract arcade work | **IMPRECISE** | (web) Wikipedia: they worked as employees at Associated Leisure and Zilec on arcade conversions; ACG founded 1982. *CRASH* issue 51, April 1988: "started as designers of real-life arcade-machine programs" | ACG did not exist in the late 1970s. |
| `vault/people/stamper-brothers.mdx` | "By 1988… folded Ultimate's UK publishing arm into US Gold (selling the Ultimate brand)" | **IMPRECISE** | *CRASH* issue 51, April 1988, p. 36: US Gold "taken over Ultimate", the Stampers "retained a majority shareholding"; Wikipedia Rare (web) gives 1986 |  |
| `vault/games/knight-lore.mdx` | Delayed because "worried it would devalue Sabre Wulf and Atic Atac" | **IMPRECISE** | *CRASH* issue 51, April 1988, p. 38, Tim: "Knight Lore was finished before Sabre Wulf… we wouldn't have sold Sabre Wulf" | Tim named only Sabre Wulf, and says Alien 8 was held back as well. Atic Atac is not mentioned. |
| `vault/people/matthew-smith.mdx` | `born: 1966` | **IMPRECISE** | (web) Wikipedia: born 1966. PCG issue 4 (March 1984): "At 18…", interviewed in December 1983, which implies a 1965 birth | The sources conflict. The entry also puts him at 17 in 1983 and 18 at Jet Set Willy. |
| `vault/people/matthew-smith.mdx` | "taught himself Z80 assembly on a ZX Spectrum in his parents' house" | **IMPRECISE** | PCG issue 4 (March 1984): started on a Tandy (4K); "wrote Manic Miner on a Model 4 Tandy with 5 Megabyte hard disk and then transcribed it on to the Spectrum"; first got a Spectrum in April 1983 | The machine is wrong. |
| `vault/people/matthew-smith.mdx` | "over several months… homebrew assembler and… squared paper" | **IMPRECISE** | PCG Mar 1984: "spend eight solid weeks on the new program"; drew graphics "on graph paper"; wrote on a Tandy Model 4 | Graph paper is supported. "Several months" and "homebrew assembler" are not. |
| `vault/games/jet-set-willy.mdx` | PCG 10/10 "the same month" | **IMPRECISE** | PCG issue 06 (May 1984): Game of the Month confirmed; the score is not legible in the scan | SU 9/10 and Big K 3/3 were not checked. |
| `vault/games/jet-set-willy.mdx` | POKE culture "ran ahead of the magazines rather than out of them" | **IMPRECISE** | *CRASH* issue 6, July 1984, p. 100, prints the Attic POKEs the next month, with Software Projects' permission | CRASH held off for one issue only. |
| `vault/companies/mastertronic.mdx` | "In 1987, Richard Branson's Virgin Group acquired Mastertronic… as Virgin Mastertronic" (The Virgin years) | **IMPRECISE** | Contradicts the entry's own ACE-based section (minority stake, ~Oct 1987). Wikipedia (web): Virgin took the remaining 55% in 1988, creating Virgin Mastertronic | Fast facts and "The Virgin years" still carry the 1987-acquisition version the body argues against; the page contradicts itself. |
| `vault/companies/mastertronic.mdx` | CRASH issue 41 (April 1987): "yet another MASTERTRONIC label, this time BULLDOG" | **IMPRECISE** | The quote is in *CRASH* issue 39, April 1987, p. 130; April 1987 is issue **39**, not 41. The "Mastersounds… Mastervision… Arcadia… Paul Street" quote is in the same issue (p. 91) | Frontmatter cites the wrong issue number. |
| `vault/companies/mastertronic.mdx` | "Codemasters' best Spectrum score in the same index is 79%, below Mastertronic's 85%" | **IMPRECISE** | Professional Ski Simulator, Code Masters 79% (*CRASH* issue 48, p. 99) is correct; Mastertronic's best is 94%, not 85% | The conclusion holds more strongly than stated, but the numbers given are wrong. |
| `vault/companies/acornsoft.mdx` | "ACE's readers had voted it second in an all-time list… 'we couldn't agree more'" | **IMPRECISE** | *ACE* issue 41, February 1991, p. 64: the item is headed "A READER WRITES", one reader's (Vincent's) top ten with ACE's comments. Elite is no. 2, followed by Stunt Car Racer (3), Alien 8 (5), Atic Atac (6) and Kick Off (7) | One reader's list, not a readers' vote. The quote is correct. |
| `vault/companies/acornsoft.mdx` | "Crammond… took an earlier game to a publisher who released it as Super Invaders" | **IMPRECISE** | Same interview (p. 12): he sent Super Invaders to **Acornsoft**, which accepted it over its own Mode 7 invaders game | The publisher was Acornsoft itself, which undercuts the entry's "first published elsewhere" framing. |
| `vault/people/ian-logan.mdx` | Jupiter Ace User Dec 1982: listing obtained by cross-loading Ace ROM to Spectrum; cassette standards identical | **IMPRECISE** | *Ace User* (Jupiter Ace Users Club newsletter) issue 1, December 1982, p. 4: "has **apparently** obtained a listing… The cassette standards are **apparently** identical" | The source is hearsay (a postscript, hedged twice), but the entry states it as fact. |
| `vault/people/ian-logan.mdx` | Summary: "across four Melbourne House books" | **IMPRECISE** | The entry's own list has six titles, and the Microdrive book makes seven | Internal inconsistency. |
| `vault/techniques/scrolling.mdx` | SNES: "Up to 4 BG layers (modes 0-1)" | **IMPRECISE** | SNESdev Wiki, PPU registers and background modes (BGMODE): 4 layers in Mode 0 only; Mode 1 has 3 |  |
| `vault/games/dungeon-master.mdx` | "Developer: FTL Games (Doug Bell, Andy Jaros, Wayne Holder)" | **IMPRECISE** | *ACE* issue 11, August 1988, p. 37, credits "Andy Jaros, Doug Bell & Mike Newton"; Wayne Holder is FTL's head in *ACE* issue 9, June 1988, p. 9. Wikipedia (web) also lists Dennis Walker | Mike Newton is left out. Holder was producer rather than developer. |
| `vault/games/dungeon-master.mdx` | "Crystal Computing's unrelated 1984 Spectrum game The Dungeon Master" | **IMPRECISE** | *CRASH* issue 1, February 1984, p. 12, already calls Crystal "famous for… Halls of the Things, and Dungeon Master" in Feb 1984 | That points to a 1983 release, not 1984. |
| `vault/people/roberta-williams.mdx` | "She invented the graphic adventure. Before Roberta Williams, adventure games were text-only" | **IMPRECISE** | As above; the claim overreaches | Ken Williams programmed Mystery House (*Antic*, November 1982, p. 23: "which her husband programmed"). Crediting her alone as "inventor" oversimplifies. |
| `vault/people/roberta-williams.mdx` | "Career: 1980-1999" | **IMPRECISE** | Wikipedia (web): she left Sierra in 1999, then returned to game development (Colossal Cave 3D remake, 2023) and published a novel in 2021 | The end date reads as final, but she is alive and working. |
| `vault/genres/western-rpg.mdx` | `emerged: 1974` / "Origins: Tabletop RPGs (1974)" | **IMPRECISE** | Tim Hartnell, *Tim Hartnell's Giant Book of Computer Games* (Ballantine, 1984), p. 95 ("initially gave to the world in 1974 as a boxed set of three booklets under the title Dungeons and Dragons"); also Tim Hartnell, *Creating Adventure Games on Your Computer* (Ballantine, 1984), p. 12 (TSR formed 1974) | 1974 is correct for D&D, but D&D is tabletop. The frontmatter field reads as the date the video-game genre emerged, which is later (Ultima and Wizardry both appeared in 1981). The body frames it correctly as "Origins". |
| `vault/genres/western-rpg.mdx` | WRPG "Real-time/tactical" vs JRPG "Turn-based" | **IMPRECISE** | — | Overgeneralised. Wizardry and early Ultima were turn-based, as were Fallout and many CRPG-revival titles. The WRPG-vs-JRPG table asserts contrasts with no source. |
| `vault/genres/western-rpg.mdx` | `platforms:` list (IBM PC, Xbox, PS3…) | **IMPRECISE** | — | Omits the Apple II, where Ultima and Wizardry launched, and every 8-bit home computer, even though the entry names 1980s titles. |
| `vault/games/hypersports.mdx` | "one of the games CRASH's reader ranking credits him with, alongside Green Beret and Cobra" | **IMPRECISE** | *CRASH* issue 50, March 1988, p. 8 | The credit list comes from a CRASH news item (Mar 1988) about Firefly, not from a reader ranking. |
| `vault/games/hypersports.mdx` | "Joysticks broke. Microswitched sticks were sold on their ability to survive this genre" | **IMPRECISE** | *CRASH* issue 10, November 1984, p. 25 ("A joystick must be able to withstand games that require fast and repeated movement, so what better than Ocean's Daley Thompson's Decathlon?") | CRASH did test joystick toughness on a waggle game. The claim that microswitched sticks were *marketed* on this basis is not shown. The "£9.99 joystick" price is unsourced colour. |
| `vault/people/bob-yannes.mdx` | "amateur musician and electronics tinkerer before joining MOS" | **IMPRECISE** | *Compute!* issue 32, January 1983, p. 34 ("I played with synthesizers for years, so I'm quite familiar with them") | Supports a synth hobbyist. "Amateur musician and electronics tinkerer" is an embellishment of that. |
| `vault/people/bob-yannes.mdx` | "disliked simplistic square-wave chips, so he built SID to sound musical" | **IMPRECISE** | *Compute!* issue 32, January 1983, p. 34 ("given specifications by Commodore only to develop a 'sound chip,' and then he decided to make it as much like a synthesizer as possible"); a secondary summary with no primary locator adds "frustrated by the primitive sound capabilities of other computers" | The gist is supported. The "square-wave" specifics and the motive are paraphrased with no primary quote. |
| `vault/games/dig-dug.mdx` | "Character: Taizo Hori" | **IMPRECISE** | *Blip* vol. 1 no. 1, February 1983, p. 20 ("Dig Dug also happens to be the name of the game's hero") | The period name for the hero was "Dig Dug". The name Taizo Hori came later, in the Mr. Driller era (web, same Wikipedia page). |
| `vault/games/dig-dug.mdx` | "Later starred in Mr. Driller" | **IMPRECISE** | (web) Wikipedia: Taizo is the father of Mr. Driller's protagonist Susumu Hori | He appears in the series, but his son is its star. |
| `vault/companies/sinclair-research.mdx` | `founded: 1979` / "founded ... in 1979" | **VERIFIED** | SU issue 51, June 1986, p. 47: Sinclair Research "not founded until July 1979"; timeline "1979 Sinclair splits from NEB. Sets up Science of Cambridge with Chris Curry" | The entry's own Companies House section shows the legal company dates from 1973; the prose handles this correctly. |
| `vault/companies/sinclair-research.mdx` | Company 01135105: incorporated 19 Sep 1973 as Westminster Mail Order; five names; dissolved 14 Oct 2025 | **VERIFIED** | (web) https://find-and-update.company-information.service.gov.uk/company/01135105: incorporated 19 September 1973, dissolved 14 October 2025, previous names and years match the table |  |
| `vault/companies/sinclair-research.mdx` | "ZX80 (1980, £99.95), the ZX81 (1981, £49.95 kit / £69.95 built), ZX Spectrum (1982, £125 / £175)" | **VERIFIED** | C&VG issue 1, November 1981, p. 22 ("In March 1981 ... For just £69.95 the Sinclair ZX81"), coupon p. 23 (kit £49.95); SU issue 51, June 1986, p. 47, timeline "1980 ZX80 (£99.95)", "1982 Spectrum launched 16K (£125) 48K (£175)" | The ZX80's £99.95 is the built price; the kit was cheaper. |
| `vault/companies/sinclair-research.mdx` | Radionics 1961; Curry 1966; Searle 1973; Black Watch cost £355,000; NEB 43% for £650,000 in 1976 | **VERIFIED** | SU issue 51, June 1986, p. 47, timeline column |  |
| `vault/companies/sinclair-research.mdx` | SU quote: "a disastrous operation ... The pattern of late deliveries and unreliability had begun to emerge" | **VERIFIED** | SU issue 51, June 1986, p. 47 |  |
| `vault/companies/sinclair-research.mdx` | "By May ... £5 million against 13,000 orders, of which only a few hundred had been delivered" | **VERIFIED** | SU 51 p.47 (same column); also *Bits & Bytes* (New Zealand) vol. 2 no. 9, June 1984, p. 8 ("backlog of 13,000 orders") |  |
| `vault/companies/sinclair-research.mdx` | CRASH/Minson quote: "hastily called press conference at noon on 7th April" | **VERIFIED** | *CRASH* issue 28, May 1986, p. 12 | The quotation is word for word. |
| `vault/companies/sinclair-research.mdx` | YS: "sitting next to ... Alan Sugar who's called the Spectrum a pregnant calculator" | **VERIFIED** | YS issue 6, June 1986, p. 11 |  |
| `vault/companies/sinclair-research.mdx` | Amstrad sold "over 20,000 rubber-key 16K and 48K Spectrums" plus QL stock "worth more than £2 million" | **VERIFIED** | SU issue 51, June 1986, p. 7 (to "PMT, an overseas distributor") |  |
| `vault/companies/sinclair-research.mdx` | Address "6 Kings Parade, Cambridge, CB2 1SN", C&VG Nov 1981 | **VERIFIED** | C&VG issue 1, November 1981, p. 23 |  |
| `vault/people/clive-sinclair.mdx` | `born: 1940`, `died: 2021`; "until his death in September 2021" | **VERIFIED** | SU issue 51, June 1986, p. 47, timeline "born 30 July 1940"; (web) https://www.theregister.com/2021/09/17/sir_clive_sinclair_obituary/ (died 16 September 2021, aged 81) | Living/dead status is handled correctly. |
| `vault/people/clive-sinclair.mdx` | "sold ... to Amstrad in April 1986 for £5 million" | **VERIFIED** | *CRASH* issue 28, May 1986, p. 12; YS issue 6, June 1986, p. 11 |  |
| `vault/people/steven-vickers.mdx` | "wrote the ZX Spectrum manual" | **VERIFIED** | *MC Microcomputer* (Italy) no. 20, June 1983, p. 47 (the manual "bears his name"); *Sinclair ZX Spectrum BASIC Programming* (Sinclair Research, 1982) is credited to Steven Vickers |  |
| `vault/people/steven-vickers.mdx` | "Later career: academia, constructive mathematics" | **VERIFIED** | https://www.birmingham.ac.uk/news-archive/2018/dr-steve-vickers-personal-computing-pioneer | Broadly right: his field is topology and logic. |
| `vault/systems/zx-spectrum.mdx` | "Launched in April 1982 ... £125 (16K) or £175 (48K)" | **VERIFIED** | SU issue 51, June 1986, p. 47 ("The Spectrum, launched in April 1982"; timeline £125/£175) |  |
| `vault/systems/zx-spectrum.mdx` | BBC "£299 for the Model A and £399 for the Model B", C&VG Jan 1983 | **VERIFIED** | C&VG issue 15, January 1983, p. 66 (Eltec ad) and p. 5 |  |
| `vault/hardware/ula.mdx` | Part numbers 6C001E / 5C112E / 5C102E; 7K010E (128K); Amstrad 40077 (+2A/+3) | **VERIFIED** | Smith, ch. 24 ("ULA Versions") and ch. 15 (pp. 137-146) | The table puts the grey +2 with the 7K010E. That was not checked. |
| `vault/hardware/ula.mdx` | ULA "gates the processor's clock" rather than using WAIT | **VERIFIED** | Adrian Dickens, *Spectrum Hardware Manual*, 2nd edn (Melbourne House), ch. 8, "The Uncommitted Logic Array" ("it hastily stops the CPU clock", monitoring A14 and A15) |  |
| `vault/hardware/ula.mdx` | Snow: refresh address not treated as contention, "technically correct", /RAS collision | **VERIFIED** | Smith, ch. 23, "Hidden Features and Errors", pp. 245-246 | Smith gives the range as 0x4000-0x7F7F, not 0x7FFF. The frontmatter cites p.268, which does not match Smith's pp.245-246. |
| `vault/hardware/ula.mdx` | 69,888 T-states/frame; FLASH every 16 frames; contention 6,5,4,3,2,1,0,0 | **VERIFIED** | Smith, ch. 14 (frame timing and the flash counter) and ch. 18, pp. 192 and 197 (contention) |  |
| `vault/systems/zx81.mdx` | "Launch: March 1981" | **VERIFIED** | C&VG issue 1, November 1981, p. 22 ("In March 1981 ..."); SU issue 51, June 1986, p. 47 ("ZX81, launched in March 1981") |  |
| `vault/systems/zx81.mdx` | "3.25 MHz — a 6.5 MHz ceramic filter, halved by the ULA" | **VERIFIED** | Thomasson, pp. 17 and 44 |  |
| `vault/systems/zx81.mdx` | FAST "four times as fast"; SLOW program runs "about a quarter of the time" | **VERIFIED** | Thomasson pp.10-11 (quoted accurately in frontmatter) |  |
| `vault/magazines/crash-magazine.mdx` | `founded: 1984` (Feb 1984, issue 1); `ended: 1992` (Apr 1992, issue 98) | **VERIFIED** | *CRASH* issue 1, February 1984, and issue 98, April 1992; the run is unbroken from issue 1 to issue 98 |  |
| `vault/magazines/crash-magazine.mdx` | No November 1991; Europress first appears in issue 94 | **VERIFIED** | Issue 93 is dated October 1991 and issue 94 December 1991, with no issue between; Europress does not appear in issue 93 and first appears in issue 94, p. 5 |  |
| `vault/magazines/crash-magazine.mdx` | "rose to £1.95 by 1990" | **VERIFIED** | *CRASH* issue 71, December 1989, p. 1, and issue 72, January 1990, p. 1: £1.95 | It later fell back to £1.70 (*CRASH* issue 75, April 1990, p. 1). |
| `vault/magazines/crash-magazine.mdx` | Issue 1 axes: Use of computer, Graphics, Playability, Getting started, Addictive qualities, Value for money, Overall | **VERIFIED** | *CRASH* issue 1, February 1984, p. 12 |  |
| `vault/magazines/crash-magazine.mdx` | Editor Roger Kean, with Oliver Frey | **VERIFIED** | *CRASH* issue 1, February 1984, p. 5 | Frey is credited as "Designer" and "Cover illustration", not "art director". |
| `vault/magazines/crash-magazine.mdx` | "Crash Smash 91%" in mail-order copy into 1990 | **VERIFIED** | *8000 Plus* issue 41, February 1990, p. 71 |  |
| `vault/people/oliver-frey.mdx` | Pseudonym "Zack"; partnership with Kean; Thalamus Publishing | **VERIFIED** | Wikipedia; downthetubes |  |
| `vault/companies/ultimate.mdx` | `founded: 1982` | **VERIFIED** | Stamper brothers, Wikipedia (web, last resort): https://en.wikipedia.org/wiki/Stamper_brothers — ACG founded 1982 in Ashby-de-la-Zouch; *CRASH* issue 51, April 1988, p. 35, has Jetpac and Pssst out in 1983 | The earliest sighting of the trade name found is 1983 (C&VG issue 25, November 1983 advert). |
| `vault/companies/ultimate.mdx` | "Louise Stamper collected the awards on behalf of Ultimate" (June 1985) | **VERIFIED** | C&VG issue 44, June 1985, p. 122 |  |
| `vault/companies/ultimate.mdx` | "ULTIMATE PLAY THE GAME is a Trade name of Ashby Computers & Graphics Ltd." | **VERIFIED** | SU issue 20, November 1983, p. 127; *CRASH* issue 2, March 1984, p. 7; C&VG issue 25 (November 1983), p. 127 | Found in many adverts; the Annual 1984 itself was not checked. |
| `vault/companies/ultimate.mdx` | ZZAP! 21 reader: "Ashby Computers and Graphics, more commonly known as Ultimate" | **VERIFIED** | *Zzap!64* issue 21 (Christmas special, 1986), p. 22 |  |
| `vault/companies/ultimate.mdx` | C&VG 1996: "JETPAC and PSST… crammed into just 16K… Interface II" | **VERIFIED** | C&VG issue 181, December 1996, p. 103 | The entry contradicts itself: "Four games sit in between", then "Six games before Atic Atac". CRASH Apr 1988 says Lunar Jetman came out with Atic Atac as a 48K pair. |
| `vault/companies/ultimate.mdx` | Jetpac "£5.50 cassette" | **VERIFIED** | SU issue 17, August 1983, p. 92 (mail-order list, Jetpac and PSSST at £5.50) |  |
| `vault/companies/ultimate.mdx` | "Microsoft acquired Rare in 2002 for $375 million" | **VERIFIED** | (web) https://en.wikipedia.org/wiki/Rare_(company) — 24 Sep 2002, $375m |  |
| `vault/companies/rare.mdx` | `founded: 1985`; company 01905690, incorporated 1985-04-16 | **VERIFIED** | (web) https://find-and-update.company-information.service.gov.uk/company/01905690 — RARE LIMITED, incorporated 16 April 1985 |  |
| `vault/companies/rare.mdx` | "Location: Twycross, Leicestershire" | **VERIFIED** | *CRASH* issue 51, April 1988, p. 36: Rare moved "to the nearby village of Twycross" |  |
| `vault/companies/rare.mdx` | "Microsoft acquisition: 2002, for $375 million" | **VERIFIED** | (web) Wikipedia, Rare (company) |  |
| `vault/companies/rare.mdx` | DKC "Sold over 9 million copies" | **VERIFIED** | (web) Wikipedia, Rare: "over nine million copies" | Wikipedia only. |
| `vault/companies/rare.mdx` | "Reverse-engineered the NES. Pitched directly to Nintendo Japan." | **VERIFIED** | (web) Wikipedia, Stamper brothers (six months studying NES hardware); *CRASH* issue 51, April 1988, p. 38: found the console "through their contacts in the Japanese…" | The detail rests largely on web sources. |
| `vault/people/stamper-brothers.mdx` | "They almost never gave interviews" | **VERIFIED** | *CRASH* issue 51, April 1988, p. 35: "secretive and gave no interviews" | This contradicts the Ultimate entry's "reclusive is overstated" box. |
| `vault/people/stamper-brothers.mdx` | "Slalom (1986), R.C. Pro-Am (1988), Wizards & Warriors (1987)" | **VERIFIED** | (web) Wikipedia, Rare |  |
| `vault/people/stamper-brothers.mdx` | "In 2007, the Stampers left Rare" | **VERIFIED** | (web) Wikipedia, Rare and Stamper brothers: left in early 2007 |  |
| `vault/games/knight-lore.mdx` | `released: 1984`; launch advert Nov 1984 (CRASH 10) | **VERIFIED** | PCG issue 12 (November 1984): news "the big surprise is the release of… Knight Lore at the same time" as Underwurlde, plus the Ultimate advert with £9.95 |  |
| `vault/games/knight-lore.mdx` | "99% in Sinclair Programs" | **VERIFIED** | *Sinclair Programs* issue 27 (January 1985, Soft Focus): "Rating: 98%(U), 99%(K)" |  |
| `vault/games/knight-lore.mdx` | "94% in CRASH" | **VERIFIED** | *CRASH* issue 12, January 1985, p. 17 (Overall 94%); also the ratings table in *CRASH* issue 51, April 1988, p. 38 |  |
| `vault/games/knight-lore.mdx` | Monochrome rooms to avoid attribute clash | **VERIFIED** | *Sinclair Programs* issue 27 (January 1985): "Each room is shown in one colour only… so there is no colour clash"; *CRASH* issue 12, January 1985: "only one colour is used per screen" |  |
| `vault/people/matthew-smith.mdx` | "co-founded Software Projects with Alan Maton" | **VERIFIED** | PCG issue 03 (Feb 1984): "co-founders, Alan and Soo Maton" | Soo Maton was a co-founder too. |
| `vault/people/matthew-smith.mdx` | JSW bug fix "published as a series of POKEs in CRASH" | **VERIFIED** | *CRASH* issue 6, July 1984, p. 100: "JET SET WILLY ATTIC POKES", published with Software Projects' permission | "Smith had inadvertently made several rooms uncompletable" is loose. CRASH Jun 1984 first presented the Attic effect as "built into the game". |
| `vault/games/manic-miner.mdx` | `released: 1983`; PCN 17 Aug 1983 information box | **VERIFIED** | PCN, 17 August 1983: 48K Spectrum, £5.95, Bug-Byte, Mulberry House…, "Other versions None" |  |
| `vault/games/manic-miner.mdx` | C&VG July 1983 "in the shops now at £5.95" | **VERIFIED** | C&VG issue 21, July 1983, p. 16 (garbled in the scan but legible) |  |
| `vault/games/manic-miner.mdx` | C&VG Aug 1983 "sixteen screen… due out shortly" | **VERIFIED** | C&VG issue 22, August 1983, p. 17 | The same notice also says "in the shops in July" and "16 or 48k", so the August notice contradicts itself as well as the July one. |
| `vault/games/manic-miner.mdx` | PCN title-screen quote; "Skater's Waltz"; "since I first encountered Donkey Kong" | **VERIFIED** | PCN, 17 August 1983 |  |
| `vault/games/manic-miner.mdx` | Styx review "once you've done it a few times there's nothing much left" | **VERIFIED** | same PCN issue |  |
| `vault/games/manic-miner.mdx` | MRIB chart No. 10; "within a few weeks of release… best-selling" | **VERIFIED** | PCG issue 2 (December 1983): "10 Manic Miner Bug Byte Spectrum"; Screen Star text |  |
| `vault/games/manic-miner.mdx` | Maton was Bug-Byte's marketing manager, "despatch rider to marketing manager" | **VERIFIED** | PCG issue 3 (February 1984) | Tony Baden and Tony Milner staying was not checked. |
| `vault/games/manic-miner.mdx` | CRASH Hotline March 1984: No. 1, up from 23, credited to Software Projects | **VERIFIED** | *CRASH* issue 2, March 1984, p. 68 |  |
| `vault/games/manic-miner.mdx` | CRASH 2: "best platform game around… probably the best arcade game" | **VERIFIED** | *CRASH* issue 2, March 1984, p. 54 |  |
| `vault/games/manic-miner.mdx` | PCG "a bit of Tchaikovsky"; Screen Star; "Superb."; Eugene Evans bracket | **VERIFIED** | PCG issue 2 (December 1983) |  |
| `vault/games/manic-miner.mdx` | CRASH "get off your Eugene's Lair and back to the surface" | **VERIFIED** | *CRASH* issue 2, March 1984, p. 23 |  |
| `vault/games/manic-miner.mdx` | Your Spectrum issue 1 lists it at £7.95 | **VERIFIED** | *Your Spectrum* issue 1, January 1984, p. 55 |  |
| `vault/games/jet-set-willy.mdx` | CRASH May 1984, 95% overall; 99% value, 98% addictive, 96% graphics; "Lives: 8" | **VERIFIED** | *CRASH* issue 4, May 1984, pp. 8-9 |  |
| `vault/games/jet-set-willy.mdx` | Entered chart at 41, "only a very few days on sale"; MM "as yet unaffected" | **VERIFIED** | *CRASH* issue 4, May 1984, p. 94 |  |
| `vault/games/jet-set-willy.mdx` | Colour code card "must be looked after at all costs" | **VERIFIED** | *CRASH* issue 4, May 1984, p. 8 |  |
| `vault/games/jet-set-willy.mdx` | £5.95 | **VERIFIED** | PCG issue 06 (May 1984): "SUPPLIER: SOFTWARE PROJECTS PRICE: £5.95" |  |
| `vault/games/jet-set-willy.mdx` | Attic bug details; "reload it to remove the block"; "only mishap with JSW" | **VERIFIED** | *CRASH* issue 5, June 1984, p. 49 | CRASH also relayed that the effect "has been built into the game to make life more difficult", which the entry leaves out. |
| `vault/games/jet-set-willy.mdx` | "clever dicks… We're not publishing those yet" | **VERIFIED** | *CRASH* issue 5, June 1984, p. 49 |  |
| `vault/games/jet-set-willy.mdx` | "Gaping Pit" became "We Must Perform a Quirkafleeg" | **VERIFIED** | *CRASH* issue 5, June 1984, p. 49 |  |
| `vault/games/jet-set-willy.mdx` | Review quotes ("proscribed drugs", "dreadful Maria…", "Very sensibly…") | **VERIFIED** | *CRASH* issue 4, May 1984, p. 8 |  |
| `vault/companies/mastertronic.mdx` | founded 1983 by Frank Herman, Terry Medway, Martin Alper, Alan Sharam | **VERIFIED** | https://en.wikipedia.org/wiki/Mastertronic (web, Wikipedia as last resort): "In 1983 Martin Alper, Frank Herman … Terry Medway and Alan Sharam founded…". In print: Herman and Sharam pictured as Virgin Mastertronic in *Amiga Format* issue 4, November 1989, p. 6; Alper as MD in *Amstrad Action* issue 7, April 1986, p. 43 | No print source found names Medway. |
| `vault/companies/mastertronic.mdx` | C&VG July 1985: "audited figures of sales for two million games" in first 12 months | **VERIFIED** | C&VG issue 45, July 1985, p. 92 |  |
| `vault/companies/mastertronic.mdx` | Sinclair User Jan 1984: "that elusive extra 90 percent of British homes" | **VERIFIED** | SU issue 22, January 1984, p. 5 |  |
| `vault/companies/mastertronic.mdx` | Electronic Games Nov 1984: 7% of US homes vs 11% of British homes | **VERIFIED** | *Electronic Games* vol. 2 no. 16, November 1984, p. 8 |  |
| `vault/companies/mastertronic.mdx` | ACE Feb 1988: "swallowed up Melbourne House in February; eight months later, Virgin bought substantial minority interest" | **VERIFIED** | *ACE* issue 5, February 1988, p. 8 |  |
| `vault/companies/acornsoft.mdx` | founded: 1980 | **VERIFIED** | https://en.wikipedia.org/wiki/Acornsoft (web, Wikipedia): "established in late 1980" by Hauser, Curry and David Johnson-Davies | No print source found. No `ended` field, although Acornsoft stopped operating as a separate company in January 1986 (same page). |
| `vault/companies/acornsoft.mdx` | Elite prices: £14.95 cassette, £17.95 disc in charts; Acornsoft's own advert says £17.65 disc | **VERIFIED** | *Acorn User* issue 27, October 1984: advert p. 19, "£14.95 on cassette, or £17.65 on disc"; chart p. 157, "Acornsoft £14.95 (£17.95)"; Quinn review p. 167, "£14.95 (disc £17.95)" | The advert also gives £12.95 for the Electron, while the review says £14.95. That is a second disagreement the entry does not mention. |
| `vault/companies/acornsoft.mdx` | ACE March 1991: "Probably responsible for selling many BBCs… much imitated but… never surpassed" | **VERIFIED** | *ACE* issue 42, March 1991, p. 69 |  |
| `vault/companies/acornsoft.mdx` | ACE Sept 1989 reader: "original Acornsoft version of Elite would have died at birth" | **VERIFIED** | *ACE* issue 24, September 1989, p. 13 |  |
| `vault/companies/acornsoft.mdx` | ACE: Planetoid "the definitive Defender" | **VERIFIED** | *ACE* issue 42, March 1991, p. 69 |  |
| `vault/people/ian-logan.mdx` | 1981 ads: "the first person to disassemble the Sinclair ZX80 Monitor", co-author of ZX80 Companion | **VERIFIED** | C&VG issue 1, November 1981, p. 40 (Melbourne House ad; scan text "…emble the Sinclair ZX80 Monitor and was the co-author of the ZX80 COMPANION") |  |
| `vault/people/ian-logan.mdx` | ZX81 ROM Disassembly Part A £7.00; Understanding Your ZX81 ROM £8.95 | **VERIFIED** | SU issue 5, August 1982, p. 4 (ad coupon) | Part B's price is illegible in the scan ("U3,00"). |
| `vault/people/ian-logan.mdx` | Complete Spectrum ROM Disassembly (1983, £9.95, with O'Hara) | **VERIFIED** | Advertised in SU issue 12, March 1983, p. 8; £9.95 in *Your Spectrum* issue 2, March 1984, p. 77 | Your Sinclair 18 later lists it at £8.95. |
| `vault/people/ian-logan.mdx` | CRASH Nov 1985: Logan "actually wrote a part of the shadow ROM"; contract with Sinclair prevented more | **VERIFIED** | *CRASH* issue 22, November 1985, p. 119 |  |
| `vault/people/ian-logan.mdx` | CRASH: Understanding Your Spectrum and the disassembly "by far the best I've seen" | **VERIFIED** | *CRASH* issue 31, August 1986, p. 102 |  |
| `vault/techniques/scrolling.mdx` | C64: `$D016` bits 0-2 X scroll, `$D011` bits 0-2 Y scroll, 0-7 px | **VERIFIED** | MOS Technology, *6567 VIC-II Preliminary Datasheet*, registers $D011 and $D016; Christian Bauer, "The MOS 6567/6569 video controller (VIC-II) and its application in the Commodore 64", https://www.zimmers.net/cbmpics/cbm/c64/vic-ii.txt |  |
| `vault/techniques/scrolling.mdx` | NES: `$2005` X then Y; `$2000` bits 0-1 base nametable; two nametables in VRAM | **VERIFIED** | NESdev Wiki, PPU registers (PPUSCROLL, PPUCTRL) and nametables (2 KB CIRAM), https://www.nesdev.org/wiki/PPU_registers |  |
| `vault/techniques/scrolling.mdx` | Amiga: BPLCON1 fine scroll | **VERIFIED** | *Amiga Hardware Reference Manual*, 2nd edn (Commodore-Amiga/Addison-Wesley, 1989), BPLCON1 register |  |
| `vault/techniques/scrolling.mdx` | Codebase64/Cadaver quotes ("more than half of the rastertime", "usually too limiting", Turrican/Navy Seals, Butler's Commando) | **VERIFIED** | https://cadaver.github.io/rants/scroll.html (web; codebase64.org gave an SSL error): all four sentences present verbatim |  |
| `vault/games/dungeon-master.mdx` | released 1987; "December 1987 (Atari ST)" | **VERIFIED** | https://en.wikipedia.org/wiki/Dungeon_Master_(video_game) (web, Wikipedia): ST 15 Dec 1987; Amiga 1988 | The frontmatter `platforms` lists only the Amiga, although the entry says the ST was the original. |
| `vault/games/dungeon-master.mdx` | "The Atari ST original became the platform's best-selling game" | **VERIFIED** | Wikipedia (web): "the ST's best-selling game of all time". In print, *3DO Magazine* issue 1, August 1995, p. 47, says "a bestseller" | Relies on web and Wikipedia. |
| `vault/games/dungeon-master.mdx` | "Fourteen levels" | **VERIFIED** | Public-domain "DM-Maps… All 14 levels" disk listing, *AC's Guide to the Commodore Amiga*, Spring/Summer 1990, p. 172 | The source is a public-domain disk catalogue, which is weak. |
| `vault/companies/epyx.mdx` | founded 1978 as Automated Simulations; renamed Epyx 1983 | **VERIFIED** | https://en.wikipedia.org/wiki/Epyx (web, Wikipedia). In print, *80 Micro* issue 14, February 1981, p. 31, has "Epyx computer games from Automated Simulations" | The Epyx brand was in use from 1980–81, before the company rename. |
| `vault/companies/epyx.mdx` | ended 1993 | **VERIFIED** | Wikipedia (web): assets sold to Bridgestone Multimedia Group in 1993 |  |
| `vault/companies/epyx.mdx` | "Bankruptcy — 1989, restructured" | **VERIFIED** | Wikipedia (web): Chapter 11 by end of 1989 |  |
| `vault/companies/epyx.mdx` | Hardware: "Handy (Lynx) — sold to Atari" | **VERIFIED** | Wikipedia (web) |  |
| `vault/people/roberta-williams.mdx` | Mystery House (1980), "First graphic adventure" | **VERIFIED** | Period press says so: *Antic*, September 1985, p. 46 ("creators of the first graphics adventure games"); *The Australian Commodore and Amiga Review* vol. 8 no. 9, September 1991, p. 69 ("the first true graphic adventure") | A superlative, but a widely repeated one. |
| `vault/people/roberta-williams.mdx` | Co-founder of Sierra On-Line | **VERIFIED** | *Amiga Format* special issue 4 (1992), p. 95: "founded… by Ken and Roberta Williams in May 1980" |  |
| `vault/people/roberta-williams.mdx` | King's Quest I 1984, III 1986, V 1990, VI 1992; Phantasmagoria 1995 | **VERIFIED** | https://en.wikipedia.org/wiki/Roberta_Williams (web, Wikipedia) |  |
| `vault/magazines/acorn-user.mdx` | founded August 1982; issue 1 "official magazine… published by Addison-Wesley for Acorn Computers Limited" | **VERIFIED** | *Acorn User* issue 1, August 1982, p. 3 | Wikipedia dates the first issue July/August 1982. |
| `vault/magazines/acorn-user.mdx` | Oct 1984 issue carried both the Acornsoft Elite advert and Tony Quinn's review | **VERIFIED** | *Acorn User* issue 27, October 1984, p. 19 (advert) and p. 167 (review) | Quinn was also the magazine's editor (same issue, p. 4), which strengthens the entry's "in-house" point. |
| `vault/magazines/acorn-user.mdx` | Micro User "launched seven months later" | **VERIFIED** | *The Micro User* vol. 1 no. 1 (March 1983, seven months after August 1982) |  |
| `vault/genres/western-rpg.mdx` | "descend from tabletop Dungeons & Dragons" | **VERIFIED** | same Hartnell locator; *Amiga Joker* (Germany), December 1990, p. 104 ("Was Gary Gygax 1974 mit seinen 'Papier-Drachen' begann ... Die digitale AD&D-Welt von SSI") |  |
| `vault/genres/western-rpg.mdx` | Lineage: "1980s Ultima, Wizardry … 2000s Morrowind, KOTOR … 2010s Skyrim, Witcher 3" | **VERIFIED** | general knowledge, not checked title by title against sources | The decade groupings are accurate: Morrowind 2002, KOTOR 2003, Skyrim 2011, Witcher 3 2015. |
| `vault/games/hypersports.mdx` | `released: 1985` | **VERIFIED** | *CRASH* issue 20, September 1985, p. 70 (enters chart "16 (—) HYPERSPORTS Imagine") |  |
| `vault/games/hypersports.mdx` | "converted to the Spectrum by Jonathan 'Joffa' Smith for Imagine" | **VERIFIED** | *CRASH* issue 50, March 1988, p. 8 ("Smith's previous Ocean/Imagine credits include Green Beret and Smashes Cobra and Hypersports") |  |
| `vault/people/bob-yannes.mdx` | "As an engineer at MOS Technology, Bob Yannes designed the SID" | **VERIFIED** | *Compute!* issue 32, January 1983, p. 34 ("Yannes designed SID while an engineer for MOS Technology, which is owned by Commodore"). Also *Commodore Microcomputers* vol. 3 no. 2, April 1982, p. 107 (Yannes in the chip-design group photo under design manager Al Charpentier) |  |
| `vault/people/bob-yannes.mdx` | "co-founded Ensoniq … synthesizers and samplers like the Mirage" | **VERIFIED** | *Compute!* issue 56, January 1985, p. 36 ("Mirage designer Yannes claims that Ensoniq was able to keep the Mirage's costs down"); a secondary summary with no primary locator says he co-founded Ensoniq | The primary source confirms Yannes as Mirage designer at Ensoniq. The "co-founded" wording rests on that secondary summary. Compute! Jan 1983 says he first left Commodore to form "Peripheral Visions, Inc." |
| `vault/people/ed-boon.mdx` | `born: 1964` / "Born: 1964, Chicago" | **VERIFIED** | (web) https://en.wikipedia.org/wiki/Ed_Boon ("February 22, 1964, in Chicago, Illinois") | Web only (Wikipedia, last resort). No print source found. |
| `vault/people/ed-boon.mdx` | "co-created Mortal Kombat with John Tobias" | **VERIFIED** | (web) same page (Tobias lead designer, Boon lead programmer) |  |
| `vault/people/ed-boon.mdx` | Voice acting "Scorpion's 'Get over here!'" | **VERIFIED** | (web) same page (Boon voiced "Get over here!"; Guinness record as longest-serving video game voice actor) |  |
| `vault/people/ed-boon.mdx` | Series years MK 1992, MKII 1993, MK3 1995, MK4 1997 | **VERIFIED** | (web) same page |  |
| `vault/people/ed-boon.mdx` | "sparked congressional hearings" / "ESRB creation: Direct influence" | **VERIFIED** | (web) https://en.wikipedia.org/wiki/Entertainment_Software_Rating_Board (1993 Lieberman/Kohl hearings cited Mortal Kombat; ESRB established 16 Sep 1994 under that pressure) | Boon is still alive. The "Midway, then NetherRealm" career summary skips his start at Williams (pinball, ~1987–89), though Williams and Midway were related companies. |
| `vault/games/supreme-commander.mdx` | `released: 2007`; Gas Powered Games; designer Chris Taylor | **VERIFIED** | (web) https://en.wikipedia.org/wiki/Supreme_Commander_(video_game) (16 Feb 2007 EU / 20 Feb 2007 NA; GPG; Chris Taylor; publisher THQ) | Web only. It falls outside the period magazines consulted. |
| `vault/games/supreme-commander.mdx` | "Map sizes 80km × 80km" | **VERIFIED** | (web) same page ("up to 80 km x 80 km") |  |
| `vault/games/supreme-commander.mdx` | Strategic zoom out to the whole map | **VERIFIED** | (web) same page | "Revolutionary" and "transformed RTS interface design" are unsourced evaluation. |
| `vault/games/supreme-commander.mdx` | Legacy: Forged Alliance 2007, Supreme Commander 2 2010 | **VERIFIED** | (web) same page | `platforms` omits the 2008 Xbox 360 port (Aspyr/505). "Monkeylord … spider assault" is confirmed on the same page; I did not check the other experimentals. |
| `vault/games/wizball.mdx` | "Sinclair User gave the Spectrum version 10/10 in October 1987" | **VERIFIED** | SU issue 67, October 1987 (review: "Wizball is virtually flawless … A classic!"; p. 23: "classic now automatically gets ten") | The printed score is not legible in the scan. 10/10 follows from SU's stated rule that a Classic gets ten. |
| `vault/games/wizball.mdx` | "CRASH 92% the same month" | **VERIFIED** | *CRASH* issue 45, October 1987, p. 23 ("OVERALL 92%") |  |
| `vault/games/wizball.mdx` | Developer Sensible Software (Jon Hare, Chris Yates); publisher Ocean | **VERIFIED** | *Zzap!64* issue 23, March 1987, p. 50 (interview with Sensible, speakers "JH"/"CY", "What's it like working for Ocean?"); YS issue 20 (August 1987), p. 41, Fax Box ("Designed by Sensible Software", "Publisher Ocean") |  |
| `vault/games/wizball.mdx` | `released: 1987` (C64) | **VERIFIED** | *Zzap!64* issue 27, July 1987, p. 3 and review from p. 14 (C64 review, OVERALL 96%) |  |
| `vault/games/wizball.mdx` | Composer Martin Galway; soundtrack "frequently cited as one of the SID chip's finest moments" | **VERIFIED** | *ACE* issue 39, December 1990, p. 11 ("Martin Galway's work on [Wizball] … was undoubtedly the best audio heard on any C64 game") |  |
| `vault/games/wizball.mdx` | Two-player: second player controls the cat | **VERIFIED** | YS issue 20 (August 1987), p. 41 ("two players can play, one taking the part of the cat") | "Unusual for the era" is unsourced. Zzap names the cat "Nifta". The entry's "Catellite … a smaller ball" framing is loose. |
| `vault/games/dig-dug.mdx` | `released: 1982`; developer Namco | **VERIFIED** | (web) https://en.wikipedia.org/wiki/Dig_Dug (JP arcade 20 Feb 1982; NA April 1982). *Blip* vol. 1 no. 1, February 1983, p. 20 ("Atari manufactures and distributes the game") | Atari was the North American publisher, which the entry does not mention. |
| `vault/games/dig-dug.mdx` | Rocks "One enemy 1,000; Two 2,500" | **VERIFIED** | (web) blueskyrangers Intellivision manual ("1,000 for 1 monster, 2,500 for 2 monsters, 4,000 for 3") | The source is a home version manual. It matches the commonly cited arcade values. |
| `vault/games/dig-dug.mdx` | "Deeper enemies worth more" | **VERIFIED** | *Blip* vol. 1 no. 1, February 1983, p. 21 ("the deeper the level you're at when you zap a monster, the more points you'll get") |  |
| `vault/games/dig-dug.mdx` | "Walking music plays only when moving" | **VERIFIED** | (web) Wikipedia: composer Yuriko Keino made a short melody instead of a stepping sound | "Unusual" is unsourced. |
| `vault/games/dig-dug.mdx` | "Last enemy flees to surface" | **VERIFIED** | (web) Wikipedia (last enemy "attempts to escape … at the top of the stage") |  |
