#!/usr/bin/python

import os
import yaml


supple1 = yaml.load(file('supple.yml'))
# print "supple1 = %s" % str(supple1)

with open('supple2.yml', 'w') as outfile:
    outfile.write(yaml.dump(supple1, default_flow_style=False))

# os.system('cat supple.yml')
# os.system('cat supple2.yml')
print 'diff supple.yml supple2.yml'
os.system('diff supple.yml supple2.yml')
