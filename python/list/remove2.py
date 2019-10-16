#!/usr/bin/python

import apihelper

list1 = [ 0, 1, 2, 3, 5, 7 ]

print "list1 = %s" % str(list1)
# for i in xrange(len(list1)):
while list1:
    list1.remove(0)
    print "list1 = %s" % str(list1)
print "list1 = %s" % str(list1)
