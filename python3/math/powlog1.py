#!/usr/bin/env python3

# pow        Return x**y (x to the power of y).

import math

# pow(5.6, 1.72) = 19.359021691633924

val1 = 5.6
log1 = math.log(val1)
print("1 log(%s) = %s" % (str(val1), str(log1)))

val2 = 4.0
log2 = math.log(val2)
print("2 log(%s) = %s" % (str(val2), str(log2)))

print("math.e = %s" % str(math.e))

val3 = math.e
log3 = math.log(val3)
print("3 log(%s) = %s" % (str(val3), str(log3)))
# 3 log(2.718281828459045) = 1.0

val4 = math.log(4.0) / math.log(2.0)
print("4 val4 = %s" % str(val4))

val5 = math.log(8.0) / math.log(2.0)
print("5 val5 = %s" % str(val5))

pow6 = 16.0
base6 = 2.0
exp6 = math.log(pow6) / math.log(base6)
print("6 exp6 = %s" % str(exp6))

pow6a = math.pow(base6, exp6)

if pow6a == pow6:
    print("found relationship")
else:
    print("did not find relationship")
