#!/usr/bin/env python3
#!/usr/bin/python

import yaml
import random

tbg1 = yaml.load(file('../../../test/john/env/tbg/tbg1.yml'))
print "tbg1 = %s" % str(tbg1)
tbg2 = yaml.load(file('../../../test/john/env/tbg/tbg2.yml'))
print "tbg2 = %s" % str(tbg2)

world = {}
x = 0
y = 0
z = 0
while True:
    current = {}
    current['up'] = random.randint(0, 1)
    current['down'] = random.randint(0, 1)
    current['right'] = random.randint(0, 1)
    current['left'] = random.randint(0, 1)
    current['forward'] = random.randint(0, 1)
    current['back'] = random.randint(0, 1)
    ind1 = random.randint(0, len(tbg2) - 1)
    res1 = tbg2.keys()[ind1]
    print "looking at %s %s" % (res1, str(tbg2[res1]))
    if not len(tbg2[res1]):
        print "found %s %s" % (res1, str(tbg2[res1]))
    print "%s %s %s" % (str(x), str(y), str(z))
    command = raw_input('? ')
    if 'go' in command:
        if 'up' in command:
            if current['up']:
                z += 1
            else:
                print "can't go up"
        if 'down' in command:
            if current['down']:
                z -= 1
            else:
                print "can't go down"
        if 'right' in command:
            if current['right']:
                x += 1
            else:
                print "can't go right"
        if 'left' in command:
            if current['left']:
                x -= 1
            else:
                print "can't go left"
        if 'forward' in command:
            if current['forward']:
                y += 1
            else:
                print "can't go forward"
        if 'back' in command:
            if current['back']:
                y -= 1
            else:
                print "can't go back"
    else:
        print "what?"
