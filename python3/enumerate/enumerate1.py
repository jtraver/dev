#!/usr/bin/env python3

# https://medium.com/better-programming/stop-using-range-in-your-python-for-loops-53c04593f936

import sys

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"

def main():
    ret1 = 0
    ret1 += enumerate1()
    if ret1:
        print("%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP))
    else:
        print("%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP))
    print("DONE")
    print("")
    sys.stdout.flush()
    sys.exit(ret1)

def enumerate1():
    ret1 = 0
    list1 = []
    for angle in range(0, 10):
        list1.append(angle)
    for i, angle in enumerate(list1, 1):
        print(i, angle)
    return ret1

main()
