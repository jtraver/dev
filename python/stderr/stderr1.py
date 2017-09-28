#!/usr/bin/python

import sys
import glob

def is_version_number(candidate):
    fields1 = candidate.split(".")
    len1 = len(fields1)
    if len1 < 2:
        return False
    for n1 in fields1:
        fields2 = n1.split("-")
        len2 = len(fields2)
        if len2 > 1:
            for n2 in fields2:
                try:
                    if n2.startswith("g"):
                        n2 = n2[1:]
                    else:
                        n3 = int(n2)
                except Exception, e:
                    return False
        else:
            try:
                n2 = int(n1)
            except Exception, e:
                return False
    return True

# semantic versioning
def get_newer_version(v1, v2):
    if not v1:
        return v2
    if not v2:
        return v1
    if v1 == v2:
        return v1
    if not is_version_number(v1):
        return v2
    if not is_version_number(v2):
        return v1
    a1 = v1.split("-")
    a2 = v2.split("-")
    b1 = a1[0].split(".")
    b2 = a2[0].split(".")
    l1 = len(b1)
    l2 = len(b2)
    l3 = l1
    if l1 > l2:
        l3 = l2
    for i1 in xrange(l3):
        c1 = int(b1[i1])
        c2 = int(b2[i1])
        if c1 > c2:
            return v1
        if c2 > c1:
            return v2
    if l1 > l2:
        return v1
    if l2 > l1:
        return v2
    l1 = len(a1)
    l2 = len(a2)
    if l1 > 1 and l2 > 1:
        d1 = int(a1[1])
        d2 = int(a2[1])
        if d1 > d2:
            return v1
        if d2 > d1:
            return v2
    if l1 > l2:
        return v1
    if l2 > l1:
        return v2
    if v1 > v2:
        return v1
    return v2

def do_sort(a, b):
    if a == b:
        return 0
    a1 = find_version(a)
    b1 = find_version(b)
    c = get_newer_version(a1, b1)
    # print "c = %s" % c
    if c == a1:
        # print "%s > %s" % (a, b)
        return 1
    # print "%s < %s" % (a, b)
    return -1

def find_version(c1):
    # print "looking at %s" % c1
    if not is_version_number(c1):
        # print "not a version number: %s" % c1
        # sys.exit(1)
        pass
    else:
        return c1
    # not a version number: ../../../test/john/python/aerospike/e/conf/3.10.0.1.enterprise
    fields1 = c1.split("/")
    c2 = fields1[len(fields1) - 1]
    if not is_version_number(c2):
        # print "not a version number: %s" % c2
        # sys.exit(1)
        pass
    else:
        return c2
    # not a version number: 3.10.0.1.enterprise
    fields2 = c2.split(".enterprise")
    c3 = fields2[0]
    if not is_version_number(c3):
        # print "not a version number: %s" % c3
        # sys.exit(1)
        pass
    else:
        return c3
    # not a version number: 3.10.0.1.community
    fields3 = c3.split(".community")
    c4 = fields3[0]
    if not is_version_number(c4):
        # print "not a version number: %s" % c4
        # sys.exit(1)
        pass
    else:
        return c4
    # not a version number: 3.12.1_60.auth
    fields4 = c4.split(".auth")
    c5 = fields4[0]
    if not is_version_number(c5):
        # print "not a version number: %s" % c5
        # sys.exit(1)
        pass
    else:
        return c5
    # not a version number: 3.12.1_60
    fields5 = c5.split("_")
    c6 = "-".join(fields5)
    if not is_version_number(c6):
        # print "not a version number: %s" % c6
        # sys.exit(1)
        pass
    else:
        return c6
    # not a version number: 3.12.1-60.generic
    fields6 = c6.split(".generic")
    c7 = fields6[0]
    if not is_version_number(c7):
        # print "not a version number: %s" % c7
        # sys.exit(1)
        pass
    else:
        return c7
    # not a version number: 3.5.12-xdr
    fields7 = c7.split("-xdr")
    c8 = fields7[0]
    if not is_version_number(c8):
        # print "not a version number: %s" % c8
        # sys.exit(1)
        pass
    else:
        return c8
    # not a version number: Aerospike-Enterprise-Edition-build-3.12.1-104-gff25936
    fields8 = c8.split("-build-")
    c9 = fields8[len(fields8) - 1]
    if not is_version_number(c9):
        # print "not a version number: %s" % c9
        # sys.exit(1)
        pass
    else:
        return c9
    # not a version number: version.3.12.1-60
    fields9 = c9.split("version.")
    c10 = fields9[len(fields9) - 1]
    if not is_version_number(c10):
        # print "not a version number: %s" % c10
        sys.exit(1)
        pass
    else:
        return c10

def main():
    # /Users/jtraver/dev/git/jtraver/dev/python/sort
    pyfiles = glob.glob("../../../test/john/python/aerospike/e/conf/*")
    # for pyfile in pyfiles:
        # print "pyfile %s" % pyfile
    pyfiles.sort(do_sort)
    # print "pyfiles = %s" % str(pyfiles)
    print "\n"
    print "sorted"
    for pyfile in pyfiles:
        print "%s" % pyfile
    print ""

main()
sys.stderr.write("")
os.write(2, "")
print ""
