# Vault entry candidates

Subjects the Vault mentions but has no entry for, with the entries that should link to each one once it exists. Reviewers add to this list as they work through batches (see [the Vault specification](specifications/vault.md#reviewing-existing-entries)). When an entry is written, add its links from the pages named here and remove its row.

A candidate earns an entry by helping a reader of an existing entry or lesson, not by being mentioned. Check that no entry already covers the subject under another name first. The website's `node scripts/vault-candidates.mjs` surfaces emphasised names across the whole Vault and is a useful source for new rows.

Paths are Vault entries (`category/slug`) in the website repository.

## Machines and hardware

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Sinclair Microdrive | hardware | The Spectrum's and QL's tape-loop storage, central to the QL's troubles | `companies/sinclair-research`, `systems/sinclair-ql`, `systems/sinclair-zx-spectrum`, `people/rick-dickinson` |
| ZX Interface 2 | hardware | Sinclair's joystick and ROM-cartridge interface; Ultimate's early games came out on cartridge for it | `companies/sinclair-research`, `companies/ultimate`, `games/jetpac`, `systems/sinclair-zx-spectrum`, `techniques/copy-protection` |
| MK14 | systems | Science of Cambridge's kit micro, Sinclair's first computer product | `companies/sinclair-research`, `people/clive-sinclair`, `systems/sinclair-zx80` |
| Grundy NewBrain | systems | Designed at Sinclair Radionics, sold on, and released two years later | `companies/sinclair-research`, `phenomena/bbc-computer-literacy-project`, `companies/acorn-computers` |
| Acorn Atom | systems | Bug-Byte's and Acornsoft's first market | `companies/bug-byte`, `companies/acornsoft`, `hardware/mc6847`, `companies/acorn-computers` |
| Currah Microspeech | hardware | The Spectrum speech add-on that *Atic Atac* and *Lunar Jetman* supported | `games/atic-atac` |
| Sinclair ZX Spectrum 128 | systems | The first Spectrum with the AY chip; a separate entry or a redirect to the Spectrum entry | `hardware/ay-3-8912`, `systems/sinclair-zx-spectrum`, `techniques/double-buffering`, `techniques/screen-memory`, `techniques/bank-switching`, `techniques/interrupt-driven-music`, `people/david-whittaker`, `people/tim-follin` |
| Yamaha YM2149 | hardware | The AY-3-8910's licensed twin, used in the Atari ST and later Spectrums | `hardware/ay-3-8912`, `hardware/ay-3-8910` |
| Intel 8080 | hardware | The processor the Z80 was built to run the software of | `hardware/z80` |
| Oric | systems | Another British micro built round the AY chip | `hardware/ay-3-8912`, `people/eric-chahi` |
| Commodore 128 | systems | The C64's successor with a C64 mode | `systems/commodore-64`, `hardware/6510`, `techniques/disk-fastloaders`, `hardware/1541-disk-drive`, `emulators/vice`, `systems/commodore-vic-20`, `techniques/kernal-io` |
| Commodore Max Machine (Ultimax) | systems | Shown beside the C64 at CES 1982 on the same chips | `systems/commodore-64`, `hardware/6510` |
| Commodore SX-64 | systems | The portable C64 | `systems/commodore-64`, `hardware/cia` |
| 10NES lockout chip | hardware | How Nintendo controlled NES cartridge publishing | `systems/nintendo-entertainment-system`, `phenomena/nintendo-seal`, `hardware/cartridge`, `techniques/copy-protection` |
| Amiga CD32 | systems | Commodore's last machine | `systems/commodore-amiga`, `hardware/cd-rom`, `people/mark-sibly`, `companies/acid-software`, `games/skidmarks`, `people/rob-northen`, `games/beneath-a-steel-sky`, `companies/frontier-developments`, `companies/commodore` |
| HAM and Extra Half-Brite | techniques | The Amiga's two special display modes | `systems/commodore-amiga`, `hardware/denise`, `hardware/amiga-chipset`, `people/eric-graham`, `culture/the-juggler` |
| Microdigital TK90X and TK95 | systems | Brazilian Spectrum clones; the TK95 is the Next's starting point | `systems/zx-spectrum-next`, `systems/sinclair-zx-spectrum`, `culture/brazilian-market-reserve`, `people/clive-sinclair`, `culture/spectrum-clones` |
| Commodore PET | systems | Commodore's first computer, built on the 6502 | `people/jack-tramiel`, `companies/mos-technology`, `companies/commodore`, `magazines/club-commodore`, `magazines/commodore-computer-club`, `people/mike-singleton`, `emulators/vice`, `systems/commodore-64`, `systems/commodore-vic-20`, `people/david-simons`, `tools/simons-basic`, `companies/microsoft`, `people/chuck-peddle`, `techniques/basic-v2`, `techniques/kernal-io`, `magazines/compute-magazine`, `people/jim-butterfield`, `distribution/type-in-listings`, `games/colossal-cave-adventure`, `companies/audiogenic` |
| KIM-1 | systems | MOS Technology's 6502 development board | `companies/mos-technology`, `people/jim-butterfield`, `people/chuck-peddle`, `hardware/6502` |
| MOS 6560/6561 VIC | hardware | The VIC-20's video and sound chip, the VIC-II's predecessor | `people/al-charpentier`, `people/bob-yannes`, `hardware/vic-ii` |
| TI-99/4A | systems | Texas Instruments' machine, driven out by the 1983 price war | `people/jack-tramiel`, `techniques/sprites`, `techniques/sprite-flicker`, `companies/milton-bradley` |
| Tatung Einstein | systems | A British micro with the AY-3-8910 | `hardware/ay-3-8910`, `people/david-whittaker` |
| Fujitsu FM-7 | systems | Japanese micro with a 6809 and a Z80 | `hardware/6809` |
| Motorola 6800 | hardware | The 6809's predecessor, whose code its designers studied | `hardware/6809` |
| MC6883 SAM | hardware | The Dragon's and CoCo's memory and address chip | `hardware/6809`, `systems/tandy-coco`, `systems/dragon-32`, `hardware/mc6847`, `systems/dragon-64` |
| Konami VRC6 and Famicom expansion audio | hardware | Extra sound channels through the Famicom's cartridge slot | `hardware/apu`, `systems/nintendo-entertainment-system`, `hardware/mmc5`, `hardware/famicom-disk-system`, `hardware/vrc2`, `tools/famitracker`, `companies/konami` |
| Commodore Datassette | hardware | The C64's tape deck, driven through the 6510's port | `hardware/6510`, `techniques/kernal-io`, `techniques/cassette-loading` |
| Commodore serial bus (IEC) | hardware | The disk-drive bus the CIA drives | `hardware/cia` |
| TIA | hardware | The 2600's line-at-a-time video and sound chip, the counterpart to ANTIC | `systems/atari-2600`, `people/jay-miner`, `techniques/sprite-flicker`, `games/pac-man-atari-2600`, `techniques/sprites` |
| Atari 7800 | systems | Atari's 1984 console, held back by the takeover | `companies/atari`, `systems/atari-2600`, `phenomena/1983-crash`, `games/pole-position`, `games/xevious`, `games/centipede`, `games/galaga` |
| Atari Jaguar | systems | Atari Corporation's last console, home of *Tempest 2000* | `companies/atari`, `people/jack-tramiel`, `people/jeff-minter`, `games/tempest-2000`, `systems/atari-lynx`, `techniques/sprite-scaling`, `games/theme-park`, `games/tempest`, `companies/rebellion` |
| Atari Falcon030 | systems | The ST's successor and Atari's last computer | `magazines/st-format`, `systems/atari-st`, `demos/starstruck`, `demos/ocean-machine`, `groups/the-black-lotus` |
| Virtual Boy | systems | Nintendo's 1995 3D console, whose failure ended Yokoi's time there | `people/gunpei-yokoi`, `companies/nintendo`, `companies/nintendo-rd1`, `systems/game-boy`, `companies/intelligent-systems` |
| WonderSwan | systems | Bandai's 1999 handheld, designed by Yokoi's company Koto | `people/gunpei-yokoi`, `systems/game-boy`, `systems/neo-geo-pocket` |
| Game Boy Color | systems | The Game Boy's 1998 colour successor with a double-speed processor | `systems/game-boy`, `systems/game-boy-advance`, `systems/neo-geo-pocket`, `systems/sega-game-gear`, `games/perfect-dark` |
| Nintendo VS. System | systems | The arcade *Super Mario Bros.* British players met first | `games/super-mario-bros`, `games/duck-hunt`, `hardware/nes-zapper`, `systems/nintendo-entertainment-system`, `games/balloon-fight` |
| SPC700 and S-DSP | hardware | The SNES sound unit | `systems/super-nintendo`, `hardware/apu`, `people/nobuo-uematsu`, `games/chrono-trigger` |
| SG-1000 | systems | Sega's 1983 console, the start of the Master System's hardware line | `systems/sega-master-system`, `companies/sega`, `hardware/z80`, `systems/colecovision`, `people/yu-suzuki`, `games/galaga`, `games/choplifter` |
| TMS9918 | hardware | Texas Instruments' video chip behind the TI-99/4A, ColecoVision, MSX and Master System | `techniques/sprite-flicker`, `systems/sega-master-system`, `systems/msx`, `systems/colecovision`, `techniques/sprites` |
| Master System VDP | hardware | Sega's enhanced TMS9918, a companion to the PPU and VIC-II | `systems/sega-master-system`, `techniques/sprite-flicker`, `techniques/hardware-scroll` |
| SN76489 | hardware | Texas Instruments' tone generator in the Master System, BBC Micro and Mega Drive | `systems/sega-master-system`, `systems/sega-mega-drive`, `systems/bbc-micro`, `hardware/ym2612`, `systems/colecovision`, `tools/deflemask`, `people/matt-furniss` |
| SegaScope 3-D glasses | hardware | The Master System's shutter-glasses peripheral | `systems/sega-master-system`, `people/mark-cerny`, `hardware/light-gun` |
| Mega Drive VDP (315-5313) | hardware | The video chip whose sprite, colour and DMA limits the Mega Drive entry explains | `systems/sega-mega-drive`, `techniques/blast-processing` |
| Sega Mega-CD | hardware | The Mega Drive's CD add-on | `systems/sega-mega-drive`, `techniques/blast-processing`, `hardware/cd-rom`, `techniques/sprite-scaling`, `games/final-fight`, `techniques/fmv`, `games/wing-commander`, `companies/sega`, `companies/core-design` |
| Sega 32X | hardware | The Mega Drive's cartridge-slot upgrade | `systems/sega-mega-drive`, `games/space-harrier`, `games/virtua-fighter` |
| Commodore 1571 and 1581 | hardware | The burst-mode disk drives that followed the 1541 | `techniques/disk-fastloaders`, `hardware/1541-disk-drive`, `hardware/action-replay` |
| MOS 6522 VIA | hardware | The chip whose shift-register bug made the Commodore serial bus slow | `techniques/disk-fastloaders`, `hardware/cia`, `systems/commodore-vic-20`, `hardware/1541-disk-drive` |
| sd2iec and 1541 Ultimate | hardware | Modern replacements for the 1541 | `techniques/disk-fastloaders`, `hardware/1541-disk-drive` |
| The Tube and second processors | hardware | The BBC Micro's co-processor interface | `systems/bbc-micro`, `companies/acorn-computers` |
| Econet | hardware | Acorn's classroom network | `systems/bbc-micro`, `companies/acorn-computers` |
| Acorn Electron | systems | Acorn's cut-down BBC Micro, Acornsoft's second machine and a home for *Elite* | `companies/acornsoft`, `people/david-braben`, `people/ian-bell`, `games/elite`, `companies/acorn-computers`, `games/repton`, `companies/superior-software` |
| 3DO Interactive Multiplayer | systems | Trip Hawkins's 1993 console, built under licence by other companies | `people/trip-hawkins`, `companies/electronic-arts`, `systems/sega-saturn`, `hardware/cd-rom`, `companies/elite-systems`, `games/theme-park`, `people/mark-cerny` |
| CP System | hardware | Capcom's standard arcade board from 1988, behind *Final Fight* and *Street Fighter II* | `companies/capcom`, `games/street-fighter-ii`, `games/strider`, `games/final-fight`, `hardware/arcade-hardware`, `techniques/copy-protection`, `games/ghouls-n-ghosts` |
| Expert cartridge and back-up cartridges | hardware | The freezer cartridges at the centre of the 1988 argument over copy protection | `communities/cracking-scene`, `techniques/copy-protection`, `techniques/trainers`, `hardware/action-replay` |
| 64DD | hardware | The Japan-only N64 disk drive and Randnet | `systems/nintendo-64`, `companies/nintendo`, `games/legend-of-zelda-ocarina-of-time` |
| AGA chipset | hardware | The Amiga 1200 and 4000 chipset (Alice and Lisa), now covered inside the chipset entry | `demos/nexus-7` |
| Amiga 500 Batman Pack | hardware | Commodore's 1989–90 Amiga bundle | `games/batman-the-movie`, `systems/commodore-amiga`, `companies/ocean-software` |
| Amstrad PCW | systems | Amstrad's word processor, for which *Batman* was sold | `games/batman-1986` |
| ANTIC and GTIA | hardware | The Atari 8-bit display chips behind players, missiles, display lists and hardware scrolling | `techniques/sprites`, `systems/atari-8-bit`, `techniques/sprite-flicker`, `techniques/hardware-scroll` |
| Apple Macintosh | systems | Apple's 1984 computer, used as a platform across the Vault with no system entry | `companies/cyan`, `games/myst`, `companies/broderbund`, `culture/disk-magazines` |
| ARM | hardware | The Archimedes processor architecture, later in the Game Boy Advance and DS | `systems/acorn-archimedes`, `systems/game-boy-advance`, `systems/nintendo-ds`, `companies/acorn-computers` |
| Atari 5200 | systems | Atari's console with Centipede among its first cartridges; its joystick problems explain the trackball | `hardware/trackball`, `hardware/paddle-controller`, `systems/atari-8-bit`, `games/centipede`, `games/pole-position`, `games/xevious`, `games/joust`, `games/tempest`, `companies/atari`, `techniques/analog-control`, `games/robotron-2084`, `games/mario-bros` |
| Atari Cosmos | systems | Atari's unreleased holographic games machine of 1980 | `people/al-alcorn`, `companies/atari` |
| Atari CX40 joystick and the Atari joystick port | hardware | The de facto nine-pin standard | `hardware/d-sub-connector`, `systems/atari-2600`, `hardware/paddle-controller` |
| Atari Math Box | hardware | The bit-slice arithmetic unit behind Atari's 3D vector games | `games/battlezone`, `techniques/vector-graphics` |
| Atari System 1 | hardware | Atari Games' cartridge-based arcade board | `games/marble-madness`, `companies/atari-games` |
| BBC Buggy | hardware | The MEP/BBC robot for classroom control and Logo | `culture/educational-software`, `tools/logo-language`, `phenomena/bbc-computer-literacy-project` |
| Beta Disk and TR-DOS | hardware | The Spectrum disk system the *Lyra II* was converted to | `demos/lyra-ii`, `groups/esi` |
| Big Trak | hardware | Milton Bradley's 1979 programmable toy, used in schools before Logo | `companies/milton-bradley`, `tools/logo-language` |
| Camputers Lynx | systems | Chris Sawyer's first computer | `people/chris-sawyer` |
| Coleco Adam | systems | Coleco's home computer: late, unreliable, with a bundled printer and Digital Data Packs | `systems/colecovision` |
| Commodore 64 Games System | systems | Commodore's 1990 cartridge-only console built from the C64 | `magazines/commodore-format`, `systems/commodore-64` |
| Commodore CDTV | systems | Commodore's 1991 system, named in the Bushnell and Commodore entries | `hardware/trackball`, `hardware/cd-rom`, `systems/commodore-amiga`, `people/nolan-bushnell`, `companies/commodore` |
| CP1610 | hardware | General Instrument's 16-bit processor in the Intellivision | `systems/intellivision`, `hardware/ay-3-8910` |
| DEC PDP-1 | systems | In period since the 1960s extension; its Type 30 display explains what came before vector monitors | `techniques/vector-graphics` |
| DECO Cassette System | hardware | Data East's tape-based arcade system | `hardware/arcade-hardware`, `companies/data-east` |
| Disk II | hardware | Wozniak's minimal disk controller and the basis of Apple copy protection | `systems/apple-ii`, `techniques/disk-protection` |
| Dismac D-8000 | systems | The first cheap Brazilian personal computer | `companies/dismac`, `culture/brazilian-market-reserve`, `systems/trs-80` |
| DSP-1 | hardware | Nintendo's cartridge coprocessor, which brought 3D maths to mode 7 games | `techniques/mode-7`, `techniques/super-fx-chip`, `techniques/cycle-accuracy`, `hardware/cartridge` |
| Electronika 60 | systems | The Soviet machine the first *Tetris* ran on | `games/tetris`, `culture/soviet-computing`, `people/alexey-pajitnov` |
| Fairchild Channel F | systems | The first cartridge console, and home of *Video Whizball* | `hardware/cartridge`, `hardware/arcade-hardware`, `systems/atari-2600`, `people/warren-robinett` |
| FM Towns | systems | Fujitsu's 1989 CD-ROM computer, which used the YM2612 | `hardware/ym2612`, `hardware/cd-rom` |
| Galaksija Plus | systems | The Galaksija's 1985 successor | `systems/galaksija` |
| Game Boy Camera and Printer | hardware | The Game Boy's camera and printer add-ons | `techniques/link-cable`, `systems/game-boy` |
| Game Boy Four-Player Adapter | hardware | The link-cable hub for *F-1 Race* and Rare's *Super R.C. Pro-Am* | `techniques/link-cable`, `companies/rare`, `systems/game-boy` |
| Game port (IBM Game Control Adapter) | hardware | The resistor-timing interface behind PC joysticks, flight sticks and wheels | `hardware/flight-stick`, `hardware/paddle-controller`, `hardware/steering-wheel` |
| GD-ROM | hardware | The Dreamcast's and NAOMI's disc format | `systems/sega-dreamcast`, `systems/sega-naomi` |
| Genlock | hardware | The Amiga desktop-video basic that the Toaster built on | `hardware/video-toaster`, `systems/commodore-amiga` |
| Gravis UltraSound | hardware | The PC demo scene's favourite sound card | `groups/future-crew`, `communities/demo-scene`, `demos/second-reality`, `people/purple-motion` |
| GTIA / CTIA | hardware | Atari's 8-bit video chip, with the richest collision hardware of the 8-bit machines | `techniques/collision-detection`, `systems/atari-8-bit` |
| GunCon | hardware | Namco's light gun, the standard for PlayStation gun games | `hardware/light-gun`, `games/time-crisis` |
| Hackaday Superconference badges | hardware | Voja Antonić's later hardware work | `people/voja-antonic` |
| Hitachi SuperH (SH-2 and SH-4) | hardware | The CPU family of the Saturn, 32X, Dreamcast and NAOMI | `systems/sega-saturn`, `systems/sega-dreamcast`, `systems/sega-naomi` |
| HuC6280 | hardware | The PC Engine's 6502-derived CPU with an on-chip MMU and wavetable PSG | `systems/pc-engine`, `tools/deflemask` |
| Hyper Neo Geo 64 | systems | SNK's 1997 system | `companies/snk`, `systems/neo-geo` |
| IBM PC | systems | The platform hundreds of entries use, with no system entry | `hardware/flight-stick`, `culture/pc-gaming`, `companies/microsoft`, `companies/sierra`, `companies/softdisk`, `companies/id-software`, `distribution/shareware` |
| IBM PCjr | systems | Why *King's Quest* exists, and a well-known commercial failure | `games/kings-quest`, `companies/sierra`, `hardware/flight-stick`, `techniques/agi-engine` |
| J-Cart | hardware | Codemasters' Mega Drive cartridge with built-in joypad ports | `games/micro-machines`, `people/darling-brothers`, `systems/sega-mega-drive` |
| JAMMA | hardware | The cabinet wiring standard later arcade boards assumed | `hardware/arcade-hardware`, `systems/neo-geo`, `systems/sega-naomi`, `companies/capcom` |
| Kempston joystick interface | hardware | The Spectrum's de facto joystick standard, built into the Multiface One | `hardware/multiface`, `systems/sinclair-zx-spectrum`, `hardware/d-sub-connector` |
| KoalaPad and Koala Painter | hardware | The tablet often confused with light pens, and the multicolour bitmap format C64 artists used | `demos/deus-ex-machina`, `hardware/light-pen`, `systems/commodore-64` |
| Laser Clay Shooting System | hardware | Nintendo's light-gun toys, the ancestors of the 1976 *Duck Hunt* | `games/duck-hunt`, `people/gunpei-yokoi`, `people/masayuki-uemura`, `hardware/nes-zapper` |
| Later Sony consoles (PSP, PlayStation 3, 4 and 5, PS Vita) | systems | Named in the Sony entry and used as platform IDs, with no system entries | `companies/sony`, `companies/psygnosis`, `people/mark-cerny` |
| Magnavox Odyssey | systems | The first home console, with the first video light gun and 1972 tennis and hockey games | `hardware/light-gun`, `people/ralph-baer`, `hardware/paddle-controller`, `games/pong`, `genres/sports-games`, `companies/atari`, `people/nolan-bushnell`, `genres/horror-games`, `people/al-alcorn` |
| Memotech MTX | systems | Where Sawyer and others started in 1983–85 | `people/chris-sawyer` |
| Microvision | systems | Milton Bradley's 1979 handheld, the first with cartridges | `companies/milton-bradley`, `systems/game-boy`, `systems/nintendo-game-and-watch`, `companies/gce` |
| Minimig and MiST | hardware | MiSTer's ancestors and early FPGA Amiga projects | `hardware/mister-fpga`, `systems/commodore-amiga` |
| MITS Altair 8800 | systems | The kit Microsoft BASIC was written for | `companies/microsoft`, `games/colossal-cave-adventure`, `systems/apple-ii` |
| Motorola 6845 CRTC | hardware | The display controller in the BBC Micro, Amstrad CPC, PET and PC adapters | `hardware/light-pen`, `systems/bbc-micro`, `systems/amstrad-cpc` |
| Namco System 11 | hardware | The PlayStation-based arcade board | `games/tekken`, `companies/namco`, `systems/sony-playstation` |
| Namco System 22 | hardware | Model 2's rival | `techniques/model-2`, `techniques/texture-mapping` |
| Nascom | systems | The British kit computer where Level 9 began | `companies/level-9` |
| NEC PC-8801 | systems | The Japanese computer where *Dragon Slayer*, *Hydlide* and *Ys* began, and where Koshiro wrote his FM music | `games/streets-of-rage`, `people/yuzo-koshiro`, `techniques/sound-drivers`, `genres/action-rpg`, `companies/falcom`, `genres/jrpg`, `hardware/ym2612`, `techniques/fm-synthesis` |
| NEC VR4300 | hardware | The N64's MIPS CPU | `systems/nintendo-64`, `systems/sony-playstation` |
| Neo Geo CD | systems | SNK's cheaper 1994 CD console, known for slow loading | `systems/neo-geo`, `companies/snk` |
| Net Yaroze | hardware | The first legal consumer console development kit (1997) | `systems/sony-playstation`, `phenomena/bedroom-coder`, `companies/sony` |
| Nintendo 3DS | systems | The DS's successor | `systems/nintendo-ds` |
| Nintendo 64 Expansion Pak | hardware | *Perfect Dark* and *Donkey Kong 64* depended on it | `games/perfect-dark`, `systems/nintendo-64` |
| Nintendo 64DD | hardware | Nintendo's second disk add-on, compared with the Disk System at the time | `hardware/famicom-disk-system`, `systems/nintendo-64` |
| Nintendo GameCube | systems | Nintendo's rival to the PS2 and Xbox | `systems/microsoft-xbox`, `systems/sony-playstation-2`, `systems/nintendo-64` |
| Nintendo Wii | systems | Home of the light-gun revival | `genres/rail-shooters`, `hardware/light-gun`, `games/house-of-the-dead` |
| Nvidia GeForce 256 | hardware | The card *Halo* was shown on in 1999 | `games/halo` |
| PC-FX | systems | NEC and Hudson's 1994 successor console | `systems/pc-engine`, `companies/hudson-soft` |
| Pegasus and BobMark | systems | The Polish famiclone | `systems/famiclone`, `magazines/bajtek` |
| Philips CD-i | systems | Philips's interactive CD player and the rival deal in the Nintendo–Sony split | `systems/sony-playstation`, `people/howard-lincoln`, `people/hiroshi-yamauchi`, `hardware/cd-rom`, `techniques/fmv`, `games/7th-guest` |
| PLATO | systems | The University of Illinois system behind pedit5 and early multiplayer games | `genres/western-rpg`, `genres/roguelike`, `genres/mmorpg-history`, `games/wizardry`, `culture/online-multiplayer`, `genres/mud-history` |
| PlayStation Classic | systems | Sony's 2018 miniature console, running a fork of PCSX ReARMed | `systems/sony-playstation`, `emulators/pcsx`, `companies/sony` |
| POKEY | hardware | Atari's sound and I/O chip, used in Centipede and across the 8-bit machines | `hardware/paddle-controller`, `systems/atari-8-bit`, `games/centipede`, `games/star-raiders`, `techniques/analog-control` |
| Reality Coprocessor | hardware | The N64's RSP and RDP in more detail than the system entry gives | `systems/nintendo-64` |
| Recreated ZX Spectrum | hardware | Elite's 2014 Bluetooth Spectrum keyboard | `companies/elite-systems`, `systems/sinclair-zx-spectrum` |
| Research Machines 380Z and 480Z | systems | The third approved school machine | `culture/educational-software`, `systems/bbc-micro` |
| Roland MT-32 | hardware | The sound module many late-1980s PC games targeted | `hardware/mister-fpga`, `hardware/raspberry-pi`, `techniques/sci-engine`, `games/kings-quest` |
| RS-232 / user port | hardware | The C64's user port and RS-232 interface | `techniques/kernal-io`, `hardware/cia` |
| SA-1 and Sega SVP | hardware | Cartridge co-processors for the Super Nintendo and Mega Drive | `hardware/cartridge`, `systems/super-nintendo`, `systems/sega-mega-drive`, `techniques/super-fx-chip` |
| SAM Coupé | systems | Miles Gordon Technology's Spectrum-compatible machine, with Andy Wright's ROM BASIC; ESI moved to it | `people/david-whittaker`, `demos/shock-megademo`, `groups/esi`, `systems/sinclair-zx-spectrum`, `tools/beta-basic` |
| Sammy Atomiswave | hardware | Dreamcast-derived rival to NAOMI | `systems/sega-naomi` |
| Satellaview | hardware | Nintendo's satellite service for the Super Famicom | `distribution/digital-distribution`, `systems/super-nintendo` |
| Sega Chihiro | hardware | The arcade board for *Virtua Cop 3* | `games/virtua-cop`, `companies/sega-am2` |
| Sega Light Phaser | hardware | The Master System's light gun | `hardware/light-gun`, `systems/sega-master-system` |
| Sega Model 1 | hardware | Sega's first polygon board, behind *Virtua Racing* and *Virtua Fighter* | `hardware/arcade-hardware`, `techniques/model-2`, `people/yu-suzuki`, `games/virtua-fighter`, `companies/sega-am2`, `systems/sega-naomi` |
| Sega Model 3 | hardware | One of Sega's other polygon boards | `systems/sega-naomi`, `hardware/arcade-hardware`, `techniques/model-2`, `companies/sega-am2` |
| Sega ST-V | hardware | The Saturn-based arcade board, NAOMI's precedent | `systems/sega-saturn`, `systems/sega-naomi`, `hardware/arcade-hardware` |
| Sharp X68000 | systems | Japanese home computer with arcade-faithful Capcom ports | `games/ghouls-n-ghosts`, `companies/capcom` |
| Steam Deck | systems | Valve's handheld PC, used to play period software | `tools/steam`, `companies/valve` |
| Super Multitap | hardware | The SNES adaptor for more than two players | `games/secret-of-mana`, `games/bomberman`, `culture/couch-co-op` |
| Super Scope and Menacer | hardware | The 16-bit infrared light guns | `hardware/light-gun`, `systems/super-nintendo`, `systems/sega-mega-drive` |
| Taito Type X, Sega Lindbergh and Namco System 11 | hardware | Later arcade platforms | `hardware/arcade-hardware`, `systems/sega-naomi`, `companies/namco` |
| Tandy 1000 | systems | The PCjr-compatible machine that sold Sierra's PCjr games and saved Sierra in 1985 | `companies/sierra`, `companies/tandy`, `games/kings-quest` |
| TED (MOS 7360) | hardware | The chip at the centre of the C16 and Plus/4 | `systems/commodore-16`, `hardware/vic-ii` |
| Timex Computer 2048 | systems | A Spectrum-compatible machine in Bajtek's price tables that sold in Poland | `magazines/bajtek`, `systems/sinclair-zx-spectrum` |
| Timex Sinclair 2068 and Pentagon | systems | Spectrum relatives Fuse emulates; the Pentagon matters for Soviet computing | `emulators/fuse`, `systems/sinclair-zx-spectrum` |
| Trance Vibrator | hardware | ASCII's vibration peripheral for *Rez* | `games/rez`, `people/tetsuya-mizuguchi` |
| TurboExpress (PC Engine GT) | systems | The handheld that played home HuCards | `systems/pc-engine`, `systems/atari-lynx`, `systems/sega-game-gear` |
| V9938 and V9958 | hardware | The MSX2 video chips | `systems/msx` |
| Valiant Turtle and floor turtles | hardware | Classroom Logo robots | `tools/logo-language`, `systems/bbc-micro` |
| Vector-06C | systems | Soviet home computer still getting new demos in 2025 | `events/chaos-constructions`, `culture/soviet-computing` |
| VIDC, MEMC and IOC | hardware | The Archimedes chipset | `systems/acorn-archimedes` |
| VideoFace | hardware | Data-Skip's Spectrum video digitiser, sold by Romantic Robot | `demos/jesus-on-es-spectrum`, `hardware/multiface` |
| VideoLogic PowerVR | hardware | The tile-based graphics behind Dreamcast and NAOMI, also sold on PC cards | `systems/sega-dreamcast`, `systems/sega-naomi`, `hardware/arcade-hardware` |
| Visual Memory Unit | hardware | The Dreamcast's memory card with a screen | `systems/sega-dreamcast`, `systems/sega-naomi` |
| Whirlwind and SAGE | systems | Where the light pen began | `hardware/light-pen`, `hardware/light-gun` |
| Wii and Wii U | systems | Nintendo's 2006 and 2012 consoles | `people/satoru-iwata`, `companies/nintendo` |
| XBAND | hardware | The first widely sold console modem network in America, later behind Mega Net 2 in Brazil | `culture/online-multiplayer`, `systems/sega-mega-drive`, `systems/super-nintendo` |
| Xbox 360 and Xbox One | systems | Microsoft's second console, with achievements, Live Silver/Gold and Xbox Live Arcade; used as a platform ID with no system entry | `companies/microsoft`, `companies/rare`, `companies/lionhead`, `companies/remedy-entertainment`, `culture/xbox-live`, `systems/microsoft-xbox`, `games/perfect-dark`, `games/killer-instinct` |
| Xbox One | systems | Used as a platform ID with no system entry | `games/perfect-dark`, `games/killer-instinct`, `companies/rare` |
| Yamaha YM2151 (OPM) | hardware | FM chip used from Marble Madness on across arcade boards and the X68000 | `hardware/ym2612`, `techniques/fm-synthesis`, `companies/irem`, `games/marble-madness` |
| Yamaha YM2610 | hardware | The FM, SSG and ADPCM chip behind Neo Geo sound | `systems/neo-geo`, `hardware/ym2612` |
| Zeebo | systems | A console launched in Brazil in 2009 | `companies/tectoy` |

## People

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Richard Altwasser | people | Designed the Spectrum's hardware and its ULA logic | `systems/sinclair-zx-spectrum`, `hardware/ula`, `companies/sinclair-research`, `people/steven-vickers` |
| John Grant | people | Co-wrote the Spectrum ROM with Steven Vickers, on contract from Nine Tiles | `people/steven-vickers`, `systems/sinclair-zx-spectrum`, `systems/sinclair-zx81`, `systems/sinclair-zx80`, `tools/sinclair-basic` |
| Chris Curry | people | Co-founded Science of Cambridge with Sinclair, then Acorn | `companies/sinclair-research`, `people/clive-sinclair`, `companies/acorn-computers` |
| Jim Westwood | people | Designed the ZX80 and the ZX81's custom chip | `systems/sinclair-zx80`, `systems/sinclair-zx81`, `companies/sinclair-research`, `people/rick-dickinson` |
| Eugene Evans | people | The face of Imagine's publicity, later at Psygnosis; *Manic Miner*'s Eugene's Lair is named after him | `companies/imagine-software`, `companies/bug-byte`, `games/manic-miner`, `companies/psygnosis`, `culture/liverpool-games-scene`, `companies/denton-designs`, `people/ian-hetherington`, `people/david-lawson` |
| Bruce Everiss | people | Imagine's operations director and the main witness to its finances | `companies/imagine-software`, `culture/liverpool-games-scene`, `companies/denton-designs`, `people/ian-hetherington`, `people/david-lawson` |
| Mark Butler | people | Co-founded Imagine; David Lawson has an entry, Butler does not | `companies/imagine-software`, `companies/bug-byte`, `people/david-lawson`, `culture/liverpool-games-scene`, `companies/denton-designs`, `people/ian-hetherington` |
| Matt Bielby | people | *Your Sinclair* editor, 1989–91, then *Amiga Power*'s launch editor | `magazines/your-sinclair`, `people/teresa-maughan`, `magazines/amiga-power` |
| Stuart Campbell | people | *Your Sinclair* reviewer from 1991 and *Amiga Power* deputy editor; the old entry confused him with Phil South | `magazines/your-sinclair`, `magazines/amiga-power`, `games/cannon-fodder`, `culture/amiga-power-versus-team17` |
| Linda Barker | people | *Your Sinclair* staff writer, then editor 1992–93 | `magazines/your-sinclair`, `people/teresa-maughan` |
| Phil South | people | *Your Sinclair* contributor from issue 1 and Tipshop host | `magazines/your-sinclair` |
| Jonathan Davies | people | Program Pitstop host and author of "The YS Story" | `magazines/your-sinclair` |
| Alan Dykes and Garth Sumpter | people | The last two *Sinclair User* editors | `magazines/sinclair-user`, `magazines/crash-magazine` |
| John Pemberton | people | Designed the ZX80's case | `systems/sinclair-zx80`, `people/rick-dickinson` |
| Phil Candy | people | Rick Dickinson's design partner; co-designed the Next's case | `people/rick-dickinson`, `systems/zx-spectrum-next` |
| Kevin Cox | people | *Your Sinclair*'s first editor | `magazines/your-sinclair`, `people/teresa-maughan` |
| Alan Maton | people | Co-founded Software Projects | `companies/software-projects`, `companies/bug-byte` |
| Masatoshi Shima | people | Co-designed the Z80 | `hardware/z80`, `companies/zilog` |
| Mike Follin | people | Spectrum programmer named in the AY entry | `hardware/ay-3-8912`, `techniques/software-scroll`, `people/tim-follin` |
| Irving Gould | people | Commodore's chairman and main shareholder | `systems/commodore-64`, `systems/commodore-amiga`, `people/jack-tramiel` |
| R. J. Mical | people | Wrote Intuition and told the Amiga Corporation story | `systems/commodore-amiga`, `people/trip-hawkins`, `systems/atari-lynx`, `companies/epyx`, `hardware/amiga-chipset` |
| Carl Sassenrath | people | Designed the Amiga's multitasking Exec | `systems/commodore-amiga` |
| Dave Morse and Dave Needle | people | Amiga Corporation's founder and a chipset designer | `systems/commodore-amiga`, `people/trip-hawkins`, `systems/atari-lynx`, `companies/epyx`, `hardware/amiga-chipset` |
| Karsten Obarski | people | Wrote Soundtracker | `systems/commodore-amiga`, `hardware/paula`, `tools/soundtracker`, `tools/protracker`, `culture/tracker-music`, `techniques/mod-format` |
| Henrique Olifiers | people | Led the Spectrum Next project and its three Kickstarters | `systems/zx-spectrum-next` |
| Victor Trucco and Fabio Belavenuto | people | Built the TBBlue board the Next grew from | `systems/zx-spectrum-next` |
| Garry Lancaster | people | Wrote NextZXOS | `systems/zx-spectrum-next` |
| Michael Tomczyk | people | Tramiel's assistant; wrote *The Home Computer Wars* | `people/jack-tramiel`, `people/bob-yannes` |
| Charles Winterble | people | MOS engineering manager named in the C64 design history | `people/al-charpentier`, `hardware/vic-ii` |
| Bill Mensch | people | 6502 co-designer | `companies/mos-technology` |
| Doug Smith | people | Wrote Lode Runner | `games/lode-runner`, `companies/broderbund` |
| Martin Walker | people | C64 programmer whose *ZZAP!64* diary covers multiplexers and SID bugs | `hardware/vic-ii`, `hardware/sid-chip`, `techniques/arpeggio`, `techniques/game-loop`, `magazines/zzap-64`, `techniques/interrupt-driven-music`, `companies/thalamus`, `techniques/multidirectional-scrolling` |
| Terry Ritter and Joel Boney | people | Designed the 6809 and wrote *BYTE*'s 1979 series on it | `hardware/6809` |
| Marko Mäkelä | people | Wrote the 1995 *C=Hacking* article on stable rasters | `techniques/stable-raster`, `magazines/c-hacking`, `hardware/vic-ii` |
| Shaun Southern | people | Magnetic Fields programmer quoted on the AGA blitter | `hardware/agnus`, `hardware/blitter` |
| Doug Neubauer | people | Designed POKEY and wrote *Star Raiders* | `games/star-raiders`, `systems/atari-8-bit`, `systems/atari-2600` |
| Steve Mayer | people | Credited in period sources as the 2600's main designer | `systems/atari-2600`, `systems/atari-8-bit`, `companies/atari` |
| Carol Shaw | people | Wrote *River Raid*; her 1983 interview explains how 2600 programming worked | `systems/atari-2600`, `companies/activision`, `techniques/procedural-generation`, `people/ed-logg` |
| Alan Miller | people | Atari programmer who co-founded Activision and Accolade | `systems/atari-2600`, `companies/activision`, `culture/atari-vs-activision`, `people/david-crane` |
| Ted Dabney | people | Co-founded Atari with Bushnell | `companies/atari`, `people/nolan-bushnell`, `games/pong`, `people/al-alcorn` |
| James J. Morgan | people | Kassar's successor at Atari | `people/ray-kassar`, `phenomena/1983-crash`, `companies/atari` |
| Tod Frye | people | Programmed the 2600 *Pac-Man* | `games/pac-man-atari-2600`, `phenomena/1983-crash` |
| Mark Turmell | people | Sirius programmer whose 1982 interview explains the 2600 *Pac-Man*'s flicker | `techniques/sprite-flicker`, `people/ed-boon`, `games/nba-jam`, `people/john-tobias`, `people/eugene-jarvis` |
| Derek Meakin | people | Founded Database Publications and Europress | `companies/europress`, `magazines/amiga-computing`, `magazines/micro-user`, `magazines/atari-st-user`, `magazines/amiga-action` |
| Matthew Uffindell | people | One of CRASH's first reviewers and the main source on who wrote as Lloyd Mangram | `people/lloyd-mangram`, `magazines/crash-magazine`, `people/roger-kean`, `companies/newsfield` |
| Tim Boone | people | Edited *C&VG* and then *Nintendo Magazine System* | `magazines/nintendo-magazine-system`, `magazines/computer-and-video-games` |
| Eugene Lacey | people | Edited *Commodore User* and *C&VG*, and consulted on *ACE* | `magazines/cu-amiga`, `magazines/ace-magazine`, `magazines/computer-and-video-games`, `companies/emap` |
| Terry Pratt and Tim Metcalfe | people | *C&VG*'s other 1980s editors | `magazines/computer-and-video-games`, `companies/emap`, `companies/beyond-software`, `people/mike-singleton`, `games/lords-of-midnight` |
| Steve Cooke | people | Co-founded *ACE* and wrote its adventure pages throughout | `magazines/ace-magazine`, `magazines/personal-computer-games`, `magazines/zzap-64` |
| Bob Wade | people | Worked on *Personal Computer Games*, *Amstrad Action*, *ACE* and *Amiga Format* | `magazines/amiga-format`, `magazines/amstrad-action`, `magazines/ace-magazine`, `magazines/personal-computer-games` |
| Greg Ingham | people | Published *ST/Amiga Format*, later Future's chief executive | `magazines/st-format`, `magazines/amiga-format`, `companies/future-publishing`, `people/chris-anderson` |
| Mel Croucher | people | Wrote *Deus Ex Machina* and the AMOS manuals | `tools/amos` |
| Sandra Sharkey | people | Ran the first AMOS PD library and founded *Adventure Probe* | `tools/amos`, `distribution/licenseware` |
| Marc Haigh-Hutchinson | people | Wrote *Alien Highway* for Vortex | `companies/vortex-software`, `people/costa-panayi` |
| Geoff Brown | people | Founded CentreSoft and U.S. Gold, and part-owned Gremlin | `companies/us-gold`, `companies/centresoft`, `companies/gremlin-graphics`, `companies/kixx`, `systems/atari-8-bit`, `games/flashback`, `companies/tiertex`, `companies/eidos` |
| Donald Campbell and John Prince | people | Founded Tiertex | `companies/tiertex` |
| Ken Kutaragi | people | Designed the SNES sound chip, then led the PlayStation | `systems/super-nintendo`, `companies/sony`, `systems/sony-playstation`, `systems/sony-playstation-2` |
| Satoru Okada | people | Directed *Kid Icarus* and was chief director of *Metroid* | `games/metroid`, `games/kid-icarus`, `systems/game-boy`, `people/gunpei-yokoi`, `companies/nintendo-rd1` |
| Hiroji Kiyotake and Makoto Kano | people | Samus's designer and *Metroid*'s scenario writer | `games/metroid` |
| Toru Osawa | people | Designed *Kid Icarus* | `games/kid-icarus`, `people/yoshio-sakamoto` |
| Takashi Tezuka | people | Miyamoto's co-designer on *Super Mario Bros.* and *Zelda* | `games/super-mario-bros`, `people/shigeru-miyamoto`, `games/legend-of-zelda`, `people/koji-kondo`, `games/super-mario-bros-3` |
| Howard Phillips | people | Nintendo of America's "game master" in court, later the face of *Nintendo Power* | `culture/universal-vs-nintendo`, `systems/nintendo-entertainment-system`, `magazines/nintendo-power`, `companies/nintendo` |
| David Aubrey Jones | people | Co-wrote Speedlock and the Spectrum *Mercenary*; not the Magic Knight David Jones | `techniques/fast-loader`, `techniques/copy-protection` |
| Jim Levy | people | Activision's president and fifth founder, who brought *Little Computer People* to Crane | `companies/activision`, `people/david-crane`, `culture/atari-vs-activision` |
| Bob Whitehead and Larry Kaplan | people | Two of Activision's founding designers; Kaplan later helped start the Amiga company | `companies/activision`, `people/david-crane`, `culture/atari-vs-activision`, `people/jay-miner` |
| Mike Male | people | Hewson's simulation author | `companies/hewson-consultants` |
| Gary Bracey | people | Ocean's head of software development and the main source on its film licences | `companies/ocean-software`, `games/batman-1986`, `games/batman-the-movie`, `people/mike-lamb`, `games/renegade` |
| David Rosen | people | The American who ran Sega for about twenty years and co-led its 1984 buyout | `companies/sega`, `systems/sega-master-system` |
| Hayao Nakayama | people | Sega's chief executive from the 1984 buyout through the Mega Drive years | `companies/sega`, `systems/sega-mega-drive`, `people/yu-suzuki` |
| Kagemasa Kozuki | people | Konami's founder and long-time president | `companies/konami` |
| Kazuhisa Hashimoto | people | Programmed the Famicom *Gradius* and gave it the Konami code | `companies/konami`, `culture/konami-code`, `games/gradius`, `games/contra` |
| Frank Herman | people | Mastertronic's chairman and co-founder, who found Sega its British distribution | `companies/mastertronic`, `people/martin-alper`, `systems/sega-master-system` |
| Kenzo Tsujimoto | people | Founded Capcom after Irem; one entry could settle the I.R.M. question | `companies/capcom`, `companies/irem` |
| David Johnson-Davies | people | Ran Acornsoft from the Atom years to 1986 | `companies/acornsoft` |
| Takashi Nishiyama | people | Designed *Moon Patrol* and *Kung-Fu Master*, then *Street Fighter* at Capcom | `companies/irem`, `games/moon-patrol`, `games/kung-fu-master`, `games/fatal-fury`, `games/street-fighter`, `companies/snk` |
| Bill Budge | people | Wrote *Pinball Construction Set* and led EA's "software artists" advert | `companies/electronic-arts`, `people/trip-hawkins` |
| Masaya Nakamura | people | Namco's founder, central to its Atari deals and the *Pac-Man* story | `companies/namco`, `games/pac-man`, `companies/atari`, `companies/atari-games`, `people/toru-iwatani` |
| Hideyuki Nakajima | people | Ran Atari Japan and Namco America, then Atari Games and Tengen | `companies/namco`, `companies/atari`, `companies/atari-games`, `games/pac-man` |
| Larry Probst | people | EA's chief executive from 1991 to 2007 | `companies/electronic-arts`, `people/trip-hawkins` |
| Isao Okawa | people | Sega's chairman, whose personal gift in 2001 helped it survive leaving hardware | `companies/sega`, `systems/sega-dreamcast` |
| Hideki Kamiya | people | Directed *Devil May Cry* and *Okami* at Capcom, then moved to Platinum Games | `companies/capcom`, `games/resident-evil`, `people/shinji-mikami` |
| Yoshinori Ono | people | The Capcom producer who revived the series with *Street Fighter IV* | `companies/capcom`, `people/katsuhiro-harada` |
| Adrian Carmack | people | id co-founder and lead artist | `companies/id-software`, `games/doom`, `games/quake`, `people/john-carmack`, `people/john-romero`, `companies/softdisk` |
| Akira Kitamura | people | Director of *Mega Man* and *Mega Man 2*; credit for the character often goes to Inafune | `games/mega-man`, `games/mega-man-2`, `companies/capcom`, `people/keiji-inafune`, `people/tokuro-fujiwara` |
| Akira Nishitani | people | Planner of *Final Fight* and *Street Fighter II*, later founder of Arika | `games/street-fighter-ii`, `games/final-fight`, `companies/capcom` |
| Akira Toriyama | people | The artist behind Dragon Quest's look, Dragon Ball and Chrono Trigger | `genres/jrpg`, `games/dragon-quest`, `people/yuji-horii`, `games/chrono-trigger`, `people/hironobu-sakaguchi`, `companies/enix` |
| Akira Yasuda (Akiman) | people | Character designer on *Street Fighter II* and *Final Fight* | `games/street-fighter-ii`, `games/final-fight` |
| Alan Kay | people | Ran Atari's research lab and hired Crawford | `people/chris-crawford`, `companies/atari` |
| Alan Steele | people | Designer of PSS's Wargamers series | `companies/pss`, `genres/wargame`, `people/gary-mays` |
| Alex Rigopulos, Eran Egozy and Greg LoPiccolo | people | Harmonix's founders and project lead, quoted throughout | `companies/harmonix`, `games/rock-band`, `games/guitar-hero` |
| Alex Ward and Three Fields Entertainment | people | Burnout's creator and his later studio | `companies/criterion`, `games/burnout` |
| Alexander Brandon | people | Tracker musician turned composer for *Unreal* and *Deus Ex* | `culture/tracker-music`, `games/unreal`, `games/deus-ex` |
| Alfred Milgrom and Naomi Besen | people | Founders of Melbourne House and Beam; Milgrom drove *The Hobbit* | `companies/melbourne-house`, `companies/beam-software`, `games/the-hobbit` |
| Allen Adham | people | Blizzard co-founder who started and shaped Warcraft | `games/warcraft`, `companies/blizzard` |
| Allen Hastings | people | Author of Videoscape 3D and LightWave | `hardware/video-toaster`, `tools/lightwave-3d`, `companies/newtek`, `tools/sculpt-3d`, `people/eric-graham` |
| Allister Brimble | people | Amiga and PC composer (*Alien Breed*, *Superfrog*, *RollerCoaster Tycoon*) | `companies/team17`, `games/alien-breed`, `people/andreas-tadic`, `distribution/public-domain`, `games/roller-coaster-tycoon`, `people/chris-sawyer` |
| Ally Noble | people | Denton co-founder who kept the company going after 1986 | `companies/denton-designs`, `culture/liverpool-games-scene` |
| American McGee | people | Doom and Quake level designer | `games/quake`, `games/doom` |
| Andreas Axelsson | people | DICE co-founder, with a long first-hand interview on record | `companies/dice-studio`, `groups/the-silents` |
| Andreas Escher | people | Manfred Trenz's designer and artist on *Katakis* and *Turrican* | `companies/rainbow-arts`, `games/turrican`, `people/manfred-trenz`, `companies/factor-5` |
| Andrew Fluegelman | people | Originator of freeware, PC-Talk and *PC World* | `distribution/shareware`, `distribution/public-domain` |
| Andrew Graham | people | Programmed the NES *Micro Machines* and *Treasure Island Dizzy* | `games/micro-machines`, `games/dizzy` |
| Andrew Greenberg | people | Co-designer of Wizardry | `games/wizardry`, `genres/western-rpg` |
| Andy Wright and Betasoft | people | Author of Beta BASIC and SAM BASIC | `tools/beta-basic`, `tools/sinclair-basic` |
| Ann Piestrup | people | Founder of The Learning Company | `companies/the-learning-company`, `games/rockys-boots` |
| Anthony Lees | people | Composer on *The Last Ninja*, later of *Tarran* | `games/the-last-ninja`, `people/ben-daglish` |
| Archer Maclean | people | Wrote *Dropzone*, *IK*, *IK+* and *Jimmy White's Whirlwind Snooker* | `games/international-karate`, `games/international-karate-plus`, `companies/system-3` |
| Aric Wilmunder | people | Co-builder of SCUMM, who took it to the PC | `techniques/scumm`, `companies/lucasarts` |
| Arnie Katz, Bill Kunkel and Joyce Worley | people | Founders of American games journalism and of *Electronic Games* | `magazines/electronic-games` |
| Atsushi Inaba | people | Founder of Clover Studio and head of Platinum Games | `people/shinji-mikami`, `companies/capcom` |
| Ayami Kojima | people | The painter whose art set *Castlevania*'s look from 1997 | `games/symphony-of-the-night`, `people/koji-igarashi` |
| Barrington Pheloung | people | The *Inspector Morse* composer who wrote *Broken Sword*'s interactive 400-cue score | `games/broken-sword`, `companies/revolution-software` |
| Bil Herd | people | The C128's designer | `magazines/c-hacking` |
| Bill Gates | people | Microsoft's co-founder, behind the BASIC that Commodore licensed | `companies/microsoft`, `systems/trs-80`, `systems/msx`, `systems/microsoft-xbox`, `techniques/basic-v2` |
| Bill Harbison | people | Ocean artist on WEC Le Mans and Chase H.Q. | `games/chase-hq`, `games/batman-the-movie` |
| Bill Stealey | people | Co-founder and public face of MicroProse, later Interactive Magic | `companies/microprose`, `people/sid-meier` |
| Billy Mitchell | people | Arcade champion from 1982, and the 2018–2024 score dispute | `events/twin-galaxies`, `games/pac-man`, `games/donkey-kong` |
| Bjørn Lynne | people | *Worms* composer and Amiga musician | `games/worms` |
| Bomb the Bass | people | Tim Simenon's act, whose *Megablast* became *Xenon 2*'s music | `games/xenon-2`, `people/david-whittaker` |
| Brenda Laurel | people | Early CGDC board member and interactive-drama theorist | `culture/gdc`, `people/chris-crawford` |
| Brett Sperry | people | Westwood co-founder and president, producer of Dune II, who named Command & Conquer | `genres/rts-genre`, `companies/westwood-studios`, `games/dune-ii`, `games/command-and-conquer`, `people/louis-castle` |
| Brewster Kahle | people | Founder of the Internet Archive | `communities/internet-archive`, `culture/game-preservation` |
| Brian Moriarty | people | Wrote *Wishbringer*, *Trinity* and *Beyond Zork* | `companies/infocom` |
| Bruce Daniels | people | Zork co-author | `games/zork`, `companies/infocom` |
| Bruce Shelley | people | Co-designer of *Railroad Tycoon* and *Civilization*, later *Age of Empires* | `games/civilization`, `people/sid-meier`, `genres/tycoon-games` |
| Bruno Bonnell | people | Infogrames' co-founder and head for 24 years | `companies/infogrames`, `companies/ocean-software` |
| Chaos (Dierk Ohlerich) | people | Sanity coder and farbrausch's lead tool author | `groups/farbrausch`, `groups/sanity`, `demos/fr-08-the-product`, `demos/debris`, `people/ryg`, `people/kb` |
| Charles Brannon | people | COMPUTE!'s program editor, author of MLX, the Automatic Proofreader and SpeedScript | `magazines/compute-magazine`, `magazines/computes-gazette`, `distribution/type-in-listings` |
| Charles Deenen | people | Maniacs of Noise co-founder and *Stormlord* C64 musician, later Interplay's audio director | `people/jeroen-tel`, `games/stormlord`, `techniques/sound-drivers`, `companies/interplay` |
| Chris Abbott | people | Remixer behind *Back in Time* and C64Audio.com, and the HVSC's contact for commercial use | `communities/chiptune-scene`, `people/rob-hubbard`, `people/ben-daglish`, `tools/hvsc` |
| Chris Andrew | people | Originated Freescape and led Major Developments; Ian Andrew's brother | `techniques/freescape`, `people/ian-andrew`, `companies/incentive-software`, `games/driller` |
| Chris Butler | people | Elite's C64 programmer of Commando, Ghosts 'n Goblins and Space Harrier | `games/commando`, `games/ghosts-n-goblins`, `techniques/scrolling`, `companies/elite-systems`, `games/space-harrier`, `techniques/memory-management`, `techniques/tile-graphics`, `techniques/tile-maps` |
| Chris Clarke | people | Co-author of *Match Day*, founder member of Crystal Computing, and author of *Three and In* | `people/jon-ritman`, `people/bernie-drummond`, `games/match-day`, `companies/design-design` |
| Chris Hecker | people | Described the ragdoll technique in 1998 | `techniques/motion-capture`, `techniques/physics-engines`, `techniques/ragdoll-physics` |
| Chris Hinsley | people | Mikro-Gen's lead programmer | `companies/mikro-gen`, `people/david-perry`, `people/raffaele-cecco` |
| Chris Oxlade | people | Author or programmer on many Usborne titles | `books/usborne-computing-books`, `books/machine-code-for-beginners` |
| Chris Serle | people | The layman presenter of *The Computer Programme* | `people/ian-mcnaught-davis`, `phenomena/bbc-computer-literacy-project` |
| Chris Taylor | people | Designed *Total Annihilation*, then founded Gas Powered Games (*Dungeon Siege*, *Supreme Commander*) | `games/total-annihilation`, `games/supreme-commander`, `companies/cavedog-entertainment` |
| Chris Wild and Chilli Hugger Software | people | Kept *Lords of Midnight* alive after 2012 | `games/lords-of-midnight`, `games/doomdarks-revenge`, `people/mike-singleton` |
| Chris Yates | people | Co-founder and programmer of Sensible Software | `games/wizball`, `companies/sensible-software`, `people/jon-hare`, `games/cannon-fodder` |
| Christopher Weaver | people | Bethesda's founder | `companies/bethesda` |
| Chuck Bueche | people | Origin co-founder ("Chuckles") | `companies/origin-systems`, `people/richard-garriott`, `games/ultima` |
| Cliff Bleszinski | people | Designer of Jazz Jackrabbit and Gears of War, co-creator of Fortnite | `companies/epic-games`, `games/unreal`, `people/tim-sweeney` |
| Colin McComb | people | Designer on Planescape: Torment | `games/planescape-torment` |
| Colin Porch | people | Ocean programmer who converted *Head Over Heels* and wrote *Return to Blacktooth* | `games/head-over-heels`, `companies/ocean-software`, `games/contra` |
| Corrado Giustozzi | people | Founder and editor of MC | `magazines/mc-microcomputer` |
| Craig Bruce | people | *C=Hacking*'s most regular early contributor (ACE, ZED, Little Red Reader) | `magazines/c-hacking` |
| Crossbow | people | Crest's founder, credited with FPP, sprite crunching and several FLI modes | `groups/crest`, `techniques/sprite-crunching`, `techniques/fpp`, `techniques/fli`, `demos/deus-ex-machina` |
| Cynthia Solomon and Wally Feurzeig | people | Logo's co-designers at BBN | `tools/logo-language`, `people/seymour-papert` |
| Daigo Umehara | people | The best-known fighting-game player, central to Moment 37 | `events/evo`, `communities/fighting-game-community`, `games/street-fighter-ii` |
| Dan Gorlin | people | Author of *Choplifter*, *Airheart* and *Typhoon Thompson* | `companies/broderbund`, `games/choplifter` |
| Darran Jones | people | *Retro Gamer*'s editor since 2005 | `magazines/retro-gamer`, `companies/imagine-publishing` |
| Dave Gibbons | people | The *Watchmen* artist who designed *Beneath a Steel Sky* and *Beyond a Steel Sky* | `companies/revolution-software`, `people/charles-cecil`, `games/beneath-a-steel-sky`, `genres/graphic-adventure` |
| Dave Grossman | people | Co-led *Day of the Tentacle*, co-wrote both *Monkey Island*s, later Telltale's design director | `games/monkey-island`, `companies/lucasarts`, `games/day-of-the-tentacle`, `companies/telltale`, `people/tim-schafer`, `people/ron-gilbert` |
| David Bishop | people | Designer of Crowther's Mirrorsoft games and *Bombuzal* | `people/tony-crowther`, `companies/mirrorsoft`, `companies/ariolasoft`, `companies/domark` |
| David Brevik | people | Condor co-founder and Diablo's lead, later Flagship and Torchlight | `companies/blizzard`, `games/diablo` |
| David Collier | people | Ocean programmer on Arkanoid | `games/arkanoid`, `companies/ocean-software` |
| David Doak | people | Co-director of *Perfect Dark* and head of design at Free Radical | `games/goldeneye-007`, `games/perfect-dark` |
| David Kaemmer | people | Designer of *Indy 500*, *IndyCar*, *NASCAR* and *GPL*, and co-founder of iRacing | `genres/racing-simulation`, `genres/racing-game` |
| David Lau-Kee | people | Founder of Criterion and RenderWare | `companies/criterion`, `techniques/renderware` |
| Dawn Drake | people | Ocean artist on *Batman: The Movie*, *RoboCop* and *Target Renegade* | `games/batman-the-movie`, `people/mike-lamb`, `games/renegade` |
| Debbie Bestwick | people | Team17 from 1990, chief executive 2009–2023 | `companies/team17`, `games/worms` |
| Dejan Ristanović | people | Wrote the first issue of *Računari u vašoj kući* and later edited *PC* | `systems/galaksija`, `magazines/racunari`, `people/voja-antonic` |
| Demis Hassabis and Elixir Studios | people | Co-creator of Theme Park, Lionhead co-founder, Elixir, DeepMind, Nobel laureate | `companies/bullfrog`, `companies/lionhead`, `games/theme-park`, `culture/guildford-games-cluster` |
| Dennis "Thresh" Fong | people | Winner at Deathmatch 95 and Red Annihilation | `communities/esports-origins`, `games/quake`, `games/doom` |
| Dennis Caswell | people | Made Starpath 2600 games, then *Impossible Mission* | `games/impossible-mission`, `companies/epyx` |
| Dominic Robinson | people | Hewson programmer of Spectrum Uridium and Zynaps, later Graftgold's 16-bit engine programmer | `games/uridium`, `games/zynaps`, `companies/graftgold`, `companies/hewson-consultants`, `techniques/software-scroll`, `games/rainbow-islands`, `people/andrew-braybrook`, `people/steve-turner` |
| Don Bluth | people | Dragon's Lair and Space Ace | `techniques/fmv` |
| Don Rawitsch | people | Co-author of *The Oregon Trail* and MECC executive | `companies/mecc`, `games/oregon-trail` |
| Don Woods | people | Expanded *Adventure* into the widely copied version | `genres/text-adventure`, `games/colossal-cave-adventure`, `people/will-crowther` |
| Doug and Gary Carlston | people | Brøderbund's founders | `companies/broderbund`, `people/jordan-mechner`, `games/prince-of-persia` |
| Doug Bell | people | Lead designer and programmer of *Dungeon Master* | `games/dungeon-master`, `genres/western-rpg` |
| Doug Church | people | Looking Glass project lead on Ultima Underworld and System Shock, a key source for the immersive-sim idea | `games/thief`, `companies/looking-glass`, `games/system-shock`, `games/deus-ex`, `genres/immersive-sim`, `games/system-shock-2`, `people/ken-levine` |
| Douglas Adams | people | Co-wrote Infocom's best-selling game and *Bureaucracy* | `companies/infocom`, `people/steve-meretzky` |
| Douglas Crockford | people | Managed the NES Maniac Mansion and wrote the account of its censorship | `games/maniac-mansion`, `techniques/scumm` |
| Dylan Cuthbert | people | Argonaut programmer who worked on the Super FX and *Star Fox* in Kyoto | `companies/argonaut`, `games/star-fox`, `techniques/super-fx-chip` |
| Eben Upton | people | The Raspberry Pi's co-founder | `hardware/raspberry-pi`, `people/david-braben`, `systems/bbc-micro` |
| Ed Krakauer | people | Ran GCE after Mattel Electronics | `companies/gce`, `systems/intellivision` |
| Ed Rotberg | people | Designer of *Battlezone* and the Bradley Trainer, later *Blasteroids* and *S.T.U.N. Runner* | `people/dona-bailey`, `games/asteroids`, `people/ed-logg`, `games/battlezone`, `games/tempest` |
| Eikichi Kawasaki | people | SNK's founder and Playmore's creator | `companies/snk`, `systems/neo-geo`, `companies/nazca` |
| Feargus Urquhart | people | Ran Black Isle and co-founded Obsidian (not the existing people/christian-urquhart) | `companies/black-isle-studios`, `companies/obsidian-entertainment`, `games/baldurs-gate`, `companies/interplay`, `games/planescape-torment`, `games/fallout` |
| Fergus McGovern | people | Founder of Probe and HotGen | `companies/probe-software`, `companies/acclaim` |
| Firefox | people | Phenomena's main musician | `groups/phenomena`, `demos/enigma` |
| fiver2 (Thomas Mahlke) | people | Artist and director of *fr-08*, *.kkrieger* and *debris.* | `groups/farbrausch`, `demos/fr-08-the-product`, `demos/debris` |
| Francis Tresham | people | Designed the *Civilization* board game and *1829* | `games/civilization` |
| Frank Cifaldi | people | Preservationist and founder of the Video Game History Foundation | `culture/game-preservation` |
| Frank Klepacki | people | Westwood's composer for Dune II, Command & Conquer and Red Alert, including "Hell March" | `games/command-and-conquer`, `games/red-alert`, `games/dune-ii`, `companies/westwood-studios` |
| Frank O'Hara | people | Co-author of the ZX81 Part B and Spectrum ROM disassemblies | `people/ian-logan`, `books/complete-spectrum-rom-disassembly`, `companies/melbourne-house` |
| Frank Ostrowski | people | Author of GFA BASIC and Turbo-BASIC XL | `tools/gfa-basic`, `systems/atari-8-bit` |
| Fredrik Huss (Mr. H) | people | Co-author of *Fasttracker* and *Crystal Dream* | `groups/triton`, `people/vogue`, `demos/crystal-dream` |
| Frédérick Raynal | people | Designer of *Alone in the Dark* and *Little Big Adventure* | `companies/infogrames`, `genres/survival-horror`, `techniques/pre-rendered-backgrounds`, `techniques/tank-controls` |
| Fukio Mitsuji | people | Designer of *Bubble Bobble*, *Rainbow Islands* and *Volfied* | `companies/taito`, `games/bubble-bobble`, `games/rainbow-islands`, `games/puzzle-bobble` |
| Gabe Newell | people | Valve's co-founder | `games/half-life`, `companies/valve`, `games/half-life-2`, `tools/steam`, `communities/modding` |
| Gail Tilden | people | Nintendo Power's founding editor, who later ran the American Pokémon launch | `magazines/nintendo-power`, `companies/nintendo`, `games/pokemon-red-blue` |
| Gary Liddon | people | ZZAP! writer and Thalamus's first technical executive | `companies/thalamus`, `companies/newsfield`, `magazines/zzap-64` |
| Gary Penn | people | *PCG* reader turned *ZZAP!64* editor, then *The One*, BMG and DMA; wrote the account of *GTA*'s development | `magazines/personal-computer-games`, `magazines/zzap-64`, `games/grand-theft-auto`, `culture/dundee-games-scene`, `magazines/the-one`, `magazines/the-games-machine`, `games/uridium` |
| Gary Timmons | people | DMA animator who drew the lemmings | `games/lemmings`, `companies/dma-design`, `people/mike-dailly` |
| Gary Whitta | people | Staff writer on *ACE* and *The One*, later deputy editor | `magazines/the-one`, `magazines/ace-magazine` |
| Gary Winnick | people | Lucasfilm's first games artist and co-designer of *Maniac Mansion* and *Thimbleweed Park* | `games/maniac-mansion`, `techniques/scumm`, `companies/lucasarts`, `people/ron-gilbert`, `games/monkey-island`, `techniques/pixel-art` |
| Geoff Heath | people | Publishing figure at Melbourne House, Telecomsoft and Mastertronic | `companies/melbourne-house`, `companies/telecomsoft`, `companies/mastertronic` |
| George Broussard | people | Apogee partner and 3D Realms head who led *Duke Nukem Forever* | `companies/apogee-software`, `people/scott-miller`, `companies/3d-realms`, `games/duke-nukem-3d` |
| George Plimpton | people | The face of the first comparative console advertising | `systems/intellivision`, `systems/atari-2600` |
| George Sanger (The Fat Man) | people | Composer of *Wing Commander II* and *The 7th Guest* | `games/wing-commander`, `companies/origin-systems`, `games/7th-guest` |
| Glenn Corpes | people | *Populous* artist and co-designer, later a Lost Toys founder | `games/populous`, `companies/bullfrog`, `people/peter-molyneux`, `games/syndicate`, `culture/guildford-games-cluster`, `games/dungeon-keeper` |
| Graham Nelson | people | Author of Inform and the Z-Machine Standards Document | `techniques/z-machine`, `companies/infocom` |
| Greg Fischbach | people | Acclaim's co-founder and chief executive | `companies/acclaim`, `companies/activision`, `games/mortal-kombat` |
| Greg Zeschuk | people | BioWare co-founder | `companies/bioware`, `games/baldurs-gate` |
| Gregg Barnett | people | Designed *Exploding Fist*, then *Shadowrun*'s starting point at Beam | `companies/beam-software`, `games/way-of-the-exploding-fist`, `companies/melbourne-house`, `people/rob-hubbard` |
| Gregg Mayles | people | DKC's game designer, later Banjo-Kazooie | `games/donkey-kong-country`, `companies/rare` |
| Guido Henkel | people | Realms of Arkania designer and Torment producer | `games/planescape-torment` |
| Guy Wilday | people | Produced *Colin McRae Rally*, then led Sega Racing Studio's 2007 *Sega Rally* | `games/sega-rally`, `companies/codemasters` |
| Harold Lee | people | Co-designer of the home *Pong* chip | `games/pong`, `companies/atari`, `people/al-alcorn` |
| Harry Williams | people | Pinball designer credited with the tilt | `companies/williams-electronics` |
| Harvey Smith | people | Deus Ex lead designer, director of Invisible War, co-director of Dishonored | `games/deus-ex`, `companies/ion-storm`, `games/dishonored`, `genres/immersive-sim`, `companies/arkane-studios`, `people/warren-spector` |
| HCL | people | Booze Design's coder, author of ByteBoozer and lead coder of *Edge of Disgrace* | `groups/booze-design`, `demos/edge-of-disgrace`, `techniques/compression`, `techniques/disk-fastloaders` |
| Hermann Hauser | people | Co-founder and chairman of Acorn | `companies/acorn-computers`, `magazines/acorn-user` |
| Hidetaka Miyazaki | people | Director of *Demon's Souls*, *Dark Souls*, *Bloodborne*, *Sekiro* and *Elden Ring*, and FromSoftware's president from 2014 | `games/dark-souls`, `games/demons-souls`, `games/bloodborne`, `companies/fromsoft`, `genres/action-rpg`, `techniques/difficulty-design` |
| Hirokazu Yasuhara | people | Planner of the early Sonic games, later at Naughty Dog | `games/sonic-the-hedgehog`, `companies/sonic-team`, `people/yuji-naka` |
| Hiroki Kikuta | people | Composer of *Secret of Mana* | `games/secret-of-mana` |
| Hiromichi Tanaka | people | Producer of *Secret of Mana* and a long-serving Square designer | `games/secret-of-mana`, `companies/square` |
| Hiroshi Kawaguchi | people | Composer of *Out Run*, *Space Harrier* and *After Burner* | `games/out-run`, `games/after-burner`, `games/space-harrier` |
| Hiroyuki Imabayashi / Thinking Rabbit | people | Designer and publisher of *Sokoban* | `techniques/puzzle-game-design` |
| Hitoshi Akamatsu | people | Director of the first three Castlevanias | `games/castlevania`, `companies/konami` |
| Howard Delman | people | Built Atari's vector hardware, Lunar Lander and the Asteroids sounds; a Videa founder | `games/asteroids`, `techniques/vector-graphics`, `people/dona-bailey`, `people/ed-logg` |
| Hugh Riley | people | Artist of *The Last Ninja* and co-founder of Vivid Image | `games/the-last-ninja`, `people/john-twiddy`, `companies/system-3` |
| Ian Livingstone | people | Designed Eureka!, invested in Domark and chaired Eidos | `companies/domark`, `companies/eidos`, `games/tomb-raider` |
| Ivan Sutherland and Sketchpad | people | Where interactive graphics began | `hardware/light-pen`, `hardware/light-gun` |
| J. E. Sawyer | people | Lead designer of Icewind Dale and Fallout: New Vegas | `companies/black-isle-studios`, `companies/obsidian-entertainment`, `games/fallout-new-vegas` |
| Jack Friedman | people | Founded LJN, THQ and JAKKS Pacific | `companies/ljn` |
| Jaime Griesemer | people | Bungie designer on *Halo* | `techniques/enemy-design`, `games/halo`, `companies/bungie` |
| Jake Kazdal | people | *Rez* artist, later founder of 17-Bit | `companies/united-game-artists`, `games/rez` |
| James Follett | people | The novelist behind the *Starglider* novellas | `games/starglider`, `companies/rainbird` |
| Jane Jensen / Gabriel Knight | people | Sierra designer and her series, an SCI-32 launch title | `companies/sierra`, `people/roberta-williams`, `games/kings-quest`, `techniques/sci-engine` |
| Janice Hendricks (Woldenberg-Miller) | people | *Joust*'s animator, profiled in *Video Games* in 1983 | `games/joust`, `companies/williams-electronics` |
| Jason D. Anderson | people | Troika co-founder and *Fallout* artist, creative director on *Bloodlines*, later at inXile | `people/tim-cain`, `games/fallout`, `companies/troika-games`, `games/arcanum`, `phenomena/crpg-renaissance` |
| Jason Jones and Alex Seropian | people | Bungie's founders | `companies/bungie`, `games/halo` |
| Jason Kingsley | people | Rebellion's co-founder and chief executive since 1992 | `companies/rebellion`, `companies/core-design`, `companies/bitmap-brothers` |
| Jason Scott | people | Internet Archive software curator, involved in the Prince of Persia recovery and the Infocom source release | `communities/internet-archive`, `culture/game-preservation`, `games/prince-of-persia`, `companies/infocom`, `games/zork` |
| Jay Wilbur | people | id's chief executive, who designed the retail shareware scheme | `games/doom`, `companies/id-software`, `companies/softdisk` |
| Jeff Braun | people | Maxis co-founder and president | `companies/maxis`, `games/sim-city`, `people/will-wright` |
| Jeff Stephenson | people | Designer of SCI and co-designer of AGI | `techniques/agi-engine`, `techniques/sci-engine`, `companies/sierra`, `games/kings-quest` |
| Jeff, DeeKay and Graham | people | The musician, artist and coder behind *Deus Ex Machina*, recurring in Crest, Oxyron and Comaland | `demos/deus-ex-machina`, `groups/crest`, `groups/oxyron`, `demos/comaland` |
| Jenny Tyler | people | Co-author or editor of most of the Usborne games and adventure books | `books/usborne-computing-books`, `books/computer-battlegames`, `distribution/type-in-listings` |
| Jeremy Heath-Smith | people | Co-founded Core, ran it through the *Tomb Raider* years and later founded Circle Studio | `games/tomb-raider`, `companies/core-design`, `companies/gremlin-graphics` |
| Jeremy Soule | people | Composer of *Total Annihilation*, *Secret of Evermore*, *Icewind Dale* and *Dungeon Siege* | `games/total-annihilation` |
| Jerry Lawson | people | Designer of the Channel F and an early microprocessor arcade game | `hardware/cartridge`, `hardware/arcade-hardware` |
| Jess Cliffe | people | Co-creator of *Counter-Strike*, the game's voice, later a Valve designer | `games/counter-strike`, `companies/valve` |
| Jim Brain | people | Edited *C=Hacking* issues 11–15, and the comp.sys.cbm FAQ | `magazines/c-hacking` |
| Jim Mackonochie | people | Founded and ran Mirrorsoft, later at Commodore | `companies/mirrorsoft`, `phenomena/tetris-legal-battles` |
| Jochen Hippel | people | Atari ST composer whose sound system became part of Turrican II's seven-voice music | `people/chris-huelsbeck`, `hardware/paula`, `techniques/sound-drivers` |
| Joe Bostic | people | Designer and lead programmer of Dune II, Command & Conquer and Red Alert | `games/dune-ii`, `games/command-and-conquer`, `games/red-alert`, `games/warcraft` |
| Joe Lieberman | people | The senator who led the 1993 hearings and the push for ratings | `culture/congressional-hearings-1993`, `culture/esrb`, `games/mortal-kombat` |
| Joel Berez | people | Co-designer of the Z-machine and Infocom's president | `techniques/z-machine`, `companies/infocom` |
| Joel Billings | people | Founder of SSI | `genres/wargame` |
| John Broomhall | people | MicroProse composer of *Transport Tycoon*'s jazz score | `games/transport-tycoon` |
| John Coll | people | The BBC's technical adviser, co-presenter of the live shows and author of the BBC Micro User Guide | `people/ian-mcnaught-davis`, `phenomena/bbc-computer-literacy-project`, `systems/bbc-micro` |
| John Cumming | people | Graftgold's artist and Zynaps C64 programmer | `companies/graftgold`, `games/rainbow-islands`, `people/andrew-braybrook`, `games/zynaps` |
| John Foxx | people | Made the *Gods* soundtrack with Nation 12 | `games/gods` |
| John Gibson | people | Imagine programmer through whom the Liverpool scene's history runs | `companies/imagine-software`, `culture/liverpool-games-scene`, `companies/denton-designs`, `culture/basic-to-machine-code` |
| John Hollis | people | Quicksilva co-founder and author of *Games Designer* | `companies/quicksilva` |
| John M. Phillips | people | Programmer of *Nebulus*, *Impossaball* and *Eliminator* | `games/nebulus`, `companies/hewson-consultants`, `people/andrew-hewson` |
| John Madden | people | The coach and broadcaster whose name, playbook and 11-a-side insistence shaped EA's football games | `companies/ea-sports`, `games/madden`, `companies/electronic-arts`, `genres/sports-games` |
| John Newcomer | people | Designer of *Joust*, who came to video games from toys, and Boon's partner on *Super High Impact Football* | `companies/williams-electronics`, `games/joust`, `people/ed-boon`, `games/nba-jam` |
| John O'Brien | people | Ocean programmer of Spectrum/CPC Chase H.Q. | `games/chase-hq`, `companies/ocean-software` |
| John Salwitz and Dave Ralston | people | The *Paperboy* team, who went on to *720°*, *Cyberball* and *Rampart* | `games/paperboy`, `companies/atari-games` |
| Johnny Wilson | people | *CGW*'s editor and editor-in-chief in the 1990s | `magazines/computer-gaming-world` |
| Jon Freeman | people | Epyx co-founder who later made *Archon* at Free Fall Associates | `companies/epyx`, `people/chris-crawford`, `people/dan-bunten` |
| Jonathan Chey | people | Irrational co-founder and head of its Canberra studio | `companies/irrational-games`, `games/system-shock-2` |
| Jonathan Ellis | people | Psygnosis's business head, later at Sony Electronic Publishing Europe | `companies/psygnosis`, `people/ian-hetherington`, `people/roger-dean` |
| Jonathan Nash | people | *Amiga Power* writer at the centre of the Team17 dispute | `culture/amiga-power-versus-team17`, `magazines/amiga-power` |
| Josh Mandel | people | Sierra writer and designer (*Freddy Pharkas*, *Space Quest 6*) | `games/space-quest`, `people/al-lowe` |
| Jukka Tapanimäki | people | Finnish programmer of *Netherworld* and author of the Finnish C64 game-making guide | `techniques/multidirectional-scrolling` |
| Julian Eggebrecht | people | Factor 5's producer and spokesman from *Turrican* to *Lair* | `companies/factor-5`, `games/turrican`, `companies/rainbow-arts`, `people/manfred-trenz` |
| Justin Wong | people | The other half of Moment 37, an Evo champion in several games | `events/evo`, `communities/fighting-game-community` |
| Jürgen Friedrich | people | Wrote the 16-bit *Hard Drivin'* and *Hard Drivin' II* | `games/hard-drivin`, `companies/domark` |
| Karl Hilton | people | GoldenEye's artist | `games/goldeneye-007` |
| Katsuya Eguchi | people | Director of Star Fox | `games/star-fox` |
| Kazuhiko Nishi | people | ASCII co-founder and the driving force behind MSX | `systems/msx`, `companies/microsoft` |
| Kazunori Sawano | people | Worked on *Galaxian* and *Pole Position* | `games/galaxian`, `games/galaga`, `companies/namco`, `games/pole-position` |
| Kazunori Yamauchi | people | Creator of *Gran Turismo* and head of Polyphony Digital | `games/gran-turismo`, `companies/polyphony-digital`, `systems/sony-playstation` |
| Keith Burkhill | people | Elite's Spectrum programmer of Ghosts 'n Goblins and Space Harrier | `games/ghosts-n-goblins`, `companies/elite-systems`, `techniques/software-scroll`, `games/space-harrier` |
| Ken St. Andre | people | Creator of *Tunnels & Trolls* and a *Wasteland* designer | `games/wasteland` |
| Ken Williams | people | Sierra's co-founder and the programmer of *Mystery House* | `companies/sierra`, `people/roberta-williams`, `games/kings-quest`, `games/leisure-suit-larry`, `games/colossal-cave-adventure`, `techniques/agi-engine`, `techniques/sci-engine`, `people/al-lowe` |
| Kenji Sasaki | people | Directed *Sega Rally*, *Sega Rally 2* and *Sega Rally 2005/2006*, and a long-time Mizuguchi collaborator | `people/tetsuya-mizuguchi`, `games/sega-rally` |
| Kinuyo Yamashita | people | Composer of *Castlevania* | `games/castlevania` |
| Koichi Ishii | people | Creator of the Mana series and director of *Secret of Mana* and *Legend of Mana* | `games/secret-of-mana`, `companies/square`, `genres/action-rpg` |
| Koichi Nakamura | people | Chunsoft's founder, who proposed Dragon Quest | `games/dragon-quest`, `companies/chunsoft`, `people/yuji-horii` |
| Koichi Sugiyama | people | Dragon Quest's composer for 35 years | `genres/jrpg`, `games/dragon-quest`, `people/yuji-horii` |
| Kotaro Hayashida | people | Planner and scenario writer of *Phantasy Star* and *Alex Kidd* | `games/phantasy-star`, `games/alex-kidd` |
| Lance Barr | people | Nintendo of America designer of the NES case and the Zapper | `hardware/nes-zapper`, `systems/nintendo-entertainment-system` |
| Larry DeMar | people | Co-designer of Robotron and Stargate, and of Defender's attract mode | `games/defender`, `games/robotron-2084`, `people/eugene-jarvis`, `companies/williams-electronics` |
| Larry Rosenthal | people | Space Wars and Vectorbeam | `techniques/vector-graphics` |
| Lasse Öörni (Cadaver) | people | Author of *Metal Warrior* and GoatTracker, whose write-ups are the main C64 source on scrolling and tile maps | `techniques/scrolling`, `techniques/multidirectional-scrolling`, `techniques/tile-maps`, `techniques/pulse-width-modulation`, `culture/tracker-music`, `hardware/sid-chip` |
| Lauren Elliott | people | Carmen Sandiego co-designer and Wright's Gallium partner | `people/will-wright`, `companies/broderbund` |
| Len Lindsay / The PET Gazette | people | The newsletter COMPUTE! grew from | `magazines/compute-magazine` |
| Leonard Boyarsky | people | Troika co-founder, *Fallout*'s art director, *Diablo III* world designer and co-director of *The Outer Worlds* | `games/fallout`, `companies/troika-games`, `people/tim-cain`, `games/arcanum`, `companies/obsidian-entertainment` |
| Les Edgar | people | Bullfrog co-founder | `companies/bullfrog`, `games/populous`, `companies/electronic-arts`, `people/peter-molyneux` |
| Leslie Grimm | people | Co-designer of *Rocky's Boots* and *Robot Odyssey* | `games/robot-odyssey`, `companies/the-learning-company`, `games/rockys-boots` |
| Linus Åkesson (lft) | people | Explained the VSP crash; a C64 musician and demo coder | `techniques/vsp` |
| Liz Danforth | people | Drew *Wasteland*'s maps | `games/wasteland` |
| Lone Starr | people | Coder of *Wayfarer*, *State of the Art*, *Mobile* and *9 Fingers* | `groups/spaceballs`, `demos/state-of-the-art` |
| Lyle Rains | people | Atari coin-op engineering chief behind Tank, Asteroids and Asteroids Deluxe | `games/asteroids`, `people/ed-logg`, `companies/atari` |
| Makoto Kanoh | people | Producer of Super Metroid and early Metroid staff | `games/super-metroid`, `games/metroid`, `people/yoshio-sakamoto` |
| Marc Laidlaw | people | Writer of the *Half-Life* series | `games/half-life`, `games/half-life-2` |
| Marcus Dyson | people | *Amiga Format* editor turned Team17 development co-ordinator | `games/worms`, `companies/team17`, `magazines/amiga-format` |
| Mark Cale | people | Founder and still chief executive of System 3 | `companies/system-3`, `games/international-karate`, `games/the-last-ninja`, `people/john-twiddy` |
| Mark Coleman | people | Bitmap Brothers artist on *Speedball*, *Xenon 2*, *Gods* and *Magic Pockets*, often confused with Dan Malone | `games/xenon-2`, `games/gods`, `companies/bitmap-brothers`, `people/dan-malone` |
| Mark Cooksey | people | Composer of Elite's C64 conversions | `games/ghosts-n-goblins`, `companies/elite-systems` |
| Mark Crowe | people | Space Quest co-designer and Larry artist | `games/space-quest`, `companies/sierra`, `games/leisure-suit-larry` |
| Mark Eyles | people | Quicksilva designer, then of *Back to the Future* and *Aliens* at Electric Dreams | `companies/quicksilva`, `games/aliens`, `companies/electric-dreams` |
| Mark Overmars | people | Creator of Game Maker and a computer scientist at Utrecht | `tools/game-maker` |
| Mark Rein | people | Former id executive who ran Unreal engine licensing | `companies/epic-games`, `tools/unreal-engine`, `companies/id-software`, `games/unreal`, `people/tim-sweeney` |
| Mark Webley | people | Lionhead co-founder, *Theme Park* programmer and Two Point co-founder | `companies/bullfrog`, `companies/lionhead` |
| Martijn van der Heide | people | Founder of World of Spectrum and author of the Sinclair Infoseek | `tools/world-of-spectrum`, `emulators/fuse` |
| Martin Edmondson | people | Reflections' founder, the designer behind the *Beast* parallax | `games/shadow-of-the-beast`, `companies/psygnosis` |
| Martyn Brown | people | Team17 co-founder and producer on its Amiga games | `companies/team17`, `games/alien-breed`, `culture/amiga-power-versus-team17`, `people/andreas-tadic` |
| Martyn Carroll | people | *Retro Gamer*'s founding editor and the main source on its Live years | `magazines/retro-gamer`, `companies/imagine-publishing` |
| Marvin Minsky | people | Co-director of the MIT AI Lab and co-author of *Perceptrons* | `people/seymour-papert` |
| Masato Kato | people | Story designer of Chrono Trigger, writer of Chrono Cross | `games/chrono-trigger` |
| Matt Gray | people | C64 musician who wrote *Driller*'s 15-minute soundtrack | `games/driller` |
| Matt Householder and Craig Nelson | people | Project managers for the Epyx Games series | `games/summer-games`, `games/winter-games`, `games/california-games` |
| Matthew Cannon | people | Ocean composer (C64 *Batman: The Movie*, *The Untouchables*) | `people/jonathan-dunn`, `games/batman-the-movie`, `companies/ocean-software` |
| Max and Erich Schaefer | people | Condor co-founders, later Flagship and Torchlight | `games/diablo`, `companies/blizzard` |
| Mentor | people | Rune L. H. Stubbe, *Elevated*'s synth and optimisation and Crinkler co-author | `demos/elevated`, `techniques/size-coding` |
| Mev Dinc | people | Wrote the Spectrum *Last Ninja 2* and co-founded Vivid Image | `people/john-twiddy` |
| Michael A. Stackpole | people | Writer on *Wasteland* and *The Bard's Tale III* | `games/wasteland`, `companies/interplay` |
| Michael Abrash | people | Quake renderer programmer and author of the *Graphics Programming Black Book* | `games/quake`, `people/john-carmack`, `tools/id-tech` |
| Michael Cranford | people | Author of *The Bard's Tale* and Fargo's collaborator from the start | `people/brian-fargo`, `companies/interplay` |
| Michael Katz | people | Head of Sega of America in the Genesis's first year | `phenomena/console-wars`, `companies/sega` |
| Michael Morhaime | people | Blizzard co-founder | `companies/blizzard`, `games/warcraft` |
| Michael Toy, Glenn Wichman and Ken Arnold | people | *Rogue*'s authors; Arnold also wrote curses | `games/rogue`, `genres/roguelike`, `techniques/procedural-generation` |
| Michiru Yamane | people | Composer of *Symphony of the Night* and later *Castlevania* games | `people/koji-igarashi`, `games/symphony-of-the-night`, `games/castlevania` |
| Mike Kasprzak | people | Ludum Dare's organiser for most of its life | `communities/ludum-dare`, `culture/game-jams` |
| Mike Montgomery, Eric Matthews and Steve Kelly | people | The Bitmap Brothers' founders | `companies/bitmap-brothers`, `games/speedball-2` |
| Miles Jacobson | people | Sports Interactive's studio director since the 1990s and its public voice | `games/football-manager`, `companies/sports-interactive` |
| Minh Le | people | Creator of *Counter-Strike* | `games/counter-strike`, `games/half-life`, `communities/modding`, `companies/valve` |
| Mirko Buffoni | people | Ran MAME in 1997 | `emulators/mame`, `people/nicola-salmoria` |
| Mitchel Resnick | people | Papert's student, creator of Scratch and StarLogo | `people/seymour-papert`, `tools/scratch`, `tools/logo-language` |
| Moby | people | Frédéric Motte, musician on *Arte* and *Elektrik Funk* | `demos/arte`, `groups/sanity`, `people/jester`, `events/the-party` |
| Motohiro Kawashima | people | Co-composer of Streets of Rage 2 and 3 | `games/streets-of-rage`, `people/yuzo-koshiro` |
| Mr. H (Fredrik Huss) | people | The main author of FastTracker | `groups/triton`, `demos/crystal-dream` |
| Naoto Ohshima | people | Designed Sonic and *Phantasy Star*'s monsters, directed *Sonic CD* and *NiGHTS*, co-founded Artoon | `games/sonic-the-hedgehog`, `companies/sonic-team`, `games/phantasy-star`, `people/yuji-naka` |
| Nasir Gebelli | people | Apple II programmer who went on to program *Final Fantasy* I–III and *Secret of Mana* | `games/secret-of-mana`, `games/final-fantasy`, `companies/square` |
| Nick Alexander | people | Founded Virgin Games, ran Sega Europe, later chaired Future Publishing | `companies/virgin-games`, `companies/mastertronic`, `companies/sega` |
| Nick Bruty | people | Perry's artist partner from *Trantor* to *MDK* | `people/david-perry`, `companies/probe-software` |
| Nick Burcombe | people | Designed *WipEout* | `games/wipeout`, `companies/psygnosis` |
| Nick Gollop | people | Co-designer of X-COM credited by CGW | `games/x-com-ufo-defense`, `people/julian-gollop`, `games/laser-squad` |
| Nick Jones | people | Cecco's regular partner: C64 Cybernoid and Stormlord, Exolon's 128K sound, First Samurai's sound | `games/exolon`, `games/stormlord`, `people/raffaele-cecco`, `games/cybernoid` |
| Nick Lambert | people | Quicksilva's founder, whose ZX80 RAM pack started the company | `companies/quicksilva` |
| Nick Pelling | people | Frak! author and Amiga converter | `games/wing-commander`, `companies/mindscape` |
| Nigel Brownjohn | people | Animator of Raffaele Cecco's heroes | `games/exolon`, `games/stormlord` |
| Nobuyuki Matsushima | people | Mega Man's programmer and the two-sprite trick | `games/mega-man` |
| Noritaka Funamizu | people | *Street Fighter II* producer and the source of the combo story | `games/street-fighter-ii`, `companies/capcom` |
| Owen Garriott | people | Astronaut father who wrote the maths routines for Akalabeth and Ultima, and co-founded Encore | `people/richard-garriott`, `companies/origin-systems` |
| Paolo Nuti | people | Founder and editor of MC | `magazines/mc-microcomputer` |
| Pasi Ojala | people | Wrote *C=Hacking*'s Demo Corner and later compression articles (pucrunch) | `magazines/c-hacking`, `techniques/sprite-stretching`, `techniques/dycp`, `techniques/fli`, `techniques/tech-tech`, `techniques/open-borders`, `techniques/linecrunch` |
| Patricia Crowther | people | Caver and surveyor with a key part in the 1972 Flint Ridge–Mammoth connection | `people/will-crowther`, `games/colossal-cave-adventure` |
| Patrick Wyatt | people | Producer and lead programmer of Warcraft, later StarCraft and Battle.net | `games/warcraft`, `companies/blizzard` |
| Paul Allen | people | Microsoft co-founder who negotiated the 86-DOS purchase | `companies/microsoft`, `systems/trs-80` |
| Paul and Oliver Collyer | people | Founded Sports Interactive and created *Championship Manager* | `games/football-manager`, `genres/management-game`, `companies/domark`, `companies/sports-interactive` |
| Paul Cuisset | people | Delphine's lead designer, from Future Wars to Flashback and Flashback 2 | `games/flashback`, `companies/delphine-software`, `games/another-world`, `games/prince-of-persia`, `techniques/rotoscoping`, `people/eric-chahi` |
| Paul de Senneville | people | The composer whose record label paid for Delphine | `companies/delphine-software`, `games/flashback` |
| Paul Holmes | people | Led the team, with Andy Williams and Karen Trueman, behind Elite's Spectrum and Amstrad *Bomb Jack* and its sequel | `games/bomb-jack`, `companies/elite-systems` |
| Paul Neurath | people | Founder of Blue Sky Productions and Looking Glass, later Floodgate and OtherSide | `genres/immersive-sim`, `companies/looking-glass`, `companies/origin-systems`, `companies/arkane-studios`, `people/warren-spector`, `games/system-shock-2` |
| Paul Owens | people | Ocean programmer of *Gryzor* and *Cobra*'s scrolling | `games/contra`, `games/cobra`, `companies/ocean-software` |
| Paul Shirley | people | Wrote *Spindizzy*, later *Quartz* | `companies/electric-dreams` |
| Paul Woakes | people | Novagen's programmer (Encounter, Mercenary) | `techniques/open-world-design`, `companies/novagen` |
| Paula Byrne | people | Moved from Melbourne House's marketing to running Telecomsoft | `companies/telecomsoft`, `companies/rainbird`, `companies/firebird`, `companies/melbourne-house` |
| Pete Austin | people | Designer and public voice of Level 9 | `companies/level-9` |
| Peter Chan | people | Lead artist of *Day of the Tentacle*, and artist on *Grim Fandango* | `games/day-of-the-tentacle` |
| Peter Connor | people | *PCG* writer, then first editor of *Amstrad Action* and *ACE* | `magazines/personal-computer-games`, `magazines/amstrad-action`, `magazines/ace-magazine` |
| Peter Harrap | people | Monty Mole author and Krisalis co-founder | `companies/krisalis`, `companies/gremlin-graphics` |
| Peter Irvin and Jeremy Smith | people | Exile's authors; Irvin also wrote Acornsoft's Starship Command | `companies/acornsoft`, `companies/superior-software` |
| Peter Johnson | people | Ocean programmer on Arkanoid | `games/arkanoid`, `companies/ocean-software` |
| Peter Langston, David Fox, Gary Winnick, Dave Grossman and Brian Moriarty | people | Lucasfilm programmer on Maniac Mansion, designer of Zak McKracken | `companies/lucasarts`, `games/maniac-mansion`, `companies/infocom` |
| Peter Liepa | people | Designer of *Boulder Dash*, later a 3D software developer at Alias and Autodesk | `games/boulder-dash`, `techniques/puzzle-game-design` |
| Peter Main | people | Nintendo of America's sales chief during the rivalry, previously at Chuck E. Cheese's | `phenomena/console-wars`, `companies/nintendo` |
| Peter McConnell | people | Composer, co-creator of iMUSE with Michael Land, and writer of *Grim Fandango*'s score | `games/grim-fandango`, `techniques/scumm` |
| Peter Scott | people | Superior's "conversion king" (Barbarian, The Last Ninja, Sim City on the BBC Micro) | `companies/superior-software` |
| Peter Tuleby | people | Co-author of *Alien Breed* and Team 7 member | `people/andreas-tadic`, `companies/team17`, `games/alien-breed` |
| Philip Kendall | people | Author of Fuse for more than 25 years | `emulators/fuse`, `systems/sinclair-zx-spectrum` |
| Philip Mitchell | people | Programmer of *The Hobbit* and the adventure system behind *Sherlock* and *The Lord of the Rings* | `games/the-hobbit`, `companies/melbourne-house`, `genres/text-adventure`, `companies/beam-software` |
| Rand and Robyn Miller | people | Myst's creators | `games/myst`, `companies/cyan`, `companies/broderbund` |
| Ray Muzyka | people | BioWare co-founder | `companies/bioware`, `games/baldurs-gate` |
| Rebecca Heineman | people | 1980 Space Invaders champion, later a game programmer | `communities/esports-origins`, `games/space-invaders` |
| Renato Degiovani | people | *Micro Sistemas* editor, author of Brazilian adventures and Graphos III | `magazines/micro-sistemas`, `culture/brazilian-market-reserve`, `culture/brazil-gaming` |
| Rich Adam | people | Junior programmer on *Missile Command* and author of *Missile Command 2* | `games/missile-command`, `people/dave-theurer` |
| Richard Bannister | people | Prolific Mac emulator porter, quoted on cycle-exact emulation | `techniques/cycle-accuracy`, `emulators/emulation`, `techniques/emulators`, `people/byuu` |
| Richard Hanson | people | Founded Superior and ran it from 1982 to the present | `companies/superior-software`, `games/repton` |
| Richard Joseph | people | Musician for Palace, Sensible Software and the Bitmap Brothers | `games/cannon-fodder`, `companies/sensible-software`, `games/speedball-2`, `companies/bitmap-brothers`, `games/chaos-engine`, `games/gods` |
| Richard Turner | people | Artic Computing's founder | `people/charles-cecil`, `companies/tiertex` |
| Richard Wilcox | people | Wrote *Blue Thunder* and *Airwolf*, Elite's origin | `companies/elite-systems`, `people/steve-wilcox` |
| Rico Holmes | people | The artist on Andreas Tadic's games (*Alien Breed*, *Project-X*, *Superfrog*) | `companies/team17`, `games/alien-breed`, `people/andreas-tadic` |
| Rieko Kodama | people | One of the first widely known women in Japanese game development, artist on *Phantasy Star* and director of *Phantasy Star IV* | `games/phantasy-star`, `people/yuji-naka`, `companies/sega` |
| Rob Fulop | people | Programmed the 2600 *Missile Command* and *Night Driver*, then *Demon Attack* at Imagic | `techniques/fmv`, `games/missile-command`, `games/asteroids` |
| Rob Landeros | people | Co-creator of *The 7th Guest*, later of Aftermath Media | `games/7th-guest`, `people/graeme-devine` |
| Robert Cook | people | Ported Karateka to the C64 and Atari, later worked on The Last Express | `games/karateka`, `people/jordan-mechner` |
| Robert Maxwell | people | Mirrorsoft's owner, would-be buyer of Sinclair and a figure in the *Tetris* dispute | `companies/mirrorsoft`, `phenomena/tetris-legal-battles`, `companies/sinclair-research` |
| Robert Stein | people | The Andromeda agent who carried *Tetris* west | `games/tetris`, `phenomena/tetris-legal-battles`, `companies/mirrorsoft` |
| Robert Woodhead | people | Co-designer of Wizardry, who later worked in Japan | `games/wizardry`, `genres/western-rpg` |
| Robin Antonick | people | Designer of the original *Madden* and plaintiff in the royalties case | `games/madden`, `companies/electronic-arts` |
| Robin Candy | people | *CRASH* reviewer and tipster | `games/shadowfire`, `magazines/crash-magazine` |
| Rod Cousens | people | Quicksilva managing director, organiser of Soft Aid and founder of Electric Dreams | `companies/quicksilva`, `companies/electric-dreams`, `games/aliens`, `companies/activision`, `companies/codemasters` |
| Rodney Greenblat | people | The American artist behind *PaRappa*'s look and characters | `games/parappa-the-rapper`, `people/masaya-matsuura`, `companies/nanaon-sha`, `genres/music-games` |
| Roger Buoy | people | Mindscape's founder | `companies/mindscape` |
| Roy Trubshaw | people | Co-author of MUD | `genres/mmorpg-history`, `genres/mud-history`, `people/richard-bartle` |
| Russell Kay | people | DMA programmer on the PC *Lemmings*, later Visual Sciences | `games/lemmings`, `companies/dma-design`, `people/mike-dailly` |
| Russell Sipe | people | Founded *Computer Gaming World* and ran it for 14 years | `magazines/computer-gaming-world`, `magazines/electronic-games` |
| Sam Dicker | people | Programmer of *Defender*'s explosions and sound effects | `games/defender`, `people/eugene-jarvis` |
| Sam Houser and Dan Houser | people | Founders and creative leads of Rockstar | `companies/rockstar`, `games/grand-theft-auto`, `games/gta-iii`, `companies/rockstar-north` |
| Sam Houser, Dan Houser and Leslie Benzies | people | The people behind the Grand Theft Auto series | `games/gta-iii`, `companies/rockstar`, `companies/rockstar-north` |
| Sam Lake | people | Remedy's writer and creative director, and Max Payne's face | `companies/remedy-entertainment` |
| Samuli Syvähuoko | people | Gore, Future Crew's organiser and co-founder of Remedy | `people/psi`, `people/skaven`, `groups/future-crew`, `companies/remedy-entertainment` |
| Sandy Petersen | people | *Call of Cthulhu* designer who built much of Doom and Quake | `games/doom`, `games/quake`, `companies/id-software`, `people/john-romero` |
| Scorpia | people | CGW's role-playing columnist, cited across the RPG entries | `magazines/computer-gaming-world`, `companies/activision`, `games/ultima`, `games/wizardry`, `games/baldurs-gate`, `genres/western-rpg` |
| Scott Adams and Adventure International | people | Brought the adventure to 16K home computers with an interpreter | `genres/text-adventure`, `games/colossal-cave-adventure`, `systems/commodore-vic-20`, `systems/trs-80`, `people/will-crowther` |
| Scott Johnston and Brian Johnston | people | DMA's graphics and music on *Lemmings* | `games/lemmings` |
| Seamus Blackley and J Allard | people | The Xbox's technical and public leads | `systems/microsoft-xbox`, `culture/xbox-live` |
| Sean Cooper | people | Syndicate's project leader and Flood's author | `games/syndicate`, `companies/bullfrog` |
| Sean Ellis | people | Wrote GAC and STAC, then Freescape ports and the Superscape engine | `tools/graphic-adventure-creator`, `companies/incentive-software`, `games/driller`, `techniques/freescape` |
| Seiichi Ishii | people | Directed the first *Tekken* after *Virtua Fighter*, then founded Dream Factory | `games/virtua-fighter`, `games/tekken`, `people/katsuhiro-harada` |
| Seth Killian | people | Battle by the Bay co-founder who went on to Capcom and Sony Santa Monica | `events/evo`, `communities/fighting-game-community`, `companies/capcom` |
| Shaun Hollingworth | people | Gremlin and Krisalis programmer who wrote the Sega sound systems Furniss used | `companies/krisalis`, `companies/gremlin-graphics`, `people/matt-furniss`, `techniques/sound-drivers` |
| Shigeru Yokoyama | people | Designer of *Galaga* | `games/galaga`, `games/galaxian` |
| Shingo "Seabass" Takatsuka | people | Producer of *Winning Eleven* and *Pro Evolution Soccer* | `games/pro-evolution-soccer`, `companies/konami` |
| Shoichiro Irimajiri | people | Sega president who launched the Dreamcast and NAOMI | `systems/sega-dreamcast`, `systems/sega-naomi` |
| Shouzou Kaga | people | Creator of *Fire Emblem*'s scenario | `companies/intelligent-systems`, `games/fire-emblem` |
| Shuji Utsumi | people | Co-founder and chief executive of Q Entertainment | `companies/q-entertainment` |
| Sidney Sheinberg | people | Universal's president in the King Kong case | `culture/universal-vs-nintendo`, `people/howard-lincoln`, `games/donkey-kong` |
| Silas Warner | people | Muse's designer (*Castle Wolfenstein*, *Robotwar*) | `techniques/stealth-mechanics` |
| Simon Armstrong | people | Acid Software co-founder and *Blitz User* editor | `tools/blitz-basic-2`, `companies/acid-software`, `people/mark-sibly` |
| Simon Brattel | people | Programmer of Dark Star and Forbidden Planet, designer of Basil and Zeus | `companies/design-design`, `culture/basic-to-machine-code` |
| Simon Foster | people | Artist on *Transport Tycoon* and *RollerCoaster Tycoon* | `games/transport-tycoon`, `games/roller-coaster-tycoon`, `people/chris-sawyer` |
| Simon Goodwin | people | Prolific technical writer, with *CRASH* Tech Tips and more than a hundred published listings | `distribution/type-in-listings`, `techniques/copy-protection`, `techniques/emulators`, `emulators/emulation`, `emulators/winuae` |
| Sophie Wilson | people | Designed the System 1, BBC BASIC and the ARM instruction set | `companies/acorn-computers`, `systems/bbc-micro`, `systems/acorn-archimedes` |
| Stavros Fasoulas | people | The Finnish programmer whose Sanxion started Thalamus; Delta, Quedex | `companies/thalamus`, `people/rob-hubbard` |
| Stefano Arnhold | people | Tectoy's long-serving chief executive and the main witness to Sega in Brazil | `companies/tectoy`, `culture/brazil-gaming`, `systems/sega-master-system` |
| Steinar Lund and David Rowe | people | Cover artists who defined early British cassette art | `companies/quicksilva`, `games/ant-attack` |
| Stephen Judd | people | Edited *C=Hacking* issues 16–21; 3D graphics on the C64 | `magazines/c-hacking` |
| Stephen Ruddy | people | Programmer of C64 Bubble Bobble and NES Sky Shark, later FIFA | `games/bubble-bobble` |
| Stephen Streater | people | Eidos founder and Archimedes programmer | `companies/eidos`, `systems/acorn-archimedes` |
| Steve Bristow | people | Atari and Kee Games engineer, co-credited with *Breakout*'s concept and a key source for early Atari history | `games/breakout`, `companies/atari`, `games/pong` |
| Steve Ellis | people | GoldenEye's multiplayer programmer | `games/goldeneye-007` |
| Steve Furber | people | Designer of the BBC Micro and co-designer of ARM | `systems/bbc-micro`, `systems/acorn-archimedes`, `hardware/raspberry-pi`, `companies/acorn-computers` |
| Steve Jackson | people | Games Workshop co-founder and Lionhead co-founder | `companies/lionhead` |
| Steve Jarratt | people | *Edge*'s founding editor, also of *Commodore Format* and *Total!* | `magazines/edge`, `magazines/amiga-format`, `magazines/commodore-format`, `magazines/the-one`, `magazines/zzap-64` |
| Steve Jobs | people | Atari technician and Apple co-founder, central to the *Breakout* story | `games/breakout`, `companies/atari`, `people/nolan-bushnell` |
| Steve Purcell | people | Monkey Island artist and creator of Sam & Max | `games/monkey-island`, `games/sam-and-max`, `companies/lucasarts`, `companies/telltale` |
| Steve Ritchie | people | Pinball designer behind *Defender*'s flying idea | `people/eugene-jarvis`, `games/defender` |
| Steve Wozniak | people | Designer of the Apple I and II and of the *Breakout* prototype, who showed *Breakout* in BASIC at the Homebrew Computer Club | `systems/apple-ii`, `hardware/6502`, `games/breakout`, `people/al-alcorn` |
| Steven Poole / Trigger Happy | people | *Edge* columnist and author of *Trigger Happy* | `techniques/enemy-design` |
| Takahashi Meijin | people | Hudson's celebrity spokesman and the hero of Adventure Island | `companies/hudson-soft`, `games/adventure-island` |
| Takashi Iizuka | people | Designer of *NiGHTS*, behind *Sonic Adventure*, head of Sonic Team USA and later of Sonic Team | `companies/sonic-team`, `games/sonic-the-hedgehog` |
| Takashi Tateishi | people | Composer of *Mega Man 2* | `games/mega-man-2`, `people/manami-matsumae` |
| Takenobu Mitsuyoshi | people | Composer and singer of the Daytona USA soundtrack | `games/daytona-usa` |
| Ted Woolsey | people | Square's American translator (*Secret of Mana*, *Final Fantasy VI*, *Chrono Trigger*) | `games/secret-of-mana`, `games/chrono-trigger`, `genres/jrpg` |
| Terri Brosius | people | Voice of SHODAN, and designer and writer on Thief | `games/system-shock`, `games/system-shock-2`, `games/thief` |
| Tetsuya Nomura | people | Character designer of *Final Fantasy VII* | `games/final-fantasy-vii`, `companies/square` |
| Tim Anderson | people | Zork co-author and Infocom founder | `games/zork`, `companies/infocom` |
| Tim Chaney | people | Ran Virgin Games/VIE from 1991 to 1998 after U.S. Gold | `companies/virgin-games`, `companies/us-gold`, `games/cannon-fodder`, `companies/centresoft`, `companies/gremlin-graphics` |
| Tim Hartnell | people | Prolific type-in book author and editor who published many young programmers | `people/david-perry`, `distribution/type-in-listings` |
| Tim Tyler | people | Repton's 16-year-old author, whose royalties Superior used to recruit programmers | `companies/superior-software`, `games/repton` |
| Tim Wright | people | Psygnosis musician who rewrote the *Lemmings* music and scored *WipEout* | `games/lemmings`, `companies/psygnosis`, `games/wipeout` |
| Toby Gard | people | Created Lara Croft and co-founded Confounding Factor | `games/tomb-raider`, `companies/core-design`, `companies/eidos` |
| Todd Hollenshead | people | id's chief executive and QuakeCon's public face | `events/quakecon`, `companies/id-software` |
| Tom Hall | people | id co-founder, Keen's designer and author of the Doom Bible | `companies/id-software`, `games/doom`, `companies/ion-storm`, `people/john-romero`, `people/john-carmack`, `companies/apogee-software`, `companies/softdisk` |
| Tom Kalinske and Bernie Stolar | people | Sega of America's chief executive, 1990–96, central to the 16-bit rivalry and the ratings push | `systems/sega-saturn`, `systems/sega-dreamcast`, `companies/sega`, `phenomena/console-wars`, `systems/sega-mega-drive`, `games/sonic-the-hedgehog`, `culture/congressional-hearings-1993` |
| Tom Watson | people | Telecomsoft and Mirrorsoft marketer who ran Renegade | `companies/renegade` |
| Tony Mott | people | *Edge*'s longest-serving editor | `magazines/edge` |
| Tony Porter | people | Programmer of the Spectrum, Amstrad, MSX and Master System Gauntlet | `games/gauntlet`, `companies/us-gold`, `companies/gremlin-graphics` |
| Tony Quinn | people | Editor of Acorn User from 1982, then group editor | `magazines/acorn-user`, `games/elite`, `companies/acornsoft` |
| Tony Rainbird | people | Founder figure of two BT labels and the Silver range strategist | `companies/rainbird`, `companies/firebird`, `companies/telecomsoft` |
| Tony Warriner | people | Revolution co-founder and Virtual Theatre programmer | `companies/revolution-software`, `games/lure-of-the-temptress` |
| Toru Hagihara | people | Director of *Rondo of Blood* and *Symphony of the Night*, usually left out of the story | `games/symphony-of-the-night`, `games/castlevania`, `people/koji-igarashi` |
| Toshihiko Nakago | people | The programmer behind *Super Mario Bros.*, and the source of the arcade *Balloon Fight* | `games/super-mario-bros`, `games/super-mario-bros-3`, `games/balloon-fight`, `people/satoru-iwata` |
| Tsunekazu Ishihara | people | Producer, head of Creatures and The Pokémon Company | `games/pokemon-red-blue`, `companies/creatures-inc`, `people/satoru-iwata`, `companies/game-freak` |
| Two Guys from Andromeda | people | The *Space Quest* designers, from Sierra and Dynamix to *SQ7* and *SpaceVenture* | `companies/sierra`, `games/space-quest`, `games/leisure-suit-larry` |
| Vadim Gerasimov | people | Wrote the PC version of *Tetris* | `games/tetris`, `people/alexey-pajitnov` |
| Veronika Megler | people | Co-programmer of *The Hobbit*, who has written about it since | `games/the-hobbit`, `companies/melbourne-house`, `genres/text-adventure`, `companies/beam-software` |
| Walter Day | people | Founder of Twin Galaxies and a party to the Mitchell litigation | `events/twin-galaxies`, `communities/esports-origins` |
| Ward Christensen (CBBS and XMODEM) | people | Ran the first BBS and wrote the public-domain XMODEM protocol | `communities/bbs-scene`, `distribution/public-domain` |
| Warren Davis | people | Q*bert's programmer and the developer of Williams' video digitising | `games/mortal-kombat`, `techniques/digitized-sprites`, `games/qbert` |
| Wayne Green | people | Founder of *Byte*, *Kilobaud* and *80 Micro*, and adviser to *Micro Sistemas*' launch | `magazines/micro-sistemas`, `culture/magazines-across-borders` |
| Władysław M. Turski | people | Polish computer scientist, interviewed in Bajtek's first issue | `magazines/bajtek` |
| Yasunori Mitsuda | people | Composer of Chrono Trigger, Chrono Cross and Xenogears | `games/chrono-trigger`, `people/nobuo-uematsu`, `companies/square` |
| Yoji Shinkawa | people | *Metal Gear*'s artist from *Metal Gear Solid* onwards | `games/metal-gear-solid`, `people/hideo-kojima`, `companies/konami` |
| Yoshihisa Kishimoto | people | Designer of *Kunio-kun*/*Renegade* and *Double Dragon*, ex-Data East | `games/renegade`, `games/double-dragon`, `companies/technos`, `companies/data-east` |
| Yoshiki Funamizu | people | Street Fighter II producer | `games/street-fighter-ii`, `games/final-fight`, `companies/capcom` |
| Yoshinori Kitase | people | Director of *Final Fantasy VI* and *VII*, later head of the series | `people/hironobu-sakaguchi`, `games/final-fantasy-vii`, `companies/square`, `people/nobuo-uematsu` |
| Yoshitaka Amano and Tetsuya Nomura | people | Final Fantasy's character designers | `companies/square`, `games/final-fantasy`, `games/final-fantasy-vii` |
| Yves Guillemot | people | Ubisoft's founder and chief executive for forty years | `companies/ubisoft` |
| Zeb Cook | people | Creator of the Planescape setting | `games/planescape-torment` |

## Companies and organisations

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Nine Tiles | companies | The contractor that wrote Sinclair's BASIC ROMs | `people/steven-vickers`, `systems/sinclair-zx81`, `systems/sinclair-zx-spectrum`, `systems/sinclair-zx80`, `tools/sinclair-basic` |
| Amstrad | companies | Bought Sinclair's computer business in 1986 and made the +2 and +3; the Vault has the CPC but not the company | `companies/sinclair-research`, `systems/sinclair-zx-spectrum`, `people/clive-sinclair`, `systems/amstrad-cpc`, `culture/dundee-games-scene`, `distribution/piracy` |
| Timex | companies | Sinclair's US partner (Timex Sinclair) and one of its 1985 creditors | `companies/sinclair-research`, `systems/sinclair-zx81`, `systems/sinclair-zx-spectrum`, `culture/dundee-games-scene`, `people/dave-jones`, `culture/british-game-development` |
| Ferranti | companies | Made the uncommitted logic arrays in the ZX81 and Spectrum | `hardware/ula`, `systems/sinclair-zx81` |
| Sinclair Radionics | companies | Sinclair's earlier company; its collapse explains how Sinclair Research began | `companies/sinclair-research`, `people/clive-sinclair` |
| Jupiter Cantab | companies | Founded by ex-Sinclair engineers to make the Jupiter Ace | `companies/sinclair-research`, `systems/jupiter-ace` |
| Argus Press Software | companies | Bought Quicksilva and Bug-Byte and ran Bug-Byte as a budget label | `companies/bug-byte`, `companies/quicksilva`, `companies/namco`, `companies/grandslam` |
| Zilec Electronics | companies | The arcade company where the Stampers worked before Ultimate (*Blue Print*) | `people/stamper-brothers`, `companies/ultimate` |
| Dennis Publishing | companies | Published *Your Spectrum* and *Your Sinclair* until 1990 | `magazines/your-sinclair`, `magazines/your-spectrum` |
| ECC Publications | companies | Launched *Sinclair User* and *Sinclair Programs*; bought by EMAP in 1984 | `magazines/sinclair-user`, `magazines/sinclair-programs`, `companies/emap`, `magazines/computer-and-video-games` |
| Mattel Electronics | companies | Made the Intellivision; closed in the crash | `phenomena/1983-crash`, `systems/nintendo-entertainment-system`, `systems/intellivision`, `systems/colecovision`, `companies/gce`, `companies/milton-bradley` |
| Coleco | companies | ColecoVision's maker, which settled with Universal over *Donkey Kong* | `phenomena/1983-crash`, `games/donkey-kong`, `culture/universal-vs-nintendo`, `people/minoru-arakawa`, `systems/colecovision`, `systems/intellivision`, `games/zaxxon`, `games/galaxian` |
| General Instrument | companies | Made the AY-3-8910 family | `hardware/ay-3-8912`, `hardware/ay-3-8910` |
| DK'tronics | companies | Made Spectrum add-ons, including an AY sound box for the 48K | `hardware/ay-3-8912` |
| Escom | companies | Bought Commodore's assets in 1995 and restarted Amiga production | `systems/commodore-amiga`, `magazines/amiga-computing` |
| Metacomco | companies | Supplied AmigaDOS (from TRIPOS) and QL software | `systems/commodore-amiga`, `systems/sinclair-ql` |
| Ensoniq | companies | Founded by Charpentier and Yannes after Commodore | `people/al-charpentier`, `people/bob-yannes`, `hardware/sid-chip` |
| Texas Instruments | companies | Commodore's rival in the 1983 price war | `people/jack-tramiel` |
| Southwest Technical Products | companies | Advertised one of the first 6809 cards, in 1979 | `hardware/6809` |
| Maniacs of Noise | groups | Dutch game-music group named in the Paula entry | `hardware/paula`, `people/jeroen-tel`, `games/cybernoid`, `games/stormlord`, `communities/chiptune-scene`, `techniques/sound-drivers`, `companies/interplay`, `techniques/fpp` |
| Mandarin Software | companies | Europress's software label, which published STOS, AMOS and Level 9 | `companies/europress`, `tools/amos`, `tools/stos`, `companies/level-9`, `companies/rainbird`, `people/francois-lionet`, `companies/telecomsoft`, `companies/ariolasoft` |
| Jawx International | companies | The Paris company credited with STOS | `tools/stos`, `people/francois-lionet`, `tools/amos` |
| Paradox Group | companies | *Commodore User*'s first publisher, not the warez group | `magazines/cu-amiga`, `companies/emap` |
| Microelectrónica y Control | companies | Commodore's Spanish distributor and *Club Commodore*'s publisher | `magazines/club-commodore`, `culture/magazines-across-borders`, `companies/commodore` |
| Parker Brothers | companies | A major 2600 publisher with its own bank-switching scheme | `techniques/bank-switching`, `systems/atari-2600`, `companies/konami`, `companies/sega`, `games/frogger`, `companies/milton-bradley` |
| Western Technologies | companies | Designed the Vectrex hardware and games | `systems/vectrex`, `companies/gce`, `companies/milton-bradley` |
| Bandai | companies | Made the WonderSwan and the *Space Chaser* handheld, and merged with Namco | `people/gunpei-yokoi`, `hardware/d-pad`, `companies/namco`, `companies/capcom`, `hardware/power-pad` |
| CGL (Computer Games Ltd) | companies | Distributed Game & Watch in Britain | `systems/nintendo-game-and-watch` |
| Elorg | companies | The Soviet agency that licensed *Tetris* | `phenomena/tetris-legal-battles`, `people/minoru-arakawa`, `people/henk-rogers`, `people/alexey-pajitnov`, `games/tetris` |
| Access Software | companies | Made *Beach-Head*, U.S. Gold's first licence | `companies/us-gold`, `companies/centresoft` |
| GO! | companies | U.S. Gold's full-price label for *Street Fighter* and *Bionic Commando* | `companies/us-gold`, `companies/centresoft`, `companies/capcom` |
| Artic Computing | companies | Where Tiertex's founders and Charles Cecil started | `companies/tiertex`, `companies/us-gold`, `people/charles-cecil`, `people/jon-ritman`, `games/match-day`, `tools/zxas` |
| HesWare | companies | Jeff Minter's American publisher | `people/jeff-minter`, `companies/llamasoft`, `games/summer-games`, `people/ron-gilbert` |
| Imagine Media | companies | Chris Anderson's American publisher; not the Bournemouth Imagine Publishing | `people/chris-anderson`, `companies/future-publishing` |
| Datel Electronics | companies | The Stoke-on-Trent maker of the Action Replay and other Commodore utilities | `hardware/action-replay`, `techniques/disk-fastloaders`, `techniques/fast-loader`, `hardware/multiface`, `techniques/rumble-pak` |
| Imagic | companies | The second cartridge maker founded by ex-Atari staff | `culture/atari-vs-activision`, `systems/atari-2600`, `systems/intellivision`, `phenomena/1983-crash` |
| 21st Century Entertainment | companies | Hewson's successor and the publisher of *Pinball Dreams* | `companies/hewson-consultants`, `people/andrew-hewson`, `companies/dice-studio`, `games/nebulus` |
| Special FX | companies | Ocean's Liverpool spin-off studio, founded by Paul Finnegan | `companies/ocean-software`, `people/jonathan-smith`, `games/batman-1986`, `companies/imagine-software`, `games/batman-the-movie`, `people/jim-bagley`, `culture/liverpool-games-scene` |
| MC Lothlorien | companies | Spectrum strategy publisher the 1985 press quoted on royalties and budget prices | `phenomena/bedroom-coder`, `distribution/budget-games`, `genres/wargame` |
| Gremlin Industries | companies | The San Diego arcade maker Sega bought; not Gremlin Graphics | `companies/sega`, `games/zaxxon`, `games/frogger` |
| Stern Electronics | companies | Konami's US licensee for *Scramble* and *Super Cobra* | `companies/konami`, `games/scramble`, `systems/vectrex`, `phenomena/golden-age-arcade` |
| Ultra Games | companies | Konami's second US NES label, publisher of *Teenage Mutant Ninja Turtles* | `companies/konami`, `games/tmnt-arcade`, `systems/nintendo-entertainment-system` |
| Absolute Entertainment | companies | Garry Kitchen's ex-Activision studio, where Crane made *A Boy and His Blob* | `people/david-crane`, `companies/activision` |
| Arcadia Systems | companies | Mastertronic's Amiga-based coin-op business | `companies/mastertronic`, `systems/sega-master-system`, `systems/commodore-amiga` |
| Software Creations | companies | The Manchester conversion house behind *Bionic Commando* and *Forgotten Worlds* | `companies/capcom`, `companies/us-gold`, `companies/sony`, `techniques/software-scroll`, `people/tim-follin`, `games/ghouls-n-ghosts`, `games/bubble-bobble`, `techniques/sound-drivers`, `techniques/filmation-engine`, `techniques/isometric-projection`, `games/bionic-commando` |
| Torus | companies | Converted *Elite* to the Spectrum and wrote *Gyron* | `games/elite`, `companies/firebird` |
| Imagineer | companies | Published the NES *Elite* | `games/elite`, `games/populous` |
| Federation Against Software Theft (FAST) | companies | Britain's software anti-piracy body from 1984 | `communities/cracking-scene`, `distribution/piracy`, `techniques/copy-protection`, `phenomena/guild-of-software-houses`, `communities/bbs-scene`, `hardware/multiface` |
| ELSPA | companies | The trade body whose Crime Unit ran the 1990s piracy raids | `communities/cracking-scene`, `distribution/piracy`, `distribution/cover-tapes`, `techniques/copy-protection`, `distribution/magazine-cover-disks`, `culture/game-ratings`, `distribution/budget-games`, `people/andrew-hewson` |
| GameTek | companies | Published both *Frontier* games; Braben took it to court over *First Encounters* | `people/david-braben`, `companies/frontier-developments`, `games/elite` |
| Camerica | companies | Published Codemasters' unlicensed NES games and made the Game Genie in Canada | `companies/codemasters`, `people/oliver-twins`, `hardware/game-genie`, `games/micro-machines`, `games/dizzy`, `people/darling-brothers` |
| Big Red Software | companies | Wrote the *Dizzy* adventures after *Fantasy World Dizzy* | `people/oliver-twins`, `games/dizzy`, `companies/codemasters`, `companies/eidos`, `companies/domark` |
| Interactive Studios (Blitz Games) | companies | The Oliver twins' own development studio | `people/oliver-twins`, `games/dizzy` |
| Nanao | companies | Irem's parent and designer of the *R-Type* hardware; not NanaOn-Sha | `companies/irem` |
| Microdeal | companies | The Dragon's main games publisher, whose *Cuthbert in the Jungle* Activision challenged | `games/pitfall`, `systems/dragon-32` |
| SSI (Strategic Simulations) | companies | The American wargame publisher behind *Computer Bismarck* | `people/trip-hawkins`, `companies/electronic-arts`, `techniques/code-wheels`, `techniques/manual-protection`, `magazines/computer-gaming-world`, `genres/wargame`, `genres/sports-games`, `companies/the-learning-company`, `companies/mindscape`, `genres/western-rpg`, `companies/westwood-studios`, `genres/rts-genre`, `genres/simulation-games`, `people/dan-bunten`, `games/baldurs-gate`, `games/wizardry`, `people/louis-castle`, `techniques/turn-based-combat`, `companies/us-gold` |
| Xerox PARC | companies | Where the Alto and much of the 1980s graphical interface began | `people/dan-silva` |
| Delta 4 | companies | Fergus McNeill's group, the best-known writers of Quilled comedy adventures | `tools/the-quill`, `tools/paw`, `companies/gilsoft`, `genres/text-adventure`, `people/tim-gilberts` |
| Reflections | companies | Martin Edmondson's studio, which made *Shadow of the Beast* | `techniques/parallax-scrolling`, `games/shadow-of-the-beast`, `companies/psygnosis` |
| General Computer Corporation | companies | Wrote *Ms. Pac-Man*, then Atari 7800 hardware and games | `games/pac-man`, `companies/atari` |
| Tengen | companies | Atari Games' home label, which fought Nintendo's lockout | `companies/atari-games`, `companies/atari`, `companies/namco`, `games/pac-man`, `people/howard-lincoln`, `phenomena/tetris-legal-battles`, `systems/atari-lynx`, `companies/nintendo`, `phenomena/nintendo-seal`, `games/gauntlet`, `companies/domark`, `people/ed-logg`, `games/hard-drivin`, `games/paperboy` |
| Atarisoft | companies | Atari's label for other machines, the route most British players took to Namco games | `companies/namco`, `games/pac-man`, `companies/atari`, `games/defender`, `games/space-invaders`, `games/galaxian`, `games/centipede`, `games/pole-position`, `games/battlezone`, `games/asteroids` |
| Pulsonic | companies | The first cut-price range, at £2.95 in March 1984 | `distribution/budget-games`, `companies/mastertronic` |
| The Hit Squad, Encore and Rack-It | companies | The re-release labels of Ocean, Elite and Hewson | `distribution/budget-games`, `companies/ocean-software`, `companies/elite-systems`, `companies/hewson-consultants`, `games/head-over-heels`, `games/driller`, `games/uridium`, `games/paradroid`, `games/bomb-jack`, `systems/commodore-16`, `companies/centresoft` |
| Fusion | groups | British C64 crew that topped *Illegal*'s chart and gave it an interview | `magazines/illegal`, `groups/triad`, `communities/cracking-scene`, `communities/crack-intros`, `people/jeff-smart` |
| Infinity Ward | companies | The studio behind *Call of Duty*, and its 2010 dispute with Activision | `companies/activision`, `companies/electronic-arts` |
| Raven Software | companies | The Wisconsin studio behind *Heretic* and *Hexen*, bought by Activision in 1997 | `companies/activision`, `companies/id-software`, `tools/id-tech`, `people/john-romero` |
| Pandemic Studios and Visceral Games | companies | EA studios bought or built, then closed | `companies/electronic-arts`, `companies/bioware` |
| The Creative Assembly | companies | British studio from 8-bit sports conversions to *Total War*, owned by Sega since 2005 | `companies/sega`, `games/alien-isolation`, `culture/british-game-development`, `genres/rts-genre` |
| Sammy | companies | The pachinko maker that bought Sega and formed Sega Sammy Holdings | `companies/sega` |
| M2 | companies | The Tokyo porting and emulation studio behind the Mega Drive Mini | `companies/sega`, `systems/sega-mega-drive`, `culture/game-preservation` |
| 17-Bit Software | companies | Wakefield public-domain library whose charts and disk numbers Amiga demo entries cite | `companies/team17`, `people/andreas-tadic`, `demos/hardwired`, `distribution/public-domain`, `demos/jesus-on-es`, `demos/state-of-the-art`, `demos/voyage` |
| 22cans | companies | Guildford-cluster studio | `people/peter-molyneux`, `genres/god-games`, `games/populous`, `companies/lionhead`, `culture/guildford-games-cluster` |
| 3dfx and the Voodoo | companies | The cancelled Saturn-successor contract, and the card GLQuake targeted | `systems/sega-dreamcast`, `games/quake`, `culture/pc-gaming` |
| 4J Studios | companies | Dundee studio behind *Minecraft*'s console editions and the *Perfect Dark* remaster | `games/minecraft`, `culture/dundee-games-scene`, `games/perfect-dark` |
| 4Mation | companies | The Barnstaple educational publisher (Granny's Garden, Flowers of Crystal) | `games/grannys-garden`, `culture/educational-software` |
| Abertay University and Dare to be Digital | companies | Dundee's games degree and student contest | `culture/dundee-games-scene`, `companies/dma-design` |
| Addison-Wesley | companies | Acorn User's first publisher | `magazines/acorn-user`, `magazines/micro-user` |
| Adeline Software | companies | The studio behind Little Big Adventure | `companies/delphine-software`, `companies/infogrames` |
| Adventure International | companies | Scott Adams's publisher, a major early home-computer adventure house | `games/colossal-cave-adventure`, `genres/text-adventure`, `people/will-crowther` |
| Aegis Development | companies | Publisher of Videoscape 3D, Sonix and Aegis Draw | `tools/lightwave-3d`, `tools/sculpt-3d` |
| Alphavite Publications and Commodore Power | companies | Your Commodore's last publisher and its successor title | `magazines/your-commodore` |
| Amblin Imaging | companies | The *seaQuest DSV* Toaster facility | `tools/lightwave-3d`, `hardware/video-toaster` |
| Analogue | companies | The commercial FPGA console maker | `hardware/mister-fpga`, `emulators/emulation` |
| Ancient | companies | Koshiro's family studio since 1990 (8-bit *Sonic*, *Thor*, *Earthion*) | `games/sonic-the-hedgehog`, `people/yuzo-koshiro`, `games/streets-of-rage` |
| Andromeda Software and Robert Stein | companies | The Hungarian company that programmed Eureka! and Golf and connects Domark to Tetris | `companies/domark`, `games/tetris`, `phenomena/tetris-legal-battles`, `companies/ariolasoft` |
| Angel Studios / Rockstar San Diego | companies | *Midnight Club* and *Red Dead* | `companies/rockstar` |
| Anirog Software | companies | Anil Gupta's earlier Dartford publisher (*Flight Path 737*) | `companies/anco` |
| Apex Computer Productions | companies | John and Steve Rowlands' company, the best-known commercial VSP users (*Creatures*, *Mayhem in Monsterland*) | `companies/thalamus`, `techniques/vsp`, `techniques/agsp`, `magazines/commodore-format`, `techniques/parallax-scrolling` |
| Apple Computer | companies | The Apple II's maker | `systems/apple-ii`, `games/lode-runner`, `people/trip-hawkins` |
| Arc System Works | companies | Owner of the Technos games since 2015 | `companies/technos`, `games/double-dragon`, `games/river-city-ransom` |
| Argus Specialist Publications | companies | Publisher of Your Commodore, Commodore Disk User and 64 Tape Computing | `magazines/your-commodore`, `culture/disk-magazines` |
| Artoon | companies | Ohshima's studio (*Blinx*, *Yoshi's Universal Gravitation*) | `companies/sonic-team` |
| Aruze | companies | The pachinko maker that bought SNK in 2000 | `companies/snk`, `systems/neo-geo`, `systems/neo-geo-pocket` |
| ASCII Corporation | companies | MSX co-owner and Microsoft's Far East partner | `systems/msx`, `companies/microsoft` |
| ASDG | companies | Maker of Art Department Professional and MorphPlus, the real source of the *Quantum Leap* morphs | `tools/lightwave-3d` |
| Atari Program Exchange (APX) | companies | Atari's label for user-written software | `people/chris-crawford`, `systems/atari-8-bit` |
| Avalon Hill | companies | The board and computer game publisher behind the *Civilization* dispute | `games/civilization`, `companies/microprose`, `people/chris-crawford`, `genres/wargame`, `genres/rts-genre` |
| Aventuras AD | companies | Spanish adventure publisher | `tools/paw`, `people/tim-gilberts` |
| Bally and Dave Nutting Associates | companies | Midway's parent and the in-house studio behind *Gorf*, *Wizard of Wor* and *Sea Wolf* | `companies/midway` |
| BBN and ARPANET | companies | The network Adventure spread across | `people/will-crowther`, `games/colossal-cave-adventure`, `games/zork` |
| Beamdog | companies | Trent Oster's studio, maker of the Enhanced Editions of the Infinity Engine games | `companies/bioware`, `games/baldurs-gate`, `games/planescape-torment`, `games/icewind-dale` |
| Big Blue Box | companies | Lionhead satellite that made *Fable* | `companies/lionhead`, `games/fable` |
| Binary Design | companies | Manchester developer of *Glider Rider*, *Amaurote* and the *Double Dragon* conversions | `people/david-whittaker`, `companies/quicksilva`, `games/double-dragon`, `companies/melbourne-house` |
| Bitboys | companies | Finnish graphics-chip company started by Future Crew's Trug | `groups/future-crew`, `people/psi`, `people/wildfire`, `companies/futuremark` |
| Bizarre Creations | companies | Liverpool studio behind Formula 1, MSR, Project Gotham Racing and Geometry Wars | `companies/psygnosis`, `culture/liverpool-games-scene`, `games/geometry-wars` |
| Blade Software | companies | The 1989 publisher of Laser Squad and Lords of Chaos, tied to Krisalis | `games/laser-squad`, `people/julian-gollop`, `companies/krisalis` |
| bleem! | companies | The commercial PlayStation emulator Sony failed to stop in court | `emulators/emulation`, `systems/sony-playstation`, `systems/sega-dreamcast`, `culture/sony-vs-connectix`, `emulators/pcsx` |
| Blizzard North | companies | Condor, the Diablo studio, with its own arc from 1993 to 2005 | `companies/blizzard`, `games/diablo` |
| Blue Byte | companies | German studio co-founded by ex-Rainbow Arts Thomas Hertzler (*Battle Isle*, *The Settlers*) | `companies/rainbow-arts`, `companies/ubisoft` |
| Blue Fang Games | companies | *Zoo Tycoon*'s developer | `genres/tycoon-games` |
| BMG Interactive | companies | The original publisher of *GTA* | `companies/dma-design`, `games/grand-theft-auto`, `companies/rockstar-north`, `companies/rockstar` |
| Bugbear Entertainment | companies | Finnish studio of *FlatOut* and *Wreckfest*, named by *Edge* as Future Crew-founded | `groups/future-crew`, `companies/futuremark`, `companies/remedy-entertainment` |
| Bullet-Proof Software | companies | Henk Rogers's company, publisher of *The Black Onyx* and Famicom *Tetris* | `games/tetris`, `people/henk-rogers`, `phenomena/tetris-legal-battles`, `people/alexey-pajitnov` |
| Byte by Byte | companies | Publisher of Sculpt 3D, Animate 3D and Sculpt-Animate 4D | `tools/sculpt-3d`, `people/eric-graham`, `culture/the-juggler` |
| Cases Computer Simulations | companies | An early British strategy and management publisher (*Airline*, *Autochef*) | `genres/wargame`, `genres/management-game`, `genres/simulation-games` |
| Cave | companies | The Toaplan successor behind DonPachi, DoDonPachi and Mushihime-sama | `genres/shoot-em-up`, `companies/toaplan` |
| CBS Software (UK) | companies | Epyx's first British channel | `games/impossible-mission`, `games/summer-games`, `companies/epyx` |
| CBS Software and K-tel software | companies | The other record-company software labels | `phenomena/record-companies-in-software` |
| Central Point Software | companies | Sold the Copy II copiers for the Apple II, PC, Mac and C64, and later PC Tools | `techniques/disk-protection` |
| CH Products | companies | Maker of the Force FX and flight controllers | `techniques/force-feedback`, `hardware/flight-stick` |
| CH Products and Thrustmaster | companies | The two PC flight-stick makers | `hardware/flight-stick`, `hardware/steering-wheel` |
| Choice Software | companies | Programmed Ocean's Spectrum *Mario Bros.* | `games/mario-bros`, `companies/ocean-software` |
| Chuck E. Cheese's Pizza Time Theatre | companies | Bushnell's arcade-restaurant chain, where Nintendo's Peter Main came from | `people/nolan-bushnell`, `companies/nintendo` |
| Cinematronics | companies | Vector games in the arcades before *Asteroids*, from *Space Wars* (1977) to *Tail Gunner* | `techniques/vector-graphics`, `systems/vectrex`, `phenomena/golden-age-arcade`, `games/asteroids`, `games/battlezone` |
| Clover Studio and Platinum Games | companies | The studios Mikami's later career ran through | `people/shinji-mikami`, `companies/capcom` |
| Comcept | companies | Inafune's company | `people/keiji-inafune` |
| Commodore's Corby factory | companies | The British plant that built C64s for Europe | `companies/commodore`, `systems/commodore-64`, `culture/the-c64-across-borders` |
| CompuServe | companies | *DecWars*, *MegaWars* and *Island of Kesmai* | `culture/online-multiplayer`, `genres/mmorpg-history`, `communities/bbs-scene` |
| Cranberry Source and Super Match Soccer | companies | Ritman's own company and the last *Match Day* game | `people/jon-ritman`, `games/match-day` |
| Crawfish Interactive | companies | Croydon handheld specialist founded in 1997 | `systems/game-boy-advance`, `companies/bitmap-brothers`, `games/speedball-2` |
| Creative Materials | companies | The Bury studio behind U.S. Gold's *Street Fighter II* and *Final Fight* conversions | `games/street-fighter-ii`, `companies/us-gold`, `games/final-fight` |
| Creative Sparks (Thorn EMI) | companies | The largest record-industry software label after Virgin and Ariolasoft | `phenomena/record-companies-in-software` |
| Cronosoft | companies | Publisher of new 8-bit games on tape, started on the WoS forums in 2003 | `tools/world-of-spectrum`, `people/jonathan-cauldwell`, `tools/arcade-game-designer` |
| Crystal Dynamics | companies | 3DO launch developer (Gex, Legacy of Kain), an Eidos studio from 1998 and later Tomb Raider's | `companies/eidos`, `games/tomb-raider`, `games/deus-ex`, `companies/square`, `people/mark-cerny`, `companies/core-design` |
| Cyan Engineering | companies | Atari's Grass Valley engineering firm, not the *Myst* studio | `games/breakout`, `companies/atari` |
| Datasoft | companies | The American publisher behind U.S. Gold's early imports (*Kung Fu Master*, *Pole Position II*, *Alternate Reality*) | `games/zaxxon`, `games/kung-fu-master`, `companies/us-gold` |
| Davidson & Associates and Math Blaster | companies | A major educational rival to The Learning Company | `companies/the-learning-company`, `companies/mecc`, `culture/educational-software`, `companies/blizzard`, `companies/sierra` |
| Dendy and Steepler | companies | The Russian famiclone and its seller | `systems/famiclone`, `systems/nintendo-entertainment-system` |
| Digital Anvil | companies | Roberts's Austin studio, 1996–2001 (Starlancer, Freelancer), bought by Microsoft | `people/martin-galway`, `people/chris-roberts`, `games/wing-commander`, `companies/origin-systems` |
| Digital Eclipse | companies | Maker of the 2024 Wizardry remake, The Making of Karateka and other preservation releases | `games/wizardry` |
| Digital Extremes | companies | *Unreal*'s co-developer, later *Pariah* and *Warframe* | `companies/epic-games`, `games/unreal`, `tools/unreal-engine` |
| Digital Integration | companies | UK simulation house and the most committed Lenslok user (*Tomahawk*, *TT Racer*) | `techniques/lenslock`, `techniques/copy-protection`, `genres/simulation-games`, `genres/flight-sim` |
| Digital Pictures | companies | Tom Zito's FMV studio (Night Trap, Sewer Shark) | `techniques/fmv`, `games/7th-guest`, `culture/congressional-hearings-1993` |
| Dinamic | companies | The Madrid publisher of Camelot Warriors | `companies/ariolasoft`, `companies/alternative-software` |
| Discovery Software | companies | US Amiga publisher of Arkanoid | `games/arkanoid` |
| Double Fine Productions | companies | Tim Schafer's studio: *Psychonauts*, the LucasArts remasters, and *Broken Age*, the Kickstarter that began the adventure and CRPG revivals | `companies/lucasarts`, `people/tim-schafer`, `culture/game-jams`, `culture/indie-games`, `companies/microsoft`, `people/ron-gilbert`, `techniques/point-and-click`, `genres/graphic-adventure`, `games/day-of-the-tentacle`, `games/grim-fandango`, `phenomena/crpg-renaissance`, `genres/western-rpg` |
| Drean | companies | The Argentine licensee that built C64s at San Luis | `magazines/drean-commodore`, `culture/the-c64-across-borders` |
| Dynamix and Coktel Vision | companies | Sierra's Eugene studio: *Space Quest V*, *Heart of China*, *Red Baron* | `companies/sierra`, `games/space-quest` |
| EA Tiburon | companies | The Orlando studio that made *Madden* from the mid-1990s | `games/madden`, `companies/ea-sports` |
| Eclipse | companies | Acorn publisher of the RISC OS Dune II | `games/dune-ii`, `systems/acorn-archimedes` |
| Eidos-Montréal | companies | The studio behind Human Revolution and Mankind Divided | `games/deus-ex`, `companies/eidos`, `companies/square` |
| Enchanted Scepters and Silicon Beach Software | companies | The Mac's first adventure-construction system (World Builder), its one commercial game, and Dark Castle's maker | `techniques/point-and-click`, `companies/mindscape` |
| Enhance | companies | Mizuguchi's company since 2014, which made *Rez Infinite*, *Tetris Effect* and *Lumines Arise* | `people/tetsuya-mizuguchi`, `companies/q-entertainment`, `games/rez`, `games/lumines` |
| Epyx's Rogue / A.I. Design | companies | The first company to sell a roguelike | `games/rogue`, `companies/epyx`, `genres/roguelike` |
| ERE Informatique and Exxos | companies | French publisher of *Bubble Ghost* and *Captain Blood* | `companies/infogrames`, `companies/delphine-software`, `companies/pss` |
| Eurohard | companies | The Spanish company that bought the Dragon in 1984 | `systems/dragon-32`, `systems/dragon-64`, `companies/dragon-data` |
| Evolution Studios | companies | The Runcorn studio behind WRC and MotorStorm | `culture/liverpool-games-scene`, `people/ian-hetherington`, `companies/psygnosis` |
| Exidy | companies | Arcade maker, with its Max-A-Flex cabinet | `games/boulder-dash` |
| Extended Play Productions / EA Canada | companies | The Canadian developer of the first *FIFA*, which became EA Canada (*FIFA*, *NHL*, *Need for Speed*) | `companies/ea-sports`, `games/fifa`, `companies/electronic-arts` |
| Firaxis Games | companies | Meier's studio from 1996, maker of *Civilization III* onwards and *XCOM* | `companies/microprose`, `people/sid-meier`, `games/civilization`, `games/xcom-enemy-unknown`, `games/x-com-ufo-defense` |
| Firesprite | companies | The post-2012 Liverpool studio bought by Sony | `culture/liverpool-games-scene`, `companies/psygnosis` |
| First Star Software | companies | Publisher of Boulder Dash and Spy vs Spy | `games/boulder-dash`, `games/spy-vs-spy`, `systems/atari-8-bit` |
| Foundation Imaging | companies | Ron Thornton's *Babylon 5* effects house | `hardware/video-toaster`, `tools/lightwave-3d`, `tools/imagine` |
| Free Radical Design | companies | The studio the *GoldenEye* and *Perfect Dark* team founded | `games/goldeneye-007`, `companies/rare`, `games/perfect-dark`, `games/fifa` |
| FreeStyleGames | companies | Made *DJ Hero* and *Guitar Hero Live* | `games/guitar-hero` |
| Frognation | companies | The UK localisation firm for the *Souls* games | `games/dark-souls`, `games/demons-souls` |
| Front Runner (K-Tel) | companies | Published the Spectrum Boulder Dash | `games/boulder-dash` |
| FTL Games | companies | Made *SunDog*, *Dungeon Master*, *Oids* and *Chaos Strikes Back* | `games/dungeon-master`, `systems/atari-st`, `companies/mirrorsoft` |
| Funcom | companies | Norwegian developer that hired sceners and advertised in *R.A.W.* | `groups/spaceballs`, `communities/demo-scene`, `groups/melon-dezign`, `techniques/super-fx-chip` |
| Games Workshop | companies | Livingstone's company, which published Chaos; its Warlock inspired Chaos | `people/julian-gollop`, `companies/domark` |
| Gas Powered Games | companies | Chris Taylor's studio after Cavedog | `games/total-annihilation`, `games/supreme-commander` |
| Gathering of Developers | companies | Publishing co-operative with Epic and 3D Realms | `companies/remedy-entertainment`, `companies/3d-realms`, `people/scott-miller`, `companies/epic-games` |
| Gearbox Software | companies | Made *Opposing Force* and the *Halo* PC port; Randy Pitchford spoke for developers at Xbox Live's launch | `companies/3d-realms`, `games/half-life`, `games/halo`, `culture/xbox-live` |
| Ghost Story Games | companies | Irrational's successor, making *Judas* | `people/ken-levine`, `companies/irrational-games` |
| Gottlieb / Mylstar | companies | The pinball maker turned video maker whose 1984 closure marks the slump, and the *Reactor* difficulty story | `phenomena/golden-age-arcade`, `games/qbert`, `techniques/difficulty-design` |
| Gradiente | companies | Polyvox Atari, Expert MSX, Phantom System and Playtronic | `culture/brazil-gaming`, `culture/brazilian-market-reserve`, `systems/msx` |
| Gruppo Editoriale Jackson | companies | Milan's dominant computer publisher, credited on PAPERsoft's covers | `magazines/papersoft`, `magazines/mc-microcomputer` |
| GT Interactive | companies | Published *Total Annihilation*, *Unreal* and *Unreal Tournament*, owned Humongous, and later became part of Infogrames | `companies/id-software`, `games/quake`, `companies/infogrames`, `games/total-annihilation`, `companies/cavedog-entertainment`, `games/unreal`, `companies/epic-games`, `tools/unreal-engine` |
| Guildhall Leisure | companies | Doncaster budget publisher of Gloom and Acid reissues | `companies/acid-software`, `people/mark-sibly` |
| GURPS and Steve Jackson Games | companies | Tabletop publisher where several computer game designers began | `games/fallout`, `people/warren-spector`, `companies/origin-systems`, `people/tim-cain` |
| Hasbro and Hasbro Interactive | companies | Owner of Milton Bradley and Parker Brothers; published *RollerCoaster Tycoon*, bought MicroProse and later Atari's catalogue | `companies/milton-bradley`, `companies/atari`, `companies/gce`, `games/roller-coaster-tycoon`, `companies/microprose`, `people/chris-sawyer` |
| Housemarque | companies | Finnish studio formed from the demo-scene studios Bloodhouse and Terramarque | `companies/remedy-entertainment`, `groups/future-crew` |
| Humongous Entertainment | companies | Gilbert's children's-game company (Putt-Putt, Freddi Fish), SCUMM's second licensee and Cavedog's parent | `techniques/scumm`, `people/ron-gilbert`, `companies/cavedog-entertainment`, `games/total-annihilation` |
| Hyperion Entertainment and AmigaOS 4 | companies | The other side of the Cloanto dispute and the post-Commodore OS | `companies/cloanto`, `systems/commodore-amiga` |
| ICOM Simulations and Deja Vu | companies | The MacVenture games (Deja Vu, Uninvited, Shadowgate), the first established point-and-click adventures | `companies/mindscape`, `techniques/point-and-click`, `genres/graphic-adventure` |
| Iguana Entertainment | companies | The Austin studio behind Turok, bought by Acclaim in 1995 | `companies/acclaim`, `companies/probe-software`, `games/mortal-kombat` |
| Image Works | companies | Mirrorsoft's 1988–91 label for the Bitmap Brothers, Tony Crowther and others | `companies/mirrorsoft`, `games/xenon-2`, `games/speedball-2`, `companies/bitmap-brothers`, `people/tony-crowther`, `people/gary-mays` |
| Immersion Corporation | companies | Force-feedback licensor, and the Sony and Microsoft suits | `hardware/dualshock`, `techniques/force-feedback`, `hardware/flight-stick`, `techniques/rumble-pak`, `hardware/steering-wheel` |
| Impulse, Inc. | companies | Maker of Silver, Turbo Silver, Imagine and Firecracker 24 | `tools/imagine`, `tools/sculpt-3d` |
| Indianapolis 500: The Simulation / Papyrus Design Group | companies | The American racing-simulation line, from *Indy 500* to *NASCAR Racing 2003* | `genres/racing-game`, `genres/racing-simulation` |
| Individual Computers / C64 Reloaded | companies | Modern C64 hardware with the VSP fix | `techniques/vsp`, `systems/commodore-64` |
| Infernal Byte Systems | companies | Florian Sauer's company, which made *Nebulus 2* | `games/nebulus` |
| Interceptor Micros | companies | Richard Jones's company, Players' parent, and a pioneer of load-time mini-games | `companies/players-software`, `people/jeff-minter`, `people/oliver-twins` |
| Inti Creates | companies | The studio behind Mega Man 9, 10 and Zero | `games/mega-man`, `companies/capcom` |
| Introversion Software | companies | British indie studio (*Uplink*, *Darwinia*) and an early Steam success | `tools/steam`, `culture/indie-games` |
| inXile Entertainment | companies | Fargo's studio from 2002 (*Wasteland 2* and *3*, *Torment*), bought by Microsoft in 2018 | `companies/interplay`, `people/brian-fargo`, `phenomena/crpg-renaissance`, `companies/obsidian-entertainment`, `games/wasteland`, `companies/microsoft` |
| J.soft (Super Sinc, SuperVIC, Super Commodore) | companies | PAPERsoft's publisher and its Compute!-derived monthlies | `magazines/papersoft`, `culture/magazines-across-borders` |
| Jagex | companies | British studio in Edge's 2013 list | `culture/british-game-development` |
| Jaleco | companies | Published the NES Maniac Mansion | `games/maniac-mansion` |
| Joker Verlag and PC Joker | companies | Michael Labiner's German games-magazine stable | `magazines/amiga-joker`, `magazines/pc-player` |
| Kadokawa | companies | FromSoftware's owner since 2014 | `companies/fromsoft` |
| Kaiko | companies | Hülsbeck's employer in 1994 (*Apidya*, *Gem'X*) | `people/chris-huelsbeck` |
| Kalisto | companies | The Bordeaux studio (Fury of the Furries, Nightmare Creatures) | `companies/mindscape` |
| Kee Games / Joe Keenan | companies | Atari's "rival", set up to get around exclusive distribution | `companies/atari`, `people/nolan-bushnell`, `people/al-alcorn`, `games/breakout` |
| Kele Line | companies | The Danish publisher of *The Vikings* and *Tiger Mission* | `techniques/fld` |
| Kenner | companies | Turned down the Mini Arcade | `companies/gce`, `systems/vectrex` |
| Koei | companies | The MMC5's most regular customer and the publisher of historical strategy games | `hardware/mmc5`, `companies/tecmo`, `companies/team-ninja`, `games/dead-or-alive` |
| Krome Studios | companies | The last owner of the Beam studio | `companies/beam-software`, `companies/melbourne-house` |
| Larian Studios / Divinity: Original Sin | companies | The CRPG revival's biggest success, profiled in *Wireframe* 23 | `phenomena/crpg-renaissance`, `genres/western-rpg`, `games/baldurs-gate` |
| Left Field Productions | companies | Studio linked to Mike Lamb | `people/mike-lamb` |
| Legend Entertainment | companies | Made *Return to Na Pali*, *Unreal II* and *The Wheel of Time* | `games/unreal` |
| Leisure Genius | companies | Virgin label named in the Virgin Games entry | `companies/virgin-games` |
| Live Publishing | companies | *Retro Gamer*'s first publisher | `companies/imagine-publishing`, `magazines/retro-gamer` |
| Logo Computer Systems Inc. (LCSI) | companies | Wrote the Apple, Atari, Sinclair and BBC Logos | `tools/logo-language`, `people/seymour-papert` |
| Logotron | companies | Herbert Wright's next publisher (*XOR*, *Starray*) | `companies/telecomsoft` |
| Loriciels | companies | France's leading 8-bit publisher, which published Chahi's Doggy and Le Pacte and L'Aigle d'Or | `people/eric-chahi`, `people/francois-lionet` |
| Lost Toys | companies | Corpes, Longley and Thomas's Bullfrog spin-off | `companies/bullfrog`, `culture/guildford-games-cluster` |
| MachineGames | companies | Founded in 2009 by Högdahl and other senior Starbreeze staff | `groups/triton`, `people/vogue`, `companies/starbreeze`, `companies/bethesda` |
| Maelstrom Games | companies | Mike Singleton's company behind *Dark Sceptre*, *Midwinter* and *Ashes of Empire* | `people/mike-singleton`, `companies/rainbird` |
| Magnetic Fields | companies | Shaun Southern's studio behind *Lotus* | `companies/gremlin-graphics`, `companies/krisalis` |
| Memory and Storage Technology | companies | Sydney publisher of the first Blitz BASIC | `people/mark-sibly`, `tools/blitz-basic-2` |
| Mettoy | companies | The Corgi toy maker behind the Dragon's launch | `systems/dragon-32`, `companies/dragon-data` |
| Micro Genius and TXC | companies | Taiwanese famiclone maker | `systems/famiclone` |
| Micro Power | companies | Superior's Leeds rival and Hanson's first publisher | `companies/superior-software`, `systems/bbc-micro` |
| Microdigital | companies | Brazil's biggest home-computer maker and leading Sinclair-compatible maker (TK 82-C, TK 85, TK 90X, TK 2000) | `culture/brazilian-market-reserve`, `culture/brazil-gaming`, `systems/zx-spectrum-next`, `people/clive-sinclair`, `magazines/micro-sistemas`, `culture/spectrum-clones` |
| Microdigital (Liverpool) | companies | The 1978 Liverpool computer shop at the root of the Liverpool scene | `culture/liverpool-games-scene`, `companies/imagine-software`, `companies/bug-byte` |
| Microids | companies | Publisher of the 2018 Flashback edition and Flashback 2 | `games/flashback` |
| Micromega | companies | Derek Brewster's and Mervyn Estcourt's publisher | `people/derek-brewster`, `companies/zeppelin-games` |
| Mistwalker | companies | Sakaguchi's studio (*Blue Dragon*, *Lost Odyssey*, *Fantasian*) | `people/hironobu-sakaguchi`, `people/nobuo-uematsu`, `companies/square` |
| Mosaic Publishing | companies | Book-licence publisher of *Erik the Viking* and *Adrian Mole* | `companies/level-9` |
| Mossmouth | companies | Derek Yu's company | `games/spelunky`, `people/derek-yu` |
| Motivetime | companies | Developer of Elite's *Dragon's Lair* and *Virtuoso* | `companies/elite-systems` |
| Mucky Foot Productions | companies | Bullfrog spin-off (*Urban Chaos*, *Startopia*) | `companies/bullfrog`, `culture/guildford-games-cluster` |
| Muse Software | companies | The Baltimore publisher of *Castle Wolfenstein* | `techniques/stealth-mechanics` |
| Mythic Entertainment | companies | *Dark Age of Camelot*, *Warhammer Online* and the 2014 *Dungeon Keeper* | `games/dungeon-keeper`, `companies/electronic-arts` |
| Mythos Games | companies | The Gollops' 1990s studio (UFO, Apocalypse, Magic & Mayhem), after Target Games | `companies/microprose`, `people/julian-gollop`, `games/x-com-ufo-defense`, `games/laser-squad` |
| NCsoft | companies | Publisher of Lineage and Garriott's home after Origin | `people/richard-garriott`, `companies/origin-systems`, `games/ultima` |
| NEC Home Electronics | companies | The PC Engine's maker, also behind the PC-88, PC-98 and PC-FX | `systems/pc-engine`, `companies/hudson-soft` |
| Nightdive Studios | companies | System Shock rights holder: re-releases, the source release, the 2023 remake and period-game restorations | `genres/immersive-sim`, `games/system-shock`, `games/system-shock-2` |
| Ninja Theory | companies | The studio that came out of Argonaut's collapse | `companies/argonaut`, `people/jez-san` |
| Nvidia | companies | The GeForce maker, party to the 3DMark03 dispute | `companies/futuremark` |
| Olivetti | companies | Owned Acorn from 1985 | `companies/acorn-computers` |
| Overkill Software and Payday | companies | The heist series that has kept Starbreeze going since 2013 | `companies/starbreeze` |
| Ozark Softscape | companies | Dan Bunten's four-person Little Rock team | `people/dan-bunten`, `companies/electronic-arts` |
| Paragon Publishing | companies | Bournemouth games-magazine house whose staff and titles became Imagine's | `companies/imagine-publishing`, `magazines/retro-gamer` |
| Park Place Productions | companies | The San Diego studio behind the Mega Drive *Madden*, *EA Hockey* and *ABC Monday Night Football* | `games/madden`, `companies/ea-sports`, `games/nhl-94` |
| PC Data | companies | The US retail sales tracker behind most 1990s American PC sales figures | `games/roller-coaster-tycoon` |
| PC-SIG | companies | The main IBM PC public-domain and shareware library of the 1980s | `distribution/public-domain`, `distribution/shareware` |
| Personal Software (VisiCorp) | companies | Zork I's first publisher | `games/zork`, `companies/infocom` |
| Petroglyph Games | companies | Westwood's successor studio, which made the 2020 remaster | `companies/westwood-studios`, `games/command-and-conquer` |
| Pewex and Baltona | companies | The hard-currency shops where Poles bought Western computers for dollars | `magazines/bajtek`, `culture/the-c64-across-borders` |
| Playtronic | companies | Nintendo's Brazilian licensee from 1993 (Gradiente and Estrela) | `culture/brazil-gaming`, `companies/nintendo`, `companies/tectoy` |
| Postern | companies | Cheltenham publisher of *Snake Pit* and *Shadowfax* | `people/mike-singleton` |
| Presto Studios | companies | Developer of Myst III and The Journeyman Project | `companies/cyan`, `games/myst` |
| Prológica | companies | Maker of the CP-500, CP-200 and CP-400, the best-selling Brazilian TRS-80 compatible | `culture/brazilian-market-reserve`, `culture/brazil-gaming`, `companies/dismac` |
| Prope | companies | Yuji Naka's studio from 2006 | `companies/sonic-team`, `people/yuji-naka` |
| Psion | companies | Maker of *Flight Simulation*, one of the first Sinclair software houses | `genres/simulation-games`, `systems/sinclair-zx81`, `systems/sinclair-zx-spectrum`, `techniques/pixel-art`, `systems/sinclair-ql` |
| Rage Software | companies | The Liverpool developer that absorbed Denton; *Striker* | `culture/liverpool-games-scene`, `companies/ocean-software`, `companies/denton-designs` |
| Raw Thrills | companies | The longest-running US arcade maker of the 2000s | `people/eugene-jarvis`, `companies/midway` |
| RazorSoft | companies | US publisher of the Mega Drive *Stormlord*, known for marketing on controversy | `games/stormlord` |
| Real3D | companies | Lockheed Martin's texture-mapping supplier for Model 2 and Model 3, later a PC graphics maker | `techniques/model-2` |
| Realtime Worlds | companies | Dave Jones's second Dundee studio (*Crackdown*, *APB*), which collapsed in 2010 | `companies/dma-design`, `people/dave-jones`, `culture/dundee-games-scene`, `companies/rockstar-north`, `people/mike-dailly`, `people/ian-hetherington` |
| Red Orb Entertainment | companies | Brøderbund's games label (Riven, the Masterpiece Edition, The Last Express) | `companies/broderbund`, `games/myst` |
| Red Storm Entertainment | companies | The Rainbow Six developer Ubi Soft bought in 2000 | `companies/ubisoft`, `games/splinter-cell` |
| RedOctane | companies | The publisher that conceived *Guitar Hero* and was bought by Activision for $100m | `games/guitar-hero`, `companies/activision`, `companies/harmonix` |
| Redwood Publishing | companies | Acorn User's contract publisher, later part of BBC Enterprises | `magazines/acorn-user` |
| Rhythm King | companies | The record label behind Bomb the Bass and Betty Boo that co-founded Renegade | `companies/renegade`, `companies/bitmap-brothers`, `games/xenon-2`, `games/speedball-2` |
| Rocksteady Studios | companies | British studio in Edge's 2013 list | `culture/british-game-development` |
| Romantic Robot | companies | Maker of the Multiface, Multiprint and Genie, and seller of VideoFace | `hardware/multiface`, `demos/jesus-on-es-spectrum`, `culture/poke-culture`, `distribution/piracy` |
| Ryu Ga Gotoku Studio | companies | Making the next Virtua Fighter, and absorbed AM2 | `games/virtua-fighter`, `companies/sega-am2` |
| Sakhr | companies | Arabic MSX maker | `systems/msx` |
| Sanders Associates | companies | Owner of the videogame patents behind a decade of litigation | `people/ralph-baer`, `hardware/power-pad`, `games/pong` |
| Scavenger | companies | The American publisher behind *Into the Shadows* and its GT Interactive deal | `people/jesper-kyd`, `groups/triton`, `people/vogue`, `companies/starbreeze` |
| SCi Entertainment | companies | Took over Eidos in 2005 | `companies/eidos` |
| Sculptured Software | companies | Made the SNES Mortal Kombat, Super FX Doom and many licensed SNES conversions; bought by Acclaim in 1995 | `games/mortal-kombat`, `companies/acclaim`, `techniques/super-fx-chip`, `companies/probe-software` |
| Sega Technical Institute | companies | Mark Cerny's Californian studio, where *Sonic 2*, *3* and *Sonic & Knuckles* were made | `games/sonic-the-hedgehog`, `people/mark-cerny`, `games/marble-madness`, `people/yuji-naka`, `companies/sonic-team` |
| Shiny Entertainment | companies | David Perry's studio: *Earthworm Jim*, *MDK*, *Messiah*, *Sacrifice*, *Enter the Matrix* | `companies/virgin-games`, `companies/interplay`, `people/david-perry`, `companies/atari`, `companies/infogrames` |
| Silicon Graphics | companies | The workstation maker behind DKC's renders, FF7 and the N64's graphics chip | `systems/nintendo-64`, `companies/nintendo`, `companies/rare`, `games/super-mario-64`, `techniques/pre-rendered-backgrounds`, `games/donkey-kong-country`, `games/final-fantasy-vii` |
| Silicon Knights | companies | Developer of *The Twin Snakes* and *Eternal Darkness* | `games/metal-gear-solid` |
| Simis | companies | One of Eidos's 1995 purchases | `companies/eidos`, `companies/domark` |
| Sir-Tech | companies | *Wizardry*'s publisher, which used code wheels and manual look-ups | `techniques/code-wheels`, `techniques/manual-protection`, `genres/western-rpg`, `games/wizardry`, `genres/jrpg` |
| Smoking Car Productions | companies | Mechner's studio | `people/jordan-mechner` |
| Snapshot Games | companies | Gollop's studio since 2013 | `people/julian-gollop`, `games/x-com-ufo-defense`, `games/xcom-enemy-unknown` |
| Soft Pro | companies | Karateka's Famicom converter | `games/karateka` |
| Softgold | companies | The German group behind Rainbow Arts and its labels | `companies/rainbow-arts` |
| SoftKey | companies | Took over The Learning Company and MECC in 1995 and took the Learning Company name | `companies/the-learning-company`, `companies/mecc`, `companies/broderbund`, `companies/mindscape` |
| Software 2000 | companies | German publisher of *Pizza Tycoon* and *Bundesliga Manager* | `genres/tycoon-games`, `genres/management-game` |
| Software Preservation Society and IPF | companies | The preservation format built for protected disks | `techniques/disk-protection`, `techniques/copylock`, `hardware/kryoflux`, `culture/game-preservation` |
| Spectrum HoloByte | companies | *Tetris*'s American publisher and *Falcon*'s, Mirrorsoft's US sister, later owner of MicroProse | `games/tetris`, `companies/mirrorsoft`, `companies/microprose`, `phenomena/tetris-legal-battles`, `people/alexey-pajitnov`, `games/chaos-engine`, `techniques/puzzle-game-design` |
| Square Enix | companies | The merged company from 2003, Taito's owner since 2005 | `companies/taito`, `companies/square`, `companies/enix`, `companies/eidos`, `games/deus-ex`, `games/thief` |
| Starpath | companies | The 2600 maker Epyx took over in 1983, bringing in the *Summer Games* team | `games/summer-games`, `games/impossible-mission`, `companies/epyx`, `systems/atari-2600` |
| Strategic Studies Group | companies | Roger Keating and Ian Trout's Australian wargame house (Reach for the Stars, Carriers at War, Warlords) | `genres/wargame`, `genres/4x-strategy` |
| subLOGIC and Bruce Artwick | companies | The makers of Flight Simulator | `genres/simulation-games`, `genres/flight-sim`, `games/microsoft-flight-simulator` |
| Sumo Digital | companies | Sheffield studio that produced *Broken Sword: The Angel of Death* | `culture/british-game-development`, `companies/gremlin-graphics`, `companies/revolution-software`, `people/charles-cecil`, `games/broken-sword` |
| Supermassive Games | companies | Guildford-cluster studio | `culture/guildford-games-cluster` |
| Superscape | companies | The VR and business 3D system and company that grew from Incentive | `companies/incentive-software`, `people/ian-andrew`, `techniques/freescape` |
| Supersoft | companies | Early British PET software house (the *Mikro* assembler) that rescued Audiogenic | `companies/audiogenic` |
| Synapse Software | companies | Converted *Zaxxon*; its *Blue Max* was a Zaxxon-style game | `games/zaxxon` |
| Takara | companies | Published SNK's SNES and Genesis conversions, including *Fatal Fury* | `games/fatal-fury`, `companies/snk` |
| Take-Two Interactive | companies | Owner of Rockstar and 2K; bought BMG Interactive and DMA, owned 19.9 per cent of Bungie and kept *Myth* and *Oni* | `games/civilization`, `companies/dma-design`, `companies/rockstar-north`, `games/grand-theft-auto`, `companies/rockstar`, `games/gta-iii`, `companies/bungie`, `games/halo`, `companies/remedy-entertainment`, `companies/irrational-games`, `games/bioshock` |
| Tango Gameworks | companies | Mikami's studio, 2010–2023, closed and then bought by Krafton | `people/shinji-mikami`, `companies/bethesda` |
| Taskset | companies | Andy Walker's C64 publisher | `techniques/enemy-design`, `games/space-invaders` |
| TecMagik | companies | Console converter of *Populous* | `games/populous` |
| Teque Software | companies | The conversion house for *Chase H.Q.* and *Continental Circus* | `techniques/pseudo-3d-road`, `games/chase-hq`, `companies/krisalis` |
| Terrible Toybox | companies | Gilbert and Winnick's studio, which made Thimbleweed Park and Return to Monkey Island | `games/monkey-island`, `people/ron-gilbert`, `techniques/scumm` |
| The 3DO Company | companies | The console company named in the Warshaw entry | `people/howard-scott-warshaw` |
| The Pokémon Company | companies | The jointly owned rights holder | `companies/game-freak`, `companies/creatures-inc`, `companies/nintendo`, `games/pokemon` |
| The Software Toolworks | companies | Maker of Chessmaster and Mavis Beacon, and Mindscape's parent from 1990 | `companies/mindscape`, `companies/the-learning-company` |
| The Tetris Company | companies | Rogers's company, which has held and licensed the *Tetris* rights since the mid-1990s | `games/tetris`, `people/henk-rogers`, `phenomena/tetris-legal-battles`, `people/alexey-pajitnov`, `people/roger-dean` |
| THQ | companies | Founded by LJN's Jack Friedman in 1990, a major licensee into the 2010s | `companies/ljn`, `companies/acclaim` |
| Time Warner Interactive | companies | Atari Games' owner from 1994 to 1996 | `companies/atari-games`, `companies/midway` |
| Titus Interactive | companies | The French owner of both Interplay and Virgin | `companies/interplay`, `companies/virgin-games`, `companies/black-isle-studios` |
| Topo Soft | companies | The Spanish developer of Mad Mix and Kixx's first original games | `companies/kixx`, `companies/us-gold` |
| Trace | companies | The disk duplicators that made most protected Amiga and ST disks | `techniques/copylock`, `techniques/disk-protection` |
| Tradewest | companies | Texas publisher of the NES *Double Dragon* games and *Battletoads* | `games/double-dragon`, `companies/technos`, `games/battletoads`, `companies/rare` |
| Traveller's Tales | companies | Developer David Whittaker worked with | `people/david-whittaker` |
| Trilobyte | companies | The studio behind *The 7th Guest*, with a studio history in *Wireframe* 44 | `techniques/fmv`, `games/7th-guest`, `people/graeme-devine` |
| TSR and Dungeons & Dragons | companies | The rules and licence behind the Gold Box games, Baldur's Gate and Planescape, and a tabletop start for several designers | `genres/western-rpg`, `genres/jrpg`, `companies/epyx`, `genres/roguelike`, `games/ultima`, `games/baldurs-gate`, `people/warren-spector`, `games/planescape-torment`, `games/neverwinter-nights`, `companies/black-isle-studios`, `companies/origin-systems` |
| Two Point Studios | companies | Mark Webley and Gary Carr's studio | `companies/bullfrog`, `companies/lionhead`, `games/theme-park`, `culture/guildford-games-cluster` |
| Tynesoft | companies | The Newcastle publisher where Zeppelin's founders met | `people/derek-brewster`, `companies/zeppelin-games` |
| Universal Interactive Studios | companies | Publisher of Crash Bandicoot and Spyro | `people/mark-cerny`, `companies/naughty-dog`, `games/crash-bandicoot`, `games/spyro`, `companies/insomniac` |
| Valiant Comics | companies | The source of Turok and Shadow Man | `companies/acclaim` |
| Vektor Grafix | companies | The Leeds 3D specialist that converted Star Wars for Domark | `companies/domark`, `techniques/vector-graphics`, `games/starglider` |
| Vid Kidz | companies | Jarvis and DeMar's studio behind *Stargate* and *Robotron* | `games/defender`, `games/robotron-2084`, `people/eugene-jarvis`, `companies/williams-electronics` |
| Videa and Sente Technologies | companies | The company former Atari coin-op engineers founded, bought by Bushnell in 1983 | `people/dona-bailey`, `people/nolan-bushnell` |
| Video Game History Foundation | companies | The main US game-history non-profit, author of the 2023 availability study | `culture/game-preservation`, `communities/internet-archive` |
| Vision Software | companies | Auckland studio that shared Acid's office | `companies/acid-software`, `games/skidmarks` |
| Vivid Image | companies | Dinc, Twiddy and Riley's company (*Hammerfist*, *First Samurai*) | `people/john-twiddy`, `people/raffaele-cecco` |
| Walnut Creek CDROM and Schatztruhe | companies | Publishers of the Aminet CDs | `communities/aminet` |
| Warner Bros. Games | companies | Owner of *Mortal Kombat* since 2009 | `companies/netherrealm-studios`, `companies/midway`, `games/mortal-kombat` |
| Warner Interactive Entertainment | companies | Renegade's buyer | `companies/renegade`, `companies/graftgold`, `companies/bitmap-brothers` |
| Westone | companies | The Wonder Boy developer that licensed its game to Hudson | `games/wonder-boy`, `games/adventure-island`, `companies/hudson-soft` |
| Wireplay | companies | BT's late-1990s online games service, organiser of Insomnia '99 | `communities/lan-parties`, `culture/online-multiplayer` |
| Yamaha | companies | Maker of the YM2612, YM2151, YM2413 and OPL chips | `hardware/ym2612`, `techniques/fm-synthesis`, `systems/sega-mega-drive`, `systems/msx` |
| YoYo Games | companies | Mike Dailly's later company, home of GameMaker | `people/mike-dailly`, `tools/game-maker`, `culture/dundee-games-scene` |
| Ys Net | companies | Suzuki's studio since 2008 | `people/yu-suzuki`, `games/shenmue` |
| ZeniMax Media | companies | Parent of Bethesda and id, and the subject of the Weaver and Fallout Online cases | `events/quakecon`, `companies/id-software`, `companies/bethesda`, `companies/microsoft`, `companies/interplay` |
| Ziff Davis | companies | *CGW*'s owner from 1993 and publisher of *PC Magazine* and 1UP | `magazines/computer-gaming-world`, `magazines/compute-magazine` |
| Zyrinx | companies | Danish scene-to-console developer (*Sub-Terrania*), forerunner of IO Interactive | `groups/crionics`, `groups/the-silents`, `demos/hardwired`, `people/jesper-kyd`, `companies/io-interactive` |

## Magazines

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Personal Computer News | magazines | Dated Manic Miner's release (August 1983 review) | `games/manic-miner`, `people/matthew-smith`, `systems/sinclair-zx81`, `games/jetpac`, `games/football-manager-1982`, `companies/dragon-data` |
| Big K | magazines | IPC's 1984–85 games monthly; the source of Bug-Byte's company history | `companies/bug-byte`, `companies/imagine-software`, `games/football-manager-1982`, `distribution/cover-tapes`, `culture/reading-the-charts`, `genres/rts-genre`, `genres/simulation-games`, `culture/liverpool-games-scene`, `companies/gce`, `companies/milton-bradley` |
| Your Computer | magazines | Carried Bug-Byte's first adverts and much ZX80 coverage | `companies/bug-byte`, `systems/sinclair-zx80`, `systems/commodore-64`, `companies/ocean-software`, `phenomena/bedroom-coder`, `games/jetpac`, `games/football-manager-1982`, `distribution/type-in-listings`, `systems/dragon-32`, `systems/dragon-64`, `culture/liverpool-games-scene`, `companies/imagine-software`, `techniques/interrupt-driven-music`, `culture/basic-to-machine-code`, `distribution/piracy` |
| BYTE | magazines | Reviewed the ZX80 in January 1981 | `systems/sinclair-zx80`, `hardware/z80`, `systems/commodore-amiga`, `hardware/mc6847`, `hardware/6809`, `systems/trs-80`, `systems/apple-ii`, `hardware/6502`, `genres/rts-genre`, `genres/simulation-games`, `distribution/piracy` |
| TV Gamer | magazines | 1984 source of the most detailed *Atic Atac* guide | `games/atic-atac`, `games/pitfall` |
| Zero | magazines | Dennis's games magazine; Teresa Maughan was its publisher | `people/teresa-maughan` |
| Ahoy! and INFO | magazines | US Commodore magazines cited for C64 sales and fast loaders | `systems/commodore-64`, `techniques/disk-fastloaders`, `techniques/disk-protection`, `techniques/copy-protection`, `culture/the-juggler`, `genres/simulation-games`, `culture/basic-to-machine-code` |
| AmigaWorld | magazines | The main US Amiga magazine, whose readers became *Amiga Computing*'s US edition | `systems/commodore-amiga`, `magazines/amiga-computing`, `culture/magazines-across-borders`, `companies/idg`, `tools/lightwave-3d`, `tools/imagine`, `tools/sculpt-3d`, `people/eric-graham`, `tools/blitz-basic-2`, `culture/the-juggler` |
| Amazing Computing | magazines | Long-running US Amiga magazine | `systems/commodore-amiga`, `techniques/compression`, `tools/lightwave-3d`, `tools/imagine`, `tools/sculpt-3d`, `people/eric-graham`, `tools/blitz-basic-2`, `culture/the-juggler`, `culture/basic-to-machine-code` |
| Next Magazine | magazines | SpecNext's own magazine | `systems/zx-spectrum-next`, `people/tim-gilberts`, `people/graeme-yeandle`, `tools/arcade-game-designer` |
| Commodore Disk User | magazines | Cited on border sprites and fast loaders | `hardware/vic-ii`, `techniques/disk-fastloaders`, `hardware/action-replay`, `techniques/fast-loader`, `culture/disk-magazines`, `magazines/your-commodore`, `distribution/magazine-cover-disks`, `distribution/type-in-listings` |
| The Transactor | magazines | Canadian Commodore magazine cited on the CIA's clock | `hardware/cia` |
| Electron User | magazines | Database's Acorn Electron title, begun inside *The Micro User* | `magazines/micro-user`, `companies/europress`, `games/repton`, `companies/superior-software` |
| Atari User | magazines | Database's 8-bit Atari monthly and *Atari ST User*'s first home | `magazines/atari-st-user`, `companies/europress`, `systems/atari-8-bit` |
| ST Action | magazines | Europress's ST games magazine, *Amiga Action*'s older sister | `magazines/amiga-action`, `companies/europress`, `magazines/atari-st-user`, `magazines/the-one` |
| ST Review | magazines | One of the last two glossy ST magazines | `magazines/atari-st-user`, `magazines/st-format`, `magazines/ace-magazine`, `companies/emap` |
| Computing with the Amstrad | magazines | Database's CPC title, which absorbed *Amtix!* | `magazines/amtix`, `companies/europress`, `magazines/amstrad-action`, `systems/amstrad-cpc` |
| Commodore Force | magazines | *ZZAP!64*'s Europress successor, where Lloyd Mangram reappeared | `magazines/zzap-64`, `companies/europress`, `companies/newsfield`, `people/lloyd-mangram`, `distribution/cover-tapes`, `magazines/commodore-format` |
| LM | magazines | Newsfield's 1986–87 general-interest magazine, named after Lloyd Mangram | `people/lloyd-mangram`, `companies/newsfield` |
| Mean Machines Sega | magazines | The Sega half of the 1992 *Mean Machines* split | `magazines/mean-machines`, `magazines/nintendo-magazine-system` |
| ST/Amiga Format | magazines | The 1988–89 parent of both Formats | `magazines/st-format`, `magazines/amiga-format`, `companies/future-publishing`, `distribution/magazine-cover-disks` |
| PC Gamer | magazines | Future's PC games magazine in Britain and America | `companies/future-publishing`, `magazines/pc-player`, `games/civilization`, `emulators/emulation`, `games/dune-ii`, `games/warcraft`, `games/deus-ex`, `games/x-com-ufo-defense`, `games/syndicate`, `games/diablo` |
| New Computer Express and Sega Power | magazines | Future's weekly news title and its Sega magazine | `companies/future-publishing` |
| Next Generation | magazines | Chris Anderson's American games magazine | `people/chris-anderson`, `companies/future-publishing`, `magazines/edge` |
| Electronic Fun with Computers & Games, JoyStik, Video Games and Sega Visions | magazines | US period magazines cited on the 2600, Vectrex and Mega Drive | `games/pac-man-atari-2600`, `systems/vectrex`, `systems/sega-mega-drive`, `techniques/sprite-flicker`, `companies/midway`, `people/eugene-jarvis`, `games/pac-man`, `games/defender`, `games/mario-bros` |
| Commodore Computing International | magazines | British Commodore monthly cited on the Action Replay and fast loaders | `hardware/action-replay`, `techniques/fast-loader`, `techniques/disk-fastloaders` |
| 2000 AD | magazines | The British comic Rebellion has owned since 2000, source of *Judge Dredd* and *Rogue Trooper* games since the 1980s | `companies/rebellion`, `games/judge-dredd` |
| 64'er | magazines | Markt & Technik's C64 magazine, which ran the competition Hülsbeck won | `people/chris-huelsbeck` |
| 80 Micro and SoftSide | magazines | The main TRS-80 periodicals | `systems/trs-80` |
| A&B Computing | magazines | Acorn magazine cited in the Repton entry | `games/repton` |
| Amiga Advis | magazines | Danish Amiga magazine with detailed late-1990s party reports and results | `groups/the-black-lotus`, `groups/scoopex`, `events/the-party`, `events/the-gathering` |
| ANALOG Computing | magazines | US magazine cited for 1983–89 coverage | `games/mario-bros` |
| Antic and COMPUTE!'s Atari ST | magazines | US Atari magazines cited by the GFA BASIC entry | `tools/gfa-basic`, `culture/basic-to-machine-code`, `techniques/pixel-art`, `companies/lucasarts`, `games/mario-bros` |
| Atari Age | magazines | The US Atari Club magazine, 1982–84 | `magazines/atari-club-magazin`, `companies/atari`, `culture/magazines-across-borders`, `games/mario-bros` |
| Big Blue Disk | magazines | Softdisk's PC disk magazine | `companies/softdisk`, `culture/disk-magazines` |
| Brazilian games magazines (VideoGame, SuperGame, GamePower, SuperGamePower) | magazines | The main period evidence for Brazil's console market | `culture/brazil-gaming`, `culture/online-multiplayer`, `systems/famiclone` |
| Commodore Power Play | magazines | Source for many Commodore interviews | `people/david-simons` |
| Computer Gamer | magazines | British games magazine of the mid-1980s, cited in the Repton and Wargame entries | `games/repton`, `genres/wargame` |
| Dragon User | magazines | The Dragon's own magazine, 1983–1989 | `systems/dragon-32`, `systems/dragon-64`, `companies/dragon-data` |
| Elbug | magazines | The BBC Micro user magazine, cited in the BASIC-to-machine-code entry | `culture/basic-to-machine-code`, `books/usborne-computing-books` |
| Electronic Gaming Monthly | magazines | The major US games magazine from 1989 | `games/mega-man` |
| Eurochart | magazines | The Crusaders' scene chart, which ranked the groups | `groups/the-silents`, `demos/hardwired`, `magazines/scene-diskmags`, `groups/quartex`, `communities/cracking-scene`, `magazines/illegal` |
| Family Computing | magazines | American home-computing magazine of the 1980s, cited in the BASIC-to-machine-code entry | `culture/basic-to-machine-code` |
| Galaksija (magazine) | magazines | The Belgrade popular-science magazine behind the Galaksija project | `systems/galaksija`, `magazines/racunari` |
| Game Developer (magazine) | magazines | The trade magazine connected to GDC's owners | `culture/gdc` |
| GamesMaster (magazine) | magazines | The British magazine and TV spin-off that ran Boon's Kombat Kolumn | `people/ed-boon`, `games/mortal-kombat` |
| gamesTM | magazines | Imagine's multiformat games magazine, whose retro section preceded *Retro Gamer* | `companies/imagine-publishing`, `magazines/retro-gamer` |
| GO64! and Lotek64 | magazines | German and Austrian C64 magazines of the 1999–2000s | `events/x-party`, `demos/deus-ex-machina`, `groups/booze-design` |
| Hugi | magazines | The longest-running PC diskmag, 1996–2014 | `magazines/scene-diskmags`, `groups/fairlight` |
| L'Atarien | magazines | The French Atari Club magazine, 1983–86 | `magazines/atari-club-magazin`, `culture/magazines-across-borders` |
| Loadstar | magazines | Softdisk's longest-lived commercial disk magazine, 1984–99 | `culture/disk-magazines`, `companies/softdisk`, `systems/commodore-64` |
| MICRO | magazines | The US 6502 journal | `techniques/interrupt-driven-music` |
| Micro & Personal Computer | magazines | Gruppo Editoriale Suono's 1979 predecessor of MC | `magazines/mc-microcomputer` |
| Micro Adventurer | magazines | The British magazine devoted to adventures, 1983–85 | `tools/the-quill`, `companies/gilsoft`, `genres/text-adventure` |
| MikroBitti | magazines | Finnish computer magazine, and its *Illuminatus* April fool | `people/psi`, `people/skaven` |
| Nintendo Fun Club | magazines | Nintendo Power's free predecessor | `magazines/nintendo-power`, `culture/hint-lines` |
| PC Zone | magazines | British PC magazine of the 1990s, cited in several PC game entries | `games/civilization`, `emulators/emulation`, `genres/simulation-games`, `games/red-alert`, `games/command-and-conquer`, `games/dune-ii`, `games/warcraft`, `games/deus-ex`, `games/x-com-ufo-defense`, `games/syndicate`, `games/diablo` |
| Play Meter | magazines | The American arcade trade magazine whose earnings polls the period press reprinted | `games/pole-position`, `games/xevious`, `phenomena/golden-age-arcade` |
| Popular Computing Weekly | magazines | A British weekly that ran listings, cited in several entries | `people/richard-cockayne`, `people/darling-brothers`, `companies/renegade`, `companies/codemasters` |
| Professional Amiga User | magazines | Amiga magazine cited with no Vault entry | `techniques/compression`, `groups/red-sector-inc` |
| R.A.W. | magazines | Spaceballs' disk magazine, source of the making-of *State of the Art* and the arguments over it | `groups/spaceballs`, `demos/state-of-the-art`, `magazines/scene-diskmags`, `demos/enigma` |
| Recollection | magazines | C64 scene history magazine, the main public source for many C64 group entries | `groups/eagle-soft-incorporated`, `groups/1001-crew` |
| RUN | magazines | US Commodore magazine whose Magic column carried type-ins such as Sprite Stretch 64 | `techniques/sprite-stretching` |
| RUN (Scandinavian edition) | magazines | The Danish/Norwegian Commodore magazine, with period sales data | `culture/the-c64-across-borders` |
| Sega Saturn Magazine | magazines | Sega's official British Saturn magazine, cited in the Red Alert and Command & Conquer entries | `systems/sega-saturn`, `games/red-alert`, `games/command-and-conquer` |
| Sex'n'Crime | magazines | Genesis Project's diskmag, described as the first real C64 scene diskmag | `groups/genesis-project`, `magazines/scene-diskmags` |
| SoftSide | magazines | US type-in magazine and the source of PAPERsoft's first listing | `magazines/papersoft`, `magazines/compute-magazine` |
| Super Commodore 64/128 | magazines | Gruppo Editoriale Jackson's Italian C64 magazine, a source of Commodore sales figures | `culture/the-c64-across-borders` |
| Super Play | magazines | Future's British Super NES magazine, much cited in SNES entries | `games/super-metroid`, `companies/nintendo-rd1`, `games/mortal-kombat`, `techniques/super-fx-chip`, `techniques/mode-7`, `systems/super-nintendo`, `techniques/turn-based-combat`, `companies/fromsoft`, `games/dark-souls`, `genres/action-rpg`, `games/secret-of-mana`, `companies/square` |
| Svet kompjutera | magazines | The other major Yugoslav computer magazine, from 1984, which reported the 1984 import decision | `systems/galaksija`, `magazines/racunari`, `people/voja-antonic`, `culture/the-c64-across-borders`, `culture/institutional-computer-press` |
| Tau Press and Qercus | magazines | Acorn User's last publisher and its successor title | `magazines/acorn-user` |
| The Rainbow | magazines | The main CoCo magazine, 1981–93 | `systems/tandy-coco` |
| Top Secret | magazines | Polish games magazine named in the *Lyra II* scrollers | `groups/esi`, `demos/lyra-ii`, `magazines/bajtek`, `culture/the-c64-across-borders` |
| Total! | magazines | Future's Nintendo magazine | `magazines/edge`, `companies/future-publishing` |
| Videogaming Illustrated | magazines | US magazine cited for 1983 coverage | `games/mario-bros` |
| Wireframe | magazines | Now cited across many entries | `culture/basic-to-machine-code`, `games/rainbow-islands`, `games/mega-man`, `games/bubble-bobble`, `companies/fromsoft`, `games/dark-souls`, `genres/action-rpg`, `games/secret-of-mana`, `companies/square` |
| Your 64 | magazines | Sportscene's C64 monthly, 1984–85, merged into Your Commodore | `magazines/your-commodore`, `systems/commodore-16`, `systems/commodore-64` |
| ZX Spectrum Gamer | magazines | Modern Spectrum magazine cited across several entries | `tools/arcade-game-designer`, `people/tim-gilberts` |

## Games

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Miner 2049er | games | The game the Manic Miner entry names as its model (as *Miner 49'er*) | `games/manic-miner`, `genres/platformer`, `genres/single-screen-platformer` |
| Styx | games | Matthew Smith's first Bug-Byte release | `people/matthew-smith`, `games/manic-miner` |
| Alien 8 | games | Ultimate's second Filmation game, after Knight Lore | `companies/ultimate`, `games/knight-lore`, `techniques/filmation-engine`, `techniques/isometric-projection` |
| Nightshade | games | Ultimate's scrolling Filmation II game | `companies/ultimate`, `games/knight-lore`, `techniques/filmation-engine`, `techniques/isometric-projection` |
| Underwurlde | games | The second Sabreman game | `companies/ultimate`, `games/sabre-wulf` |
| Lunar Jetman | games | Jetpac's sequel | `companies/ultimate`, `games/jetpac`, `people/stamper-brothers`, `people/gary-mays` |
| Pentagram | games | The last Sabreman game (1986) | `games/sabre-wulf`, `games/knight-lore`, `companies/ultimate` |
| Gunfright | games | The last game the Stampers developed as a team | `companies/ultimate`, `people/stamper-brothers`, `games/knight-lore`, `techniques/filmation-engine` |
| Wizards & Warriors | games | One of Rare's first NES games | `companies/rare`, `companies/acclaim` |
| Jet Set Willy II | games | The 1985 expanded version, with different credits and content | `games/jet-set-willy`, `companies/software-projects`, `people/matthew-smith` |
| Bandersnatch and Psyclapse | games | Imagine's unreleased megagames, whose path runs to *Brataccas* | `companies/imagine-software`, `companies/psygnosis`, `people/ian-hetherington` |
| Twin Kingdom Valley | games | Bug-Byte's cross-platform adventure hit | `companies/bug-byte` |
| Arcadia | games | Imagine's first hit | `companies/imagine-software`, `people/david-lawson`, `events/golden-joystick-awards`, `games/jetpac` |
| Dragon's Lair (Spectrum) | games | Software Projects' licence of the laserdisc game | `companies/software-projects`, `companies/elite-systems` |
| Avalon, Frankie Goes to Hollywood, Vectron, Dark Sceptre, Zombie Zombie | games | The period examples in attribute-aware design; *Avalon* is also Steve Turner's best-known Hewson game | `techniques/attribute-aware-design`, `companies/graftgold`, `people/steve-turner`, `companies/hewson-consultants`, `games/ant-attack`, `people/sandy-white`, `people/mike-singleton`, `companies/beyond-software`, `companies/denton-designs`, `companies/ocean-software` |
| Gyromite | games | R.O.B.'s pack-in game | `systems/nintendo-entertainment-system`, `hardware/rob`, `games/duck-hunt` |
| Championship Lode Runner | games | The 1984 sequel | `games/lode-runner` |
| Space Panic | games | Arcade climbing game named in the Lode Runner entry | `games/lode-runner`, `genres/platformer`, `genres/single-screen-platformer`, `games/donkey-kong` |
| Menace | games | Dave Jones's Amiga shooter; the blitter entry uses his account of it | `hardware/blitter`, `hardware/denise`, `companies/dma-design`, `companies/psygnosis`, `people/dave-jones` |
| F/A-18 Interceptor | games | Amiga flight game discussed in the blitter entry | `hardware/blitter` |
| Mighty Final Fight | games | NES example of sprite flicker | `hardware/ppu` |
| Morpheus | games | Andrew Braybrook's 1987 C64 game, with a *ZZAP!64* diary and a dispute over who would publish it | `hardware/vic-ii`, `people/andrew-braybrook`, `companies/graftgold`, `companies/hewson-consultants`, `companies/rainbird` |
| Sinistar and Stargate | games | Williams arcade games named in the 6809 entry | `hardware/6809`, `games/defender`, `people/eugene-jarvis`, `companies/williams-electronics`, `games/robotron-2084`, `games/joust` |
| Guardian (Amiga) | games | Mark Sibly's game with a copper sky | `hardware/copper`, `people/mark-sibly`, `companies/acid-software` |
| Blood Money, Agony, Wonder Dog, Pioneer Plague | games | Amiga games the Denise and Agnus entries use as examples | `hardware/denise`, `hardware/agnus`, `companies/dma-design`, `companies/psygnosis`, `people/dave-jones`, `people/roger-dean` |
| Highway Encounter | games | Vortex's highest-rated game | `companies/vortex-software`, `people/costa-panayi`, `techniques/isometric-projection` |
| Deflektor | games | The first Vortex game Gremlin published | `companies/vortex-software`, `companies/gremlin-graphics`, `people/costa-panayi` |
| Computer Space | games | Bushnell's first arcade game, made before Atari existed | `companies/atari`, `people/nolan-bushnell`, `hardware/arcade-hardware`, `games/pong`, `genres/arcade-game` |
| Raiders of the Lost Ark (Atari 2600) | games | Warshaw's game before *E.T.* | `games/et-the-extra-terrestrial`, `people/howard-scott-warshaw`, `culture/licensed-games` |
| Yars' Revenge | games | Warshaw's first game, named after Kassar backwards | `people/howard-scott-warshaw`, `games/et-the-extra-terrestrial`, `people/ray-kassar`, `systems/atari-2600` |
| Ms. Pac-Man | games | The best-selling American sequel, begun as General Computer's *Crazy Otto*; its 8K 2600 version fixed the first cartridge's problems | `games/pac-man-atari-2600`, `techniques/sprite-flicker`, `games/pac-man`, `companies/namco`, `companies/midway` |
| Robot Tank and Decathlon | games | Activision's self-switching 2600 cartridges | `techniques/bank-switching`, `companies/activision`, `systems/atari-2600` |
| Mine Storm | games | The Vectrex's built-in game | `systems/vectrex`, `companies/gce` |
| Radar Scope | games | The failed arcade game that became *Donkey Kong* | `games/donkey-kong`, `people/shigeru-miyamoto`, `people/minoru-arakawa` |
| Donkey Kong Jr. | games | The sequel with the roles swapped | `games/donkey-kong`, `games/super-mario-bros`, `systems/nintendo-game-and-watch` |
| Zelda II: The Adventure of Link | games | *Zelda*'s direct sequel | `games/legend-of-zelda` |
| Famicom Detective Club | games | Sakamoto's adventures, which set his directing style | `people/yoshio-sakamoto` |
| Metroid Fusion and Metroid: Zero Mission | games | The Game Boy Advance *Metroid* games | `people/yoshio-sakamoto`, `games/metroid`, `games/super-metroid`, `genres/metroidvania` |
| WarioWare | games | Nintendo's microgame series, produced by Sakamoto | `people/yoshio-sakamoto`, `games/wario-land`, `companies/intelligent-systems`, `companies/nintendo-rd1` |
| Super Mario World | games | The SNES launch game | `systems/super-nintendo`, `games/donkey-kong-country`, `games/super-mario-64`, `genres/platformer`, `games/super-mario-bros`, `phenomena/sega-vs-nintendo` |
| Pilotwings | games | The first cartridge with an extra chip, and a Mode 7 showcase | `systems/super-nintendo`, `techniques/mode-7`, `techniques/sprite-scaling` |
| The Great Giana Sisters | games | Rainbow Arts' game, withdrawn under pressure from Nintendo | `games/super-mario-bros`, `companies/nintendo`, `companies/rainbow-arts`, `people/chris-huelsbeck` |
| Beach-Head | games | U.S. Gold's first licence | `companies/us-gold`, `companies/centresoft` |
| World Cup Carnival | games | The period press's standard example of a cynical licence | `companies/us-gold`, `magazines/ace-magazine` |
| Thunder Blade | games | Sega's coin-op and a well-documented Spectrum conversion | `companies/tiertex`, `companies/us-gold`, `culture/arcade-conversion` |
| 720° | games | Atari's skateboarding coin-op, Tiertex's first job | `companies/tiertex`, `companies/us-gold` |
| Human Killing Machine | games | Tiertex's notorious *Street Fighter* follow-up | `companies/tiertex`, `games/street-fighter`, `culture/bad-ports`, `companies/us-gold` |
| Kick Off | games | Anco's football game, *Amiga Format*'s first Format Gold | `magazines/amiga-format`, `companies/anco`, `games/sensible-soccer`, `people/dino-dini`, `people/steve-screech`, `genres/sports-games`, `games/fifa` |
| Bombuzal | games | *Amiga Power*'s first cover-disk game | `magazines/amiga-power` |
| Jetstrike | games | A commercial Amiga game written in AMOS | `tools/amos` |
| Scorched Tanks | games | The best-known AMOS shareware game | `tools/amos`, `people/francois-lionet` |
| Kong Strikes Back | games | Galway's claimed first fast-arpeggio chords | `techniques/arpeggio`, `people/martin-galway` |
| Gridrunner | games | Minter's first hit | `people/jeff-minter`, `companies/llamasoft`, `systems/commodore-vic-20`, `genres/shoot-em-up` |
| Iridis Alpha | games | Minter's C64 shoot-'em-up | `people/jeff-minter`, `companies/llamasoft`, `systems/commodore-64` |
| Llamatron | games | A full-price game Llamasoft released as shareware | `companies/llamasoft`, `distribution/shareware`, `games/robotron-2084`, `people/jeff-minter` |
| Quazatron and Technician Ted | games | Hewson's two highest-scoring Spectrum games | `companies/hewson-consultants`, `people/steve-turner`, `games/paradroid`, `companies/graftgold`, `people/andrew-hewson` |
| Daley Thompson's Decathlon | games | The licence that made Ocean's name, with its joystick-waggling controls | `companies/ocean-software`, `people/christian-urquhart`, `phenomena/bedroom-coder`, `people/martin-galway`, `genres/sports-games` |
| Hunchback | games | Ocean's first licence, programmed by Christian Urquhart | `companies/ocean-software`, `people/christian-urquhart`, `culture/licensed-games` |
| RoboCop (Ocean) | games | Ocean's 1988 film licence, which Data East took into the arcades | `companies/ocean-software`, `companies/data-east`, `people/jonathan-dunn`, `culture/arcade-conversion`, `culture/licensed-games`, `people/mike-lamb` |
| Ghostbusters | games | Crane's best-selling 1984 licence, with a well-documented development story | `people/david-crane`, `companies/activision`, `games/knight-lore`, `games/sabre-wulf` |
| Little Computer People | games | Crane's early life simulation | `people/david-crane`, `companies/activision` |
| A Boy and His Blob | games | Crane's NES game | `people/david-crane` |
| M.U.L.E., Pinball Construction Set and Archon | games | EA's first-wave games | `companies/electronic-arts`, `people/dan-bunten`, `companies/ariolasoft`, `people/trip-hawkins`, `communities/modding`, `magazines/computer-gaming-world` |
| Gribbly's Day Out | games | Braybrook's first original game | `people/andrew-braybrook`, `companies/hewson-consultants`, `games/paradroid` |
| Chiller | games | The Darling brothers' early best-seller and the *Thriller* dispute | `companies/mastertronic`, `people/darling-brothers` |
| Booty | games | Firebird's first hit | `companies/firebird` |
| The Sentinel | games | Geoff Crammond's game and Firebird's highest *CRASH* score | `companies/firebird`, `people/tim-follin`, `people/geoff-crammond`, `techniques/procedural-generation`, `people/ian-andrew`, `games/driller` |
| Forgotten Worlds | games | The first CP System game, converted under U.S. Gold's GO! label | `companies/capcom`, `games/ghouls-n-ghosts` |
| Gradius II | games | *Gradius*'s arcade sequel, *Vulcan Venture* in the West | `games/gradius`, `games/salamander` |
| Devil May Cry | games | Capcom's 2001 action game, begun as a *Resident Evil* offshoot | `companies/capcom`, `people/shinji-mikami`, `genres/survival-horror` |
| Frontier: Elite II and Frontier: First Encounters | games | *Elite*'s sequels, the second troubled at release | `games/elite`, `people/david-braben`, `people/ian-bell`, `companies/frontier-developments`, `people/chris-sawyer`, `techniques/procedural-generation`, `games/elite-dangerous` |
| Obliterator | games | Psygnosis's game, the period's example of a crack within hours | `communities/cracking-scene`, `companies/psygnosis` |
| Zarch and Virus | games | Braben's Archimedes showpiece and its 16-bit conversions | `people/david-braben`, `systems/acorn-archimedes`, `companies/superior-software`, `companies/firebird`, `companies/frontier-developments` |
| Revs and Aviator | games | Geoff Crammond's Acornsoft simulators | `companies/acornsoft`, `people/geoff-crammond`, `genres/racing-game`, `genres/racing-simulation`, `companies/firebird`, `companies/microprose` |
| Katakis and Denaris | games | Rainbow Arts' shooter, withdrawn and reworked over its likeness to *R-Type* | `companies/irem`, `games/r-type`, `companies/factor-5`, `companies/rainbow-arts`, `people/manfred-trenz`, `groups/triad`, `magazines/zzap-64`, `companies/activision` |
| Pitfall II: Lost Caverns | games | Crane's sequel, one of the few Activision cartridges converted to the Spectrum | `games/pitfall`, `people/david-crane` |
| Bored of the Rings | games | Delta 4's Quilled parody | `tools/the-quill` |
| Hampstead | games | A Quilled game from a big publisher, which reviewers debated | `tools/the-quill`, `companies/melbourne-house` |
| Mayhem in Monsterland | games | Apex's late C64 showpiece, with a published development diary | `techniques/parallax-scrolling`, `techniques/character-shift-parallax`, `magazines/commodore-format`, `techniques/vsp`, `techniques/agsp` |
| Beyond the Forbidden Forest | games | Paul Norman's early C64 multi-speed scrolling | `techniques/parallax-scrolling` |
| Ridge Racer | games | Namco's 1993 arcade racer and a PlayStation launch game | `companies/namco`, `companies/sony`, `games/tekken`, `systems/sony-playstation`, `games/daytona-usa`, `games/wipeout`, `games/pole-position`, `genres/racing-game`, `games/sega-rally`, `techniques/model-2` |
| Rally-X | games | Namco's 1980 maze game, which the trade expected to beat *Pac-Man* | `games/pac-man`, `companies/namco` |
| In the Hunt | games | Irem's 1993 submarine shooter, whose team became Nazca | `companies/irem`, `companies/nazca`, `games/metal-slug` |
| Neo Turf Masters | games | Nazca's other game | `companies/nazca`, `companies/snk`, `systems/neo-geo` |
| Pac-Land | games | Namco's 1984 side-scroller, Iwatani's favourite and a claimed influence on *Super Mario Bros.* | `people/toru-iwatani`, `games/pac-man`, `people/shigeru-miyamoto`, `companies/namco`, `genres/platformer`, `games/super-mario-bros` |
| Libble Rabble | games | Iwatani's twin-joystick game | `people/toru-iwatani`, `companies/namco` |
| Call of Duty | games | Activision's best-selling series, from 2003 | `companies/activision`, `companies/electronic-arts`, `genres/fps` |
| The Sims | games | Will Wright's 2000 game, made after EA bought Maxis | `companies/electronic-arts`, `companies/maxis`, `people/will-wright`, `genres/simulation-games`, `games/myst`, `people/dan-bunten` |
| Yu-Gi-Oh! | games | Konami's card and video games, one of its largest businesses since 1999 | `companies/konami` |
| Taiko no Tatsujin | games | Namco's long-running arcade drumming game | `companies/namco`, `genres/music-games` |
| .kkrieger | games | The 96 KB first-person shooter from .theprodukkt, Breakpoint 2004 | `communities/demo-parties`, `groups/farbrausch`, `groups/sanity`, `demos/fr-08-the-product`, `demos/debris`, `techniques/size-coding`, `people/ryg`, `people/kb` |
| 1943: The Battle of Midway | games | Capcom's 1987 sequel to *1942*, converted widely | `games/1942`, `companies/capcom` |
| 3D Monster Maze | games | J. K. Greye and Malcolm Evans's 1982 ZX81 T. rex chase | `genres/survival-horror`, `genres/horror-games`, `systems/sinclair-zx81`, `techniques/first-person-horror` |
| Abandoned Places | games | Amiga game known for its anti-cracker message | `groups/skid-row`, `groups/quartex` |
| Action Quake 2 | games | The mod where Le and Cliffe first worked together | `games/counter-strike`, `communities/modding` |
| ActRaiser | games | Quintet and Enix's action and god-game hybrid, with praised music | `people/yuzo-koshiro`, `companies/enix`, `genres/god-games`, `systems/super-nintendo` |
| Actua Soccer | games | Gremlin's motion-captured football game | `techniques/motion-capture`, `companies/gremlin-graphics` |
| Airwolf, Frank Bruno's Boxing, Kokotoni Wilf and Ikari Warriors | games | Elite's big sellers | `companies/elite-systems`, `people/john-twiddy`, `companies/gargoyle-games` |
| Alien Breed 3D | games | The first-person sequel, 91% in *Amiga Power* | `games/alien-breed`, `companies/team17`, `culture/amiga-power-versus-team17` |
| Alien Trilogy | games | Acclaim's first motion-capture showcase | `techniques/motion-capture`, `companies/acclaim` |
| Aliens TC | games | The best-documented *Doom* total conversion | `communities/total-conversions`, `games/doom` |
| Aliens Vs Predator (1999) | games | Rebellion's PC game, central to the first-person horror entry | `techniques/first-person-horror`, `genres/horror-games`, `companies/rebellion`, `games/aliens` |
| Alone in the Dark | games | Infogrames' 1992 game, the founding fixed-camera, pre-rendered horror game and the template for Resident Evil | `companies/infogrames`, `genres/survival-horror`, `techniques/tank-controls`, `techniques/pre-rendered-backgrounds`, `games/resident-evil`, `genres/horror-games` |
| Alpha Protocol | games | One of Obsidian's original worlds | `companies/obsidian-entertainment`, `people/tim-cain` |
| Anachronox | games | Cult RPG, the last Ion Storm Dallas game | `companies/ion-storm` |
| Aquaria | games | The 2007 IGF grand prize winner | `people/derek-yu`, `culture/indie-games` |
| Arkanoid: Revenge of Doh | games | The sequel, with its own reviews and credits | `games/arkanoid`, `companies/taito`, `people/mike-lamb` |
| Armored Core | games | FromSoftware's mech series, 1997 to 2023, where Miyazaki started | `companies/fromsoft`, `games/dark-souls` |
| Arx Fatalis | games | Arkane's 2002 Ultima Underworld homage | `genres/immersive-sim`, `companies/arkane-studios` |
| Asteroids Deluxe | games | The 1981 sequel that answered lurking with shields and harder saucers | `games/asteroids` |
| Astron Belt | games | Sega's first laserdisc game, 1983 | `techniques/fmv`, `companies/sega` |
| Axiom Verge | games | A key indie Metroidvania | `genres/metroidvania`, `culture/indie-games` |
| Bahamut Lagoon | games | One of the best-known fan-translation targets | `people/byuu`, `communities/fan-translations` |
| Balance of Power | games | Chris Crawford's Cold War diplomacy simulation | `companies/mindscape`, `people/chris-crawford` |
| Baldur's Gate 3 | games | Covered only inside other entries | `games/baldurs-gate`, `phenomena/crpg-renaissance`, `genres/western-rpg` |
| Baldur's Gate II: Shadows of Amn | games | The Hall of Fame sequel, named in several entries | `games/baldurs-gate`, `companies/bioware`, `companies/black-isle-studios` |
| Baldur's Gate: Dark Alliance | games | The console side of the Black Isle label | `companies/black-isle-studios`, `games/baldurs-gate` |
| Balloon Kid | games | The 1990 Game Boy follow-up to *Balloon Fight* | `games/balloon-fight` |
| Barbarian (Psygnosis) | games | Psygnosis's 1987 game, not Palace's, and Dean's favourite cover | `companies/psygnosis`, `companies/imagine-software`, `people/roger-dean`, `people/ian-hetherington` |
| BASIC Programming (Atari 2600 cartridge) | games | Robinett's programming environment on a 128-byte machine | `people/warren-robinett`, `systems/atari-2600` |
| Batman: The Caped Crusader | games | Ocean's 1988 Batman game, the middle of three, by Special FX | `games/batman-1986`, `companies/ocean-software`, `games/batman-the-movie`, `people/jonathan-smith`, `genres/arcade-adventure` |
| Batsugun and DoDonPachi | games | The bullet-hell starting points | `genres/shoot-em-up`, `companies/toaplan` |
| Battle Chess | games | Interplay's first self-published hit (1988) | `companies/interplay`, `people/brian-fargo` |
| Battle for Midway | games | The first PSS Wargamers title | `people/gary-mays`, `companies/pss` |
| Battlefield 1942 | games | DICE's 2002 game and the start of the *Battlefield* series | `companies/dice-studio`, `companies/electronic-arts`, `genres/fps` |
| Bejeweled / Hexic | games | Pajitnov's example of a puzzle game without progression, and his reply to it | `techniques/puzzle-game-design`, `people/alexey-pajitnov` |
| Below the Root | games | 1984 open-world adventure with ability-gated areas | `genres/metroidvania` |
| Beneath Apple Manor | games | Don Worth's 1978 random-dungeon game, which predates *Rogue* | `genres/roguelike`, `games/rogue`, `techniques/procedural-generation`, `techniques/permadeath` |
| Beyond a Steel Sky | games | Revolution's 2020 sequel | `companies/revolution-software`, `games/beneath-a-steel-sky`, `people/charles-cecil` |
| BioShock Infinite | games | Irrational's last game (2013) | `people/ken-levine`, `games/bioshock`, `companies/irrational-games` |
| Blade Runner (1997 game) | games | Westwood's voxel-character adventure and Castle's favourite | `companies/westwood-studios`, `people/louis-castle`, `companies/virgin-games` |
| Blast Corps | games | Rare's 1997 Nintendo 64 game, mentioned in the Rumble Pak entry | `techniques/rumble-pak`, `systems/nintendo-64` |
| Body Blows | games | Team17's Amiga reply to *Street Fighter II* | `games/street-fighter-ii` |
| Body Harvest | games | DMA Design's 1998 free-roaming N64 vehicle game, credited as GTA III's precursor | `companies/dma-design`, `systems/nintendo-64`, `people/dave-jones`, `games/gta-iii`, `techniques/open-world-design`, `games/grand-theft-auto` |
| Braid and Jonathan Blow | games | The independent platformer revival; *Braid* also introduced *Spelunky* to the Xbox | `culture/indie-games`, `distribution/digital-distribution`, `genres/platformer`, `games/spelunky`, `culture/xbox-live` |
| Brataccas | games | Psygnosis's first game, sold with a Dean poster | `companies/psygnosis`, `companies/imagine-software`, `people/roger-dean`, `people/ian-hetherington` |
| Broken Sword II: The Smoking Mirror | games | Revolution's 1997 sequel | `games/broken-sword`, `companies/revolution-software` |
| Buck Rogers: Planet of Zoom | games | Sega's 1982 sprite-scaling into-the-screen shooter | `genres/rail-shooters`, `games/space-harrier`, `techniques/sprite-scaling` |
| Buggy Boy | games | Elite's big-selling racer, which *Zzap!64* preferred to *Out Run* on the C64 | `games/out-run`, `companies/elite-systems` |
| BurgerTime | games | Data East's first remembered hit | `companies/data-east` |
| Burning Rangers and Samba de Amigo | games | Lower-priority Sonic Team games | `companies/sonic-team` |
| Bust a Groove | games | Enix's 1998 dance game, the first *PaRappa* follower | `games/parappa-the-rapper`, `genres/music-games` |
| Cadaver | games | The Bitmap Brothers' 1990 isometric adventure | `companies/bitmap-brothers`, `people/dan-malone` |
| Capcom vs. SNK | games | The crossover fighting series | `companies/snk`, `companies/capcom`, `games/king-of-fighters`, `games/street-fighter-ii` |
| Captive | games | Tony Crowther's generated-base Amiga RPG, an award-winner and the base for *Knightmare* and *Liberation* | `techniques/procedural-generation`, `people/tony-crowther`, `companies/mindscape`, `games/dungeon-master` |
| Carrier Command | games | Realtime's 1988 3D strategy game, also a manual look-up example | `companies/rainbird`, `companies/realtime-games`, `companies/telecomsoft`, `techniques/manual-protection` |
| Castle Master | games | The first Freescape game published by Domark (1990) | `techniques/freescape`, `companies/incentive-software`, `games/driller` |
| Castle Wolfenstein | games | Muse's 1981 game, the foundation of the stealth lineage and of id's *Wolfenstein 3D* | `communities/modding`, `communities/total-conversions`, `companies/id-software`, `techniques/stealth-mechanics`, `people/john-romero` |
| Castlevania II: Simon's Quest and Vampire Killer | games | The series' exploration precursors | `genres/metroidvania`, `games/castlevania`, `games/symphony-of-the-night` |
| Castlevania III: Dracula's Curse | games | The best-known MMC5 game, released on two mapper chips with different sound | `hardware/mmc5`, `hardware/apu`, `techniques/bank-switching`, `games/castlevania`, `games/symphony-of-the-night` |
| Castlevania: Rondo of Blood | games | The 1993 PC Engine CD prequel to *Symphony of the Night*, directed by Toru Hagihara | `people/koji-igarashi`, `games/castlevania`, `games/symphony-of-the-night`, `systems/pc-engine` |
| Chack'n Pop | games | Taito's 1983 precursor whose monsters reappear in Bubble Bobble | `games/bubble-bobble`, `companies/taito` |
| Champion Boxing | games | Suzuki's first game | `people/yu-suzuki` |
| Championship Manager | games | The Collyer brothers' series, the source of Sports Interactive's *Football Manager* | `companies/domark`, `companies/sports-interactive`, `companies/eidos`, `genres/management-game`, `games/football-manager`, `people/kevin-toms` |
| Chaos Strikes Back | games | *Dungeon Master*'s stand-alone sequel | `games/dungeon-master` |
| Chaos: The Battle of Wizards | games | One of the Spectrum's most discussed strategy games, now described only inside Gollop's entry | `people/julian-gollop`, `games/laser-squad`, `companies/firebird` |
| Chex Quest | games | A commercial *Doom* total conversion given away in cereal boxes | `communities/total-conversions` |
| Child of Eden | games | The 2011 spiritual sequel to *Rez* | `people/tetsuya-mizuguchi`, `games/rez`, `companies/q-entertainment` |
| ChipWits | games | The 1984 robot-programming rival to *Robot Odyssey* | `games/robot-odyssey` |
| Chocks Away and Star Fighter 3000 | games | Archimedes originals | `systems/acorn-archimedes` |
| Chris Sawyer's Locomotion | games | The 2004 successor to *Transport Tycoon* | `people/chris-sawyer`, `games/transport-tycoon` |
| Chrono Cross | games | The 1999 sequel to Chrono Trigger | `games/chrono-trigger`, `companies/square` |
| ChuChu Rocket! | games | Sonic Team's online puzzle game, given away to bring Dreamcast owners online | `companies/sonic-team`, `systems/sega-dreamcast` |
| Clive Barker's Undying | games | A PC game the period press cited for first-person horror | `techniques/first-person-horror`, `genres/horror-games` |
| Clock Tower | games | Human's 1995 game, the defenceless-heroine branch of survival horror | `genres/survival-horror` |
| Codename MAT | games | One of Brewster's best-known games | `people/derek-brewster` |
| Colin McRae Rally | games | Codemasters' 1998 rally game, whose producer said its premise came from *Sega Rally*'s handling | `games/sega-rally`, `companies/codemasters`, `genres/racing-game` |
| Colossal Adventure (Level 9) | games | Level 9's home-computer version of *Adventure* | `genres/text-adventure`, `companies/level-9` |
| Combat School | games | Konami's 1987 arcade game, converted for home computers by Ocean | `people/mike-lamb`, `people/andrew-deakin` |
| Command & Conquer: Tiberian Sun | games | The 1999 sequel to Command & Conquer | `games/command-and-conquer`, `games/red-alert` |
| Commander Keen | games | id's first hit and Apogee's breakthrough, built on adaptive tile refresh | `companies/id-software`, `companies/apogee-software`, `companies/softdisk`, `people/john-carmack`, `people/john-romero`, `distribution/shareware`, `people/scott-miller`, `companies/3d-realms` |
| Cool Spot | games | Virgin game linked to David Perry | `companies/virgin-games`, `people/david-perry` |
| Crackdown | games | Realtime Worlds' game | `people/dave-jones`, `culture/dundee-games-scene` |
| Croc: Legend of the Gobbos | games | Argonaut's biggest commercial success | `companies/argonaut` |
| Cruis'n USA and Cruis'n World | games | Eugene Jarvis's "Ultra 64" coin-op racers | `games/killer-instinct`, `companies/midway`, `systems/nintendo-64`, `techniques/difficulty-design` |
| Cruise for a Corpse | games | Delphine's 1991 Cinématique adventure | `games/prince-of-persia`, `companies/delphine-software`, `games/flashback`, `games/another-world` |
| Cyber Troopers Virtual-On | games | A multi-board Model 2 game | `techniques/model-2` |
| Cybernoid II: The Revenge | games | Hewson's 1988 sequel, 88% in CRASH and Rogers's favourite game | `games/cybernoid`, `people/dave-rogers`, `people/raffaele-cecco` |
| Cytron Masters | games | An early real-time strategy claimant, published by SSI | `genres/rts-genre`, `people/dan-bunten`, `games/dune-ii` |
| Daikatana | games | Ion Storm Dallas's 2000 game, against which the Deus Ex reviews measured it | `people/john-romero`, `companies/ion-storm`, `games/deus-ex`, `companies/eidos` |
| Dan Dare (Virgin) | games | Virgin game named in the Virgin Games entry | `companies/virgin-games` |
| Dance Central | games | Harmonix's Kinect series after the plastic-instrument slump | `companies/harmonix`, `genres/music-games` |
| Dandy | games | John Palevich's 1983 Atari 8-bit dungeon game that Logg named as an influence | `games/gauntlet` |
| Dark Reign | games | Activision's 1997 RTS, first with 3D terrain by *Edge*'s account | `games/total-annihilation`, `genres/rts-genre` |
| Dark Side | games | The second Freescape game (1988) | `techniques/freescape`, `companies/incentive-software`, `games/driller` |
| Dark Star | games | Design Design's 1984 CRASH Smash in 3D vector graphics | `companies/design-design`, `techniques/vector-graphics` |
| David's Midnight Magic | games | A 1983 Arkie winner | `magazines/electronic-games` |
| Dead Rising | games | Capcom's Xbox 360 million-seller | `people/keiji-inafune`, `companies/capcom` |
| Death Rally | games | Remedy's first game (1996), with music by Purple Motion | `people/purple-motion`, `companies/remedy-entertainment` |
| Death Star Interceptor | games | System 3's first game and an unlicensed *Star Wars* game | `companies/system-3` |
| Deathtrap Dungeon | games | Eidos game named in its entry | `companies/eidos` |
| Defense of the Ancients (DotA) | games | The *Warcraft III* mod behind Dota 2 and League of Legends | `communities/modding`, `culture/modding-to-industry`, `games/warcraft`, `companies/valve` |
| Deja Vu | games | ICOM Simulations' 1985 game, the first established mouse-driven adventure | `genres/graphic-adventure`, `techniques/point-and-click`, `companies/mindscape` |
| Deliverance: Stormlord II | games | Hewson's 1990 sequel, 91% in Your Sinclair | `games/stormlord`, `people/raffaele-cecco`, `people/dave-rogers` |
| Demon Attack | games | Imagic's 1983 Arkie winner, over which Atari sued | `magazines/electronic-games` |
| Der Langrisser | games | One of the best-known fan-translation targets | `people/byuu`, `communities/fan-translations` |
| Descent | games | Parallax's 1995 shooter with six degrees of freedom, published by Interplay | `companies/interplay` |
| Destiny | games | Bungie's post-*Halo* series (2014–2026) and the reason for the Activision and Sony deals | `companies/bungie`, `companies/activision`, `companies/sony` |
| Destruction Derby | games | Reflections' PlayStation launch hit for Psygnosis | `companies/psygnosis`, `games/wipeout` |
| Deus Ex: Invisible War and Human Revolution | games | Sequels with their own reception histories | `games/deus-ex` |
| Diablo II | games | The best-known game in the series | `games/diablo`, `companies/blizzard` |
| Dino Crisis | games | Capcom series that grew out of Mikami's team | `people/shinji-mikami`, `companies/capcom`, `genres/survival-horror` |
| Dirt Dash | games | Namco's 1995 System Super 22 stablemate of *Time Crisis* | `games/time-crisis`, `companies/namco` |
| Disgaea / Nippon Ichi Software | games | The series that led the tactical RPG in the 2000s | `genres/tactical-rpg` |
| Donkey Kong 64 | games | Rare's game sold with the Expansion Pak | `systems/nintendo-64`, `companies/rare` |
| Donkey Kong Country 2: Diddy's Kong Quest | games | The sequel | `games/donkey-kong-country`, `companies/rare`, `people/david-wise` |
| Doom II: Hell on Earth | games | The retail sequel and 1994 bestseller | `games/doom`, `companies/id-software` |
| Dota 2 | games | Valve game with modding roots | `companies/valve`, `communities/modding` |
| Double Dragon II: The Revenge | games | The arcade sequel, with its own NES and home versions | `games/double-dragon`, `companies/technos` |
| Dracula (CRL) | games | The first game given a BBFC certificate | `genres/horror-games`, `companies/crl-group`, `culture/game-ratings` |
| Dragon Slayer | games | Falcom's foundational action RPG | `genres/action-rpg`, `companies/falcom` |
| Dragon's Lair (laserdisc) | games | The 1983 laserdisc game the trade saw as the future, and the reference point for quick time events | `games/another-world`, `techniques/fmv`, `techniques/rotoscoping`, `people/eric-chahi`, `phenomena/golden-age-arcade`, `games/shenmue` |
| Dropzone | games | Archer Maclean's Atari and C64 shooter, whose game shell *IK* was built on | `games/international-karate` |
| Duke Nukem (1991) | games | Apogee's in-house franchise before *Duke Nukem 3D* | `companies/apogee-software`, `people/scott-miller`, `games/duke-nukem-3d`, `companies/3d-realms` |
| Duke Nukem Forever | games | The best-documented case of a game stuck in development | `companies/3d-realms`, `games/duke-nukem-3d`, `people/scott-miller` |
| Dune 2000 and Emperor: Battle for Dune | games | Westwood's return to Arrakis | `games/dune-ii`, `companies/westwood-studios` |
| Dungeons of Daggorath | games | Early real-time first-person dungeon game on the Tandy Color Computer (1982–83) | `games/dungeon-master`, `systems/tandy-coco` |
| Dwarf Fortress | games | Bay 12 Games' colony sim, which inspired RubyDung | `games/minecraft`, `genres/survival-games` |
| Dynamite Dan | games | Mirrorsoft's first hit, a *CRASH* Smash | `companies/mirrorsoft` |
| Earthworm Jim | games | A major Mega Drive and SNES platformer, with its own cartoon | `companies/virgin-games`, `companies/interplay`, `people/david-perry` |
| Eastern Front (1941) | games | Chris Crawford's landmark Atari wargame, with released source code | `techniques/hardware-scroll`, `people/chris-crawford`, `genres/wargame`, `systems/atari-8-bit` |
| Egghead | games | Jonathan Cauldwell's CRASH covertape series from 1990 | `people/jonathan-cauldwell`, `distribution/cover-tapes` |
| Elden Ring | games | An open-world *Souls* game made with George R. R. Martin, with more than 30 million sales | `companies/fromsoft`, `genres/action-rpg` |
| Emerald Mine | games | Kingsoft's Amiga Boulder Dash imitation | `games/boulder-dash`, `games/repton` |
| Emlyn Hughes International Soccer | games | A well-reviewed C64 football game that period magazines used as a yardstick | `companies/audiogenic`, `genres/sports-games`, `games/sensible-soccer` |
| Empire (Walter Bright) | games | The map-conquest game *CGW* compared *Civilization* with | `games/civilization`, `genres/4x-strategy` |
| Enigma Force | games | *Shadowfire*'s icon-driven 1986 sequel | `games/shadowfire`, `companies/denton-designs`, `companies/beyond-software` |
| Epic Mickey | games | Spector's Disney work | `people/warren-spector` |
| Escape from Monkey Island | games | The second and last GrimE game | `games/grim-fandango`, `games/monkey-island` |
| Eternal Darkness | games | The game with the sanity meter | `genres/horror-games` |
| Etrian Odyssey | games | Atlus's DS dungeon game, scored with PC-88 sounds | `people/yuzo-koshiro`, `companies/atlus`, `systems/nintendo-ds` |
| Eureka! | games | Domark's 1984 prize game with a documented winner, designed by Livingstone and programmed by Andromeda | `companies/domark`, `distribution/cover-tapes` |
| EverQuest | games | The second big American MMORPG, with period subscriber figures from *CGW* and *Edge* | `genres/mmorpg-history`, `companies/blizzard` |
| Every Extend Extra | games | A freeware PC game turned into Q Entertainment's commercial music shooter | `people/tetsuya-mizuguchi`, `companies/q-entertainment` |
| Exile | games | Irvin and Smith's 1988 arcade adventure, often paired with Elite as the peak of Acorn 8-bit games | `companies/superior-software`, `companies/acornsoft`, `companies/audiogenic` |
| Eye of the Beholder | games | Westwood's real-time dungeon crawler for SSI, its breakthrough | `companies/westwood-studios`, `games/dungeon-master`, `people/louis-castle`, `genres/western-rpg` |
| F-15 Strike Eagle, Silent Service and Gunship | games | The simulations that made MicroProse | `companies/microprose`, `people/sid-meier` |
| F-Zero | games | The SNES launch game that showed off mode 7 | `techniques/mode-7`, `systems/super-nintendo` |
| Fade to Black | games | Delphine's 1995 3D sequel to Flashback | `games/flashback`, `companies/delphine-software` |
| Falcon 3.0 | games | The sim period guides name for Thrustmaster set-ups | `hardware/flight-stick`, `genres/flight-sim` |
| Falklands '82 | games | PSS wargame attacked in the press | `people/gary-mays` |
| Fallout 2 | games | The first Black Isle-branded game, 1998 | `games/fallout`, `companies/black-isle-studios`, `people/tim-cain` |
| Famicom Wars | games | Intelligent Systems' grid wargame behind *Fire Emblem* and *Advance Wars* | `companies/intelligent-systems`, `games/advance-wars`, `genres/tactical-rpg` |
| Fantasy World Dizzy | games | The masked-sprite Dizzy the Olivers describe | `techniques/sprites`, `games/dizzy`, `people/oliver-twins` |
| Far Cry | games | Ubisoft series named in its entry | `companies/ubisoft` |
| Fatal Frame (Project Zero) | games | Tecmo's 2001 camera-as-weapon horror series | `genres/survival-horror`, `companies/tecmo` |
| Fez | games | A clear case of pixel art as a chosen style | `techniques/pixel-art` |
| Fighting Force | games | Core Design's 1997 game, the beat 'em up's move to 3D | `genres/beat-em-up` |
| Final Fantasy Adventure (Seiken Densetsu) | games | The first Mana game (Game Boy, 1991) | `games/secret-of-mana`, `companies/square` |
| Final Fantasy IV | games | The game that introduced Active Time Battle | `genres/jrpg`, `companies/square`, `games/final-fantasy`, `techniques/active-time-battle` |
| Final Fantasy VI and Final Fantasy X | games | The SNES and PS2 peaks of Uematsu's scores | `games/final-fantasy`, `people/nobuo-uematsu`, `companies/square` |
| First Samurai | games | Cecco's best-known Amiga game | `people/raffaele-cecco` |
| FlatOut | games | Bugbear's 2004 racer, with the ragdoll as entertainment | `techniques/ragdoll-physics` |
| Flight Unlimited | games | Looking Glass's self-published flight simulator | `companies/looking-glass`, `genres/flight-sim` |
| Flying Shark | games | Dominic Robinson's next Spectrum job after Zynaps | `games/zynaps`, `people/steve-turner` |
| Football Manager 2 | games | Addictive's 1988 sequel | `games/football-manager-1982`, `people/kevin-toms`, `companies/addictive-games` |
| Formula One Grand Prix | games | Crammond's series (*World Circuit* in the US) | `people/geoff-crammond`, `companies/microprose`, `genres/racing-simulation`, `genres/racing-game` |
| Fort Apocalypse | games | Synapse's helicopter game, accused of being a *Choplifter* clone | `games/choplifter` |
| Fortnite | games | Post-period, but part of the story of Epic and the Unreal engine | `companies/epic-games`, `tools/unreal-engine`, `people/tim-sweeney` |
| Freddy Pharkas, Frontier Pharmacist | games | Lowe and Josh Mandel's Western comedy, praised by *CGW* | `people/al-lowe`, `companies/sierra` |
| Freedom Fighters | games | IO's 2003 EA-published game, scored by Kyd | `companies/io-interactive`, `people/jesper-kyd` |
| Freedom Force | games | Irrational's second game (2002) and the Boston–Canberra split | `people/ken-levine`, `companies/irrational-games` |
| Frequency and Amplitude | games | Harmonix's first games and the root of *Guitar Hero*'s note highway | `genres/music-games`, `companies/harmonix`, `games/guitar-hero`, `games/rock-band` |
| From Dust | games | Éric Chahi's god game | `genres/god-games`, `people/eric-chahi` |
| FTL and Rogue Legacy | games | Modern permadeath examples | `genres/roguelike`, `techniques/permadeath` |
| Full Contact | games | One of Team17's first Amiga games | `companies/team17`, `people/andreas-tadic` |
| Future Wars and the Cinématique games | games | Delphine's adventure system and series (Future Wars, Operation Stealth, Cruise for a Corpse), and Chahi's earlier work | `companies/delphine-software`, `games/another-world`, `games/flashback` |
| G-LOC and the R360 cabinet | games | The fully rotating cockpit often confused with After Burner's | `games/after-burner`, `companies/sega-am2`, `people/yu-suzuki` |
| Gabriel Knight and Jane Jensen | games | One of Sierra's main series | `companies/sierra` |
| Galaga '88 | games | Namco's 1987 sequel, the fans' favourite in period reviews | `games/galaga`, `games/galaxian`, `companies/namco` |
| Galaxy Game | games | The 1971 Stanford PDP-11 coin-op, and the question of which coin-op came first | `genres/arcade-game`, `techniques/vector-graphics` |
| Galcon, Evoland, Titan Souls and Friday Night Funkin' | games | Commercial games that began at Ludum Dare | `communities/ludum-dare`, `culture/game-jams` |
| Game & Watch Mario Bros. | games | The other 1983 game with Luigi in it | `games/mario-bros`, `systems/nintendo-game-and-watch` |
| Gargoyle's Quest | games | Red Arremer's own series | `games/ghosts-n-goblins`, `people/tokuro-fujiwara` |
| Gauntlet II | games | The 1986 sequel, also converted by U.S. Gold | `games/gauntlet`, `people/ed-logg` |
| Gears of War | games | Post-period, but part of the story of Epic and the Unreal engine | `companies/epic-games`, `tools/unreal-engine`, `people/tim-sweeney` |
| Gertrude's Puzzles and Gertrude's Secrets | games | Learning Company titles reviewed alongside *Rocky's Boots* | `games/rockys-boots`, `companies/the-learning-company` |
| Gitaroo Man / iNiS | games | A rhythm game whose designer credits *PaRappa* | `games/parappa-the-rapper`, `genres/music-games` |
| Gloom | games | One of the first Amiga answers to *Doom* | `people/mark-sibly`, `companies/acid-software`, `games/doom` |
| Goal! | games | Dino Dini's Virgin game, marketed against *Sensible Soccer* | `people/dino-dini`, `games/sensible-soccer`, `companies/virgin-games` |
| Godus | games | 22cans' successor to *Populous* | `people/peter-molyneux`, `genres/god-games`, `games/populous` |
| Golf Construction Set | games | Ariolasoft game named in its entry | `companies/ariolasoft` |
| Gorf | games | Midway's 1981 game, origin of the "Galaxians" name | `games/galaxian`, `companies/midway` |
| Graham Gooch cricket and Brian Lara Cricket | games | Audiogenic's long-running cricket line, which became Codemasters' series | `companies/audiogenic`, `companies/codemasters` |
| Gran Trak 10 | games | Atari's first video driving game with a wheel | `hardware/steering-wheel`, `companies/atari`, `genres/racing-game` |
| Grand Prix Legends | games | Papyrus's 1998 sim, with period coverage in *Edge*, *CGW* and *InterAction* | `genres/racing-simulation`, `techniques/force-feedback`, `companies/sierra` |
| Grand Theft Auto 2 | games | The main-series game between *GTA* and *GTA III* | `games/grand-theft-auto`, `companies/rockstar-north`, `games/gta-iii` |
| Grand Theft Auto: Vice City and San Andreas | games | The main-series games after *GTA III* | `games/grand-theft-auto`, `companies/rockstar-north`, `games/gta-iii`, `techniques/renderware` |
| Green Beret | games | Joffa Smith's conversion of Konami's coin-op, *CRASH*'s reference point for *Cobra* | `games/cobra`, `people/jonathan-smith`, `companies/ocean-software` |
| Gridiron! | games | Bethesda game whose dispute with EA bears on the Madden origin story | `companies/bethesda`, `games/madden`, `companies/electronic-arts` |
| Guitar Freaks and Drummania | games | Konami's 1999 guitar and drum arcade games, with a linked band mode long before Rock Band | `genres/music-games`, `companies/bemani`, `games/guitar-hero`, `games/rock-band`, `games/beatmania` |
| Gun Fight (Western Gun) | games | Nishikado's 1975 game, licensed to Midway, and an early microprocessor game | `hardware/arcade-hardware`, `companies/midway`, `people/tomohiro-nishikado`, `companies/taito` |
| Gyroscope | games | Melbourne House's Marble Madness-style game | `games/marble-madness`, `companies/melbourne-house` |
| H.A.T.E. | games | Vortex/Gremlin, 1989 | `techniques/software-scroll`, `people/costa-panayi`, `companies/vortex-software` |
| Habitat | games | Chip Morningstar's Lucasfilm online world, where SCUMM's walking code came from | `techniques/scumm`, `companies/lucasarts`, `genres/mmorpg-history`, `systems/commodore-64` |
| Hack | games | The 1982–85 link between *Rogue* and *NetHack*, with its own Usenet history | `games/nethack`, `games/rogue`, `genres/roguelike` |
| Hack, Moria and Angband | games | The main branches of the traditional roguelike family | `genres/roguelike`, `games/nethack`, `games/rogue` |
| Halls of the Things | games | A well-known 1983 Spectrum game from Design Design | `companies/design-design` |
| Halo 2 | games | The 2004 game that took Xbox Live mainstream | `games/halo`, `culture/xbox-live`, `companies/bungie` |
| Hamurabi and The Sumerian Game | games | The earliest management games | `genres/simulation-games`, `books/basic-computer-games`, `people/david-ahl`, `genres/management-game`, `distribution/type-in-listings` |
| Haunted House (Atari VCS) | games | The 1982 game about fear of the dark, the earliest console game in the horror line | `genres/survival-horror`, `genres/horror-games`, `systems/atari-2600` |
| Heart of Darkness and Amazing Studio | games | Chahi's six-year cinematic platformer, made with Flashback staff | `games/another-world`, `people/eric-chahi`, `techniques/pre-rendered-backgrounds`, `games/flashback`, `companies/delphine-software` |
| Her Story | games | The 2015 FMV revival | `techniques/fmv` |
| Herzog Zwei | games | Technosoft's 1989 game, the most-cited first RTS | `genres/rts-genre`, `companies/technosoft`, `systems/sega-mega-drive`, `games/dune-ii` |
| Hexic | games | Pajitnov's Microsoft puzzle game, packed with the Xbox 360 | `people/alexey-pajitnov` |
| Hogan's Alley and Wild Gunman | games | NES launch light-gun games; Wild Gunman is a known Zapper test case | `hardware/nes-zapper`, `games/duck-hunt`, `hardware/light-gun` |
| Hydlide / T&E Soft | games | One of the 1984 action RPGs, which sold widely in Japan | `genres/action-rpg` |
| I, Robot | games | Dave Theurer's 1983 filled-polygon arcade game, with a period review that predicted its failure | `games/tempest`, `people/dave-theurer`, `games/hard-drivin`, `techniques/vector-graphics`, `companies/atari-games`, `companies/atari` |
| Ikari Warriors | games | SNK's 1986 shooter, with Elite's home versions | `companies/snk`, `companies/elite-systems`, `games/commando`, `people/tokuro-fujiwara` |
| Ikaruga and Radiant Silvergun | games | Treasure's shooters | `genres/shoot-em-up`, `companies/treasure` |
| Impossible Mission II | games | The 1988 sequel, a *ZZAP!64* Gold Medal | `companies/epyx`, `games/impossible-mission` |
| In Cold Blood | games | Revolution's 2000 spy adventure for Sony | `companies/revolution-software` |
| Indiana Jones and the Fate of Atlantis | games | LucasArts' SCUMM adventure, referenced in the SCUMM and Day of the Tentacle entries | `techniques/scumm`, `games/day-of-the-tentacle` |
| Infiniminer | games | Zachary Barth's 2009 game, which Persson credited with inspiring *Minecraft* | `games/minecraft`, `people/markus-persson` |
| Infocom's other games (Starcross, the Enchanter trilogy, Suspect, The Lurking Horror) | games | Individual Infocom games with good period coverage | `people/dave-lebling`, `companies/infocom`, `people/marc-blank`, `people/steve-meretzky` |
| Injustice: Gods Among Us | games | NetherRealm's second series (2013) | `people/ed-boon`, `companies/netherrealm-studios` |
| International Soccer | games | Commodore's C64 football game, the benchmark for mid-1980s football games | `games/match-day`, `genres/sports-games` |
| International Superstar Soccer | games | Konami's series before *Pro Evolution Soccer*, often confused with it | `games/fifa`, `games/pro-evolution-soccer`, `companies/konami` |
| Island of Kesmai / Kesmai | games | CompuServe's 1985 multiplayer RPG | `genres/mmorpg-history`, `genres/mud-history` |
| Jack the Ripper (St Brides) | games | CRL's 1987 adventure, described as the first commercial PAW adventure | `tools/paw`, `companies/crl-group` |
| Jade Empire | games | BioWare game named in its entry | `companies/bioware` |
| Jagged Alliance | games | The Western tactical RPG between *X-COM* and later squad games | `genres/tactical-rpg` |
| Jazz Jackrabbit | games | Epic's best-known shareware platform game | `distribution/shareware`, `companies/epic-games`, `people/tim-sweeney` |
| Jill of the Jungle | games | Epic MegaGames' 1992 breakthrough, paid for by ZZT's registrations | `tools/zzt`, `people/tim-sweeney`, `companies/epic-games`, `distribution/shareware` |
| Joe Blade | games | Players' best-known release, a 1987–88 budget best seller | `companies/players-software`, `distribution/budget-games` |
| Journey (arcade) | games | The 1983 arcade game with digitised faces, and a home-to-coin-op first | `techniques/digitized-sprites`, `companies/midway` |
| Joust 2: Survival of the Fittest | games | Williams' 1986 sequel | `games/joust`, `companies/williams-electronics` |
| Jump Bug and Crazy Climber | games | Early side-scrolling and climbing games | `genres/platformer` |
| Jumpman | games | Randy Glover's game, Epyx's first action hit | `companies/epyx` |
| Just Dance | games | Ubisoft's controller-free dance series, which outsold instrument games in 2009 | `genres/music-games`, `companies/ubisoft` |
| Kaboom! | games | Activision's paddle game, the best-known reason to own VCS paddles | `hardware/paddle-controller`, `companies/activision` |
| Kane & Lynch | games | IO Interactive's second series (2007, 2010) | `companies/io-interactive` |
| Karaoke Revolution | games | Harmonix's singing game for Konami, the source of *Rock Band*'s vocals | `companies/harmonix`, `games/rock-band`, `genres/music-games` |
| Karate Champ | games | Data East's arcade game, at the centre of the Epyx case and the model for *Exploding Fist* | `companies/data-east`, `games/international-karate`, `games/way-of-the-exploding-fist`, `companies/epyx`, `companies/technos`, `genres/beat-em-up`, `games/street-fighter`, `games/street-fighter-ii` |
| Kentilla | games | One of Brewster's best-known games | `people/derek-brewster` |
| King's Field | games | FromSoftware's first game, a PlayStation launch RPG and the ancestor of the *Souls* games | `games/dark-souls`, `games/demons-souls`, `companies/fromsoft` |
| Kingdom Hearts | games | Square and Disney's 2002 series | `companies/square` |
| Kirby's Adventure | games | The 1993 NES game where copy abilities began | `games/kirby`, `people/masahiro-sakurai` |
| Knight Orc | games | Level 9's first KAOS game, with independent characters | `companies/level-9`, `companies/rainbird` |
| Knight Tyme | games | MAD's 1986 Magic Knight game, the first CRASH Smash for a Spectrum 128 game | `people/david-jones-magic-knight`, `games/spellbound`, `companies/mastertronic` |
| Kokotoni Wilf | games | Elite's first release under that name | `people/steve-wilcox`, `companies/elite-systems` |
| Krakout | games | Gremlin's 1987 Breakout game that every Arkanoid review compared | `games/arkanoid`, `games/breakout` |
| Kroz | games | Scott Miller's first shareware trilogy and the origin of the Apogee model | `distribution/shareware`, `people/scott-miller`, `companies/apogee-software` |
| Labyrinth (Lucasfilm Games) | games | The first Lucasfilm adventure, 1986, whose word wheel came before the verb list | `techniques/point-and-click`, `games/maniac-mansion` |
| Lands of Lore | games | Westwood's non-RTS work | `companies/westwood-studios`, `companies/virgin-games` |
| Laser Squad Nemesis | games | Codo's 2002 play-by-email successor | `games/laser-squad`, `people/julian-gollop` |
| Last Ninja 2 | games | The first *Last Ninja* on the Spectrum, a *CRASH* Smash | `games/the-last-ninja`, `companies/system-3`, `people/john-twiddy`, `techniques/vsync`, `techniques/frameskipping-and-interpolation` |
| Laura Bow mysteries | games | *The Colonel's Bequest* and *The Dagger of Amon Ra* | `people/roberta-williams`, `companies/sierra` |
| Lazy Jones | games | David Whittaker's game and the source of *Kernkraft 400* | `people/david-whittaker` |
| Legend of the Red Dragon | games | The best-known door game | `communities/bbs-door-games`, `communities/bbs-scene` |
| Lemmings 2: The Tribes | games | The 1993 sequel | `games/lemmings` |
| Lethal Enforcers | games | Konami's 1992 digitised-actor gun game, which the press compared *Virtua Cop* to | `games/virtua-cop`, `hardware/light-gun` |
| Lightforce and Faster Than Light | games | Gargoyle's 1986 shoot-'em-up and its FTL label | `companies/gargoyle-games`, `games/heavy-on-the-magick` |
| Lineage / NCsoft | games | The largest online game of its day, and the Korean PC-café scene | `genres/mmorpg-history`, `people/richard-garriott` |
| Loom, Zak McKracken, Fate of Atlantis, The Dig and The Curse of Monkey Island | games | Lucasfilm's adventure designed with no dead ends | `companies/lucasarts`, `techniques/scumm`, `culture/lucasarts-adventures`, `techniques/point-and-click`, `genres/graphic-adventure`, `culture/adventure-game-deaths` |
| Lords of Chaos | games | Gollop's game, published by Blade Software | `games/laser-squad`, `people/julian-gollop` |
| Lost Planet | games | Capcom game named in the Inafune entry | `people/keiji-inafune`, `companies/capcom` |
| LostWinds | games | Frontier's first self-published game, a WiiWare launch game | `companies/frontier-developments` |
| Lotus Esprit Turbo Challenge | games | Magnetic Fields' racing series for Gremlin | `companies/gremlin-graphics`, `companies/krisalis` |
| Lunar Lander | games | Atari's first vector game, the hardware Asteroids was built on | `games/asteroids`, `people/ed-logg`, `techniques/vector-graphics` |
| Magic Carpet | games | Bullfrog game named in several entries | `people/peter-molyneux`, `companies/bullfrog`, `genres/god-games`, `games/populous`, `games/syndicate` |
| Magic Knight series (Finders Keepers, Stormbringer) | games | The rest of David Jones's Magic Knight games, as one entry or several | `people/david-jones-magic-knight`, `games/spellbound`, `companies/mastertronic`, `companies/mastertronic-added-dimension` |
| Magic Pockets | games | The Bitmap Brothers' second Renegade game (1991), with Betty Boo's music | `companies/bitmap-brothers`, `companies/renegade`, `games/gods`, `games/chaos-engine` |
| Major Havoc | games | Owen Rubin's 1983 vector game | `people/mark-cerny`, `companies/atari-games` |
| Manchester United (Krisalis) | games | Krisalis's football series | `companies/krisalis` |
| Manhunt | games | Rockstar North's 2003 game and the 2004 retail withdrawal | `companies/rockstar-north` |
| Manhunter | games | The last AGI games | `techniques/agi-engine` |
| Manx TT Super Bike and Sega Touring Car Championship | games | Mizuguchi's AM3 and AM Annex racers, before United Game Artists | `people/tetsuya-mizuguchi`, `games/sega-rally`, `genres/racing-game`, `companies/united-game-artists` |
| Marathon | games | Bungie's 1994–95 Mac shooters, source of the Aleph One engine, sold to Microsoft with *Halo* | `games/halo`, `companies/bungie`, `games/doom`, `genres/console-fps` |
| Mario Party | games | Hudson's Nintendo 64 series | `companies/hudson-soft`, `companies/nintendo` |
| Marsport | games | The third Cuchulainn game (1985), 95% in *CRASH* | `companies/gargoyle-games`, `games/dun-darach`, `genres/arcade-adventure` |
| Marvel vs. Capcom 2 | games | The first game other than Street Fighter at Battle by the Bay events | `events/evo`, `communities/fighting-game-community`, `systems/sega-naomi`, `systems/sega-dreamcast` |
| Master of Orion | games | The 1993 game the term "4X" was coined for | `games/civilization`, `genres/4x-strategy` |
| Match Day II | games | Ritman and Drummond's sequel, *CRASH* readers' number one in 1988 | `people/jon-ritman`, `people/bernie-drummond` |
| Max Payne | games | Remedy's defining game (2001), with bullet time and the Max-FX engine | `people/skaven`, `companies/remedy-entertainment`, `companies/futuremark`, `companies/rockstar`, `companies/3d-realms`, `techniques/ragdoll-physics`, `techniques/havok` |
| Maze War | games | The early networked first-person maze game at MIT and on the ARPANET | `people/dave-lebling`, `games/zork` |
| MDK2 | games | BioWare game named in its entry | `companies/bioware` |
| Mega Man 3 | games | The next game, which kept the eight-master structure | `games/mega-man-2`, `games/mega-man` |
| Mega-lo-Mania | games | Early games the press called real-time strategy | `genres/god-games`, `companies/sensible-software`, `people/jon-hare`, `companies/mirrorsoft`, `genres/rts-genre`, `companies/bullfrog` |
| Mercenary | games | Paul Woakes's open-world 3D game, *ZZAP!64*'s benchmark for free-roaming 3D | `games/driller`, `techniques/freescape`, `people/mike-dailly`, `techniques/open-world-design`, `companies/novagen`, `games/elite` |
| Mercs | games | Capcom's 1990 game | `games/commando`, `companies/capcom` |
| Meridian 59 | games | Early Internet graphical MUD (3DO/Archetype) | `genres/mmorpg-history` |
| Metal Gear | games | Konami's 1987 MSX2 game, the origin of the series and of its stealth design | `systems/msx`, `companies/konami`, `people/hideo-kojima`, `games/metal-gear-solid`, `techniques/stealth-mechanics` |
| Metal Gear Solid 2: Sons of Liberty | games | The 2001 sequel | `games/metal-gear-solid`, `people/hideo-kojima`, `companies/konami`, `systems/sony-playstation-2` |
| Metal Slug 2, Metal Slug X and Metal Slug 3 | games | The sequels | `games/metal-slug`, `companies/nazca`, `companies/snk` |
| Metal Warrior | games | Lasse Öörni's C64 game series, the main example in the scrolling and tile-map entries | `techniques/multidirectional-scrolling`, `techniques/tile-maps` |
| Meteos | games | Sakurai's 2005 DS puzzle game for Q Entertainment | `people/tetsuya-mizuguchi`, `companies/q-entertainment`, `people/masahiro-sakurai` |
| Metroid Dread | games | The 2D Metroid line after Super Metroid | `genres/metroidvania`, `games/metroid`, `people/yoshio-sakamoto` |
| MicroProse Soccer | games | Sensible's 1988 C64 football game | `companies/sensible-software`, `people/jon-hare`, `games/sensible-soccer`, `companies/microprose` |
| Midwinter | games | Mike Singleton's 1990 Rainbird game and a landmark 3D strategy game | `companies/rainbird`, `people/mike-singleton`, `companies/telecomsoft`, `people/pete-cooke` |
| Mighty Bomb Jack | games | Tecmo's 1986 sequel and its first Famicom game | `games/bomb-jack`, `companies/tecmo` |
| Mighty No. 9 | games | A crowdfunding case study with a period link | `people/keiji-inafune`, `games/mega-man`, `phenomena/crpg-renaissance` |
| Mikie | games | Joffa Smith's 1986 Konami conversion for Imagine | `people/jonathan-smith`, `companies/ocean-software` |
| Millipede | games | Logg's 1982 Centipede sequel, with published source | `people/ed-logg`, `games/centipede` |
| Mindfighter | games | Abstract Concepts' game, the one written with S.W.A.N. | `people/tim-gilberts`, `people/graeme-yeandle` |
| Mined-Out | games | Ian Andrew's 1983 Quicksilva game, a precursor of Minesweeper-style deduction | `people/ian-andrew`, `companies/quicksilva`, `companies/incentive-software` |
| Monkey Island 2: LeChuck's Revenge | games | The first iMUSE game and the source of the disputed ending | `games/monkey-island`, `companies/lucasarts`, `magazines/ace-magazine`, `tools/deluxe-paint` |
| Monster Max | games | Ritman and Drummond's last game together (Game Boy, 1994) | `people/jon-ritman`, `people/bernie-drummond`, `companies/rare`, `people/david-wise` |
| Moon Cresta | games | Nichibutsu's 1980 game, the best known on Galaxian hardware | `games/galaxian` |
| Moria and Angband | games | The other major Usenet dungeon games, named alongside *NetHack* | `games/diablo`, `genres/roguelike`, `games/nethack`, `games/rogue` |
| Mortal Kombat Mythologies: Sub-Zero | games | Tobias's 1997 story-driven spin-off | `people/john-tobias`, `games/mortal-kombat` |
| Mother 3 | games | The *EarthBound* sequel known in the West through its fan translation | `communities/fan-translations`, `games/earthbound`, `people/shigesato-itoi` |
| Moto Racer | games | Delphine's racing series | `companies/delphine-software`, `companies/electronic-arts` |
| Motor Toon Grand Prix | games | The PlayStation racer whose physics and team led to *Gran Turismo* | `games/gran-turismo`, `companies/polyphony-digital` |
| Mystery Dungeon and Fatal Labyrinth | games | Chunsoft's roguelike series and Sega's | `genres/roguelike`, `companies/chunsoft`, `games/pokemon-mystery-dungeon` |
| Mystery House | games | The 1980 adventure with pictures that launched Sierra, the first graphic adventure by the usual reckoning | `companies/sierra`, `people/roberta-williams`, `genres/graphic-adventure`, `games/kings-quest` |
| Myth | games | Bungie's real-time tactics series, with no base-building and full 3D terrain; *Halo* began on its engine | `games/halo`, `companies/bungie`, `genres/rts-genre` |
| Myth: History in the Making | games | System 3 game, a *ZZAP!64* Sizzler, with Amiga music by Jeroen Tel | `companies/system-3`, `hardware/paula`, `people/jeroen-tel` |
| Mônica no Castelo do Dragão | games | Tectoy's localised Master System game, the first rebuilt around a Brazilian character | `culture/brazil-gaming`, `companies/tectoy`, `games/wonder-boy` |
| Namco Museum | games | How Namco's early arcade games reached the PlayStation | `games/galaga`, `companies/namco`, `games/pac-man` |
| NARC | games | Jarvis's 1988 digitised Williams game, which drew Boon into video games | `people/ed-boon`, `people/eugene-jarvis`, `techniques/digitized-sprites`, `companies/williams-electronics` |
| Naughty Ones | games | Kompart platform game by Melon Dezign and Interactivision | `groups/melon-dezign` |
| Navy Seals | games | Öörni's example of char-step C64 scrolling | `techniques/scrolling`, `techniques/multidirectional-scrolling` |
| Need for Speed | games | Series named in the Criterion, Guildford and EA entries | `companies/criterion`, `culture/guildford-games-cluster`, `companies/electronic-arts` |
| Nether Earth | games | 1987 Spectrum game with robot production | `genres/rts-genre` |
| Netherworld | games | Hewson's 1988 game with Rogers's music-fader design | `people/dave-rogers`, `companies/hewson-consultants` |
| Neverwinter Nights (AOL, 1991) | games | AOL's 1991 online RPG, distinct from BioWare's 2002 game | `genres/mmorpg-history` |
| Night Driver | games | Atari's 1976 first-person driving game | `techniques/pseudo-3d-road`, `genres/racing-game`, `hardware/steering-wheel` |
| Night Trap | games | Digital Pictures' Mega-CD game, the most discussed exhibit at the 1993 hearings | `people/howard-lincoln`, `culture/congressional-hearings-1993`, `companies/midway`, `culture/mortal-kombat-controversy`, `games/mortal-kombat`, `culture/esrb`, `companies/sega`, `techniques/fmv`, `genres/horror-games`, `techniques/digitized-sprites` |
| NiGHTS into Dreams, Guardian Heroes, F355 Challenge, Virtua Tennis and Phantasy Star Online | games | Sonic Team's first Saturn game, sold with its own analogue pad | `systems/sega-saturn`, `systems/sega-dreamcast`, `systems/sega-naomi`, `companies/sonic-team`, `techniques/analog-control`, `people/yuji-naka` |
| Nintendogs and Brain Training | games | The DS's audience-widening hits | `systems/nintendo-ds` |
| Nosferatu | games | Design Design's 1986 game, published by Piranha | `companies/design-design`, `companies/piranha` |
| Number Munchers and Odell Lake | games | MECC's other widely used programs | `companies/mecc`, `culture/educational-software` |
| Obduction | games | Cyan's first Kickstarter game | `companies/cyan` |
| Onimusha | games | Capcom's samurai series, produced by Inafune | `people/keiji-inafune`, `companies/capcom`, `people/shinji-mikami` |
| Operation Wolf (Ocean) | games | Taito's 1987 gun game, which *Edge* said "defined the rules", with Ocean's home conversions | `people/jonathan-dunn`, `companies/ocean-software`, `companies/taito`, `games/chase-hq`, `games/virtua-cop`, `hardware/light-gun`, `hardware/nes-zapper`, `genres/rail-shooters` |
| Ostron | games | Softek's 1983–84 Spectrum clone of *Joust* | `games/joust` |
| Out Run Europa | games | Probe's US Gold original, delayed from 1989 to 1991 | `games/out-run`, `companies/probe-software`, `people/jeroen-tel`, `people/matt-furniss` |
| OutRun 2 | games | The 2003 arcade sequel Suzuki produced | `games/out-run`, `people/yu-suzuki` |
| P.T. | games | The 2014 game cited in the Konami and survival horror entries | `genres/survival-horror`, `games/silent-hill`, `people/hideo-kojima`, `techniques/first-person-horror` |
| Panzer General | games | The wargame that reached non-wargamers | `genres/wargame` |
| Paper Mario | games | Intelligent Systems' series | `companies/intelligent-systems` |
| Paperboy 2 | games | Mindscape's sequel | `games/paperboy`, `companies/mindscape` |
| Paradroid 90 | games | Braybrook's Amiga/ST remake and the Hewson/Activision episode | `games/paradroid`, `people/andrew-braybrook`, `companies/graftgold` |
| Parallax | games | Sensible Software's first game, for Ocean, with Galway's longest-composed theme | `people/martin-galway`, `companies/sensible-software`, `people/jon-hare`, `companies/ocean-software` |
| Parasol Stars | games | The third Bub-and-Bob game, released only on home formats | `games/bubble-bobble`, `games/rainbow-islands`, `companies/taito`, `companies/ocean-software` |
| Passengers on the Wind | games | Early comic-strip adaptation reviewers struggled to classify | `companies/infogrames`, `genres/graphic-adventure` |
| Penetrator | games | Melbourne House's Scramble-style Spectrum bestseller | `games/scramble`, `companies/melbourne-house` |
| Penguin Adventure | games | Konami's 1986 MSX game, Kojima's first credit | `systems/msx`, `people/hideo-kojima` |
| Phantasmagoria | games | Sierra's 1995 seven-CD FMV horror game | `people/roberta-williams`, `companies/sierra`, `techniques/fmv` |
| Phantasy Star Online | games | Sonic Team's Dreamcast online RPG, with word-select translation | `companies/sonic-team`, `systems/sega-dreamcast`, `games/phantasy-star`, `people/yuji-naka`, `culture/online-multiplayer` |
| Pilotwings 64 | games | The other Japanese N64 launch game | `games/super-mario-64`, `systems/nintendo-64` |
| Pinball and Golf (Famicom) | games | HAL's first Nintendo work, 1984 | `people/satoru-iwata`, `companies/hal-laboratory` |
| Pinball Dreams | games | The Silents' founders' first game, the founding game of DICE | `groups/fairlight`, `groups/the-silents`, `companies/dice-studio`, `companies/hewson-consultants`, `people/andrew-hewson`, `groups/skid-row` |
| Pipe Mania / Pipe Dream | games | Named by Pajitnov as a classic puzzle game | `techniques/puzzle-game-design` |
| Pit-Fighter | games | The first game made entirely of digitised fighters, on scaling hardware | `games/mortal-kombat`, `techniques/digitized-sprites`, `techniques/sprite-scaling`, `companies/atari-games`, `companies/domark` |
| Platoon | games | Ocean's first film breakthrough, 1987 | `culture/reading-the-charts`, `culture/licensed-games`, `companies/ocean-software` |
| Player Manager | games | The first *Kick Off* spin-off, which put the player on the pitch as manager | `people/dino-dini`, `companies/anco` |
| Podd | games | Acornsoft's primary-school staple | `culture/educational-software`, `companies/acornsoft` |
| Point Blank | games | Namco's 1994 gun game, the second GunCon game | `games/time-crisis`, `hardware/light-gun` |
| Pokémon Stadium | games | The first Pokémon home-console game, with Game Boy teams in 3D | `games/pokemon-red-blue`, `games/pokemon`, `systems/nintendo-64` |
| Pokémon Trading Card Game | games | Launched in Japan in October 1996 | `games/pokemon-red-blue`, `phenomena/pokemon-phenomenon` |
| Police Quest and Jim Walls | games | Sierra's AGI and SCI police series, designed by Jim Walls | `companies/sierra`, `games/leisure-suit-larry`, `techniques/agi-engine`, `techniques/sci-engine`, `people/al-lowe`, `games/space-quest` |
| Policenauts | games | Kojima's 1994 detective adventure, never officially translated | `people/hideo-kojima`, `companies/konami` |
| Pool of Radiance | games | SSI's first Gold Box game, with a code wheel and manual look-ups | `techniques/code-wheels`, `techniques/manual-protection` |
| Pooyan | games | Konami's 1982 balloon game, which *C&VG* saw in *Balloon Fight* | `games/balloon-fight` |
| Pop'n Music | games | Konami's big-button music game for younger players | `games/beatmania`, `companies/bemani` |
| Populous II | games | Bullfrog's 1991 sequel | `games/populous`, `companies/bullfrog`, `genres/god-games` |
| Portal and The Orange Box | games | Valve's compilation and *Portal* | `companies/valve`, `games/half-life-2` |
| Power Drift, G-LOC and the R360 | games | Sega's 1988 Y Board scaling-and-rotation racer | `people/yu-suzuki`, `companies/sega-am2`, `techniques/sprite-scaling` |
| Powerdrome | games | The Amiga racer that inspired WipEout | `games/wipeout` |
| Powermonger | games | Bullfrog's 1990 follow-up to *Populous* | `games/populous`, `companies/bullfrog`, `genres/god-games`, `people/peter-molyneux`, `games/syndicate` |
| Prey (2017) | games | Arkane Austin's System Shock successor | `genres/immersive-sim`, `companies/arkane-studios` |
| Primal Rage | games | Atari Games fighting game converted by Probe to 17 formats | `companies/probe-software`, `companies/atari-games` |
| Primal Rage, Area 51, Klax and S.T.U.N. Runner | games | Atari Games' later coin-ops | `companies/atari-games` |
| Prince of Persia: The Sands of Time | games | Ubisoft's 2003 reboot | `games/prince-of-persia`, `people/jordan-mechner`, `companies/ubisoft` |
| Project-X | games | Team17's shooter and first number one | `companies/team17`, `people/andreas-tadic` |
| Pssst, Cookie and Tranz Am | games | Ultimate's other 16K Spectrum games | `games/jetpac`, `companies/ultimate` |
| Psychonauts | games | Schafer's first Double Fine game | `people/tim-schafer` |
| Psytron | games | Beyond's 1984 *CRASH* Smash | `companies/beyond-software` |
| Pulseman | games | Game Freak's best-regarded game before *Pokémon* (1994) | `companies/game-freak`, `people/satoshi-tajiri` |
| Pump It Up | games | Korean rival to DDR with a different pad layout | `hardware/dance-mat`, `games/dance-dance-revolution` |
| Putty Squad | games | System 3's game, finished in 1995 and released in 2013 | `people/john-twiddy`, `companies/system-3` |
| Quake II and Quake III Arena | games | The series' later direction and esports role | `games/quake`, `companies/id-software`, `communities/esports-origins`, `events/quakecon` |
| Quest for Glory and Lori and Corey Cole | games | Lori Cole's Sierra series, the Sierra side of the 1991 death debate | `companies/sierra`, `games/monkey-island`, `culture/adventure-game-deaths`, `techniques/sci-engine` |
| Quinty / Mendel Palace | games | Game Freak's first game (1989) | `people/satoshi-tajiri`, `companies/game-freak`, `people/ken-sugimori` |
| Race Drivin' | games | Atari Games' 1990 arcade sequel to *Hard Drivin'* | `games/hard-drivin`, `companies/atari-games` |
| Rag Doll Kung Fu | games | Mark Healey's early third-party Steam game, which led to Media Molecule | `tools/steam`, `companies/media-molecule`, `culture/indie-games` |
| Raid on Bungeling Bay | games | Will Wright's first game, set in the *Choplifter* world | `games/sim-city`, `people/will-wright`, `companies/broderbund`, `games/choplifter`, `games/lode-runner` |
| Railroad Tycoon | games | Meier's 1990 game and the direct forerunner of *Civilization* | `companies/microprose`, `people/sid-meier`, `games/civilization`, `genres/simulation-games`, `genres/tycoon-games`, `games/transport-tycoon` |
| Ranarama | games | Steve Turner's 1987 Hewson game, a CRASH Smash that did better in Spain than Britain | `people/dave-rogers`, `people/steve-turner`, `companies/hewson-consultants` |
| Rare Replay | games | The 2015 compilation where many readers now play *Jetpac* | `games/jetpac`, `companies/rare` |
| Reader Rabbit | games | The Learning Company's longest-running series | `companies/the-learning-company`, `companies/mecc`, `culture/educational-software` |
| Realms of the Haunting | games | A PC game the period press cited for first-person horror | `techniques/first-person-horror`, `genres/horror-games`, `companies/gremlin-graphics` |
| Rebelstar | games | Gollop's Spectrum game with action points and opportunity fire | `people/julian-gollop`, `games/laser-squad`, `companies/firebird`, `techniques/turn-based-combat`, `genres/wargame` |
| Red Baron | games | Atari's 1980 3D vector game from the rival team | `games/battlezone`, `techniques/vector-graphics` |
| Red Dead Redemption | games | Rockstar's western series | `companies/rockstar`, `companies/rockstar-north` |
| Red Faction | games | Volition's 2001 game, Poole's example of incoherent AI | `techniques/enemy-design` |
| Rescue on Fractalus! and Ballblazer | games | Lucasfilm's first games | `companies/lucasarts`, `systems/atari-8-bit` |
| Resident Evil 4 | games | The 2005 turn to action, and a big influence on third-person shooters | `games/resident-evil`, `genres/survival-horror`, `techniques/tank-controls`, `companies/capcom`, `people/shinji-mikami` |
| Return to Blacktooth | games | The 2026 sequel to *Head Over Heels* | `games/head-over-heels` |
| Rick Dangerous | games | Core Design's 1989 platformer, the "spiritual father" of Lara Croft and the game *Spelunky* is most often compared with | `games/spelunky`, `companies/core-design`, `games/tomb-raider`, `companies/firebird` |
| Riven | games | Myst's 1997 sequel, Red Orb's biggest release | `games/myst`, `companies/cyan`, `companies/broderbund`, `techniques/pre-rendered-backgrounds` |
| River Raid | games | Activision's 1982 game, the clearest period example of a generated level in a 4K ROM | `techniques/procedural-generation`, `techniques/random-numbers`, `systems/atari-2600` |
| Roc'n Rope | games | Konami's 1983 coin-op, where Fujiwara first tried the grappling hook | `people/tokuro-fujiwara`, `games/bionic-commando` |
| Rogue Legacy and Slay the Spire | games | The roguelite wave | `genres/roguelike`, `techniques/permadeath` |
| RollerCoaster Tycoon 2 | games | *RollerCoaster Tycoon*'s sequel | `people/chris-sawyer`, `games/roller-coaster-tycoon` |
| Saboteur! | games | Durell's well-known 1985 Spectrum game | `techniques/stealth-mechanics` |
| Sanxion, Armalyte and Creatures | games | Three of Thalamus's ZZAP! Gold Medal and Sizzler C64 games | `companies/thalamus` |
| SD-Snatcher and Metal Gear 2: Solid Snake | games | MSX landmarks and among the first fan translations | `communities/fan-translations`, `systems/msx`, `companies/konami` |
| Seiken Densetsu 3 (Trials of Mana) | games | The best-known cancelled localisation | `communities/fan-translations`, `games/secret-of-mana`, `companies/square` |
| Sensible World of Soccer | games | The 1994 successor to *Sensible Soccer* | `games/sensible-soccer`, `companies/sensible-software`, `people/jon-hare` |
| Seven Cities of Gold | games | Dan Bunten's early game with a generated world | `people/dan-bunten`, `companies/electronic-arts` |
| Shadow Warrior | games | 1997 Build game and a period argument about racial stereotypes | `companies/3d-realms` |
| Shadowrun (Super NES) | games | Beam's best-remembered console game | `companies/beam-software`, `companies/data-east` |
| Shattered Steel | games | BioWare's first game | `companies/bioware`, `companies/interplay` |
| Shenmue II | games | The Hong Kong sequel, also released on the Xbox | `games/shenmue`, `people/yu-suzuki`, `companies/sega-am2` |
| Shenmue III | games | The 2019 Kickstarter-funded sequel | `games/shenmue`, `people/yu-suzuki` |
| Sherlock | games | *The Hobbit*'s 1984 successor, with an extended Inglish | `companies/melbourne-house`, `games/the-hobbit`, `genres/text-adventure`, `companies/beam-software` |
| Sid Meier's Alpha Centauri | games | *Civilization*'s 1999 space follow-up | `games/civilization`, `genres/4x-strategy` |
| SimCity 2000 and SimEarth | games | *SimCity*'s direct successors | `games/sim-city`, `companies/maxis`, `people/will-wright` |
| SimEarth, SimAnt and SimCity 2000 | games | Maxis's core "software toys" | `people/will-wright`, `companies/maxis`, `games/sim-city` |
| Simon | games | Baer's best-selling electronic game for Milton Bradley, derived from Atari's Touch Me, which set the copy-the-sequence pattern | `genres/music-games`, `people/ralph-baer`, `companies/milton-bradley`, `techniques/rhythm-matching` |
| Ski Star 2000 | games | Pete Cooke's game, credited by *CRASH* with the first use of icons | `games/shadowfire`, `people/pete-cooke` |
| Slot Racers | games | Robinett's first game | `people/warren-robinett` |
| Smash TV and NARC | games | Jarvis and Turmell's 1990 twin-stick game, and John Tobias's first | `people/eugene-jarvis`, `people/john-tobias`, `games/robotron-2084` |
| Snatcher | games | Kojima's 1988 cyberpunk adventure, a well-known Mega-CD game in the West | `people/hideo-kojima`, `companies/konami`, `systems/msx` |
| Sniper Elite | games | Rebellion's longest-running series, from 2005, with more than 10 million sold by 2015 | `companies/rebellion` |
| Soccer Kid | games | Krisalis's best-reviewed original game | `companies/krisalis`, `people/matt-furniss` |
| Softaid | games | The 1985 industry charity compilation, given a special Golden Joystick | `events/golden-joystick-awards` |
| Softporn Adventure | games | The source of *Leisure Suit Larry*, and one of the first adult games | `companies/sierra`, `games/leisure-suit-larry`, `people/al-lowe` |
| Sokoban | games | The model single-rule puzzle game from 1982, released in the US by Spectrum HoloByte alongside *Tetris* | `techniques/puzzle-game-design`, `games/tetris` |
| Solomon's Key, Tecmo Bowl and Star Force | games | Widely ported Tecmo games | `companies/tecmo`, `companies/hudson-soft`, `companies/us-gold` |
| Solstice | games | Software Creations' NES descendant of *Knight Lore*, with Tim Follin's score | `techniques/filmation-engine`, `techniques/isometric-projection` |
| Sonic Adventure | games | The first full 3D Sonic, a Dreamcast launch-period game | `companies/sonic-team`, `systems/sega-dreamcast` |
| Sonic the Hedgehog 2 | games | Launched worldwide on 24 November 1992 | `games/sonic-the-hedgehog`, `companies/sega` |
| Space Channel 5: Part 2 | games | United Game Artists' last main release (2002), which *Edge* ranked above the original | `companies/united-game-artists`, `games/space-channel-5`, `people/tetsuya-mizuguchi` |
| Space Invaders Part II | games | Nishikado's 1979 sequel with colour and a signable high-score table | `games/space-invaders`, `people/tomohiro-nishikado` |
| Space Wars | games | Cinematronics' first vector coin-op | `techniques/vector-graphics`, `systems/vectrex` |
| Spacewar! | games | The 1962 PDP-1 game behind Computer Space and Asteroids, in period since the 1960s extension | `communities/esports-origins`, `companies/atari`, `people/nolan-bushnell`, `games/pong`, `games/asteroids`, `people/ed-logg`, `techniques/vector-graphics`, `techniques/game-loop`, `genres/shoot-em-up`, `genres/arcade-game` |
| Special Criminal Investigation (Chase H.Q. II) | games | The sequel, with period coverage and a notable C64 cartridge release | `games/chase-hq`, `companies/probe-software` |
| Speed Race | games | Nishikado's 1974 driving game with a vertically scrolling road | `people/tomohiro-nishikado`, `companies/taito`, `hardware/steering-wheel` |
| Speedball | games | The Bitmap Brothers' second game (1988), for Image Works | `companies/bitmap-brothers`, `games/speedball-2`, `games/xenon-2`, `companies/mirrorsoft` |
| Spindizzy | games | Paul Shirley's award-winning Electric Dreams original | `companies/electric-dreams`, `techniques/filmation-engine`, `games/marble-madness` |
| Splat! | games | Incentive's first game (1983) and its prize gimmick | `companies/incentive-software`, `people/ian-andrew` |
| Spore | games | Wright's last Maxis game | `genres/god-games`, `people/will-wright`, `companies/maxis` |
| Stack-Up | games | R.O.B.'s other game | `hardware/rob` |
| Star Castle | games | The arcade game behind *Yars' Revenge* | `people/howard-scott-warshaw` |
| Star Citizen and Cloud Imperium Games | games | The largest crowdfunded game, born of the Wing Commander line | `games/wing-commander`, `people/chris-roberts` |
| Star Fox 2 | games | The unreleased Super NES sequel that introduced All-Range Mode, released in 2017 | `games/star-fox`, `techniques/super-fx-chip`, `companies/argonaut`, `games/star-fox-64` |
| Star Soldier | games | Hudson's Caravan shooter series | `companies/hudson-soft`, `systems/pc-engine` |
| Star Wars (Atari arcade) | games | Atari's 1983 arcade game, which used the Bradley Trainer's controller | `techniques/vector-graphics`, `games/battlezone` |
| Star Wars Episode I: Battle for Naboo | games | Minor example in the difficulty entry | `techniques/difficulty-design` |
| Star Wars: Rogue Squadron | games | Factor 5's best-known game and an N64 technical landmark | `people/chris-huelsbeck`, `companies/factor-5`, `companies/lucasarts` |
| Starblade | games | Namco's 1991 polygon rail shooter, which influenced *Star Fox* | `genres/rail-shooters`, `games/star-fox`, `companies/namco` |
| StarCraft II | games | The sequel trilogy and its esports | `games/starcraft`, `companies/blizzard`, `genres/rts-genre` |
| Starflight | games | Open-world space game with the earliest code wheel found in print | `techniques/code-wheels`, `techniques/manual-protection` |
| Starglider 2 | games | The solid-3D sequel to *Starglider* | `companies/argonaut`, `games/starglider`, `companies/rainbird` |
| StarTropics | games | One of only two MMC6 games | `hardware/mmc5`, `hardware/apu` |
| Steel Battalion | games | Capcom's game with save-wiping permadeath on a console | `techniques/permadeath` |
| Stonkers | games | Imagine's 1983 Spectrum real-time wargame | `genres/rts-genre`, `companies/imagine-software`, `games/dune-ii` |
| Street Fighter III: 3rd Strike | games | The game the scene kept alive, and the setting of Moment 37 | `events/evo`, `communities/fighting-game-community`, `companies/capcom` |
| Streets of Rage 2 | games | The best-remembered game of the series, now covered only in passing | `games/streets-of-rage`, `genres/beat-em-up`, `hardware/ym2612` |
| Striker | games | Elite and Rage's Super NES football game | `companies/elite-systems` |
| Stryker's Run | games | A chart-topping BBC Micro game from Superior Software | `people/chris-roberts`, `companies/superior-software` |
| Stunt Car Racer | games | Geoff Crammond's 1989 home polygon racer, which reviewers compared with *Hard Drivin'* | `games/hard-drivin`, `people/geoff-crammond`, `genres/racing-simulation`, `genres/racing-game`, `companies/firebird`, `companies/microprose`, `techniques/procedural-generation` |
| Stunt Race FX | games | A game for the faster Super FX chip | `techniques/super-fx-chip`, `games/star-fox`, `companies/argonaut` |
| Sub-Terrania | games | Zyrinx's 1994 Mega Drive shooter | `groups/crionics`, `demos/hardwired`, `people/jesper-kyd` |
| Super Breakout | games | Ed Logg's 1978 sequel and a 5200 pack-in game | `people/ed-logg`, `games/breakout` |
| Super Cobra | games | Scramble's sequel, with Parker Brothers home versions | `games/scramble`, `companies/konami` |
| Super Cycle | games | Epyx's 1986 home-computer Hang-On substitute that topped charts | `games/hang-on`, `companies/epyx` |
| Super Dodge Ball and Nintendo World Cup | games | The other *Kunio-kun* games that reached the West | `companies/technos`, `games/river-city-ransom` |
| Super Hang-On | games | Suzuki's 1987 sequel, whose Spectrum version *Sinclair User* rated above *Out Run* | `games/out-run`, `people/yu-suzuki`, `games/hang-on`, `techniques/sprite-scaling`, `distribution/budget-games` |
| Super Mario All-Stars | games | The SNES compilation of SMB1–3 and The Lost Levels | `games/super-mario-bros`, `games/super-mario-bros-3` |
| Super Mario Bros.: The Lost Levels | games | The sequel judged too hard to export, later on *Super Mario All-Stars* | `techniques/difficulty-design`, `games/super-mario-bros` |
| Super Mario Kart | games | Split-screen mode 7 and the DSP-1, 1992 | `techniques/mode-7`, `techniques/sprite-scaling`, `games/mario-kart-64` |
| Super Mario RPG | games | A Super Nintendo cartridge with the SA-1 co-processor | `hardware/cartridge` |
| Super Mario World 2: Yoshi's Island | games | Used the Super FX for sprites | `techniques/super-fx-chip`, `systems/super-nintendo` |
| Super Smash Bros. | games | Sakurai's series, with a long competitive history, and where the *Duck Hunt* dog lives on | `people/satoru-iwata`, `people/masahiro-sakurai`, `companies/hal-laboratory`, `games/duck-hunt`, `events/evo`, `communities/fighting-game-community`, `games/kirby` |
| Super Smash Bros. Melee | games | A major Evo game from 2013, and the source of Evo's tension with Nintendo | `events/evo`, `communities/fighting-game-community` |
| Superfrog | games | Team17's platform game | `companies/team17`, `people/andreas-tadic`, `culture/amiga-power-versus-team17` |
| Superman (Atari 2600) | games | John Dunn's 1979 game, built from Robinett's prototype code | `games/adventure`, `people/warren-robinett` |
| SWAT 4 / Tribes: Vengeance | games | Irrational's mid-2000s games and their shared engine | `companies/irrational-games` |
| Sweet Home | games | Capcom's 1989 Famicom game, the direct ancestor of Resident Evil, never released outside Japan | `genres/survival-horror`, `games/resident-evil`, `people/tokuro-fujiwara`, `genres/horror-games`, `people/shinji-mikami` |
| Sweevo's World | games | Gargoyle's 1985 isometric game, named by *CRASH* as a forerunner of *Head Over Heels* | `companies/gargoyle-games`, `genres/arcade-adventure`, `games/head-over-heels` |
| Sword of Fargoal and Telengard | games | 8-bit dungeon games with random levels; their save rules still need checking | `genres/roguelike`, `techniques/permadeath` |
| Swordquest | games | *Adventure*'s intended sequel, with its comic books and prize competition | `games/adventure`, `people/warren-robinett` |
| Swords and Sorcery | games | PSS's delayed MIDAS role-playing game | `people/richard-cockayne`, `people/gary-mays`, `companies/pss` |
| Syndicate Wars | games | The 1996 sequel with its own period reviews | `games/syndicate`, `companies/bullfrog` |
| Tabula Rasa | games | Garriott's post-Origin game for NCsoft, 2007 | `people/richard-garriott`, `genres/mmorpg-history` |
| Tactics Ogre / Ogre Battle | games | *Edge*'s definitive SNES wargame, and the source of *Final Fantasy Tactics* | `genres/tactical-rpg`, `games/final-fantasy-tactics` |
| Tail Gunner | games | Cinematronics' 1979 3D vector game, which Rotberg names | `games/battlezone`, `techniques/vector-graphics` |
| Taito Legends | games | The 2005 compilation | `games/rainbow-islands`, `games/bubble-bobble`, `companies/taito` |
| Target Renegade | games | Ocean's British sequel to *Renegade*, by Mike Lamb and Dawn Drake | `games/renegade`, `people/mike-lamb`, `games/river-city-ransom` |
| Tau Ceti | games | Pete Cooke's CRL 3D game, which made Twiddy's name on the C64 | `people/pete-cooke`, `people/john-twiddy`, `companies/crl-group` |
| Team Fortress | games | The *Quake* mod Valve bought and brought to *Half-Life* | `communities/modding`, `communities/total-conversions`, `companies/valve`, `culture/modding-to-industry`, `games/quake`, `games/half-life`, `games/counter-strike` |
| Tehkan World Cup | games | The trackball football coin-op behind MicroProse Soccer and Sensible Soccer | `companies/tecmo`, `companies/sensible-software` |
| Temple of Apshai | games | Epyx's real-time dungeon games, American forerunners of the action RPG | `companies/epyx`, `genres/roguelike`, `genres/action-rpg`, `genres/western-rpg` |
| Tenchu: Stealth Assassins | games | A 1998 stealth game named in the stealth entry | `techniques/stealth-mechanics` |
| Tennis for Two | games | William Higinbotham's 1958 oscilloscope tennis game, often cited before Pong | `games/pong`, `genres/sports-games` |
| Tetris Effect | games | Enhance's *Tetris* game | `people/tetsuya-mizuguchi`, `games/tetris` |
| Thanatos | games | Durell's 1986 game, which hides a Roger Dean tribute | `people/roger-dean`, `companies/durell` |
| The 11th Hour | games | *The 7th Guest*'s sequel, with a well-documented troubled production | `games/7th-guest`, `techniques/fmv` |
| The Bard's Tale | games | Interplay's 1985 hit, sold by EA | `genres/western-rpg`, `companies/interplay`, `people/brian-fargo`, `companies/electronic-arts`, `games/wasteland` |
| The Beatles: Rock Band | games | Harmonix's Beatles band game | `games/rock-band`, `companies/harmonix` |
| The Black Cauldron | games | Sierra's first keyboard-free AGI game | `techniques/agi-engine` |
| The Black Onyx | games | An early Japanese computer RPG, a year before *Dragon Quest* | `people/henk-rogers`, `genres/jrpg`, `games/dragon-quest`, `people/roger-dean` |
| The Chronicles of Riddick: Escape from Butcher Bay | games | Starbreeze's best-known work | `companies/starbreeze`, `people/vogue`, `culture/licensed-games` |
| The Curse of Monkey Island | games | The coin interface and the last SCUMM game | `techniques/point-and-click`, `techniques/scumm`, `games/monkey-island` |
| The Elder Scrolls | games | The series (Arena, Daggerfall, Oblivion, Skyrim), of which only Morrowind has an entry | `companies/bethesda`, `companies/bethesda-game-studios`, `people/todd-howard`, `genres/western-rpg`, `communities/modding`, `games/morrowind` |
| The Evil Within | games | Mikami's return to survival horror | `people/shinji-mikami`, `genres/survival-horror` |
| The Eye of the Moon | games | The unfinished third Midnight game, promised for four years | `games/lords-of-midnight`, `games/doomdarks-revenge`, `companies/beyond-software`, `people/mike-singleton` |
| The Great Escape | games | Denton's 1986 game, a *CRASH* 96% and readers' second-best game of 1986 | `games/shadowfire`, `companies/denton-designs`, `companies/ocean-software`, `techniques/isometric-projection`, `people/mike-lamb` |
| The Hitchhiker's Guide to the Galaxy (game) | games | Infocom's biggest hit and its most famous feelies | `companies/infocom`, `genres/text-adventure` |
| The Last Express | games | Mechner's 1997 real-time Orient Express adventure | `techniques/rotoscoping`, `people/jordan-mechner`, `companies/broderbund` |
| The Legend of Kyrandia | games | Westwood's non-RTS work | `companies/westwood-studios`, `companies/virgin-games` |
| The Lion King (1994 game) | games | Virgin's 1994 Disney game, linked to Perry and Westwood | `companies/virgin-games`, `people/david-perry`, `people/louis-castle`, `companies/westwood-studios` |
| The Lord of the Rings and Shadows of Mordor | games | Melbourne House's Tolkien sequels, 1986–87 | `companies/melbourne-house`, `games/the-hobbit`, `companies/beam-software` |
| The Lost Vikings | games | Silicon & Synapse's best-known SNES game | `games/warcraft`, `companies/blizzard`, `companies/interplay` |
| The Lurking Horror | games | Infocom's horror adventure | `genres/horror-games`, `companies/infocom`, `people/dave-lebling` |
| The Making of Karateka | games | Digital Eclipse's 2023 interactive documentary | `games/karateka`, `people/jordan-mechner`, `culture/game-preservation` |
| The Manhole | games | Cyan's first CD-ROM title | `games/myst`, `companies/cyan` |
| The Mega-Tree | games | The unreleased Miner Willy game whose development disks *Retro Gamer* bought and documented | `magazines/retro-gamer`, `people/matthew-smith`, `games/jet-set-willy` |
| The Messenger | games | A 2018 game whose music was written in both FamiTracker and DefleMask | `tools/famitracker`, `tools/deflemask` |
| The Movies | games | Lionhead's film-studio sim | `companies/lionhead` |
| The New Zealand Story | games | Taito's 1988 arcade game, widely converted to home computers | `companies/taito` |
| The Outer Worlds | games | Obsidian's RPG, co-directed by Leonard Boyarsky | `companies/obsidian-entertainment`, `people/tim-cain` |
| The Pawn | games | Magnetic Scrolls' debut, on the QL and then the ST, and 1986 Golden Joystick winner | `companies/rainbird`, `companies/magnetic-scrolls`, `people/anita-sinclair`, `companies/telecomsoft` |
| The Portopia Serial Murder Case | games | Horii's 1983 adventure, which brought him and Nakamura together | `genres/jrpg`, `games/dragon-quest`, `people/yuji-horii`, `companies/enix` |
| The Revenge of Shinobi | games | Koshiro's first Mega Drive score, with his name on the title screen | `people/yuzo-koshiro`, `games/shinobi`, `games/streets-of-rage` |
| The Sacred Armour of Antiriad | games | Dan Malone's Palace game | `people/dan-malone`, `companies/palace-software` |
| The Temple of Elemental Evil | games | Troika's 2003 D&D game, reviewed in *CGW* 234 and *Hyper* 122 | `people/tim-cain`, `companies/troika-games`, `genres/western-rpg` |
| The Tower of Druaga | games | Masanobu Endo's 1984 game after *Xevious* | `people/masanobu-endo`, `games/xevious` |
| The Walking Dead (Telltale) | games | Telltale's 2012 game, which made episodic choice-driven adventures mainstream | `companies/telltale`, `distribution/episodic-gaming` |
| The Witcher and CD Projekt | games | Poland's best-known RPG series | `genres/western-rpg` |
| Theatre Europe | games | PSS's best-known game and the centre of the CND controversy | `genres/wargame`, `companies/pss`, `companies/mirrorsoft`, `people/gary-mays`, `people/richard-cockayne` |
| Theme Hospital | games | Bullfrog's 1997 follow-up to Theme Park and the ancestor of Two Point Hospital | `companies/bullfrog`, `people/peter-molyneux`, `games/theme-park`, `culture/guildford-games-cluster`, `games/dungeon-keeper` |
| Thimbleweed Park | games | Gilbert and Winnick's 2017 revival of the point-and-click adventure | `techniques/scumm`, `people/ron-gilbert`, `games/maniac-mansion`, `genres/graphic-adventure` |
| Thunderhawk and Chuck Rock | games | Core's best-known games before *Tomb Raider* | `companies/core-design` |
| Time Pilot | games | Okamoto's earlier aerial shooter at Konami (1982) | `games/1942`, `people/yoshiki-okamoto`, `companies/konami` |
| Time Zone | games | Sierra's 1982 1,300-room, $99.95 Apple II adventure | `people/roberta-williams`, `companies/sierra` |
| Times of Lore | games | Chris Roberts's C64 game with Galway's music, Origin's route into Britain | `people/martin-galway`, `people/chris-roberts`, `companies/origin-systems` |
| TimeSplitters | games | Free Radical's series and the direct heir to the *GoldenEye* and *Perfect Dark* design | `games/perfect-dark`, `games/goldeneye-007` |
| Tir Na Nog | games | Gargoyle's first Cuchulainn game (1984), 92% in *CRASH* | `games/dun-darach`, `companies/gargoyle-games`, `genres/arcade-adventure`, `people/greg-follis`, `people/roy-carter` |
| Tobal No. 1 and Dream Factory | games | Dream Factory's game, linked to Ishii | `games/tekken`, `games/virtua-fighter` |
| Toh Shin Den | games | The first PlayStation 3D fighter, and Edge's yardstick against Virtua Fighter | `techniques/motion-capture`, `games/tekken`, `games/virtua-fighter` |
| Tokimeki Memorial | games | Konami's dating-game hit, which Igarashi wrote | `people/koji-igarashi`, `companies/konami`, `systems/pc-engine` |
| Tomahawk | games | Digital Integration's helicopter simulator, Lenslok's well-run second title | `techniques/lenslock` |
| Tomba! / Whoopee Camp | games | Fujiwara's post-Capcom studio and its PlayStation platform game | `people/tokuro-fujiwara` |
| Top Gear | games | Gremlin and Kemco's 1992 SNES racer with a software road | `techniques/pseudo-3d-road`, `companies/gremlin-graphics`, `techniques/mode-7` |
| Top Gun (Ocean) | games | Ocean's 1986 game, linked to Mike Lamb | `people/mike-lamb` |
| Torment: Tides of Numenera | games | The crowdfunded successor to Planescape: Torment | `games/planescape-torment`, `phenomena/crpg-renaissance` |
| Total Eclipse | games | The third Freescape game (1988), set in an Egyptian pyramid | `techniques/freescape`, `companies/incentive-software`, `games/driller` |
| Touhou Project and dōjin soft | games | Self-published Japanese games and Comiket | `genres/shoot-em-up` |
| Trade Wars | games | The door game *CGW* singled out in 1993, still sold | `communities/bbs-door-games`, `communities/bbs-scene` |
| Treasure Island Dizzy and Fantasy World Dizzy | games | The best-selling *Dizzy* games | `games/dizzy`, `people/oliver-twins`, `companies/codemasters` |
| Trespasser | games | An early physically simulated character game (1998), and Seamus Blackley's work before the Xbox | `techniques/physics-engines`, `techniques/ragdoll-physics` |
| Tron (arcade) | games | Bally Midway's spinner-and-joystick cabinet, one of its biggest in-house hits | `hardware/spinner`, `companies/midway` |
| Turbo | games | Sega's 1981 behind-the-car racer, credited by *Electronic Games* with reviving racing games | `techniques/sprite-scaling`, `games/pole-position`, `techniques/pseudo-3d-road`, `genres/racing-game`, `games/out-run`, `hardware/steering-wheel` |
| Turbo Out Run | games | The 1989 sequel, converted by US Gold with Jeroen Tel's C64 music | `people/jeroen-tel`, `games/out-run` |
| Turok: Dinosaur Hunter | games | The 1997 game that saved Acclaim, and an early console FPS | `companies/acclaim`, `systems/nintendo-64` |
| Turrican II | games | The sequel, with its own reception and Hülsbeck's seven-voice music | `games/turrican`, `people/chris-huelsbeck`, `people/manfred-trenz` |
| UFO 50 | games | A 2024 collection built as an imaginary 1980s console library | `people/derek-yu`, `games/spelunky` |
| Ultima Online | games | Origin's 1997 online game, still running, now covered only inside other entries | `games/ultima`, `companies/origin-systems`, `genres/mmorpg-history`, `people/richard-garriott`, `companies/electronic-arts` |
| Ultima Underworld: The Stygian Abyss | games | Blue Sky/Looking Glass's 1992 first-person dungeon, named as the first immersive sim | `games/ultima`, `companies/origin-systems`, `companies/looking-glass`, `genres/western-rpg`, `genres/immersive-sim`, `games/deus-ex`, `people/warren-spector`, `games/system-shock` |
| Um Jammer Lammy | games | NanaOn-Sha's 1999 guitar follow-up to *PaRappa* | `games/parappa-the-rapper`, `companies/nanaon-sha`, `genres/music-games` |
| Undertale and Hyper Light Drifter | games | GameMaker's best-known games | `tools/game-maker`, `culture/indie-games` |
| Uniracers | games | DMA Design's Nintendo game, and its other ACM-rendered title | `companies/dma-design`, `systems/super-nintendo`, `people/dave-jones`, `games/donkey-kong-country`, `techniques/pre-rendered-backgrounds` |
| Unreal Tournament | games | Epic's 1999 multiplayer shooter | `companies/epic-games`, `games/unreal`, `tools/unreal-engine`, `people/tim-sweeney` |
| Unreal Tournament 2003 | games | The game the period press credited with the first ragdoll showcase | `techniques/ragdoll-physics`, `games/hitman`, `games/unreal`, `companies/epic-games` |
| Uridium 2 | games | The 1993 Amiga sequel, published by Renegade | `games/uridium`, `people/andrew-braybrook`, `companies/renegade` |
| Uru: Ages Beyond Myst | games | Cyan's online game and its open-sourced engine | `companies/cyan`, `culture/online-multiplayer` |
| Vanguard | games | SNK's first hit, 1980, and an early scrolling shooter | `companies/snk` |
| Vib-Ribbon | games | NanaOn-Sha's game that builds levels from any music CD | `companies/nanaon-sha`, `genres/music-games`, `games/parappa-the-rapper` |
| Virtua Cop 2 | games | Sega AM2's 1995 sequel on Model 2 | `games/virtua-cop`, `techniques/model-2` |
| Virtua Racing | games | AM2's first polygon racer, which Model 1 was built for, and Daytona's predecessor | `hardware/cartridge`, `hardware/arcade-hardware`, `people/yu-suzuki`, `companies/sega-am2`, `games/virtua-fighter`, `games/daytona-usa`, `techniques/model-2`, `genres/racing-game` |
| Vlambeer, Surgeon Simulator 2013 and Super Hexagon | games | Jam-born studios and games | `culture/game-jams` |
| Walker and Hired Guns | games | DMA's 1993 Amiga games | `companies/dma-design` |
| Wally games / Pyjamarama | games | Chris Hinsley's Mikro-Gen series, which launched Perry and Raffaele Cecco | `companies/mikro-gen`, `people/david-perry`, `people/raffaele-cecco` |
| Wanted: Monty Mole | games | The game that took Gremlin onto the national news | `companies/gremlin-graphics`, `culture/british-game-development` |
| Warcraft II: Tides of Darkness | games | Blizzard's 1995 sequel and C&C's main rival in 1995–96, now folded into the Warcraft entry | `games/warcraft`, `games/command-and-conquer`, `genres/rts-genre`, `techniques/fog-of-war` |
| Warlords | games | Four-player paddle game | `hardware/paddle-controller` |
| Wasteland 2 and Torment: Tides of Numenera | games | The flagship crowdfunded RPGs of the CRPG revival | `people/brian-fargo`, `phenomena/crpg-renaissance`, `games/planescape-torment`, `games/wasteland` |
| Wave Race 64 | games | One of the two Shindō re-releases with rumble | `techniques/rumble-pak`, `systems/nintendo-64`, `techniques/analog-control` |
| WEC Le Mans | games | Ocean's earlier racer, whose road engine O'Brien rewrote | `games/chase-hq`, `techniques/pseudo-3d-road` |
| Where in the World Is Carmen Sandiego? | games | Among the best-known educational games | `companies/broderbund`, `companies/the-learning-company`, `culture/educational-software` |
| Where Time Stood Still | games | A Denton Designs game | `companies/denton-designs` |
| Who Dares Wins | games | Alligata's game, the best-documented British licence dispute of 1985 | `games/commando`, `companies/elite-systems`, `companies/alligata` |
| Williams pinball of the late 1980s (Black Knight 2000) | games | Shows what a pinball programmer like Boon did | `people/ed-boon`, `companies/williams-electronics` |
| Wing Commander: Privateer | games | The Elite-style branch of the series | `games/wing-commander`, `games/elite` |
| Winning Run | games | Namco's 1989 polygon racer, shown alongside *Hard Drivin'* | `games/hard-drivin`, `techniques/pseudo-3d-road`, `companies/namco` |
| Wizard's Crown | games | SSI's 1985 Western RPG built around tactical combat | `genres/tactical-rpg`, `techniques/turn-based-combat` |
| Wizkid | games | The 1992 sequel to *Wizball* | `games/wizball`, `companies/sensible-software` |
| Wolfenstein 3D | games | The game that set id's shooter formula and its shareware success | `companies/id-software`, `games/doom`, `companies/apogee-software`, `genres/fps`, `tools/id-tech`, `people/john-carmack`, `people/john-romero`, `distribution/shareware`, `people/scott-miller`, `companies/3d-realms`, `companies/softdisk` |
| World Class Track Meet (Stadium Events) | games | The Power Pad's pack-in, and Bandai's original | `hardware/power-pad` |
| World Games | games | Epyx's 1986 Games-series title | `games/summer-games`, `games/winter-games`, `games/california-games`, `companies/epyx` |
| World of Warcraft | games | Blizzard's online game, whose links currently go to the Warcraft entry | `companies/blizzard`, `companies/activision`, `genres/mmorpg-history`, `games/warcraft` |
| Worm in Paradise | games | Level 9's game that ended *Heavy on the Magick*'s run at the top of the adventure chart | `games/heavy-on-the-magick` |
| Worms Armageddon and Worms: The Director's Cut | games | The Amiga finale and the PC version still played | `games/worms`, `people/andy-davidson`, `companies/team17` |
| WWF WrestleFest | games | American Technos's best-selling arcade game | `companies/technos` |
| X-Wing and Dark Forces | games | LucasArts' 1990s Star Wars line | `companies/lucasarts` |
| Xenon | games | The Bitmap Brothers' first game (1988), also an Arcadia coin-op | `companies/bitmap-brothers`, `games/speedball-2`, `games/xenon-2`, `companies/mirrorsoft` |
| Xybots | games | The Gauntlet III that became a first-person maze game | `people/ed-logg`, `games/gauntlet` |
| Yie Ar Kung-Fu | games | Konami's 1985 one-on-one fighter, one of the games *Street Fighter* was measured against | `genres/beat-em-up`, `companies/imagine-software`, `companies/konami`, `games/street-fighter`, `games/street-fighter-ii`, `games/international-karate`, `games/kung-fu-master` |
| Ys | games | Falcom's 1987 action RPG, with Yuzo Koshiro's score | `genres/action-rpg`, `companies/falcom`, `people/yuzo-koshiro` |
| Z and Z: Steel Soldiers | games | The Bitmap Brothers' PC strategy games (1996, 2001) | `companies/bitmap-brothers` |
| Zak McKracken and the Alien Mindbenders | games | The second SCUMM game, designed by David Fox | `techniques/scumm`, `companies/lucasarts`, `games/maniac-mansion` |
| Zanac | games | Compile's game with early self-adjusting difficulty | `techniques/difficulty-design`, `companies/compile` |
| Zoo Tycoon | games | The biggest tycoon series after *RollerCoaster Tycoon* | `genres/tycoon-games`, `companies/frontier-developments` |

## Culture, events and tools

| Candidate | Category | Why | Link from |
|---|---|---|---|
| *Commercial Breaks*: Imagine | culture | The 1984 BBC documentary behind most retellings of Imagine's collapse | `companies/imagine-software`, `culture/liverpool-games-scene` |
| GEOS | tools | The C64's graphical desktop | `systems/commodore-64` |
| *Babylon 5* | culture | The TV series whose space scenes Foundation Imaging rendered on networked Amiga 2000s with the Video Toaster and LightWave | `tools/lightwave-3d`, `hardware/video-toaster` |
| *seaQuest DSV* | culture | Amblin Imaging rendered its effects on a network of more than 60 Amigas, with no miniature models | `tools/lightwave-3d`, `hardware/video-toaster` |
| *Quantum Leap* | culture | Its "evil leaper" morphs were made with ASDG's MorphPlus on the Amiga, not the Toaster, as is often claimed | `tools/lightwave-3d` |
| *Star Trek: Voyager* | culture | *Amiga Shopper* reported Amblin Imaging, the *seaQuest* effects house, working on it by September 1994 | `tools/lightwave-3d` |
| The Final Cartridge | tools | The Dutch C64 utility and fast-loader cartridge, sold across Europe | `systems/commodore-64`, `techniques/disk-fastloaders`, `techniques/fast-loader`, `hardware/cartridge`, `hardware/action-replay` |
| Family BASIC | tools | Nintendo's BASIC for the Famicom | `systems/nintendo-entertainment-system`, `companies/hudson-soft` |
| AmigaOS, Kickstart and Workbench | tools | The Amiga's operating system | `systems/commodore-amiga` |
| CSpect | tools | A ZX Spectrum Next emulator | `systems/zx-spectrum-next`, `people/mike-dailly` |
| Amiga Hardware Reference Manual | tools | The primary source for Amiga chipset entries | `hardware/blitter`, `systems/commodore-amiga` |
| Mapping the Commodore 64 | tools | The register reference the VIC-II entry follows | `hardware/vic-ii`, `hardware/sid-chip`, `hardware/6510`, `hardware/cia`, `techniques/screen-memory`, `systems/commodore-64`, `techniques/basic-v2`, `techniques/kernal-io`, `techniques/disk-fastloaders` |
| Christian Bauer's VIC-II article | tools | The standard technical description of the VIC-II | `hardware/vic-ii`, `techniques/stable-raster`, `techniques/fld`, `techniques/vsp`, `techniques/fli`, `techniques/linecrunch`, `techniques/fpp`, `techniques/sprite-stretching`, `magazines/c-hacking` |
| Badlines | techniques | The VIC-II's stolen cycles | `hardware/vic-ii`, `systems/commodore-64` |
| Sample playback through the SID volume register | techniques | How C64 games played speech and drums | `hardware/sid-chip`, `people/martin-galway`, `people/chris-huelsbeck` |
| Sprite 0 hit and nametable mirroring | techniques | Two NES PPU techniques the PPU entry introduces | `hardware/ppu` |
| Bitplanes | techniques | The Amiga's planar display, behind every blit | `hardware/blitter`, `systems/commodore-amiga` |
| OS-9 | tools | Microware's 6809 operating system | `hardware/6809`, `systems/tandy-coco`, `systems/dragon-64` |
| CyberSound and AHI | tools | The 14-bit Paula playback method and the Amiga audio system that used it | `hardware/paula` |
| Amiga disk format (MFM) | techniques | How the Amiga stores tracks, decoded in software | `hardware/paula` |
| Copper bars | techniques | The copper's best-known effect | `hardware/copper` |
| Dual playfield | techniques | Denise's two independent playfields | `hardware/denise`, `techniques/parallax-scrolling`, `hardware/copper`, `hardware/amiga-chipset`, `games/shadow-of-the-beast` |
| Undocumented 6502 opcodes | techniques | The instructions the 6510 executes but MOS never listed | `hardware/6510`, `hardware/6502` |
| Fun School | tools | Europress's best-known educational series, and the reason Hasbro bought it | `companies/europress` |
| Mini Office | tools | Database's best-selling 8-bit business suite | `companies/europress` |
| Shoot-'Em-Up Construction Kit | tools | The game creator reviewers compared STOS and Klik & Play with | `tools/stos`, `tools/amos`, `companies/clickteam`, `tools/game-maker`, `tools/3d-construction-kit`, `companies/sensible-software`, `companies/palace-software`, `genres/shoot-em-up`, `communities/modding`, `techniques/hardware-scroll`, `techniques/scrolling`, `techniques/multidirectional-scrolling`, `techniques/tile-maps` |
| AOZ Studio | tools | Lionet's successor to AMOS | `people/francois-lionet`, `tools/amos` |
| OctaMED | tools | The Amiga tracker most British hobbyists met | `techniques/arpeggio`, `tools/protracker`, `hardware/paula`, `tools/soundtracker`, `techniques/mod-format`, `culture/tracker-music` |
| BBC BASIC | tools | The BBC Micro's BASIC, with named procedures and an inline assembler | `systems/bbc-micro`, `systems/acorn-archimedes`, `culture/basic-to-machine-code` |
| Psychedelia and the light synthesiser | tools | Minter's non-game programs | `people/jeff-minter`, `companies/llamasoft` |
| JiffyDOS | tools | The longest-lived C64 speed-up ROM | `techniques/disk-fastloaders`, `techniques/fast-loader`, `hardware/1541-disk-drive`, `hardware/action-replay` |
| Epyx Fast Load | tools | The best-known US fast-load cartridge | `techniques/disk-fastloaders`, `techniques/fast-loader` |
| Dolphin DOS | tools | The best-known parallel-cable speed-up for the 1541 | `techniques/disk-fastloaders`, `hardware/1541-disk-drive` |
| Krill's loader, Spindle and Bitfire | tools | Today's demoscene disk loaders | `techniques/disk-fastloaders`, `techniques/fast-loader`, `demos/comaland` |
| GCR (group code recording) | techniques | How the 1541 encodes its disks, and what copy protection played with | `techniques/disk-fastloaders`, `hardware/1541-disk-drive`, `techniques/disk-protection`, `hardware/paula` |
| HDMA | techniques | The per-scanline trick behind Mode 7 perspective | `systems/super-nintendo`, `techniques/mode-7`, `techniques/raster-effects` |
| Radio teletype (RTTY) | techniques | A common early-1980s amateur-radio project on home computers | `magazines/club-commodore`, `systems/commodore-vic-20` |
| Nintendo licensing and the 1991 FTC price case | phenomena | How Nintendo's control of retail prices drew a 1991 US government settlement | `phenomena/nintendo-seal`, `people/john-kirby` |
| Speedlock | techniques | The Spectrum's best-known protected loader | `techniques/fast-loader`, `techniques/copy-protection`, `techniques/cassette-loading`, `distribution/piracy` |
| Novaload | techniques | The C64's most-named tape loader of 1984–86 | `techniques/fast-loader`, `companies/novagen`, `techniques/cassette-loading` |
| *Inside Commodore DOS* | books | The standard 1541 reference | `hardware/1541-disk-drive`, `techniques/disk-fastloaders`, `techniques/disk-protection` |
| IFF (Interchange File Format) | techniques | EA's 1985 file standard behind Amiga pictures and sounds | `companies/electronic-arts`, `tools/deluxe-paint`, `systems/commodore-amiga`, `techniques/mod-format` |
| Compunet | communities | The Commodore online service where early C64 demos circulated | `communities/cracking-scene`, `communities/demo-scene`, `communities/crack-intros`, `groups/triad`, `people/tony-crowther`, `communities/bbs-scene`, `communities/chiptune-scene` |
| Copy parties | events | The swap meets where crackers traded games, from Venlo in 1988 to Gothenburg's TCC in 1993 | `communities/cracking-scene`, `magazines/illegal`, `groups/triad`, `communities/crack-intros`, `communities/demo-parties`, `groups/ikari` |
| Copyright (Computer Software) Amendment Act 1985 | phenomena | The British law FAST lobbied for | `communities/cracking-scene`, `distribution/piracy` |
| *The Dark Wheel* | books | Robert Holdstock's novella that came with *Elite* | `games/elite`, `companies/acornsoft` |
| Photon Paint and Digi-Paint | tools | The HAM paint programs *Deluxe Paint IV* replaced | `tools/deluxe-paint` |
| *Game Over* | books | David Sheff's 1993 history of Nintendo, cited across the Vault | `people/toru-iwatani`, `games/pac-man`, `companies/nintendo`, `people/minoru-arakawa`, `people/hiroshi-yamauchi`, `culture/universal-vs-nintendo`, `systems/nintendo-entertainment-system`, `phenomena/tetris-legal-battles`, `people/henk-rogers`, `people/alexey-pajitnov`, `people/howard-lincoln` |
| 3DMark | tools | The benchmark series, 1998 to the present | `companies/futuremark`, `companies/remedy-entertainment` |
| 40 Best Machine Code Routines for the ZX Spectrum | books | Hardman and Hewson's 1982 book, the source of the standard Spectrum scroll routines | `techniques/scrolling`, `techniques/software-scroll`, `people/andrew-hewson`, `companies/hewson-consultants`, `culture/basic-to-machine-code` |
| 8bitpeoples and the Blip Festival | events | Chip-music label and festival | `communities/chiptune-scene` |
| Adaptive tile refresh and ray casting | techniques | Explained in prose in several entries, with no technique entry | `people/john-carmack`, `tools/id-tech`, `techniques/hardware-scroll` |
| Alias PowerAnimator | tools | The 3D package used for DKC, Killer Instinct and films | `games/donkey-kong-country`, `techniques/pre-rendered-backgrounds` |
| AmiEXPO | events | The Amiga trade show where Silver and LightWave were first shown | `tools/imagine`, `tools/lightwave-3d` |
| Amiga Forever | tools | Cloanto's licensed Kickstart and Workbench package, the legal route to Amiga ROMs | `emulators/winuae`, `emulators/fs-uae`, `emulators/emulation`, `companies/cloanto`, `people/toni-wilen` |
| Anarchy | groups | British Amiga demo group that co-hosted The Party | `groups/the-silents`, `demos/hardwired`, `events/the-party`, `communities/demo-parties`, `groups/scoopex`, `demos/mental-hangover`, `groups/skid-row`, `communities/crack-intros` |
| Applesoft BASIC | tools | The Apple II's Microsoft BASIC | `systems/apple-ii`, `companies/microsoft` |
| Arcade Awards | events | The first recurring games awards in the US press | `magazines/electronic-games`, `games/pitfall` |
| AROS | tools | The open-source AmigaOS reimplementation whose Kickstart replacement ships with UAE emulators | `emulators/winuae`, `emulators/fs-uae` |
| Artifact colours | techniques | Colour from composite artefacts on the CoCo, Apple II, Atari and CGA | `hardware/mc6847`, `systems/tandy-coco` |
| Asm-One | tools | The standard Amiga demo-coding assembler, with its Trash'm-One derivative | `groups/kefrens`, `groups/crionics` |
| Atari: Game Over (2014 documentary) | culture | The documentary of the Alamogordo dig | `games/et-the-extra-terrestrial`, `phenomena/1983-crash`, `people/howard-scott-warshaw` |
| Back in Time Live and Chris Abbott | events | The C64 remix CDs and concerts where Daglish performed | `people/ben-daglish`, `people/rob-hubbard` |
| BASIC compilers for the Spectrum (Mcoder, Softek FP/IS) | tools | The route from Sinclair BASIC to compiled code | `culture/basic-to-machine-code`, `tools/sinclair-basic` |
| Battle.net | distribution | Blizzard's free built-in online service | `companies/blizzard`, `games/diablo`, `games/starcraft`, `games/warcraft`, `communities/esports-origins`, `culture/online-multiplayer` |
| BizHawk | emulators | The multi-system emulator TASVideos calls more accurate than FCEUX | `culture/tool-assisted-speedrun`, `emulators/fceux` |
| Blitz3D and BlitzMax | tools | The PC successors to Blitz Basic, with their source released | `tools/blitz-basic-2`, `people/mark-sibly` |
| Blue Sky Rangers | groups | Mattel's anonymous Intellivision programmers, later keepers of its rights | `systems/intellivision` |
| Bonanza (MDT, 1988) | demos | The first VSP and linecrunch picture mover, and a 7-sprite side-border scroller | `techniques/linecrunch`, `techniques/vsp`, `techniques/agsp` |
| Breakpoint | events | German Easter party (2003–2010) between Mekka & Symposium and Revision | `groups/fairlight`, `communities/demo-parties`, `groups/andromeda`, `groups/farbrausch`, `events/revision-party`, `demos/debris`, `demos/elevated`, `events/the-gathering`, `groups/rgba`, `people/iq`, `people/ryg`, `events/mekka-symposium`, `groups/the-black-lotus`, `demos/ocean-machine`, `groups/oxyron`, `groups/crest`, `demos/starstruck` |
| BRender | tools | Argonaut's 3D library, open-sourced in 2022 | `companies/argonaut`, `techniques/renderware` |
| Brutal Deluxe | groups | French Apple IIGS group that made *LemminGS* | `games/lemmings` |
| bsnes and higan | emulators | byuu's accuracy-first SNES emulator, the main example in Cycle Accuracy | `techniques/cycle-accuracy`, `people/byuu`, `emulators/emulation`, `emulators/retroarch`, `systems/super-nintendo` |
| Build engine and Ken Silverman | tools | Ken Silverman's engine behind *Duke Nukem 3D*, *Shadow Warrior* and *Blood* | `companies/apogee-software`, `companies/3d-realms`, `games/duke-nukem-3d` |
| ByteBoozer | tools | HCL's widely used C64 cruncher | `groups/booze-design`, `techniques/compression`, `techniques/run-length-encoding`, `techniques/size-coding` |
| Bytecode interpreters in games | techniques | The shared approach of Another World, SCUMM and Infocom's Z-machine | `games/another-world`, `techniques/scumm` |
| Byterapers | groups | Long-running Finnish group, co-makers of *Superselection* with Future Crew | `events/assembly-party`, `groups/future-crew` |
| C64 packers and crunchers (Card Cruncher) | tools | A staple of the cracking scene | `groups/1001-crew`, `techniques/compression`, `communities/cracking-scene` |
| Camelot | groups | Danish C64 group, winner at The Party 1993 with *Tower Power* | `events/the-party`, `groups/oxyron` |
| Candytron | demos | farbrausch's fr-030, the first kkrunchy intro, Breakpoint 2003 | `groups/farbrausch`, `people/ryg` |
| Chunky-to-planar conversion | techniques | The method behind AGA 3D demos such as *Mindprobe* | `groups/the-black-lotus`, `systems/commodore-amiga`, `demos/ocean-machine` |
| Classic Gaming Expo UK | events | Where *Retro Gamer* met its readers in 2004 and 2005 | `magazines/retro-gamer` |
| CNCD and Closer | demos | The Party V winner (1995) | `events/the-party`, `communities/demo-parties`, `communities/demo-scene` |
| Cocktail | demos | Triad's 1989 demo, listed first for sprite stretching | `techniques/sprite-stretching`, `groups/triad` |
| Codebase64 | communities | The C64 coding wiki cited as a secondary source across the C64 technique entries | `techniques/interrupt-driven-music`, `techniques/raster-interrupts`, `techniques/hard-restart`, `techniques/collision-detection`, `techniques/fld`, `techniques/vsp`, `techniques/linecrunch`, `techniques/agsp`, `techniques/sprite-stretching`, `techniques/sprite-crunching`, `techniques/tile-maps`, `techniques/multidirectional-scrolling` |
| COMPET-N | communities | The Doom demo leaderboard from 1994 | `communities/speedrunning`, `games/doom` |
| Complex | groups | Finnish groups that founded Assembly with Future Crew | `groups/andromeda`, `events/the-party`, `demos/desert-dream`, `communities/demo-parties`, `events/assembly-party`, `groups/spaceballs`, `demos/nine-fingers`, `demos/arte`, `groups/sanity`, `demos/nexus-7`, `groups/scoopex` |
| Computer Spacegames | books | The best-known Usborne type-in collection | `books/usborne-computing-books`, `distribution/type-in-listings`, `books/computer-battlegames` |
| Console Wars (Blake J. Harris) | books | A popular but reconstructed account of the Sega–Nintendo rivalry | `phenomena/console-wars` |
| Contended memory | techniques | Covered now only inside the ULA entry | `techniques/software-scroll`, `techniques/double-buffering`, `techniques/screen-memory` |
| Cornerstone | tools | Infocom's database, whose failure warns against diversification | `companies/infocom`, `companies/activision` |
| CP/M User Group | groups | One of the first public-domain libraries for microcomputers | `distribution/public-domain`, `culture/user-groups` |
| Crinkler | tools | The compressing linker used by most PC 4K intros | `demos/elevated`, `techniques/size-coding`, `techniques/compression`, `people/iq` |
| CRL 3D Game Maker | tools | CRL's *Knight Lore*-style construction kit | `techniques/filmation-engine`, `techniques/isometric-projection` |
| Crowdfunding (Kickstarter) | phenomena | Double Fine Adventure, Wasteland 2 and Shadowrun Returns | `culture/indie-games`, `people/tim-schafer`, `phenomena/crpg-renaissance` |
| Crowdfunding revivals | phenomena | Period developers returning through Kickstarter in 2012–13: *Elite Dangerous*, *Broken Sword 5*, the failed *Dizzy Returns*, and the CRPG revival | `games/elite-dangerous`, `companies/frontier-developments`, `phenomena/crpg-renaissance`, `genres/western-rpg`, `companies/obsidian-entertainment` |
| Cryonics | groups | Swedish group that won DreamHack's demo and 64K intro competitions | `events/dreamhack` |
| Crystal | groups | Amiga cracking group, Skid Row's main rival and Melon Dezign's parent | `groups/melon-dezign`, `groups/quartex`, `groups/skid-row`, `groups/fairlight` |
| CSDb | tools | The C64 scene database behind most C64 entries' credits, dates and placings | `groups/oxyron`, `groups/crest`, `groups/1001-crew`, `demos/coma-light-13`, `techniques/fli`, `techniques/open-borders`, `events/x-party`, `demos/wonderland`, `demos/deus-ex-machina`, `groups/censor-design`, `groups/booze-design`, `tools/sid-wizard`, `communities/demo-scene`, `tools/hvsc`, `techniques/fld`, `techniques/vsp`, `techniques/linecrunch`, `techniques/agsp`, `techniques/sprite-stretching`, `techniques/sprite-crunching` |
| curses | tools | The screen library that made *Rogue* possible | `games/rogue`, `genres/roguelike` |
| Cyberathlete Professional League and Red Annihilation | events | Early US Quake competitions; the CPL was founded in 1997 | `events/quakecon`, `communities/esports-origins`, `games/quake`, `games/counter-strike` |
| Cyberzone, Knightmare and Broadsword | culture | TV productions that used Dimension's 3D | `companies/incentive-software`, `people/ian-andrew` |
| DAAD and Aventuras AD | tools | Gilberts's multi-machine adventure system and the Spanish house that used it | `people/tim-gilberts`, `companies/gilsoft`, `genres/text-adventure`, `tools/paw` |
| Dark Engine | tools | The engine shared by Thief and System Shock 2 | `games/thief`, `games/system-shock-2`, `companies/looking-glass` |
| Data East USA v. Epyx | phenomena | The *Karate Champ* case, told in three entries | `companies/epyx`, `companies/data-east`, `games/international-karate` |
| De Re Atari | books | Atari's own 1982 programming guide to the 8-bit hardware | `techniques/hardware-scroll`, `systems/atari-8-bit`, `people/chris-crawford`, `techniques/collision-detection` |
| DeBabelizer | tools | A widely used 1990s image-conversion tool for game and multimedia art | `people/dave-theurer` |
| Dexion X-Mas Conference 1990 | events | An early Danish Christmas party, before The Party | `groups/phenomena`, `communities/demo-parties` |
| Digital Symposium | events | British Amiga party, Rotherham 1992 | `demos/jesus-on-es`, `communities/demo-parties` |
| DirectX | tools | Microsoft's games API | `companies/microsoft`, `systems/microsoft-xbox` |
| Distant Worlds | events | The touring Final Fantasy concert series since 2007 | `people/nobuo-uematsu`, `games/final-fantasy` |
| Doom source ports | tools | Boom, ZDoom, GZDoom, Chocolate Doom and others | `games/doom`, `communities/modding`, `tools/id-tech` |
| DOSBox | emulators | The DOS emulator behind the Archive's DOS collection | `communities/internet-archive`, `emulators/emulation` |
| Doubled text lines (d011 stretchers) | techniques | The repeated character-line trick that linecrunch's timing sits next to | `techniques/linecrunch`, `techniques/fpp`, `techniques/sprite-stretching` |
| Dreamdealers | groups | French demo group from which Ra and Moby came | `groups/sanity`, `demos/arte` |
| DWANGO / Kali | tools | 1990s dial-up and IPX-over-internet services | `culture/online-multiplayer`, `games/doom` |
| Dynamic recompilation and high-level emulation | techniques | Emulation techniques the existing entries only name | `techniques/emulators`, `emulators/emulation` |
| E3 (Electronic Entertainment Expo) | events | The trade show GDC is compared with | `culture/gdc` |
| Early Swedish demo parties | events | The 1988–91 party circuit (Arvika, Eskilstuna, Arboga, Motala) where Phenomena won | `groups/phenomena`, `demos/enigma`, `communities/demo-parties` |
| Easter eggs | culture | The hidden-credit tradition from *Starship 1*, *Video Whizball* and *Adventure* to Atari's 1982 change of policy and the magazines' egg hunts | `people/warren-robinett`, `games/adventure`, `people/howard-scott-warshaw`, `culture/cheat-codes` |
| ECTS | events | The London trade show where *Worms* was signed | `games/worms`, `people/andy-davidson` |
| Encarta | tools | The CD-ROM encyclopaedia | `culture/educational-software`, `hardware/cd-rom` |
| Euskal Encounter and BCN Party | events | Spanish parties where rgba won most of its early prizes | `groups/rgba` |
| Evoke | events | Long-running German demo party from 1997 | `communities/demo-parties` |
| Exergaming | culture | DDR in schools, Konami's *Aerobics Revolution*, the Power Pad and later Wii Fit | `games/dance-dance-revolution`, `hardware/dance-mat`, `hardware/power-pad` |
| eXoDOS | tools | The DOS game collection behind the Archive's DOS library | `communities/internet-archive`, `emulators/emulation` |
| Exomizer and Pucrunch | tools | The C64 cross-crunchers | `techniques/compression`, `magazines/c-hacking` |
| FamiStudio | tools | The most-used modern alternative to FamiTracker | `tools/famitracker`, `hardware/apu`, `communities/nesdev` |
| FastTracker 2 | tools | One of the main PC trackers and the origin of the XM format | `groups/triton`, `culture/tracker-music`, `tools/protracker`, `tools/famitracker`, `people/vogue`, `demos/crystal-dream`, `techniques/mod-format` |
| FidoNet | communities | The network that linked tens of thousands of boards | `communities/bbs-scene`, `techniques/ascii-art` |
| Field-programmable gate array | techniques | The hardware shared by the MiSTer and ZX Spectrum Next | `hardware/mister-fpga`, `systems/zx-spectrum-next` |
| Fighting Fantasy | books | The British gamebook series whose name *Final Fantasy* had to avoid | `games/final-fantasy` |
| Fighting games | genres | One-on-one fighters, separate from scrolling beat 'em ups | `companies/data-east`, `games/international-karate`, `games/way-of-the-exploding-fist`, `games/street-fighter`, `games/street-fighter-ii`, `genres/beat-em-up`, `games/mortal-kombat` |
| Filled-polygon graphics | techniques | The technique behind Another World, Cruise for a Corpse and Alone in the Dark's characters | `games/another-world`, `techniques/vector-graphics` |
| Final Fantasy: The Spirits Within | culture | The 2001 film that hurt Square's finances | `companies/square`, `people/hironobu-sakaguchi` |
| Flash Cracking Group | groups | Credited with the first opened top and bottom borders | `techniques/open-borders`, `groups/1001-crew` |
| Focus Design | groups | Three-time winner of Datastorm's Amiga 1200 demo competition | `events/datastorm` |
| FPD (flexible pixel distance) | techniques | The order-preserving middle step between FLD/linecrunch and FPP | `techniques/fpp`, `techniques/linecrunch`, `techniques/fld` |
| fr-025: the popular demo | demos | The Breakpoint 2003 PC demo winner | `groups/farbrausch` |
| Fred Fish collection | distribution | The Amiga public-domain disk series that carried *NetHack*, *Hack* and much else | `games/nethack`, `distribution/public-domain`, `communities/aminet` |
| Fred Fish disks | distribution | The main Amiga public-domain series before Aminet, which spread the Juggler | `communities/aminet`, `distribution/public-domain`, `people/eric-graham`, `culture/the-juggler`, `people/nicola-salmoria`, `distribution/shareware` |
| Gaikai / cloud gaming | phenomena | Streaming older games, the basis of PlayStation Now | `people/david-perry`, `companies/sony` |
| Gallup software charts | culture | Who compiled the UK software sales charts, and how | `culture/reading-the-charts`, `companies/renegade`, `phenomena/record-companies-in-software` |
| Game Center CX | culture | The Japanese TV programme behind several developer interviews | `people/satoshi-tajiri`, `companies/game-freak` |
| Game decompilation projects | communities | The SM64 reconstruction and its successors | `games/super-mario-64` |
| GameLine | distribution | Control Video Corporation's 2600 games by phone, and a line to AOL | `distribution/digital-distribution`, `systems/atari-2600` |
| Games Designer | tools | A 1983 game-creation kit that preceded *HURG* | `companies/quicksilva`, `tools/3d-construction-kit` |
| Garry Kitchen's GameMaker | tools | Activision's 1985 C64 game-creation kit with the same name | `tools/game-maker` |
| GEMS | tools | Sega of America's Mega Drive sound driver | `techniques/sound-drivers`, `hardware/ym2612`, `systems/sega-mega-drive` |
| Giełda (Polish computer markets) | culture | How software and hardware moved in 1980s Poland | `magazines/bajtek`, `systems/famiclone`, `culture/the-c64-across-borders` |
| Glacier (engine) | tools | IO's in-house engine, 2000 to the present | `games/hitman`, `companies/io-interactive`, `techniques/physics-engines` |
| GoatTracker | tools | The PC-based C64 tracker SID-Wizard borrowed from and imports | `tools/sid-wizard`, `hardware/sid-chip`, `communities/chiptune-scene`, `techniques/interrupt-driven-music`, `techniques/sound-drivers`, `techniques/pulse-width-modulation`, `culture/tracker-music` |
| GOG.com | distribution | The download store mentioned in several entries | `distribution/digital-distribution`, `distribution/abandonware` |
| GoldSrc and WorldCraft (Hammer) | tools | Valve's engine and editor, central to the mod scene | `games/half-life`, `games/counter-strike`, `tools/id-tech` |
| GrimE / Lua in games | techniques | LucasArts' engine after SCUMM, and one of the first uses of Lua in a game | `games/grim-fandango`, `techniques/scumm` |
| Haujobb | groups | German group, repeated winner at Mekka & Symposium and The Party 2000 | `groups/scoopex`, `events/the-party`, `events/mekka-symposium`, `events/assembly-party` |
| HiSoft BASIC | tools | Named by period reviewers as a main rival to GFA, AMOS and Blitz | `tools/gfa-basic`, `tools/blitz-basic-2`, `tools/amos` |
| HiSoft Devpac | tools | The standard Spectrum and Amstrad assembler | `culture/basic-to-machine-code`, `hardware/z80`, `systems/amstrad-cpc` |
| Homebrew Computer Club | communities | Where Wozniak showed *Breakout* in BASIC | `games/breakout`, `systems/apple-ii` |
| Hot Coffee (Grand Theft Auto: San Andreas) | culture | The ESRB's biggest test | `culture/esrb`, `games/grand-theft-auto`, `companies/rockstar` |
| Hudson Caravan | events | Hudson's touring shooting contests from 1985 | `companies/hudson-soft` |
| Humble Bundle | distribution | Pay-what-you-want game bundles | `culture/indie-games`, `distribution/digital-distribution` |
| HyperCard | tools | Apple's authoring program that Myst and The Manhole were built with | `games/myst`, `companies/cyan` |
| Impulse Tracker | tools | The IT format, used in the Unreal engine, source released in 2014 | `tools/protracker`, `culture/tracker-music`, `techniques/mod-format`, `games/unreal`, `games/deus-ex` |
| iMUSE | techniques | LucasArts' interactive music system by Michael Land and Peter McConnell | `games/monkey-island`, `techniques/scumm`, `companies/lucasarts` |
| Independent Games Festival | events | GDC's indie awards since the late 1990s | `culture/gdc`, `culture/indie-games`, `people/derek-yu` |
| Indie Game Jam and Global Game Jam | events | The jams before and alongside Ludum Dare; Global Game Jam is the largest | `communities/ludum-dare`, `culture/game-jams` |
| iNES format and Marat Fayzullin | tools | The `.nes` format and mapper numbering used across NES emulation | `communities/nesdev`, `systems/nintendo-entertainment-system`, `emulators/mesen` |
| Infinity Engine | tools | BioWare's engine behind five games | `games/baldurs-gate`, `games/planescape-torment`, `games/icewind-dale`, `companies/bioware`, `companies/black-isle-studios`, `genres/western-rpg` |
| Inform and Graham Nelson | tools | Graham Nelson's 1993 Z-machine compiler, which carried the format past Infocom | `genres/text-adventure`, `techniques/z-machine`, `companies/infocom` |
| Interactive Fiction Competition | events | An annual event since 1995 | `genres/text-adventure` |
| InvisiClues | culture | Infocom's invisible-ink hint books | `games/zork`, `companies/infocom`, `genres/text-adventure` |
| iRacing | communities | The online sim-racing service that grew from Papyrus | `genres/racing-simulation` |
| Iwata Asks | culture | The 2006–2015 interview series cited throughout the Vault | `people/satoru-iwata`, `companies/nintendo`, `people/koji-kondo`, `games/super-mario-bros`, `systems/nintendo-game-and-watch` |
| KANDU and Crusaders | groups | The Gathering's organisers | `events/the-gathering`, `groups/spaceballs` |
| Kefrens bars | techniques | Vertical raster bars from a one-line buffer and a negative modulo | `groups/kefrens`, `techniques/raster-effects`, `hardware/copper` |
| KeSPA and OnGameNet | communities | Governing body and broadcaster of Korean pro gaming | `games/starcraft`, `communities/esports-origins`, `companies/blizzard` |
| kkrunchy | tools | ryg's 64K executable compressor, public domain since 2012 | `groups/farbrausch`, `demos/debris`, `techniques/size-coding`, `techniques/compression`, `people/ryg`, `demos/fr-08-the-product` |
| Kracker Jax and parameter copiers | tools | The US mail-order trade in one-game crack files, the best-documented C64 copier business | `techniques/copy-protection`, `techniques/disk-protection`, `communities/cracking-scene` |
| Lakka | tools | RetroArch-based emulation operating system | `emulators/retroarch`, `hardware/raspberry-pi` |
| Lewis Galoob Toys v. Nintendo | culture | The fair-use case over the Game Genie | `hardware/game-genie`, `companies/galoob`, `companies/nintendo` |
| Linus Åkesson and A Mind Is Born | demos | A C64 256-byte landmark with a detailed write-up by its author | `techniques/size-coding` |
| Linux for PlayStation 2 and Yabasic | tools | Sony's two official hobbyist programming routes on the PS2 | `systems/sony-playstation-2` |
| Little Sound DJ and Nanoloop | tools | The Game Boy music programs behind the 2000s chip scene | `communities/chiptune-scene`, `systems/game-boy` |
| Loonies | groups | Danish Amiga group, winner at Mekka & Symposium, Revision and Assembly | `demos/elevated`, `events/mekka-symposium`, `events/revision-party`, `events/assembly-party` |
| LSD (Amiga group) | groups | English Amiga group behind *Jesus on E's*, the *Grapevine* diskmag and *LSD Legal Tools* | `demos/jesus-on-es`, `demos/state-of-the-art`, `demos/nine-fingers`, `distribution/public-domain`, `magazines/scene-diskmags` |
| MathEngine / Karma | tools | The physics middleware behind *Unreal Tournament 2003*'s ragdolls | `techniques/ragdoll-physics`, `techniques/havok`, `techniques/physics-engines`, `games/hitman` |
| MC-Link | communities | Early Italian online service, later an ISP | `magazines/mc-microcomputer`, `communities/bbs-scene` |
| Mega BASIC and Laser BASIC | tools | Rival Spectrum BASIC extensions; Laser BASIC also appeared on the C64 | `tools/sinclair-basic`, `tools/beta-basic`, `tools/simons-basic` |
| Megademo | techniques | The multi-part demo form the trackmo replaced | `demos/desert-dream`, `groups/kefrens`, `communities/demo-scene`, `demos/mental-hangover`, `groups/scoopex`, `groups/red-sector-inc`, `demos/shock-megademo` |
| MegaZeux | tools | The best-known successor to ZZT | `tools/zzt`, `people/tim-sweeney` |
| Memories and HellMood | demos | A modern 256-byte MS-DOS landmark | `techniques/size-coding` |
| MESS | emulators | The computer and console emulator merged into MAME in 2015 | `emulators/mame`, `communities/internet-archive` |
| Metacritic | culture | Review aggregation and its role in developer contracts | `companies/obsidian-entertainment`, `games/fallout-new-vegas` |
| Micro Live | culture | The BBC's live computer magazine series, 1984–87 | `phenomena/bbc-computer-literacy-project`, `people/ian-mcnaught-davis` |
| Microelectronics Education Programme (MEP) | phenomena | The state body behind most British school software, 1980/81–1986 | `culture/educational-software`, `culture/educational-gaming`, `systems/bbc-micro`, `phenomena/bbc-computer-literacy-project`, `games/grannys-garden` |
| Micronet 800 / Prestel | communities | Britain's telephone software service, and the root of Firebird | `distribution/digital-distribution`, `companies/firebird`, `companies/telecomsoft`, `systems/bbc-micro` |
| Micropolis | tools | The open-source *SimCity* | `games/sim-city` |
| Micros in Schools | phenomena | The Department of Industry subsidies that put BBC Micros in schools | `culture/educational-software`, `systems/bbc-micro`, `systems/sinclair-zx-spectrum` |
| Microsoft BASIC (Altair BASIC) | tools | Common ancestor of Applesoft, Commodore, Level II, Color and MSX BASIC | `companies/microsoft`, `techniques/basic-v2`, `systems/trs-80`, `systems/apple-ii`, `systems/tandy-coco`, `systems/msx` |
| Mindstorms | books | Papert's 1980 book behind the Logo movement | `tools/logo-language`, `people/seymour-papert` |
| MOBA genre | genres | What grew out of RTS: DotA, League of Legends and Dota 2 | `genres/rts-genre`, `communities/esports-origins`, `games/warcraft` |
| MobyGames | communities | The game database the VGHF availability study sampled from | `culture/game-preservation` |
| MS-DOS | tools | Microsoft's PC operating system | `companies/microsoft` |
| Multiplay and Insomnia | events | The British LAN party organiser and series | `communities/lan-parties` |
| Music Macro Language (MML) | techniques | The text notation used by Koshiro, MUCOM88 and many Japanese computer musicians | `people/yuzo-koshiro`, `techniques/sound-drivers`, `techniques/fm-synthesis` |
| Mysdata | events | Swedish party co-run by Censor since 2022 | `groups/censor-design` |
| National Videogame Museum | culture | The UK's main game museum and its predecessor, the National Videogame Archive | `culture/game-preservation`, `games/manic-miner` |
| NesCartDB | tools | The cartridge board database cited by NES hardware and game entries | `hardware/mmc1`, `hardware/mmc3`, `communities/nesdev` |
| NESticle | emulators | The 1997 NES emulator, NESdev's example of compatibility without accuracy | `emulators/emulation`, `systems/nintendo-entertainment-system`, `emulators/fceux`, `techniques/cycle-accuracy`, `communities/nesdev`, `emulators/mesen` |
| Nestopia | emulators | The third of NESdev's best-of-breed NES emulators | `emulators/mesen`, `communities/nesdev` |
| NetImmerse and Gamebryo | tools | RenderWare's main rival | `techniques/renderware` |
| NewIcons | tools | Salmoria's Amiga icon system | `people/nicola-salmoria`, `systems/commodore-amiga` |
| Nintendo World Championships | events | Nintendo's 1990 touring competition | `communities/esports-origins`, `companies/nintendo`, `games/tetris`, `games/super-mario-bros` |
| No-Intro | communities | The standard verified catalogue of cartridge dumps | `culture/game-preservation`, `emulators/emulation`, `emulators/mame` |
| NoisePacker and module packers | tools | How demo musicians shrank tracker modules | `groups/phenomena`, `communities/chiptune-scene` |
| NoiseTracker | tools | Mahoney & Kaktus's rewrite that fixed the 31-sample `M.K.` form | `tools/soundtracker`, `tools/protracker`, `techniques/mod-format`, `culture/tracker-music` |
| NSF (Nintendo Sound Format) | techniques | How NES music is ripped and played outside the game | `tools/famitracker`, `tools/deflemask`, `hardware/apu` |
| Odyssey and Alcatraz | demos | Alcatraz's 1991 demo, a winner at The Party 1991 and a public-domain bestseller | `demos/hardwired`, `communities/demo-parties`, `events/the-party`, `demos/voyage` |
| OpenTTD and OpenRCT2 | tools | Long-running open-source re-implementations of Chris Sawyer's games | `games/roller-coaster-tycoon`, `games/transport-tycoon`, `people/chris-sawyer` |
| Operation Buccaneer | phenomena | The 2001 US anti-piracy investigation behind Razor 1911's prosecution | `groups/razor-1911`, `distribution/piracy`, `communities/cracking-scene` |
| Operation Fastlink | events | The 2004 multinational raid on release groups | `groups/fairlight`, `groups/razor-1911`, `communities/cracking-scene` |
| Origin | demos | Complex's Amiga demo, winner of The Party 1993 | `communities/demo-parties`, `events/the-party`, `demos/arte`, `groups/sanity` |
| Panic | demos | Future Crew's demo, second at The Party 1992 | `groups/future-crew`, `people/psi`, `people/wildfire`, `demos/second-reality` |
| PC bang | culture | Korean PC rooms, the social setting of Korean StarCraft | `games/starcraft`, `communities/esports-origins` |
| PC-Write and Bob Wallace | tools | The commission-paying shareware word processor | `distribution/shareware` |
| PCSX2 | emulators | The main PlayStation 2 emulator, developed since 2001 | `emulators/pcsx`, `systems/sony-playstation-2`, `emulators/emulation` |
| PEGI | culture | Europe's route from voluntary labels to legally enforced ratings | `culture/esrb`, `culture/game-ratings` |
| Performers and Bonzai | groups | Frequent top finishers and winners at X | `events/x-party` |
| Personal Paint | tools | Cloanto's paint program, bundled with Amigas and freed in 1998 | `companies/cloanto`, `tools/deluxe-paint` |
| Pinball | culture | Williams' main business for most of its life | `companies/williams-electronics`, `companies/midway` |
| Play-by-mail games | culture | The pre-internet multiplayer culture that shaped Singleton's designs | `people/mike-singleton`, `magazines/computer-and-video-games` |
| PlayCable | distribution | The earliest games-by-cable service (1980) | `distribution/digital-distribution`, `systems/intellivision` |
| PlayStation homebrew SDKs (PSn00bSDK, ps2sdk) | tools | Current open-source routes for both PlayStations | `systems/sony-playstation`, `systems/sony-playstation-2` |
| PowerPacker and Turbo Imploder | tools | The main Amiga crunchers | `techniques/compression`, `communities/cracking-scene` |
| Professional Page | tools | The Amiga desktop publishing program behind Amiga Shopper's page demonstration | `magazines/amiga-shopper` |
| Programming the Z80 (Rodnay Zaks) | books | The book nearly every period source recommends | `culture/basic-to-machine-code`, `hardware/z80`, `people/matthew-smith` |
| ProPack (RNC compression) | tools | Rob Northen's compressor, used across Amiga, ST, PC and console games | `people/rob-northen`, `techniques/compression`, `techniques/copylock` |
| PSEmu Pro | emulators | The early PlayStation emulator whose plugin interface PCSX and ePSXe adopted | `emulators/pcsx`, `emulators/emulation` |
| Quake done Quick | culture | The 1997 run that founded Quake speedrunning | `communities/speedrunning`, `games/quake`, `culture/speed-demos-archive` |
| QuakeWorld and GLQuake | tools | Quake's internet play and 3D-card support | `games/quake`, `culture/online-multiplayer`, `techniques/client-side-prediction` |
| Quick time event | techniques | The name comes from *Shenmue*; the idea runs from *Dragon's Lair* to *Resident Evil 4* | `games/shenmue`, `games/resident-evil`, `people/yu-suzuki` |
| Radwar Enterprises | groups | German C64 and Amiga group whose parties drew the cracking scene | `groups/red-sector-inc`, `groups/genesis-project`, `groups/paradox`, `magazines/illegal`, `groups/fairlight` |
| Ray marching and signed distance fields | techniques | The defining 4K technique of 2008–2009 and later Shadertoy | `groups/rgba`, `demos/elevated`, `people/iq`, `techniques/size-coding` |
| Ray tracing | techniques | Explained from scratch in the Juggler and Sculpt entries | `people/eric-graham`, `culture/the-juggler`, `tools/sculpt-3d`, `tools/imagine` |
| Real 3D | tools | The other major Amiga 3D package of the 1990s | `tools/imagine`, `tools/lightwave-3d` |
| Real Masters | groups | Winners of the first Chaos Constructions Spectrum demo competition | `events/chaos-constructions`, `systems/sinclair-zx-spectrum` |
| Recreational Software Advisory Council | culture | The PC industry's content-scale alternative to the ESRB, 1994–1999 | `culture/esrb`, `culture/congressional-hearings-1993`, `culture/game-ratings` |
| Red Sector Demomaker | tools | Demo-construction kit sold by British PD libraries from 1991 to 1995 | `groups/red-sector-inc`, `communities/demo-scene` |
| Repton Infinity | tools | An early user-programmable game engine with its own language, Reptol | `games/repton` |
| reSID and Dag Lem | tools | The SID model used by VICE and SID players | `emulators/vice`, `hardware/sid-chip` |
| RetroAchievements | communities | Achievement service integrated with RetroArch | `emulators/retroarch`, `communities/speedrunning` |
| RetroPie | tools | The most common Raspberry Pi emulation setup, often confused with RetroArch | `hardware/raspberry-pi`, `emulators/retroarch`, `emulators/emulation` |
| Retrospec | groups | The remake group behind several notable 2000s remakes of 8-bit games | `games/head-over-heels` |
| RISC OS | tools | Acorn's operating system, still developed and open source since 2018 | `systems/acorn-archimedes`, `companies/acorn-computers` |
| Romhacking.net | communities | The main hub for fan translations and ROM hacks from 2005 to 2024 | `communities/fan-translations`, `communities/internet-archive`, `communities/modding` |
| RPGe, DeJap and Oasis | groups | The groups behind the landmark fan-translation patches | `communities/fan-translations`, `games/final-fantasy`, `games/tales-of-phantasia` |
| SCA virus | phenomena | The first well-known Amiga boot-block virus, which could wipe protection data | `techniques/disk-protection`, `communities/cracking-scene` |
| Scene.org Awards | events | The demoscene's annual juried awards from the early 2000s | `demos/edge-of-disgrace`, `demos/starstruck`, `demos/ocean-machine`, `groups/fairlight`, `groups/booze-design`, `groups/razor-1911` |
| Scream Tracker | tools | The PC's main tracker in the early 1990s, written by Psi of Future Crew | `groups/future-crew`, `culture/tracker-music`, `tools/protracker`, `people/psi`, `people/purple-motion`, `people/skaven`, `techniques/mod-format` |
| ScummVM | emulators | The engine reimplementation that runs SCUMM, AGI, SCI and Revolution's games today, and holds the *Beneath a Steel Sky* source | `techniques/scumm`, `games/monkey-island`, `companies/lucasarts`, `culture/game-preservation`, `games/driller`, `techniques/freescape`, `techniques/agi-engine`, `techniques/sci-engine`, `games/day-of-the-tentacle`, `games/grim-fandango`, `companies/revolution-software`, `games/beneath-a-steel-sky`, `games/lure-of-the-temptress`, `distribution/abandonware` |
| Secretaria Especial de Informática / CAPRE | phenomena | The agencies that ran Brazil's market reserve | `culture/brazilian-market-reserve`, `magazines/micro-sistemas`, `companies/dismac` |
| SecuROM | techniques | The best-known PC DRM of the late 2000s | `games/bioshock`, `techniques/copy-protection` |
| Sega Channel | distribution | Games by cable for the Mega Drive, 1994–98 | `distribution/digital-distribution`, `systems/sega-mega-drive`, `companies/sega` |
| sfxr | tools | The sound-effect generator made for Ludum Dare | `communities/ludum-dare` |
| Shadertoy | tools | The browser shader site by Quílez and Jeremias that grew out of 4K shader work | `groups/rgba`, `people/iq`, `techniques/size-coding` |
| Shoryuken.com | communities | The FGC website that ran Evo | `events/evo`, `communities/fighting-game-community` |
| SIDPLAY and PlaySID | tools | The players that made ripped SID music listenable on the Amiga and PC | `tools/hvsc`, `communities/chiptune-scene`, `hardware/sid-chip` |
| SkoolKit | tools | The modern annotated Spectrum ROM and game disassembly toolkit | `books/complete-spectrum-rom-disassembly`, `techniques/zx-spectrum-rom-disassembly` |
| Smash Designs | groups | German C64 then PC group, repeated Mekka & Symposium winner | `events/mekka-symposium`, `events/the-party` |
| Software Preservation Society and IPF | communities | The group behind the IPF disk format and KryoFlux | `emulators/winuae`, `hardware/kryoflux`, `techniques/disk-protection`, `techniques/copylock`, `culture/game-preservation`, `people/toni-wilen` |
| Soundmonitor | tools | Hülsbeck's C64 music editor, sold to *64'er*, an early tracker | `people/chris-huelsbeck`, `culture/tracker-music` |
| Source engine | tools | Valve's engine for *Half-Life 2* and *Counter-Strike* | `games/half-life-2`, `companies/valve`, `games/counter-strike` |
| Spectrum Computing and ZXDB | tools | The archive and open database most Spectrum research now uses | `tools/world-of-spectrum`, `systems/sinclair-zx-spectrum`, `tools/graphic-adventure-creator`, `games/stormlord`, `games/driller`, `tools/paw`, `tools/arcade-game-designer`, `tools/the-quill` |
| SpeedScript | tools | The best-known type-in word processor | `magazines/compute-magazine`, `magazines/computes-gazette`, `distribution/type-in-listings` |
| Starcade | culture | The 1982–84 TV game show | `communities/esports-origins`, `culture/arcade-culture` |
| Stealth games (genre) | genres | The genre, as opposed to the existing technique entry | `games/metal-gear-solid`, `games/thief`, `games/splinter-cell` |
| StepMania | tools | Free PC dance-game engine | `hardware/dance-mat`, `games/dance-dance-revolution` |
| Stern Electronics v. Kaufman | phenomena | The 1982 ruling on copyright in screen displays | `games/scramble`, `companies/konami`, `distribution/piracy` |
| Success + The Ruling Company (SCS*TRC) | groups | Dutch cracking group that has organised X since 1995 | `events/x-party` |
| Super Expander 64 | tools | Commodore's own BASIC extension, often confused with Simons' BASIC | `tools/simons-basic`, `systems/commodore-64`, `people/david-simons` |
| Super Scaler and taikan cabinets | techniques | Sega's sprite-scaling hardware and moving cabinets | `games/hang-on`, `games/space-harrier`, `games/out-run`, `games/after-burner`, `techniques/sprite-scaling` |
| Supermon | tools | The standard community machine-code monitor for the PET, VIC and C64 | `people/jim-butterfield`, `hardware/6502`, `techniques/kernal-io` |
| Symphonic game-music concerts | events | Thomas Böcker's Merregnon Studios concerts of game music | `people/purple-motion`, `people/chris-huelsbeck` |
| TADS | tools | The main rival text-adventure design system to Inform | `techniques/z-machine`, `genres/text-adventure` |
| Talent | groups | Danish C64 group, half of the Ikari + Talent co-op | `groups/ikari` |
| TASVideos | communities | The site that publishes tool-assisted runs and sets their emulator rules | `culture/tool-assisted-speedrun`, `communities/speedrunning`, `emulators/fceux` |
| TBC | groups | Danish demo group, co-author of *Elevated* and home of Mentor | `demos/elevated`, `groups/rgba`, `techniques/size-coding` |
| Technium 220 | groups | Spectrum group linking Reb's *Jesus on E's* conversion and *Speed 2* | `demos/jesus-on-es-spectrum`, `demos/signal-part-3` |
| Teesside Cracking Service / The Omega Man | groups | UK crack group whose intros the scene credits with the first linecrunch | `techniques/linecrunch`, `communities/crack-intros` |
| Telesoftware / Ceefax | techniques | Broadcasting programs over teletext | `phenomena/bbc-computer-literacy-project`, `systems/bbc-micro` |
| TFMX | tools | Hülsbeck's Amiga music system, sold commercially in 1990 | `people/chris-huelsbeck`, `tools/soundtracker`, `culture/tracker-music`, `techniques/interrupt-driven-music`, `games/turrican`, `techniques/sound-drivers` |
| The Art of Computer Game Design | books | Chris Crawford's 1984 book on game design | `people/chris-crawford`, `games/rockys-boots` |
| The Art Studio | tools | Rainbird's Lenslok-protected Spectrum art package | `techniques/lenslock` |
| The Automatic Proofreader and MLX | tools | *COMPUTE!*'s typing checkers for listings | `distribution/type-in-listings`, `magazines/compute-magazine` |
| The Black Mages | groups | Uematsu's rock band of Square staff, 2002–2010 | `people/nobuo-uematsu`, `companies/square` |
| The Computer Crossroads | events | Gothenburg's 1993 party, the biggest in Sweden at the time, where *Wonderland X* won | `groups/kefrens`, `groups/phenomena`, `demos/crystal-dream`, `communities/demo-parties`, `companies/dice-studio`, `groups/the-silents`, `groups/censor-design`, `groups/booze-design`, `demos/comaland`, `communities/crack-intros`, `demos/wonderland` |
| The Computer Programme | culture | The BBC's 1982 TV series at the centre of the Computer Literacy Project, presented by Chris Serle and Ian McNaught-Davis | `phenomena/bbc-computer-literacy-project`, `systems/bbc-micro`, `people/ian-mcnaught-davis` |
| The Future Was Here | books | Jimmy Maher's 2012 history of the Amiga, with a chapter on the scene | `demos/state-of-the-art`, `communities/demo-scene`, `systems/commodore-amiga` |
| The King of Kong | culture | The 2007 documentary that made the Donkey Kong rivalry famous | `events/twin-galaxies`, `games/donkey-kong` |
| The Meteoriks | events | Demoscene awards presented at Revision | `demos/comaland` |
| The Print Shop | tools | The home-printing program that carried the Brøderbund name for decades | `companies/broderbund` |
| The Wizard (1989 film) | culture | The film that previewed Super Mario Bros. 3 | `games/super-mario-bros-3`, `magazines/nintendo-power` |
| TIGSource | communities | The forum where many 2000s and 2010s independent games were made in public | `people/derek-yu`, `culture/indie-games`, `games/spelunky` |
| Toronto PET Users Group (TPUG) | communities | It claimed 15,000 members worldwide by 1986, and its software library was a model for user groups | `people/jim-butterfield`, `culture/user-groups` |
| TOSEC | tools | The software catalogue used across preservation | `communities/internet-archive`, `emulators/emulation`, `culture/game-preservation` |
| track one | demos | Fairlight's 2006 demo, second at Assembly and winner of a Scene.org award | `demos/starstruck`, `groups/fairlight` |
| Trackmo | techniques | The track-loaded continuous demo | `demos/desert-dream`, `groups/kefrens`, `communities/demo-scene`, `demos/mental-hangover`, `groups/scoopex`, `demos/coma-light-13`, `communities/crack-intros` |
| Tron (1982 film) | culture | The arcade boom reaching Hollywood | `phenomena/golden-age-arcade` |
| TRSI | groups | Red Sector's successor from 1990, with its own demos and the TRSI Recordz label | `demos/state-of-the-art`, `demos/desert-dream`, `groups/kefrens`, `groups/red-sector-inc`, `people/jester`, `events/the-gathering` |
| Turbo-BASIC XL | tools | Widely used free BASIC for the Atari 8-bits | `tools/gfa-basic`, `systems/atari-8-bit` |
| TZX format | techniques | The Spectrum tape-image format behind WoS tape preservation | `tools/world-of-spectrum`, `emulators/fuse`, `systems/sinclair-zx-spectrum` |
| UAE and Bernd Schmidt | emulators | The parent Amiga emulator of WinUAE, FS-UAE and PUAE, and its author | `emulators/emulation`, `emulators/winuae`, `emulators/fs-uae`, `emulators/retroarch`, `people/toni-wilen`, `techniques/emulators` |
| UCSD p-System / P-code | techniques | The portable virtual machine Blank and Galley compared Z-code to | `techniques/z-machine` |
| UFLI, NUFLI and sprite-underlay modes | techniques | The C64's post-FLI picture modes, mentioned only in passing | `groups/crest`, `techniques/fli`, `techniques/raster-tricks` |
| UK Video Games Tax Relief | phenomena | The 2014 relief and its cultural test | `culture/british-game-development` |
| UltraHLE | emulators | The 1999 N64 emulator that brought high-level emulation to wide attention | `emulators/emulation`, `systems/nintendo-64`, `techniques/emulators` |
| Understanding Your Spectrum | books | Logan's companion volume, recommended alongside the ROM disassembly | `books/complete-spectrum-rom-disassembly`, `people/ian-logan`, `companies/melbourne-house` |
| Unlicensed NES games | phenomena | Camerica, Color Dreams, AVE and Tengen's workarounds for the 10NES, and Nintendo's response | `games/micro-machines`, `systems/nintendo-entertainment-system` |
| Unreal (demo) | demos | Future Crew's Assembly '92 winner; games/unreal is the Epic game | `groups/future-crew`, `communities/demo-parties`, `people/psi`, `people/wildfire`, `demos/second-reality` |
| Untouchable Cracking Force | groups | ESI's rival in the North American scene | `groups/eagle-soft-incorporated`, `communities/cracking-scene` |
| Up Rough | groups | Swedish group that ran Datastorm with Genesis Project | `events/datastorm` |
| Usenet | communities | How *Hack* and *NetHack* were distributed and discussed | `games/nethack`, `genres/roguelike` |
| V2 synthesiser | tools | farbrausch's softsynth, with its public release | `people/kb`, `groups/farbrausch`, `demos/fr-08-the-product`, `demos/debris` |
| Verlet integration | techniques | The technique behind *Hitman*'s corpses and cloth | `techniques/ragdoll-physics`, `techniques/physics-engines` |
| VGM file format | techniques | The logging format behind most modern Sega, PC Engine and arcade chip-music collections | `tools/deflemask`, `hardware/ym2612` |
| Videogames: In the Beginning | books | Baer's own documented account | `people/ralph-baer`, `games/pong` |
| Virtual Dreams | groups | Finnish demo group, second at The Party 1994 with *Psychedelic* | `groups/andromeda`, `events/the-party`, `demos/nexus-7`, `demos/arte` |
| Virtual Theatre | techniques | Revolution's character-simulation engine, with NPC routines and autorouting, across three games | `companies/revolution-software`, `games/lure-of-the-temptress`, `games/beneath-a-steel-sky`, `techniques/point-and-click`, `games/broken-sword` |
| VisiCalc | tools | The program that turned the Apple II into a business machine | `systems/apple-ii`, `culture/pc-gaming` |
| Vision Factory and Paranoimia | groups | Two of the big three Amiga groups of 1990 and the roots of Skid Row | `groups/skid-row`, `groups/quartex` |
| Wayback Machine | tools | The main way lost game websites are read today | `communities/internet-archive` |
| Wayfarer | demos | Spaceballs' demo, winner at The Gathering 1992 | `groups/spaceballs`, `groups/andromeda`, `events/the-gathering` |
| Werkkzeug | tools | farbrausch's operator-based content editor, released as source in 2012 | `groups/farbrausch`, `demos/fr-08-the-product`, `demos/debris`, `techniques/procedural-generation` |
| WHDLoad | tools | The hard-disk installer behind most Amiga game emulation setups | `emulators/fs-uae`, `emulators/winuae`, `systems/commodore-amiga` |
| Wireplay | communities | BT's dial-up games network | `culture/online-multiplayer`, `communities/lan-parties` |
| World of Commodore | events | Commodore trade shows with demo competitions | `groups/sanity` |
| Write Your Own Adventure Programs | books | Usborne's adventure-writing book, cited by the Colossal Cave Adventure entry | `books/usborne-computing-books`, `games/colossal-cave-adventure` |
| Xbox Live Arcade | distribution | The download channel that carried *Geometry Wars* and retro re-releases | `culture/indie-games`, `distribution/digital-distribution`, `culture/xbox-live`, `games/geometry-wars` |
| Xenon | groups | Dutch demo group, X co-organiser since 2000 | `events/x-party` |
| Zeus assembler | tools | Crystal Computing's 1983 Spectrum and C64 assembler, still maintained for the PC and the Spectrum Next | `culture/basic-to-machine-code`, `companies/design-design` |
| ZSNES and Snes9x | emulators | The speed-first SNES emulators bsnes was measured against | `techniques/cycle-accuracy`, `emulators/emulation`, `people/byuu` |
| Zuntata | groups | Taito's sound team and band, formed in 1987 | `companies/taito`, `games/darius`, `games/bubble-bobble` |

The *Your Sinclair* Smash Tapes and *Sinclair User* Megatape fit better as sections of `distribution/cover-tapes` than as entries.

Graftgold's 16-bit games (*Paradroid 90*, *Fire & Ice*, *Uridium 2*) fit better as a section of `companies/graftgold`, and Gilsoft's The Illustrator as a section of `companies/gilsoft` or `tools/the-quill`.
