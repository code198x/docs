# Phase 1 Breakdown: Amiga Signal

**Game:** Signal (Game 1)
**Phase:** 1 of 8 (128-unit structure)
**Units:** 1-16
**Theme:** Custom Chip Fundamentals + First Display

---

## Phase 1 Overview

The Amiga is challenging to start because:
- Three custom chips working together (Agnus, Denise, Paula)
- Copper coprocessor required for display
- Bitplane graphics (not chunky pixels)
- Memory must be in "chip RAM" for custom chips to access
- Bootable disk creation required to run code

By the end of Phase 1, learners will:
- Have a colourful display under Copper control
- Understand the display DMA pipeline
- Know how bitplanes create colours
- Be able to diagnose "black screen" and "corrupted display" problems

**Phase 1 Output:** Animated colour bars filling the screen, controlled by Copper and responding to joystick input.

---

## Unit Progression

### Unit 1: Your First Copper Bars
**Time:** 45 minutes
**Builds on:** Nothing — this is the start

**What happens:**
- Type complete working program
- Build with vasm, create bootable ADF
- See horizontal colour bars on screen

**Key code (complete, runnable):**
```asm
; Signal - Unit 1
; Assemble: vasmm68k_mot -Fhunkexe -kick1hunks -o signal signal.asm

        section code,code

start:
        ; Disable interrupts and DMA
        move.w  #$7fff,$dff09a      ; INTENA - disable all
        move.w  #$7fff,$dff096      ; DMACON - disable all

        ; Set up minimal display
        move.w  #$0200,$dff100      ; BPLCON0 - no bitplanes, colour on

        ; Point to our Copper list
        move.l  #copperlist,$dff080 ; COP1LC
        move.w  #0,$dff088          ; COPJMP1 - start Copper

        ; Enable Copper DMA
        move.w  #$8280,$dff096      ; DMACON - enable Copper + Master

        ; Loop forever
.loop:  bra.s   .loop

        section data,data_c         ; Must be in chip RAM!

copperlist:
        ; Wait for line 44, set colour
        dc.w    $2c01,$fffe         ; Wait for vpos=$2c (line 44)
        dc.w    $0180,$0f00         ; COLOR00 = red

        dc.w    $4c01,$fffe         ; Wait for line 76
        dc.w    $0180,$0f80         ; COLOR00 = orange

        dc.w    $6c01,$fffe         ; Wait for line 108
        dc.w    $0180,$0ff0         ; COLOR00 = yellow

        dc.w    $8c01,$fffe         ; Wait for line 140
        dc.w    $0180,$00f0         ; COLOR00 = green

        dc.w    $ac01,$fffe         ; Wait for line 172
        dc.w    $0180,$00ff         ; COLOR00 = cyan

        dc.w    $cc01,$fffe         ; Wait for line 204
        dc.w    $0180,$000f         ; COLOR00 = blue

        dc.w    $ec01,$fffe         ; Wait for line 236
        dc.w    $0180,$0f0f         ; COLOR00 = magenta

        dc.w    $ffff,$fffe         ; End of Copper list (wait forever)
```

**What learner sees:** Rainbow horizontal bars filling the screen.

**Concepts introduced (not explained):**
- Custom chip registers live at $dff000
- Something called "Copper" creates the display
- Colours are written as $0RGB values
- The Copper "waits" for screen positions

**Output:** Rainbow colour bars.

**Experiment:** Change colour values ($0f00 → $0fff). See different colours.

---

### Unit 2: The Custom Chips
**Time:** 60 minutes
**Builds on:** Unit 1's working display

**What happens:**
- Meet Agnus, Denise, and Paula
- Each chip has a job
- All share the custom register space at $dff000

**The custom chip family:**
```
Agnus:  Memory controller + Copper + Blitter
        Controls when things happen
        "The traffic cop"

Denise: Display generation
        Reads bitplanes, outputs colours
        "The artist"

Paula:  Audio + Disk + Serial
        Handles sound and I/O
        "The musician"
```

**Register map (simplified):**
```
$dff000-$dff01e: Disk
$dff020-$dff07e: Blitter
$dff080-$dff08e: Copper
$dff090-$dff09e: Control (DMACON, INTENA)
$dff0a0-$dff0de: Audio (Paula)
$dff0e0-$dff0fe: Bitplane pointers
$dff100-$dff11e: Display control
$dff120-$dff17e: Sprites
$dff180-$dff1be: Colours
```

