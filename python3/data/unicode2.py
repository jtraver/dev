#!/usr/bin/env python3
#!/usr/bin/python

import sys
import yaml


def test1():
    r1 = {
        'a': chr(135).encode('utf-8')
    }
    sr1 = str(r1)
    r2 = yaml.load(sr1)
    sr2 = str(r2)
    r3 = yaml.load(sr2)
    if r3 != r2:
        print(("%s %s" % (str(r3), str(r2))))
        sys.exit(1)


def test2():
    for x1 in range(0x10000):
        for x2 in range(0x10000):
            # u1 = unichr(x1)
            # u1 = unichr(0xFFFF) + unichr(x1)
            # u1 = unichr(0xFFFE) + unichr(x1)
            # u1 = unichr(0xFFFB) + unichr(x1)
            # u1 = unichr(0xFFFA) + unichr(x1)
            # u1 = unichr(0xFFF9) + unichr(x1)
            # u1 = unichr(0xFEFF) + unichr(x1)
            u1 = chr(x1) + chr(x2)
            # print "%0.4X %s" % (x1, u1.encode('utf-8'))
            # print "%0.4X %s" % (x1, u1)
            s1 = str(u1.encode('utf-8'))
            r1 = {'b': s1}
            sr1 = str(r1)
            r2 = yaml.load(sr1)
            if r1 != r2:
                print(("%0.4X %0.4X %s %s %s" % (x1, x2, u1.encode('utf-8'), str(r1), str(r2))))
                sys.exit(1)


def test3():
    # for x1 in range(0x1010000):
    for x1 in range(0x10000):
        u1 = chr(x1)
        print(("%0.4X %s" % (x1, u1.encode('utf-8'))))


def main():
    test3()

main()
