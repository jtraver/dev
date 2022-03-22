#!/usr/bin/env python3
#!/usr/bin/python

import time

def main():
    print("Start : %s" % time.ctime())
    time1 = time.time()
    time.sleep( 0 )
    time2 = time.time()
    print("End : %s" % time.ctime())
    dur = time2 - time1
    print("time1 = %s, time2 = %s, dur = %s" % (str(time1), str(time2), str(dur)))
    starttime = time.time()
    # for i1 in xrange(10):
    elapsed = 0
    while elapsed < 1:
        now = time.time()
        elapsed = now - starttime
        ielapsed = int(elapsed)
        print("elasped time is %s" % str(elapsed))
        print("ielasped time is %s" % str(ielapsed))
        time.sleep(elapsed)

main()
