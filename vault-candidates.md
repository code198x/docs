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
| Intellivision | systems | The 2600's main rival, closed by the crash | `phenomena/1983-crash`, `systems/atari-2600`, `hardware/ay-3-8910`, `games/donkey-kong` |
| ColecoVision | systems | The site has the system ID but the Vault has no entry | `phenomena/1983-crash`, `hardware/z80`, `games/donkey-kong`, `culture/universal-vs-nintendo`, `people/minoru-arakawa` |
| Sinclair ZX Spectrum 128 | systems | The first Spectrum with the AY chip; a separate entry or a redirect to the Spectrum entry | `hardware/ay-3-8912`, `systems/sinclair-zx-spectrum` |
| Yamaha YM2149 | hardware | The AY-3-8910's licensed twin, used in the Atari ST and later Spectrums | `hardware/ay-3-8912`, `hardware/ay-3-8910` |
| Intel 8080 | hardware | The processor the Z80 was built to run the software of | `hardware/z80` |
| Oric | systems | Another British micro built round the AY chip | `hardware/ay-3-8912` |
| Commodore 128 | systems | The C64's successor with a C64 mode | `systems/commodore-64`, `hardware/6510`, `techniques/disk-fastloaders`, `hardware/1541-disk-drive` |
| Commodore Max Machine (Ultimax) | systems | Shown beside the C64 at CES 1982 on the same chips | `systems/commodore-64`, `hardware/6510` |
| Commodore SX-64 | systems | The portable C64 | `systems/commodore-64`, `hardware/cia` |
| Famicom Disk System | hardware | Nintendo's Japanese disk add-on, where *Zelda*, *Metroid* and *Kid Icarus* first appeared | `systems/nintendo-entertainment-system`, `hardware/apu`, `games/legend-of-zelda`, `games/metroid`, `games/kid-icarus`, `games/super-mario-bros`, `companies/nintendo-rd1`, `people/gunpei-yokoi`, `people/yoshio-sakamoto` |
| 10NES lockout chip | hardware | How Nintendo controlled NES cartridge publishing | `systems/nintendo-entertainment-system`, `phenomena/nintendo-seal` |
| MMC5 and MMC6 | hardware | Nintendo's later mappers: the MMC5 with its own sound channels, the MMC6 often mistaken for the MMC3 | `systems/nintendo-entertainment-system`, `hardware/mmc1`, `hardware/mmc3`, `hardware/apu`, `techniques/bank-switching`, `games/castlevania` |
| Amiga CD32 | systems | Commodore's last machine | `systems/commodore-amiga` |
| HAM and Extra Half-Brite | techniques | The Amiga's two special display modes | `systems/commodore-amiga`, `hardware/denise`, `hardware/amiga-chipset` |
| Microdigital TK90X and TK95 | systems | Brazilian Spectrum clones; the TK95 is the Next's starting point | `systems/zx-spectrum-next`, `systems/sinclair-zx-spectrum` |
| Commodore PET | systems | Commodore's first computer, built on the 6502 | `people/jack-tramiel`, `companies/mos-technology`, `companies/commodore`, `magazines/club-commodore`, `magazines/commodore-computer-club` |
| KIM-1 | systems | MOS Technology's 6502 development board | `companies/mos-technology` |
| MOS 6560/6561 VIC | hardware | The VIC-20's video and sound chip, the VIC-II's predecessor | `people/al-charpentier`, `people/bob-yannes`, `hardware/vic-ii` |
| TI-99/4A | systems | Texas Instruments' machine, driven out by the 1983 price war | `people/jack-tramiel` |
| Tatung Einstein | systems | A British micro with the AY-3-8910 | `hardware/ay-3-8910` |
| Fujitsu FM-7 | systems | Japanese micro with a 6809 and a Z80 | `hardware/6809` |
| Motorola 6800 | hardware | The 6809's predecessor, whose code its designers studied | `hardware/6809` |
| MC6883 SAM | hardware | The Dragon's and CoCo's memory and address chip | `hardware/6809`, `systems/tandy-coco`, `systems/dragon-32` |
| Konami VRC6 and Famicom expansion audio | hardware | Extra sound channels through the Famicom's cartridge slot | `hardware/apu`, `systems/nintendo-entertainment-system` |
| Commodore Datassette | hardware | The C64's tape deck, driven through the 6510's port | `hardware/6510` |
| Commodore serial bus (IEC) | hardware | The disk-drive bus the CIA drives | `hardware/cia` |
| TIA | hardware | The 2600's line-at-a-time video and sound chip, the counterpart to ANTIC | `systems/atari-2600`, `people/jay-miner`, `techniques/sprite-flicker`, `games/pac-man-atari-2600` |
| Atari 7800 | systems | Atari's 1984 console, held back by the takeover | `companies/atari`, `systems/atari-2600`, `phenomena/1983-crash` |
| Atari Jaguar | systems | Atari Corporation's last console, home of *Tempest 2000* | `companies/atari`, `people/jack-tramiel`, `people/jeff-minter`, `games/tempest-2000` |
| Atari Falcon030 | systems | The ST's successor and Atari's last computer | `magazines/st-format`, `systems/atari-st` |
| Virtual Boy | systems | Nintendo's 1995 3D console, whose failure ended Yokoi's time there | `people/gunpei-yokoi`, `companies/nintendo`, `companies/nintendo-rd1`, `systems/game-boy` |
| WonderSwan | systems | Bandai's 1999 handheld, designed by Yokoi's company Koto | `people/gunpei-yokoi`, `systems/game-boy` |
| Game Boy Color | systems | The Game Boy's 1998 colour successor with a double-speed processor | `systems/game-boy`, `systems/game-boy-advance` |
| Nintendo VS. System | systems | The arcade *Super Mario Bros.* British players met first | `games/super-mario-bros` |
| SPC700 and S-DSP | hardware | The SNES sound unit | `systems/super-nintendo`, `hardware/apu` |
| SG-1000 | systems | Sega's 1983 console, the start of the Master System's hardware line | `systems/sega-master-system`, `companies/sega`, `hardware/z80` |
| TMS9918 | hardware | Texas Instruments' video chip behind the TI-99/4A, ColecoVision, MSX and Master System | `techniques/sprite-flicker`, `systems/sega-master-system`, `systems/msx` |
| Master System VDP | hardware | Sega's enhanced TMS9918, a companion to the PPU and VIC-II | `systems/sega-master-system`, `techniques/sprite-flicker` |
| SN76489 | hardware | Texas Instruments' tone generator in the Master System, BBC Micro and Mega Drive | `systems/sega-master-system`, `systems/sega-mega-drive`, `systems/bbc-micro`, `hardware/ym2612` |
| SegaScope 3-D glasses | hardware | The Master System's shutter-glasses peripheral | `systems/sega-master-system` |
| Mega Drive VDP (315-5313) | hardware | The video chip whose sprite, colour and DMA limits the Mega Drive entry explains | `systems/sega-mega-drive`, `techniques/blast-processing` |
| Sega Mega-CD | hardware | The Mega Drive's CD add-on | `systems/sega-mega-drive`, `techniques/blast-processing` |
| Sega 32X | hardware | The Mega Drive's cartridge-slot upgrade | `systems/sega-mega-drive` |
| Commodore 1571 and 1581 | hardware | The burst-mode disk drives that followed the 1541 | `techniques/disk-fastloaders`, `hardware/1541-disk-drive` |
| MOS 6522 VIA | hardware | The chip whose shift-register bug made the Commodore serial bus slow | `techniques/disk-fastloaders`, `hardware/cia`, `systems/commodore-vic-20`, `hardware/1541-disk-drive` |
| sd2iec and 1541 Ultimate | hardware | Modern replacements for the 1541 | `techniques/disk-fastloaders`, `hardware/1541-disk-drive` |
| The Tube and second processors | hardware | The BBC Micro's co-processor interface | `systems/bbc-micro`, `companies/acorn-computers` |
| Econet | hardware | Acorn's classroom network | `systems/bbc-micro`, `companies/acorn-computers` |

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
| Matt Bielby | people | *Your Sinclair* editor, 1989–91, then *Amiga Power*'s launch editor | `magazines/your-sinclair`, `people/teresa-maughan`, `magazines/amiga-power` |
| Stuart Campbell | people | *Your Sinclair* reviewer from 1991 and *Amiga Power* deputy editor; the old entry confused him with Phil South | `magazines/your-sinclair`, `magazines/amiga-power` |
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
| Irving Gould | people | Commodore's chairman and main shareholder | `systems/commodore-64`, `systems/commodore-amiga`, `people/jack-tramiel` |
| R. J. Mical | people | Wrote Intuition and told the Amiga Corporation story | `systems/commodore-amiga` |
| Carl Sassenrath | people | Designed the Amiga's multitasking Exec | `systems/commodore-amiga` |
| Dave Morse and Dave Needle | people | Amiga Corporation's founder and a chipset designer | `systems/commodore-amiga` |
| Karsten Obarski | people | Wrote Soundtracker | `systems/commodore-amiga`, `hardware/paula`, `hardware/paula` |
| Henrique Olifiers | people | Led the Spectrum Next project and its three Kickstarters | `systems/zx-spectrum-next` |
| Victor Trucco and Fabio Belavenuto | people | Built the TBBlue board the Next grew from | `systems/zx-spectrum-next` |
| Garry Lancaster | people | Wrote NextZXOS | `systems/zx-spectrum-next` |
| Michael Tomczyk | people | Tramiel's assistant; wrote *The Home Computer Wars* | `people/jack-tramiel`, `people/bob-yannes` |
| Charles Winterble | people | MOS engineering manager named in the C64 design history | `people/al-charpentier`, `hardware/vic-ii` |
| Bill Mensch | people | 6502 co-designer | `companies/mos-technology` |
| Doug Smith | people | Wrote Lode Runner | `games/lode-runner` |
| Martin Walker | people | C64 programmer whose *ZZAP!64* diary covers multiplexers and SID bugs | `hardware/vic-ii`, `hardware/sid-chip`, `techniques/arpeggio` |
| Terry Ritter and Joel Boney | people | Designed the 6809 and wrote *BYTE*'s 1979 series on it | `hardware/6809` |
| Marko Mäkelä | people | Wrote the 1995 *C=Hacking* article on stable rasters | `techniques/stable-raster` |
| Shaun Southern | people | Magnetic Fields programmer quoted on the AGA blitter | `hardware/agnus`, `hardware/blitter` |
| Doug Neubauer | people | Designed POKEY and wrote *Star Raiders* | `games/star-raiders`, `systems/atari-8-bit`, `systems/atari-2600` |
| Steve Mayer | people | Credited in period sources as the 2600's main designer | `systems/atari-2600`, `systems/atari-8-bit`, `companies/atari` |
| Carol Shaw | people | Wrote *River Raid*; her 1983 interview explains how 2600 programming worked | `systems/atari-2600`, `companies/activision` |
| Alan Miller | people | Atari programmer who co-founded Activision and Accolade | `systems/atari-2600`, `companies/activision`, `culture/atari-vs-activision` |
| Ted Dabney | people | Co-founded Atari with Bushnell | `companies/atari`, `people/nolan-bushnell`, `games/pong` |
| James J. Morgan | people | Kassar's successor at Atari | `people/ray-kassar`, `phenomena/1983-crash`, `companies/atari` |
| Tod Frye | people | Programmed the 2600 *Pac-Man* | `games/pac-man-atari-2600`, `phenomena/1983-crash` |
| Mark Turmell | people | Sirius programmer whose 1982 interview explains the 2600 *Pac-Man*'s flicker | `techniques/sprite-flicker` |
| Derek Meakin | people | Founded Database Publications and Europress | `companies/europress`, `magazines/amiga-computing`, `magazines/micro-user`, `magazines/atari-st-user`, `magazines/amiga-action` |
| Matthew Uffindell | people | One of CRASH's first reviewers and the main source on who wrote as Lloyd Mangram | `people/lloyd-mangram`, `magazines/crash-magazine`, `people/roger-kean`, `companies/newsfield` |
| Tim Boone | people | Edited *C&VG* and then *Nintendo Magazine System* | `magazines/nintendo-magazine-system`, `magazines/computer-and-video-games` |
| Eugene Lacey | people | Edited *Commodore User* and *C&VG*, and consulted on *ACE* | `magazines/cu-amiga`, `magazines/ace-magazine`, `magazines/computer-and-video-games`, `companies/emap` |
| Terry Pratt and Tim Metcalfe | people | *C&VG*'s other 1980s editors | `magazines/computer-and-video-games`, `companies/emap` |
| Steve Cooke | people | Co-founded *ACE* and wrote its adventure pages throughout | `magazines/ace-magazine` |
| Bob Wade | people | Worked on *Personal Computer Games*, *Amstrad Action*, *ACE* and *Amiga Format* | `magazines/amiga-format`, `magazines/amstrad-action`, `magazines/ace-magazine` |
| Greg Ingham | people | Published *ST/Amiga Format*, later Future's chief executive | `magazines/st-format`, `magazines/amiga-format`, `companies/future-publishing`, `people/chris-anderson` |
| Mel Croucher | people | Wrote *Deus Ex Machina* and the AMOS manuals | `tools/amos` |
| Sandra Sharkey | people | Ran the first AMOS PD library and founded *Adventure Probe* | `tools/amos`, `distribution/licenseware` |
| Marc Haigh-Hutchinson | people | Wrote *Alien Highway* for Vortex | `companies/vortex-software`, `people/costa-panayi` |
| Geoff Brown | people | Founded CentreSoft and U.S. Gold, and part-owned Gremlin | `companies/us-gold`, `companies/centresoft`, `companies/gremlin-graphics`, `companies/kixx`, `systems/atari-8-bit` |
| Donald Campbell and John Prince | people | Founded Tiertex | `companies/tiertex` |
| Ken Kutaragi | people | Designed the SNES sound chip, then led the PlayStation | `systems/super-nintendo`, `companies/sony`, `systems/sony-playstation` |
| Satoru Okada | people | Directed *Kid Icarus* and was chief director of *Metroid* | `games/metroid`, `games/kid-icarus`, `systems/game-boy`, `people/gunpei-yokoi`, `companies/nintendo-rd1` |
| Hiroji Kiyotake and Makoto Kano | people | Samus's designer and *Metroid*'s scenario writer | `games/metroid` |
| Toru Osawa | people | Designed *Kid Icarus* | `games/kid-icarus`, `people/yoshio-sakamoto` |
| Takashi Tezuka | people | Miyamoto's co-designer on *Super Mario Bros.* and *Zelda* | `games/super-mario-bros`, `people/shigeru-miyamoto`, `games/legend-of-zelda`, `people/koji-kondo` |
| Howard Lincoln | people | Nintendo of America's lawyer in the Universal and *Tetris* cases, later its chairman | `culture/universal-vs-nintendo`, `games/donkey-kong`, `people/john-kirby`, `people/minoru-arakawa`, `people/hiroshi-yamauchi`, `phenomena/tetris-legal-battles`, `phenomena/nintendo-seal` |
| Howard Phillips | people | Nintendo of America's "game master" in court, later the face of *Nintendo Power* | `culture/universal-vs-nintendo`, `systems/nintendo-entertainment-system` |

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
| ECC Publications | companies | Launched *Sinclair User* and *Sinclair Programs*; bought by EMAP in 1984 | `magazines/sinclair-user`, `magazines/sinclair-programs`, `companies/emap`, `magazines/computer-and-video-games` |
| Mattel Electronics | companies | Made the Intellivision; closed in the crash | `phenomena/1983-crash`, `systems/nintendo-entertainment-system` |
| Coleco | companies | ColecoVision's maker, which settled with Universal over *Donkey Kong* | `phenomena/1983-crash`, `games/donkey-kong`, `culture/universal-vs-nintendo`, `people/minoru-arakawa` |
| General Instrument | companies | Made the AY-3-8910 family | `hardware/ay-3-8912`, `hardware/ay-3-8910` |
| DK'tronics | companies | Made Spectrum add-ons, including an AY sound box for the 48K | `hardware/ay-3-8912` |
| Escom | companies | Bought Commodore's assets in 1995 and restarted Amiga production | `systems/commodore-amiga`, `magazines/amiga-computing` |
| Metacomco | companies | Supplied AmigaDOS (from TRIPOS) and QL software | `systems/commodore-amiga`, `systems/sinclair-ql` |
| Ensoniq | companies | Founded by Charpentier and Yannes after Commodore | `people/al-charpentier`, `people/bob-yannes`, `hardware/sid-chip` |
| Texas Instruments | companies | Commodore's rival in the 1983 price war | `people/jack-tramiel` |
| Southwest Technical Products | companies | Advertised one of the first 6809 cards, in 1979 | `hardware/6809` |
| Maniacs of Noise | groups | Dutch game-music group named in the Paula entry | `hardware/paula` |
| Mandarin Software | companies | Europress's software label, which published STOS, AMOS and Level 9 | `companies/europress`, `tools/amos`, `tools/stos`, `companies/level-9`, `companies/rainbird`, `people/francois-lionet` |
| Jawx International | companies | The Paris company credited with STOS | `tools/stos`, `people/francois-lionet`, `tools/amos` |
| Paradox Group | companies | *Commodore User*'s first publisher, not the warez group | `magazines/cu-amiga`, `companies/emap` |
| Microelectrónica y Control | companies | Commodore's Spanish distributor and *Club Commodore*'s publisher | `magazines/club-commodore`, `culture/magazines-across-borders`, `companies/commodore` |
| Parker Brothers | companies | A major 2600 publisher with its own bank-switching scheme | `techniques/bank-switching`, `systems/atari-2600` |
| Western Technologies | companies | Designed the Vectrex hardware and games | `systems/vectrex`, `companies/gce` |
| Bandai | companies | Made the WonderSwan and the *Space Chaser* handheld | `people/gunpei-yokoi`, `hardware/d-pad` |
| CGL (Computer Games Ltd) | companies | Distributed Game & Watch in Britain | `systems/nintendo-game-and-watch` |
| Elorg | companies | The Soviet agency that licensed *Tetris* | `phenomena/tetris-legal-battles`, `people/minoru-arakawa`, `people/henk-rogers`, `people/alexey-pajitnov` |
| Access Software | companies | Made *Beach-Head*, U.S. Gold's first licence | `companies/us-gold`, `companies/centresoft` |
| GO! | companies | U.S. Gold's full-price label for *Street Fighter* and *Bionic Commando* | `companies/us-gold`, `companies/centresoft`, `companies/capcom` |
| Artic Computing | companies | Where Tiertex's founders and Charles Cecil started | `companies/tiertex`, `companies/us-gold`, `people/charles-cecil` |
| HesWare | companies | Jeff Minter's American publisher | `people/jeff-minter`, `companies/llamasoft` |
| Imagine Media | companies | Chris Anderson's American publisher; not the Bournemouth Imagine Publishing | `people/chris-anderson`, `companies/future-publishing` |

