# Sega Saturn Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sega Saturn (1994-2000) → Sega's 32-bit dual-CPU powerhouse
**Approach:** Game-first, pattern library, dual SH-2 mastery, complex 2D/3D graphics
**Gateway:** Direct to assembly (though C development common via official SDK)
**Historical Note:** Sega 32-bit console (1994), dual Hitachi SH-2 @ 28.6MHz (two 32-bit RISC CPUs!), CD-ROM based, complex architecture (8 processors total!), 2MB RAM + 1.5MB VRAM, 320×224/640×448 resolution, 16.7M colors, VDP1 (3D sprites) + VDP2 (backgrounds), competed with PlayStation, stronger at 2D than 3D, ~1000 games, successful in Japan (~9.5M units!), less successful in USA/Europe (~18M total worldwide), discontinued 2000, Dreamcast successor, complex but powerful architecture

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sega Saturn had no BASIC. Professional development used C/C++ via official Sega SDK (SGL - Sega Graphics Library). Assembly used for performance-critical code and understanding architecture.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** Dual SH-2 fundamentals, CD-ROM access, VDP1/VDP2 graphics, complex multi-processor coordination
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **Dual SH-2 patterns** - TWO Hitachi SH-2 @ 28.6MHz each (32-bit RISC CPUs!)
- **VDP1** - Video Display Processor 1 (3D sprites, textured quads)
- **VDP2** - Video Display Processor 2 (backgrounds, scrolling, rotation)
- **SCU (System Control Unit)** - DMA, DSP for geometry
- **68EC000** - Sound CPU @ 11.3MHz
- **SCSP** - Sound processor (32 channels PCM + FM synthesis!)
- **CD-ROM** - 2× speed (300KB/s), upgradeable to 4× with cartridge
- **2MB RAM** - Main work RAM
- **1.5MB VRAM** - Video RAM
- **512KB sound RAM** - Audio memory
- **Expansion cartridges** - RAM expansion, video CD, 4× CD