**Concepts explained:**
- Custom chips as coprocessors
- Memory-mapped registers
- Why $dff000 base address

**Output:** Same as Unit 1 (understanding, not new features).

---

### Unit 3: The Copper
**Time:** 60 minutes
**Builds on:** Unit 2's chip overview

**What happens:**
- Copper is a simple coprocessor
- It has only 3 instructions: WAIT, MOVE, SKIP
- Runs in parallel with 68000
- Restarts every frame

**Copper instructions:**
```
WAIT:  Wait until beam reaches position
       dc.w $VVHH,$fffe
       VV = vertical position (line number)
       HH = horizontal position (usually $01)

MOVE:  Write value to register
       dc.w $RREG,$DATA
       REG = register offset from $dff000
       DATA = value to write

SKIP:  Skip next instruction if beam past position
       dc.w $VVHH,$ffff  (note: $ffff not $fffe)
```

**Copper list dissected:**
```asm
        dc.w    $2c01,$fffe         ; WAIT for line $2c, any hpos
        dc.w    $0180,$0f00         ; MOVE $0f00 to $dff180 (COLOR00)
```

**Concepts explained:**
- WAIT/MOVE commands
- Beam position (raster line)
- Per-line colour changes
- Copper list structure

**Output:** Same rainbow, but now learner understands how it works.

**Experiment:** Change wait positions. Move bars up/down.

---

### Unit 4: Colours and the Palette
**Time:** 60 minutes
**Builds on:** Unit 3's Copper understanding

**What happens:**
- Amiga has 32 colour registers (OCS)
- Each colour is 12-bit: $0RGB (4 bits each)
- COLOR00 is background, COLOR01-31 for graphics

**Colour format:**
```
$0RGB where:
R = Red   (0-15)
G = Green (0-15)
B = Blue  (0-15)

Examples:
$0000 = Black       $0fff = White
$0f00 = Red         $00f0 = Green
$000f = Blue        $0ff0 = Yellow
$0f0f = Magenta     $00ff = Cyan
$0888 = Grey
```

**Multiple colours:**
```asm
copperlist:
        dc.w    $0180,$0000         ; COLOR00 = black (background)
        dc.w    $0182,$0fff         ; COLOR01 = white
        dc.w    $0184,$0f00         ; COLOR02 = red
        dc.w    $0186,$00f0         ; COLOR03 = green
        ; ... etc
        dc.w    $ffff,$fffe
```

**Concepts explained:**
- 12-bit colour (4096 colours possible)
- Colour registers $180-$1be
- Background vs foreground colours

**Output:** Palette fully configured via Copper.

**Experiment:** Create your own colour scheme. Design a palette.

---

### Unit 5: Copper Animation
**Time:** 60 minutes
**Builds on:** Unit 4's palette control

**What happens:**
- Copper list is in RAM — we can change it
- 68000 modifies Copper list values
- Copper replays modified list each frame

**Animating colours:**
```asm
start:
        ; ... setup ...

mainloop:
        ; Wait for vertical blank
        bsr     wait_vblank

        ; Animate the colour values in Copper list
        move.w  colour_offset,d0
        addq.w  #1,d0
        and.w   #$0f,d0             ; Keep 0-15
        move.w  d0,colour_offset

        ; Modify first colour in Copper list
        lea     copperlist+6,a0     ; Point to first colour value
        move.w  d0,d1
        lsl.w   #8,d1               ; Shift to red position
        move.w  d1,(a0)             ; Write new colour

        bra     mainloop

wait_vblank:
        ; Wait for line 300 (past visible area)
.wait:  move.l  $dff004,d0          ; VPOSR/VHPOSR
        and.l   #$1ff00,d0          ; Mask out vertical position
        cmp.l   #300<<8,d0
        bne     .wait
        rts
```

**Concepts explained:**
- Vblank synchronisation
- Modifying Copper list at runtime
- Frame-based animation

**Output:** Colour bars animate (cycling hue).

**Experiment:** Different animation patterns. Speed changes.

---

### Unit 6: Bitplanes — The Amiga's Pixel Format
**Time:** 75 minutes
**Builds on:** Unit 5's animation framework

**What happens:**
- Amiga uses bitplanes, not chunky pixels
- 1 bitplane = 2 colours, 2 bitplanes = 4 colours, etc.
- Each bitplane is a separate memory area
- Display hardware interleaves them

