# Unit 1 Template: Magic First, Explain After

**Purpose:** Template for Unit 1 of any game, demonstrating the "wonder first" pedagogy
**Principle:** Something works in the first 10 minutes. Explanation comes later.

---

## Structure

Every Unit 1 follows this pattern:

```
1. THE HOOK (5-10 mins)
   - Show the finished result (screenshot/audio description)
   - "By the end of this unit, you'll have this running"

2. THE INCANTATION (10-15 mins)
   - Type the code exactly as shown
   - No explanation yet — just type
   - Run it. See/hear the result.

3. THE PAUSE (5 mins)
   - Celebrate: "You just programmed the SID chip"
   - Brief reassurance: "Don't worry if you don't understand it yet"
   - Preview: "Over the next few units, we'll break this down"

4. THE FIRST PEEK (15-20 mins)
   - Explain ONE thing from what they typed
   - Keep it concrete and visual
   - "Change this value. See what happens."

5. THE TEASE (5 mins)
   - "Next unit, we'll understand [specific thing]"
   - Leave them curious, not confused
```

**Total:** 40-55 minutes (shorter than standard unit — Unit 1 is about momentum, not depth)

---

## Example: C64 Game 1 (SID Symphony), Unit 1

### Your First Sound

![Screenshot: Simple waveform display with "SID SYMPHONY" title](screenshot-unit-01.png)

By the end of this unit, your C64 will be making noise. Real noise, from the SID chip — the same chip that powered the music in Commando, Wizball, and everything else you remember.

Let's not waste time. Fire up your assembler.

---

### The Code

Type this exactly. Don't worry about what it means — we'll get to that.

```asm
; SID Symphony - Unit 1
; Type this exactly as shown

*= $0801

; BASIC launcher (just type it)
!byte $0c,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00

*= $080d

start:
        ; Clear decimal mode
        cld

        ; Turn the volume up
        lda #$0f
        sta $d418

        ; Set a frequency
        lda #$25
        sta $d400
        lda #$1c
        sta $d401

        ; Set the envelope
        lda #$00
        sta $d405
        lda #$f0
        sta $d406

        ; Start the note (sawtooth wave)
        lda #$21
        sta $d404

        ; Loop forever
loop:   jmp loop
```

Save it as `symphony.asm`.

---

### Build and Run

```bash
acme -f cbm -o symphony.prg symphony.asm
```

Load it in VICE (or your real C64):

```
LOAD "SYMPHONY.PRG",8,1
RUN
```

You should hear a continuous tone. A raw, buzzing sawtooth wave.

**That's the SID chip.** You just programmed it.

---

### What Just Happened?

Don't panic. You don't need to understand all of that yet. Here's what matters:

1. **You wrote machine code.** Those `lda` and `sta` instructions are 6510 assembly language — the native tongue of the C64.

2. **You talked to the SID.** The addresses starting with `$d4` are the SID chip's registers. You told it what frequency to play, how loud, and what waveform to use.

3. **It worked.** The SID is now doing exactly what you told it.

Over the next fifteen units, we'll break down every line. But first, let's experiment.

---

### Your First Experiment

Find this line:

```asm
        lda #$21
        sta $d404
```

The `#$21` controls the waveform. Change it to `#$11`:

```asm
        lda #$11
        sta $d404
```

Rebuild and run. Hear the difference? That's a triangle wave instead of sawtooth — smoother, more mellow.

Try these values:

| Value | Waveform | Sound |
|-------|----------|-------|
| `#$11` | Triangle | Smooth, flute-like |
| `#$21` | Sawtooth | Buzzy, aggressive |
| `#$41` | Pulse | Hollow, square-ish |
| `#$81` | Noise | Static, drums |

Each waveform has a completely different character. The SID has three voices, and each can use any waveform. That's how C64 music gets its richness.

---

### Coming Up

You've heard the SID. You've changed a waveform. But there's a lot of magic in that code you typed.

**Unit 2:** We'll decode the BASIC launcher — that mysterious `!byte` line at the top.

**Unit 3:** We'll understand `lda` and `sta` — the two instructions that do almost everything.

**Unit 4:** We'll explore the SID's frequency registers and play different notes.

For now, you've done something real. You've made the C64's most famous chip sing.

---

