#!/usr/bin/env python3
#!/usr/bin/python

def main():
    # hex1()
    hex2()

def hex1():
    # ba1 = bytearray.fromhex("0x69")
    ba1 = bytearray.fromhex("69")
    print(("ba1 = %s" % str(ba1)))

def hex2():
    strings = []
    strings.append("asclient.connection.recv 1037 BYTE = 0x21 33 '!'")
    strings.append("asclient.connection.recv 1038 BYTE = 0x69 105 'i'")
    strings.append("asclient.connection.recv 1039 BYTE = 0x6f 111 'o'")
    strings.append("asclient.connection.recv 1040 BYTE = 0x34 52 '4'")
    strings.append("asclient.connection.recv 1041 BYTE = 0x54 84 'T'")
    strings.append("asclient.connection.recv 1042 BYTE = 0xcf 207 '?'")
    strings.append("asclient.connection.recv 1043 BYTE = 0x29 41 ')'")
    strings.append("asclient.connection.recv 1044 BYTE = 0x7a 122 'z'")
    strings.append("asclient.connection.recv 1045 BYTE = 0xd2 210 '?'")
    strings.append("asclient.connection.recv 1046 BYTE = 0x51 81 'Q'")
    for str1 in strings:
        print(("str1 = %s" % str(str1)))
        fields1 = str1.split(" ")
        for i1 in range(len(fields1)):
            field1 = fields1[i1]
            print(("  %s %s" % (str(i1), str(field1))))

main()
