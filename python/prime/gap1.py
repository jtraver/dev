#!/usr/bin/python

import sys

limit = 1000000

primes = [ 2 ]

def is_prime(candi):
    for i1 in range(0, len(primes)):
        p1 = primes[i1]
        if p1 * p1 > candi:
            break
        if candi % p1 == 0:
            return False
    return True

lastprime = 3
maxgap = 0
for c1 in range(3, limit, 2):
    if is_prime(c1):
        primes.append(c1)
        # print "%d" % c1
        gap = c1 - lastprime
        if gap > maxgap:
            print "new max gap %s - %s = %s" % (str(c1), str(lastprime), str(gap))
            sys.stdout.flush()
            maxgap = gap
        lastprime = c1

# print "%s" % str(primes)
