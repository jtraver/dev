#!/usr/bin/env python3
#!/usr/bin/python

import sys
import inspect

DEBUG1 = True

def func0(fof1):
    print(("START func0 fof1 = %s" % str(fof1)))
    c=inspect.currentframe()
    print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    print("END func0")

def func1(fof1):
    print(("START func1 fof1 = %s" % str(fof1)))
    fof1(func0)
    c=inspect.currentframe()
    print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    if DEBUG1:
        print((sys._getframe().f_code.co_name))
        print(("called from %s:%d" % inspect.stack()[1][1:3]))
        print(("line = %s" % str(c.f_lineno)))
        print(("file = %s" % str(c.f_code.co_filename)))
        print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    print("END func1")


def func2(fof1):
    print(("START func2 fof1 = %s" % str(fof1)))
    fof1(func1)
    c=inspect.currentframe()
    print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    if DEBUG1:
        print((sys._getframe().f_code.co_name))
        print(("called from %s:%d" % inspect.stack()[1][1:3]))
        print(("line = %s" % str(c.f_lineno)))
        print(("file = %s" % str(c.f_code.co_filename)))
        print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    print("END func2")


def func3(fof1):
    print(("START func3 fof1 = %s" % str(fof1)))
    fof1(func2)
    c=inspect.currentframe()
    print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    if DEBUG1:
        print((sys._getframe().f_code.co_name))
        print(("called from %s:%d" % inspect.stack()[1][1:3]))
        print(("line = %s" % str(c.f_lineno)))
        print(("file = %s" % str(c.f_code.co_filename)))
        print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    print("END func3")


def main():
    print("\nmain1")
    func1(func0)
    print("\nmain2")
    func2(func1)
    print("\nmain3")
    func3(func2)
    print("\nmain4")

    f0 = func0
    func1
    func2
    func3


main()
