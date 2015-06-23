#!/usr/bin/python

import random

# max = 10
# max_depth = 5
# max_unicode = 100
# max_string = 100

max = 3
max_record = 0xFFFF
max_depth = 3
max_unicode = 10
max_string = 10

# max_string = 10
# max_unicode = 10
# max_depth = 3
# max = 3
# max_record = 3

max_byte_array = max
max_list = max
max_dict = max
max_unicode_char = 0xFFFF

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

hashable = [
    "boolean",
    "float",
    "integer",
    "string",
    "tuple",
    "unicode",
]

basic = [
    "boolean",
    "bytearray",
    "float",
    "integer",
    "string",
    "unicode",
]

# done
def make_bytearray():
    val = bytearray()
    len1 = random.randint(0, max_byte_array)
    for x in range(len1):
        byte = random.randint(0, 255)
        val.append(byte)
    return val

# done
def make_list(depth):
    if depth > max_depth:
        return None
    val = []
    nbins = random.randint(0, max_list)
    dtype = random.randint(0, 2)
    htype = random.randint(0, len(basic) - 1)
    for bin in range(nbins):
        if dtype == 0:
            val.append(make_homogenous_data(htype))
        elif dtype == 1:
            val.append(make_basic_data())
        else:
            val.append(make_any_data(depth + 1))
    return val

# TODO: hmmm
def make_tuple():
    val = (0, 1, 2, 3)
    return val

# done
# hashable = [ "boolean", "float", "integer", "string", "tuple", "unicode", ]
def make_hashable_data():
    val = 4
    dtype = random.randint(0, len(hashable) - 1)
    stype = hashable[dtype]
    if stype == 'boolean':
        dtype = random.randint(0, 1)
        if dtype:
            val = True
        else:
            val = False
    elif stype == 'bytearray':
        val = make_bytearray()
    elif stype == 'float':
        val = random.random() * random.randint(1, 100000)
    elif stype == 'integer':
        val = random.randint(1, 100000)
    elif stype == 'string':
        val = make_string()
    elif stype == 'tuple':
        val = make_tuple()
    elif stype == 'unicode':
        val = make_unicode()
    return val

# done
def make_hashable_list():
    val = []
    nbins = random.randint(0, max_list)
    for bin in range(nbins):
        val.append(make_hashable_data())
    return val

# done
def make_frozenset(depth):
    if depth > max_depth:
        return None
    val = make_hashable_list()
    return frozenset(val)

def make_set(depth):
    if depth > max_depth:
        return None
    val = make_hashable_list()
    return set(val)

# types = [ "boolean", "bytearray", "dict", "float", "frozenset", "integer", "list", "set", "string", "tuple", "unicode", ]
# basic = [ "boolean", "bytearray", "float", "integer", "string", "unicode", ]
def make_any_data(depth):
    if depth > max_depth:
        return None
    val = 1
    dtype = random.randint(0, len(types) - 1)
    stype = types[dtype]
    if stype == 'boolean' or stype == 'bytearray' or stype == 'float' or stype == 'integer' or stype == 'string' or stype == 'unicode':
        val = make_homogenous_data(stype)
    elif stype == 'dict':
        val = make_dict(depth + 1)
    elif stype == 'frozenset':
        val = make_frozenset(depth + 1)
    elif stype == 'list':
        val = make_list(depth + 1)
    elif stype == 'set':
        val = make_set(depth + 1)
    elif stype == 'tuple':
        val = make_tuple()
    return val

# done
def make_dict(depth):
    if depth > max_depth:
        return None
    nbins = random.randint(0, max_dict)
    return make_record(nbins, depth + 1)

# basic = [ "boolean", "bytearray", "float", "integer", "string", "unicode", ]
def make_basic_data():
    dtype = random.randint(0, len(basic) - 1)
    return make_homogenous_data(dtype)

# done
def make_string():
    nbins = random.randint(0, max_string)
    val = bytearray()
    for x in range(nbins):
        val.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    return str(val)

# done
def make_unicode():
    nbins = random.randint(0, max_unicode)
    u = unichr(random.randint(0, max_unicode_char))
    for x in range(nbins):
        c = random.randint(0, 1)
        if c:
            u = u + unichr(random.randint(0, max_unicode_char))
        else:
            u = u + unichr(random.randint(0xd800, 0xdbff))
            u = u + unichr(random.randint(0xdc00, 0xdfff))
    return u

# done
# basic = [ "boolean", "bytearray", "float", "integer", "string", "unicode", ]
def make_homogenous_data(htype):
    val = 2
    if type(htype) == int:
        stype = basic[htype]
    else:
        stype = htype
    if stype == 'boolean':
        dtype = random.randint(0, 1)
        if dtype:
            val = True
        else:
            val = False
    elif stype == 'bytearray':
        val = make_bytearray()
    elif stype == 'float':
        val = random.random() * random.randint(1, 100000)
    elif stype == 'integer':
        val = random.randint(1, 100000)
    elif stype == 'string':
        val = make_string()
    elif stype == 'unicode':
        val = make_unicode()
    return val

# done
def make_record(max_bins, depth):
    if depth > 5:
        return None
    record = dict()
    btype = random.randint(0, 32)
    if btype < 2:
        tot_bins = 1
    elif btype < 4:
        tot_bins = 10
    elif btype < 28:
        tot_bins = 100
    elif btype < 32:
        tot_bins = 1000
    else:
        tot_bins = max_bins
    nbins = random.randint(0, tot_bins)
    dtype = random.randint(0, 2)
    # dtype = 2
    htype = random.randint(0, len(basic) - 1)
    for bin in range(nbins):
        bname = "b" + str(bin)
        if dtype == 0:
            record[bname] = make_homogenous_data(htype)
        elif dtype == 1:
            record[bname] = make_basic_data()
        else:
            record[bname] = make_any_data(depth + 1)
    return record

# done
def doit():
    record = make_record(max_record, 0)
    print "record = %s" % str(record)
    for k,v in record.items():
        if type(v) == unicode:
            print "%s %s" % (k, v.encode('utf-8'))
        else:
            print "%s %s" % (k, str(v))

def countit():
    record = make_record(max_record, 0)
    len1 = len(str(record))
    print "  len1 = %s" % str(len1)
    if len1 < 0:
        print "  record = %s" % str(record)
        for k,v in record.items():
            if type(v) == unicode:
                print "  %s %s" % (k, v.encode('utf-8'))
            else:
                print "  %s %s" % (k, str(v))
    return len1

def main():
    # doit()
    t = 0
    c = 0
    for i in range(10000):
        print "i = %s" % str(i)
        l = countit()
        t += l
        c += 1
        a = t / c
        print "  average is %s" % str(a)


main()
