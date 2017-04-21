#!/usr/bin/python

import glob

def main():
    pyfiles = glob.glob("../*/*.py")
    for pyfile in pyfiles:
        print "pyfile %s" % pyfile

main()
