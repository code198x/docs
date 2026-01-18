# Dragon & The 6809: The Best 8-bit CPU

**Purpose:** Document the Dragon 32/64, the Motorola 6809 processor, and related platforms - a distinct architectural branch worthy of curriculum inclusion.

**Last Updated:** 2026-01-18

---

## Why The 6809 Matters

The Motorola 6809 is often considered **the finest 8-bit CPU ever designed**:

| Feature | Significance |
|---------|--------------|
| **Clean architecture** | Orthogonal instruction set |
| **16-bit operations** | D register (A+B combined) |
| **Two index registers** | X and Y |
| **Two stack pointers** | S (system) and U (user) |
| **Position-independent code** | PC-relative addressing |
| **Sophisticated addressing** | All modes on all registers |
| **Modern design** | Felt like a 16-bit CPU |

The 6809 was what the 6502 could have been with a larger transistor budget.

---

## Part 1: The Motorola 6809

### Architecture Overview

```
+------------------+
|    Registers     |
+------------------+
| A  | 8-bit accumulator
| B  | 8-bit accumulator
| D  | 16-bit (A:B combined)
| X  | 16-bit index register
| Y  | 16-bit index register
| U  | 16-bit user stack pointer
| S  | 16-bit system stack pointer
| PC | 16-bit program counter
| DP | 8-bit direct page register
| CC | 8-bit condition codes
+------------------+
```

### What Made It Special

#### Two Accumulators That Combine

```asm
    LDA #$12      ; A = $12
    LDB #$34      ; B = $34
    ; D now equals $1234
    ADDD #$0001   ; 16-bit add: D = $1235
```

No other 8-bit CPU did this so elegantly.

#### Position-Independent Code

```asm
    LBSR SUBROUTINE   ; Long branch to subroutine
    LEAX TABLE,PCR    ; Load effective address, PC-relative
```

Code could run at any address without modification - revolutionary for 1978.

#### Two Stack Pointers

```asm
    PSHS A,B,X       ; Push to system stack
    PSHU Y           ; Push to user stack
    PULS A,B,X,PC    ; Pull and return in one instruction
```

Made subroutine calls and interrupt handling elegant.

#### Orthogonal Design

Unlike 6502's quirks, most 6809 instructions worked with most addressing modes:

| 6502 | 6809 |
|------|------|
| LDA works differently from LDX | All loads work the same |
| Some modes only on some instructions | Consistent across instruction set |
| Awkward 16-bit operations | Native 16-bit with D register |

### Comparison to Other 8-bit CPUs

| Feature | 6502 | Z80 | 6809 |
|---------|------|-----|------|
| **Accumulators** | 1 (A) | 1 (A) + others | 2 (A, B) + D |
| **Index registers** | 2 (X, Y) limited | IX, IY | 2 (X, Y) full |
| **Stack pointers** | 1 (8-bit!) | 1 | 2 (both 16-bit) |
| **16-bit ops** | Very limited | Some | Extensive |
| **Addressing modes** | Limited per instruction | Complex | Orthogonal |
| **Position-independent** | No | No | Yes |
| **Instruction set** | Small, quirky | Large, irregular | Medium, clean |

### Why It Didn't Win

| Factor | Impact |
|--------|--------|
| **Cost** | More expensive than 6502 |
| **Timing** | Arrived after 6502 established |
| **Apple II/C64** | 6502 machines dominated |
| **IBM PC** | 8088/8086 became standard |
| **Zilog** | Z80 was cheaper alternative |

The 6809 was technically superior but lost on economics and timing.

**Vault entries:**
- `motorola-6809` - Hardware entry (major)
- `6809-architecture` - Technique entry
- `position-independent-code` - Technique entry

---

## Part 2: Dragon 32/64

### The Machine

| Specification | Dragon 32 | Dragon 64 |
|---------------|-----------|-----------|
| **CPU** | Motorola 6809E @ 0.89 MHz | Same |
| **RAM** | 32 KB | 64 KB |
| **ROM** | 16 KB (BASIC) | 16 KB |
| **Graphics** | MC6847 VDG | Same |
| **Sound** | 1-bit DAC | Same |
| **Storage** | Cassette, optional disk | Same |
| **Released** | 1982 | 1983 |
| **Price** | £199 | £299 |
| **Manufacturer** | Dragon Data, Wales | Same |

### The Company

