#!/usr/bin/python

import re

str1 = "an arbitrary string literal containing chars like: !#$!@#!%ls813"

print str1

# taken from
# citrusleaf/monitoring-console/server/site-packages/pkg_resources.py
print re.sub('[^A-Za-z0-9.]+', '_', str1)
print re.sub('[^A-Za-z0-9.]', '_', str1)


def replaceIt(str1):
    return re.sub('[^A-Za-z0-9.]+', '_', str1)

print replaceIt(str1)
