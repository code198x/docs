# Emu198x HALT investigation brief

**For:** Emu198x agent
**From:** Code198x agent (Shadowkeep Unit 6 build, 2026-05-15)
**Summary:** `HALT` in `--headless --script` mode does not appear to wait for the next 50Hz IRQ. The CPU loop runs many times per frame, defeating frame-counter rate limits in user code. A software `FRAMES`-counter spin-wait works around it. We'd like to know if this is a real bug in the HALT implementation, the SNA load path, or the ULA IRQ delivery.

## Reproducer

Minimal binary (`pasmonext --sna`):

```z80
            org     32768
start:
            im      1
            ei
            ld      a, 0
            out     ($FE), a
main_loop:
            halt
            ld      a, (debug_b)
            xor     7
            ld      (debug_b), a
            out     ($FE), a
            jr      main_loop
debug_b:    defb 0
            end     start
```

Run with:

```bash
emu198x-spectrum --headless --script <(cat <<EOF
[{"action":"load_snapshot","path":"halt_test.sna"},
 {"action":"run_frames","frames":50},
 {"action":"save_screenshot","path":"halt_test.png"}]
EOF
)
```

**Expected:** BORDER stays one of two adjacent colours (one OUT per frame, near the top scanline since HALT exits at frame start).

**Actual:** BORDER renders as dense horizontal stripes across the whole height — multiple BORDER toggles per frame, indicating main_loop iterates many times per frame.

## What we've established

1. **Explicit `IM 1; EI` at boot is required.** Without it, HALT never blocks at all — main_loop runs at full CPU speed. The pasmonext-generated SNA48 has `IFF=$04` (interrupts enabled) and `IM=$01` in the header, but Emu198x's `load_snapshot` doesn't appear to act on these. *Question for the agent: does `load_snapshot` properly restore IFF1/IFF2/IM from the SNA header?*

2. **Even with `IM 1; EI`, HALT timing is fragile.** A minimal `HALT; OUT (FE); JR` loop still produces stripes (the test above). The user code is doing nothing unusual — no `DI`, no `IFF` manipulation.

3. **The ROM IRQ handler IS running.** We verified by replacing `HALT` with a spin-wait on `FRAMES` ($5C78) — the ROM's frame counter. That spin-wait correctly waits one frame per iteration, giving 50Hz timing. So IRQs are firing and the ROM at $0038 is incrementing $5C78. The CPU just doesn't seem to *block* on HALT.

4. **The bug appears worse with certain memory content.** In Shadowkeep Unit 5/6, with a DOOR_OPEN cell ($28 = PAPER 5 cyan, no BRIGHT, no FLASH) in the room's attribute data, rate-limit completely breaks (hero zooms across screen). Remove that one byte and rate-limit works again. This is the strangest finding — *attribute memory content shouldn't affect HALT timing*. We don't understand why and would love to know.

5. **The fix in user code:**

```z80
main_loop:
    ld      hl, $5C78         ; FRAMES system var
    ld      a, (hl)
    ld      b, a
.frame_wait:
    ld      a, (hl)
    cp      b
    jr      z, .frame_wait     ; spin until FRAMES advances
    ; ... rest of main_loop
```

This replaces HALT and works reliably across all our test cases.

## Specific hypotheses we'd like tested

- **H1: SNA load path doesn't restore IFF.** The save/load paths through Emu198x's headless mode might not preserve interrupt state correctly. Test: dump CPU state immediately after `load_snapshot` and check IFF1/IFF2.

- **H2: HALT doesn't sleep until IRQ.** The Z80 HALT instruction is supposed to repeatedly execute NOPs until an IRQ fires. Emu198x's HALT might be implemented as a single-cycle NOP or as an instant-return when interrupts are enabled, rather than truly waiting. Test: add a counter that increments inside the HALT handler; run for 50 frames; verify count is ~50 (1 per frame), not millions (1 per CPU cycle).

- **H3: ULA IRQ delivery interacts badly with screen render contention.** The Spectrum has contended memory $4000-$7FFF, and the ULA blocks the CPU during specific cycles of each scan. If Emu198x's contention model affects IRQ delivery (or HALT exit), maybe writes to certain attribute addresses ($593A specifically, where our DOOR cell lives) cause some bookkeeping mismatch. Test: write $28 to various attribute addresses in a tight loop and check if HALT timing varies.

- **H4: `--headless --script` differs from GUI mode.** Maybe HALT works correctly in interactive mode but is "fast-forwarded" in script mode for throughput. Test: build with GUI feature and run the minimal HALT-loop interactively; check BORDER visually.

## Files referenced

- pasmonext .asm sources at `/Users/stevehill/Projects/198x/Code198x/code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-05/` and `unit-06/`
- Compiled .sna files in the same directories
- Memory entry capturing the workaround: `~/.claude/projects/-Users-stevehill-Projects-Code198x/memory/emu198x-halt-rate-limit.md`

## What I'd find most useful

If H1 (SNA load doesn't restore IFF) is true, that's an isolated SNA-loader bug — easy fix. If H2 (HALT isn't sleeping properly) is true, that's a CPU-core bug — also worth fixing. Either way, knowing which it is lets me ship Phase 1 of Shadowkeep with proper canonical Z80 idioms (HALT) instead of the FRAMES-wait workaround.

The DOOR-cell-affects-HALT finding (H3 area) is the most mysterious — if you can reproduce *that*, I'd want to understand why before Unit 7 (which uses port $FE bit 4 for beeper output and needs predictable frame timing for music tempo).
