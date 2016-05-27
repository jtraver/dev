#!/usr/bin/python

import sys

print "sys = %s" % str(sys)
print "sys = %s" % str(dir(sys))
print "sys.platform = %s" % str(sys.platform)


def func1():
    print sys._getframe().f_code.co_name


def func2():
    print sys._getframe().f_code.co_name


def func3():
    print sys._getframe().f_code.co_name


def main():
    func1()
    func2()
    func3()


main()
