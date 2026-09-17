# Quickstep prototype record

The user chose crossing and timing as the next BASIC prototype after Drift. The [bounded brief](brief.md) now has a runnable 48K PAL Sinclair BASIC listing and self-starting tape in `code-samples/sinclair-zx-spectrum/basic/quickstep/prototype/`. A native preview has been launched for play. The endpoint, difficulty and lesson sequence await user feedback; nothing is published on the website.

## Implemented trial

One board has three vehicle lanes, safe strips between them and a marked centre exit. Each vehicle occupies two logical cells. Two lanes move right every second update; the middle lane moves left every third. All phases reset with R. The opening vehicle positions require choosing a gap or moving sideways instead of holding up for an immediate straight crossing.

I/J/K/L steer, S starts, R retries and Q quits. At each beat the program consumes one movement command, combining a held key with the ROM's last-key latch. Recognised taps during drawing can survive until the next step. The latch holds one key, not an event history. A buffered step can happen after release; simultaneous keys and arbitrarily short taps are not guaranteed.

The player moves into a currently empty cell before due vehicles advance; a second occupancy check catches a vehicle arriving at the new player position. This also rejects exchanging places with a vehicle. Safe strips never collide, and the goal requires the centre tile rather than reaching any top-row cell. Geometry includes transparent sprite corners. Original UDG artwork provides the player, vehicles and strip texture. Play is deliberately silent.

## Execution evidence

Every line was independently entered through stock ROM keyword keys, saved with `SAVE "quickstep" LINE 10`, and loaded in fresh Emu198x Spectrum 0.25.0 processes. The final independent rebuild produced the same tape bytes and ROM-stored lines as the revised trial. `verification/evidence/build.json` records source, tape and executable hashes and the emulator identity.

The CPU-stepped checks compare keyboard-driven outcomes with an independent host model using occupied cell sets. They cover safe waiting over 90 beats, both wrap directions, all board bounds, the specific exit cell, complete crossing, both contact phases, result freezing, full reset and quit control flow. Input events are flushed through a zero-frame session run before CPU-only stepping; otherwise the session's queued key events are not applied. There is no game-state injection.

Separate ordinary-frame checks exercise held movement at a boundary, a four-frame tap during update work, a complete crossing, retry, collision, and quit from title, active play and result. Original title, arena, success and collision PNGs are retained. Their top 176 display rows are compared with the live RAM bitmap and colour attributes; screenshots are neither reconstructed nor edited. Captures were visually inspected.

`verification/evidence/manifest.json` records 20 passed execution check groups and audits the results, source/stored-line identities, both TAP block checksums and original capture hashes. CPU-stepped checks establish state transitions, not animation or timing. The native user's judgement of clarity, response and appeal remains a separate next check.

## Timing and refinements

The first ordinary-frame measurement found a median of 73 PAL frames between update commits. The revised loop keeps the player visible on resting strips, avoids reprinting unchanged lane arrows, and starts its 32-frame timing target before update work rather than adding a fixed wait afterwards.

The retained 1,200-frame resting trial observed 28 commit intervals, with a median of 39 frames and a range of 20–68. These are commit-to-commit intervals, not input latency: lane work varies and the commit happens later within busy updates. The 32-frame target spaces update starts; it is not a fixed-rate guarantee. No catch-up burst occurs after an overrun. These observations apply to this emulator/configuration and are not original-hardware measurements.

The initial input loop could discard a short press near the sampling boundary. Consuming one buffered command at the update boundary passes the retained short-tap and ordinary crossing checks. The first lane phases also allowed holding up to cross immediately; the revised opening makes a gap choice necessary. Neither the prototype's difficulty nor its final teaching scope is approved yet.
