#!/usr/bin/env python3
#!/usr/bin/python

for x in range(256 * 256):
    u1 = chr(x)
    #  0x10ffff from 0 to 0x10ffff. Th
    # u1 = u"\ud83d" + unichr(x)    # smileys
    # u1 = unichr(x) + u"\uDC00"
    print(("%0.4X %s" % (x, u1.encode('utf-8'))))

for x1 in range(0xd800, 0xdc00):
    for x2 in range(0xdc00, 0xe000):
        u1 = chr(x1) + chr(x2)
        print(("%0.4X %0.4X %s" % (x1, x2, u1.encode('utf-8'))))
