# Apple Pippin Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Apple Pippin (1995-1997) → Apple/Bandai's multimedia console
**Approach:** Game-first, pattern library, PowerPC mastery, Mac OS integration
**Gateway:** Direct to assembly (though C development via Mac SDK was standard)
**Historical Note:** Apple/Bandai joint venture (1995), PowerPC 603 @ 66MHz (full 32-bit RISC!), Mac OS-based (System 7.5.2), CD-ROM only, $599 launch price (extremely expensive!), keyboard + mouse included, built-in modem (internet capable!), 5.8MB RAM, 640×480 resolution, ~80 titles (games + edutainment), Japan-focused (Pippin Atmark), limited US (Pippin @World), ~42,000 units sold (massive commercial failure!), Apple's only game console attempt, discontinued 1997, PowerPC architecture (knowledge transfers to Mac/consoles!)

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Apple Pippin shipped without BASIC. Most commercial development used C via Mac OS SDK (Macintosh Toolbox), but assembly programming possible and powerful for performance. Curriculum begins with assembly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** PowerPC 603 fundamentals, Mac OS integration, CD-ROM access, 640×480 graphics, multimedia capabilities, internet features
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **PowerPC 603 patterns** - IBM/Motorola PowerPC 603 @ 66MHz (32-bit RISC!)
- **Mac OS integration** - System 7.5.2 API (Toolbox, QuickDraw)
- **CD-ROM access** - 4× speed (600KB/s), ISO 9660
- **640×480 graphics** - High resolution, thousands of colors
- **5.8MB RAM** - Large for 1995 (expandable to 128MB!)
- **128KB VRAM** - Dedicated video memory
- **Keyboard + mouse** - Full Mac peripherals
- **Built-in modem** - 14.4K modem (internet capable!)
- **QuickDraw graphics** - Mac graphics API
- **QuickTime video** - Multimedia playback
- **AppleTalk networking** - Network protocols

#### Example Tier 1 Lesson: "Your First PowerPC Sprite"
```asm
; Apple Pippin Assembly - Lesson 001
; Display sprite using PowerPC 603
; PowerPC 603 @ 66 MHz

; PowerPC is modern RISC architecture:
; - 32 general-purpose 32-bit registers (r0-r31)
; - 32 floating-point 64-bit registers (f0-f31)
; - Load/store architecture
; - Big-endian (matches 68K Macs!)
; - Branch prediction
; - Superscalar (2 instructions/cycle possible)

        .ppc                    ; PowerPC mode

        .org    0x00000000

; Mac OS System 7.5.2 integration
; Uses Toolbox for graphics

        .include "MacTypes.h"   ; Mac OS types
        .include "QuickDraw.h"  ; QuickDraw API

; Entry point (called by Mac OS)
main:
        ; Set up stack frame
        stwu    r1,-64(r1)      ; Allocate stack frame
        mflr    r0              ; Get link register
        stw     r0,68(r1)       ; Save return address

        ; Initialize QuickDraw
        bl      InitGraf        ; Initialize graphics
        bl      InitFonts       ; Initialize fonts
        bl      InitWindows     ; Initialize windows

        ; Open main window
        lis     r3,bounds@ha    ; High 16 bits of bounds
        addi    r3,r3,bounds@l  ; Low 16 bits
        lis     r4,title@ha     ; Window title
        addi    r4,r4,title@l
        li      r5,1            ; Visible
        li      r6,0            ; GoAway box
        li      r7,-1           ; In front
        bl      NewWindow       ; Create window
        mr      r31,r3          ; Save window pointer

        ; Set up sprite
        lis     r3,sprite_x@ha
        addi    r3,r3,sprite_x@l
        li      r4,320          ; Center X
        stw     r4,0(r3)
        lis     r3,sprite_y@ha
        addi    r3,r3,sprite_y@l
        li      r4,240          ; Center Y
        stw     r4,0(r3)

game_loop:
        ; Handle events
        lis     r3,event@ha
        addi    r3,r3,event@l
        li      r4,0            ; No wait
        bl      GetNextEvent    ; Get event

        cmpwi   r3,0            ; Any event?
        beq     no_event

        ; Check for mouse down
        lis     r3,event@ha
        addi    r3,r3,event@l
        lhz     r4,0(r3)        ; Event type
        cmpwi   r4,1            ; mouseDown?
        bne     no_event

        ; Move sprite right
        lis     r3,sprite_x@ha
        addi    r3,r3,sprite_x@l
        lwz     r4,0(r3)
        addi    r4,r4,1         ; Increment X
        cmpwi   r4,640
        blt     update_x
        li      r4,0            ; Wrap
update_x:
        stw     r4,0(r3)

no_event:
        ; Draw sprite
        mr      r3,r31          ; Window pointer
        bl      BeginUpdate

        ; Set pen color (QuickDraw)
        lis     r3,color@ha
        addi    r3,r3,color@l
        bl      RGBForeColor

        ; Draw rectangle (sprite)
        lis     r3,sprite_x@ha
        addi    r3,r3,sprite_x@l
        lwz     r4,0(r3)        ; X
        lis     r3,sprite_y@ha
        addi    r3,r3,sprite_y@l
        lwz     r5,0(r3)        ; Y

        addi    r6,r4,32        ; Width
        addi    r7,r5,32        ; Height

        stwu    r1,-16(r1)      ; Allocate Rect
        stw     r5,0(r1)        ; top
        stw     r4,4(r1)        ; left
        stw     r7,8(r1)        ; bottom
        stw     r6,12(r1)       ; right
        mr      r3,r1           ; Rect pointer
        bl      PaintRect       ; Draw
        addi    r1,r1,16        ; Deallocate

        mr      r3,r31
        bl      EndUpdate

        ; Check for quit
        ; (Simplified - real app checks menu, etc.)
        b       game_loop

; Data
bounds:         .long   50,50,400,600   ; Window bounds
title:          .string "Pippin Sprite"
sprite_x:       .long   320
sprite_y:       .long   240
color:          .short  65535,0,0       ; RGB red
event:          .space  16              ; EventRecord

        .align  4
```

