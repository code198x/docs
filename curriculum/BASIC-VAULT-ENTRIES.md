# BASIC Curricula: Vault Entries

**Purpose:** Catalogue all Vault entries arising from the BASIC curriculum documentation.

**Last Updated:** 2026-01-18

---

## People

| Entry | Type | Notes |
|-------|------|-------|
| `david-simons` | People | Creator of Simons' BASIC for C64 |
| `francois-lionet` | People | Creator of STOS and AMOS |
| `andy-davidson` | People | Creator of Worms (in Blitz Basic) |
| `mark-sibly` | People | Creator of Blitz Basic |

### David Simons

| Aspect | Details |
|--------|---------|
| **Known for** | Simons' BASIC |
| **Platform** | Commodore 64 |
| **Publisher** | Commodore |
| **Impact** | Made C64 BASIC viable for games |

### François Lionet

| Aspect | Details |
|--------|---------|
| **Known for** | STOS (1988), AMOS (1990) |
| **Platforms** | Atari ST, Amiga |
| **Company** | Later co-founded Clickteam |
| **Impact** | Revolutionised game creation tools |

### Andy Davidson

| Aspect | Details |
|--------|---------|
| **Known for** | Worms (1995) |
| **Language** | Blitz Basic |
| **Publisher** | Team17 |
| **Impact** | Proved BASIC could make commercial hits |

### Mark Sibly

| Aspect | Details |
|--------|---------|
| **Known for** | Blitz Basic series |
| **Company** | Acid Software |
| **Platforms** | Amiga, PC |
| **Legacy** | BlitzMax, Monkey X |

---

## Software

| Entry | Type | Platform |
|-------|------|----------|
| `simons-basic` | Software | Commodore 64 |
| `amos` | Software | Amiga |
| `amos-professional` | Software | Amiga |
| `blitz-basic-2` | Software | Amiga |
| `stos` | Software | Atari ST |
| `beta-basic` | Software | ZX Spectrum |
| `laser-basic-spectrum` | Software | ZX Spectrum |
| `laser-basic-c64` | Software | Commodore 64 |
| `gfa-basic` | Software | Atari ST |
| `turbo-basic-xl` | Software | Atari 8-bit |

### Simons' BASIC

| Aspect | Details |
|--------|---------|
| **Platform** | Commodore 64 |
| **Creator** | David Simons |
| **Publisher** | Commodore (1983) |
| **Commands** | 114 additional commands |
| **Features** | Sprites, graphics, sound, toolkit |

### AMOS Professional

| Aspect | Details |
|--------|---------|
| **Platform** | Amiga |
| **Creator** | François Lionet |
| **Publisher** | Europress (1992) |
| **Features** | Sprites, bobs, screens, samples |
| **Commercial games** | Ultimate Soccer Manager, Guardian |

### Blitz Basic 2

| Aspect | Details |
|--------|---------|
| **Platform** | Amiga |
| **Creator** | Mark Sibly |
| **Company** | Acid Software (1993) |
| **Features** | Compiled, fast, low-level access |
| **Commercial games** | Worms, Skidmarks, Super Skidmarks |

### Beta BASIC

| Aspect | Details |
|--------|---------|
| **Platform** | ZX Spectrum |
| **Creator** | Andy Wright |
| **Features** | Procedures, toolkit, extensions |
| **Impact** | Made Spectrum BASIC more capable |

---

## Games (BASIC-made commercial releases)

| Entry | Type | Language |
|-------|------|----------|
| `worms-original` | Game | Blitz Basic |
| `skidmarks` | Game | Blitz Basic |
| `super-skidmarks` | Game | Blitz Basic |
| `ultimate-soccer-manager` | Game | AMOS |
| `guardian-amiga` | Game | AMOS |
| `scorched-tanks` | Game | AMOS |

### Worms (1995)

| Aspect | Details |
|--------|---------|
| **Developer** | Team17 |
| **Creator** | Andy Davidson |
| **Language** | Blitz Basic |
| **Genre** | Artillery/strategy |
| **Impact** | One of gaming's biggest franchises |
| **Significance** | Proved BASIC could make AAA games |

