; Audit fixture. ASCII conversion and ROM calculator operations, not injected results.
org 32768
start:
 di
 ld hl,text0
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9000
 ld bc,5
 ldir
 ld hl,text1
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9005
 ld bc,5
 ldir
 ld hl,text2
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$900a
 ld bc,5
 ldir
 ld hl,text3
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$900f
 ld bc,5
 ldir
 ld hl,text4
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9014
 ld bc,5
 ldir
 ld hl,text5
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9019
 ld bc,5
 ldir
 ld hl,text6
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$901e
 ld bc,5
 ldir
 ld hl,text7
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9023
 ld bc,5
 ldir
 ld hl,text8
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9028
 ld bc,5
 ldir
 ld hl,text9
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$902d
 ld bc,5
 ldir
 ld hl,text10
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9032
 ld bc,5
 ldir
 ld hl,text11
 ld (23645),hl
 ld a,(hl)
 call $2c9b
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9037
 ld bc,5
 ldir
 ld bc,1
 call $2d2b
 ld bc,2
 call $2d2b
 rst $28
 defb $05,$38
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$903c
 ld bc,5
 ldir
 ld bc,3
 call $2d2b
 ld bc,4
 call $2d2b
 rst $28
 defb $05,$38
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9041
 ld bc,5
 ldir
 ld bc,1
 call $2d2b
 ld bc,10
 call $2d2b
 rst $28
 defb $05,$38
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9046
 ld bc,5
 ldir
 ld bc,5
 call $2d2b
 ld bc,10
 call $2d2b
 rst $28
 defb $05,$38
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$904b
 ld bc,5
 ldir
 ld bc,1
 call $2d2b
 ld bc,10
 call $2d2b
 rst $28
 defb $05,$38
 ld bc,5
 call $2d2b
 rst $28
 defb $04,$38
 ld hl,(23653)
 ld de,5
 or a
 sbc hl,de
 ld (23653),hl
 ld de,$9050
 ld bc,5
 ldir
 ld a,$a5
 ld ($91ff),a
hold:
 jr hold
text0: defb "0.5",13
text1: defb ".5",13
text2: defb "0.1",13
text3: defb "0.75",13
text4: defb "0.25",13
text5: defb "0.2",13
text6: defb "0.125",13
text7: defb "0.0625",13
text8: defb "0.3",13
text9: defb "0.9",13
text10: defb "1.5",13
text11: defb "5e-1",13
end start
