# Sony PlayStation Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sony PlayStation (1994-2006) → The console that changed gaming
**Approach:** Game-first, pattern library, MIPS R3000A mastery, 3D graphics revolution
**Gateway:** Direct to assembly (though C/C++ development standard via official SDK)
**Historical Note:** Sony's first console (1994), MIPS R3000A @ 33.87MHz (32-bit RISC), CD-ROM based, 2MB RAM + 1MB VRAM, GPU with geometry engine, 3D revolution (polygons!), 320×240/640×480 resolution, 16.7M colors, competed with Saturn/N64, DOMINATED market (~102M units sold!), huge game library (3000+ games!), iconic franchises (Final Fantasy VII, Metal Gear Solid, Crash Bandicoot, Gran Turismo), affordable CD-ROM games, third-party developer friendly, Sony entered and won console war, PlayStation 2 backward compatible, discontinued 2006, historically pivotal console

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sony PlayStation had no BASIC. Professional development used C/C++ via official Sony SDK (Psy-Q). Assembly used for performance-critical code and understanding architecture.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** MIPS R3000A fundamentals, GPU programming, GTE (geometry), CD-ROM access, 3D graphics
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **MIPS R3000A patterns** - MIPS R3000A @ 33.87MHz (32-bit RISC!)
- **GPU** - Graphics Processing Unit with command buffer
- **GTE** - Geometry Transformation Engine (3D math co-processor!)
- **SPU** - Sound Processing Unit (24 channels ADPCM)
- **MDEC** - Motion Decoder (FMV decompression)
- **CD-ROM** - 2× speed (300KB/s, double-speed)
- **2MB RAM** - Main work RAM
- **1MB VRAM** - Video RAM
- **512KB sound RAM** - Audio memory
- **320×240/640×480** - Standard/high-res modes
- **Texture mapping** - Hardware texture support!
- **Gouraud shading** - Smooth polygon shading

