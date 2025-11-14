# Nintendo 64 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Nintendo 64 (1996-2002) → Nintendo's powerful 64-bit cartridge console
**Approach:** Game-first, pattern library, MIPS R4300i mastery, RCP (Reality Co-Processor) programming
**Gateway:** Direct to assembly (though C development standard via Nintendo SDK)
**Historical Note:** Nintendo's 64-bit console (1996), MIPS R4300i @ 93.75MHz (64-bit RISC!), cartridge-based (ROM + save RAM), 4MB RAM expandable to 8MB (Expansion Pak), RCP (Reality Co-Processor: RSP + RDP), 3D graphics powerhouse, 320×240/640×480 resolution, 4 controller ports built-in, analog stick innovation, rumble pak, ~390 games, competed with PlayStation/Saturn, third place in sales (~33M units) but iconic games (Super Mario 64, Zelda: Ocarina of Time, GoldenEye 007), cartridge load times = instant, expensive cartridges limited third-party support, discontinued 2002, GameCube successor, N64 homebrew very active!

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Nintendo 64 had no BASIC. Professional development used C via official Nintendo SDK. Assembly used for performance-critical code and understanding architecture.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** MIPS R4300i fundamentals, RCP programming (RSP + RDP), 3D graphics, cartridge optimization
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge (instant!)

#### Pattern Library Established:
- **MIPS R4300i patterns** - MIPS R4300i @ 93.75MHz (64-bit RISC!)
- **RCP (Reality Co-Processor)** - Custom graphics/audio chip
- **RSP (Reality Signal Processor)** - Vector processor for 3D math
- **RDP (Reality Display Processor)** - Rasterizer, texture mapper
- **4MB RAM** - Base memory (expandable to 8MB!)
- **Cartridge-based** - ROM cartridges (4-64MB) + save RAM
- **320×240/640×480** - Standard/hi-res modes
- **4 controller ports** - Built-in 4-player support!
- **Analog stick** - Nintendo's analog innovation
- **Expansion Pak** - 4MB RAM expansion (total 8MB)
- **Transfer Pak** - Game Boy connectivity
- **Rumble Pak** - Controller vibration

