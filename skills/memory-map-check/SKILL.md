---
name: memory-map-check
description: Use when validating memory access in code - ensures safe memory ranges, correct hardware register access, and no system memory corruption
---

# Memory Map Check

## Overview

This skill validates code against platform-specific memory maps to ensure safe memory usage. Each platform has distinct memory layout with safe/unsafe regions, hardware registers, and system areas. Writing to wrong addresses causes crashes, corruption, or unexpected behavior. Validates POKE/PEEK (BASIC) and STA/LDA (assembly) against memory maps.

## When to Use

Use when:
- Creating new lesson code (check before compilation)
- Reviewing existing code for memory safety
- Semantic validator flags memory issue
- Code crashes or corrupts unexpectedly
- Using advanced memory techniques (direct hardware access)

**Do NOT use for:**
- Code that doesn't access memory directly (pure calculations)
- Code already validated by semantic validator
- Tiny examples with obvious memory usage

---

## Platform Memory Maps

### Commodore 64

#### Safe Ranges (BASIC/User Programs)

| Range | Hex | Purpose | Safety |
|-------|-----|---------|--------|
| 2049-40959 | $0801-$9FFF | BASIC/User Program | ✅ SAFE |
| 49152-53247 | $C000-$CFFF | RAM (if no ROM) | ⚠ CONDITIONAL |
| 251-254 | $FB-$FE | Safe Zero Page | ✅ SAFE |

#### Unsafe Ranges (Avoid!)

