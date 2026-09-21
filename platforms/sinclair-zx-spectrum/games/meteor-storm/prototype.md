# Meteor Storm — native prototype

**Status:** Accepted after native play. The user confirmed: “Sorted. Perfect.
Let's proceed with this.” The [teaching progression](lesson-brief.md) proposes
how to develop this accepted game into the replacement first assembly module.

Accepted source SHA-256: `fefac65915baa0a2fa29395a7ff8f19fac9c2261b11073ebd37e7a602d302f4d`.
Accepted tape SHA-256: `99bf888e88ab29e65908aa755b8a0e99be37f6a95f132926c90755aa35414e9a`.
The matching evidence report contains 46 passed native check groups.

The [brief](brief.md) defines the scope. Sources, original pixel artwork,
verification scripts and evidence live in
`code-samples/sinclair-zx-spectrum/assembly/meteor-storm/prototype/`.

## Playable baseline

The user rejected the uniform rows as boring and requested independent X positions,
varied falling speeds and an optional boost. After completing that trial first time, the user requested gentle sideways
variation and bonuses. The revised trial scatters 100 meteors and 20 stars
at pixel positions across the screen, falling at 2, 3, 4 or 5 pixels per course step.
Faster objects can overtake slower ones. Meteors drift -1, 0 or +1 pixel
horizontally every four course steps, reflecting at the edges. Stars fall straight
down. This reduces sideways meteor speed to a quarter of the previous trial
after the user found its drift excessive. The reproducible event schedule is
prepared on the host and verified; it does not require a runtime random generator.

The user requested a speed-focused timed run with unlimited boost and competing
time/score records. Hold Space for double-speed travel through the same fixed
course; release to return to normal speed. O/P steer, R retries and Q returns
to the title. Both steering keys cancel. One meteor hit ends the run.

Stars award 10 points normally or 20 while boosting. Successful arrival adds
10 points for every whole second below 100 seconds, calculated as
`10 × max(0, 100 − floor(elapsed seconds))`. A failed run gets no finish bonus.
The timer counts elapsed PAL frames independently of course steps. Arrival waits
for the last object to pass; fatal contact takes precedence. Full boost advances
two collision-checked steps per update, bringing objects and encounters towards
the ship twice as fast. Steering also advances with each course step.

Separate records keep the fastest successful completion and highest score.
They survive retries and title returns within the running program. Failed runs
can set a score record but cannot replace a successful time. Restarting the
program resets both records; no disk or tape persistence is claimed.

The course remains 1046 simulation steps: 41.84 seconds normally or 20.92 seconds
at full boost. Stars fall vertically; meteor drift remains one pixel per four
course steps. Boost therefore speeds up the field without introducing erratic
sideways motion.

Entry is 32768, stack $FCF0; a private IM2 clock uses the $FE00–$FF00 vector table
and $FDFD jump. Explicit positions and inset rectangles govern collision. A
20-slot collection peaks at nine active meteors in the host schedule. Each object
stores its own speed, drift, kind and previous image position. Both boosted
physics steps run before each meteor is erased and redrawn once, keeping the
25 Hz update cadence. XOR drawing preserves overlapping objects. Rendering and interrupt choices still need teaching review.

## Evidence and limits

Asm198x builds the tape with its BASIC loader and a separate verification
snapshot using explicit Z80 and pasmonext options. The evidence report records
source, tape and emulator identities. Verification uses the Emu198x stock 48K
PAL configuration; this is emulator evidence, not a physical-machine claim.

The native harness checks normal and full-boost completion, records and scoring alongside
opposing keys, held launch, title return, first-hit destruction, frozen results,
retry reset, vertical star motion, limited meteor drift, star scoring, score retention, and a complete keyboard-driven passage with the single life intact.
It measures a two-frame update cadence and checks the bounded object pool.
A separate fresh machine loads the actual tape through the ROM and reaches play.
No state writes or CPU stepping stage these outcomes. Title lines are centred
from their actual lengths; the text routine clips at the 32-column, 24-row bounds.
A native bitmap check compares every title glyph and both margins with the ROM
font, detecting wraparound rather than relying solely on screenshots.

An independent host tick model finds a damage-free route through the scattered field.
Native keyboard runs exercise that route at normal speed and full boost.
All 109 stationary ship positions fail, so staying in one lane cannot win this
schedule. This proves route availability and the need to move; it does not prove
that a human can read the route comfortably or that the game is enjoyable.

Flight and result captures are retained with the route and impact audio.
The user accepted the game after native play. Independent listening of the
retained sound capture is not separately recorded. Next, execute the proposed
teaching checkpoints before authoring or publishing replacement lessons.