**Bitplane concept:**
```
One bitplane (2 colours):
Pixel:    0 0 1 1 0 1 0 0
Colour:   0 0 1 1 0 1 0 0   (index 0 or 1)

Two bitplanes (4 colours):
Plane 0:  0 0 1 1 0 1 0 0
Plane 1:  0 1 0 1 0 0 1 0
Colour:   0 1 2 3 0 1 2 0   (combined index 0-3)
```

**Setting up 1 bitplane:**
```asm
        ; Tell Denise: 1 bitplane, low-res
        move.w  #$1200,$dff100      ; BPLCON0 - 1 bitplane, colour

        ; Point BPL1PT to our graphics
        move.l  #bitplane1,$dff0e0  ; BPL1PTH/BPL1PTL

        ; Enable bitplane DMA
        move.w  #$8380,$dff096      ; DMACON - Master + Copper + Bitplanes
```

**Concepts explained:**
- Bitplane organisation
- How colour depth relates to bitplane count
- BPLxPT pointers
- DMA enables

**Output:** A single bitplane pattern displayed (simple graphic).

---

### Unit 7: Drawing Pixels via Bitplane
**Time:** 75 minutes
**Builds on:** Unit 6's bitplane setup

**What happens:**
- Create bitplane data in memory
- Each row is 40 bytes (320 pixels ÷ 8)
- Plot pixels by setting bits

**Bitplane memory layout:**
```
Low-res screen: 320×256 pixels
One bitplane: 320 pixels ÷ 8 bits = 40 bytes per row
256 rows × 40 bytes = 10,240 bytes per bitplane

Byte 0, bit 7 = pixel (0,0)  top-left
Byte 0, bit 0 = pixel (7,0)
Byte 1, bit 7 = pixel (8,0)
...
Byte 40, bit 7 = pixel (0,1) second row
```

**Clearing and filling:**
```asm
clear_bitplane:
        lea     bitplane1,a0
        move.w  #(40*256/4)-1,d0    ; Longwords to clear
.clear: clr.l   (a0)+
        dbf     d0,.clear
        rts

; Draw a horizontal line at row 100
draw_line:
        lea     bitplane1,a0
        add.w   #40*100,a0          ; Point to row 100
        move.w  #40-1,d0
.fill:  move.b  #$ff,(a0)+          ; Fill entire row
        dbf     d0,.fill
        rts
```

**Concepts explained:**
- Row stride (40 bytes)
- Pixel-to-byte calculation
- Memory clearing

**Output:** Lines and rectangles drawn via CPU.

**Experiment:** Draw different patterns. Create a border.

---

### Unit 8: Display Timing (DIWSTRT/DIWSTOP)
**Time:** 60 minutes
**Builds on:** Unit 7's bitplane graphics

**What happens:**
- Display window defines visible area
- Data fetch defines when Agnus reads bitplanes
- Standard values for PAL/NTSC

**Display registers:**
```asm
        ; Standard PAL display setup
        move.w  #$2c81,$dff08e      ; DIWSTRT - display window start
        move.w  #$2cc1,$dff090      ; DIWSTOP - display window stop
        move.w  #$0038,$dff092      ; DDFSTRT - data fetch start
        move.w  #$00d0,$dff094      ; DDFSTOP - data fetch stop
```

**What these mean:**
```
DIWSTRT $2c81:
  - Vertical start: $2c (line 44)
  - Horizontal start: $81 (pixel 129)

DIWSTOP $2cc1:
  - Vertical stop: $2c + $100 = line 300 (PAL)
  - Horizontal stop: $c1 (pixel 449)

Visible area: 320×256 PAL standard
```

**Concepts explained:**
- Display window vs data fetch
- PAL vs NTSC differences
- Standard display setup

**Output:** Properly positioned display.

---

### Unit 9: Multiple Bitplanes (4 Colours)
**Time:** 60 minutes
**Builds on:** Unit 8's display setup

**What happens:**
- Add a second bitplane
- Now have 4 colours (indices 0-3)
- Both planes must be set up