### Files

- `symphony.asm` — Your first SID program

---

## Example: C64 BASIC Gateway Game 1, Unit 1

### Your First Program

![Screenshot: Screen filled with "HELLO WORLD"](screenshot-basic-unit-01.png)

By the end of this unit, your C64 screen will be filled with text — and you'll have written the code that does it.

No setup. No theory. Just type.

---

### The Code

Turn on your C64 (or VICE). At the `READY.` prompt, type:

```basic
10 print "HELLO WORLD"
20 goto 10
```

Press `RETURN` after each line. Then type:

```
RUN
```

Watch the screen fill up.

**Press `RUN/STOP` to stop it.**

---

### What Just Happened?

You wrote a program. Two lines:

- **Line 10** prints "HELLO WORLD" on the screen
- **Line 20** goes back to line 10 and does it again

Forever. Or until you press `RUN/STOP`.

That's a loop — the computer doing something repeatedly. Every game you've ever played has a loop at its heart.

---

### Your First Experiment

Let's make it more interesting. Type:

```
NEW
```

This clears your program. Now type:

```basic
10 print "HELLO WORLD ";
20 goto 10
```

Notice the semicolon after the closing quote? Run it.

Different, isn't it? The semicolon tells PRINT to stay on the same line.

Now try:

```
NEW
10 for i = 1 to 10
20 print "HELLO WORLD"
30 next i
```

This prints exactly 10 times, then stops. No `RUN/STOP` needed.

---

### Coming Up

You've made the C64 print text. You've made it loop. You've controlled how many times it loops.

**Unit 2:** We'll put text exactly where we want on screen — not just scrolling down.

**Unit 3:** We'll add colour. Lots of colour.

For now, experiment. Change the text. Change the number. See what happens when you make mistakes — the C64 will tell you.

---

## Example: ZX Spectrum Game 1 (Ink War), Unit 1

### Your First Attribute

![Screenshot: Single coloured square on black background](screenshot-zx-unit-01.png)

The Spectrum's secret weapon isn't its speed or its memory. It's the attribute system — the way it handles colour. It's weird, it's limiting, and it's what makes Spectrum games look like nothing else.

By the end of this unit, you'll have painted a coloured square on screen. In assembly. On real hardware.

---

### The Code

```asm
; Ink War - Unit 1
; Type this exactly

        org $8000

start:
        ; Set border to black
        ld a, 0
        out ($fe), a

        ; Clear the screen
        ld hl, $4000
        ld de, $4001
        ld bc, $17ff
        ld (hl), 0
        ldir

        ; Clear attributes to black on black
        ld hl, $5800
        ld de, $5801
        ld bc, $02ff
        ld (hl), 0
        ldir

        ; Paint one cell bright red on black
        ld a, %01000010     ; Bright + red ink
        ld ($5800), a       ; Top-left attribute cell

        ; Fill that cell with pixels
        ld hl, $4000
        ld b, 8
fill:   ld (hl), $ff
        inc h
        djnz fill

        ; Loop forever
loop:   jr loop
```

Save as `inkwar.asm` and build:

```bash
pasmonext --sna inkwar.asm inkwar.sna
```

Run in Fuse. You should see a bright red square in the top-left corner. Everything else is black.

**That's the attribute system.** One byte controls the colour of an 8×8 pixel cell.

---

### Your First Experiment

Find this line:

```asm
        ld a, %01000010     ; Bright + red ink
```

That `%01000010` is binary. Each bit means something:

```
  0 1 0 0 0 0 1 0
  │ │ │ │ │ │ └─┴── Ink (foreground): 010 = red
  │ │ │ └─┴─┴────── Paper (background): 000 = black
  │ │ └──────────── Bright: 1 = bright colours
  │ └────────────── Flash: 0 = no flashing
  └──────────────── (unused)
```

Try `%01000011` — that's red ink (011 = magenta? Let's see...). Actually:

| Ink bits | Colour |
|----------|--------|
| 000 | Black |
| 001 | Blue |
| 010 | Red |
| 011 | Magenta |
| 100 | Green |
| 101 | Cyan |
| 110 | Yellow |
| 111 | White |

Change the value, rebuild, see the colour change.

---

### Coming Up

You've painted one cell. The screen has 768 of them (32 × 24).

