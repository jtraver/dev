#!/usr/bin/python

import sys

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"

def main():
    ret1 = 0
    ret1 += print1()
    if ret1:
        print "%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP)
    else:
        print "%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP)
    print "DONE"
    print "^G"
    sys.stdout.flush()
    sys.exit(ret1)

def print1():
    ret1 = 0
    for i1 in xrange(100):
        print "i1 = %02d" % i1
    return ret1

main()
