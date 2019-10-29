#!/usr/bin/env python3
#!/usr/bin/python

import os
import platform
import sys

import aerospike

def main():
    print "\nos"
    print "os.name = %s" % str(os.name)
    print "sys.platform = %s" % str(sys.platform)
    print "platform.platform() = %s" % str(platform.platform())
    print "\npython"
    print "sys.version = %s" % str(sys.version)
    print "sys.version_info = %s" % str(sys.version_info)
    print "sys.version_info[0] = %s" % str(sys.version_info[0])
    print "\naerospike"
    try:
        print "aerospike client version is %s" % str(aerospike.__version__)
    except Exception, e:
        print "e = %s" % str(e)
        pass

main()
