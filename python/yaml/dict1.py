#!/usr/bin/python

import sys
import yaml

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"

def list1():
    l1 = []
    l1.append("sunrider")
    l1.append("bulletproof")
    l1.append("metagenics")
    l1.append("nutrigold")
    l1.append("standard process")
    l1.append("irwin naturals")
    fn1 = "list1.yaml"
    s1 = yaml.dump(l1, default_flow_style=False)
    print "s1 =\n%s" % str(s1)
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    l2 = yaml.load(file(fn1))
    if l1 == l2:
        print "list1: load and dump worked"
        return 0
    else:
        print "list1: load and dump did not work"
        return 1

def dict1():
    d1 = []
    d1.append("sunrider")
    d1.append("bulletproof")
    d1.append("metagenics")
    d1.append("nutrigold")
    d1.append("standard process")
    d1.append("irwin naturals")
    fn1 = "dict1.yaml"
    s1 = yaml.dump(d1, default_flow_style=False)
    print "s1 =\n%s" % str(s1)
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    d2 = yaml.load(file(fn1))
    if d1 == d2:
        print "load and dump worked"
        return 0
    else:
        print "load and dump did not work"
        return 1

def main():
    ret1 = 0
    ret1 += dict1()
    if ret1:
        print "%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP)
    else:
        print "%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP)
    print "DONE"
    print "^G"
    sys.stdout.flush()
    sys.exit(ret1)

main()
