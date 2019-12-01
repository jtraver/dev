#!/usr/bin/env python3
#!/usr/bin/python

import subprocess
import os
import shutil

args = ('stdin1.py')
popen = subprocess.Popen( args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='.')
popen.stdin.write("this is line 0\n")
out, err = popen.communicate(input = "this is line 1\nthis is line 2\n\d")
if err != None:
    print('errput = %s' % str(err))

print("output = %s" % str(out))

subprocess.call(['echo', ''])
