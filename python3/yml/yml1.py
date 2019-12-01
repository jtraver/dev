#!/usr/bin/env python3
#!/usr/bin/python

import yaml

grid1 = yaml.load(file('grid1.yml'))
print("grid1 = %s" % str(grid1))

grid2 = yaml.load(file('grid2.yml'))
print("grid2 = %s" % str(grid2))

grid3 = yaml.load(file('grid3.yml'))
print("grid3 = %s" % str(grid3))

grid4 = yaml.load(file('grid4.yml'))
print("grid4 = %s" % str(grid4))
