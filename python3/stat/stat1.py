#!/usr/bin/env python3
#!/usr/bin/python

import os

stat1 = os.stat('stat1.py')
print("stat1 = %s" % str(stat1))

size1 = stat1.st_size
print("size1 = %s" % str(size1))
