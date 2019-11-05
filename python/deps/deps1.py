#!/usr/bin/python

import apihelper
import sys
import os
import platform


has_argparse = False
try:
    import argparse
    has_argparse = True
except Exception, e:
    print "e = %s" % str(e)
if has_argparse:
    print "\nSTART apihelper.info(argparse)"
    apihelper.info(argparse)


has_bcrypt = False
try:
    import bcrypt
    has_bcrypt = True
except Exception, e:
    print "e = %s" % str(e)
if has_bcrypt:
    print "\nSTART apihelper.info(bcrypt)"
    apihelper.info(bcrypt)


has_openssl = False
try:
    import OpenSSL
    has_openssl = True
except Exception, e:
    print "e = %s" % str(e)
if has_openssl:
    print "\nSTART apihelper.info(OpenSSL)"
    apihelper.info(OpenSSL)

has_pexpect = False
try:
    import pexpect
    has_pexpect = True
except Exception, e:
    print "e = %s" % str(e)
if has_pexpect:
    print "\nSTART apihelper.info(pexpect)"
    apihelper.info(pexpect)

has_ply = False
try:
    import ply
    has_ply = True
except Exception, e:
    print "e = %s" % str(e)
if has_ply:
    print "\nSTART apihelper.info(ply)"
    apihelper.info(ply)


print "\nSTART apihelper.info(sys)"
apihelper.info(sys)
print "\nSTART apihelper.info(os)"
apihelper.info(os)

print "\nSTART platform = %s" % str(sys.platform)
print "\nSTART os name = %s" % str(os.name)
print "\nSTART apihelper.info(sys.platform)"
apihelper.info(sys.platform)
print "\nSTART apihelper.info(os.name)"
apihelper.info(os.name)
print "\nSTART uname -a"
os.system("uname -a")
print "\nSTART apihelper.info(platform)"
apihelper.info(platform)

print "platform.platform = %s" % str(platform.platform())
print "platform.system = %s" % str(platform.system())
print "platform.release = %s" % str(platform.release())
print "platform.version = %s" % str(platform.version())
print "platform.linux_distrubution = %s" % str(platform.linux_distribution())

print "sys.version = %s" % str(sys.version)
print "platform.dist = %s" % str(platform.dist())
print "platform.system = %s" % str(platform.system())
print "platform.machine = %s" % str(platform.machine())
print "platform.platform = %s" % str(platform.platform())
print "platform.uname = %s" % str(platform.uname())
print "platform.version = %s" % str(platform.version())
print "platform.mac_ver = %s" % str(platform.mac_ver())

osname = "centos"
print "\nchecking pip for argparse"
os.system("pip list --format=columns | grep -i argparse")
print "\nchecking pip for bcrypt"
os.system("pip list --format=columns | grep -i bcrypt")
print "\nchecking pip for openssl"
os.system("pip list --format=columns | grep -i openssl")
print "\nchecking pip for pexpect"
os.system("pip list --format=columns | grep -i pexpect")
print "\nchecking pip for ply"
os.system("pip list --format=columns | grep -i ply")
if "centos" in platform.dist():
    print "found centos"
    print "\nchecking rpm for argparse"
    os.system("rpm -q -a | grep -i argparse")
    print "\nchecking rpm for bcrypt"
    os.system("rpm -q -a | grep -i bcrypt")
    print "\nchecking rpm for openssl"
    os.system("rpm -q -a | grep -i openssl")
    print "\nchecking rpm for pexpect"
    os.system("rpm -q -a | grep -i pexpect")
    print "\nchecking rpm for ply"
    os.system("rpm -q -a | grep -i ply")
else:
    osname = "debian"
    print "\nchecking dpkg for argparse"
    os.system("dpkg -l | grep -i argparse")
    print "\nchecking dpkg for bcrypt"
    os.system("dpkg -l | grep -i bcrypt")
    print "\nchecking dpkg for openssl"
    os.system("dpkg -l | grep -i openssl")
    print "\nchecking dpkg for pexpect"
    os.system("dpkg -l | grep -i pexpect")
    print "\nchecking dpkg for ply"
    os.system("dpkg -l | grep -i ply")

if has_argparse:
    print "has argparse"
else:
    print "does not have argparse"

if has_bcrypt:
    print "has bcrypt"
else:
    print "does not have bcrypt"

if has_openssl:
    print "has openssl"
else:
    print "does not have openssl"

if has_pexpect:
    print "has pexpect"
else:
    print "does not have pexpect"

if has_ply:
    print "has ply"
else:
    print "does not have ply"
