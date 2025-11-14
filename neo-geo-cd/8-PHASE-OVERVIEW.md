# Neo Geo CD Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Neo Geo CD / CDZ (1994-1999) → Same as Neo Geo MVS/AES but CD-ROM!
**Approach:** Game-first, pattern library, dual-processor coordination, CD-ROM optimization
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** CD-ROM version of Neo Geo (1994), IDENTICAL hardware to MVS/AES (68000 + Z80, same sprite system, same audio), but CD-ROM instead of cartridge, major advantage: cheaper games ($50 vs $200-300 cartridge!), major disadvantage: LONG load times (1× CD), 1 million units sold, CDZ (1996) has 2× CD drive (faster loading), all MVS/AES games convertible to CD with load screens added

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Neo Geo CD is CD-ROM version of Neo Geo, no BASIC interpreter. Curriculum begins directly with assembly.

**Prerequisite Knowledge:** Neo Geo MVS/AES assembly programming (68000, Z80, sprite system, YM2610). This curriculum focuses on NEO GEO CD-SPECIFIC aspects: CD-ROM streaming, loading optimization, CD-DA audio, RAM loading strategies.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** CD-ROM access, loading strategies, CD-DA audio, RAM management (7MB!), minimizing load times
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **CD-ROM access patterns** - 1× speed (150KB/s), sector reading, file systems
- **Loading strategies** - Minimizing visible load times (critical on Neo Geo CD!)
- **7MB RAM** - Huge vs cartridge systems! Load everything to RAM
- **CD-DA audio** - Redbook audio tracks (44.1kHz stereo, arcade quality!)
- **Same graphics as Neo Geo** - 380+ sprites, 4096 colors on-screen
- **Same audio chip** - YM2610 ADPCM (15 channels: 7 FM + 4 ADPCM-A + 3 ADPCM-B + 1 SSG)
- **Dual-processor** - 68000 @ 12MHz (main) + Z80 @ 4MHz (sound)
- **Pre-loading** - Load entire games to 7MB RAM (no cartridge instant access!)
- **CDZ (1996)** - 2× CD drive (300KB/s, faster loading!)
- **Memory card** - Save game data (vs expensive cartridge NVRAM)

