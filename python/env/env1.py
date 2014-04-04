import os

print "env = %s" % str(os.environ)

print os.environ['HOME']
print os.environ.get('HOME')
print os.environ.get('JOB_NAME', 'job_name')
