#!/usr/bin/python

from ctypes import create_string_buffer

buf = create_string_buffer(10)
print "buf = %s" % str(buf)
print "buf = %s" % str(type(buf))
print "buf = %s" % str(dir(buf))
buf[0] = 'a'
print "buf = %s" % str(buf.raw)
print "buf = %s" % str(buf[0])
