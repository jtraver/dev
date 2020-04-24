#!/usr/bin/env python3

import datetime
import sys

def main():
    int1()
    int2()

def int1():
    s = sys.maxsize
    print("sys.maxsize = %s" % str(s))
    # s = 9223372036854775807
    # print("%s" % str(s))
    for _ in range(30):
        s *= 2
        print("%s" % str(s))
    s *= 2
    print("%s" % str(s))

def int2():
    max1 = sys.maxsize
    d1 = datetime.datetime.now()
    ts1 = d1.strftime("%y%m%d%H%M%S%f")
    int1 = int(ts1)
    str1 = str(int1)
    if str1 == ts1:
        print("conversion worked")
    else:
        print("conversion failed")
        print("ts1 = %s" % str(ts1))
        print("int1 = %s" % str(int1))
        print("str1 = %s" % str(str1))
    if int1 > max1:
        print("%s is too big" % str(int1))
        print("%s is max size" % str(max1))
    else:
        print("timestamp worked as an int")


main()
