#!/usr/bin/env python

def main():
    for i1 in xrange(256):
        print "%s 0x%x '%c'" % (str(i1), i1, i1)

main()
