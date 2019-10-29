#!/usr/bin/env python3
#!/usr/bin/python

str1 = 'test1'

if str1 == 'test1' or str1 == 'test2':
    print '1 or 2'
elif str1 == 'test3' or str1 == 'test4':
    print "3 or 4"
else:
    print "else"

str1 = ''
if str1:
    print "'%s' is True" % str1
else:
    print "'%s' is False" % str1

str1 = ' '
if str1:
    print "'%s' is True" % str1
else:
    print "'%s' is False" % str1
