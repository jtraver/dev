#!/usr/bin/env python3
#!/usr/bin/python

import re

str1 = 'ok'
re1 = re.search('OK', str1, re.IGNORECASE)
# re1 = re.search('OK', str1)
print(re1)
print(dir(re1))
print(re1.group(0))
