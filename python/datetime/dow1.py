#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import time
import datetime

now = datetime.datetime.now()
print "now = %s" % str(now)
print now
today = datetime.datetime.today()
print "today = %s" % str(today)
print today
dow = datetime.datetime.today().weekday()
print "dow = %s" % str(dow)

d1 = datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
print "d1 = %s" % str(d1)
print d1

for year in xrange(1000, 10000):
    dows = ''
    for month in xrange(1, 13):
        d1 = datetime.datetime(year, month, 1, 13, 13, 13, 173504)
        print "d1 = %s" % str(d1)
        print "dow = %s" % str(d1.weekday())
        dows += str(d1.weekday())
        dows += ' '
    # dows += str(year)
    print "dows %s" % str(dows)
