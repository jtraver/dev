#!/usr/bin/env python

spheres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def main():
    # twos()
    # threes()
    # fours()
    # fives()
    # sixes()
    # sevens()
    eights()

def twos():
    d1 = {}
    for v1 in spheres:
        for v2 in spheres:
            if v1 == v2:
                continue
            l1 = [v1, v2]
            s1 = sorted(l1)
            t1 = (s1[0], s1[1])
            if t1 in d1:
                d1[t1] += 1
            else:
                d1[t1] = 1
    for k in sorted(d1.keys()):
        v = d1[k]
        print "%s = %s" % (str(k), str(v))
    len1 = len(d1.keys())
    print "%s" % str(len1)

def threes():
    d1 = {}
    for v1 in spheres:
        for v2 in spheres:
            if v1 == v2:
                continue
            for v3 in spheres:
                if v1 == v3 or v2 == v3:
                    continue
                l1 = [v1, v2, v3]
                s1 = sorted(l1)
                t1 = (s1[0], s1[1], s1[2])
                if t1 in d1:
                    d1[t1] += 1
                else:
                    d1[t1] = 1
    for k in sorted(d1.keys()):
        v = d1[k]
        print "%s = %s" % (str(k), str(v))
    len1 = len(d1.keys())
    print "%s" % str(len1)

def fours():
    d1 = {}
    for v1 in spheres:
        for v2 in spheres:
            if v1 == v2:
                continue
            for v3 in spheres:
                if v1 == v3 or v2 == v3:
                    continue
                for v4 in spheres:
                    if v1 == v4 or v2 == v4 or v3 == v4:
                        continue
                    l1 = [v1, v2, v3, v4]
                    s1 = sorted(l1)
                    t1 = (s1[0], s1[1], s1[2], s1[3])
                    if t1 in d1:
                        d1[t1] += 1
                    else:
                        d1[t1] = 1
    for k in sorted(d1.keys()):
        v = d1[k]
        print "%s = %s" % (str(k), str(v))
    len1 = len(d1.keys())
    print "%s" % str(len1)

def fives():
    d1 = {}
    for v1 in spheres:
        for v2 in spheres:
            if v1 == v2:
                continue
            for v3 in spheres:
                if v1 == v3 or v2 == v3:
                    continue
                for v4 in spheres:
                    if v1 == v4 or v2 == v4 or v3 == v4:
                        continue
                    for v5 in spheres:
                        if v1 == v5 or v2 == v5 or v3 == v5 or v4 == v5:
                            continue
                        l1 = [v1, v2, v3, v4, v5]
                        s1 = sorted(l1)
                        t1 = (s1[0], s1[1], s1[2], s1[3], s1[4])
                        if t1 in d1:
                            d1[t1] += 1
                        else:
                            d1[t1] = 1
    for k in sorted(d1.keys()):
        v = d1[k]
        print "%s = %s" % (str(k), str(v))
    len1 = len(d1.keys())
    print "%s" % str(len1)

def sixes():
    d1 = {}
    for v1 in spheres:
        for v2 in spheres:
            if v1 == v2:
                continue
            for v3 in spheres:
                if v1 == v3 or v2 == v3:
                    continue
                for v4 in spheres:
                    if v1 == v4 or v2 == v4 or v3 == v4:
                        continue
                    for v5 in spheres:
                        if v1 == v5 or v2 == v5 or v3 == v5 or v4 == v5:
                            continue
                        for v6 in spheres:
                            if v1 == v6 or v2 == v6 or v3 == v6 or v4 == v6 or v5 == v6:
                                continue
                            l1 = [v1, v2, v3, v4, v5, v6]
                            s1 = sorted(l1)
                            t1 = (s1[0], s1[1], s1[2], s1[3], s1[4], s1[5])
                            if t1 in d1:
                                d1[t1] += 1
                            else:
                                d1[t1] = 1
    for k in sorted(d1.keys()):
        v = d1[k]
        print "%s = %s" % (str(k), str(v))
    len1 = len(d1.keys())
    print "%s" % str(len1)

def sevens():
    d1 = {}
    for v1 in spheres:
        for v2 in spheres:
            if v1 == v2:
                continue
            for v3 in spheres:
                if v1 == v3 or v2 == v3:
                    continue
                for v4 in spheres:
                    if v1 == v4 or v2 == v4 or v3 == v4:
                        continue
                    for v5 in spheres:
                        if v1 == v5 or v2 == v5 or v3 == v5 or v4 == v5:
                            continue
                        for v6 in spheres:
                            if v1 == v6 or v2 == v6 or v3 == v6 or v4 == v6 or v5 == v6:
                                continue
                            for v7 in spheres:
                                if v1 == v7 or v2 == v7 or v3 == v7 or v4 == v7 or v5 == v7 or v6 == v7:
                                    continue
                                l1 = [v1, v2, v3, v4, v5, v6, v7]
                                s1 = sorted(l1)
                                t1 = (s1[0], s1[1], s1[2], s1[3], s1[4], s1[5], s1[6])
                                if t1 in d1:
                                    d1[t1] += 1
                                else:
                                    d1[t1] = 1
    for k in sorted(d1.keys()):
        v = d1[k]
        print "%s = %s" % (str(k), str(v))
    len1 = len(d1.keys())
    print "%s" % str(len1)

def eights():
    d1 = {}
    for v1 in spheres:
        for v2 in spheres:
            if v1 == v2:
                continue
            for v3 in spheres:
                if v1 == v3 or v2 == v3:
                    continue
                for v4 in spheres:
                    if v1 == v4 or v2 == v4 or v3 == v4:
                        continue
                    for v5 in spheres:
                        if v1 == v5 or v2 == v5 or v3 == v5 or v4 == v5:
                            continue
                        for v6 in spheres:
                            if v1 == v6 or v2 == v6 or v3 == v6 or v4 == v6 or v5 == v6:
                                continue
                            for v7 in spheres:
                                if v1 == v7 or v2 == v7 or v3 == v7 or v4 == v7 or v5 == v7 or v6 == v7:
                                    continue
                                for v8 in spheres:
                                    if v1 == v8 or v2 == v8 or v3 == v8 or v4 == v8 or v5 == v8 or v6 == v8 or v7 == v8:
                                        continue
                                    l1 = [v1, v2, v3, v4, v5, v6, v7, v8]
                                    #if check_ms(l1):
                                    #    print "FAIL %s %s %s %s %s %s %s %s" % (v1, v2, v3, v4, v5, v6, v7, v8)
                                    #    continue
                                    sl1 = sorted(l1)
                                    l2 = []
                                    for e1 in sl1:
                                        l2.append(e1)
                                    s1 = sorted(l2)
                                    t1 = (s1[0], s1[1], s1[2], s1[3], s1[4], s1[5], s1[6], s1[7])
                                    if t1 in d1:
                                        d1[t1] += 1
                                    else:
                                        d1[t1] = 1
    for k in sorted(d1.keys()):
        v = d1[k]
        print "%s = %s" % (str(k), str(v))
    len1 = len(d1.keys())
    print "%s" % str(len1)

def check_ms(l1):
    res1 = False
    len1 = len(l1)
    for x1 in xrange(len1):
        v1 = l1[x1]
        for x2 in xrange(len1):
            if x1 == x2:
                continue
            v2 = l1[x2]
            if v1 == v2:
                res1 = True
                print "FAIL: %s %s = %s" % (str(x1), str(x2), v1)
    return res1

main()
