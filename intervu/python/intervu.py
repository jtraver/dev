#!/usr/bin/python

import re

str1 = "an arbitrary string literal containing chars like: !#$!@#!%ls813"

print " "
print str1

# taken from
# citrusleaf/monitoring-console/server/site-packages/pkg_resources.py
print " "
print "re.sub('[^A-Za-z0-9.]+', '_', str1)"
print re.sub('[^A-Za-z0-9.]+', '_', str1)
print " "
print "re.sub('[^A-Za-z0-9.]', '_', str1)"
print re.sub('[^A-Za-z0-9.]', '_', str1)


def replaceIt(str1):
    print " "
    print "return re.sub('[^A-Za-z0-9.]+', '_', str1)"
    return re.sub('[^A-Za-z0-9.]+', '_', str1)

print " "
print "replaceIt(str1)"
print replaceIt(str1)

print re.sub('[^a-z]', '_', "A basic string.")
print re.sub('[^a-z]', '_', "A BASIC STRING.")
print re.sub('[^a-z|^A-Z]', '_', "A basic string.")
print re.sub('[^a-z|^A-Z]', '_', "A basic string | ^.")
print re.sub('[^a-z|^A-Z]', '_', "A basic string with | ^ and the numbers 1 and 13.")
