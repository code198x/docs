# Sega Dreamcast Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sega Dreamcast (1998-2001) → Sega's final console, ahead of its time
**Approach:** Game-first, pattern library, SH-4 mastery, PowerVR graphics, online gaming pioneer
**Gateway:** Direct to assembly (though C/C++ development standard via official SDK)
**Historical Note:** Sega's final console (1998), Hitachi SH-4 @ 200MHz (32-bit RISC, superscalar!), PowerVR2 GPU (tile-based deferred rendering!), 16MB RAM + 8MB VRAM, GD-ROM drive (1GB discs!), built-in modem (56K, online gaming!), 4 controller ports, VMU (Visual Memory Unit - screen in controller!), ahead of its time, beautiful graphics, online gaming pioneer (SegaNet, Phantasy Star Online!), ~688 games, 10.6M units sold (commercial failure vs PS2), discontinued 2001 after PS2 launch, Sega exited hardware, very active homebrew scene!, historically significant as last Sega console

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sega Dreamcast had no BASIC. Professional development used C/C++ via official Sega Katana SDK. Assembly used for performance-critical code and understanding architecture.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** SH-4 fundamentals, PowerVR2 programming, GD-ROM access, online features, VMU
**Professional Autoload:** From lesson 1, all programs professionally load from GD-ROM

#### Pattern Library Established:
- **SH-4 patterns** - Hitachi SH-4 @ 200MHz (32-bit RISC, superscalar!)
- **PowerVR2** - Tile-based deferred rendering GPU!
- **16MB RAM** - Main system RAM
- **8MB VRAM** - Video RAM
- **GD-ROM** - 1GB GigaByte Disc (12× speed!)
- **Built-in modem** - 56K for online gaming!
- **4 controller ports** - Standard 4-player
- **VMU (Visual Memory Unit)** - Memory card with LCD screen!
- **Sound** - ARM7 @ 2.82MHz, 64 channels
- **640×480** - VGA output support!
- **Hardware lighting** - PowerVR2 features
- **Texture compression** - VQ (Vector Quantization)

