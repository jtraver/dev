#!/usr/bin/env python3
#!/usr/bin/python

import time

def main():
    tuple1 = ("str", 0, bytearray("bytearray", "utf-8"))
    print("tuple1 = %s" % str(tuple1))
    print("type tuple1 = %s" % str(type(tuple1)))
    if isinstance(tuple1, tuple):
        print("PASS")
    else:
        print("FAIL")

main()
