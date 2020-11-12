#!/usr/bin/env python3

import sys

def main():
    i1 = 256
    i2 = i1 * i1
    print("i2 = %s" % str(i2))
    i4 = i2 * i2
    print("i4 = %s" % str(i4))
    packint1()

def packint1():
    i1 = 256
    i2 = i1 * i1
    i4 = i2 * i2
    print("packint1")
    limit1 = 33
    int1 = 1
    for _ in range(limit1):
        print("\npackint1: int1 = %s" % str(int1))
        str1 = get_hex_string(int1)
        print("  packint1: str1 = %s" % str1)
        int2 = int(str1, 16)
        if int2 != int1:
            print("FAIL int1 = %s" % str(int1))
            print("FAIL str1 = %s" % str(str1))
            print("FAIL int2 = %s" % str(int2))
            sys.exit(1)
        int1 <<= 1

def get_hex_string(int1):
    print("  get_hex_string int1 = 0x%x" % int1)
    if int1 < 16:
        byte1 = "%02x" % int1
        return byte1
    elif int1 < 65536:
        byte1 = int1 & 0xff
        byte2 = (int1 >> 8)
        return "%02x%02x" % (byte2, byte1)
    elif int1 < 4294967296:
        byte1 = int1 & 0xff
        byte2 = (int1 >> 8) & 0xff
        byte3 = (int1 >> 16) & 0xff
        byte4 = (int1 >> 24)
        return "%02x%02x%02x%02x" % (byte4, byte3, byte2, byte1)
    else:
        return "FAIL"
    return "---"

main()
