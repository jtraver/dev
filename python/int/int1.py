#!/usr/bin/python

def main():
    int1()

def int1():
    s = 400
    y = 22
    i = 0.08
    for t in xrange(y):
        a = s * i
        s += a
    print "%s" % str(s)
        
main()
