#!/usr/bin/python

def main():
    int1()

def int1():
    y = 256
    for t in xrange(y):
        print "%x %d" % (t, t)
        
main()
