#!/usr/bin/python

file1 = open('file1.py', 'r')
print "file1 is %s" % str(type(file1))
print "file1 is %s" % str(dir(file1))
data = file1.read()
file1.close()
print "data is %s" % str(type(data))
print data

file1 = open('file2.txt', 'w')
file1.write('hello\n')
file1.write('world\n')
file1.close()


file1 = open('file1.py', 'r')
for line in file1.xreadlines():
# for line in file1.readlines():
    line = line.rstrip()
    print "%s" % line
