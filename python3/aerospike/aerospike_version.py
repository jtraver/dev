#!/usr/bin/env python3

import aerospike



def main():
    if '__version__' in dir(aerospike):
        print(("Python client version is %s" % aerospike.__version__))

main()
