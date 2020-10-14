#!/usr/bin/env python3

# https://docs.python.org/3/library/modulefinder.html

from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('graph1.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))

print('-'*50)
print('Modules not imported:')
print('\n'.join(finder.badmodules.keys()))
