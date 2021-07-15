#!/usr/bin/env python3

import sys

def twos():
    # 16406297185095647658 - 8579294738944438520
    # 7827002446151209138
    cval = 16406297185095647658
    sval = 8579294738944438520
    dval = cval - sval
    sum1 = cval + sval
    val1 = 1
    last1 = val1
    for i1 in range(68):
        print("%s %s" % (str(i1), str(val1)))
        if val1 > cval:
            print("  cval = %s" % str(cval))
            cval1 = val1 - cval
            print("    cval1 = %s" % str(cval1))
            cval2 = cval + last1
            print("    cval2 = %s" % str(cval2))
        if val1 > sval:
            print("  sval = %s" % str(sval))
            sval1 = val1 - sval
            print("    sval1 = %s" % str(sval1))
            sval2 = sval + last1
            print("    sval2 = %s" % str(sval2))
            sval3 = val1 + sval
            print("    sval3 = %s" % str(sval3))
        if val1 > dval:
            print("  dval = %s" % str(dval))
            dval1 = val1 - dval
            print("    dval1 = %s" % str(dval1))
            dval2 = dval + last1
            print("    dval2 = %s" % str(dval2))
        if val1 > sval:
            print("  sum1 = %s" % str(sum1))
            sum11 = val1 - sum1
            print("    sum11 = %s" % str(sum11))
            sum12 = sum1 + last1
            print("    sum12 = %s" % str(sum12))
            sum13 = val1 + sum1
            print("    sum13 = %s" % str(sum13))
            sum14 = val1 + sum1
            print("    sum14 = %s" % str(sum14))
            sum15 = sum1 - val1
            print("    sum15 = %s" % str(sum15))
        last1 = val1
        val1 *= 2

def main():
    print("main")
    twos()

main()
print("")
sys.stderr.write("\n")
