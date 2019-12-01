#!/usr/bin/env python3
#!/usr/bin/python

import subprocess

args = ('ls', '-lat')
popen = subprocess.Popen(
    args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='.')

print("popen = %s" % str(popen))
print("popen = %s" % dir(popen))

out, err = popen.communicate()

print("out = %s" % str(out))
print("out = %s" % dir(out))
print("err = %s" % str(err))
print("err = %s" % dir(err))

lines = out.splitlines()
for line in lines:
    print(line)

subprocess.call(['echo', ''])
