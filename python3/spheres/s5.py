#!/usr/bin/env python3
#!/usr/bin/env python

spheres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def main():
    # twos()
    # threes()
    # fours()
    fives()

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
        print("%s = %s" % (str(k), str(v)))
    len1 = len(list(d1.keys()))
    print("%s" % str(len1))

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
        print("%s = %s" % (str(k), str(v)))
    len1 = len(list(d1.keys()))
    print("%s" % str(len1))

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
        print("%s = %s" % (str(k), str(v)))
    len1 = len(list(d1.keys()))
    print("%s" % str(len1))

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
        print("%s = %s" % (str(k), str(v)))
    len1 = len(list(d1.keys()))
    print("%s" % str(len1))

main()