#### Example Tier 1 Lesson: "Your First CD Load + Sprite"
```asm
; Neo Geo CD Assembly - Lesson 001
; Load sprite data from CD and display
; 68000 @ 12 MHz

;-------------------------------------------------
; 68000 MAIN CODE
;-------------------------------------------------
        .ORG    $00000000

START:  ; Neo Geo CD boot process
        move.w  #$2700,sr       ; Disable interrupts
        move.l  #$100000,sp     ; Set stack

        ; Display "LOADING..." message
        jsr     ShowLoadScreen

        ; Load sprite data from CD to RAM
        lea     CD_FILE_SPRITES,a0
        move.l  #$200000,a1     ; Destination in RAM
        jsr     CD_LoadFile

        ; Load sprite patterns from CD
        lea     CD_FILE_PATTERNS,a0
        move.l  #$400000,a1
        jsr     CD_LoadFile

        ; Hide load screen
        jsr     HideLoadScreen

        ; Now game runs from RAM (like cartridge Neo Geo)
        ; Display sprite
        move.w  #$0050,$400000  ; Sprite X position
        move.w  #$0050,$400002  ; Sprite Y position
        move.w  #$0000,$400004  ; Sprite tile
        move.w  #$000F,$400006  ; Sprite palette

LOOP:   ; Main game loop
        jsr     WaitVBL

        ; Update sprite position
        move.w  $400000,d0
        addq.w  #1,d0           ; Move right
        cmpi.w  #320,d0         ; Check boundary
        blt     .CONT
        moveq   #0,d0           ; Wrap
.CONT:  move.w  d0,$400000

        bra     LOOP

;-------------------------------------------------
; CD-ROM LOADING ROUTINES
;-------------------------------------------------

CD_LoadFile:
        ; Load file from CD to RAM
        ; a0 = filename string
        ; a1 = destination address
        movem.l d0-d7/a0-a6,-(sp)

        ; Open file
        move.l  a0,-(sp)        ; Filename
        move.l  #CD_OPEN,a0
        jsr     (a0)            ; Call BIOS CD_OPEN
        addq.l  #4,sp
        move.l  d0,d7           ; Save file handle

        ; Get file size
        move.l  d7,-(sp)
        move.l  #CD_SIZE,a0
        jsr     (a0)
        addq.l  #4,sp
        move.l  d0,d6           ; File size in bytes

        ; Read file
        move.l  a1,-(sp)        ; Destination
        move.l  d6,-(sp)        ; Size
        move.l  d7,-(sp)        ; Handle
        move.l  #CD_READ,a0
        jsr     (a0)
        add.l   #12,sp

        ; Close file
        move.l  d7,-(sp)
        move.l  #CD_CLOSE,a0
        jsr     (a0)
        addq.l  #4,sp

        movem.l (sp)+,d0-d7/a0-a6
        rts

ShowLoadScreen:
        ; Display "NOW LOADING" screen
        ; (FIX layer text rendering code)
        ; This is CRITICAL for Neo Geo CD!
        rts

HideLoadScreen:
        ; Clear load screen
        rts

WaitVBL:
        ; Wait for vertical blank
        move.w  $3C0006,d0
.WAIT:  move.w  $3C0006,d1
        cmp.w   d0,d1
        beq     .WAIT
        rts

; CD-ROM BIOS function addresses (Neo Geo CD BIOS)
CD_OPEN:        .dc.l   $C00444
CD_CLOSE:       .dc.l   $C00468
CD_READ:        .dc.l   $C0047C
CD_SIZE:        .dc.l   $C00490

; Filenames on CD
CD_FILE_SPRITES:        .dc.b   'SPR.DAT',0
CD_FILE_PATTERNS:       .dc.b   'PAT.DAT',0

;-------------------------------------------------
; Z80 SOUND CODE
;-------------------------------------------------
; (Same as Neo Geo MVS/AES, see Neo Geo curriculum)
; Plus: CD-DA audio track playback
```

**Key teaching moment:** Neo Geo CD has SAME hardware as MVS/AES, but CD-ROM instead of cartridge! MAJOR difference: LONG LOAD TIMES (1× CD = 150KB/s). Solution: Load everything to 7MB RAM first. CD-DA audio is huge advantage (arcade-quality music!). CDZ (1996) has 2× CD (faster). Must show "NOW LOADING" screens (infamous!). Once loaded to RAM, plays exactly like cartridge Neo Geo.

**Tier progression:**
1. CD file loading (BIOS routines, file I/O)
2. Loading screens (critical for user experience!)
3. 7MB RAM management (loading entire games)
4. CD-DA audio playback (Redbook tracks)
5. Sprite display (same as Neo Geo MVS/AES)
6. Background graphics (FIX/SPR system, same as cartridge)
7. YM2610 audio (same as cartridge)
8. Loading optimization (minimize load times!)
9. CDZ detection (2× vs 1× CD drive)
10. Memory card saves (vs expensive cartridge NVRAM)
11. Pre-loading strategies (load during attract mode)
12. Streaming audio (CD-DA during gameplay)
13. Multi-file games (level-based loading)
14. Data compression (faster loading)
15. Polish patterns (hiding load times creatively)
16. Complete Neo Geo CD mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced loading strategies, CD-DA mastery, 7MB RAM utilization, hiding load times, CDZ optimization