**Unit 2:** We'll fill the whole screen with colour.

**Unit 3:** We'll understand why this system causes "colour clash" — and how to use it creatively.

---

## Example: NES Game 1 (Neon Nexus), Unit 1

### Your First Tile

![Screenshot: Single coloured tile on NES](screenshot-nes-unit-01.png)

The NES doesn't have pixels you can set directly. It has tiles — 8×8 patterns stored in ROM. Everything you see on an NES is made of tiles.

By the end of this unit, you'll have one tile on screen. Just one. But it's yours.

---

### The Code

```asm
; Neon Nexus - Unit 1

.segment "HEADER"
    .byte "NES", $1a
    .byte $01           ; 1 PRG bank
    .byte $01           ; 1 CHR bank
    .byte $00, $00      ; Mapper 0, horizontal mirroring
    .byte $00, $00, $00, $00, $00, $00, $00, $00

.segment "CODE"

reset:
    sei
    cld
    ldx #$ff
    txs

    ; Wait for PPU
    bit $2002
:   bit $2002
    bpl :-
:   bit $2002
    bpl :-

    ; Set palette
    lda #$3f
    sta $2006
    lda #$00
    sta $2006
    lda #$0f        ; Black background
    sta $2007
    lda #$30        ; White foreground
    sta $2007

    ; Write one tile to nametable
    lda #$20
    sta $2006
    lda #$00
    sta $2006
    lda #$01        ; Tile index 1
    sta $2007

    ; Enable rendering
    lda #%00001000
    sta $2000
    lda #%00011110
    sta $2001

loop:
    jmp loop

nmi:
irq:
    rti

.segment "VECTORS"
    .word nmi, reset, irq

.segment "CHARS"
    ; Tile 0: empty
    .byte $00,$00,$00,$00,$00,$00,$00,$00
    .byte $00,$00,$00,$00,$00,$00,$00,$00

    ; Tile 1: solid block
    .byte $ff,$ff,$ff,$ff,$ff,$ff,$ff,$ff
    .byte $ff,$ff,$ff,$ff,$ff,$ff,$ff,$ff
```

Build with ca65/ld65 and run in FCEUX. You should see a single white square in the top-left corner.

**That's a tile.** The NES PPU looked up tile #1 in your CHR data and drew it.

---

### Your First Experiment

Find the CHR data at the bottom — the tile that's all `$ff`. Change one line:

```asm
    ; Tile 1: pattern
    .byte $ff,$81,$81,$81,$81,$81,$81,$ff
    .byte $00,$00,$00,$00,$00,$00,$00,$00
```

Rebuild. Now it's a hollow square. The first 8 bytes are the tile's bit pattern.

Every NES game — Mario, Zelda, Mega Man — is built from tiles like this.

---

### Coming Up

**Unit 2:** We'll understand how the PPU addresses work (those mysterious `$2006` and `$2007` writes).

**Unit 3:** We'll fill the screen with tiles and make a pattern.

---

## Template Checklist

For any Unit 1:

- [ ] Screenshot of final result shown first
- [ ] Code is complete and runnable (no "we'll add this later")
- [ ] Learner types and runs within first 15 minutes
- [ ] Only ONE concept explained in detail
- [ ] Hands-on experiment with immediate visible result
- [ ] Clear preview of Units 2-3
- [ ] Total time: 40-55 minutes (shorter than standard units)
- [ ] Tone: excited but not breathless, confident but not condescending

---

## Anti-Patterns (What NOT to Do)

**Don't start with theory:**
> ❌ "Before we write any code, let's understand the SID chip's architecture. The SID has three voices, each with..."

**Don't explain everything:**
> ❌ "The `lda #$0f` instruction loads the accumulator with the immediate value $0f, which in decimal is 15, which sets the volume to maximum because..."

**Don't apologise for complexity:**
> ❌ "This might look complicated, but don't worry..."

**Don't delay the payoff:**
> ❌ "In this unit we'll set up our project structure. In Unit 2 we'll configure the assembler. In Unit 3 we'll finally write some code..."

**Do trust the learner:**
> ✓ "Type this. Run it. Hear that? Good. Now let's understand one piece of what you just did."

---

**Version:** 1.0
**Last Updated:** 2026-01-17