## Magazines

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Personal Computer Games | magazines | A key 1983–85 source for Manic Miner and the Liverpool scene, and where the *ZZAP!64*, *Amstrad Action* and *ACE* teams started | `games/manic-miner`, `people/matthew-smith`, `people/chris-anderson`, `magazines/ace-magazine`, `magazines/amstrad-action`, `magazines/zzap-64`, `companies/future-publishing` |
| Personal Computer News | magazines | Dated Manic Miner's release (August 1983 review) | `games/manic-miner`, `people/matthew-smith`, `systems/sinclair-zx81` |
| Big K | magazines | IPC's 1984–85 games monthly; the source of Bug-Byte's company history | `companies/bug-byte`, `companies/imagine-software` |
| Your Computer | magazines | Carried Bug-Byte's first adverts and much ZX80 coverage | `companies/bug-byte`, `systems/sinclair-zx80`, `systems/commodore-64` |
| BYTE | magazines | Reviewed the ZX80 in January 1981 | `systems/sinclair-zx80`, `hardware/z80`, `systems/commodore-amiga` |
| TV Gamer | magazines | 1984 source of the most detailed *Atic Atac* guide | `games/atic-atac` |
| Zero | magazines | Dennis's games magazine; Teresa Maughan was its publisher | `people/teresa-maughan` |
| Ahoy! and INFO | magazines | US Commodore magazines cited for C64 sales and fast loaders | `systems/commodore-64`, `techniques/disk-fastloaders` |
| AmigaWorld | magazines | The main US Amiga magazine, whose readers became *Amiga Computing*'s US edition | `systems/commodore-amiga`, `magazines/amiga-computing`, `culture/magazines-across-borders`, `companies/idg` |
| Amazing Computing | magazines | Long-running US Amiga magazine | `systems/commodore-amiga` |
| Next Magazine | magazines | SpecNext's own magazine | `systems/zx-spectrum-next` |
| Commodore Disk User | magazines | Cited on border sprites and fast loaders | `hardware/vic-ii`, `techniques/disk-fastloaders` |
| The Transactor | magazines | Canadian Commodore magazine cited on the CIA's clock | `hardware/cia` |
| Electron User | magazines | Database's Acorn Electron title, begun inside *The Micro User* | `magazines/micro-user`, `companies/europress` |
| Atari User | magazines | Database's 8-bit Atari monthly and *Atari ST User*'s first home | `magazines/atari-st-user`, `companies/europress`, `systems/atari-8-bit` |
| ST Action | magazines | Europress's ST games magazine, *Amiga Action*'s older sister | `magazines/amiga-action`, `companies/europress`, `magazines/atari-st-user` |
| ST Review | magazines | One of the last two glossy ST magazines | `magazines/atari-st-user`, `magazines/st-format`, `magazines/ace-magazine`, `companies/emap` |
| Computing with the Amstrad | magazines | Database's CPC title, which absorbed *Amtix!* | `magazines/amtix`, `companies/europress`, `magazines/amstrad-action`, `systems/amstrad-cpc` |
| Commodore Force | magazines | *ZZAP!64*'s Europress successor, where Lloyd Mangram reappeared | `magazines/zzap-64`, `companies/europress`, `companies/newsfield`, `people/lloyd-mangram` |
| LM | magazines | Newsfield's 1986–87 general-interest magazine, named after Lloyd Mangram | `people/lloyd-mangram`, `companies/newsfield` |
| Mean Machines Sega | magazines | The Sega half of the 1992 *Mean Machines* split | `magazines/mean-machines`, `magazines/nintendo-magazine-system` |
| ST/Amiga Format | magazines | The 1988–89 parent of both Formats | `magazines/st-format`, `magazines/amiga-format`, `companies/future-publishing` |
| Edge | magazines | Future's multi-format magazine from 1993, cited across the Vault | `companies/future-publishing`, `people/chris-anderson`, `hardware/d-pad`, `techniques/bank-switching`, `systems/atari-2600` |
| PC Gamer | magazines | Future's PC games magazine in Britain and America | `companies/future-publishing`, `magazines/pc-player` |
| New Computer Express and Sega Power | magazines | Future's weekly news title and its Sega magazine | `companies/future-publishing` |
| Next Generation | magazines | Chris Anderson's American games magazine | `people/chris-anderson`, `companies/future-publishing` |
| Electronic Games | magazines | The US games magazine cited most often across the Vault | `hardware/d-pad`, `techniques/bank-switching`, `systems/atari-2600`, `games/pac-man-atari-2600`, `systems/vectrex`, `systems/sega-mega-drive`, `techniques/sprite-flicker` |
| Electronic Fun with Computers & Games, JoyStik, Video Games and Sega Visions | magazines | US period magazines cited on the 2600, Vectrex and Mega Drive | `games/pac-man-atari-2600`, `systems/vectrex`, `systems/sega-mega-drive`, `techniques/sprite-flicker` |

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
| Championship Lode Runner | games | The 1984 sequel | `games/lode-runner` |
| Space Panic | games | Arcade climbing game named in the Lode Runner entry | `games/lode-runner` |
| Menace | games | Dave Jones's Amiga shooter; the blitter entry uses his account of it | `hardware/blitter`, `hardware/denise` |
| F/A-18 Interceptor | games | Amiga flight game discussed in the blitter entry | `hardware/blitter` |
| Mighty Final Fight | games | NES example of sprite flicker | `hardware/ppu` |
| Morpheus | games | C64 game cited in the VIC-II entry | `hardware/vic-ii` |
| Sinistar and Stargate | games | Williams arcade games named in the 6809 entry | `hardware/6809` |
| Guardian (Amiga) | games | Mark Sibly's game with a copper sky | `hardware/copper` |
| Blood Money, Agony, Wonder Dog, Pioneer Plague | games | Amiga games the Denise and Agnus entries use as examples | `hardware/denise`, `hardware/agnus` |
| Highway Encounter | games | Vortex's highest-rated game | `companies/vortex-software`, `people/costa-panayi` |
| Deflektor | games | The first Vortex game Gremlin published | `companies/vortex-software`, `companies/gremlin-graphics`, `people/costa-panayi` |
| Computer Space | games | Bushnell's first arcade game, made before Atari existed | `companies/atari`, `people/nolan-bushnell` |
| Raiders of the Lost Ark (Atari 2600) | games | Warshaw's game before *E.T.* | `games/et-the-extra-terrestrial`, `people/howard-scott-warshaw` |
| Yars' Revenge | games | Warshaw's first game, named after Kassar backwards | `people/howard-scott-warshaw`, `games/et-the-extra-terrestrial`, `people/ray-kassar` |
| Ms. Pac-Man (Atari 2600) | games | The 8K follow-up that fixed the first cartridge's problems | `games/pac-man-atari-2600`, `techniques/sprite-flicker` |
| Robot Tank and Decathlon | games | Activision's self-switching 2600 cartridges | `techniques/bank-switching`, `companies/activision`, `systems/atari-2600` |
| Mine Storm | games | The Vectrex's built-in game | `systems/vectrex` |
| Radar Scope | games | The failed arcade game that became *Donkey Kong* | `games/donkey-kong`, `people/shigeru-miyamoto`, `people/minoru-arakawa` |
| Donkey Kong Jr. | games | The sequel with the roles swapped | `games/donkey-kong`, `games/super-mario-bros`, `systems/nintendo-game-and-watch` |
| Zelda II: The Adventure of Link | games | *Zelda*'s direct sequel | `games/legend-of-zelda` |
| Famicom Detective Club | games | Sakamoto's adventures, which set his directing style | `people/yoshio-sakamoto` |
| Metroid Fusion and Metroid: Zero Mission | games | The Game Boy Advance *Metroid* games | `people/yoshio-sakamoto`, `games/metroid`, `games/super-metroid` |
| WarioWare | games | Nintendo's microgame series, produced by Sakamoto | `people/yoshio-sakamoto`, `games/wario-land` |
| Super Mario World | games | The SNES launch game | `systems/super-nintendo` |
| Pilotwings | games | The first cartridge with an extra chip, and a Mode 7 showcase | `systems/super-nintendo`, `techniques/mode-7` |
| The Great Giana Sisters | games | Rainbow Arts' game, withdrawn under pressure from Nintendo | `games/super-mario-bros`, `companies/nintendo` |
| Beach-Head | games | U.S. Gold's first licence | `companies/us-gold`, `companies/centresoft` |
| World Cup Carnival | games | The period press's standard example of a cynical licence | `companies/us-gold`, `magazines/ace-magazine` |
| Thunder Blade | games | Sega's coin-op and a well-documented Spectrum conversion | `companies/tiertex`, `companies/us-gold`, `culture/arcade-conversion` |
| 720° | games | Atari's skateboarding coin-op, Tiertex's first job | `companies/tiertex`, `companies/us-gold` |
| Human Killing Machine | games | Tiertex's notorious *Street Fighter* follow-up | `companies/tiertex`, `games/street-fighter`, `culture/bad-ports` |
| Kick Off | games | Anco's football game, *Amiga Format*'s first Format Gold | `magazines/amiga-format`, `companies/anco` |
| Bombuzal | games | *Amiga Power*'s first cover-disk game | `magazines/amiga-power` |
| Jetstrike | games | A commercial Amiga game written in AMOS | `tools/amos` |
| Scorched Tanks | games | The best-known AMOS shareware game | `tools/amos`, `people/francois-lionet` |
| Kong Strikes Back | games | Galway's claimed first fast-arpeggio chords | `techniques/arpeggio`, `people/martin-galway` |
| Gridrunner | games | Minter's first hit | `people/jeff-minter`, `companies/llamasoft`, `systems/commodore-vic-20` |
| Iridis Alpha | games | Minter's C64 shoot-'em-up | `people/jeff-minter`, `companies/llamasoft`, `systems/commodore-64` |

