# Vault entry candidates

Subjects the Vault mentions but has no entry for, with the entries that should link to each one once it exists. Reviewers add to this list as they work through batches (see [the Vault specification](specifications/vault.md#reviewing-existing-entries)). When an entry is written, add its links from the pages named here and remove its row.

A candidate earns an entry by helping a reader of an existing entry or lesson, not by being mentioned. Check that no entry already covers the subject under another name first. The website's `node scripts/vault-candidates.mjs` surfaces emphasised names across the whole Vault and is a useful source for new rows.

Paths are Vault entries (`category/slug`) in the website repository.

## Machines and hardware

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Sinclair Microdrive | hardware | The Spectrum's and QL's tape-loop storage, central to the QL's troubles | `companies/sinclair-research`, `systems/sinclair-ql`, `systems/sinclair-zx-spectrum`, `people/rick-dickinson` |
| ZX Interface 2 | hardware | Sinclair's joystick and ROM-cartridge interface; Ultimate's early games came out on cartridge for it | `companies/sinclair-research`, `companies/ultimate` |
| MK14 | systems | Science of Cambridge's kit micro, Sinclair's first computer product | `companies/sinclair-research`, `people/clive-sinclair`, `systems/sinclair-zx80` |
| Grundy NewBrain | systems | Designed at Sinclair Radionics, sold on, and released two years later | `companies/sinclair-research` |
| Acorn Atom | systems | Bug-Byte's and Acornsoft's first market | `companies/bug-byte`, `companies/acornsoft` |
| Currah Microspeech | hardware | The Spectrum speech add-on that *Atic Atac* and *Lunar Jetman* supported | `games/atic-atac` |
| Intellivision | systems | The 2600's main rival, closed by the crash | `phenomena/1983-crash`, `systems/atari-2600` |
| ColecoVision | systems | The site has the system ID but the Vault has no entry | `phenomena/1983-crash`, `hardware/z80` |
| Sinclair ZX Spectrum 128 | systems | The first Spectrum with the AY chip; a separate entry or a redirect to the Spectrum entry | `hardware/ay-3-8912`, `systems/sinclair-zx-spectrum` |
| Yamaha YM2149 | hardware | The AY-3-8910's licensed twin, used in the Atari ST and later Spectrums | `hardware/ay-3-8912` |
| Intel 8080 | hardware | The processor the Z80 was built to run the software of | `hardware/z80` |
| Oric | systems | Another British micro built round the AY chip | `hardware/ay-3-8912` |
| Commodore 128 | systems | The C64's successor with a C64 mode | `systems/commodore-64` |
| Commodore Max Machine (Ultimax) | systems | Shown beside the C64 at CES 1982 on the same chips | `systems/commodore-64` |
| Commodore SX-64 | systems | The portable C64 | `systems/commodore-64` |
| Famicom Disk System | hardware | Nintendo's Japanese disk add-on | `systems/nintendo-entertainment-system` |
| 10NES lockout chip | hardware | How Nintendo controlled NES cartridge publishing | `systems/nintendo-entertainment-system` |
| MMC5 | hardware | Nintendo's mapper with its own sound channels on the Famicom | `systems/nintendo-entertainment-system`, `hardware/mmc1` |
| Amiga CD32 | systems | Commodore's last machine | `systems/commodore-amiga` |
| HAM and Extra Half-Brite | techniques | The Amiga's two special display modes | `systems/commodore-amiga` |
| Microdigital TK90X and TK95 | systems | Brazilian Spectrum clones; the TK95 is the Next's starting point | `systems/zx-spectrum-next`, `systems/sinclair-zx-spectrum` |

## People

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Richard Altwasser | people | Designed the Spectrum's hardware and its ULA logic | `systems/sinclair-zx-spectrum`, `hardware/ula`, `companies/sinclair-research`, `people/steven-vickers` |
| John Grant | people | Co-wrote the Spectrum ROM with Steven Vickers, on contract from Nine Tiles | `people/steven-vickers`, `systems/sinclair-zx-spectrum`, `systems/sinclair-zx81`, `systems/sinclair-zx80` |
| Chris Curry | people | Co-founded Science of Cambridge with Sinclair, then Acorn | `companies/sinclair-research`, `people/clive-sinclair`, `companies/acorn-computers` |
| Jim Westwood | people | Designed the ZX80 and the ZX81's custom chip | `systems/sinclair-zx80`, `systems/sinclair-zx81`, `companies/sinclair-research`, `people/rick-dickinson` |
| Eugene Evans | people | The face of Imagine's publicity, later at Psygnosis; *Manic Miner*'s Eugene's Lair is named after him | `companies/imagine-software`, `companies/bug-byte`, `games/manic-miner`, `companies/psygnosis` |
| Bruce Everiss | people | Imagine's operations director and the main witness to its finances | `companies/imagine-software` |
| Mark Butler | people | Co-founded Imagine; David Lawson has an entry, Butler does not | `companies/imagine-software`, `companies/bug-byte`, `people/david-lawson` |
| Matt Bielby | people | *Your Sinclair* editor, 1989–91 | `magazines/your-sinclair`, `people/teresa-maughan` |
| Stuart Campbell | people | *Your Sinclair* reviewer from 1991; the old entry confused him with Phil South | `magazines/your-sinclair` |
| Linda Barker | people | *Your Sinclair* staff writer, then editor 1992–93 | `magazines/your-sinclair`, `people/teresa-maughan` |
| Phil South | people | *Your Sinclair* contributor from issue 1 and Tipshop host | `magazines/your-sinclair` |
| Jonathan Davies | people | Program Pitstop host and author of "The YS Story" | `magazines/your-sinclair` |
| Alan Dykes and Garth Sumpter | people | The last two *Sinclair User* editors | `magazines/sinclair-user`, `magazines/crash-magazine` |
| John Pemberton | people | Designed the ZX80's case | `systems/sinclair-zx80`, `people/rick-dickinson` |
| Phil Candy | people | Rick Dickinson's design partner; co-designed the Next's case | `people/rick-dickinson`, `systems/zx-spectrum-next` |
| Kevin Cox | people | *Your Sinclair*'s first editor | `magazines/your-sinclair`, `people/teresa-maughan` |
| Alan Maton | people | Co-founded Software Projects | `companies/software-projects`, `companies/bug-byte` |
| Masatoshi Shima | people | Co-designed the Z80 | `hardware/z80`, `companies/zilog` |
| Mike Follin | people | Spectrum programmer named in the AY entry | `hardware/ay-3-8912` |
| Irving Gould | people | Commodore's chairman and main shareholder | `systems/commodore-64`, `systems/commodore-amiga` |
| R. J. Mical | people | Wrote Intuition and told the Amiga Corporation story | `systems/commodore-amiga` |
| Carl Sassenrath | people | Designed the Amiga's multitasking Exec | `systems/commodore-amiga` |
| Dave Morse and Dave Needle | people | Amiga Corporation's founder and a chipset designer | `systems/commodore-amiga` |
| Karsten Obarski | people | Wrote Soundtracker | `systems/commodore-amiga`, `hardware/paula` |
| Henrique Olifiers | people | Led the Spectrum Next project and its three Kickstarters | `systems/zx-spectrum-next` |
| Victor Trucco and Fabio Belavenuto | people | Built the TBBlue board the Next grew from | `systems/zx-spectrum-next` |
| Garry Lancaster | people | Wrote NextZXOS | `systems/zx-spectrum-next` |

## Companies and organisations

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Nine Tiles | companies | The contractor that wrote Sinclair's BASIC ROMs | `people/steven-vickers`, `systems/sinclair-zx81`, `systems/sinclair-zx-spectrum`, `systems/sinclair-zx80` |
| Amstrad | companies | Bought Sinclair's computer business in 1986 and made the +2 and +3; the Vault has the CPC but not the company | `companies/sinclair-research`, `systems/sinclair-zx-spectrum`, `people/clive-sinclair`, `systems/amstrad-cpc` |
| Timex | companies | Sinclair's US partner (Timex Sinclair) and one of its 1985 creditors | `companies/sinclair-research`, `systems/sinclair-zx81`, `systems/sinclair-zx-spectrum` |
| Ferranti | companies | Made the uncommitted logic arrays in the ZX81 and Spectrum | `hardware/ula`, `systems/sinclair-zx81` |
| Sinclair Radionics | companies | Sinclair's earlier company; its collapse explains how Sinclair Research began | `companies/sinclair-research`, `people/clive-sinclair` |
| Jupiter Cantab | companies | Founded by ex-Sinclair engineers to make the Jupiter Ace | `companies/sinclair-research`, `systems/jupiter-ace` |
| Argus Press Software | companies | Bought Quicksilva and Bug-Byte and ran Bug-Byte as a budget label | `companies/bug-byte`, `companies/quicksilva` |
| Zilec Electronics | companies | The arcade company where the Stampers worked before Ultimate (*Blue Print*) | `people/stamper-brothers`, `companies/ultimate` |
| Dennis Publishing | companies | Published *Your Spectrum* and *Your Sinclair* until 1990 | `magazines/your-sinclair`, `magazines/your-spectrum` |
| ECC Publications | companies | Launched *Sinclair User* and *Sinclair Programs*; bought by EMAP in 1984 | `magazines/sinclair-user`, `magazines/sinclair-programs`, `companies/emap` |
| Mattel Electronics | companies | Made the Intellivision; closed in the crash | `phenomena/1983-crash`, `systems/nintendo-entertainment-system` |
| Coleco | companies | ColecoVision's maker | `phenomena/1983-crash` |
| General Instrument | companies | Made the AY-3-8910 family | `hardware/ay-3-8912` |
| DK'tronics | companies | Made Spectrum add-ons, including an AY sound box for the 48K | `hardware/ay-3-8912` |
| Tengen | companies | Atari Games' label that got round the NES lockout | `systems/nintendo-entertainment-system` |
| Escom | companies | Bought Commodore's assets in 1995 and restarted Amiga production | `systems/commodore-amiga` |
| Metacomco | companies | Supplied AmigaDOS (from TRIPOS) and QL software | `systems/commodore-amiga`, `systems/sinclair-ql` |

## Magazines

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Personal Computer Games | magazines | A key 1983–85 source for Manic Miner, Matthew Smith and the Liverpool scene | `games/manic-miner`, `people/matthew-smith` |
| Personal Computer News | magazines | Dated Manic Miner's release (August 1983 review) | `games/manic-miner`, `people/matthew-smith`, `systems/sinclair-zx81` |
| Big K | magazines | IPC's 1984–85 games monthly; the source of Bug-Byte's company history | `companies/bug-byte`, `companies/imagine-software` |
| Your Computer | magazines | Carried Bug-Byte's first adverts and much ZX80 coverage | `companies/bug-byte`, `systems/sinclair-zx80`, `systems/commodore-64` |
| BYTE | magazines | Reviewed the ZX80 in January 1981 | `systems/sinclair-zx80`, `hardware/z80`, `systems/commodore-amiga` |
| TV Gamer | magazines | 1984 source of the most detailed *Atic Atac* guide | `games/atic-atac` |
| Zero | magazines | Dennis's games magazine; Teresa Maughan was its publisher | `people/teresa-maughan` |
| Ahoy! and INFO | magazines | US Commodore magazines cited for C64 sales | `systems/commodore-64` |
| AmigaWorld | magazines | The main US Amiga magazine | `systems/commodore-amiga` |
| Amazing Computing | magazines | Long-running US Amiga magazine | `systems/commodore-amiga` |
| Next Magazine | magazines | SpecNext's own magazine | `systems/zx-spectrum-next` |

## Games

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Miner 2049er | games | The game the Manic Miner entry names as its model (as *Miner 49'er*) | `games/manic-miner` |
| Styx | games | Matthew Smith's first Bug-Byte release | `people/matthew-smith`, `games/manic-miner` |
| Alien 8 | games | Ultimate's second Filmation game, after Knight Lore | `companies/ultimate`, `games/knight-lore` |
| Nightshade | games | Ultimate's scrolling Filmation II game | `companies/ultimate` |
| Underwurlde | games | The second Sabreman game | `companies/ultimate`, `games/sabre-wulf` |
| Lunar Jetman | games | Jetpac's sequel | `companies/ultimate`, `games/jetpac` |
| Pentagram | games | The last Sabreman game (1986) | `games/sabre-wulf`, `games/knight-lore`, `companies/ultimate` |
| Gunfright | games | The last game the Stampers developed as a team | `companies/ultimate`, `people/stamper-brothers`, `games/knight-lore` |
| Wizards & Warriors | games | One of Rare's first NES games | `companies/rare` |
| Jet Set Willy II | games | The 1985 expanded version, with different credits and content | `games/jet-set-willy`, `companies/software-projects`, `people/matthew-smith` |
| Bandersnatch and Psyclapse | games | Imagine's unreleased megagames, whose path runs to *Brataccas* | `companies/imagine-software`, `companies/psygnosis`, `people/ian-hetherington` |
| Twin Kingdom Valley | games | Bug-Byte's cross-platform adventure hit | `companies/bug-byte` |
| Arcadia | games | Imagine's first hit | `companies/imagine-software`, `people/david-lawson` |
| Dragon's Lair (Spectrum) | games | Software Projects' licence of the laserdisc game | `companies/software-projects` |
| Avalon, Frankie Goes to Hollywood, Vectron, Dark Sceptre, Zombie Zombie | games | The period examples in attribute-aware design | `techniques/attribute-aware-design` |
| Gyromite | games | R.O.B.'s pack-in game | `systems/nintendo-entertainment-system`, `hardware/rob` |

## Culture, events and tools

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Golden Joystick Awards | culture | *Computer & Video Games*' readers' awards; Ultimate won three in 1985 | `games/knight-lore`, `companies/ultimate`, `companies/rare` |
| *Commercial Breaks*: Imagine | culture | The 1984 BBC documentary behind most retellings of Imagine's collapse | `companies/imagine-software`, `culture/liverpool-games-scene` |
| GEOS | tools | The C64's graphical desktop | `systems/commodore-64` |
| The Final Cartridge | tools | A C64 fast-loader cartridge cited for tape speeds | `systems/commodore-64` |
| Family BASIC | tools | Nintendo's BASIC for the Famicom | `systems/nintendo-entertainment-system` |
| AmigaOS, Kickstart and Workbench | tools | The Amiga's operating system | `systems/commodore-amiga` |
| CSpect | tools | A ZX Spectrum Next emulator | `systems/zx-spectrum-next` |

The *Your Sinclair* Smash Tapes and *Sinclair User* Megatape fit better as sections of `distribution/cover-tapes` than as entries.