### Skidmarks (1993)

| Aspect | Details |
|--------|---------|
| **Developer** | Acid Software |
| **Language** | Blitz Basic |
| **Genre** | Top-down racing |
| **Features** | Split-screen multiplayer, physics |
| **Sequel** | Super Skidmarks (1995) |

### Ultimate Soccer Manager (1995)

| Aspect | Details |
|--------|---------|
| **Developer** | Impressions Games |
| **Language** | AMOS |
| **Genre** | Management simulation |
| **Platforms** | Amiga, DOS |

---

## Techniques

| Entry | Type | Platforms |
|-------|------|-----------|
| `udg-graphics` | Technique | Spectrum, C64, CPC |
| `bob-graphics` | Technique | Amiga (AMOS/Blitz) |
| `double-buffering-basic` | Technique | Amiga |
| `c64-custom-characters` | Technique | Commodore 64 |
| `peek-poke-gaming` | Technique | Commodore 64 |
| `destructible-terrain` | Technique | Amiga (Blitz) |
| `basic-inline-assembly` | Technique | BBC Micro |

### User Defined Graphics (UDGs)

| Aspect | Details |
|--------|---------|
| **Platforms** | Spectrum, C64, CPC, MSX |
| **Purpose** | Custom character graphics |
| **Method** | POKE character data into memory |
| **Use** | Simple sprites in BASIC games |

```basic
; Spectrum UDG definition
FOR n = 0 TO 7
  READ a
  POKE USR "a"+n, a
NEXT n
DATA 24,60,126,255,255,90,36,102
```

### Bob Graphics (Blitter Objects)

| Aspect | Details |
|--------|---------|
| **Platform** | Amiga |
| **Languages** | AMOS, Blitz Basic |
| **Purpose** | Software sprites using blitter |
| **Advantage** | Unlimited objects (vs 8 hardware sprites) |
| **Requirement** | Double buffering |

### Destructible Terrain

| Aspect | Details |
|--------|---------|
| **Famous use** | Worms |
| **Language** | Blitz Basic |
| **Method** | Bitmap manipulation, pixel collision |
| **Key technique** | Circle fill with background colour |

---

## Culture

| Entry | Type | Notes |
|-------|------|-------|
| `type-in-culture` | Culture | Magazine BASIC listings |
| `basic-game-legitimacy` | Culture | BASIC as complete development path |
| `bedroom-coder-basic` | Culture | Home game development |
| `magazine-basic-listings` | Culture | CRASH, ZZAP!64, etc. |

### Type-In Culture

| Aspect | Details |
|--------|---------|
| **Era** | 1980s-early 1990s |
| **Method** | Print BASIC listings, readers type in |
| **Magazines** | CRASH, Your Sinclair, ZZAP!64, etc. |
| **Volume** | Thousands of games published |
| **Legacy** | How a generation learned to code |

### BASIC Game Development Legitimacy

| Aspect | Details |
|--------|---------|
| **Misconception** | BASIC was "just for learning" |
| **Reality** | Commercial games shipped in BASIC |
| **Evidence** | Worms, Skidmarks, USM, countless others |
| **Modern view** | Complete development environment |

---

## Companies

| Entry | Type | Notes |
|-------|------|-------|
| `acid-software` | Company | Blitz Basic creators, Skidmarks |
| `europress` | Company | AMOS publisher |
| `team17-early` | Company | Worms, Blitz Basic games |
| `clickteam` | Company | François Lionet's later company |

### Acid Software

| Aspect | Details |
|--------|---------|
| **Founded** | Late 1980s |
| **Key people** | Mark Sibly |
| **Products** | Blitz Basic 2, Skidmarks |
| **Platform** | Amiga |

---

## Summary

| Category | New Entries |
|----------|-------------|
| **People** | 4 |
| **Software** | 10 |
| **Games** | 6 |
| **Techniques** | 6 |
| **Culture** | 4 |
| **Companies** | 4 |
| **Total** | **34** |

---

## Running Vault Total

| Previous | This Document | New Total |
|----------|---------------|-----------|
| ~1,625 | +34 | **~1,659 entries** |