## Culture, events and tools

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Golden Joystick Awards | culture | *Computer & Video Games*' readers' awards; Ultimate won three in 1985 | `games/knight-lore`, `companies/ultimate`, `companies/rare`, `magazines/computer-and-video-games`, `games/jetpac`, `games/manic-miner`, `games/the-hobbit` |
| *Commercial Breaks*: Imagine | culture | The 1984 BBC documentary behind most retellings of Imagine's collapse | `companies/imagine-software`, `culture/liverpool-games-scene` |
| GEOS | tools | The C64's graphical desktop | `systems/commodore-64` |
| The Final Cartridge | tools | The Dutch C64 utility and fast-loader cartridge, sold across Europe | `systems/commodore-64`, `techniques/disk-fastloaders`, `techniques/fast-loader`, `hardware/cartridge` |
| Family BASIC | tools | Nintendo's BASIC for the Famicom | `systems/nintendo-entertainment-system` |
| AmigaOS, Kickstart and Workbench | tools | The Amiga's operating system | `systems/commodore-amiga` |
| CSpect | tools | A ZX Spectrum Next emulator | `systems/zx-spectrum-next` |
| Amiga Hardware Reference Manual | tools | The primary source for Amiga chipset entries | `hardware/blitter`, `systems/commodore-amiga` |
| Mapping the Commodore 64 | tools | The register reference the VIC-II entry follows | `hardware/vic-ii`, `hardware/sid-chip`, `hardware/6510`, `hardware/cia` |
| Christian Bauer's VIC-II article | tools | The standard technical description of the VIC-II | `hardware/vic-ii`, `techniques/stable-raster` |
| Badlines | techniques | The VIC-II's stolen cycles | `hardware/vic-ii`, `systems/commodore-64` |
| Sample playback through the SID volume register | techniques | How C64 games played speech and drums | `hardware/sid-chip` |
| Sprite 0 hit and nametable mirroring | techniques | Two NES PPU techniques the PPU entry introduces | `hardware/ppu` |
| Bitplanes | techniques | The Amiga's planar display, behind every blit | `hardware/blitter`, `systems/commodore-amiga` |
| OS-9 | tools | Microware's 6809 operating system | `hardware/6809`, `systems/tandy-coco` |
| CyberSound and AHI | tools | The 14-bit Paula playback method and the Amiga audio system that used it | `hardware/paula` |
| Amiga disk format (MFM) | techniques | How the Amiga stores tracks, decoded in software | `hardware/paula` |
| Copper bars | techniques | The copper's best-known effect | `hardware/copper` |
| Dual playfield | techniques | Denise's two independent playfields | `hardware/denise` |
| Undocumented 6502 opcodes | techniques | The instructions the 6510 executes but MOS never listed | `hardware/6510`, `hardware/6502` |
| Fun School | tools | Europress's best-known educational series, and the reason Hasbro bought it | `companies/europress` |
| Mini Office | tools | Database's best-selling 8-bit business suite | `companies/europress` |
| Shoot-'Em-Up Construction Kit | tools | The game creator reviewers compared STOS and Klik & Play with | `tools/stos`, `tools/amos`, `companies/clickteam`, `tools/game-maker`, `tools/3d-construction-kit` |
| AOZ Studio | tools | Lionet's successor to AMOS | `people/francois-lionet`, `tools/amos` |
| OctaMED | tools | The Amiga tracker most British hobbyists met | `techniques/arpeggio`, `tools/protracker`, `hardware/paula` |
| BBC BASIC | tools | The BBC Micro's BASIC, with named procedures and an inline assembler | `systems/bbc-micro`, `systems/acorn-archimedes` |
| Psychedelia and the light synthesiser | tools | Minter's non-game programs | `people/jeff-minter`, `companies/llamasoft` |
| JiffyDOS | tools | The longest-lived C64 speed-up ROM | `techniques/disk-fastloaders`, `techniques/fast-loader`, `hardware/1541-disk-drive` |
| Epyx Fast Load | tools | The best-known US fast-load cartridge | `techniques/disk-fastloaders`, `techniques/fast-loader` |
| Dolphin DOS | tools | The best-known parallel-cable speed-up for the 1541 | `techniques/disk-fastloaders`, `hardware/1541-disk-drive` |
| Krill's loader, Spindle and Bitfire | tools | Today's demoscene disk loaders | `techniques/disk-fastloaders`, `techniques/fast-loader` |
| GCR (group code recording) | techniques | How the 1541 encodes its disks, and what copy protection played with | `techniques/disk-fastloaders`, `hardware/1541-disk-drive`, `techniques/disk-protection`, `hardware/paula` |
| HDMA | techniques | The per-scanline trick behind Mode 7 perspective | `systems/super-nintendo`, `techniques/mode-7` |
| Radio teletype (RTTY) | techniques | A common early-1980s amateur-radio project on home computers | `magazines/club-commodore`, `systems/commodore-vic-20` |
| Nintendo licensing and the 1991 FTC price case | phenomena | How Nintendo's control of retail prices drew a 1991 US government settlement | `phenomena/nintendo-seal`, `people/john-kirby` |

The *Your Sinclair* Smash Tapes and *Sinclair User* Megatape fit better as sections of `distribution/cover-tapes` than as entries.
