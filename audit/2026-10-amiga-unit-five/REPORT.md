# Amiga unit 5: loops and animation

Both lessons now give learners edits with specific, observable results. AMOS distinguishes counting order from screen position and repairs the ten-line message overlap. Blitz distinguishes drawing from changing state, traces the two bitmaps and uses a fixed colour for the larger workload. No update-rate or language-speed comparison is claimed.

This is the bounded pilot for [website #776](https://github.com/code198x/website/issues/776), under umbrella #116. The opening qualification in docs #99 is separate.

## What we ran

We used FS-UAE 3.2.35, A1200/68020, PAL, 2 MB chip and 8 MB fast memory, Kickstart 3.1 and Workbench 3.1. AMOS Professional 2.00 ran the baseline and four editor variants. AmiBlitz 3.13.0b compiled and executed the old listing, changed baseline, fixed-colour 80/200-circle variants, frozen pattern and smaller increment.

| Experiment | Observed result |
| --- | --- |
| AMOS original | Five numbered lines, 1–5, with `Done!` below |
| AMOS ten passes, message still at row 12 | `Done!number 8` on row 12 |
| AMOS ten passes, message moved to row 16 | All ten lines intact; finish message below |
| AMOS descending counter, original row formula | Final arrangement still reads 1–5 |
| AMOS descending counter, row `10-N` | Final arrangement reads 5–1 |
| Blitz changed baseline | Coloured pattern changes position and mouse input exits |
| Blitz fixed colour, 80 then 200 calls | Moving pink patterns; denser in the second; mouse input exits |
| Blitz increment 0 | Pattern unchanged across separate observations; mouse input still exits |
| Blitz increment 0.01 | Pattern changes position; mouse input exits |

The Blitz baseline includes `VWait 100` before `BLITZ`, matching the earlier lessons. Its historical capture driver's typed payload matches the maintained listing exactly. The old capture driver itself was not replayed or qualified as PED automation. Native compilation used the CLI with the `RuntimeDebug = 0` import header; the learner-facing PED controls come from the earlier qualified opening procedure.

Brief injected clicks sometimes missed the between-update button check; repeated explicit left clicks returned Workbench. We advise keeping the button down until the program responds. We did not inject a timed held button. We restarted with input capture enabled after an unsuccessful input-control attempt; hardware and media identities stayed the same. The original ungrabbed configuration and later captured configuration both reached a mouse exit. These observations do not establish an update rate, a guaranteed input latency or behaviour on every configuration.

The AMOS variants were applied in the editor after importing the baseline. Retained ASCII files represent those exact changes; they were not all separately imported. `observations.json` records the method and limits. Compiler logs retain the actual six successful compile reports. Failed UI attempts and extraction/browser limitations are recorded in `validation.json` rather than counted as passes.

## Source and repeatability

`source.json` identifies both lesson files and maintained inputs by SHA-256. `inputs.json` hashes the actual runtime archives, compiler and user-supplied media. No ROM, Workbench disk, executable or private media path is included.

AMOS came from the official repository at revision `533b4b1f5acd604814513f78e02c7b4796cb0531`. AmiBlitz came from the official [3.13.0b release](https://github.com/AmiBlitz/AmiBlitz3/releases/tag/v3.13.0b). Acquisition URLs and archive identities are also retained in the earlier [greetings acquisition record](../2026-10-amiga-greetings/acquisition.json). LHA extraction returned 1 on an accented catalogue pathname; required compiler files were present, matched their identity, and ran the retained programs.

The lesson cites the [AMOS control-structures manual](https://amospromanual.dev/05-04-control-structures.html) and [Blitz BASIC 2.1 manual](https://daemonbite.com/files/linked/BB21Manual.pdf): double-buffer example, printed pp. 85–87; `VWait`, p. 98; `Joyb`, p. 108; `Sin`/`Cos`, p. 113. The bundled Blitz programmer's guide agrees with the shown bitmap sequence. The wait before `BLITZ` follows the earlier qualification and the manual's mode-switch guidance.

For a native rerun, acquire the named official tools and supply licensed media matching the input hashes. Substitute a local test directory for `TEST_ROOT` in `runtime/boot.fs-uae.example`. Import `p.asc` through AMOS's Merge ASCII and apply the named changes. For each Blitz file, assign its bundled `Libs` directory, compile with `AmiBlitz3 -s Tools:<name>.ab3 -e Tools:<name>.exe`, then run the executable. Observe positions across multiple moments and press the left mouse button until it exits. The header disables runtime debugging only; it does not bypass the compiler.

## Delivery checks

The final website build passed, including shared-frame checks on 2,459 public pages. Content checks passed with existing coverage advisories. Both built lessons contain their complete maintained listing, three questions, and resolving Amiga links. The source verifier checks variant transformations and capture equality; a missing-toggle reasoning control is rejected. Its bitmap check is a reasoning check, not a measurement of the emulator's display pipeline.

Run from a compatible docs checkout:

```
python3 audit/2026-10-amiga-unit-five/verify.py --website <built-website> --samples <code-samples>
```

The installed Chrome browser was checked in an isolated headless session at 390×844 and 1440×900. All three explanations on each page open and close with Enter, answers become visible, and neither page overflows horizontally. The existing Blitz video decodes at 768×576 and its playback time advances. Its 25 fps encoding is not evidence of the program's update rate. Representative screenshots were visually inspected and retained in `browser/`.

With the website's existing Playwright dependency and Chrome available, create an empty output directory, serve its built `dist`, and run:

```
node audit/2026-10-amiga-unit-five/browser/check.cjs <website> <local-server-url> <output-directory>
```

A native Chrome responsive-toolbar attempt changed fields unexpectedly. We restored width 320 and empty height and closed only the task window; exact viewport results above come from the isolated browser checker.

No beginner was available. Learning effectiveness, VoiceOver, other runtimes and physical Amiga models remain unverified. The earlier opening qualification is not broadened by these checks.
