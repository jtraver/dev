#!/usr/bin/python

import subprocess
import os
import shutil



if os.path.exists('envars.prop'):
    shutil.copy2('envars.prop', "work.current")
args = ('tar', '-czvf', 'work.tgz', ".")
popen = subprocess.Popen(
    args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='.', shell=True)
out, err = popen.communicate()
if err != None:
    print 'tar errput = %s' % str(err)


subprocess.call(['echo', ''])
