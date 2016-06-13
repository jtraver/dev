#!/usr/bin/python

import time

def main():
    starttime = time.time()
    for i1 in xrange(10):
        now = time.time()
        elapsed = now - starttime
        print "elasped time is %s" % str(elapsed)
        time.sleep(1)

main()
