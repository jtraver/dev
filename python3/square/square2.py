#!/usr/bin/env python3
#!/usr/bin/env python

LIMIT = 32

dict1 = {}

def main():
    squares()
    a1 = 0
    while a1 < LIMIT:
        sums(a1)
        a1 += 1
    results()

def squares():
    global dict1
    for i1 in range(1, LIMIT * 2):
        # print "%s" % str(i1)
        s1 = i1 * i1
        if not s1 in dict1:
            dict1[s1] = []
            dict1[s1].append(i1)

def results():
    r1 = sorted(dict1.keys())
    for k1 in r1:
        v1 = dict1[k1]
        print("%s %s" % (str(k1), str(sorted(v1))))
    print("\nnot found")
    l1 = len(r1)
    lim1 = r1[l1 - 1]
    for x1 in range(lim1):
        if not x1 in r1:
            print("%s not found" % str(x1))

def sums(l0):
    global dict1
    ret1 = False
    for k1 in sorted(dict1.keys()):
        v1 = dict1[k1]
        for i1 in range(1, l0):
            s1 = i1 * i1
            t1 = s1 + k1
            if not t1 in dict1 and not i1 in v1:
                ret1 = True
                dict1[t1] = []
                dict1[t1].append(i1)
                for p1 in v1:
                    dict1[t1].append(p1)
    return ret1

main()
print("")
