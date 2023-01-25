#!/usr/bin/env python3

file1 = open('file1.py', 'r')
print(("file1 is %s" % str(type(file1))))
print(("file1 is %s" % str(dir(file1))))
data = file1.read()
file1.close()
print(("data is %s" % str(type(data))))
print(data)

file1 = open('file2.txt', 'w')
file1.write('hello\n')
file1.write('world\n')
file1.close()


file1 = open('file1.py', 'r')
print(("file1 = %s" % str(file1)))
print(("file1 = %s" % str(type(file1))))
print(("file1 = %s" % str(dir(file1))))
for line in file1:
# for line in file1.readlines():
    line = line.rstrip()
    print(("%s" % line))
file1.close()

# file1 = <open file 'file1.py', mode 'r' at 0x10e426660>
# file1 = <type 'file'>
# file1 = ['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
