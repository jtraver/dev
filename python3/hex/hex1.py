#!/usr/bin/env python3
#!/usr/bin/python

def main():
    hex1()

def hex1():
    # ba1 = bytearray.fromhex("0x69")
    ba1 = bytearray.fromhex("69")
    print(("ba1 = %s" % str(ba1)))

main()

# asclient.connection.recv 1037 BYTE = 0x21 33 '!'
# asclient.connection.recv 1038 BYTE = 0x69 105 'i'
# asclient.connection.recv 1039 BYTE = 0x6f 111 'o'
# asclient.connection.recv 1040 BYTE = 0x34 52 '4'
# asclient.connection.recv 1041 BYTE = 0x54 84 'T'
# asclient.connection.recv 1042 BYTE = 0xcf 207 '?'
# asclient.connection.recv 1043 BYTE = 0x29 41 ')'
# asclient.connection.recv 1044 BYTE = 0x7a 122 'z'
# asclient.connection.recv 1045 BYTE = 0xd2 210 '?'
# asclient.connection.recv 1046 BYTE = 0x51 81 'Q'

