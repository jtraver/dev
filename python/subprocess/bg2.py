#!/usr/bin/python

import subprocess

subprocess.call("count1.plx > count1.out 2>&1 &", shell=True);
# subprocess.call("count1.plx");

# subprocess.call("/usr/bin/perl ./count1.plx > count1.out 2>&1 &");
# subprocess.call("/usr/bin/perl ./count1.plx > count1.out 2>&1 &");


subprocess.call(['echo', ''])
