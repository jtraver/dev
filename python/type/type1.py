#!/usr/bin/python

test1 = None
if test1:
    print str(test1) + " is True"
else:
    print str(test1) + " is False"

test1 = 0
if test1:
    print str(test1) + " is True"
else:
    print str(test1) + " is False"

test1 = ''
if test1:
    print str(test1) + " is True"
else:
    print str(test1) + " is False"
if type(test1) is str:
    print str(test1) + " is String"
else:
    print str(test1) + " is not String"
if type(test1) is not str:
    print str(test1) + " is not String"
else:
    print str(test1) + " is String"

test1 = []
type1 = str(type(test1))
print "test1 type is %s" % type1
if type(test1) == list:
    print "test1 type is list"