#### Example Tier 1 Lesson: "Your First Dreamcast 3D Scene"
```asm
; Sega Dreamcast Assembly - Lesson 001
; 3D scene using SH-4 and PowerVR2
; SH-4 @ 200 MHz

; Hitachi SH-4 architecture (superscalar RISC):
; - 32-bit RISC CPU
; - 16 general-purpose 32-bit registers (R0-R15)
; - 32 floating-point 32/64-bit registers (FR0-FR15/DR0-DR7)
; - Superscalar (2 instructions/cycle possible!)
; - FPU (floating-point unit) built-in
; - On-chip cache (8KB instruction + 16KB data)
; - PowerVR2 does tile-based rendering!

        .sh4                    ; SH-4 mode

        .org    $8C010000       ; Dreamcast RAM base

; Dreamcast memory map
RAM_BASE        = $8C000000     ; Main RAM (16MB)
VRAM_64         = $A5000000     ; VRAM 64-bit access
VRAM_32         = $A4000000     ; VRAM 32-bit access
TA_FIFO         = $10000000     ; Tile Accelerator FIFO
YUV_FIFO        = $10800000     ; YUV converter FIFO
PVR_REG         = $A05F8000     ; PowerVR2 registers

; PowerVR2 registers
PVR_ID          = $A05F8000     ; Chip ID/revision
PVR_RESET       = $A05F8008     ; Reset control
PVR_START_RENDER = $A05F8014    ; Start rendering
PVR_PARAM_BASE  = $A05F8020     ; Parameter base address
PVR_REGION_BASE = $A05F802C     ; Region array base
PVR_TA_OL_BASE  = $A05F8124     ; TA object list base

; System registers
HOLLY_REG       = $A05F6800     ; Holly system controller
MAPLE_DMA       = $A05F6C04     ; Maple DMA (controllers)
G1_ATA          = $A05F7000     ; GD-ROM interface

START:  ; Initialize
        # Set up stack pointer
        mov.l   #$8C100000,r15  # Stack at top of RAM

        # Initialize Dreamcast hardware
        bsr     InitDreamcast
        nop                     # SH-4 delay slot!

        # Initialize PowerVR2
        bsr     InitPowerVR2
        nop

        # Set up video mode (640×480 VGA!)
        bsr     SetVideoMode
        nop

        # Create 3D scene
        bsr     BuildScene
        nop

MAIN_LOOP:
        # Wait for VBlank
        bsr     WaitVBlank
        nop

        # Start new frame on PowerVR2
        # PowerVR uses tile-based deferred rendering!
        bsr     StartFrame
        nop

        # Submit geometry to Tile Accelerator
        bsr     SubmitGeometry
        nop

        # Finish frame (PowerVR sorts and renders)
        bsr     FinishFrame
        nop

        # Read controller via Maple Bus
        # Dreamcast uses Maple Bus for peripherals!
        mov     #0,r4           # Port 0
        bsr     ReadController
        nop
        mov     r0,r8           # Save input

        # Check for online features
        # Dreamcast has built-in 56K modem!
        bsr     CheckModem
        nop

        # Check VMU
        # VMU is memory card with LCD screen!
        bsr     CheckVMU
        nop

        # Check for exit
        mov     #0x0800,r1      # Start button
        tst     r1,r8
        bt      MAIN_LOOP

        # Exit (return to BIOS)
        mov.l   #0x8C000000,r0
        jmp     @r0
        nop

# Initialize Dreamcast
InitDreamcast:
        # Initialize Holly (system controller)
        mov.l   #HOLLY_REG,r1
        mov.l   #0x00000001,r0
        mov.l   r0,@r1

        # Initialize video hardware
        # (Simplified initialization)

        rts
        nop

# Initialize PowerVR2
InitPowerVR2:
        # Reset PowerVR2
        mov.l   #PVR_RESET,r1
        mov.l   #0x00000001,r0
        mov.l   r0,@r1

        # Wait for reset
        mov     #1000,r2
.wait:  dt      r2
        bf      .wait

        # Set up tile accelerator
        mov.l   #PVR_TA_OL_BASE,r1
        mov.l   #$8D000000,r0   # Object list in VRAM
        mov.l   r0,@r1

        # Set parameter base
        mov.l   #PVR_PARAM_BASE,r1
        mov.l   #$8D100000,r0
        mov.l   r0,@r1

        rts
        nop

# Set video mode (640×480 VGA!)
SetVideoMode:
        # Dreamcast supports VGA output!
        # Set up 640×480 progressive scan

        mov.l   #PVR_REG,r1
        mov.l   #0x00160020,r0  # 640×480 mode
        mov.l   r0,@(0x44,r1)

        rts
        nop

# Build scene
BuildScene:
        # Create display list for PowerVR2
        # PowerVR uses tile-based rendering!

        rts
        nop

# Start new frame
StartFrame:
        # Begin new frame on PowerVR2
        mov.l   #PVR_START_RENDER,r1
        mov.l   #0x00000001,r0
        mov.l   r0,@r1

        rts
        nop

# Submit geometry to Tile Accelerator
SubmitGeometry:
        # Send triangles to TA FIFO
        # PowerVR sorts geometry into tiles!

        mov.l   #TA_FIFO,r1

        # Triangle header
        mov.l   #0x80000000,r0  # Polygon type
        mov.l   r0,@r1

        # Vertex 0 (X, Y, Z, U, V, color)
        fmov.s  #160.0,fr0      # X
        fmov.s  #120.0,fr1      # Y
        fmov.s  #1.0,fr2        # Z
        fmov.s  fr0,@r1
        fmov.s  fr1,@r1
        fmov.s  fr2,@r1

        # Vertex 1
        fmov.s  #140.0,fr0
        fmov.s  #180.0,fr1
        fmov.s  #1.0,fr2
        fmov.s  fr0,@r1
        fmov.s  fr1,@r1
        fmov.s  fr2,@r1

        # Vertex 2
        fmov.s  #180.0,fr0
        fmov.s  #180.0,fr1
        fmov.s  #1.0,fr2
        fmov.s  fr0,@r1
        fmov.s  fr1,@r1
        fmov.s  fr2,@r1

        rts
        nop

# Finish frame
FinishFrame:
        # PowerVR2 now renders sorted tiles!
        # Tile-based deferred rendering is efficient!

        rts
        nop

WaitVBlank:
        # Wait for vertical blank
        mov.l   #PVR_REG,r1
.wait:  mov.l   @(0x10,r1),r0
        tst     #0x0008,r0
        bt      .wait
        rts
        nop

# Read controller via Maple Bus
ReadController:
        # $r4 = controller port (0-3)
        # Dreamcast has 4 ports via Maple Bus

        mov.l   #MAPLE_DMA,r1
        mov     r4,r0
        shll2   r0              # Port × 4
        add     r0,r1

        # Request controller data
        mov.l   #0x01000000,r0  # Read controller command
        mov.l   r0,@r1

        # Wait for DMA
        nop
        nop

        # Read button data
        mov.l   @(4,r1),r0      # Button state
        rts
        nop

# Check modem status
CheckModem:
        # Dreamcast has built-in 56K modem!
        # Can connect to SegaNet, play online!

        # (Simplified - real code complex)
        rts
        nop

# Check VMU
CheckVMU:
        # VMU = Visual Memory Unit
        # Memory card with LCD screen in controller!

        # Can display graphics on VMU screen
        # Can run mini-games on VMU when disconnected!

        # (Simplified - VMU programming is separate topic!)
        rts
        nop

# Data
        .align  4
```

