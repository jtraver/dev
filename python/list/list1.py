#!/usr/bin/python

import apihelper

list1 = [ 0, 1, 2, 3, 5, 7 ]

print "list1 = %s" % str(list1)
print "list1 = %s" % str(dir(list1))
# list1 = ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
apihelper.info(list1)

list1.insert(2, 11)
print "list1 = %s" % str(list1)

index = 3
for item in [13, 17, 19]:
    list1.insert(index, item)
    index += 1
print "list1 = %s" % str(list1)
