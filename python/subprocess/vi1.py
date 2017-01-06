#!/usr/bin/python

import subprocess
import os
import shutil

# not working!
# http://vi.stackexchange.com/questions/5989/is-it-possible-to-pipe-input-to-vim


# args = ('vi', '-s', "<(printf(ithis is a test\033:wq! test1.txt)", '-')
# vim +"1 | put! ='hello' | x" j
args = ('vi', "+\"1 | put! ='hello' | x\"", "test1.txt")
popen = subprocess.Popen( args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='.')
# out, err = popen.communicate(input = "ithis is a test\033:wq! test1.txt")
out, err = popen.communicate()
if err != None:
    print 'vi errput = %s' % str(err)

print "vi output = %s" % str(out)

subprocess.call(['echo', ''])
