# Quickstep prototype record

The user chose crossing and timing as the next BASIC prototype after Drift. The [bounded brief](brief.md) now has a runnable 48K PAL Sinclair BASIC listing and self-starting tape in `code-samples/sinclair-zx-spectrum/basic/quickstep/prototype/`. The first native trial worked, but the user found it too easy and too small. A larger, harder revision is now open for play. The endpoint, difficulty and lesson sequence await further user feedback; nothing is published on the website.

## Implemented trial

The 15×9 board occupies 240×144 pixels, with six vehicle lanes arranged in two banks of three. Safe ground exists only at the start, halfway point and finish. Each lane has three two-cell vehicles with three-cell gaps. Directions alternate; lane periods from top to bottom are three, four, two, three, four and two updates. All phases reset with R. The shortest opening route found by breadth-first search takes 16 updates, including lateral moves and waits, versus ten on the first trial. The exact route also completes under ordinary frame execution.

I/J/K/L steer, S starts, R retries and Q quits. At each beat the program consumes one movement command, combining a held key with the ROM's last-key latch. Recognised taps during drawing can survive until the next step. The latch holds one key, not an event history. A buffered step can happen after release; simultaneous keys and arbitrarily short taps are not guaranteed.

The player moves into a currently empty cell before due vehicles advance; a second occupancy check catches a vehicle arriving at the new player position. This also rejects exchanging places with a vehicle. Safe strips never collide, and the goal requires the centre tile rather than reaching any top-row cell. Geometry includes transparent sprite corners. Original UDG artwork provides the player, vehicles and strip texture. Play is deliberately silent.

## Execution evidence

Every line was independently entered through stock ROM keyword keys, saved with `SAVE "quickstep" LINE 10`, and loaded in fresh Emu198x Spectrum 0.25.0 processes. `verification/evidence/build.json` records source, tape and executable hashes and the emulator identity.

The CPU-stepped checks compare keyboard-driven outcomes with an independent host model using occupied cell sets. They cover safe waiting over 90 beats, both wrap directions, all board bounds, the specific exit cell, complete crossing, both contact phases, result freezing, full reset and quit control flow. Input events are flushed through a zero-frame session run before CPU-only stepping; otherwise the session's queued key events are not applied. There is no game-state injection.

Separate ordinary-frame checks exercise held movement at a boundary, a four-frame tap during update work, a complete crossing, retry, collision, and quit from title, active play and result. Original title, arena, success and collision PNGs are retained. Their top 176 display rows are compared with the live RAM bitmap and colour attributes; screenshots are neither reconstructed nor edited. Captures were visually inspected.

`verification/evidence/manifest.json` records 20 passed execution check groups and audits the results, source/stored-line identities, both TAP block checksums and original capture hashes. CPU-stepped checks establish state transitions, not animation or timing. The native user's judgement of clarity, response and appeal remains a separate next check.

## Timing and refinements

The retained 1,200-frame resting trial observed 22 consecutive commit intervals, with a median of 46 PAL frames and a range of 25–99. This is slower than the smaller board’s median of 39 frames. These are commit-to-commit intervals, not input latency: lane work varies and the commit happens later within busy updates. The 32-frame target spaces update starts; it is not a fixed-rate guarantee. No catch-up burst occurs after an overrun. These observations apply to this emulator/configuration and are not original-hardware measurements. Native review needs to judge whether the fuller crossing remains responsive enough.

The ordinary-frame crossing harness observes the update counter directly. Waiting specifically to sample line 200 could miss several updates on the busier board, leaving its planned commands behind the traffic. This was an observation error in the trial, not a change to the game’s collision rules. The revised harness completes the 16-update route, and the separate cadence check confirms every consecutive update was observed.

The buffered input still passes the four-frame tap and held-key checks. The revised board and original captures have been inspected, and the native preview reopened. Difficulty and final teaching scope remain unapproved.