#### Example Tier 1 Lesson: "Your First PlayStation 3D Triangle"
```asm
; Sony PlayStation Assembly - Lesson 001
; 3D triangle using GTE and GPU
; MIPS R3000A @ 33.87 MHz

; MIPS R3000A architecture (RISC):
; - 32-bit RISC CPU
; - 32 general-purpose 32-bit registers ($0-$31)
; - $0 is always zero
; - Load/store architecture
; - Delayed branches (1 delay slot!)
; - No hardware multiply/divide in pipeline
; - PlayStation's GTE does 3D math!

        .psx                    ; PlayStation mode

        .org    $80010000       ; PlayStation RAM base

; PlayStation memory map
KUSEG           = $00000000     ; User segment (2GB)
KSEG0           = $80000000     ; Kernel cached (512MB)
KSEG1           = $A0000000     ; Kernel uncached (512MB)
RAM_BASE        = $80000000     ; Main RAM (2MB)
SCRATCHPAD      = $1F800000     ; Fast scratchpad (1KB)
IO_BASE         = $1F801000     ; I/O ports

; GPU registers
GPU_GP0         = $1F801810     ; GPU command/data
GPU_GP1         = $1F801814     ; GPU status/control
GPU_STATUS      = $1F801814     ; GPU status read

; GTE (Geometry Transformation Engine) registers
GTE_VXY0        = $00000000     ; Vertex 0 X,Y
GTE_VZ0         = $00000004     ; Vertex 0 Z
GTE_RGB         = $00000006     ; RGB color
GTE_OTZ         = $00000007     ; Order table Z
GTE_IR0         = $00000008     ; Intermediate result
GTE_SXYP        = $0000000E     ; Screen XY FIFO

; SPU (Sound Processing Unit)
SPU_MAIN_VOL_L  = $1F801D80     ; Main volume left
SPU_MAIN_VOL_R  = $1F801D82     ; Main volume right

START:  ; Initialize
        # Set up stack pointer
        li      $sp,0x801FFF00  # Stack at top of RAM

        # Initialize GPU
        jal     InitGPU
        nop                     # Delay slot (MIPS!)

        # Initialize GTE (geometry engine)
        jal     InitGTE
        nop

        # Clear VRAM
        jal     ClearVRAM
        nop

        # Set up display/draw environments
        jal     InitDisplay
        nop

MAIN_LOOP:
        # Wait for VBlank
        jal     WaitVBlank
        nop

        # Clear ordering table (Z-sorting)
        la      $a0,OT_BASE
        li      $a1,1024        # OT size
        jal     ClearOT
        nop

        # Draw 3D triangle using GTE + GPU

        # Load vertices to GTE
        la      $t0,TRIANGLE_VERTS

        # Vertex 0
        lw      $t1,0($t0)      # X,Y
        mtc2    $t1,$0          # Move to GTE VXY0
        lw      $t1,4($t0)      # Z
        mtc2    $t1,$1          # Move to GTE VZ0

        # Vertex 1
        lw      $t1,8($t0)
        mtc2    $t1,$2          # VXY1
        lw      $t1,12($t0)
        mtc2    $t1,$3          # VZ1

        # Vertex 2
        lw      $t1,16($t0)
        mtc2    $t1,$4          # VXY2
        lw      $t1,20($t0)
        mtc2    $t1,$5          # VZ2

        # Execute GTE transformation
        nop                     # GTE needs time
        cop2    0x0180001       # RTPT (perspective transform)
        nop
        nop

        # Read transformed vertices from GTE
        mfc2    $t0,$14         # Read SXYP (screen coords)

        # Build GPU command (flat-shaded triangle)
        li      $t1,0x20FF0000  # Command: flat triangle, red
        sw      $t1,GPU_PACKET

        # Vertex 0 screen coords
        mfc2    $t2,$12         # SXY0
        sw      $t2,GPU_PACKET+4

        # Vertex 1
        mfc2    $t2,$13         # SXY1
        sw      $t2,GPU_PACKET+8

        # Vertex 2
        mfc2    $t2,$14         # SXY2
        sw      $t2,GPU_PACKET+12

        # Send to GPU
        la      $a0,GPU_PACKET
        jal     SendGPUPacket
        nop

        # Draw ordering table
        la      $a0,OT_BASE
        jal     DrawOT
        nop

        # Read controller
        jal     ReadController
        nop
        move    $s0,$v0         # Save input

        # Check for exit
        andi    $t0,$s0,0x8000  # Start button
        beq     $t0,$zero,MAIN_LOOP
        nop

        # Exit (return to BIOS)
        li      $v0,0xA0
        syscall
        nop

# Initialize GPU
InitGPU:
        # Reset GPU
        li      $t0,0x00000000
        sw      $t0,GPU_GP1

        # Display enable
        li      $t0,0x03000000
        sw      $t0,GPU_GP1

        # Set display area
        li      $t0,0x05000000  # X=0, Y=0
        sw      $t0,GPU_GP1

        jr      $ra
        nop

# Initialize GTE
InitGTE:
        # Set up projection matrix
        # (Simplified - real code loads full matrix)

        # Screen offset
        li      $t0,160         # X offset (center)
        li      $t1,120         # Y offset (center)
        mtc2    $t0,$24         # OFX
        mtc2    $t1,$25         # OFY

        # Projection distance
        li      $t0,320         # H (projection plane distance)
        mtc2    $t0,$26

        jr      $ra
        nop

# Clear VRAM
ClearVRAM:
        # Fill VRAM with black
        li      $t0,0x02000000  # VRAM fill command
        sw      $t0,GPU_GP0

        li      $t0,0x00000000  # Top-left (0,0)
        sw      $t0,GPU_GP0

        li      $t0,0x03FF01FF  # Size (1024×512)
        sw      $t0,GPU_GP0

        jr      $ra
        nop

InitDisplay:
        # Set up 320×240 display
        li      $t0,0x08000001  # 320×240, 15-bit mode
        sw      $t0,GPU_GP1

        jr      $ra
        nop

WaitVBlank:
        li      $t0,GPU_STATUS
.wait:  lw      $t1,0($t0)
        andi    $t1,$t1,0x80000000 # VBlank flag
        beq     $t1,$zero,.wait
        nop
        jr      $ra
        nop

ClearOT:
        # Clear ordering table for Z-sorting
        # $a0 = OT base, $a1 = size
.loop:  sw      $zero,0($a0)
        addiu   $a0,$a0,4
        addiu   $a1,$a1,-1
        bne     $a1,$zero,.loop
        nop
        jr      $ra
        nop

SendGPUPacket:
        # Send packet to GPU
        # $a0 = packet address
        lw      $t0,0($a0)
        sw      $t0,GPU_GP0
        lw      $t0,4($a0)
        sw      $t0,GPU_GP0
        lw      $t0,8($a0)
        sw      $t0,GPU_GP0
        lw      $t0,12($a0)
        sw      $t0,GPU_GP0
        jr      $ra
        nop

DrawOT:
        # Draw ordering table
        # (Simplified - real code processes linked list)
        jr      $ra
        nop

ReadController:
        # Read PlayStation controller
        li      $t0,0x1F801040  # Controller port
        lw      $v0,0($t0)
        jr      $ra
        nop

# Data
        .align  4
TRIANGLE_VERTS:
        # 3D vertices (X,Y,Z)
        .word   -50,-50,200     # Vertex 0
        .word   50,-50,200      # Vertex 1
        .word   0,50,200        # Vertex 2

GPU_PACKET:
        .space  16              # GPU command packet

OT_BASE:
        .space  4096            # Ordering table (1024 entries)
```

