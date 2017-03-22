#!/usr/bin/python

import os
import sys
import env
import apihelper

print "env = %s" % str(os.environ)

print os.environ['HOME']
print os.environ.get('HOME')
print os.environ.get('JOB_NAME', 'job_name')

print sys.prefix

def pinfos():
    pinfo(env)

def pinfo(object):
    print
    print "--------------------------------------------------------------------------------"
    print "| %s" % str(object)
    print "--------------------------------------------------------------------------------"
    apihelper.info(object)
    # print "aerospike = %s" % str(aerospike)
    # print "aerospike = %s" % dir(aerospike)
    # print "aerospike = %s" % type(aerospike)

    # print "--------------------------------------------------------------------------------"
    # print "| aerospike.Client"
    # print "--------------------------------------------------------------------------------"
    # apihelper.info(aerospike.Client)

pinfos()

print "env = %s" % str(env)
print "env = %s" % str(type(env))
print "env = %s" % str(dir(env))
