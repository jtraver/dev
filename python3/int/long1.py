#!/usr/bin/env python3

import sys

def main():
    int1()

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
        
main()