**Key teaching moment:** Sony PlayStation uses MIPS R3000A @ 33.87MHz - 32-bit RISC CPU! GTE (Geometry Transformation Engine) does 3D math (matrix transforms, perspective!). GPU does texture mapping, Gouraud shading, polygons! CD-ROM 2× speed. 2MB RAM + 1MB VRAM. 3D revolution - polygons became mainstream! Dominated market with 102 MILLION units sold! 3000+ games! Final Fantasy VII, Metal Gear Solid, Crash, Gran Turismo! Affordable CD games. Third-party friendly. Sony entered and WON console war! PS2 backward compatible. Discontinued 2006. PIVOTAL console in gaming history!

**Tier progression:**
1. MIPS R3000A basics (32-bit RISC, 32 registers, delayed branches!)
2. GPU programming (command buffer, primitives)
3. GTE usage (3D transforms, perspective projection!)
4. Texture mapping (hardware texture support)
5. Gouraud shading (smooth polygon shading)
6. Ordering tables (Z-sorting for 3D)
7. CD-ROM access (2× speed, file I/O)
8. Controller input (PlayStation pad, 8-way + 4 face + 4 shoulder)
9. SPU audio (24-channel ADPCM)
10. MDEC (FMV video decompression)
11. 2MB RAM management
12. 1MB VRAM management
13. Double buffering (smooth animation)
14. 3D game techniques
15. CD-ROM streaming
16. Complete PlayStation 3D games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 3D techniques, texture mapping mastery, CD-ROM streaming, SPU audio depth

#### New Patterns:
- **GTE mastery** - Complex 3D transformations, lighting
- **GPU optimization** - Efficient command lists
- **Texture mapping mastery** - UV coordinates, texture pages
- **Z-sorting** - Ordering table optimization
- **Gouraud shading depth** - Lighting models
- **CD-ROM streaming** - Continuous loading while playing
- **SPU mastery** - 24-channel mixing, reverb, ADPCM
- **MDEC usage** - FMV cutscenes
- **Double/triple buffering** - Smooth 30/60 FPS
- **Memory card** - Save game data
- **Multitap** - 4-player support
- **Link cable** - 2-console multiplayer

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Dual Analog/DualShock controllers
**Focus:** Analog sticks, rumble (DualShock), pressure-sensitive buttons

#### Phase 3 Enhancement: DualShock Controller (1997)
- **Dual Analog** (1997) - Two analog sticks!
- **DualShock** (1997) - Analog + vibration motors!
- **Rumble feedback** - Haptic vibration
- **Analog precision** - Fine 3D movement control
- **Pressure-sensitive** - DualShock 2 (PS2, backward compatible)

