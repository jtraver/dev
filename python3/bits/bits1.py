#!/usr/bin/env python3

import sys

def main():
    bits1()

def bits1():
    for op1 in range(16):
        not1 = ~op1 & 0xf
        if (op1 & not1) != 0:
            print(" op1 = %s" % str(op1))
            print("not1 = %s" % str(not1))
        if (op1 | not1) != 15:
            print(" op1 = %s" % str(op1))
            print("not1 = %s" % str(not1))
        for op2 in range(16):
            and1 = op1 & op2
            # print("%s and %s = %s" % (str(op1), str(op2), str(and1)))
            or1 = op1 | op2
            # print("%s or %s = %s" % (str(op1), str(op2), str(or1)))
            xor1 = op1 ^ op2
            # print("%s xor %s = %s" % (str(op1), str(op2), str(xor1)))
            #if or1 != xor1:
            #    print("%s  or %s = %s" % (str(op1), str(op2), str(or1)))
            #    print("%s xor %s = %s" % (str(op1), str(op2), str(xor1)))
            ls1 = op1 << op2
            rs1 = ls1 >> op2
            if rs1 != op1:
                print("rs1 = %s" % str(rs1))
                print("op1 = %s" % str(op1))
                print("op2 = %s" % str(op2))

main()
