#!/usr/bin/env python3
#!/usr/bin/python

import time
import sys

def main():
    # for count in xrange(10000000):
    for count in range(10):
        print("%s" % str(count))
        sys.stdout.flush()
        time.sleep(1)

main()
