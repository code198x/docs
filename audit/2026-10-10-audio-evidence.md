# Audio evidence reconciliation — 10 October 2026

The four C03a pattern repairs have maintained sources, executable checks and
recorded native observations. Their source hashes still match their records.
The website includes these sources through CodeFromFile. This removes the
repair tasks from the current queue; browser acceptance and listening remain.

- [Spectrum beeper](https://github.com/code198x/code-samples/tree/be65631db11bac9127e85a76f448bef3806819a8/sinclair-zx-spectrum/patterns/assembly/audio/sound-beep): eight executed cases.
- [C64 SID note](https://github.com/code198x/code-samples/tree/be65631db11bac9127e85a76f448bef3806819a8/commodore-64/patterns/assembly/audio/sid-note-trigger): envelope, retrigger and ownership checks.
- [Amiga sample playback](https://github.com/code198x/code-samples/tree/be65631db11bac9127e85a76f448bef3806819a8/commodore-amiga/patterns/assembly/audio/playing-a-sample): cold-boot A500 PAL, DMA, pitch and one-shot timing.
- [NES square wave](https://github.com/code198x/code-samples/tree/36270ea4/nintendo-entertainment-system/patterns/assembly/audio/square-wave): all seven complete ROM cases rerun against Emu198x `df2799e2`. WAV playback pitch and duration now have separate checks, including a deliberately wrong header that both checks reject.

Emu198x already contains the triangle held-output fix (`c63d1bc3`) and the
48 kHz output-rate fix (`a1f23188`). The current APU library passed all 77
unit tests, none ignored, including the held-output and PAL/NTSC sample-rate
regressions. These results clear the emulator prerequisite for C09e; they do
not claim that the Dash feedback companion itself is complete.

The older sample records describe specific configurations and earlier
emulator binaries. Only the NES sample and current APU suite were rerun for
this reconciliation. No original-hardware or listening result is inferred.