**Two bitplane setup:**
```asm
        ; 2 bitplanes = 4 colours
        move.w  #$2200,$dff100      ; BPLCON0 - 2 bitplanes

        ; Point both bitplane pointers
        move.l  #bitplane1,$dff0e0  ; BPL1PT
        move.l  #bitplane2,$dff0e4  ; BPL2PT

        ; Set 4 colours in palette
        move.w  #$0000,$dff180      ; COLOR00 - black (background)
        move.w  #$0f00,$dff182      ; COLOR01 - red
        move.w  #$00f0,$dff184      ; COLOR02 - green
        move.w  #$0ff0,$dff186      ; COLOR03 - yellow
```

**Drawing with colours:**
```
To draw colour 0: plane1=0, plane2=0
To draw colour 1: plane1=1, plane2=0
To draw colour 2: plane1=0, plane2=1
To draw colour 3: plane1=1, plane2=1
```

**Concepts explained:**
- Multiple bitplane coordination
- Colour index = combined bits
- Memory requirements multiply

**Output:** 4-colour display.

**Experiment:** Create patterns using all 4 colours.

---

### Unit 10: Joystick Input
**Time:** 60 minutes
**Builds on:** Unit 9's multi-colour display

**What happens:**
- Joystick data at $dff00a (JOY0DAT) and $dff00c (JOY1DAT)
- Button at $bfe001 (CIA)
- Quadrature encoding (requires decoding)

**Reading joystick:**
```asm
read_joy:
        moveq   #0,d0               ; Clear result

        move.w  $dff00a,d1          ; JOY0DAT
        btst    #1,d1               ; Right
        beq.s   .not_right
        or.b    #1,d0
.not_right:
        btst    #9,d1               ; Left
        beq.s   .not_left
        or.b    #2,d0
.not_left:
        move.w  d1,d2
        lsr.w   #1,d2
        eor.w   d2,d1               ; XOR for vertical
        btst    #0,d1               ; Down
        beq.s   .not_down
        or.b    #4,d0
.not_down:
        btst    #8,d1               ; Up
        beq.s   .not_up
        or.b    #8,d0
.not_up:
        ; Fire button (active low)
        btst    #7,$bfe001
        bne.s   .not_fire
        or.b    #16,d0
.not_fire:
        rts

; Result in d0:
; Bit 0: Right
; Bit 1: Left
; Bit 2: Down
; Bit 3: Up
; Bit 4: Fire
```

**Concepts explained:**
- Hardware joystick interface
- Quadrature decoding
- CIA for buttons

**Output:** Joystick state read each frame.

**Experiment:** Move a coloured bar based on joystick.

---

### Unit 11: Interactive Colour Bars
**Time:** 60 minutes
**Builds on:** Unit 10's joystick input

**What happens:**
- Joystick controls which colour bar is selected
- Fire button changes selected colour
- Interactive colour editor

**Combining systems:**
```asm
mainloop:
        bsr     wait_vblank
        bsr     read_joy

        ; Up/down changes selected bar
        btst    #3,d0               ; Up?
        beq.s   .not_up
        subq.w  #1,selected_bar
.not_up:
        btst    #2,d0               ; Down?
        beq.s   .not_down
        addq.w  #1,selected_bar
.not_down:

        ; Fire cycles colour
        btst    #4,d0               ; Fire?
        beq.s   .not_fire
        bsr     cycle_colour
.not_fire:

        bsr     update_copper       ; Update colours in Copper list

        bra     mainloop
```

**Concepts explained:**
- Input → state → display loop
- Separating concerns
- Real-time interaction

**Output:** Interactive colour bar editor.

---

### Unit 12: Smooth Animation
**Time:** 60 minutes
**Builds on:** Unit 11's interactive display

**What happens:**
- Double buffering concept (prepare next frame while current displays)
- Smooth scrolling colour positions
- Proper frame timing

**Smooth bar movement:**
```asm
bar_position:   dc.w 44         ; Current Y position (subpixel)
bar_velocity:   dc.w 0          ; Movement speed

update_bar:
        ; Add velocity to position
        move.w  bar_velocity,d0
        add.w   d0,bar_position

        ; Bounce at edges
        move.w  bar_position,d0
        cmp.w   #44,d0
        blt.s   .bounce_top
        cmp.w   #220,d0
        bgt.s   .bounce_bottom
        bra.s   .no_bounce
.bounce_top:
        move.w  #44,bar_position
        neg.w   bar_velocity
        bra.s   .no_bounce
.bounce_bottom:
        move.w  #220,bar_position
        neg.w   bar_velocity
.no_bounce:

        ; Update Copper list with new position
        move.w  bar_position,d0
        lsl.w   #8,d0               ; Convert to Copper wait format
        or.w    #$01,d0
        move.w  d0,copperlist+0     ; Update WAIT instruction
        rts
```

