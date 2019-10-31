#!/usr/bin/env python3

print("str = %s" % str(str))

print("str = %s" % str(dir(str)))

str1 = "bytes"
print("str1 = %s" % str1)
str2 = str1.encode()
print("str2 = %s" % str2)
str3 = str2.decode()
print("str3 = %s" % str3)

if str1 == str3:
    print("coverted ok")
else:
    print("FAIL did not covert ok")
    print("FAIL str1 = %s" % str1)
    print("FAIL str3 = %s" % str3)
