#!/usr/bin/python

import bcrypt

def main():
    pwd = bcrypt.hashpw("bogus", "$2a$10$7EqJtq98hPqEX7fNZaFWoO")
    print "pwd = %s" % str(pwd)

main()
