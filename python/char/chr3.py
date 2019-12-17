#!/usr/bin/python

#for i1 in xrange(256):
#    str2 = "%s %d 0x%x '%c'" % (str(i1), i1, i1, i1)
#    print "str2 = %s" % str2

#for i1 in range(32, 127):
#    c1 = chr(i1)
#    print "%d %s" % (i1, c1)

n1 = 53023068927281
while n1:
    print "n1 = %s" % str(n1)
    n2 = n1 % 256
    n1 = n1 / 256
    print "n2 = %s %d 0x%x '%c'" % (str(n2), n2, n2, n2)
