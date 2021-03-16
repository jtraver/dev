#!/usr/bin/env python3
#!/usr/bin/python

def main():
    # hex1()
    # hex2()
    hex3()

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

def hex3():
    trid = 7804759398277278707
    print("trid = %x" % trid)
    # trid = 6c50135243b56bf3
    # trid = 6c 50 13 52 43 b5 6b f3

# scanid = 7804759398277278707
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 72 BYTE = 0x6c 108 'l'        not scanid??????
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 73 BYTE = 0x50 80 'P'
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 74 BYTE = 0x13 19 '^S'
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 75 BYTE = 0x52 82 'R'
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 76 BYTE = 0x43 67 'C'
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 77 BYTE = 0xb5 181 'µ'
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 78 BYTE = 0x6b 107 'k'
# 2021-03-16 13:13:15 DEBUG JATCCLIENT as_socket_write_deadline 660 79 BYTE = 0xf3 243 'ó'


main()
