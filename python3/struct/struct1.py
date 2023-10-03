#!/usr/bin/env python3
#!/usr/bin/python

import struct

# 
# A basic example of packing/unpacking three integers:
# 
# >>>
# >>> from struct import *
# >>> pack('hhl', 1, 2, 3)
# '\x00\x01\x00\x02\x00\x00\x00\x03'
# >>> unpack('hhl', '\x00\x01\x00\x02\x00\x00\x00\x03')
# (1, 2, 3)
# >>> calcsize('hhl')
# 8
# Unpacked fields can be named by assigning them to variables or by wrapping the result in a named tuple:
# 
# >>>
# >>> record = 'raymond   \x32\x12\x08\x01\x08'
# >>> name, serialnum, school, gradelevel = unpack('<10sHHb', record)
# 
# >>> from collections import namedtuple
# >>> Student = namedtuple('Student', 'name serialnum school gradelevel')
# >>> Student._make(unpack('<10sHHb', record))
# Student(name='raymond   ', serialnum=4658, school=264, gradelevel=8)
# The ordering of format characters may have an impact on size since the padding needed to satisfy alignment requirements is different:
# 
# >>>
# >>> pack('ci', '*', 0x12131415)
# '*\x00\x00\x00\x12\x13\x14\x15'
# >>> pack('ic', 0x12131415, '*')
# '\x12\x13\x14\x15*'
# >>> calcsize('ci')
# 8
# >>> calcsize('ic')
# 5
# The following format 'llh0l' specifies two pad bytes at the end, assuming longs are aligned on 4-byte boundaries:
# 
# >>>
# >>> pack('llh0l', 1, 2, 3)
# '\x00\x00\x00\x01\x00\x00\x00\x02\x00\x03\x00\x00'
# This only works when native siz
#

p1 = struct.pack('hhl', 1, 2, 3)
# print "p1 = %s" % str(p1)
u1 = struct.unpack('hhl', p1)
print("u1 = %s" % str(u1))
s1 = struct.calcsize('hhl')
print("s1 = %s" % str(s1))


def do_pack(fmt, *args):
    print()
    print("---------------------------------------------------------------------------------")
    print("fmt = %s" % str(fmt))
    print("args = %s" % str(args))
    p1 = struct.pack(fmt, *args)
    # print "p1 = %s" % str(p1)
    u1 = struct.unpack(fmt, p1)
    print("u1 = %s" % str(u1))
    s1 = struct.calcsize(fmt)
    print("s1 = %s" % str(s1))
    if u1 == args:
        print("equal")
    else:
        print("not equal")
    v1 = u1[0]
    print("v1 = %s" % str(v1))
    print("v1 = %s" % str(type(v1)))
    return v1


do_pack('! B', 4)
do_pack('! B 2x B x B I 8x H H', 5, 6, 7, 8, 9, 10)
do_pack('! I B', 11, 12)
do_pack('! I B B B', 13, 14, 15, 16)
do_pack('! I B B B B', 17, 18, 19, 20, 21)
do_pack('! I B B p', 22, 23, 24, b'string25')
do_pack('! Q', 26)
do_pack('! Q B 4x B I 8x H H', 27, 28, 29, 30, 31, 32)
do_pack('! Q B B B B 12x', 35, 36, 37, 38, 39)
do_pack('! Q B B B B B B I I I H H', 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52)
do_pack('! Q B B H I I H H', 53, 54, 55, 56, 57, 58, 59, 60)
do_pack('! x B x B 12x', 61, 62)
do_pack('!H', 65)
do_pack('!I', 66)
do_pack('!L', 67)
do_pack('!Q', 68)
do_pack('4sl', b'st69', 8)
do_pack('=2Q', 70, 77)
do_pack('=3Q', 71, 78, 79)
do_pack('>II', 72, 80)
do_pack('>i', 73)
do_pack('>q', 74)
do_pack('I', 75)

v1 = do_pack('! Q', 0xFFFFFFFFFFFF)
if v1 == 0xFFFFFFFFFFFF:
    print("v1 is correct")
else:
    print("v1 is not correct")

v2 = 0xFFFFFFFF
v1 = do_pack('! Q', v2)
if v1 == v2:
    print("v1 is correct")
else:
    print("v1 is not correct")

v2 = 0x8FFFFFFF
v1 = do_pack('! Q', v2)
if v1 == v2:
    print("v1 is correct")
else:
    print("v1 is not correct")

v2 = 66389026883887
print("v2 = %s" % str(v2))
print("v2 = 0x%x" % v2)
print("v2 = %s" % str(type(v2)))
v1 = do_pack('! Q', v2)
if v1 == v2:
    print("v1 is correct")
else:
    print("v1 is not correct")



STRUCT_PROTO = struct.Struct('! Q')
STRUCT_UINT8 = struct.Struct('! B')
STRUCT_UINT16 = struct.Struct('! H') 
STRUCT_UINT32 = struct.Struct('! I') 
STRUCT_UINT64 = struct.Struct('! Q')
STRUCT_INT8 = struct.Struct('! b')
STRUCT_INT16 = struct.Struct('! h') 
STRUCT_INT32 = struct.Struct('! i')
STRUCT_INT64 = struct.Struct('! q')
STRUCT_FLOAT = struct.Struct('! f')
STRUCT_DOUBLE = struct.Struct('! d')
STRUCT_HEADER = struct.Struct('! Q B B B B B B I I I H H')
STRUCT_OP = struct.Struct("! I B B B B")
STRUCT_FIELD = struct.Struct("! I B")
STRUCT_STRING_FMT = "! %ds"

