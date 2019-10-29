#!/usr/bin/env python3
#!/usr/bin/python

import distutils
from distutils.version import StrictVersion
# import verlib

print "distutils = %s" % str(distutils)
print "distutils = %s" % dir(distutils)

print "distutils.version = %s" % str(distutils.version)
print "distutils.version = %s" % dir(distutils.version)

print "StrictVersion = %s" % str(StrictVersion)
print "StrictVersion = %s" % dir(StrictVersion)

# print "verlib = %s" % str(verlib)
# print "verlib = %s" % dir(verlib)

ver1 = '0.0.1'
parts1 = ver1.split('-')
print "parts1 = %s" % str(parts1)
parts = parts1[0].split('.')
print "parts = %s" % str(parts)
parts[2] = str(int(parts[2]) + 1)
ver2 = '.'.join(parts)
print "ver2 = %s" % str(ver2)

ver1 = '0.0.1-1-g8df5492'
parts1 = ver1.split('-')
print "parts1 = %s" % str(parts1)
parts = parts1[0].split('.')
print "parts = %s" % str(parts)
parts[2] = str(int(parts[2]) + 1)
ver2 = '.'.join(parts)
print "ver2 = %s" % str(ver2)