**Key teaching moment:** Sega Dreamcast uses SH-4 @ 200MHz - 32-bit RISC, superscalar! PowerVR2 GPU uses tile-based deferred rendering (ahead of its time!). 16MB RAM + 8MB VRAM. GD-ROM (1GB discs!). Built-in 56K modem (online gaming pioneer!). VMU = memory card with LCD screen in controller! 640×480 VGA support! 688 games. 10.6M units (failure vs PS2). Sega's final console. Discontinued 2001. Sega exited hardware. VERY active homebrew scene! Historically significant as last Sega console with innovative features!

**Tier progression:**
1. SH-4 basics (32-bit RISC, superscalar, FPU)
2. PowerVR2 programming (tile-based deferred rendering!)
3. Tile Accelerator (geometry submission)
4. GD-ROM access (1GB disc, 12× speed)
5. 640×480 VGA output (progressive scan!)
6. Maple Bus (controller interface)
7. VMU programming (Visual Memory Unit!)
8. Built-in modem (56K online gaming!)
9. 16MB RAM management
10. 8MB VRAM management
11. Texture compression (VQ - Vector Quantization)
12. Hardware lighting
13. Sound (ARM7, 64 channels)
14. 4-player support
15. Online gaming (SegaNet!)
16. Complete Dreamcast 3D games

### Phase 2-8 Summary:

**Phase 2:** Advanced PowerVR2 techniques, VQ texture compression, online gaming depth, VMU mini-games

**Phase 3:** VGA Box (480p!), Keyboard, Mouse, Broadband Adapter (replacing 56K modem!)

**Phase 4:** Professional SH-4 programming, complex tile-based rendering, online multiplayer mastery

**Phase 5:** Genre specializations - 3D fighters (Soul Calibur!), online RPGs (PSO!), racers (Crazy Taxi!), shooters

**Phase 6:** Maximum Dreamcast performance, PowerVR2 showcase, pushing tile-based rendering

**Phase 7:** Commercial AAA quality - Soul Calibur, Shenmue, Phantasy Star Online level!

**Phase 8:** Modern homebrew - KallistiOS (open-source SDK!), very active DC scene!, CDI burning, indie releases!

## Key Differences from Other Platforms

1. **SH-4 @ 200MHz** - Superscalar RISC, powerful FPU!
2. **PowerVR2** - Tile-based deferred rendering (innovative!)
3. **GD-ROM** - 1GB discs (vs 700MB CD!)
4. **Built-in Modem** - 56K online gaming pioneer!
5. **VMU** - Memory card with LCD screen!
6. **VGA Support** - 640×480 progressive scan!
7. **688 Games** - Great library despite short life
8. **Sega's Last Console** - End of Sega hardware era
9. **Very Active Homebrew** - KallistiOS, indie games!
10. **Ahead of Its Time** - Features PS2/Xbox copied!

---

**Total:** 4,096 lessons | **Time:** 2-4 years
**Unique Advantage:** SH-4 mastery, PowerVR tile-based rendering, online gaming pioneer, VMU programming, Sega's final console study, very active homebrew (KallistiOS!), indie DC releases, innovative features ahead of time!
