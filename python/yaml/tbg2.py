#!/usr/bin/python

import yaml

tbg1 = yaml.load(file('../../../test/john/env/tbg/tbg1.yml'))
print "tbg1 = %s" % str(tbg1)
print "\n"
tbg2 = yaml.load(file('../../../test/john/env/tbg/tbg2.yml'))
print "tbg2 = %s" % str(tbg2)

print "\n"
t1 = {}
for k1 in tbg1.keys():
    t1[k1] = tbg1[k1].keys()
print "t1 = %s" % str(t1)
