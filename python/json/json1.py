import os
import sys
import json

print "env = %s" % str(os.environ)

print os.environ['HOME']
print os.environ.get('HOME')
print os.environ.get('JOB_NAME', 'job_name')

print sys.prefix

print json.dumps(str(os.environ))

filename = "env.json"
fileh = open(filename, "w")
# fileh.write(json.dumps(str(os.environ)))
json.dump(str(os.environ), fileh)
fileh.close()


fileh = open(filename, "r")
json1 = json.load(fileh)
fileh.close()
print "json1 = %s" % str(json1)