#### Example Tier 1 Lesson: "Your First Saturn Game"
```asm
; Sega Saturn Assembly - Lesson 001
; Dual SH-2 sprite display
; Master SH-2 @ 28.6 MHz, Slave SH-2 @ 28.6 MHz

; Hitachi SH-2 architecture (RISC):
; - 32-bit RISC CPU
; - 16 general-purpose 32-bit registers (R0-R15)
; - Special registers: MACH, MACL, PR, PC, SR
; - Load/store architecture
; - Fast multiply/accumulate (MAC)
; - Saturn has TWO SH-2 CPUs running in parallel!

        .sh2                    ; SH-2 mode

        .org    $06004000       ; Saturn RAM base

; Saturn memory map
WORKRAM_L       = $00200000     ; Low work RAM (1MB)
WORKRAM_H       = $06000000     ; High work RAM (1MB)
VDP1_VRAM       = $05C00000     ; VDP1 VRAM (512KB)
VDP1_FRAMEBUF   = $05C80000     ; VDP1 framebuffer
VDP2_VRAM       = $05E00000     ; VDP2 VRAM (512KB)
VDP2_CRAM       = $05F00000     ; VDP2 color RAM (4KB)
SOUND_RAM       = $05A00000     ; Sound RAM (512KB)
CD_REG          = $05FFFFFC     ; CD-ROM controller

; VDP1 registers (3D sprites, quads)
VDP1_TVMR       = $05D00000     ; TV mode register
VDP1_FBCR       = $05D00002     ; Framebuffer change
VDP1_PTMR       = $05D00004     ; Plot trigger
VDP1_EWDR       = $05D00006     ; Erase/write data
VDP1_EWLR       = $05D00008     ; Erase/write left
VDP1_EWRR       = $05D0000A     ; Erase/write right

; VDP2 registers (backgrounds, scrolling)
VDP2_TVMD       = $05F80000     ; TV mode
VDP2_EXTEN      = $05F80002     ; External sync
VDP2_TVSTAT     = $05F80004     ; TV status
VDP2_VRSIZE     = $05F80006     ; VRAM size
VDP2_RAMCTL     = $05F80070     ; RAM control

START:  ; Initialize (runs on MASTER SH-2)
        ; Set up stack pointer
        mov.l   #$06100000,r15  ; Stack at top of high RAM

        ; Initialize VDP1 (3D sprites)
        mov.l   #VDP1_TVMR,r1
        mov.w   #$0000,r0       ; 320×224 mode
        mov.w   r0,@r1

        ; Initialize VDP2 (backgrounds)
        mov.l   #VDP2_TVMD,r1
        mov.w   #$8000,r0       ; Enable display
        mov.w   r0,@r1

        ; Clear VDP1 VRAM
        mov.l   #VDP1_VRAM,r1
        mov.l   #512*1024,r2    ; 512KB
        mov     #0,r0
.clear1:
        mov.l   r0,@r1
        add     #4,r1
        dt      r2              ; Decrement and test
        bf      .clear1

        ; Start SLAVE SH-2 (parallel processing!)
        bsr     StartSlaveCPU

        ; Load sprite data to VDP1 VRAM
        mov.l   #SPRITE_DATA,r4
        mov.l   #VDP1_VRAM,r5
        mov     #256,r6         ; 256 bytes
.load:  mov.l   @r4+,r0
        mov.l   r0,@r5
        add     #4,r5
        dt      r6
        bf      .load

        ; Set up VDP1 command table (draw sprite)
        mov.l   #VDP1_VRAM+$1000,r1 ; Command table

        ; Command: Textured sprite
        mov.w   #$0004,r0       ; Sprite command
        mov.w   r0,@r1
        add     #2,r1

        ; Position (center)
        mov.w   #160,r0         ; X
        mov.w   r0,@r1
        add     #2,r1
        mov.w   #112,r0         ; Y
        mov.w   r0,@r1
        add     #2,r1

        ; Size
        mov.w   #32,r0          ; Width
        mov.w   r0,@r1
        add     #2,r1
        mov.w   #32,r0          ; Height
        mov.w   r0,@r1

MAIN_LOOP:
        ; Wait for VBlank
        bsr     WaitVBlank

        ; DUAL CPU: Master handles input/logic
        ; Slave handles sound/physics (parallel!)

        ; Read controller
        bsr     ReadController
        mov     r0,r7           ; Save input

        ; Check right
        tst     #$01,r7
        bt      .check_left
        ; Move sprite right (update VDP1 command)
        mov.l   #VDP1_VRAM+$1002,r1
        mov.w   @r1,r0
        add     #1,r0
        cmp/pl  #320,r0
        bf      .update_x
        mov     #0,r0
.update_x:
        mov.w   r0,@r1

.check_left:
        ; (Similar for other directions)

        ; Trigger VDP1 frame draw
        mov.l   #VDP1_FBCR,r1
        mov.w   #$0001,r0       ; Change frame
        mov.w   r0,@r1

        ; SLAVE CPU is processing physics in parallel!

        bra     MAIN_LOOP

; Start slave SH-2 CPU (parallel processing!)
StartSlaveCPU:
        ; Slave CPU entry point
        mov.l   #SLAVE_START,r0
        mov.l   #$06000300,r1   ; Slave start address reg
        mov.l   r0,@r1

        ; Start slave CPU
        mov.l   #$06000310,r1   ; Slave control
        mov.l   #$0001,r0
        mov.l   r0,@r1
        rts
        nop

; Slave CPU code (runs in parallel!)
SLAVE_START:
        ; Slave SH-2 handles sound and physics
        mov.l   #$06080000,r15  ; Slave stack

.slave_loop:
        ; Calculate physics (while master handles graphics!)
        bsr     UpdatePhysics

        ; Send sound commands to 68000 sound CPU
        bsr     UpdateSound

        ; Synchronize with master
        bsr     SyncWithMaster

        bra     .slave_loop

UpdatePhysics:
        ; Physics calculations on slave CPU
        rts
        nop

UpdateSound:
        ; Sound processing on slave CPU
        rts
        nop

SyncWithMaster:
        ; Inter-CPU synchronization
        rts
        nop

WaitVBlank:
        mov.l   #VDP2_TVSTAT,r1
.wait:  mov.w   @r1,r0
        tst     #$0008,r0       ; VBlank flag
        bt      .wait
        rts
        nop

ReadController:
        ; Read Saturn controller
        mov.l   #$05FF8100,r1   ; SMPC controller
        mov.b   @r1,r0
        rts
        nop

; Data
SPRITE_DATA:
        ; 32×32 sprite (16-bit color per pixel)
        .incbin "sprite32x32.bin"

        .align  4
```

