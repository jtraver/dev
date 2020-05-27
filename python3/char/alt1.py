#!/usr/bin/env python3

#!/usr/bin/python3


# https://en.wikipedia.org/wiki/Alt_key

alt_a = "å"
ord_alt_a = ord(alt_a)
ord_a = ord("a")
alt_diff = ord_alt_a - ord_a
print("alt_a = %s, ord_a = %s, ord_alt_a = %s, alt_diff = %s" % (str(alt_a), str(ord_a), str(ord_alt_a), str(alt_diff)))


# √∫˜µ≤Ω≈ß∂ƒ©˙∆˚¬ÅÍÎÏ˝ÓÔ
# ¡£º
# this is not ord_b: why mess up the mapping?  didn't make much sense for the chars they wanted I suspect
# I should have known when alt_diff wasn't 128 I guess
ord_b = ord_a + 1
ord_alt_b = ord_b + alt_diff
alt_b = chr(ord_alt_b)
print("alt_b = %s, ord_b = %s, ord_alt_b = %s, alt_diff = %s" % (str(alt_b), str(ord_b), str(ord_alt_b), str(alt_diff)))

#for i1 in range(256):
#    str2 = "%s %d 0x%x '%c'" % (str(i1), i1, i1, i1)
#    print(("str2 = %s" % str2))
#
#for i1 in range(32, 127):
#    c1 = chr(i1)
#    print "%d %s" % (i1, c1)


# 1 ¡
# ! ⁄
# 2 ™
# @ €
# ¡™£¢∞§¶•ªº
# 1234567890
# 
# ⁄€‹›ﬁﬂ‡‡°·‚
# !@#$%^&*()
# 
# œ∑´®†\¨ˆøπ
# qwertyuiop
# 
# Œ„´‰ˇÁ¨ˆØ∏
# QWERTYUIOP

