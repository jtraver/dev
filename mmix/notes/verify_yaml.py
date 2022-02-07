#!/usr/bin/env python3
#!/usr/bin/python

import sys
import yaml

VT100_BOLD = "[0;1m"
VT100_RED = "[0;1;31m"
VT100_GREEN = "[0;1;32m"
VT100_STOP_MARKUP = "[0m"


def file(filename):
    f = open(filename, "r")
    contents = ""
    for line in f:
        contents += line
    f.close()
    return contents

def main():
    ret1 = 0
    ret1 += verify1()
    if ret1:
        print("%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP))
    else:
        print("%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP))
    print("DONE")
    print("^G")
    sys.stdout.flush()
    sys.exit(ret1)

def verify1():
    ret1 = 0
    print("\n---------------------------------------------------------------------------------")
    print("verify1")

    fn1 = "op_codes.yaml"
    op_codes1 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    fn1 = "tmp.yaml"
    s1 = yaml.dump(op_codes1, default_flow_style=False)
    print("op_codes1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    op_codes2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if op_codes1 == op_codes2:
        print("verify1: load and dump worked")
    else:
        print("verify1: load and dump did not work")
        ret1 += 1
    return ret1

main()
