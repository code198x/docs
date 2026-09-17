# Brick Bash — prototype brief

**Status:** The user agreed to a bounded native BASIC prototype after Tail Chase. Scope is one ball, one horizontal paddle and three rows of six bricks. Native feedback reports that it works and is surprisingly tough; see the [execution record](prototype.md). The user agreed to retain this baseline and develop its teaching progression; the [lesson brief](lesson-brief.md) defines ten lessons supported by [nine executed checkpoints](lessons.md).
**Target:** Stock 48K ZX Spectrum, PAL, Sinclair BASIC, keyboard and ROM tape loading. No runtime extensions or machine-code helper.
**Sources:** `code-samples/sinclair-zx-spectrum/basic/brick-bash/prototype/`. The reviewed game and ten-lesson progression replace the inherited website proposal.

## Round and controls

Clear all eighteen bricks without missing the ball. O/P move the paddle, SPACE serves from a ready state, R restores the round and Q leaves. A miss or cleared wall freezes play and offers another attempt. Paddle contact has three zones that return the ball left, vertically or right; the player can choose a route through the wall rather than merely intercepting it.

The prototype uses a two-by-two pixel ball, a four-character paddle and eighteen three-character bricks. Colours distinguish rows; disappearance and the BRICKS count report progress. Six original UDGs supply rounded brick and paddle ends. The round is deliberately silent while movement and response are evaluated. There are no extra levels, lives, power-ups or speed ramp in this trial.

## Rule representation

Pixel positions and a 3×6 occupancy array determine contact. Screen colour and POINT do not decide collision. The ball's lower-left coordinate describes a 2×2 bounding box. A brick occupies its 24×8 character rectangle, including the tiny unlit corner pixels of its artwork. The paddle's top plane and width define its contact rule.

The candidate advances by at most four pixels on each axis. Resolve outer-wall reflection, then paddle contact, then brick contact by checking horizontal movement at the old height followed by vertical movement at the resolved horizontal position. On a brick hit, reject that axis's displacement, reverse its direction and remove the brick once. This axis order deliberately settles diagonal-corner ambiguity; it is not an exact continuous billiards simulation. Verify that the resulting ball is outside all remaining bricks. Brick gaps and thickness must be checked against the movement size before increasing speed.

The paddle is positioned on character columns and moves eight pixels per accepted O/P poll. The ball uses finer pixel coordinates. Holding a direction repeats; the world continues without a key. Initial pacing is the work of the BASIC loop, not a claimed fixed frame interval. Measure ordinary, contact and redraw updates, then judge native response. Readable, playable movement is the acceptance condition; a measured weakness may require changing this bounded design, not beginning the deferred assembly investigation.

## Teaching role

Volley supplies position, reflection and a paddle. Crates and Tail Chase supply state-based collision and safe updates. This game can introduce pixel versus character coordinate systems, rectangular overlap, mapping pixels to a stored brick, destructible state and choosing a return direction through contact position. Recall familiar arrays, UDGs and polling locally.

The [agreed teaching progression](lesson-brief.md) develops pixel drawing and movement, the paddle and serve, catches, one brick, a wall-coordinate inspector, complete wall destruction, aiming, finishing and saving. Nine executed checkpoints support ten lessons. The inherited catalogue keyword list does not require teaching every graphics command.

## Verification and play review

Enter source through actual ROM keyword keys, save a self-starting tape and load it in a fresh 48K session. Compare each observed move with a host-side model of the stated geometry; host code is a verification tool, not a game dependency. Exercise both side walls, the top, paddle edges and all three return zones, misses, brick faces and diagonal corners, already removed bricks, full clearance, R and Q from every phase, held keys and replay state. Check all eighteen occupancy cells and the BRICKS count after changes. Label any deterministic diagnostic source separately from ordinary gameplay.

Inspect original artwork and captures. Observe the moving ball and control response in native play; static images cannot establish either. Record source/tape/emulator/ROM identities and limits of the evidence. A technically correct but sluggish or repetitive game needs revision before lesson drafting.

Primary language reference: Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (Sinclair Research, 1983), chapters 3–6, 12, 14–18 and 20, particularly chapter 17 for pixel plotting/drawing and chapter 18 for input. Game rules and original artwork are project choices under the samples repository's MIT licence.
