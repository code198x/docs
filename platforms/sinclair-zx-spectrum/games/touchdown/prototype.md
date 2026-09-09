# Touchdown prototype

The sample repository's `sinclair-zx-spectrum/basic/touchdown/prototype/` holds the replacement investigation. Published Touchdown lessons remain unchanged. This is a prototype for play and teaching review, not an approved lesson breakdown.

## Chosen representation

One character is the craft's collision footprint. Two original UDG patterns show its resting and burning states within that same cell. The flame therefore cannot overwrite the ground below the craft. The skyline uses `#`, the four-cell pad uses `=`, and PAPER fills the solid terrain. The same 32-entry height array supplies both rendering and contact tests.

Vertical position and speed use hundredths of a character row. Gravity adds 2 per update; thrust subtracts 6 and uses one fuel unit. Starting fuel is 45. The current safe downward speed is 0–12. These are provisional play values, not physical units or a fixed-time simulation. Downward speed is capped at 60, upward speed at −30; the ceiling clamps position and cancels upward speed. Sideways control moves one column per update without momentum.

O and P steer; Space thrusts. The simultaneous control requirement exposed INKEY$'s single-key limitation, so two keyboard-port reads inspect O/P and Space independently. Opposing steering keys cancel. This adds a hardware-facing teaching step: explain the selected half-rows and active-low bits locally, rather than presenting a mysterious input routine. The simpler vertical checkpoints retain INKEY$.

Contact is checked before drawing. A fall crossing the surface is clamped to the surface, so there is no skipped ground. Horizontal movement is one column and tests the destination's height at the old vertical position: entering a hillside ends the attempt at the previous clear cell. Only downward pad contact can be safe; crossing into terrain while ascending cannot count as a landing. Both outer pad columns are valid for the one-cell craft.

The loop calculates while the previous craft remains visible, then clears and draws consecutively. Instruments update before that short erase/draw pair. Outcome sounds run after motion has stopped; there is no blocking thrust sound. PAUSE remains interruptible, so cadence depends on held input and interpreter work.

## Teaching stages to review

1. A constant-speed fall and contact on flat ground.
2. Velocity, gravity and unlimited thrust, with a safe-speed threshold.
3. Fuel that disables thrust without ending the flight.
4. Sideways control, simultaneous thrust and a pad on flat ground.
5. A height array that draws and checks uneven terrain.
6. Custom craft/flame construction, outcome sound and the complete challenge.

The fourth prototype checkpoint also supplies instructions and retry, which should be split into smaller teaching changes. Custom-character construction needs its own understandable step. The six source checkpoints are runnable development states, not a six-lesson commitment.

## Verification boundary

Use the maintained build and flight scripts and their result files in the sample repository for configuration-specific execution evidence. The initial ROM-entry investigation caught invalid multi-letter FOR/string variables and insufficient settling time after long-line relisting; the final helper waits for the editor and checks stored line admission. Source listings retain readable keyword spacing; only ROM entry suppresses redundant post-token spaces.

Scripted keyboard events and read-only variable inspection can establish the rules, combined input and a successful approach. They do not establish human enjoyment or original-hardware/native-host equivalence. Review the native game before fixing the feel and lesson progression.

The initial successful scripted approach took 1,009 observed PAL frames (about 20.2 seconds) from the instrument display to contact. It reached pad column 24 at speed 8 with 21 of 45 fuel units remaining. Its minimum simulated height coordinate was 364, so this approach did not depend on holding against the upper boundary. The controller inspected state and sent O/P/Space events; it did not write position or velocity. This is a feasibility observation, not evidence that a first-time player will find the timing obvious.

In native play review, the user reported that it “works well” and is “quite hard”. Keep the full terrain approach as the challenge to build towards, while reviewing the early vertical/unlimited-fuel, limited-fuel and flat-pad stages as the way to learn its controls and braking. This feedback does not yet settle final tuning or a lesson count.

Final checks cover both safe pad edges, adjacent off-pad contact, excessive speed and a fast fall, an ascending hillside collision, opposing steering keys, held steering at both screen limits, the upper boundary, fuel exhaustion with thrust held, release-gated retry/reset, and fresh-tape play/quit. A separate held-Q test found and fixed key carry-over into the editor: the game now waits for Q release before returning to BASIC. Stored token comparison confirms that this final exit-only change preserves all flight and drawing code. The final native tape is available for the next load; the user's already-open session may still contain the pre-exit-fix program.