**Key teaching moment:** Apple Pippin uses PowerPC 603 - full 32-bit RISC architecture! Knowledge transfers to Power Macs, GameCube, Wii, Xbox 360, PS3! Mac OS System 7.5.2 integration (QuickDraw, Toolbox). $599 price (extremely expensive!). Keyboard + mouse included. Built-in 14.4K modem (internet capable in 1995!). Apple/Bandai joint venture. Only ~42,000 units sold (massive failure). ~80 titles (games + edutainment). Japan-focused (Pippin Atmark). Apple's only game console. Discontinued 1997.

**Tier progression:**
1. PowerPC basics (32-bit RISC, 32 GPRs, load/store)
2. Mac OS integration (Toolbox, System 7.5.2 API)
3. QuickDraw graphics (Mac drawing API)
4. CD-ROM access (4× drive, ISO 9660)
5. Keyboard input (Mac keyboard events)
6. Mouse input (Mac mouse events, GUI)
7. QuickTime video (multimedia playback)
8. Audio (Mac Sound Manager)
9. 640×480 graphics (high resolution)
10. Color management (Mac Color Manager)
11. File I/O (Mac File Manager)
12. Modem access (built-in 14.4K modem!)
13. AppleTalk networking (LAN gaming)
14. Memory management (5.8MB RAM)
15. Resource forks (Mac resource system)
16. Complete Pippin mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced PowerPC techniques, Mac OS mastery, multimedia applications, internet features

#### New Patterns:
- **PowerPC optimization** - Superscalar execution, branch hints
- **Mac OS mastery** - Deep Toolbox integration
- **QuickDraw 3D** - 3D graphics (advanced Pippin titles)
- **QuickTime mastery** - Video codecs, streaming
- **Sound Manager** - Multi-channel audio mixing
- **CD-ROM streaming** - Continuous loading from 4× drive
- **Internet applications** - Modem-based online features
- **AppleTalk gaming** - LAN multiplayer
- **Resource Manager** - Mac resource forks
- **File Manager** - Sophisticated file I/O
- **Mouse-driven UI** - Mac-style interfaces
- **Keyboard shortcuts** - Mac UI conventions

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Pippin @World (US version) and expansions
**Focus:** US market version, RAM expansion, peripheral support