#### New Patterns:
- **Streaming strategies** - Load next level while playing current level
- **CD-DA mastery** - Multiple audio tracks, cross-fading
- **7MB pre-loading** - Loading entire fighting games to RAM
- **Loading optimization** - Data organization on CD for fast access
- **CDZ detection** - Games that adapt to 1× vs 2× drive
- **Data compression** - LZ variants for faster loading
- **Attract mode loading** - Pre-load during demo playback
- **Memory card** - Save systems (cheaper than cartridge NVRAM!)
- **Multi-disc games** - Large games across multiple CDs (rare)
- **Same graphics as cartridge** - 380+ sprites, 4096 colors, all loaded to RAM
- **Same audio as cartridge** - YM2610 ADPCM + CD-DA hybrid

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - CDZ (1996, 2× CD drive)
**Focus:** CDZ optimization (2× faster loading!), cross-compatibility (works on both CD and CDZ)

#### Phase 3 Enhancement: Neo Geo CDZ
- **2× CD drive** (1996) - 300KB/s (2× faster than original!)
- **Front-loading** - Different physical design (vs top-loading CD)
- **Backward compatible** - All Neo Geo CD games work
- **Reduced load times** - Still longer than cartridge, but much better
- **Same capabilities** - No new features, just faster loading
- **Adaptive games** - Detect CDZ, load more data to RAM

