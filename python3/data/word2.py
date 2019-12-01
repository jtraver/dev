#!/usr/bin/env python3
#!/usr/bin/python

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for v in vowels:
    for c in consonants:
        print(("%s%s" % (str(v), str(c))))
        print(("%s%s" % (str(c), str(v))))

for v1 in vowels:
    for v2 in vowels:
        print(("%s%s" % (str(v1), str(v2))))
