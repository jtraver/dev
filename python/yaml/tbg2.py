#!/usr/bin/python

import yaml

tbg1 = yaml.load(file('../../../test/john/env/tbg/tbg1.yml'))
print "tbg1 = %s" % str(tbg1)
tbg2 = yaml.load(file('../../../test/john/env/tbg/tbg2.yml'))
print "tbg2 = %s" % str(tbg2)
