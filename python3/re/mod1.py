#!/usr/bin/env python3
#!/usr/bin/python

import re
import apihelper



print "re = %s" % str(re)
print "re = %s" % dir(re)

# re = ['DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_alphanum', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_pattern_type', '_pickle', '_subx', 'compile', 'copy_reg', 'error', 'escape', 'findall', 'finditer', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']

# re = <module 're' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.pyc'>
# re = ['DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_alphanum', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copy_reg', 'error', 'escape', 'findall', 'finditer', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']

apihelper.info(re)
