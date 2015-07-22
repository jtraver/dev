#!/usr/bin/python

import os
import subprocess

os.system("./count1.plx > count1.out 2>&1 &")
# os.system("tail -f count.out &");
# os.system("./count1.plx");


subprocess.call(['echo', ''])
