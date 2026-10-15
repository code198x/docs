; Audit-only ASCII boundary fixture. Not learner pseudocode.
org 32768
start:
di
ld a,64
or 32
ld (40960),a
ld a,64
and 223
ld (40961),a
ld a,64
cp 65
jr c,lower_0
cp 91
jr nc,lower_0
or 32
lower_0:
ld (40962),a
ld a,64
cp 97
jr c,upper_0
cp 123
jr nc,upper_0
and 223
upper_0:
ld (40963),a
ld a,64
cp 48
jr c,invalid_0
cp 58
jr nc,invalid_0
sub 48
jr digit_0
invalid_0:
ld a,255
digit_0:
ld (40964),a
ld a,65
or 32
ld (40965),a
ld a,65
and 223
ld (40966),a
ld a,65
cp 65
jr c,lower_1
cp 91
jr nc,lower_1
or 32
lower_1:
ld (40967),a
ld a,65
cp 97
jr c,upper_1
cp 123
jr nc,upper_1
and 223
upper_1:
ld (40968),a
ld a,65
cp 48
jr c,invalid_1
cp 58
jr nc,invalid_1
sub 48
jr digit_1
invalid_1:
ld a,255
digit_1:
ld (40969),a
ld a,90
or 32
ld (40970),a
ld a,90
and 223
ld (40971),a
ld a,90
cp 65
jr c,lower_2
cp 91
jr nc,lower_2
or 32
lower_2:
ld (40972),a
ld a,90
cp 97
jr c,upper_2
cp 123
jr nc,upper_2
and 223
upper_2:
ld (40973),a
ld a,90
cp 48
jr c,invalid_2
cp 58
jr nc,invalid_2
sub 48
jr digit_2
invalid_2:
ld a,255
digit_2:
ld (40974),a
ld a,91
or 32
ld (40975),a
ld a,91
and 223
ld (40976),a
ld a,91
cp 65
jr c,lower_3
cp 91
jr nc,lower_3
or 32
lower_3:
ld (40977),a
ld a,91
cp 97
jr c,upper_3
cp 123
jr nc,upper_3
and 223
upper_3:
ld (40978),a
ld a,91
cp 48
jr c,invalid_3
cp 58
jr nc,invalid_3
sub 48
jr digit_3
invalid_3:
ld a,255
digit_3:
ld (40979),a
ld a,96
or 32
ld (40980),a
ld a,96
and 223
ld (40981),a
ld a,96
cp 65
jr c,lower_4
cp 91
jr nc,lower_4
or 32
lower_4:
ld (40982),a
ld a,96
cp 97
jr c,upper_4
cp 123
jr nc,upper_4
and 223
upper_4:
ld (40983),a
ld a,96
cp 48
jr c,invalid_4
cp 58
jr nc,invalid_4
sub 48
jr digit_4
invalid_4:
ld a,255
digit_4:
ld (40984),a
ld a,97
or 32
ld (40985),a
ld a,97
and 223
ld (40986),a
ld a,97
cp 65
jr c,lower_5
cp 91
jr nc,lower_5
or 32
lower_5:
ld (40987),a
ld a,97
cp 97
jr c,upper_5
cp 123
jr nc,upper_5
and 223
upper_5:
ld (40988),a
ld a,97
cp 48
jr c,invalid_5
cp 58
jr nc,invalid_5
sub 48
jr digit_5
invalid_5:
ld a,255
digit_5:
ld (40989),a
ld a,122
or 32
ld (40990),a
ld a,122
and 223
ld (40991),a
ld a,122
cp 65
jr c,lower_6
cp 91
jr nc,lower_6
or 32
lower_6:
ld (40992),a
ld a,122
cp 97
jr c,upper_6
cp 123
jr nc,upper_6
and 223
upper_6:
ld (40993),a
ld a,122
cp 48
jr c,invalid_6
cp 58
jr nc,invalid_6
sub 48
jr digit_6
invalid_6:
ld a,255
digit_6:
ld (40994),a
ld a,123
or 32
ld (40995),a
ld a,123
and 223
ld (40996),a
ld a,123
cp 65
jr c,lower_7
cp 91
jr nc,lower_7
or 32
lower_7:
ld (40997),a
ld a,123
cp 97
jr c,upper_7
cp 123
jr nc,upper_7
and 223
upper_7:
ld (40998),a
ld a,123
cp 48
jr c,invalid_7
cp 58
jr nc,invalid_7
sub 48
jr digit_7
invalid_7:
ld a,255
digit_7:
ld (40999),a
ld a,55
or 32
ld (41000),a
ld a,55
and 223
ld (41001),a
ld a,55
cp 65
jr c,lower_8
cp 91
jr nc,lower_8
or 32
lower_8:
ld (41002),a
ld a,55
cp 97
jr c,upper_8
cp 123
jr nc,upper_8
and 223
upper_8:
ld (41003),a
ld a,55
cp 48
jr c,invalid_8
cp 58
jr nc,invalid_8
sub 48
jr digit_8
invalid_8:
ld a,255
digit_8:
ld (41004),a
ld a,48
or 32
ld (41005),a
ld a,48
and 223
ld (41006),a
ld a,48
cp 65
jr c,lower_9
cp 91
jr nc,lower_9
or 32
lower_9:
ld (41007),a
ld a,48
cp 97
jr c,upper_9
cp 123
jr nc,upper_9
and 223
upper_9:
ld (41008),a
ld a,48
cp 48
jr c,invalid_9
cp 58
jr nc,invalid_9
sub 48
jr digit_9
invalid_9:
ld a,255
digit_9:
ld (41009),a
ld a,57
or 32
ld (41010),a
ld a,57
and 223
ld (41011),a
ld a,57
cp 65
jr c,lower_10
cp 91
jr nc,lower_10
or 32
lower_10:
ld (41012),a
ld a,57
cp 97
jr c,upper_10
cp 123
jr nc,upper_10
and 223
upper_10:
ld (41013),a
ld a,57
cp 48
jr c,invalid_10
cp 58
jr nc,invalid_10
sub 48
jr digit_10
invalid_10:
ld a,255
digit_10:
ld (41014),a
ld a,47
or 32
ld (41015),a
ld a,47
and 223
ld (41016),a
ld a,47
cp 65
jr c,lower_11
cp 91
jr nc,lower_11
or 32
lower_11:
ld (41017),a
ld a,47
cp 97
jr c,upper_11
cp 123
jr nc,upper_11
and 223
upper_11:
ld (41018),a
ld a,47
cp 48
jr c,invalid_11
cp 58
jr nc,invalid_11
sub 48
jr digit_11
invalid_11:
ld a,255
digit_11:
ld (41019),a
ld a,58
or 32
ld (41020),a
ld a,58
and 223
ld (41021),a
ld a,58
cp 65
jr c,lower_12
cp 91
jr nc,lower_12
or 32
lower_12:
ld (41022),a
ld a,58
cp 97
jr c,upper_12
cp 123
jr nc,upper_12
and 223
upper_12:
ld (41023),a
ld a,58
cp 48
jr c,invalid_12
cp 58
jr nc,invalid_12
sub 48
jr digit_12
invalid_12:
ld a,255
digit_12:
ld (41024),a
ld a,165
ld ($a1ff),a
hold:
jr hold
end start
