; Native arithmetic contrast; not the invented instruction codes.
org 32768
start:
 di
 xor a
 inc a
 inc a
 add a,a
 ld ($a000),a
 ld a,165
 ld ($b100),a
hold:
 jr hold
end start
