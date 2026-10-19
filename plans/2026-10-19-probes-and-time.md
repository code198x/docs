# Probe coverage and independent timing choices

Continue the approved Pattern Library expansion without changing launch priorities or implying a complete curriculum track.

1. Update `specifications/pattern-library.md` and `guides/game-loops.md`: distinguish turn progression, clocks/deadlines, input handling and presentation scheduling. Timed turns can combine them; no compulsory frame wait for an untimed input/output game.
2. Update the existing cross-platform `game-loop-choices.mdx` article in the website with concrete combinations and integration advice. Preserve routes and layout.
3. Inventory all 30 machine IDs from Emu198x `docs/status/systems.toml`, retaining its explicit crate joins. Record the six already qualified configurations separately from planned work; extend towards all catalogue systems without implying current support.
4. Add the next small runnable homebrew probes in code-samples, reusing established runtime/debug transports and source contracts where appropriate. Keep machine-specific mode, input, memory and interrupt ownership explicit. Retain assembly, execution and negative-control results separately. Do not mark an emulator build as a passing probe.
5. Verify changed source/callers and the rendered article; run failing controls, source/registry coverage checks and diff checks. Push self-contained updates to the existing open PR branches. Update parent #117 with precise progress and remaining coverage. No merge/deploy is authorised.

Temporary resources: three linked worktrees under the chat's `work/probe-expansion/`; bounded native build under that directory or `/tmp`; remove after verified remote retention and preserve user-facing evidence under `outputs/`.
