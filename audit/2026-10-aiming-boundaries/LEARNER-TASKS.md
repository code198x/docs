# Aiming boundary trial

These are optional paper tasks based on Maths for Games units 6–11. No software
or previous attendance is required. Use X to the right and Y upwards. Coordinates
are written (X,Y). A moving point touches a circular target when its route comes
within 5 units of the target centre, including exactly 5. It moves in a straight
line between each pair of recorded positions. Keep predictions before checking.
Ask for a hint when useful; the observer records it without treating it as failure.

1. A point moves from (0,0) to (3,0) in one tick. The target centre is (1.5,5).
   Draw them. Would checking only the two recorded positions detect contact?
   Does the route itself touch the target? Explain where it comes closest.
2. Keep the same movement, but put the centre at (9,0). A program says that the
   horizontal line goes through the centre, so it reports a hit this tick.
   What did it forget? Name one check that would expose this mistake.
3. At scale 4, a component is −0.125 units per tick. Encode it by multiplying by
   4 and rounding to the nearest integer, with halves away from zero. Decode
   that integer by dividing by 4. Where is the point after four ticks from zero
   if stored position retains that scale? Is the motion the original motion?

If needed, use these hints separately:

- For task 1, consider the point halfway along the route. Pythagoras gives the
  endpoint distance: square the horizontal gap and vertical gap, add, then take
  the positive square root.
- For task 2, distinguish a line that extends forever from this tick's start
  and finish. How far away is the closer endpoint?
- For task 3, −0.125 × 4 = −0.5. Which neighbouring integer is away from zero?

These tasks are prepared, not learner-tested. They do not supply a course score,
time target or evidence of retention or unaided transfer.