| Aspect | Notes |
|--------|-------|
| **Name** | Dragon Data Ltd |
| **Location** | Port Talbot, Wales |
| **Founded** | 1982 |
| **Closed** | 1984 |
| **Legacy** | Brief but significant |

Dragon Data was a Welsh company that briefly challenged the Spectrum and C64.

### Graphics: The MC6847 VDG

| Mode | Resolution | Colours |
|------|------------|---------|
| **Text** | 32×16 | 2 (fixed green/orange or black/green) |
| **Semigraphics** | 64×32 to 64×192 | 8 |
| **Graphics** | 256×192 | 2 (from sets) |
| **Graphics** | 128×192 | 4 (from sets) |

The VDG had limited colour choices - fixed colour sets, not arbitrary colours.

### Sound

| Aspect | Notes |
|--------|-------|
| **Hardware** | 1-bit DAC |
| **Capability** | Basic beeps, PWM possible |
| **Music** | Limited without tricks |

Sound was the Dragon's weakness - far behind SID or AY.

### Software Library

| Category | Notable Titles |
|----------|----------------|
| **Games** | Cuthbert Goes Walkabout, Donkey King, Chuckie Egg |
| **Business** | RollaCall (database), various |
| **Languages** | BASIC (built-in), Forth, Pascal, C |
| **Utilities** | Various tape utilities |

The library was smaller than Spectrum/C64 but had quality titles.

### CoCo Compatibility

The Dragon was **largely compatible** with the Tandy TRS-80 Color Computer:
- Same CPU (6809)
- Same video chip (MC6847)
- Similar memory map
- Most CoCo software ran on Dragon

This expanded the available software significantly.

**Vault entries:**
- `dragon-32` - Hardware entry
- `dragon-64` - Hardware entry
- `dragon-data` - Company entry
- `mc6847-vdg` - Hardware entry

---

## Part 3: Tandy TRS-80 Color Computer

### The Machine

| Specification | CoCo 1 | CoCo 2 | CoCo 3 |
|---------------|--------|--------|--------|
| **CPU** | 6809E @ 0.89 MHz | Same | 6809E @ 1.79 MHz |
| **RAM** | 4-64 KB | 16-64 KB | 128-512 KB |
| **Graphics** | MC6847 | MC6847 | GIME (enhanced) |
| **Released** | 1980 | 1983 | 1986 |
| **Market** | USA | USA | USA |

### CoCo vs Dragon

| Aspect | CoCo | Dragon |
|--------|------|--------|
| **Market** | USA (Tandy/Radio Shack) | UK/Europe |
| **Sales** | Higher (USA bigger) | Lower |
| **Support** | Longer (Tandy resources) | Shorter (company folded) |
| **Software** | Larger library | Smaller but compatible |

### The CoCo 3

The CoCo 3 (1986) was significantly enhanced:
- Faster CPU (1.79 MHz)
- Up to 512 KB RAM
- GIME chip: 320×200 in 16 colours, 640×200 in 4 colours
- Palette of 64 colours
- Enhanced sound

The CoCo 3 showed what the platform could have become.

**Vault entries:**
- `trs-80-color-computer` - Hardware entry
- `coco-3` - Hardware entry
- `tandy` - Company entry
- `gime-chip` - Hardware entry

---

## Part 4: Vectrex

### The Vector Graphics Console

| Specification | Details |
|---------------|---------|
| **CPU** | Motorola 6809 @ 1.5 MHz |
| **RAM** | 1 KB |
| **Display** | Built-in 9" vector CRT |
| **Graphics** | Vector (lines, not pixels) |
| **Sound** | AY-3-8912 |
| **Released** | 1982 |
| **Manufacturer** | GCE / Milton Bradley |

### Why Vectrex Was Unique

| Feature | Significance |
|---------|--------------|
| **Built-in display** | No TV needed |
| **Vector graphics** | Sharp lines at any angle |
| **Colour overlays** | Plastic overlays for colour |
| **Controller** | Analog joystick + 4 buttons |
| **3D capability** | 3D Imager accessory |

### Vector Graphics Programming

Unlike raster systems, Vectrex drew lines:

```asm
    ; Draw a line from current position
    LDA #$7F        ; Brightness
    LDB #$20        ; Y component
    LDX #$30        ; X component (in X register for timing)
    JSR Draw_Line
```

Concepts unique to vector:
- Beam positioning
- Line drawing
- Brightness control
- Refresh rate (redraw entire screen)

### The Vectrex Library

