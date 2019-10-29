#!/usr/bin/env python3
#!/usr/bin/python

import sys
import yaml

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"

def list1():
    print "\n---------------------------------------------------------------------------------"
    print "list1"
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
    # l2 = yaml.load(file(fn1))
    l2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if l1 == l2:
        print "list1: load and dump worked"
        return 0
    else:
        print "list1: load and dump did not work"
        return 1

def dict1():
    print "\n---------------------------------------------------------------------------------"
    print "dict1"
    d1 = {}
    d1["sunrider"] = None
    d1["bulletproof"] = None
    d1["metagenics"] = None
    d1["nutrigold"] = None
    d1["standard process"] = None
    d1["irwin naturals"] = None
    fn1 = "dict1.yaml"
    s1 = yaml.dump(d1, default_flow_style=False)
    print "s1 =\n%s" % str(s1)
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    # d2 = yaml.load(file(fn1))
    d2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if d1 == d2:
        print "dict1: load and dump worked"
        return 0
    else:
        print "dict1: load and dump did not work"
        return 1

def list2():
    print "\n---------------------------------------------------------------------------------"
    print "list2"
    l1 = []
    l1.append(["sunrider", 1])
    l1.append(["bulletproof", 2])
    l1.append(["metagenics", 3])
    l1.append(["nutrigold", 4])
    l1.append(["standard process", 5])
    l1.append(["irwin naturals", 6])
    fn1 = "list2.yaml"
    s1 = yaml.dump(l1, default_flow_style=False)
    print "s1 =\n%s" % str(s1)
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    # l2 = yaml.load(file(fn1))
    l2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if l1 == l2:
        print "list2: load and dump worked"
        return 0
    else:
        print "list2: load and dump did not work"
        return 1

def dict2():
    print "\n---------------------------------------------------------------------------------"
    print "dict2"
    d1 = {}
    d1["sunrider"] = { "order": 1 }
    d1["bulletproof"] = { "order": 2 }
    d1["metagenics"] = { "order": 3 }
    d1["nutrigold"] = { "order": 4 }
    d1["standard process"] = { "order": 5 }
    d1["irwin naturals"] = { "order": 6 }
    fn1 = "dict2.yaml"
    s1 = yaml.dump(d1, default_flow_style=False)
    print "s1 =\n%s" % str(s1)
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    d2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if d1 == d2:
        print "dict2: load and dump worked"
        return 0
    else:
        print "dict2: load and dump did not work"
        return 1

def ld1():
    print "\n---------------------------------------------------------------------------------"
    print "ld1"
    l1 = []
    l1.append({ "name": "sunrider", "order": 1})
    l1.append({ "name": "bulletproof", "order": 2})
    l1.append({ "name": "metagenics", "order": 3})
    l1.append({ "name": "nutrigold", "order": 4})
    l1.append({ "name": "standard process", "order": 5})
    l1.append({ "name": "irwin naturals", "order": 6})
    fn1 = "ld1.yaml"
    s1 = yaml.dump(l1, default_flow_style=False)
    print "s1 =\n%s" % str(s1)
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    l2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if l1 == l2:
        print "ld1: load and dump worked"
        return 0
    else:
        print "ld1: load and dump did not work"
        return 1

def dl1():
    print "\n---------------------------------------------------------------------------------"
    print "dl1"
    d1 = {}
    d1["sunrider"] = ["order", 1]
    d1["bulletproof"] = ["order", 2]
    d1["metagenics"] = ["order", 3]
    d1["nutrigold"] = ["order", 4]
    d1["standard process"] = ["order", 5]
    d1["irwin naturals"] = ["order", 6]
    fn1 = "dl1.yaml"
    s1 = yaml.dump(d1, default_flow_style=False)
    print "s1 =\n%s" % str(s1)
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    d2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if d1 == d2:
        print "dl1: load and dump worked"
        return 0
    else:
        print "dl1: load and dump did not work"
        return 1



def main():
    ret1 = 0
    ret1 += list1()
    ret1 += dict1()
    ret1 += list2()
    ret1 += dict2()
    ret1 += ld1()
    ret1 += dl1()
    if ret1:
        print "%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP)
    else:
        print "%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP)
    print "DONE"
    print "^G"
    sys.stdout.flush()
    sys.exit(ret1)

main()