#### Example Tier 1 Lesson: "Your First N64 3D Triangle"
```asm
; Nintendo 64 Assembly - Lesson 001
; 3D triangle using RSP and RDP
; MIPS R4300i @ 93.75 MHz

; MIPS R4300i architecture (64-bit RISC):
; - 64-bit RISC CPU
; - 32 general-purpose 64-bit registers ($0-$31)
; - $0 is always zero
; - FPU (floating-point unit) - 32 FP registers!
; - 64-bit operations + 32-bit compatibility mode
; - Delayed branches (1 delay slot!)
; - N64's RCP handles graphics/audio

        .n64                    ; N64 mode

        .org    $80000400       ; N64 RAM base

; N64 memory map
KSEG0           = $80000000     ; Cached kernel segment
KSEG1           = $A0000000     ; Uncached kernel segment
RDRAM           = $00000000     ; RDRAM (4-8MB)
CART_ROM        = $10000000     ; Cartridge ROM
RSP_MEM         = $04000000     ; RSP memory (4KB DMEM + 4KB IMEM)
RSP_REG         = $04040000     ; RSP registers
RDP_REG         = $04100000     ; RDP registers
MI_REG          = $04300000     ; MIPS Interface
VI_REG          = $04400000     ; Video Interface
AI_REG          = $04500000     ; Audio Interface
PI_REG          = $04600000     ; Peripheral Interface (cart)
SI_REG          = $04800000     ; Serial Interface (controllers)

; RDP command registers
DPC_START       = $04100000     ; RDP command start
DPC_END         = $04100004     ; RDP command end
DPC_CURRENT     = $04100008     ; RDP current command
DPC_STATUS      = $0410000C     ; RDP status

; Video Interface registers
VI_STATUS       = $04400000     ; VI status/control
VI_ORIGIN       = $04400004     ; VI framebuffer origin
VI_WIDTH        = $04400008     ; VI framebuffer width
VI_V_INT        = $0440000C     ; VI vertical interrupt

START:  ; Initialize
        # Set up stack pointer
        li      $sp,0x80400000-16 # Stack at top of 4MB RAM

        # Initialize N64 hardware
        jal     InitN64
        nop                     # Delay slot (MIPS!)

        # Initialize RCP (Reality Co-Processor)
        jal     InitRCP
        nop

        # Set up display list
        la      $a0,DISPLAY_LIST
        jal     BuildDisplayList
        nop

MAIN_LOOP:
        # Wait for VBlank
        jal     WaitVBlank
        nop

        # Process RSP (3D transformations)
        # N64's RSP is vector processor for 3D math!
        jal     ProcessRSP
        nop

        # Submit display list to RDP (rasterizer)
        la      $a0,DISPLAY_LIST
        jal     SubmitToRDP
        nop

        # Read controller
        jal     ReadController
        li      $a0,0           # Controller 0
        move    $s0,$v0         # Save input

        # Check for exit
        andi    $t0,$s0,0x1000  # Start button
        beq     $t0,$zero,MAIN_LOOP
        nop

        # Exit (infinite loop - no OS on N64!)
.exit:  b       .exit
        nop

# Initialize N64 hardware
InitN64:
        # Initialize Video Interface
        li      $t0,VI_STATUS
        li      $t1,0x0003      # 16-bit mode, AA off
        sw      $t1,0($t0)

        # Set framebuffer
        li      $t0,VI_ORIGIN
        li      $t1,0x00100000  # Framebuffer at 1MB
        sw      $t1,0($t0)

        # Set width
        li      $t0,VI_WIDTH
        li      $t1,320         # 320 pixels wide
        sw      $t1,0($t0)

        jr      $ra
        nop

# Initialize RCP (Reality Co-Processor)
InitRCP:
        # Initialize RSP (Reality Signal Processor)
        # RSP is vector CPU for 3D math
        li      $t0,RSP_REG
        li      $t1,0x00000001  # Start RSP
        sw      $t1,0($t0)

        # Initialize RDP (Reality Display Processor)
        # RDP is rasterizer/texture mapper
        li      $t0,DPC_STATUS
        li      $t1,0x00000001  # Start RDP
        sw      $t1,0($t0)

        jr      $ra
        nop

# Build display list (RDP commands)
BuildDisplayList:
        # $a0 = display list address
        move    $t0,$a0

        # Fill triangle command
        li      $t1,0x08000000  # Fill triangle (flat shaded)
        sw      $t1,0($t0)
        addiu   $t0,$t0,4

        # Color (red, RGBA5551)
        li      $t1,0xF800FFFF  # Red
        sw      $t1,0($t0)
        addiu   $t0,$t0,4

        # Vertex 0 (X, Y)
        li      $t1,0x00A00078  # X=160, Y=120
        sw      $t1,0($t0)
        addiu   $t0,$t0,4

        # Vertex 1
        li      $t1,0x008C00B4  # X=140, Y=180
        sw      $t1,0($t0)
        addiu   $t0,$t0,4

        # Vertex 2
        li      $t1,0x00B400B4  # X=180, Y=180
        sw      $t1,0($t0)
        addiu   $t0,$t0,4

        # Sync pipe (finish drawing)
        li      $t1,0x29000000
        sw      $t1,0($t0)
        addiu   $t0,$t0,4

        # Sync full (wait for completion)
        li      $t1,0x29000000
        sw      $t1,0($t0)

        jr      $ra
        nop

# Process RSP (3D transformations)
ProcessRSP:
        # Load microcode to RSP IMEM
        # N64's RSP is programmable vector processor!
        # Microcode does matrix transforms, lighting, clipping

        # (Simplified - real code loads full microcode)

        # Start RSP task
        li      $t0,RSP_REG
        li      $t1,0x00000001
        sw      $t1,0($t0)

        jr      $ra
        nop

# Submit display list to RDP
SubmitToRDP:
        # $a0 = display list address

        # Set RDP command start
        li      $t0,DPC_START
        sw      $a0,0($t0)

        # Set RDP command end
        li      $t0,DPC_END
        addiu   $t1,$a0,256     # Display list size
        sw      $t1,0($t0)

        jr      $ra
        nop

WaitVBlank:
        # Wait for vertical blank
        li      $t0,VI_V_INT
.wait:  lw      $t1,0($t0)
        andi    $t1,$t1,0x0200  # VBlank flag
        beq     $t1,$zero,.wait
        nop
        jr      $ra
        nop

ReadController:
        # Read N64 controller
        # $a0 = controller number (0-3)
        # N64 has 4 built-in ports!

        # Send controller command
        li      $t0,SI_REG
        sll     $t1,$a0,4       # Controller offset
        add     $t0,$t0,$t1

        # Request button data
        li      $t1,0x00FF      # Read buttons command
        sw      $t1,0($t0)

        # Wait for response
        nop
        nop
        nop

        # Read button data
        lw      $v0,4($t0)      # Button state

        jr      $ra
        nop

# Data
        .align  8
DISPLAY_LIST:
        .space  512             # RDP display list

# N64 ROM header (required!)
        .org    $00000000
        .word   0x80371240      # PI_BSD_DOM1_LAT
        .word   0x0000000F      # Clock rate
        .word   0x80000400      # Entry point (START)
        .word   0x00001444      # Release offset
        .word   0x00000000      # CRC1
        .word   0x00000000      # CRC2
        .space  8               # Reserved
        .ascii  "N64 GAME        " # Game name (20 chars)
        .space  7               # Reserved
        .ascii  "N"             # Cartridge ID
        .byte   0x00            # Country code
        .byte   0x00            # Version
```