| Range | Hex | Purpose | Risk |
|-------|-----|---------|------|
| 0-255 | $0000-$00FF | Zero Page | ❌ SYSTEM USE |
| 256-511 | $0100-$01FF | Stack | ❌ WILL CRASH |
| 512-2047 | $0200-$07FF | BASIC/Kernal | ❌ CORRUPTION |
| 40960-49151 | $A000-$BFFF | BASIC ROM | ❌ ROM (can't write) |
| 53248-53294 | $D000-$D02E | VIC-II Registers | ✅ HARDWARE (expected) |
| 54272-54295 | $D400-$D41C | SID Registers | ✅ HARDWARE (expected) |
| 55296-56295 | $D800-$DBE7 | Colour RAM | ✅ SAFE |
| 56320-56335 | $DC00-$DC0F | CIA 1 Registers | ✅ HARDWARE (expected) |
| 56576-56591 | $DD00-$DD0F | CIA 2 Registers | ✅ HARDWARE (expected) |

#### Special Notes (C64)

- **Zero page $FB-$FE**: Only safe zero page addresses
- **Screen memory**: 1024-2023 ($0400-$07E7) is safe
- **Colour memory**: 55296-56295 ($D800-$DBE7) mirrors every 1024 bytes
- **Hardware registers**: POKE to VIC-II/SID/CIA is expected

### Nintendo Entertainment System (NES)

#### Safe Ranges

| Range | Hex | Purpose | Safety |
|-------|-----|---------|--------|
| 0-255 | $0000-$00FF | Zero Page | ✅ SAFE (no OS) |
| 256-511 | $0100-$01FF | Stack | ⚠ USE CAREFULLY |
| 512-2047 | $0200-$07FF | RAM | ✅ SAFE |

#### Hardware Registers (VBlank timing required!)

| Range | Hex | Purpose | Timing |
|-------|-----|---------|--------|
| 8192-8199 | $2000-$2007 | PPU Registers | ⚠ VBLANK ONLY |
| 16384-16407 | $4000-$4017 | APU/Input Registers | ✅ ANYTIME |

#### Unsafe Ranges

| Range | Hex | Purpose | Risk |
|-------|-----|---------|------|
| 32768+ | $8000+ | ROM (PRG) | ❌ ROM (can't write) |

#### Special Notes (NES)

- **PPU writes**: MUST be during VBlank (or screen off)
- **OAM DMA**: $0200-$02FF commonly used for sprite data
- **Stack**: $0100-$01FF - use sparingly, grows down
- **Zero page**: Fully usable (unlike C64)

### ZX Spectrum

#### Safe Ranges

| Range | Hex | Purpose | Safety |
|-------|-----|---------|--------|
| 23296-65535 | $5B00-$FFFF | User Program RAM | ✅ SAFE |
| 23552+ | $5C00+ | BASIC Variable Area | ✅ SAFE |

#### Screen Memory

| Range | Hex | Purpose | Safety |
|-------|-----|---------|--------|
| 16384-22527 | $4000-$57FF | Screen Bitmap | ✅ SAFE (display) |
| 22528-23295 | $5800-$5AFF | Colour Attributes | ✅ SAFE (display) |

#### Unsafe Ranges

| Range | Hex | Purpose | Risk |
|-------|-----|---------|------|
| 0-16383 | $0000-$3FFF | ROM | ❌ ROM (can't write) |
| 23296-23551 | $5B00-$5BFF | System Variables | ❌ SYSTEM USE |

#### Special Notes (ZX Spectrum)

- **Screen memory**: Direct pixel manipulation at $4000-$57FF
- **Attributes**: Colour/flash at $5800-$5AFF (8×8 cells)
- **PRINT AT**: Uses screen memory automatically (safe)
- **No hardware registers**: Use IN/OUT for hardware (e.g., border)

### Commodore Amiga

#### Safe Ranges

| Range | Hex | Purpose | Safety |
|-------|-----|---------|--------|
| Chip RAM | $0000-$1FFFFF | Chip RAM (2MB max) | ✅ SAFE |
| Fast RAM | varies | Fast RAM (if present) | ✅ SAFE |

#### Hardware Registers

| Range | Hex | Purpose | Access |
|-------|-----|---------|--------|
| $DFF000-$DFF1FF | Custom Chip Registers | ⚠ USER MODE OK |
| $BFD000 | CIA-A | ✅ SAFE |
| $BFE001 | CIA-B | ✅ SAFE |

#### Unsafe Ranges

| Range | Hex | Purpose | Risk |
|-------|-----|---------|------|
| $F80000-$FFFFFF | Kickstart ROM | ❌ ROM (can't write) |
| $00000000-$00000400 | Exception Vectors | ⚠ SUPERVISOR ONLY |

#### Special Notes (Amiga)

- **32-bit addresses**: Use full 32-bit address space
- **Chip RAM**: Accessible by custom chips (blitter, copper)
- **Fast RAM**: CPU-only (faster but can't use for DMA)
- **Custom chips**: $DFF000 base, user mode accessible
- **Stack (A7)**: Never modify directly!

---

## Checking Memory Usage

### BASIC Programs

#### Manual Check Process

1. **Find all POKE statements**
   ```bash
   grep -ni "poke" example-1.bas
   ```

2. **Extract addresses**
   ```
   10 POKE 53280,0    → Address: 53280 ($D020)
   20 POKE 1024,160   → Address: 1024 ($0400)
   30 POKE 0,0        → Address: 0 ($0000) ← UNSAFE!
   ```

3. **Check against memory map**
   - 53280 ($D020) = VIC-II border colour ✅ SAFE (hardware)
   - 1024 ($0400) = Screen memory ✅ SAFE
   - 0 ($0000) = Zero page ❌ UNSAFE!

4. **Find all PEEK statements**
   ```bash
   grep -ni "peek" example-1.bas
   ```

5. **Check read safety**
   - Reading ROM: ✅ SAFE (read-only)
   - Reading hardware registers: ✅ SAFE (expected)
   - Reading screen memory: ✅ SAFE

#### Automated Check (Use Semantic Validator)

```bash
# C64 BASIC
python3 /scripts/validate-c64-basic.py example-1.bas

# ZX Spectrum BASIC
python3 /scripts/validate-zx-basic.py example-1.bas

# Amiga AMOS BASIC
python3 /scripts/validate-amiga-amos.py example-1.bas
```

### Assembly Programs

#### Manual Check Process

1. **Find all STA (store) instructions**
   ```bash
   grep -ni "STA" example-1.asm
   ```

2. **Extract addresses**
   ```asm
   STA $D020      → Address: $D020 (53280) ✅ VIC-II
   STA $0400      → Address: $0400 (1024) ✅ Screen
   STA $0000      → Address: $0000 (0) ❌ Zero page!
   ```

3. **Check zero page usage**
   - C64: Only $FB-$FE safe
   - NES: All zero page safe
   - Amiga: No zero page (32-bit addresses)

4. **Find indirect addressing**
   ```asm
   STA ($FB),Y    → Zero page pointer at $FB ✅ SAFE
   STA ($02),Y    → Zero page pointer at $02 ❌ UNSAFE (C64)
   ```

5. **Check hardware register access**
   - VIC-II: $D000-$D02E (C64) ✅ Expected
   - PPU: $2000-$2007 (NES) ⚠ VBlank required!
   - Custom chips: $DFF000+ (Amiga) ✅ Safe

#### Automated Check (Use Semantic Validator)

```bash
# C64 6510 Assembly
python3 /scripts/validate-c64-6510-asm.py example-1.asm

# NES 6502 Assembly
python3 /scripts/validate-nes-6502-asm.py example-1.asm

# ZX Spectrum Z80 Assembly
python3 /scripts/validate-zx-z80-asm.py example-1.asm

# Amiga 68K Assembly
python3 /scripts/validate-amiga-68k-asm.py example-1.asm
```

---

## Common Memory Errors by Platform

### C64: Zero Page Corruption

**Error:**
```basic
10 POKE 0,0    : REM Overwrites processor port!
```

**Why dangerous:**
- Address 0 is processor I/O port (memory banking)
- Writing wrong value switches ROMs in/out
- System crash or unpredictable behavior

**Fix:**
```basic
10 POKE 251,0  : REM Use safe zero page ($FB)
```

**Safe zero page (C64): $FB, $FC, $FD, $FE only.**

### C64: Stack Corruption

**Error:**
```asm
LDA #$00
STA $0100      ; Start of stack!
```

**Why dangerous:**
- Stack grows down from $01FF
- Overwriting stack corrupts return addresses
- Instant crash when RTS executed

**Fix:**
Don't write to $0100-$01FF directly. Use BASIC/user RAM instead.

### NES: PPU Write Outside VBlank

**Error:**
```asm
LDA #$00
STA $2006      ; PPU address (no VBlank wait!)
STA $2007      ; PPU data
```

**Why dangerous:**
- PPU busy during rendering (scanlines 0-239)
- Writing during rendering causes visual glitches
- May corrupt PPU internal state

**Fix:**
```asm
wait_vblank:
    BIT $2002
    BPL wait_vblank
    ; Now safe to write to PPU
    LDA #$00
    STA $2006
    STA $2007
```

### ZX Spectrum: PRINT AT Out of Bounds

**Error:**
```basic
10 PRINT AT 30,5;"HELLO"    : REM Row 30 > 21!
```

**Why dangerous:**
- Screen only has 22 rows (0-21)
- Writing beyond row 21 corrupts system variables
- Crash or unpredictable behavior

**Fix:**
```basic
10 PRINT AT 10,5;"HELLO"    : REM Row 10 is valid
```

### Amiga: Stack Pointer Corruption

**Error:**
```asm
MOVE.L #$10000,A7      ; Corrupting stack pointer!
```

**Why dangerous:**
- A7 is stack pointer
- Corrupting A7 = system crash immediately
- No recovery possible

**Fix:**
Never modify A7 directly. Use LINK/UNLK for stack frames.

---

## Memory Map Quick Reference

### C64 Safe Memory Summary

```
$0000-$00FA  ❌ Zero Page (system)
$00FB-$00FE  ✅ Zero Page (safe)
$00FF        ❌ Zero Page (system)
$0100-$01FF  ❌ Stack
$0200-$07FF  ❌ BASIC/Kernal
$0800-$9FFF  ✅ User Program
$A000-$BFFF  ❌ BASIC ROM
$C000-$CFFF  ⚠ RAM (if ROM disabled)
$D000-$D02E  ✅ VIC-II (hardware)
$D400-$D41C  ✅ SID (hardware)
$D800-$DBE7  ✅ Colour RAM
$DC00-$DC0F  ✅ CIA 1 (hardware)
$DD00-$DD0F  ✅ CIA 2 (hardware)
```

### NES Safe Memory Summary

```
$0000-$00FF  ✅ Zero Page (all safe)
$0100-$01FF  ⚠ Stack (use carefully)
$0200-$07FF  ✅ RAM
$2000-$2007  ⚠ PPU (VBlank only!)
$4000-$4017  ✅ APU/Input
$8000+       ❌ ROM (PRG)
```

### ZX Spectrum Safe Memory Summary

```
$0000-$3FFF  ❌ ROM
$4000-$57FF  ✅ Screen Bitmap
$5800-$5AFF  ✅ Colour Attributes
$5B00-$5BFF  ❌ System Variables
$5C00+       ✅ BASIC/User RAM
```

### Amiga Safe Memory Summary

```
$00000000-$001FFFFF  ✅ Chip RAM
$00200000+           ✅ Fast RAM (if present)
$00BFD000            ✅ CIA-A
$00BFE001            ✅ CIA-B
$00DFF000-$00DFF1FF  ✅ Custom Chips
$00F80000-$00FFFFFF  ❌ ROM
```

---

## Integration with Other Skills

**This skill is used by:**

1. **Semantic validators** - Memory map checks are core validation
2. **Platform-specific lesson creation skills** - Reference for safe memory
3. **lesson-validation** - Indirectly via semantic validators

**After finding memory issues:**

Run semantic validator to get detailed report with line numbers.

---

## Anti-Patterns

### 1. Using Decimal Addresses Without Hex

**Anti-pattern:**
```basic
10 POKE 53280,0    : REM What is 53280?
```

**Why suboptimal:**
Hard to verify against memory map (hex addresses).

**Fix:**
```basic
10 POKE 53280,0    : REM border colour ($D020)
```

**Always include hex in comments for hardware addresses.**

### 2. Not Checking Zero Page Safety

**Anti-pattern:**
```asm
LDA #$00
STA $02        ; Is $02 safe? (Depends on platform!)
```

**Why dangerous:**
- C64: $02 is SYSTEM, unsafe!
- NES: $02 is free, safe!

**Fix:**
Check platform-specific zero page map before using.

### 3. Writing to ROM

**Anti-pattern:**
```asm
LDA #$00
STA $A000      ; C64 BASIC ROM - can't write!
```

**Why wrong:**
ROM is read-only, writes are ignored (or crash).

**Fix:**
Only write to RAM ranges.

### 4. Assuming Same Memory Map

**Anti-pattern:**
"Sprites are at $D000 on C64, so they must be at $D000 on NES too!"

**Why wrong:**
Every platform has completely different memory map.

**Fix:**
Always check platform-specific memory map.

---

## Quick Memory Safety Checklist

**Before finalizing code:**

- [ ] All POKE addresses checked against memory map
- [ ] Zero page usage checked (C64: $FB-$FE only, NES: all safe)
- [ ] No stack corruption ($0100-$01FF on 6502/6510)
- [ ] Hardware register access appropriate (VIC-II, SID, PPU, etc.)
- [ ] PPU writes during VBlank (NES only)
- [ ] No writes to ROM ranges
- [ ] No system variable corruption
- [ ] Comments include hex addresses for hardware
- [ ] Semantic validator passes (no memory errors)

---

## Automated Checking

**For each platform, use semantic validator:**

```bash
# Check memory safety automatically
python3 /scripts/validate-{platform}-{language}.py code-file

# Exit code 0 = safe, 1 = memory errors
```

**Semantic validators include all memory map checks from this skill.**

---

## The Bottom Line

**Memory map checking prevents crashes and corruption:**

1. Check all POKE/STA against platform memory map
2. Use safe zero page only (C64: $FB-$FE, NES: all, Amiga: none)
3. Never write to stack directly ($0100-$01FF on 6502/6510)
4. Respect hardware timing (NES PPU requires VBlank)
5. Never write to ROM or system variables
6. Run semantic validator to catch issues automatically

**Zero tolerance for:**
- Zero page corruption (system crash)
- Stack corruption (instant crash)
- PPU writes outside VBlank (visual glitches)
- ROM writes (code doesn't work)
- System variable corruption (unpredictable behavior)

**Every platform has different memory layout. Always check platform-specific memory map before using direct memory access. Semantic validators automate this check.**
