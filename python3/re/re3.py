#!/usr/bin/env python3
#!/usr/bin/python

# http://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string

import re

line = "77 tests: 77 passed, 0 failed"
regex = re.compile(
    r'^\s*(?P<tests>\d+?)\s*tests:\s*(?P<passed>\d+?)\s*passed,\s*(?P<failed>\d+?)\s*failed.*$')
# regex = re.compile('^.*\d+\s*tests:\s*\d+\s*passed,\s*\d+\s*failed.*$')
# regex = re.compile(r'.*(?P<tests>\d+?)\s*failed.*$')

parts = regex.match(line)

print "parts = %s" % str(parts)
print "parts = %s" % str(dir(parts))

parts = parts.groupdict()

print "parts = %s" % str(parts)
