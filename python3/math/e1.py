#!/usr/bin/env python3

import math

phi = (1 + math.sqrt(5)) / 2
# print("math = %s" % str(math))

print("math.pi = %s" % str(math.pi))
print("math.e = %s" % str(math.e))
print("phi = %s" % str(phi))

# e = (1 + 1/n)^n

e1 = 0
found = False
for n1 in range(1, 10000000):
    f1 = n1 * 1.0
    # print("n1 = %s" % str(n1))
    e1 = (1 + 1/f1) ** f1
    if e1 == math.e:
        print("found n1 = %s, e1 = %s" % (str(n1), str(e1)))
        found = True
        break
if not found:
    d1 = math.e - e1
    print("not found n1 = %s, e1 = %s, d1 = %s" % (str(n1), str(e1), str(d1)))
