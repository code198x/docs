# Amiga opening qualification follow-up

The remaining named numeric and graphics probes now have fresh execution evidence. With `RuntimeDebug=0` and `OverflowCheck=0`, the byte program printed 1000000, 100 and -106; the word variant printed 1000000, 100 and 150. The first graphics program displayed its rectangle and circle, then returned to Workbench on a left click. All three compiled with zero errors.

Both live setup-to-first-program routes and representative changed opening pages were reviewed at phone and desktop widths. This supplies the remaining bounded checks requested by [website #767](https://github.com/code198x/website/issues/767) and [#766](https://github.com/code198x/website/issues/766), under [Amiga audit #116](https://github.com/stevehill1981/198x/issues/116). The two focused issues can close after review of this evidence; the wider audit remains open. No lesson or sample changed in this follow-up.

## Inputs and execution

The named configuration was FS-UAE 3.2.35, A1200 PAL, 68020, 2 MB chip and 8 MB fast RAM, Kickstart 3.1 rev 40.68, Workbench 3.1 rev 40.42 and its Fonts disk. `identities.json` records media, official archive and compiler hashes matching the preceding trials. The [earlier acquisition record](../2026-10-amiga-greetings/acquisition.json) supplies the public runtime download URLs. No new dependency was installed.

The three `.ab3` files are byte-identical to the [prepared claims probes](../2026-10-amiga-claims/probes/). The one-letter scripts in `runtime/` compile each and run the resulting standalone executable. Numeric scripts redirect actual guest output to the shared Tools drive. They retain MouseWait and End. These results are guest execution evidence, not a host arithmetic simulation or a new PED edit/compile qualification. The earlier [greeting recovery report](../2026-10-amiga-greetings/REPORT.md) owns the tested PED cycle.

| Program | Compiler | Observed result |
| --- | --- | --- |
| `types.ab3` | 13 lines, zero errors | Long 1000000; initial byte 100; final byte -106 |
| `word.ab3` | 13 lines, zero errors | Long 1000000; initial word 100; final word 150 |
| `blitzmode.ab3` | 10 lines, zero errors | Filled pink rectangle and purple outlined circle on black; left click restored Workbench |

`verify.py` checks the numeric outputs against the same addition and signed-byte conversion, confirms that the two results differ by one byte modulus, checks compiler completion and compares probe bytes with the earlier inputs. Its wrong-value control substitutes 150 for the byte result and must fail. It does not launch an emulator or automatically establish the graphical observation. Run with:

```sh
python3 audit/2026-10-amiga-opening-qualification/verify.py
```

Overflow-check-on behaviour remains a sourced contract; this trial did not observe its diagnostic. No new AMOS numeric boundary claim, performance comparison or whole-course compatibility claim follows.

## Live browser review

Chrome version and outcomes are in `observations.json`. Native browser review used DevTools responsive emulation at 390×844 and 1440×900, with the default DPR of 2. Eight pages supplied representative sections:

- AMOS and Blitz setup pages, including named requirements and launch/greeting instructions.
- Both first lessons, their source blocks and the links back to setup. The setup-to-greeting links also opened their intended lessons.
- AMOS unit 3's integer, real and string explanation.
- Blitz unit 2's source and mode/compile explanation; its wait precedes BLITZ.
- Blitz unit 3's storage/overflow explanation and source-header instructions.
- The Blitz module introduction's compile/run and workload-dependent performance explanation.

Prose was readable and code stayed within its containers. Direct pointer clicks on the greeting Copy buttons showed “Copied”; clipboard bytes were not inspected. One earlier accessibility-index Copy invocation showed “Copy failed”, while a later direct pointer click succeeded. No ordinary-pointer copy failure was reproduced and its cause is not established.

This is representative visual and interaction review, not an assertion that every section of the opening modules was exhaustively tested. It is also not a physical phone or learner trial. The separate [unit-4 review](../2026-10-amiga-decisions/REPORT.md) retains its own evidence.

## Failures, recovery and limits

Computer use temporarily returned `Computer Use server error -10005: cgWindowNotFound` for both FS-UAE and Chrome while the emulator session remained present. It recovered without a configuration change. The graphics result and click-to-return were observed only after recovery; window loss was not diagnosed as a program crash. The task-owned emulator and browser window were closed during cleanup.

The LHA extractor again exited 1 for an accented catalogue path. Required compiler/core files were present, the compiler identity matched, and the retained programs compiled and ran; full archive extraction is not claimed. An initial Workbench command retained previous text; it was cleared with Ctrl+U and inspected before execution. No result is attributed to the unsubmitted concatenated command. Browser inline address completion also retained a longer lesson path during an overview navigation; adding a terminal fragment prevented that completion, and the overview URL and content were then inspected.

A direct HTTP check failed with `HTTP Error 403: Forbidden`. The web-fetch fallback returned an older cached Blitz setup page and an AMOS cache miss; neither verified current publication. The live page findings above come from the native browser. No all-routes HTTP pass is claimed.

Production and content checks for the unchanged lessons remain in the preceding reports. This evidence-only change requires no new site build. No VoiceOver, human learner or timing measurement was performed. The next bounded teaching review is unit 5 in AMOS and Blitz, including the crowd-animation workload claims and the distinction between loop order and final screen position.
