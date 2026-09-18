# System curriculum and game-design material

This directory holds system-specific curriculum specifications alongside retained game briefs, development plans and prototype investigations for review. It does not contain canonical hardware references, language manuals or system-support status. [PROJECT.md](../PROJECT.md) governs direction; [current work](../work.md#spectrum-sequences) scopes the next review.

Use these designs alongside authored lessons, sample sources and capture manifests. Their mechanics and observations are useful evidence; old counts, ordering, tool availability and historical comparisons need checking. No existing brief becomes an approved replacement sequence by surviving this cleanup.

## Current specifications

| System | Module | Status |
|---|---|---|
| ZX Spectrum | [Meet BASIC](sinclair-zx-spectrum/basic/meet-basic.md) | All fifteen lessons published; [lesson/source and verification record](sinclair-zx-spectrum/basic/meet-basic-plan.md) |
| ZX Spectrum | [Bright Spark](sinclair-zx-spectrum/games/bright-spark/brief.md) | Seven replacement lessons published |
| ZX Spectrum | [Volley](sinclair-zx-spectrum/games/volley/brief.md) | Eight approved lessons published; [prototype and teaching record](sinclair-zx-spectrum/games/volley/prototype.md) |
| ZX Spectrum | [Touchdown](sinclair-zx-spectrum/games/touchdown/brief.md) | Moving lander and landscape scope agreed; [six-stage prototype](sinclair-zx-spectrum/games/touchdown/prototype.md) played; [eleven-lesson brief](sinclair-zx-spectrum/games/touchdown/lesson-brief.md) proposed for review |

| ZX Spectrum | [Tail Chase](sinclair-zx-spectrum/games/tail-chase/brief.md) | Native prototype accepted; [execution record](sinclair-zx-spectrum/games/tail-chase/prototype.md); [twelve checkpoints and ten published lessons](sinclair-zx-spectrum/games/tail-chase/lessons.md) |

| ZX Spectrum | [Brick Bash](sinclair-zx-spectrum/games/brick-bash/brief.md) | Native feedback: working and surprisingly tough; [fourteen-check execution record](sinclair-zx-spectrum/games/brick-bash/prototype.md); [ten-lesson progression](sinclair-zx-spectrum/games/brick-bash/lesson-brief.md) with [nine executed checkpoints](sinclair-zx-spectrum/games/brick-bash/lessons.md); approved overview and ten lessons published after Tail Chase |
| ZX Spectrum | [Drift](sinclair-zx-spectrum/games/drift/brief.md) | Accepted after native docking with velocity feedback; [six executed checkpoints](sinclair-zx-spectrum/games/drift/lessons.md) support an [eight-lesson progression](sinclair-zx-spectrum/games/drift/lesson-brief.md), with the approved overview and eight lessons published after Brick Bash |
| ZX Spectrum | [Quickstep](sinclair-zx-spectrum/games/quickstep/brief.md) | Six-lane BASIC baseline accepted; overview and ten approved lessons [published with live checks](sinclair-zx-spectrum/games/quickstep/lessons.md) |
| ZX Spectrum | [Locksmith](sinclair-zx-spectrum/games/locksmith/brief.md) | Approved BASIC overview and nine lessons published; seven [executed checkpoints](sinclair-zx-spectrum/games/locksmith/lessons.md), live checks passed |
| ZX Spectrum | [Three in a Row](sinclair-zx-spectrum/games/three-in-a-row/brief.md) | Native BASIC game accepted; ten replacement lessons published with eight verified checkpoints |

The [BASIC performance-revisit proposal](sinclair-zx-spectrum/basic/performance-revisits.md) has an agreed basis but is deferred while the initial BASIC versions take priority. It explores how measured limits in existing games could motivate selected assembly work. It does not establish a performance ceiling or a replacement assembly sequence.

## Existing briefs

| System | Game |
|---|---|
| Commodore 64 | [Bleeper](commodore-64/games/bleeper/brief.md) |
| Commodore 64 | [Dropzone](commodore-64/games/dropzone/brief.md) |
| Commodore 64 | [Oracle](commodore-64/games/oracle/brief.md) |
| Commodore 64 | [Reflex](commodore-64/games/reflex/brief.md) |
| Commodore 64 | [Rover](commodore-64/games/rover/brief.md) |
| Commodore 64 | [Safe Cracker](commodore-64/games/safe-cracker/brief.md) |
| Commodore 64 | [Skyline](commodore-64/games/skyline/brief.md) |
| Commodore 64 | [Starfield](commodore-64/games/starfield/brief.md) |
| Commodore 64 | [Tally](commodore-64/games/tally/brief.md) |
| Commodore Amiga | [Exodus (rung-2 Blitter puzzle)](commodore-amiga/games/exodus/brief.md) |
| Commodore Amiga | [Flock](commodore-amiga/games/flock/brief.md) |
| ZX Spectrum | [Cipher](sinclair-zx-spectrum/games/cipher/brief.md) |
| ZX Spectrum | [Crates](sinclair-zx-spectrum/games/crates/brief.md) |
| ZX Spectrum | [Dice Roller](sinclair-zx-spectrum/games/dice-roller/brief.md) |
| ZX Spectrum | [Gloaming](sinclair-zx-spectrum/games/gloaming/brief.md) |
| ZX Spectrum | [Locksmith](sinclair-zx-spectrum/games/locksmith/brief.md) |
| ZX Spectrum | [Lucky Number](sinclair-zx-spectrum/games/lucky-number/brief.md) |
| ZX Spectrum | [Oracle Stone](sinclair-zx-spectrum/games/oracle-stone/brief.md) |
| ZX Spectrum | [Shadowkeep](sinclair-zx-spectrum/games/shadowkeep/brief.md) |
| ZX Spectrum | [Sonar](sinclair-zx-spectrum/games/sonar/brief.md) |
| ZX Spectrum | [Story Builder](sinclair-zx-spectrum/games/story-builder/brief.md) |
| ZX Spectrum | [The Caverns](sinclair-zx-spectrum/games/the-caverns/brief.md) |
| ZX Spectrum | [Three in a Row](sinclair-zx-spectrum/games/three-in-a-row/brief.md) |
| ZX Spectrum | [Yearfall](sinclair-zx-spectrum/games/yearfall/brief.md) |

Additional designs without a `brief.md` are [Blockstorm](sinclair-zx-spectrum/games/blockstorm/spec.md), [Dorin](sinclair-zx-spectrum/games/dorin/spec.md) and [Night Patrol](sinclair-zx-spectrum/games/night-patrol/spec.md). The [NES Dash investigation](nintendo-entertainment-system/games/dash/design-stress-2026-07-05.md) and [The Long Night investigation](sinclair-zx-spectrum/games/the-long-night/design-stress-2026-07-05.md) also remain useful review evidence. Other files beside the briefs contain specific game specifications, prototype observations or development plans. Source and executable evidence remain in the sample repository; this directory does not prove the current build or playability of a game.

When a design is re-specified, replace obsolete passages and retire redundant companion files rather than appending amendment banners. Create new game briefs only for agreed review work, using the [brief specification](../specifications/brief.md).
