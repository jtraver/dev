#!/usr/bin/env python3
#!/usr/bin/python

import sys
import inspect

print(("sys = %s" % str(sys)))
print(("sys = %s" % str(dir(sys))))
print(("sys.platform = %s" % str(sys.platform)))

# In [47]: c=inspect.currentframe() 
# 
# In [48]: c.f_lineno 
# Out[48]: 1 
# 
# In [49]: c.f_code.co_filename 

def func1():
    c=inspect.currentframe()
    print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    if False:
        print((sys._getframe().f_code.co_name))
        print(("called from %s:%d" % inspect.stack()[1][1:3]))
        print(("line = %s" % str(c.f_lineno)))
        print(("file = %s" % str(c.f_code.co_filename)))
        print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))


def func2():
    c=inspect.currentframe()
    print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    if False:
        print((sys._getframe().f_code.co_name))
        print(("called from %s:%d" % inspect.stack()[1][1:3]))
        print(("line = %s" % str(c.f_lineno)))
        print(("file = %s" % str(c.f_code.co_filename)))
        print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))


def func3():
    c=inspect.currentframe()
    print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))
    if False:
        print((sys._getframe().f_code.co_name))
        print(("called from %s:%d" % inspect.stack()[1][1:3]))
        print(("line = %s" % str(c.f_lineno)))
        print(("file = %s" % str(c.f_code.co_filename)))
        print(("%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)))


def main():
    func1()
    func2()
    func3()


main()
