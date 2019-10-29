#!/usr/bin/env python3
#!/usr/bin/python

val1 = None
type1 = type(val1)
print "type1 = %s" % str(type1)

val1 = False
type1 = type(val1)
print "type1 = %s" % str(type1)

val1 = 1.5
type1 = type(val1)
print "type1 = %s" % str(type1)

val1 = 98765432100123456789.98765432100123456789e+210
type1 = type(val1)
print "type1 = %s" % str(type1)
