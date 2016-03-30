#!/usr/bin/python

import apihelper
import docker


def pinfo(object):
    print
    print "--------------------------------------------------------------------------------"
    print "| %s" % str(object)
    print "--------------------------------------------------------------------------------"
    apihelper.info(object)


def main():
    pinfo(docker)

main()