**Concepts explained:**
- Fixed-point position
- Velocity and physics
- Modifying Copper for animation

**Output:** Bouncing colour bar.

---

### Unit 13: Sound — Paula Speaks
**Time:** 75 minutes
**Builds on:** Unit 12's animation

**What happens:**
- Paula handles 4 audio channels
- Samples are 8-bit signed
- Simple beep demonstrates audio

**Playing a sample:**
```asm
        ; Set up audio channel 0
        move.l  #sample,$dff0a0     ; AUD0LC - sample address
        move.w  #sample_len/2,$dff0a4 ; AUD0LEN - length in words
        move.w  #428,$dff0a6        ; AUD0PER - period (C-3 ≈ 428)
        move.w  #64,$dff0a8         ; AUD0VOL - volume (0-64)

        ; Enable audio DMA
        move.w  #$8201,$dff096      ; DMACON - enable audio channel 0

sample:
        ; Simple square wave
        dcb.b   64,$7f              ; 64 bytes high
        dcb.b   64,$81              ; 64 bytes low
sample_end:
sample_len = sample_end - sample
```

**Concepts explained:**
- Paula's audio channels
- Sample format (8-bit signed)
- Period = pitch
- Audio DMA

**Output:** Sound plays when fire button pressed.

**Experiment:** Different waveforms. Different pitches.

---

### Unit 14: Integration and Polish
**Time:** 60 minutes
**Builds on:** All previous units

**What happens:**
- Title screen: "SIGNAL"
- Animated colour bars
- Joystick interaction
- Sound feedback
- Clean code organisation

**Program structure:**
```asm
start:
        bsr     init_hardware
        bsr     init_copper
        bsr     init_display
        bsr     draw_title

mainloop:
        bsr     wait_vblank
        bsr     read_input
        bsr     update_bars
        bsr     update_sound
        bsr     update_copper
        bra     mainloop
```

**Output:** Complete Phase 1 demo:
- Animated rainbow bars
- Joystick moves selection
- Fire plays sound
- Title displayed

---

### Unit 15: What Can Go Wrong
**Time:** 60 minutes
**Builds on:** All previous units

**Common Amiga bugs catalogued:**

**Bug 1: Black Screen (Nothing Displays)**
```
Symptom: Monitor shows nothing / solid colour
Check 1: DMACON — is Copper enabled? ($8280 minimum)
Check 2: Copper list in chip RAM? (section data,data_c)
Check 3: COP1LC pointing to valid address?
Check 4: Copper list terminated? ($ffff,$fffe at end)
Check 5: BPLCON0 — is colour enabled? (bit 9 set)
```

**Bug 2: Garbage/Noise on Screen**
```
Symptom: Random patterns, flickering
Check 1: Bitplane pointers correct?
Check 2: Bitplane DMA enabled? ($8100 for planes)
Check 3: DDFSTRT/DDFSTOP values correct?
Check 4: Bitplanes in chip RAM?
Check 5: Modulo values correct? (BPL1MOD/BPL2MOD)
```

**Bug 3: Sprites Not Visible**
```
Symptom: Sprites don't appear despite setup
Check 1: DMACON — are sprites AND bitplanes enabled?
         Need $83a0, not $8280!
Check 2: Sprite data in chip RAM?
Check 3: Sprite position on screen?
```

**Bug 4: Colours Wrong**
```
Symptom: Wrong colours displayed
Check 1: Writing to correct colour register? ($180 = COLOR00)
Check 2: 12-bit format correct? ($0RGB)
Check 3: Copper list MOVE format correct?
```

**Bug 5: Audio Silent**
```
Symptom: No sound
Check 1: Audio DMA enabled? ($8201 for channel 0)
Check 2: Volume non-zero? ($dff0a8)
Check 3: Sample in chip RAM?
Check 4: Period reasonable? (124-65535)
```

**Bug 6: Crashes/Guru Meditation**
```
Symptom: System crashes
Check 1: Stack set up correctly?
Check 2: Supervisor mode if accessing protected registers?
Check 3: Address errors (odd address for word/long)?
Check 4: Illegal instruction?
```

**Debugging tools introduced:**
- WinUAE debugger
- Copper list viewer
- Memory inspector
- DMA visualiser

---

