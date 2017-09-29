#!/usr/bin/python

import os
import yaml

filename = 'yaml3.config'

dc1 = []
dc1.append({"ip": "111.111.111.111", "name": "a1"})
dc1.append({"ip": "222.222.222.222", "name": "b1"})
config1 = []
config1.append({"name": "dc1", "nodes": dc1})

with open(filename, 'w') as outfile:
    outfile.write(yaml.dump(config1, default_flow_style=False))

config2 = yaml.load(file(filename))
print "config2 = %s" % str(config2)

if config1 == config2:
    print "load and dump worked"
else:
    print "load and dump did not work"

os.system("cat " + filename)