**Key teaching moment:** Nintendo 64 uses MIPS R4300i @ 93.75MHz - 64-bit RISC CPU! RCP (Reality Co-Processor) has RSP (vector processor for 3D math) + RDP (rasterizer/texture mapper). Cartridge-based = instant loading (no CD wait!). 4MB RAM expandable to 8MB (Expansion Pak). 4 controller ports built-in! Analog stick innovation. ~390 games. Competed with PlayStation but third in sales (33M units). ICONIC games: Super Mario 64, Zelda OoT, GoldenEye 007! Expensive cartridges limited third-party support. Discontinued 2002. Very active homebrew scene!

**Tier progression:**
1. MIPS R4300i basics (64-bit RISC, 32 registers, FPU)
2. RCP programming (RSP + RDP)
3. RSP microcode (vector processor, 3D transforms)
4. RDP commands (display lists, rasterization)
5. Cartridge ROM access (instant loading!)
6. 4MB RAM management (expandable to 8MB)
7. Controller input (analog stick + buttons, 4 ports!)
8. Video Interface (320×240/640×480)
9. Audio Interface (sound generation)
10. Expansion Pak detection (4MB → 8MB RAM)
11. Rumble Pak (controller vibration)
12. Transfer Pak (Game Boy connectivity)
13. Texture mapping (RDP hardware)
14. Z-buffering (3D depth)
15. Anti-aliasing (hardware AA)
16. Complete N64 3D games

### Phase 2-8 Summary:

**Phase 2:** Advanced RCP techniques, RSP microcode mastery, texture cache optimization, cartridge banking

**Phase 3:** Expansion Pak (8MB RAM!), Rumble Pak, Transfer Pak, Controller Pak (memory card)

**Phase 4:** Professional 64-bit programming, complex RSP microcode, advanced RDP, 8MB games

**Phase 5:** Genre specializations - 3D platformers (Mario 64!), FPS (GoldenEye!), action-adventure (Zelda!), racing

**Phase 6:** Maximum N64 performance, RSP/RDP showcase, pushing 64-bit limits

**Phase 7:** Commercial AAA quality - Super Mario 64, Zelda OoT, Perfect Dark level!

**Phase 8:** Modern homebrew - libdragon (modern SDK!), N64brew community (very active!), flash carts

## Key Differences from Other Platforms

1. **64-bit RISC CPU** - MIPS R4300i @ 93.75MHz!
2. **RCP Architecture** - RSP (vector) + RDP (rasterizer)
3. **Cartridge-Based** - Instant loading! No CD wait!
4. **4MB → 8MB RAM** - Expansion Pak doubles RAM!
5. **4 Controller Ports** - Built-in 4-player!
6. **Analog Innovation** - First mainstream analog stick
7. **~390 Games** - Smaller library, but ICONIC titles
8. **33M Units** - Third place, but legendary games
9. **Homebrew Active** - libdragon, N64brew community!
10. **Flash Carts** - EverDrive 64, modern development!

---

**Total:** 4,096 lessons | **Time:** 2-4 years
**Unique Advantage:** MIPS 64-bit mastery, RCP (RSP/RDP) programming, microcode development, cartridge optimization, legendary games study (Mario 64, Zelda OoT!), active homebrew (libdragon!), N64brew community!
