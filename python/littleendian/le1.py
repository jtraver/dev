#!/usr/bin/python

# 61196 versus 3311

def get_le16(int16):
    le1 = (int16 << 8) & 0xffff
    le1 |= int16 >> 8
    return le1

int0 = 3311
print "int0 %x" % int0
print "int0 %d" % int0

int1 = int("cef", 16)
print "int1 %x" % int1
print "int1 %d" % int1

int2 = int("fec", 16)
print "int2 %x" % int2
print "int2 %d" % int2

int3 = int("ef0c", 16)
print "int3 %x" % int3
print "int3 %d" % int3

int4 = 61196 - 61196
print "int4 %x" % int4
print "int4 %d" % int4

int5 = get_le16(int0)
print "int5 %x" % int5
print "int5 %d" % int5

if int3 == int5:
    print "%s swapped is %s" % (str(int0), str(int5))
else:
    print "FAIL %s swapped is not %s" % (str(int0), str(int5))

print " "
# 9477 versus 1317

int0 = 1317
print "%x" % int0
print "%d" % int0

int1 = int("525", 16)
print "%x" % int1
print "%d" % int1

int2 = int("2505", 16)
print "%x" % int2
print "%d" % int2

int3 = int("2505", 16)
print "%x" % int3
print "%d" % int3

int4 = 9477 - 9477
print "%x" % int4
print "%d" % int4