**Key teaching moment:** Sega Saturn has TWO SH-2 CPUs @ 28.6MHz EACH running in parallel! Complex architecture with 8 processors total (2× SH-2, 68EC000 sound, SCU DSP, 2× VDP, SCSP, SMPC)! VDP1 for 3D sprites/quads, VDP2 for backgrounds/scrolling. 2MB RAM + 1.5MB VRAM. CD-ROM 2× (upgradeable to 4×). Competed with PlayStation. Stronger at 2D than 3D. ~1000 games. 9.5M in Japan, 18M total. Discontinued 2000. Complex but powerful!

**Tier progression:**
1. SH-2 basics (32-bit RISC, registers, load/store)
2. Dual CPU coordination (master + slave parallel processing!)
3. VDP1 programming (3D sprites, textured quads)
4. VDP2 programming (backgrounds, scrolling, rotation)
5. CD-ROM access (2× speed, file I/O)
6. Controller input (Saturn pad, 8-way + 6 buttons)
7. 68EC000 sound CPU (32-channel SCSP)
8. SCU (DMA, DSP for geometry calculations)
9. 2MB RAM management
10. 1.5MB VRAM management
11. Color RAM (palettes, true color support)
12. Expansion cartridges (RAM, Video CD, 4× CD)
13. Inter-CPU communication (master ↔ slave sync)
14. Multi-processor optimization
15. 2D/3D hybrid graphics
16. Complete Saturn mini-games

### Phase 2-8 Summary:

**Phase 2:** Advanced dual-CPU techniques, VDP1/VDP2 mastery, SCSP audio depth, CD-ROM streaming

**Phase 3:** RAM expansion cartridge, 4× CD-ROM cartridge, Video CD cartridge

**Phase 4:** Professional dual-CPU programming, complex 3D/2D hybrids, multi-processor optimization

**Phase 5:** Genre specializations - 2D fighters (Saturn strength!), 3D games, RPGs, shooters

**Phase 6:** Maximum Saturn performance, dual-CPU showcase, VDP1+VDP2 effects

**Phase 7:** Commercial quality - Virtua Fighter 2, Panzer Dragoon Saga level!

**Phase 8:** Modern homebrew - Jo Engine, GCC SH-2, CD-R burning, active homebrew scene!

## Key Differences from Other Platforms

1. **Dual SH-2 CPUs** - Two 32-bit RISC @ 28.6MHz each!
2. **8 Processors Total** - Complex multi-processor architecture
3. **VDP1 + VDP2** - Separate 3D and 2D processors
4. **2D Powerhouse** - Stronger at 2D than PlayStation
5. **Complex Architecture** - Difficult to program but powerful
6. **~1000 Games** - Large library
7. **Japan Success** - 9.5M units in Japan!
8. **CD-ROM Based** - Expansion cartridges for enhancements
9. **32-Channel Audio** - SCSP with FM synthesis
10. **Active Homebrew** - Jo Engine, modern development!

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** Dual SH-2 mastery (parallel processing!), complex multi-processor coordination, VDP1+VDP2 graphics programming, 2D powerhouse techniques, understanding Saturn's architecture complexity, SH-2 RISC knowledge, active homebrew scene!
