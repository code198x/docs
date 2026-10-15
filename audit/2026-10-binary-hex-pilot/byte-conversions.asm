; Audit-only fixture. Emit eight binary digits and two nibble values per byte.
org 32768
start:
 di
 ld hl,$a000
 ld c,0
value:
 ld e,c
 ld b,8
bit:
 sla e
 ld a,0
 adc a,0
 ld (hl),a
 inc hl
 djnz bit
 ld a,c
 srl a
 srl a
 srl a
 srl a
 ld (hl),a
 inc hl
 ld a,c
 and 15
 ld (hl),a
 inc hl
 inc c
 jr nz,value
 ld a,165
 ld ($b100),a
hold:
 jr hold
end start
