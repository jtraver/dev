#!/usr/bin/env python3

# http://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string

import re

line = "this is the string to search"

# regex = re.compile(r'^.*Run \'(?P<filename>[^\']+?)\'.*$')
regex = re.compile(r'e.s')
regex = re.compile(r'e s')
regex = re.compile(r'e[ ]+s')
# regex = re.compile(r'ejunk[ ]+s')

#parts = <re.Match object; span=(10, 13), match='e s'>
#parts = ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']
#parts = {}


# parts = regex.match(line)
parts = regex.search(line)

print("parts = %s" % str(parts))
if parts:
    print("parts = %s" % str(parts))
    print("parts = %s" % str(dir(parts)))

    # print("match = %s" % str(parts.match()))
    # print("match = %s" % str(parts["match"]))

    # parts = parts.groupdict()

    print("groupdict = %s" % str(parts.groupdict()))
    print("group = %s" % str(parts.group()))
    print("groups = %s" % str(parts.groups()))
    print("span = %s" % str(parts.span()))
    print("string = %s" % str(parts.string))


    # print("parts = %s" % str(parts))
    # filename = parts['filename']
    # print("filename = %s" % str(filename))