| Game | Notes |
|------|-------|
| **Mine Storm** | Built-in, Asteroids-like |
| **Scramble** | Konami port |
| **Star Trek** | Vector perfect for space |
| **Pole Position** | Racing |
| **Spike** | Platformer with overlay |

### Modern Vectrex Scene

The Vectrex has an active homebrew community:
- New games still released
- Multicarts available
- Reproduction overlays
- Modern development tools

**Vault entries:**
- `vectrex` - Hardware entry
- `vector-graphics` - Technique entry
- `gce` - Company entry
- `vectrex-homebrew` - Culture entry

---

## Part 5: Other 6809 Systems

### Williams Arcade Boards

Williams used the 6809 in legendary arcade games:

| Game | Year | Notes |
|------|------|-------|
| **Defender** | 1981 | First major 6809 game |
| **Stargate** | 1981 | Defender sequel |
| **Robotron: 2084** | 1982 | Twin-stick classic |
| **Joust** | 1982 | Co-op/competitive |
| **Sinistar** | 1983 | "RUN, COWARD!" |
| **Moon Patrol** | 1982 | Irem, side-scroller |

**Eugene Jarvis** created Defender and Robotron on 6809 - landmark games.

### Konami Arcade

Konami used 6809 in:
- **Track & Field** (1983)
- **Gyruss** (1983)
- **Time Pilot** (1982)
- Early **Gradius** hardware

### Other Systems

| System | Use of 6809 |
|--------|-------------|
| **Thomson MO5/TO7** | French school computers |
| **Fujitsu FM-7** | Japanese computer |
| **SWTPC** | Early hobby computers |
| **Various arcade boards** | Many manufacturers |

**Vault entries:**
- `williams-arcade` - Company entry
- `eugene-jarvis` - People entry
- `defender` - Game entry
- `robotron-2084` - Game entry

---

## Part 6: Programming The 6809

### Key Differences from 6502

| 6502 Way | 6809 Way |
|----------|----------|
| `LDA #$00; STA $1000` | `CLR $1000` |
| Separate X,Y usage | X and Y interchangeable |
| Page zero tricks | Direct page anywhere |
| Self-modifying for speed | Position-independent instead |
| JSR/RTS | BSR/RTS or LBSR/RTS |

### 6809 Idioms

```asm
; Clear a block of memory (6809 elegance)
    LDX #$1000      ; Start address
    LDB #$40        ; 64 bytes
LOOP:
    CLR ,X+         ; Clear and increment X
    DECB
    BNE LOOP

; 16-bit counter increment
    LDD COUNTER     ; Load 16-bit value
    ADDD #1         ; 16-bit add
    STD COUNTER     ; Store back

; Table lookup with indexing
    LEAX TABLE,PCR  ; PC-relative address
    LDA B,X         ; Load TABLE[B]
```

### Position-Independent Code

```asm
; This code works at ANY address:
START:
    LEAX DATA,PCR   ; Get data address relative to PC
    LDA ,X          ; Load first byte
    LEAY BUFFER,PCR ; Get buffer address
    STA ,Y          ; Store to buffer
    BRA START       ; Branch (always relative)

DATA: FCB $12,$34
BUFFER: RMB 2
```

This was revolutionary - code could be relocated without modification.

### Stack Operations

```asm
; Push multiple registers in one instruction
    PSHS A,B,X,Y    ; Push A, B, X, Y to system stack

; Pull and return in one instruction
    PULS A,B,X,PC   ; Pull registers and return!

; Use user stack for data
    PSHU D          ; Push D to user stack
    LEAU -10,U      ; Allocate 10 bytes on user stack
```

**Vault entries:**
- `6809-programming` - Technique entry
- `direct-page` - Technique entry

---

## Part 7: Curriculum Potential

### What 6809 Teaches

| Concept | Value |
|---------|-------|
| **Clean architecture** | What good CPU design looks like |
| **16-bit thinking** | Bridge to 68000 |
| **Position-independent code** | Modern concept (shared libraries) |
| **Stack frames** | Proper call conventions |
| **Orthogonal design** | Consistent, predictable |

### Comparison Pedagogy

Teaching 6809 after 6502:
- "Remember how 6502 had weird limitations? 6809 doesn't."
- "That hack you needed on 6502? Here's the proper instruction."
- "See how much cleaner this is?"

### Suggested Curriculum Position

| Option | Approach |
|--------|----------|
| **Tier 2** | 8 games, proper coverage |
| **Tier 3** | 4 games, focused on architecture |
| **Comparative** | Teach alongside 6502 for contrast |

