#!/usr/bin/env python3
#!/usr/bin/python

import os
import sys

print "env = %s" % str(os.environ)

print os.environ['HOME']
print os.environ.get('HOME')
print os.environ.get('JOB_NAME', 'job_name')

print sys.prefix
