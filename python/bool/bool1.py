#!/usr/bin/python

def main():
    bool1()

def bool1():
    dict1 = {}
    dict1[False] = "this one is false"
    dict1[True] = "this one is true"
    for b1 in [False, True]:
        print "b1 = %s" % str(b1)
        if b1 in dict1:
            print "dict1[b1] = %s" % str(dict1[b1])
        else:
            print "b1 %s not found in dict1" % str(b1)

main();
