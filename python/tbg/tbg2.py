#!/usr/bin/python

import yaml
import random

tbg1 = yaml.load(file('../../../test/john/env/tbg/tbg1.yml'))
print "tbg1 = %s" % str(tbg1)
tbg2 = yaml.load(file('../../../test/john/env/tbg/tbg2.yml'))
print "tbg2 = %s" % str(tbg2)

def show_tbg2(start, tbgn, indent):
    tbg0 = {}
    if tbg2[start]:
        print "%s%s:" % (indent, start)
    else:
        print "%s%s: null" % (indent, start)
    tbgn[start] = {}
    indent += "    "
    for x in tbg2[start]:
        tbg0[x] = {}
        show_tbg2(x, tbg0, indent)
    tbgn[start] = tbg0

def show_tbg1(tbg0, list0, indent):
    if tbg0:
        for x in sorted(tbg0.keys()):
            dict1[x] = []
            list0.append(x)
            print "%s%s" % (indent, x)
            show_tbg1(tbg0[x], dict1[x], indent + "  ")

def show_dict1():
    print "\n"
    print "dict1"
    for x in sorted(dict1.keys()):
        if dict1[x]:
            print "%s:" % x
        else:
            print "%s: []" % x
        for y in sorted(dict1[x]):
            print "- %s" % y

def merge_tbg2():
    for t2 in tbg2.keys():
        print "%s:" % t2
        if not t2 in dict1:
            dict1[t2] = []
        for t2a in tbg2[t2]:
            print "- %s" % t2a
            if not t2a in dict1[t2]:
                dict1[t2].append(t2a)

def check_dict(d1, d2):
    # print "check_dict: d1 = %s" % str(d1)
    # print "check_dict: d2 = %s" % str(d2)
    fail_count = 0
    if d1:
        for k1 in d1.keys():
            if not k1 in d2:
                print "FAIL: %s not in d2" % k1
                fail_count += 1
            else:
                fail_count += check_dict(d1[k1], d2[k1])
    if d2:
        for k2 in d2.keys():
            if not k2 in d1:
                print "FAIL: %s not in d1" % k2
                fail_count += 1
            else:
                fail_count += check_dict(d1[k2], d2[k2])
    return fail_count

start = 'love'
tbg3 = {}
print "\n"
print "tbg2"
show_tbg2(start, tbg3, "")
print "tbg3 = %s" % str(tbg3)

fail_count = check_dict(tbg1, tbg3)
if fail_count:
    print "FAIL"
    print "tbg3 = %s" % str(tbg3)
    indent = 4
    dict1 = {}
    dict1[start] = []
    show_tbg1(tbg1, dict1[start], "")
    show_dict1()
    merge_tbg2()
    show_dict1()
else:
    print "PASS"
