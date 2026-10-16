# Keep the half between updates

This is a prepared paper trial, not a new required lesson. No learner has tried
it. Use [Nailing the Point Down](https://code198x.com/foundations/working-the-bits/unit-05/)
for more explanation; no language installation or earlier attendance is required.
Keep the [assessor notes](ASSESSOR.md) separate until you have recorded predictions.

We store a nonnegative position in units of one 256th of a pixel. Stored 128
means half a pixel; stored 256 means one pixel. Storage holds whole numbers from
0 through 65535. Our four updates below stay within that range.

A drawing needs a whole-pixel coordinate. For these nonnegative values, shifting
right eight bits extracts the whole part. Drawing that coordinate does not change
the stored position. `LET` changes a named value; `SHOW` displays it. The loop
visits updates 1, 2, 3 and 4, in that order.

```text
LET position = 0
LET step = 128
FOR update = 1 TO 4
  LET position = position + step
  SHOW position SHIFTRIGHT 8
END
```

1. Predict all four displayed coordinates. For each update, also record the
   stored position and its full value in pixels. Explain why these are three
   different columns, even when two happen to show the same number.
2. A changed version adds this line after SHOW, inside the loop:

   ```text
   LET position = (position SHIFTRIGHT 8) * 256
   ```

   Predict its four drawings. Both versions draw coordinate 0 after the first
   update. Does that one success show the change is safe? Identify the earliest
   stored-state difference and the first visible difference.
3. Repair the changed version so it preserves the halves. Explain why extracting
   a coordinate for drawing does not require replacing the stored position.
   Check all four updates again, including the first one that already matched.
4. Change the stored step to 64, a quarter of a pixel. Predict the four drawings
   before trying your repair. Explain how several sub-pixel moves can eventually
   reach a new pixel.

If you want a hint, first ask which value the next update reads. A second hint:
compare how much of the half-pixel move remains after the first drawing. Record any hint used
before reading the explanation.

Optional range question: starting at stored 65407 and adding 128 reaches 65535.
What happens to the mathematical sum if you add 128 again? What would a real
program need to decide? Our exercise does not choose wrapping or stopping for
that out-of-range update.

Keep first predictions, revisions and help separate. We have traced a position;
we have not measured smoothness, execution speed, a display or learner success.
