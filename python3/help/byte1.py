#!/usr/bin/env python3
#!/usr/bin/python

import apihelper

print("\n---------------------------------------------------------------------------------")
print("BYTE")
byte1 = b'b'
apihelper.info(byte1)

print("\n---------------------------------------------------------------------------------")
print("BYTES")
byte2 = bytes()
apihelper.info(byte2)

print("\n---------------------------------------------------------------------------------")
print("bytearray")
ba1 = bytearray(b"abc")
msg = "ba1"
for ind1 in range(len(ba1)):
    ba1[ind1] = ind1
for ind1 in range(len(ba1)):
    c1 = ba1[ind1]
    i1 = c1
    if isinstance(c1, bytes):
        i1 =  int.from_bytes(c1, byteorder='big')
    print("1 %s %s %s BYTE = 0x%x %d '%c'" % (msg, str(type(c1)), str(ind1), i1, i1, i1))

print("\n---------------------------------------------------------------------------------")
print("bytes")
ba1 = bytes("bytes", 'utf-8')   # immutable
# ba1.append(0xc7)
# ba1.append(0xd4)
msg = "ba1"
#for ind1 in range(len(ba1)):
#    ba1[ind1] = ind1
for ind1 in range(len(ba1)):
    c1 = ba1[ind1]
    i1 = c1
    if isinstance(c1, bytes):
        i1 =  int.from_bytes(c1, byteorder='big')
    print("1 %s %s %s BYTE = 0x%x %d '%c'" % (msg, str(type(c1)), str(ind1), i1, i1, i1))

