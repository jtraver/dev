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
    print(("phi = %s" % str(phi)))

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
    for x1 in range(LIMIT):
        c1 += 1
        i0 = if1[x1]
        n0 = f1[x1]
        i1 = if1[x1 + 1]
        n1 = f1[x1 + 1]
        n2 = n0 + n1
        i2 = i0 + i1
        f1.append(n2)
        if1.append(i2)
        # i2 = int(n2)
        for x2 in range(2, 20):
            if i2 % x2 == 0:
                # print "%s %s %s is divisible by %s" % (str(x1), str(c1), str(i2), str(x2))
                print(("%s %s is divisible by %s" % (str(c1), str(i2), str(x2))))
        #if i2 % 2 == 0:
        #    print "%s %s %s is divisible by 2" % (str(x1), str(c1), str(i2))
        #if i2 % 3 == 0:
        #    print "%s %s %s is divisible by 3" % (str(x1), str(c1), str(i2))
        #if i2 % 4 == 0:
        #    print "%s %s %s is divisible by 4" % (str(x1), str(c1), str(i2))
        #if i2 % 5 == 0:
        #    print "%s %s %s is divisible by 5" % (str(x1), str(c1), str(i2))
        #if i2 % 6 == 0:
        #    print "%s %s %s is divisible by 6" % (str(x1), str(c1), str(i2))
        phi1 = n2 / n1
        print(("%s %s" % (str(c1), str(phi1))))
        if False:
            diff = phi1 - 1.61803398875
            if diff < 0:
                diff = -diff
            if diff < 0.000000000001:
                break
    print(("f1 = %s" % str(f1)))

main()
