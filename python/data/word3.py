#!/usr/bin/python

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for v1 in vowels:
    for c in consonants:
        print "%s%s" % (str(v), str(c))
        print "%s%s" % (str(c), str(v))
