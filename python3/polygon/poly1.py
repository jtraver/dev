#!/usr/bin/env python3

import sys

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"

def main():
    ret1 = 0
    ret1 += polygon1()
    if ret1:
        print("%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP))
    else:
        print("%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP))
    print("DONE")
    print("")
    sys.stdout.flush()
    sys.exit(ret1)

def polygon1():
    ret1 = 0
    for angle in range(3, 100001):
        total = 180 * (angle - 2)
        inner = total / angle
        print("angle = %s, total = %s, inner = %s" % (str(angle), str(total), str(inner)))
    return ret1

main()
