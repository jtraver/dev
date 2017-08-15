#!/usr/bin/python

import sys
import inspect
import apihelper


# In [47]: c=inspect.currentframe() 
# 
# In [48]: c.f_lineno 
# Out[48]: 1 
# 
# In [49]: c.f_code.co_filename 

def func1():
    c=inspect.currentframe()
    print "%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)
    if False:
        print sys._getframe().f_code.co_name
        print "called from %s:%d" % inspect.stack()[1][1:3]
        print "line = %s" % str(c.f_lineno)
        print "file = %s" % str(c.f_code.co_filename)
        print "%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)


def func2():
    c=inspect.currentframe()
    print "%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)
    if False:
        print sys._getframe().f_code.co_name
        print "called from %s:%d" % inspect.stack()[1][1:3]
        print "line = %s" % str(c.f_lineno)
        print "file = %s" % str(c.f_code.co_filename)
        print "%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)


def func3():
    c=inspect.currentframe()
    print "%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)
    if False:
        print sys._getframe().f_code.co_name
        print "called from %s:%d" % inspect.stack()[1][1:3]
        print "line = %s" % str(c.f_lineno)
        print "file = %s" % str(c.f_code.co_filename)
        print "%s:%s:%d" % (c.f_code.co_filename, sys._getframe().f_code.co_name, c.f_lineno)

def main():
    func1()
    func2()
    func3()
    print " "
    print "str sys = %s" % str(sys)
    print "dir sys = %s" % str(dir(sys))
    print " "
    print "apihelper"
    apihelper.info(sys)
    print " "
    print "fields"
    print_sys_fields()

def print_sys_fields():
    print "sys.__displayhook__ = %s" % str(sys.__displayhook__)
    print "sys.__doc__ = %s" % str(sys.__doc__)
    print "sys.__egginsert = %s" % str(sys.__egginsert)
    print "sys.__excepthook__ = %s" % str(sys.__excepthook__)
    print "sys.__name__ = %s" % str(sys.__name__)
    print "sys.__package__ = %s" % str(sys.__package__)
    print "sys.__plen = %s" % str(sys.__plen)
    print "sys.__stderr__ = %s" % str(sys.__stderr__)
    print "sys.__stdin__ = %s" % str(sys.__stdin__)
    print "sys.__stdout__ = %s" % str(sys.__stdout__)
    print "sys._clear_type_cache = %s" % str(sys._clear_type_cache)
    print "sys._current_frames = %s" % str(sys._current_frames)
    print "sys._getframe = %s" % str(sys._getframe)
    print "sys._mercurial = %s" % str(sys._mercurial)
    print "sys.api_version = %s" % str(sys.api_version)
    print "sys.argv = %s" % str(sys.argv)
    print "sys.builtin_module_names = %s" % str(sys.builtin_module_names)
    print "sys.byteorder = %s" % str(sys.byteorder)
    print "sys.call_tracing = %s" % str(sys.call_tracing)
    print "sys.callstats = %s" % str(sys.callstats)
    print "sys.copyright = %s" % str(sys.copyright)
    print "sys.displayhook = %s" % str(sys.displayhook)
    print "sys.dont_write_bytecode = %s" % str(sys.dont_write_bytecode)
    print "sys.exc_clear = %s" % str(sys.exc_clear)
    print "sys.exc_info = %s" % str(sys.exc_info)
    print "sys.exc_type = %s" % str(sys.exc_type)
    print "sys.excepthook = %s" % str(sys.excepthook)
    print "sys.exec_prefix = %s" % str(sys.exec_prefix)
    print "sys.executable = %s" % str(sys.executable)
    print "sys.exit = %s" % str(sys.exit)
    print "sys.flags = %s" % str(sys.flags)
    print "sys.float_info = %s" % str(sys.float_info)
    print "sys.float_repr_style = %s" % str(sys.float_repr_style)
    print "sys.getcheckinterval = %s" % str(sys.getcheckinterval)
    print "sys.getdefaultencoding = %s" % str(sys.getdefaultencoding)
    print "sys.getdlopenflags = %s" % str(sys.getdlopenflags)
    print "sys.getfilesystemencoding = %s" % str(sys.getfilesystemencoding)
    print "sys.getprofile = %s" % str(sys.getprofile)
    print "sys.getrecursionlimit = %s" % str(sys.getrecursionlimit)
    print "sys.getrefcount = %s" % str(sys.getrefcount)
    print "sys.getsizeof = %s" % str(sys.getsizeof)
    print "sys.gettrace = %s" % str(sys.gettrace)
    print "sys.hexversion = %s" % str(sys.hexversion)
    print "sys.long_info = %s" % str(sys.long_info)
    print "sys.maxint = %s" % str(sys.maxint)
    print "sys.maxsize = %s" % str(sys.maxsize)
    print "sys.maxunicode = %s" % str(sys.maxunicode)
    print "sys.meta_path = %s" % str(sys.meta_path)
    print "sys.modules = %s" % str(sys.modules)
    print "sys.path = %s" % str(sys.path)
    print "sys.path_hooks = %s" % str(sys.path_hooks)
    print "sys.path_importer_cache = %s" % str(sys.path_importer_cache)
    print "sys.platform = %s" % str(sys.platform)
    print "sys.prefix = %s" % str(sys.prefix)
    print "sys.py3kwarning = %s" % str(sys.py3kwarning)
    print "sys.setcheckinterval = %s" % str(sys.setcheckinterval)
    print "sys.setdlopenflags = %s" % str(sys.setdlopenflags)
    print "sys.setprofile = %s" % str(sys.setprofile)
    print "sys.setrecursionlimit = %s" % str(sys.setrecursionlimit)
    print "sys.settrace = %s" % str(sys.settrace)
    print "sys.stderr = %s" % str(sys.stderr)
    print "sys.stdin = %s" % str(sys.stdin)
    print "sys.stdout = %s" % str(sys.stdout)
    print "sys.subversion = %s" % str(sys.subversion)
    print "sys.version = %s" % str(sys.version)
    print "sys.version_info = %s" % str(sys.version_info)
    print "sys.warnoptions = %s" % str(sys.warnoptions)

main()
