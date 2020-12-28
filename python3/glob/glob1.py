#!/usr/bin/env python3

import glob

def main():
    pyfiles = glob.glob("../*/*.py")
    for pyfile in pyfiles:
        print(("pyfile %s" % pyfile))

main()
