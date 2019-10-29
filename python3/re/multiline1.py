#!/usr/bin/env python3
#!/usr/bin/python

import re


# pass_regex = re.compile(r'passing', re.MULTILINE)
# pass_regex = re.compile(r'hello', re.MULTILINE)
# pass_regex = re.compile(r'.*hello.*')
pass_regex = re.compile(r'.*?(?P<passing>\d+?) passing.*', re.MULTILINE)
# pass_regex = re.compile(r'.*passing.*', re.MULTILINE)
# pass_regex = re.compile(r'.*hello.*', re.MULTILINE)
fail_regex = re.compile(r'.*?(?P<failing>\d+?) failing.*')

line1 = """
hello and good-bye
how to make a multiline

string
in Python

with 42 passing somewhere in here


and with 3 failing as well

"""

# print "line = %s" % line1

# line1 = " hello "

pass_parts = pass_regex.match(line1)
print "pass_parts = %s" % str(pass_parts)
if pass_parts != None:
    pass_parts = pass_parts.groupdict()
    print "pass_parts = %s" % str(pass_parts)

pass_parts = pass_regex.search(line1)
print "pass_parts = %s" % str(pass_parts)
if pass_parts != None:
    pass_parts = pass_parts.groupdict()
    print "pass_parts = %s" % str(pass_parts)

fail_parts = fail_regex.search(line1)
print "fail_parts = %s" % str(fail_parts)
if fail_parts != None:
    fail_parts = fail_parts.groupdict()
    print "fail_parts = %s" % str(fail_parts)
