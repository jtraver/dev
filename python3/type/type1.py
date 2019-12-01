#!/usr/bin/env python3
#!/usr/bin/python

help(help)

test1 = None
help(test1)
if test1:
    print(str(test1) + " is True")
else:
    print(str(test1) + " is False")
print("test1 = %s" % str(test1))
print("test1 = %s" % dir(test1))
print("test1 = %s" % dir(test1.__class__))
# ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
test1.__class__
help(test1.__class__)
print("class " + str(test1.__class__))
# test1.__class__()
print("delattr " + str(test1.__delattr__))
# test1.__delattr__()
help(test1.__delattr__)
print("doc " + str(test1.__doc__))
# test1.__doc__()
help(test1.__doc__)

print("format " + str(test1.__format__))
# print "format " + dir(test1.__format__)
# print "format " + help(test1.__format__)
help(test1.__format__)
# test1.__format__()

print("getattribute " + str(test1.__getattribute__))
# print "getattribute " + dir(test1.__getattribute__)
# print "getattribute " + help(test1.__getattribute__)
help(test1.__getattribute__)
# test1.__getattribute__()

test1 = 0
if test1:
    print(str(test1) + " is True")
else:
    print(str(test1) + " is False")

test1 = ''
if test1:
    print(str(test1) + " is True")
else:
    print(str(test1) + " is False")
if type(test1) is str:
    print(str(test1) + " is String")
else:
    print(str(test1) + " is not String")
if type(test1) is not str:
    print(str(test1) + " is not String")
else:
    print(str(test1) + " is String")

test1 = []
type1 = str(type(test1))
print("test1 type is %s" % type1)
if type(test1) == list:
    print("test1 type is list")