#### Phase 3 Enhancement: Pippin @World + Expansions
- **Pippin @World** (1996, USA) - US market version by Bandai
- **Pippin Atmark** (1995, Japan) - Original Japanese version
- **RAM expansion** - Up to 128MB possible (rarely used)
- **PRAM** - Parameter RAM for settings
- **Floppy drive** - Optional external drive
- **LocalTalk** - AppleTalk networking peripheral
- **Same software** - All Pippin titles work on both variants

**Tier 40 Example - Detect Pippin Variant:**
```asm
; Detect Pippin Atmark (Japan) vs @World (USA)

DetectVariant:
        ; Check ROM version and regional settings
        stwu    r1,-64(r1)      ; Stack frame
        mflr    r0
        stw     r0,68(r1)

        ; Get system version
        lis     r3,0x0000
        ori     r3,r3,0x0000    ; SysVersion address
        lwz     r3,0(r3)        ; Load version

        ; Check international resources
        li      r3,0            ; verUS
        bl      GetResource     ; Get resource
        cmpwi   r3,0
        beq     is_atmark       ; No US resources = Atmark

is_world:
        ; Pippin @World (USA)
        lis     r3,variant@ha
        addi    r3,r3,variant@l
        li      r4,1            ; @World
        stw     r4,0(r3)
        b       done

is_atmark:
        ; Pippin Atmark (Japan)
        lis     r3,variant@ha
        addi    r3,r3,variant@l
        li      r4,0            ; Atmark
        stw     r4,0(r3)

done:
        lwz     r0,68(r1)
        mtlr    r0
        addi    r1,r1,64
        blr

variant:        .long   0       ; 0=Atmark, 1=@World
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional PowerPC programming, Mac OS proficiency, multimedia mastery, internet applications

#### Advanced Techniques:
- **PowerPC mastery** - Branch prediction, superscalar optimization
- **Mac Toolbox depth** - Advanced API usage
- **QuickDraw 3D mastery** - Complex 3D rendering
- **QuickTime production** - Video compression, editing
- **Sound synthesis** - Advanced audio generation
- **CD-ROM optimization** - Efficient streaming from 4× drive
- **Internet protocols** - TCP/IP over built-in modem
- **LAN gaming** - AppleTalk multiplayer protocols
- **RAM management** - Using 5.8MB-128MB efficiently
- **Resource optimization** - Mac resource fork mastery
- **GUI design** - Professional Mac interfaces
- **Edutainment** - Educational software (Pippin strength!)

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games, edutainment, internet applications, multimedia (Pippin's intended market!)

#### Genre Specializations:
- **Edutainment software** - Educational games (Pippin focus!)
- **Internet applications** - Web browsers, online services
- **Multimedia encyclopedias** - CD-ROM reference works
- **Adventure games** - Point-and-click with mouse
- **Puzzle games** - Mouse-driven puzzles
- **Board games** - Digital adaptations
- **Children's software** - Age-appropriate games
- **Music applications** - MIDI, audio creation

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum PowerPC performance, multimedia mastery, internet features

#### Limit-Pushing Techniques:
- **PowerPC optimization** - Cycle-perfect code
- **QuickDraw 3D maximum** - Complex 3D scenes
- **CD-ROM streaming mastery** - Zero-load continuous streaming
- **128MB RAM utilization** - Large-scale applications
- **Sound Manager showcase** - Complex audio mixing
- **QuickTime showcase** - Full-screen video
- **Internet complexity** - Advanced online features
- **AppleTalk networking** - Complex multiplayer

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial multimedia applications, professional edutainment, internet services

#### Commercial Techniques:
- **Commercial edutainment** - Professional educational software
- **Multimedia production** - High-quality CD-ROM titles
- **Internet services** - Online content delivery
- **Interactive encyclopedias** - Comprehensive references
- **Professional graphics** - High-resolution art
- **Complex audio** - Multi-channel compositions
- **Mac polish** - Professional Mac UI/UX
- **CD-ROM production** - Multi-disc applications

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, emulation

#### Modern Development:
- **MAME emulation** - Pippin emulation support
- **Modern PowerPC toolchains** - GCC PowerPC, modern assemblers
- **Mac OS emulation** - Running System 7.5.2 in emulators
- **CD-ROM mastering** - Burning Pippin CD-Rs
- **Modern multimedia tools** - Video/audio encoding for QuickTime
- **Community techniques** - Pippin preservation scene
- **Cross-platform PowerPC** - Knowledge transfers (GameCube, Wii, PS3!)
- **ODE solutions** - Flash storage for CD drive

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 Mac OS + multimedia techniques
3. **Expansion Patterns (Phase 3)** - 50 @World + RAM expansion
4. **Optimization Patterns (Phase 4-5)** - 100 PowerPC + Mac OS
5. **Genre Patterns (Phase 5-6)** - 150 edutainment/multimedia/internet
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Apple Pippin (1995)**
- PowerPC 603 @ 66MHz (32-bit RISC!)
- 5.8MB RAM (6MB total with PRAM)
- 128KB VRAM
- CD-ROM 4× speed (600KB/s)
- 640×480 resolution, thousands of colors
- Mac OS System 7.5.2
- QuickDraw graphics API
- QuickTime multimedia
- Sound Manager audio
- Keyboard + mouse (Mac peripherals)
- Built-in 14.4K modem (internet!)
- AppleTalk networking
- $599 launch price

**Phase 3+: Pippin @World (1996) + Expansions**
- Same CPU/speed
- RAM expandable to 128MB
- Floppy drive support
- US market version
- Compatible with Atmark software

**Phase 7-8: Modern Homebrew**
- CD-R burning (create custom Pippin discs)
- ODE (Optical Disc Emulator)
- Modern development tools (MAME, GCC PowerPC)
- Mac OS emulators

## Spiral Learning Example: Educational Software (Pippin's Intended Market!)

**Phase 1 (Tier 16):** Simple educational app, Mac UI, text + images. (~400 lines)

**Phase 2 (Tier 32):** Interactive lessons, QuickTime video, Sound Manager audio. (~1000 lines)

**Phase 3 (Tier 40):** Advanced app using 128MB RAM expansion. (~1500 lines)

**Phase 4 (Tier 48):** Comprehensive learning suite, progress tracking, internet updates. (~2200 lines)

**Phase 5 (Tier 50):** Full educational platform - many subjects, multimedia. (~3000 lines)

**Phase 6 (Tier 54):** Maximum multimedia, QuickDraw 3D, QuickTime showcase. (~3800 lines)

**Phase 7 (Tier 57):** Professional edutainment - commercial quality. (~4500 lines)

**Phase 8 (Tier 59):** Modern homebrew - updated content, modern tools. (~4500 lines + tooling)

## Key Differences from Other Platforms

1. **PowerPC 603 32-bit RISC** - Knowledge transfers to many platforms!
2. **Apple/Bandai Joint Venture** - Unusual partnership
3. **Mac OS Based** - System 7.5.2 (full Mac OS!)
4. **$599 Launch** - Extremely expensive!
5. **Keyboard + Mouse** - Full Mac peripherals
6. **Built-in Modem** - Internet capable (1995!)
7. **Edutainment Focus** - Education + entertainment market
8. **~42,000 Units** - Massive commercial failure
9. **~80 Titles** - Very small library
10. **Apple's Only Console** - Never tried again

## Success Criteria

**By Phase 4, learners can:**
- Write PowerPC assembly fluently (32-bit RISC)
- Master Mac OS Toolbox integration
- Program QuickDraw graphics
- Use QuickTime multimedia
- Program Sound Manager audio
- Access CD-ROM efficiently (4× drive)
- Create Mac-style interfaces
- Implement internet features (modem)

**By Phase 8, learners can:**
- Develop commercial-quality Pippin applications
- Master PowerPC architecture (transfers to GameCube, Wii, PS3!)
- Work with modern homebrew tools (MAME)
- Create professional multimedia software
- Contribute to Pippin preservation
- Release custom CD-ROM titles

## Resources Required

**Phase 1-2:**
- MAME emulator (Pippin support)
- GCC PowerPC or assembler
- Text editor
- Apple Pippin reference documentation
- Mac OS System 7.5.2 documentation

**Phase 7-8:**
- CD burning software
- Apple Pippin hardware (optional, very rare!)
- ODE (Optical Disc Emulator)
- Modern multimedia tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** PowerPC 32-bit RISC mastery (transfers to GameCube, Wii, Xbox 360, PS3!), Mac OS programming, multimedia applications, edutainment development, understanding Apple's console attempt, rare architecture study, internet-capable console programming (1995!)