### Unit 16: Fixing Broken Code
**Time:** 60 minutes
**Builds on:** Unit 15's debugging knowledge

**Exercise 1: Black Screen**
```asm
; Should display colour bars. Screen is black.
start:
        move.w  #$7fff,$dff09a
        move.w  #$7fff,$dff096

        move.w  #$0200,$dff100

        move.l  #copperlist,$dff080
        move.w  #0,$dff088

        ; Bug here!
        move.w  #$8200,$dff096      ; <-- Missing Copper enable bit

.loop:  bra.s   .loop

copperlist:
        dc.w    $0180,$0f00
        dc.w    $ffff,$fffe
```
**Fix:** DMACON needs Copper bit. Change `$8200` to `$8280`.

**Exercise 2: Copper List Not in Chip RAM**
```asm
        section code,code           ; <-- Bug: code section, not chip RAM

copperlist:
        dc.w    $0180,$0f00
        dc.w    $ffff,$fffe
```
**Fix:** Copper list must be in chip RAM:
```asm
        section data,data_c         ; _c = chip RAM
```

**Exercise 3: Bitplanes Don't Display**
```asm
        move.w  #$1200,$dff100      ; 1 bitplane
        move.l  #bitplane1,$dff0e0  ; Pointer OK
        move.w  #$8280,$dff096      ; <-- Bug: no bitplane DMA!
```
**Fix:** Need to enable bitplane DMA:
```asm
        move.w  #$8380,$dff096      ; Master + Copper + Bitplanes
```

**Exercise 4: No Sound**
```asm
        move.l  #sample,$dff0a0
        move.w  #sample_len/2,$dff0a4
        move.w  #428,$dff0a6
        move.w  #64,$dff0a8
        ; Missing DMA enable!        ; <-- Bug
```
**Fix:** Enable audio DMA:
```asm
        move.w  #$8201,$dff096      ; Enable audio channel 0
```

**Phase 1 Complete.**

---

## Phase 1 Summary

| Unit | Focus | Key Concept | Output |
|------|-------|-------------|--------|
| 1 | First bars | — | Colour bars |
| 2 | Custom chips | Agnus/Denise/Paula | Understanding |
| 3 | Copper | WAIT/MOVE | Understanding |
| 4 | Colours | 12-bit palette | Palette control |
| 5 | Animation | Modifying Copper | Animated colours |
| 6 | Bitplanes | Planar graphics | 2-colour display |
| 7 | Drawing | Row stride | Shapes drawn |
| 8 | Display timing | DIWSTRT/DDFSTRT | Proper setup |
| 9 | Multi-plane | 4 colours | 4-colour display |
| 10 | Joystick | Quadrature decode | Input read |
| 11 | Interactive | Input→Display loop | Colour editor |
| 12 | Smooth motion | Frame timing | Bouncing bar |
| 13 | Audio | Paula samples | Sound plays |
| 14 | Polish | Integration | Complete demo |
| 15 | Debug theory | Black screen fixes | Debug reference |
| 16 | Debug practice | Hands-on fixing | Fixed programs |

**Phase 1 Result:** Working audio-visual demo with input + ability to debug common custom chip problems.

**Phase 2 Preview:** Blitter. Fast drawing. Sprite basics.

---

## Amiga-Specific Challenges Addressed

| Challenge | How Phase 1 Addresses It |
|-----------|-------------------------|
| Multiple custom chips | Unit 2: Dedicated overview |
| Copper complexity | Units 3-5: Gradual introduction |
| Bitplane confusion | Units 6-7: Thorough explanation |
| Chip RAM requirement | Units 1, 15-16: Explicit |
| Audio complexity | Unit 13: Simple sample |
| Black screen terror | Units 15-16: Dedicated debugging |

---

## DMACON Quick Reference (For Debugging)

```
DMACON ($dff096) - Write SET bits:
$8000 = Set enable (not clear)
$0200 = Master enable (REQUIRED)
$0100 = Bitplane DMA
$0080 = Copper DMA
$0040 = Blitter DMA
$0020 = Sprite DMA
$000f = Audio channels 0-3

Common combinations:
$8280 = Master + Copper (minimum for Copper bars)
$8380 = Master + Copper + Bitplanes
$83a0 = Master + Copper + Bitplanes + Sprites
$83e0 = Everything except Blitter
$83ff = Everything
```

---

**Version:** 1.0
**Last Updated:** 2026-01-17
