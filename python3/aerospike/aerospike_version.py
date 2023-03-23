#!/usr/bin/env python3

import aerospike



def main():
    if '__version__' in dir(aerospike):
        print(("Python client version is %s" % aerospike.__version__))
    else:
        print("don't know what Python client version is")
    if 'MAP_RETURN_UNORDERED_MAP' in dir(aerospike):
        print(("Python client supports MAP_RETURN_UNORDERED_MAP (%s)" % aerospike.MAP_RETURN_UNORDERED_MAP))
    else:
        print("Python client does not support MAP_RETURN_UNORDERED_MAP")

main()
