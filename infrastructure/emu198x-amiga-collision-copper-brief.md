# Emu198x handoff — Amiga CLXDAT read unwired + Copper line-255 wrap

**From:** Code198x session, 2026-06-11, authoring Flock units 6–7 (sprite collision).
**Blocks:** Flock unit 6 (pulled from publication) and unit 7 (written, unverifiable, uncommitted).
**For:** the Emu198x session — both findings verified against Emu198x source; pointers below.

## 1. CLXDAT read is unwired (the blocker)

Reading `$DFF00E` (CLXDAT) falls through the machine's register-read dispatch to the
unimplemented-register arm and returns `$FFFF` — every collision bit set, every read, always.

- `crates/machine-commodore-amiga-ocs/src/lib.rs` ~line 1989: the read `match offset` has arms
  for VPOSR/JOYxDAT/etc. and `_ => 0xFFFF`. **No `0x00E` arm.**
- `crates/commodore-denise-ocs/src/chip.rs` line 334: `pub fn read_clxdat(&mut self) -> u16`
  exists, implements clear-on-read, and the per-pixel latch logic (`latch_collisions`,
  `collision_group_mask`) looks sound — it's only the machine wiring that's missing.
- CLXCON **write** is fine: `$098` falls through to `denise.write_word`, handled at chip.rs:228.

**Fix sketch:** add `0x00E => self.denise.read_clxdat(),` to the read dispatch. Check the ECS
machine (`machine-commodore-amiga-ecs`) for the same gap. Existing test scaffolding:
`commodore-denise-ocs/tests/sprites_collisions.rs` (chip level) and
`machine-commodore-amiga-ocs/tests/m7_chipset_reads.rs` (dispatch level) — a dispatch-level
CLXDAT case would have caught this.

**Symptom that found it:** a sheep-vs-tractor game read CLXDAT bit 9 each frame; with $FFFF the
player respawned every frame from boot. (Also why any CLXDAT-polling game/demo will misbehave.)

## 2. Copper WAIT fires immediately after crossing line 255

The canonical PAL-bottom technique — `dc.w $FFDF,$FFFE` to cross beam line 255, then a WAIT for
a low line number to address lines 256+ — fires **instantly at line 256** instead of waiting.
Measured on screen: a `$1C01` wait after the `$FFDF` crossing applied its colour change at beam
line 256 (screen row 212) instead of line 284 (row 240). Looks like the post-wrap comparison
sees the full 9-bit beam line (V8 included), so `256+ ≥ $1C` matches immediately; real hardware
compares V[7:0] only (which is why the $FFDF trick exists).

- Likely home: the Copper WAIT comparison in `crates/commodore-agnus-ocs` (copper module).
- Workaround in content: Flock keeps its HUD strip at row 208 (line `$FC`) so nothing crosses
  255. Fine for now; Arc 2 polish and any full-height PAL effects will want the real behaviour.

## 3. Minor: sprite shifter leaves `spr_current_code` stale at line end

`commodore-denise-ocs/src/chip.rs` ~line 541: when `spr_shift_count` hits 0 the loop `continue`s
without clearing `spr_current_code[sprite]`, so a sprite whose **rightmost pixel is solid**
keeps "colliding" for the rest of the scanline (until the per-line reset). Not what bit us —
Flock's sprites end in transparent columns — but it'll produce phantom right-edge collision
trails once CLXDAT is readable. One `self.spr_current_code[sprite] = 0;` on shifter exhaustion.

## On the Code198x side, waiting on #1

- Flock unit 6 (`Squashed`) — published then **pulled** (`available: false`) because its
  verification was invalidated by #1; re-verify + recapture + caption check after the fix.
- Flock unit 7 (`The Flock in Hand`) — code complete in
  `code-samples/commodore-amiga/assembly/flock/unit-07/` (uncommitted), including a CLXDAT
  latch-flush at squash-beat end and collision-safe parking for unused sprite channels.
