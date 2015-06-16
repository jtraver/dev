#!/usr/bin/python

import random

types = [
    "boolean",
    "bytearray",
    "dict",
    "float",
    "frozenset",
    "integer",
    "list",
    "set",
    "string",
    "tuple",
    "unicode",
]

collections = [
    "dict",
    "frozenset",
    "list",
    "set",
    "tuple",
]

basic = [
    "boolean",
    "bytearray",
    "float",
    "integer",
    "string",
    "unicode",
]

def make_bytearray():
    val = bytearray()
    len1 = random.randint(0, 10)
    for x in range(len1):
        byte = random.randint(0, 255)
        val.append(byte)
    return val

def make_list():
    val = []
    nbins = random.randint(0, 100)
    depth = random.randint(0, 2)
    htype = random.randint(0, len(basic) - 1)
    for bin in range(nbins):
        if depth == 0:
            val.append(make_homogenous_data(htype))
        elif depth == 1:
            val.append(make_basic_data())
        else:
            val.append(make_any_data())
    return val

def make_frozenset():
    val = [ 3 ]
    return frozenset(val)

def make_any_data():
    val = 1
    type = random.randint(0, len(types) - 1)
    stype = types[type]
    if stype == 'boolean' or stype == 'bytearray' or stype == 'float':
        val = make_homogenous_data(type)
    elif stype == 'dict':
        val = make_dict()
    elif stype == 'frozenset':
        val = make_frozenset()
    return val

def make_dict():
    nbins = random.randint(0, 5)
    return make_record(nbins)

def make_basic_data():
    type = random.randint(0, len(basic) - 1)
    return make_homogenous_data(type)

# https://docs.python.org/2/library/random.html
# >>> random.random()        # Random float x, 0.0 <= x < 1.0
# 0.37444887175646646
# >>> random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
# 1.1800146073117523
# >>> random.randint(1, 10)  # Integer from 1 to 10, endpoints included
# 7
# >>> random.randrange(0, 101, 2)  # Even integer from 0 to 100
# 26
# >>> random.choice('abcdefghij')  # Choose a random element
# 'c'
# 
# >>> items = [1, 2, 3, 4, 5, 6, 7]
# >>> random.shuffle(items)
# >>> items
# [7, 3, 2, 5, 6, 4, 1]
# 
# >>> random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
# [4, 1, 5]

def make_homogenous_data(htype):
    val = 2
    stype = basic[htype]
    if stype == 'boolean':
        type = random.randint(0, 1)
        if type:
            val = True
        else:
            val = False
    elif stype == 'bytearray':
        val = make_bytearray()
    elif stype == 'float':
        val = random.random() * random.randint(1, 100000)
    return val

def make_record(max_bins):
    record = dict()
    nbins = random.randint(0, max_bins)
    depth = random.randint(0, 2)
    htype = random.randint(0, len(basic) - 1)
    for bin in range(nbins):
        bname = "b" + str(bin)
        if depth == 0:
            record[bname] = make_homogenous_data(htype)
        elif depth == 1:
            record[bname] = make_basic_data()
        else:
            record[bname] = make_any_data()
    return record

def doit():
    record = make_record(10)
    # print "record = %s" % str(record)
    for k,v in record.items():
        print "%s %s" % (k, str(v))

def main():
    doit()

main()
