#!/usr/bin/env python3


import os
import platform
import sys

import aerospike

def main():
    myhostname = os.environ['MYHOSTNAME']
    print("\nos")
    print("os.name = %s" % str(os.name))
    print("sys.platform = %s" % str(sys.platform))
    print("platform.platform() = %s" % str(platform.platform()))
    print("\npython")
    print("sys.version = %s" % str(sys.version))
    print("sys.version_info = %s" % str(sys.version_info))
    print("sys.version_info[0] = %s" % str(sys.version_info[0]))
    print("\naerospike")
    try:
        print("%s py3 aerospike client version is %s" % (str(myhostname), str(aerospike.__version__)))
    except Exception as e:
        print("e = %s" % str(e))
        pass
    if 'MAP_RETURN_UNORDERED_MAP' in dir(aerospike):
        print(("Python client supports MAP_RETURN_UNORDERED_MAP (%s)" % aerospike.MAP_RETURN_UNORDERED_MAP))
    else:
        print("Python client does not support MAP_RETURN_UNORDERED_MAP")


main()

