#!/usr/bin/python

# http://stackoverflow.com/questions/379906/parse-string-to-float-or-int
def num(s):
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


v1 = 'the longest yard'
v2 = num(v1)
v3 = str(v2)
if v1 == v2:
    print "string works"
else:
    print "string does not work"
if v1 == v3:
    print "string back to string works"
else:
    print "string back to string does not work"

v1 = '1023'
v2 = num(v1)
v3 = str(v2)
if v1 == v2:
    print "int does not work"
else:
    print "int works"
if v1 == v3:
    print "int back to string works"
else:
    print "int back to string does not work"

v1 = '3.14'
v2 = num(v1)
v3 = str(v2)
if v1 == v2:
    print "float does not work"
else:
    print "float works"
if v1 == v3:
    print "float back to string works"
else:
    print "float back to string does not work"