**Tier 40 Example - DualShock Rumble:**
```asm
# Detect and use DualShock rumble

CheckDualShock:
        # Check controller type
        li      $t0,0x1F801040
        lw      $t1,0($t0)
        andi    $t1,$t1,0xFF00
        li      $t2,0x7300      # DualShock ID
        beq     $t1,$t2,has_dualshock
        nop

        # No DualShock
        li      $v0,0
        jr      $ra
        nop

has_dualshock:
        # DualShock present!
        li      $v0,1
        jr      $ra
        nop

SetRumble:
        # Enable rumble motors
        # $a0 = small motor (0-255)
        # $a1 = large motor (0-255)
        li      $t0,0x1F801044  # Rumble control
        sb      $a0,0($t0)      # Small motor
        sb      $a1,1($t0)      # Large motor
        jr      $ra
        nop
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional 3D programming, complex scenes, PS1 style mastery

#### Advanced Techniques:
- **MIPS optimization** - Cycle-perfect code, cache usage
- **GTE depth** - Complex lighting, multiple matrices
- **GPU mastery** - Efficient primitive submission
- **Texture compression** - Fitting textures in 1MB VRAM
- **Z-fighting solutions** - Precision issues workarounds
- **CD-ROM buffering** - Multi-track streaming
- **SPU reverb** - Environmental audio
- **MDEC optimization** - Efficient FMV playback
- **Memory optimization** - Fitting games in 2MB RAM
- **DualShock integration** - Analog + rumble

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** 3D action, RPGs, racers, fighters (PlayStation strengths!)

#### Genre Specializations:
- **3D action/adventure** - Crash Bandicoot, Tomb Raider
- **JRPGs** - Final Fantasy VII, Chrono Cross
- **Racing games** - Gran Turismo, Ridge Racer
- **Stealth action** - Metal Gear Solid
- **Fighting games** - Tekken 3, Soul Blade
- **Horror** - Resident Evil, Silent Hill
- **Platformers** - Spyro, Jak and Daxter
- **Sports** - FIFA, Tony Hawk's Pro Skater

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing PS1 boundaries
**Focus:** Maximum 3D performance, PS1 aesthetic mastery

#### Limit-Pushing Techniques:
- **GTE maximum** - Complex transformations per frame
- **GPU showcase** - Maximum polygons (100K+/frame!)
- **Texture streaming** - Dynamic texture loading
- **Z-sorting mastery** - Complex scene ordering
- **CD-ROM mastery** - Zero-load continuous streaming
- **SPU showcase** - All 24 channels + reverb
- **Memory efficiency** - Maximum game in 2MB
- **PS1 aesthetic** - Embracing texture warping, polygon jitter!

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** AAA PlayStation games - FF VII, MGS, Gran Turismo level!

#### Commercial Techniques:
- **Commercial quality** - Final Fantasy VII level!
- **3D mastery** - Complex detailed scenes
- **FMV integration** - Seamless cutscenes
- **Audio excellence** - CD-quality music + effects
- **DualShock polish** - Perfect analog + rumble
- **Multi-disc epics** - 3-4 CD games
- **Professional optimization** - Smooth 30 FPS minimum
- **PS1 aesthetic perfection** - Beautiful despite warping/jitter

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s PlayStation homebrew, modern tools

#### Modern Development:
- **PSn00bSDK** - Modern open-source PS1 SDK!
- **MAME/Mednafen** - PS1 emulation
- **Modern MIPS toolchains** - GCC MIPS, modern assemblers
- **CD-R burning** - Create PS1 discs (mod chip/FreePSXBoot)
- **Modern debugging** - No$PSX debugger
- **Active homebrew scene** - Very active PS1 community!
- **MIPS knowledge** - Transfers to PS2, PSP, N64!

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 3D fundamentals
2. **Advanced Patterns (Phase 2)** - 75 GTE + GPU mastery
3. **DualShock Patterns (Phase 3)** - 50 analog + rumble
4. **Professional Patterns (Phase 4-5)** - 100 MIPS + 3D depth
5. **Genre Patterns (Phase 5-6)** - 150 game-specific 3D
6. **Polish Patterns (Phase 7)** - 75 AAA techniques
7. **Modern Patterns (Phase 8)** - 50 contemporary homebrew

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Sony PlayStation (1994)**
- MIPS R3000A @ 33.87MHz (32-bit RISC!)
- 2MB RAM
- 1MB VRAM
- 512KB sound RAM
- GPU (Graphics Processing Unit)
- GTE (Geometry Transformation Engine - 3D math!)
- SPU (24-channel ADPCM audio)
- MDEC (Motion Decoder - FMV)
- CD-ROM 2× speed (300KB/s)
- 320×240/640×480 resolution
- 16.7M colors (24-bit true color!)
- Texture mapping hardware
- Gouraud shading
- Z-sorting support

**Phase 3+: DualShock Controller (1997)**
- Dual analog sticks
- Vibration motors (rumble!)
- Pressure-sensitive buttons
- Ergonomic design

**Phase 7-8: Modern Homebrew**
- PSn00bSDK (modern open-source SDK!)
- CD-R burning
- FreePSXBoot (no mod chip needed!)
- Very active homebrew scene
- Modern MIPS tools

## Success Criteria

**By Phase 4:** MIPS assembly fluency, GTE 3D transforms, GPU programming, texture mapping, Z-sorting, CD-ROM streaming, 24-channel audio, DualShock support

**By Phase 8:** Commercial AAA PS1 games, MIPS mastery, modern homebrew (PSn00bSDK!), active community contribution, PS1 game releases

## Resources

**Phase 1-2:** MAME/Mednafen emulator, PSn00bSDK, GCC MIPS, PS1 docs

**Phase 7-8:** CD-R burner, PS1 hardware (mod chip/FreePSXBoot), modern tools, active community

---

**Total:** 4,096 lessons | **Time:** 2-4 years
**Unique Advantage:** MIPS mastery, GTE 3D math, 3D revolution study, PS1 dominated generation (102M units!), active homebrew scene, PSn00bSDK modern development, iconic games study!
