#!/usr/bin/env python3
#!/usr/bin/python

import math

LIMIT = 100

def misc():
    phi = (1 + math.sqrt(5)) / 2
    # print "math = %s" % str(math)

    # apihelper.info(math)

    # print "math.pi = %s" % str(math.pi)
    # print "math.e = %s" % str(math.e)
    print "phi = %s" % str(phi)

def main():
    fib1()
    misc()

def fib1():
    if1 = []
    f1 = []
    if1.append(0)
    if1.append(1)
    f1.append(0.0)
    f1.append(1.0)
    c1 = 1
    lphi1 = 0
    for x1 in xrange(LIMIT):
        c1 += 1
        i0 = if1[x1]
        n0 = f1[x1]
        i1 = if1[x1 + 1]
        n1 = f1[x1 + 1]
        n2 = n0 + n1
        i2 = i0 + i1
        f1.append(n2)
        if1.append(i2)
        #for x2 in xrange(2, 20):
        #    if i2 % x2 == 0:
        #        print "%s %s is divisible by %s" % (str(c1), str(i2), str(x2))
        phi1 = n2 / n1
        # print "%s %s" % (str(c1), str(phi1))
        print "%s %g %s / %s" % (str(c1), phi1, str(n2), str(n1))
        #if False:
        #    diff = phi1 - 1.61803398875
        #    if diff < 0:
        #        diff = -diff
        #    if diff < 0.000000000001:
        #        break
        if phi1 == lphi1:
            break
        lphi1 = phi1
    # print "f1 = %s" % str(f1)

main()
