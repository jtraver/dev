#!/usr/bin/env python3

import io
import tarfile
import sys

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"

def main():
    ret1 = 0
    # ret1 += do_tar()
    ret1 += write_tar()
    if ret1:
        print("%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP))
    else:
        print("%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP))
    print("DONE")
    print("")
    sys.stdout.flush()
    sys.exit(ret1)


#        t = tarfile.TarFile(mode='r', fileobj=io.BytesIO(strm.data))
#        print("compose.container.get_file: t = %s" % str(t))
#        for member in t.getmembers():
#            print("compose.container.get_file: member = %s" % str(member))
#            f = t.extractfile(member)
#            print("compose.container.get_file: f = %s" % str(f))
#            return f.read()

def do_tar():
    ret1 = 0
#    f = open("tmp1.tar", "r")
#    # strm = f.raw
#    t = tarfile.TarFile(mode='r', fileobj=f)
#    print("compose.container.get_file: t = %s" % str(t))
    t = tarfile.open("tmp1.tar")
#     t = tarfile.TarFile(mode='r', fileobj=io.BytesIO(t1.data))
    for member in t.getmembers():
        print("compose.container.get_file: member = %s" % str(member))
    return ret1

def write_tar():
    ret1 = 0
    t = tarfile.open("tmp2.tar", "w")
    t.add("..")
    t.close()
    return ret1

main()
