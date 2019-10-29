#!/usr/bin/env python3
#!/usr/bin/python

import time

def main():
    starttime = time.time()
    # for i1 in xrange(10):
    elapsed = 0
    while elapsed < 1:
        now = time.time()
        elapsed = now - starttime
        ielapsed = int(elapsed)
        print "elasped time is %s" % str(elapsed)
        print "ielasped time is %s" % str(ielapsed)
        time.sleep(elapsed)

main()
