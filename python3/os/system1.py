#!/usr/bin/env python3

import os

print("os = %s" % str(os))
print("os = %s" % str(dir(os)))

os.system("which java")
os.system("uname -m")
fields = os.uname()
print("os.uname returns %s" % str(fields))
