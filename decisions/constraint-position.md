# Decision: Constraint Position Taxonomy

## The decision

Each game declares its **constraint position** — which subset of era-period techniques it uses — explicitly in brief Section 5. Three positions, tightest to loosest:

- **Period-faithful.** Only techniques common in commercial era games. A 1984 Ultimate dev with three weeks could have built it this way.
- **Period-possible.** Techniques that existed and were technically possible in the era, even if vanishingly rare in commercial product. Often required cycle-counting or skills most commercial devs didn't have time for.
- **Modern scene.** Techniques that the hardware allowed but that were codified later (typically the 2010s onwards) through collaborative effort in the demoscene and homebrew community.

A game can sit at one position across all phases, or move along the spectrum — earlier phases period-faithful, later phases incorporating period-possible or modern-scene techniques. The position must be explicit per phase, not implicit.

## Why

"Could-have-shipped" — the previous loose framing — papered over a real distinction. Modern Spectrum-scene techniques like Einar Saukas-era 8x1 multicolour, software sprites, and interrupt-driven AY routines are technically possible on 1980s hardware. But they didn't ship commercially in 1987 because:

- **Time/economics.** £2.99 budget devs couldn't spend two weeks optimising raster routines.
- **Standardisation lag.** Many modern-scene recipes were codified in the 2010s through collaborative effort, not invented in 1987.
- **Knowledge distribution.** What we now treat as "the right way" wasn't documented yet.

A Phase 4 Shadowkeep using modern 8x1 multicolour isn't really a 1987 commercial game — it's a 1987-spec game built with 2025 knowledge. Pretending otherwise misrepresents the period and obscures what the curriculum is actually teaching.

The taxonomy makes this explicit. The curriculum honestly distinguishes "what 1987 looked like" from "what we now know was possible on 1987 hardware." That's not a weakness; it's a pedagogically richer position — the learner gets both the period-common technique and the modern improvement, with the historical context spelled out.

## What this means

### In briefs

Brief Section 5 (Constraint position) names the position(s) the game occupies. If the position varies by phase, Section 7 (Phase trajectory) names the position per phase.

### In units

A unit teaching a modern-scene technique explicitly contextualises it. Example: a unit teaching 8x1 multicolour reads "This technique was technically possible in 1987 but became standard practice in the modern Spectrum scene from the 2010s onwards. Here's how it works, and why 1987 commercial devs mostly didn't use it."

A unit teaching a period-faithful technique doesn't need this framing — but noting *that* the technique was period-common is worth a line.

### In marketing

The Code198x voice doesn't conflate "could-have-shipped" with "did-ship." A game in modern-scene position isn't marketed as "what 1987 looked like." It's marketed as "what's possible on 1987 hardware with 2025 understanding."

### In progression

For most games, expect early phases to be period-faithful (learners need to absorb foundational hardware knowledge before reaching for advanced techniques) and later phases to incorporate period-possible or modern-scene work as the learner can support it. This isn't a rule — some games might sit at one position throughout. It's a default to expect.

### Per-platform calibration

The taxonomy applies to each platform, but the dates and named techniques differ. As a rough sketch:

- **ZX Spectrum:** hardware era 1982–1992. Modern scene includes 8x1 multicolour (Einar Saukas era, 2010s), modern AY techniques.
- **Commodore 64:** hardware era 1982–1994. Modern scene includes advanced SID coding, modern compressor work (Exomizer and successors).
- **NES:** hardware era 1985–1995. Modern scene includes advanced mapper homebrew and modern CHR techniques.
- **Amiga:** hardware era 1985–1996. Modern scene includes post-Commodore demoscene Copper tricks and modern Paula audio.

Detail per platform belongs in the platform-specific reference pages in `docs/platforms/`, not here.

## Drift triggers

If a brief or unit shows any of these patterns, stop and re-read this decision:

- "It's possible on the hardware, so we can use it" without naming a constraint position.
- Modern-scene techniques appearing in period-faithful units without explicit historical framing.
- Marketing copy that says "this is what 1987 looked like" when the game uses modern-scene techniques.
- A game's brief Section 5 with multiple positions named but no per-phase mapping in Section 7.
- A "period-faithful" game whose references include techniques that didn't appear commercially until much later.
- Conflating "could-have-shipped" with "did-ship" anywhere in copy.

## Status

Active. Captured 2026-05-13. Descends from [real-retro-games.md](real-retro-games.md). The honest framing for the curriculum's relationship to the era it teaches.