### Potential Game Sequence (8 games)

| # | Game Type | Teaches |
|---|-----------|---------|
| 1 | Sound toy | Basic I/O, DAC |
| 2 | Text adventure | String handling, 16-bit |
| 3 | Maze game | Semigraphics, movement |
| 4 | Shoot 'em up | Sprites via software |
| 5 | Platformer | Collision, scrolling |
| 6 | Puzzle game | Logic, state machines |
| 7 | Action game | Performance, tricks |
| 8 | Arcade port | Put it all together |

### Vectrex Alternative Track

A Vectrex-focused track would be completely unique:

| # | Game Type | Teaches |
|---|-----------|---------|
| 1 | Line drawing | Vector basics |
| 2 | Asteroids clone | Movement, rotation |
| 3 | 3D wireframe | 3D mathematics |
| 4 | Space shooter | Particle effects |

**No other curriculum could teach vector graphics this way.**

---

## Part 8: Development Tools

### Emulators

| Emulator | Platform | Quality |
|----------|----------|---------|
| **XRoar** | Dragon/CoCo | Excellent |
| **MAME** | Dragon/CoCo/Vectrex | Good |
| **VecX** | Vectrex | Good |
| **ParaJVE** | Vectrex | Good |

### Assemblers

| Assembler | Notes |
|-----------|-------|
| **ASM6809** | Modern, cross-platform |
| **LWTOOLS** | lwasm, comprehensive |
| **asm6809** | Portable |

### Development Resources

| Resource | Type |
|----------|------|
| **6809 datasheet** | Official Motorola docs |
| **Dragon Archive** | Software preservation |
| **CoCo community** | Active users |
| **Vectrex wiki** | Homebrew documentation |

---

## Part 9: The Dragon Legacy

### Why Dragon Failed

| Factor | Impact |
|--------|--------|
| **Competition** | Spectrum at £125, C64 dominant |
| **Limited graphics** | VDG couldn't match sprites |
| **Weak sound** | No SID equivalent |
| **Company issues** | Dragon Data underfunded |
| **Timing** | Entered crowded market |

### Why Dragon Mattered

| Factor | Significance |
|--------|--------------|
| **Welsh computing** | Industry in Wales |
| **6809 exposure** | Best 8-bit CPU to UK market |
| **CoCo compatibility** | Expanded software base |
| **Alternative** | Not everyone had Spectrum/C64 |
| **Quality hardware** | Well-built machines |

### Preservation

| Project | Focus |
|---------|-------|
| **Dragon Archive** | Software preservation |
| **World of Dragon** | Community site |
| **Various emulators** | XRoar excellent |
| **Hardware reproduction** | Modern recreations |

---

## Part 10: Key People

| Person | Role | Contribution |
|--------|------|--------------|
| **Terry Ritter** | 6809 co-designer | CPU architecture |
| **Joel Boney** | 6809 co-designer | CPU architecture |
| **Eugene Jarvis** | Williams programmer | Defender, Robotron |
| **Prabhakar Goel** | Dragon Data | Dragon development |

**Vault entries:** All of the above

---

## Summary: New Vault Entries

| Category | Entries |
|----------|---------|
| **Hardware** | 6809, Dragon 32/64, CoCo, Vectrex, MC6847, GIME | 10 |
| **Companies** | Dragon Data, Tandy, GCE, Williams | 5 |
| **Games** | Defender, Robotron, Mine Storm, various | 8 |
| **People** | Ritter, Boney, Jarvis | 4 |
| **Techniques** | 6809 programming, vector graphics, PIC | 6 |
| **Culture** | Vectrex homebrew, Dragon legacy | 3 |

**Total new entries: ~36**

---

## Running Vault Total

| Previous | This Document | New Total |
|----------|---------------|-----------|
| ~1202 | +36 | **~1238 entries** |

---

## Recommendation

The Dragon/6809 deserves **Tier 2 or Tier 3 coverage**:

**For Tier 2 (8 games):**
- Full Dragon curriculum
- 6809 as architectural study
- Bridge between 6502 and 68000
- UK heritage platform

**For Tier 3 (4 games):**
- Focused on 6809 architecture
- Comparison to 6502
- Unique vector track on Vectrex

**The 6809's elegance makes it pedagogically valuable** - it shows what clean CPU design looks like, making 6502 quirks understandable and preparing for 68000's sophistication.

**Vectrex is completely unique** - no other platform teaches vector graphics. A small Vectrex track would be unlike anything else in games education.
