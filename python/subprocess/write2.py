#!/usr/bin/python

import subprocess
import os
import shutil
import pty

master, slave = pty.openpty()
args = ('stdin1.py')
# popen = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='.')
# http://stackoverflow.com/questions/5411780/python-run-a-daemon-sub-process-read-stdout/5413588#5413588
# not working
popen = subprocess.Popen(args, shell=True, stdin=subprocess.PIPE, stdout=slave, stderr=slave, close_fds=True, cwd='.')
stdout = os.fdopen(master)

# set the O_NONBLOCK flag of p.stdout file descriptor:
# flags = fcntl(popen1.stdout, F_GETFL) # get current popen1.stdout flags
# fcntl(popen1.stdout, F_SETFL, flags | O_NONBLOCK)

popen.stdin.write("this is line 0\n")
# line = popen.stdout.readline()
# line = stdout.readline()
# print "line = %s" % line
out, err = popen.communicate(input = "this is line 1\nthis is line 2\n\d")
if err != None:
    print 'errput = %s' % str(err)

print "output = %s" % str(out)
out2 = stdout.read()
print "output = %s" % str(out)

subprocess.call(['echo', ''])
