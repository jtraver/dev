#!/usr/bin/python

for i1 in xrange(256):
    str2 = "%s %d 0x%x '%c'" % (str(i1), i1, i1, i1)
    print "str2 = %s" % str2

#for i1 in range(32, 127):
#    c1 = chr(i1)
#    print "%d %s" % (i1, c1)
