#!/usr/bin/env python3
import os
import sys
import json

print(("env = %s" % str(os.environ)))

print((os.environ['HOME']))
print((os.environ.get('HOME')))
print((os.environ.get('JOB_NAME', 'job_name')))

print((sys.prefix))

print((json.dumps(str(os.environ))))

filename = "env.json"
fileh = open(filename, "w")
# fileh.write(json.dumps(str(os.environ)))
json.dump(str(os.environ), fileh)
fileh.close()


fileh = open(filename, "r")
json1 = json.load(fileh)
fileh.close()
print(("json1 = %s" % str(json1)))

hosts = ['192.168.75.205', '192.168.75.206']
filename = "hosts.json"
fileh = open(filename, "w")
output = json.dumps(hosts)
fileh.write(output)
fileh.close()
fileh = open(filename, "r")
input = fileh.read()
fileh.close()
json1 = json.loads(input)
print((json1[0]))
print((json1[1]))
