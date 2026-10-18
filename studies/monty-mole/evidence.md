# Wanted: Monty Mole — evidence and limits

Research pass: 18 October 2026. Reader-facing scope: Peter Harrap’s 1984 ZX Spectrum game, published by Gremlin Graphics. This is a substantial first reading draft, not historical sign-off or a complete playthrough.

## Executed and inspected

An already-held Z80 snapshot labelled `Wanted - Monty Mole (1984)(Gremlin Graphics).z80` supplied the run. SHA256: `08f1eb380cd62780cee7da145c059530ee27c2f8d9c5f1ab5cb301c8c00154d0`. A catalogue label is preservation identity, not independent proof of authenticity. No game binary, snapshot, firmware or full-screen gallery is included.

Emu198x Spectrum 0.32.5, 48K model with held firmware; headless, audio disabled. Starting with the snapshot: hold Space for five native frames, release for one, run 100; select 0 for 100 frames, release for one and run ten. This reached the surface. From that retained session state, hold P for 16, release for one, then P for 16 and release for one: the second observation supplies the first mine room. Inputs were emitted as shared script `input` / `run_frames` steps. Time counts are emulator frames, not measured original-hardware latency.

A separate TAP attempt (`8c4e5a24154c578deb1116b789c4a79a3f9916938a0089d63f183f748d3c8008`) remained at the loader after 18,000 frames. It did not supply the published images. Later exploratory snapshot sessions stopped showing useful progress. They do not establish bucket collection, a measured jump curve, crusher probabilities, completion, or a reliable complete emulation session. No emulator modification was attempted within this writing task.

| Claim | Evidence boundary |
|---|---|
| Surface arrangement; first room ropes, ledges, crusher and colour | Own inspected selected frames; original Spectrum inlay and CRASH review corroborate identification. |
| Controls, three lives, bucket prerequisite, 21 levels, castle/ballot framing | Original inlay transcription; CRASH 9 independently describes the bucket hiding coal until collected. Not independently executed through all these states. |
| Object dependencies and changed routes | CRASH 9 and CRASH 21 contemporary accounts, not a claimed exhaustive traversal. |
| Uncertainty at crushers | CRASH 9’s reviewer explicitly calls out luck. No inspected original code or calibrated random distribution; do not claim a specific probability or routine. |
| Generic jump arc, timing/readability, repetition costs | Our explanatory comparison and design interpretation, not a measured engine reconstruction or player study. Diagram explicitly says so. |
| Family circumstances and frustration | Harrap’s retrospective answer in Peter Ward’s interview. Attribute it; avoid inferred psychological, financial or political details. |
| Shop, Stewart/Norburn and publicity | Roger Kean’s contemporary 1985 visit/interview. Stewart’s role in the idea and publicity is his account; not an independently reconstructed contract history. |
| Strike and ballot context | People’s History Museum’s historical account. Regional differences retained. No claim the game fairly represents all participants or that family circumstances establish an ideology. |
| Review price, score and reactions | CRASH 9; price at review, not every edition. No audited sales total. |
| Later Monty soundtrack | Existing Monty on the Run Vault sources; not applied to the 1984 game. No audio distributed or evaluated in this run. |

## Images and rights

Two proportionate self-captured stills support the surface/route and first-mine-room discussions. Each crops `(48,48,304,240)` from 352×296 emulator output to the 256×192 active display, without retouching or interpolation. PNG Source metadata identifies game, publisher, year, platform and capture tool. [captures/manifest.json](captures/manifest.json) records byte hashes and claims. Rights in the game remain with their owners; publication use is criticism/review under the existing capture decision, not an open licence for the underlying artwork.

The jump diagram is original, schematic and explicitly not Monty’s measured trajectory; its phone variant explains the same relationship. Header artwork is an imagined editorial cutaway, not a historical mining reconstruction, screenshot, cover reproduction or claim about actual map layout. [Artwork provenance](artwork/provenance.json) retains exact built-in image-generation prompt, transformations and hashes. No stock image, third-party screenshot, full mine map, walkthrough, music, video, tape or snapshot is distributed.

## Review before publication

Owner reading and historical/editorial sign-off remain open. Complete original-hardware validation and full-game execution are not claimed or required for the selected image claims. A future deeper technical account of jumps or crushers needs new execution/source evidence, not more confidence in this draft. Do not turn the current exploratory emulator limitation into a statement about the historical game.
