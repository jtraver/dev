#!/usr/bin/python

import shutil

try:
    shutil.rmtree('tmp')
except Exception as e:
    pass
