#!/usr/bin/env python3
#!/usr/bin/python

import yaml

atbg1 = {
    'love': {'truth': [ 'wise' ], 'beauty': [], 'goodness': []},
    'truth': [],
    'beauty': [],
    'goodness': [],
}


dtbg1 = {
    'love': {'truth': [ 'wise' ], 'beauty': [], 'goodness': []},
}


tbg1 = {
    'love': ['truth', 'beauty', 'goodness'],
    'truth': None,
    'beauty': None,
    'goodness': None,
}

with open('tbg1.yml', 'w') as outfile:
    outfile.write(yaml.dump(tbg1, default_flow_style=False))

tbg2 = yaml.load(file('tbg1.yml'), Loader=yaml.FullLoader)
print "tbg2 = %s" % str(tbg2)

if tbg1 == tbg2:
    print "load and dump worked"
else:
    print "load and dump did not work"
