#!/usr/bin/env python3
#!/usr/bin/python3

def reciprocal(n):
    return 1.0 / n

def main():
    v = 1
    t = 1
    l = t
    for n in xrange(100):
        r = reciprocal(t)
        t = v + r
        if l == t:
            break
        print "t = %s" % str(t)
        l = t

main()