# float 1.1
v2 = 1.1        # floats are doubles in python -> this will lose precision since only 4 bytes are used
# v1 = do_pack(STRUCT_FLOAT, v2)
v1 = do_pack('! f', v2)
print("v1 = %s" % str(v1))
# print("v1 = 0x%x" % v1)
print("v1 = %s" % str(type(v1)))
print("v2 = %s" % str(v2))
# print("v2 = 0x%x" % v2)
print("v2 = %s" % str(type(v2)))
if v1 == v2:
    print("v1 is correct")
else:
    print("v1 is not correct")
if str(v1) == str(v2):
    print("v1 is correct")
else:
    print("v1 is not correct")
ba1 = bytearray(struct.pack("f", v1))
print([ "0x%02x" % b for b in ba1 ])
ba2 = bytearray(struct.pack("f", v2))
print([ "0x%02x" % b for b in ba2 ])
len1 = len(ba1)
len2 = len(ba2)
if len1 == len2:
    print("lengths are the same")
else:
    print("lengths are not the same")
    print("len1 = %s" % str(len1))
    print("len2 = %s" % str(len2))
if ba1 == ba2:
    print("byte arrays are the same")
else:
    print("byte arrays are not the same")
    print("ba1 = %s" % str(ba1))
    print("ba2 = %s" % str(ba2))

# double 1.1
v2 = 1.1
# STRUCT_DOUBLE = struct.Struct('! d')
v1 = do_pack('! d', v2)
print("v1 = %s" % str(v1))
# print("v1 = 0x%x" % v1)
print("v1 = %s" % str(type(v1)))
print("v2 = %s" % str(v2))
# print("v2 = 0x%x" % v2)
print("v2 = %s" % str(type(v2)))
if v1 == v2:
    print("v1 is correct")
else:
    print("v1 is not correct")
if str(v1) == str(v2):
    print("v1 is correct")
else:
    print("v1 is not correct")
ba1 = bytearray(struct.pack("d", v1))
print([ "0x%02x" % b for b in ba1 ])
ba2 = bytearray(struct.pack("d", v2))
print([ "0x%02x" % b for b in ba2 ])
len1 = len(ba1)
len2 = len(ba2)
if len1 == len2:
    print("lengths are the same")
else:
    print("lengths are not the same")
    print("len1 = %s" % str(len1))
    print("len2 = %s" % str(len2))
if ba1 == ba2:
    print("byte arrays are the same")
else:
    print("byte arrays are not the same")
    print("ba1 = %s" % str(ba1))
    print("ba2 = %s" % str(ba2))

# double 3.2999
v2 = 3.2999
# STRUCT_DOUBLE = struct.Struct('! d')
v1 = do_pack('! d', v2)
print("v1 = %s" % str(v1))
# print("v1 = 0x%x" % v1)
print("v1 = %s" % str(type(v1)))
print("v2 = %s" % str(v2))
# print("v2 = 0x%x" % v2)
print("v2 = %s" % str(type(v2)))
if v1 == v2:
    print("v1 is correct")
else:
    print("v1 is not correct")
if str(v1) == str(v2):
    print("v1 is correct")
else:
    print("v1 is not correct")
ba1 = bytearray(struct.pack("d", v1))
print([ "0x%02x" % b for b in ba1 ])
ba2 = bytearray(struct.pack("d", v2))
print([ "0x%02x" % b for b in ba2 ])
len1 = len(ba1)
len2 = len(ba2)
if len1 == len2:
    print("lengths are the same")
else:
    print("lengths are not the same")
    print("len1 = %s" % str(len1))
    print("len2 = %s" % str(len2))
if ba1 == ba2:
    print("byte arrays are the same")
else:
    print("byte arrays are not the same")
    print("ba1 = %s" % str(ba1))
    print("ba2 = %s" % str(ba2))

# double 3.3001
v2 = 3.3001
# STRUCT_DOUBLE = struct.Struct('! d')
v1 = do_pack('! d', v2)
print("v1 = %s" % str(v1))
# print("v1 = 0x%x" % v1)
print("v1 = %s" % str(type(v1)))
print("v2 = %s" % str(v2))
# print("v2 = 0x%x" % v2)
print("v2 = %s" % str(type(v2)))
if v1 == v2:
    print("v1 is correct")
else:
    print("v1 is not correct")
if str(v1) == str(v2):
    print("v1 is correct")
else:
    print("v1 is not correct")
ba1 = bytearray(struct.pack("d", v1))
print([ "0x%02x" % b for b in ba1 ])
ba2 = bytearray(struct.pack("d", v2))
print([ "0x%02x" % b for b in ba2 ])
len1 = len(ba1)
len2 = len(ba2)
if len1 == len2:
    print("lengths are the same")
else:
    print("lengths are not the same")
    print("len1 = %s" % str(len1))
    print("len2 = %s" % str(len2))
if ba1 == ba2:
    print("byte arrays are the same")
else:
    print("byte arrays are not the same")
    print("ba1 = %s" % str(ba1))
    print("ba2 = %s" % str(ba2))
