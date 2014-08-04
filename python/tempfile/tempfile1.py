#!/usr/bin/python

import tempfile

tmp1 = tempfile.NamedTemporaryFile()
print "tmp1 = %s" % str(tmp1)
print "tmp1 = %s" % dir(tmp1)
print "tmp1.name = %s" % str(tmp1.name)

tmp1 = tempfile.NamedTemporaryFile(suffix = '.sql')
print "tmp1 = %s" % str(tmp1)
print "tmp1 = %s" % dir(tmp1)
print "tmp1.name = %s" % str(tmp1.name)

tmp1 = tempfile.NamedTemporaryFile(suffix = '.sql', prefix = 'ldt_scan')
print "tmp1 = %s" % str(tmp1)
print "tmp1 = %s" % dir(tmp1)
print "tmp1.name = %s" % str(tmp1.name)
