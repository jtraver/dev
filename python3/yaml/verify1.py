#!/usr/bin/env python3
#!/usr/bin/python

import sys
import yaml

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"


def file(filename):
    f = open(filename, "r")
    contents = ""
    for line in f:
        contents += line
    f.close()
    return contents



def list1():
    print("\n---------------------------------------------------------------------------------")
    print("list1")
    l1 = []
    l1.append("sunrider")
    l1.append("bulletproof")
    l1.append("metagenics")
    l1.append("nutrigold")
    l1.append("standard process")
    l1.append("irwin naturals")
    fn1 = "list1.yaml"
    s1 = yaml.dump(l1, default_flow_style=False)
    print("s1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    # l2 = yaml.load(file(fn1))
    l2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if l1 == l2:
        print("list1: load and dump worked")
        return 0
    else:
        print("list1: load and dump did not work")
        return 1

def dict1():
    print("\n---------------------------------------------------------------------------------")
    print("dict1")
    d1 = {}
    d1["sunrider"] = None
    d1["bulletproof"] = None
    d1["metagenics"] = None
    d1["nutrigold"] = None
    d1["standard process"] = None
    d1["irwin naturals"] = None
    fn1 = "dict1.yaml"
    s1 = yaml.dump(d1, default_flow_style=False)
    print("s1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    # d2 = yaml.load(file(fn1))
    d2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if d1 == d2:
        print("dict1: load and dump worked")
        return 0
    else:
        print("dict1: load and dump did not work")
        return 1

def list2():
    print("\n---------------------------------------------------------------------------------")
    print("list2")
    l1 = []
    l1.append(["sunrider", 1])
    l1.append(["bulletproof", 2])
    l1.append(["metagenics", 3])
    l1.append(["nutrigold", 4])
    l1.append(["standard process", 5])
    l1.append(["irwin naturals", 6])
    fn1 = "list2.yaml"
    s1 = yaml.dump(l1, default_flow_style=False)
    print("s1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    # l2 = yaml.load(file(fn1))
    l2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if l1 == l2:
        print("list2: load and dump worked")
        return 0
    else:
        print("list2: load and dump did not work")
        return 1

def dict2():
    print("\n---------------------------------------------------------------------------------")
    print("dict2")
    d1 = {}
    d1["sunrider"] = { "order": 1 }
    d1["bulletproof"] = { "order": 2 }
    d1["metagenics"] = { "order": 3 }
    d1["nutrigold"] = { "order": 4 }
    d1["standard process"] = { "order": 5 }
    d1["irwin naturals"] = { "order": 6 }
    fn1 = "dict2.yaml"
    s1 = yaml.dump(d1, default_flow_style=False)
    print("s1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    # d2 = yaml.load(file(fn1))
    d2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if d1 == d2:
        print("dict2: load and dump worked")
        return 0
    else:
        print("dict2: load and dump did not work")
        return 1



def main():
    ret1 = 0
    ret1 += list1()
    ret1 += dict1()
    ret1 += list2()
    ret1 += dict2()
    ret1 += verify1()
    if ret1:
        print("%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP))
    else:
        print("%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP))
    print("DONE")
    print("^G")
    sys.stdout.flush()
    sys.exit(ret1)

def verify1():
    ret1 = 0
    print("\n---------------------------------------------------------------------------------")
    print("verify1a")

    list1 = []
    list1.append("list1 item 01")
    list1.append("list1 item 02")
    list1.append("list1 item 03")

    list2 = []
    list2.append("list2 item 01")
    list2.append("list2 item 02")
    list2.append("list2 item 03")

    list1.append(list2)
    list1.append("list1 item 04")
    list1.append("list1 item 05")
    list1.append("list1 item 06")

    list3 = []
    list3.append("list3 item 01")
    list3.append("list3 item 02")
    list3.append("list3 item 03")

    list4 = []
    list4.append("list4 item 01")
    list4.append("list4 item 02")
    list4.append("list4 item 03")

    dict1 = {}
    dict1["dict1 key 01"] = "dict1 value 01"
    dict1["dict1 key 02"] = "dict1 value 02"
    dict1["dict1 key 03"] = "dict1 value 03"

    dict2 = {}
    dict2["dict2 key 01"] = "dict2 value 01"
    dict2["dict2 key 02"] = "dict2 value 02"
    dict2["dict2 key 03"] = "dict2 value 03"
    dict2["list4"] = list4

    dict3 = {}
    dict3["dict3 key 01"] = "dict3 value 01"
    dict3["dict3 key 02"] = "dict3 value 02"
    dict3["dict3 key 03"] = "dict3 value 03"

    list1.append(dict3)
    list1.append("list1 item 07")
    list1.append("list1 item 08")
    list1.append("list1 item 09")

    fn1 = "verify1a.yaml"
    s1 = yaml.dump(list1, default_flow_style=False)
    print("list1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    llist1 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if list1 == llist1:
        print("verify1a: load and dump worked")
    else:
        print("verify1a: load and dump did not work")
        ret1 += 1

    print("\n---------------------------------------------------------------------------------")
    print("verify1b")

    dict1["dict2"] = dict2
    dict1["dict1 key 04"] = "dict1 value 04"
    dict1["dict1 key 05"] = "dict1 value 05"
    dict1["dict1 key 06"] = "dict1 value 06"

    dict1["list1"] = list1
    dict1["dict1 key 07"] = "dict1 value 07"
    dict1["dict1 key 08"] = "dict1 value 08"
    dict1["dict1 key 09"] = "dict1 value 09"

    fn1 = "verify1b.yaml"
    s1 = yaml.dump(dict1, default_flow_style=False)
    print("dict1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    ldict1 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if dict1 == ldict1:
        print("verify1b: load and dump worked")
    else:
        print("verify1b: load and dump did not work")
        ret1 += 1
    return ret1

main()