**Tier 40 Example - CDZ Detection and Optimization:**
```asm
; Detect Neo Geo CD (1×) vs CDZ (2×) and optimize

DetectCDZ:
        ; Test CD drive speed
        move.l  #$10000,d0      ; Test size (64KB)
        move.l  #TestBuffer,a0
        jsr     GetTime         ; Start timer
        move.l  d0,d7           ; Save start time

        ; Load test data
        lea     TestFile,a0
        move.l  #TestBuffer,a1
        jsr     CD_LoadFile

        jsr     GetTime         ; End timer
        sub.l   d7,d0           ; Calculate duration

        ; If < 450ms for 64KB, it's CDZ (2×)
        cmpi.l  #450,d0
        blt     .IS_CDZ

        ; Neo Geo CD (1×)
        move.w  #1,CDSpeed      ; 150KB/s
        bra     .DONE

.IS_CDZ:
        ; Neo Geo CDZ (2×)
        move.w  #2,CDSpeed      ; 300KB/s
        ; Load more data on CDZ (faster!)

.DONE:  rts

OptimizeForSpeed:
        ; Adapt loading strategy based on drive speed
        move.w  CDSpeed,d0
        cmpi.w  #2,d0
        beq     .CDZ

        ; CD (1×) - Aggressive compression, minimal loading
        move.l  #COMPRESS_MAX,CompressionLevel
        bra     .DONE

.CDZ:   ; CDZ (2×) - Less compression, more pre-loading
        move.l  #COMPRESS_MIN,CompressionLevel
        ; Pre-load next 2 levels

.DONE:  rts

CDSpeed:        dc.w    1       ; 1 = CD, 2 = CDZ
TestFile:       dc.b    'TEST.DAT',0
TestBuffer:     ds.b    $10000
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional loading optimization, arcade-perfect conversions (with load screens), complex CD-DA audio, 7MB mastery

#### Advanced Techniques:
- **Arcade conversion mastery** - Converting MVS games to CD (add loading)
- **Loading during gameplay** - Next level loads while playing
- **CD-DA + YM2610 hybrid** - Music on CD-DA, effects on YM2610
- **7MB game architecture** - Entire fighting game in RAM
- **Data compression mastery** - Custom compression for game data
- **CD file system optimization** - Physical sector placement for speed
- **Loading screen art** - Professional "NOW LOADING" designs
- **Memory card systems** - Progress saving, unlockables
- **Multi-language support** - All languages on same CD (vs multiple cartridges!)
- **Attract mode sophistication** - Pre-loading during demos

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Fighting games (Neo Geo CD's strength!), arcade conversions, CD-DA showcase titles

#### Genre Specializations:
- **Fighting games** - King of Fighters, Fatal Fury, Samurai Shodown (CD versions!)
- **Arcade conversions** - MVS arcade games on CD (with load screens)
- **Shoot-em-ups** - Blazing Star, Pulstar (arcade-perfect with loads)
- **Action games** - Metal Slug series (CD versions)
- **Sports games** - Baseball Stars, Soccer (with CD-DA commentary!)
- **Puzzle games** - Puzzle Bobble, Money Idol Exchanger
- **RPGs** - Rare on Neo Geo, but CD-DA music perfect for RPGs
- **Adventure games** - Larger games possible with CD storage

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Minimizing load times, maximum 7MB utilization, advanced CD-DA, hiding loads creatively

#### Limit-Pushing Techniques:
- **Zero-perceived loading** - Loading during transitions, demos
- **7MB optimization** - Entire game + assets in RAM
- **Advanced CD-DA** - Dynamic music, cross-fading, branching
- **CDZ maximum speed** - Utilizing 2× drive fully
- **Compression mastery** - Maximum data in minimum space
- **Creative loading screens** - Mini-games, tips, story (distraction!)
- **Multi-disc epics** - Large games across 2-3 CDs
- **Memory card mastery** - Complex save systems

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial arcade conversions, professional loading optimization, showcase CD-DA audio

#### Commercial Techniques:
- **Arcade-perfect conversions** - MVS games on CD (KOF, Fatal Fury, Metal Slug!)
- **Professional loading** - Fast, unobtrusive load screens
- **CD-DA showcase** - Arcade-quality soundtracks
- **Visual polish** - Same 380+ sprites as MVS
- **Loading screen design** - Beautiful, informative load screens
- **Memory card integration** - Unlockables, progress tracking
- **Attract modes** - Impressive demos (pre-loading during)
- **Multi-language** - All regions on one CD

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, CD burning, emulation

#### Modern Development:
- **NeoRaine / MAME** - Neo Geo CD emulation, debugging
- **Modern 68000 toolchains** - VASM, GCC m68k
- **CD mastering tools** - ISO creation for Neo Geo CD
- **Flash cart + CD** - Development workflows
- **Modern compression** - Better than 1990s tools
- **Community techniques** - Active Neo Geo homebrew scene
- **MVS to CD conversion** - Tools for converting cartridge games
- **ODE (Optical Disc Emulator)** - Flash storage for CD drive

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **CDZ Patterns (Phase 3)** - 50 2× CD optimization
4. **Loading Patterns (Phase 4-5)** - 100 optimization techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Neo Geo CD (1994, 1× CD)**
- 68000 @ 12MHz (main CPU)
- Z80 @ 4MHz (sound CPU)
- 7MB RAM (68KB + 1MB V-RAM + 6MB sprite RAM - HUGE!)
- CD-ROM 1× speed (150KB/s)
- CD-DA audio (Redbook, 44.1kHz stereo)
- YM2610 ADPCM (15 channels: 7 FM + 4 ADPCM-A + 3 ADPCM-B + 1 SSG)
- 380+ sprites (same as MVS/AES!)
- 4096 colors on-screen from 65,536 (same as MVS/AES!)
- Memory card (save data)
- Top-loading CD drive

**Phase 3+: Neo Geo CDZ (1996, 2× CD)**
- All same specs as CD
- 2× CD drive (300KB/s - 2× faster!)
- Front-loading CD drive
- Backward compatible with all CD games

**Phase 7-8: Modern Homebrew**
- CD-R burning (create custom Neo Geo CD games)
- ODE (Optical Disc Emulator)
- Modern development tools (NeoRaine, MAME, VASM)
- Modern compression techniques

## Spiral Learning Example: Fighting Game (Neo Geo CD's Strength!)

**Phase 1 (Tier 1):** Load character data to RAM, display sprite, simple movement. Load screen! (~150 lines assembly)

**Phase 2 (Tier 18):** Load all characters, stages, moves. Fighting game mechanics. CD-DA music! (~600 lines)

**Phase 3 (Tier 36):** CDZ optimization - faster loading on 2× drive. (~900 lines)

**Phase 4 (Tier 44):** Complete fighting game - all modes, arcade-perfect gameplay. Loading during vs screen. (~1500 lines)

**Phase 5 (Tier 50):** Full fighting game - story mode, unlockables (memory card), complex moves. (~2000 lines)

**Phase 6 (Tier 54):** Maximum characters, stages, moves. Creative loading screens. (~2500 lines)

**Phase 7 (Tier 57):** King of Fighters / Fatal Fury quality - arcade-perfect conversion. (~3000 lines)

**Phase 8 (Tier 59):** Modern homebrew - additional characters, modern tools, ODE. (~3000 lines + tooling)

## Key Differences from Other Platforms

1. **Same as Neo Geo MVS/AES** - Identical hardware (68000, Z80, sprite system, YM2610)
2. **CD-ROM Instead of Cartridge** - MAJOR difference: long load times vs instant cartridge access
3. **7MB RAM** - Load entire games to RAM (vs cartridge direct access)
4. **CD-DA Audio** - Arcade-quality music (44.1kHz stereo)
5. **CDZ 2× Drive** - 1996 model, 2× faster loading (still slower than cartridge!)
6. **Cheaper Games** - $50 CD vs $200-300 cartridge (major advantage!)
7. **"NOW LOADING"** - Infamous long load times (up to 56 seconds for KOF '94!)
8. **Memory Card Saves** - Cheaper than cartridge NVRAM
9. **All MVS Games Convertible** - Add load screens, burn to CD
10. **380+ Sprites** - Same as MVS/AES (most sprites of any console!)

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Optimize loading time by 30%")
- Pattern recognition exercises ("Identify the streaming optimization")
- Debugging challenges ("Fix the CD buffer underrun")
- Performance optimization tasks ("Reduce load screen duration")

**Summative Assessment:**
- End of each phase: Complete Neo Geo CD game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, loading optimization, gameplay quality
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working Neo Geo CD game (with load screens!)
- **Phase 2:** Game with optimized loading, CD-DA music
- **Phase 3:** CDZ-optimized game (faster on 2× drive)
- **Phase 4:** Arcade-perfect conversion (MVS game on CD)
- **Phase 5:** Genre-mastery project (fighting/shooter/action)
- **Phase 6:** Technical showcase (minimal loading, maximum gameplay)
- **Phase 7:** Commercial-quality arcade conversion
- **Phase 8:** Modern homebrew with community release (CD-R/ODE)

## Success Criteria

**By Phase 4, learners can:**
- Program 68000 + Z80 assembly fluently (same as MVS/AES)
- Master CD-ROM loading (optimization critical!)
- Implement CD-DA audio (Redbook playback)
- Manage 7MB RAM efficiently (load entire games)
- Minimize load times (CDZ detection, compression, streaming)
- Create loading screens (user experience!)
- Use memory card saves

**By Phase 8, learners can:**
- Develop commercial-quality Neo Geo CD games
- Convert MVS arcade games to CD (add loading)
- Optimize loading to minimum (CDZ maximum speed)
- Work with modern homebrew tools (NeoRaine, MAME, ODE)
- Create CD-Rs for real hardware
- Contribute to Neo Geo homebrew community
- Release and distribute CD-ROM titles

## Resources Required

**Phase 1-2:**
- NeoRaine or MAME emulator (Neo Geo CD support, free)
- VASM or GCC m68k assembler
- Text editor
- Neo Geo CD reference documentation (CD-ROM BIOS, loading)
- Neo Geo MVS/AES reference (sprites, YM2610) - see Neo Geo curriculum

**Phase 3+:**
- CDZ emulation (for 2× CD testing)

**Phase 7-8:**
- CD burning software (ISO creation for Neo Geo CD)
- Neo Geo CD/CDZ hardware (optional)
- ODE (Optical Disc Emulator, modern solution)
- Community resources (Neo Geo forums, homebrew scene)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** Same hardware as Neo Geo MVS/AES (380+ sprites, arcade-perfect!), CD-ROM loading optimization mastery, CD-DA audio, 7MB RAM management, understanding cartridge vs CD-ROM trade-offs, cheaper game distribution, memory card saves, MVS game conversion skills
