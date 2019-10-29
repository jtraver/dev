#!/usr/bin/env python3
#!/usr/bin/env python

spheres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def main():
    twos()

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

main()
