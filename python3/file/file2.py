#!/usr/bin/env python3


def file(filename):
    f = open(filename, "r")
    contents = ""
    for line in f:
        contents += line
    return contents



# file1 = file('file1.py').read()
file1 = file('file1.py')
print(("file1 = %s" % str(file1)))
