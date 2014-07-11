#!/usr/bin/python

# http://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string

import re

line = "Run '/tmp/aggr_aql.txt'"

regex = re.compile(r'^.*Run \'(?P<filename>[^\']+?)\'.*$')

parts = regex.match(line)

print "parts = %s" % str(parts)
print "parts = %s" % str(dir(parts))

parts = parts.groupdict()

print "parts = %s" % str(parts)
filename = parts['filename']
print "filename = %s" % str(filename)
