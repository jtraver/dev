#!/usr/bin/python

# ['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
set1 = set(['item1'])
print "set1 = %s" % str(type(set1))
print "set1 = %s" % dir(set1)
print "set1 = %s" % str(set1)
set1 |= set(['item2'])
print "set1 = %s" % str(set1)
set1 &= set(['item1'])
print "set1 = %s" % str(set1)

set0 = set()
print "set0 = %s" % str(set0)
set0.add('item1')
print "set0 = %s" % str(set0)

list1 = ['a', 'b', 'c', 'b', 'a']
print "list1 = %s" % str(list1)
set1 = set(list1)
print "set1 = %s" % str(set1)
for n in set1:
    print "  n = %s" % str(n)
print "sorted set"
for n in sorted(set1):
    print "  n = %s" % str(n)
