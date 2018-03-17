#!/usr/bin/python

import glob
import os
import sys
import yaml

def main():
    buildfile = sys.argv[1]
    cname = 'container'
    bname = 'build'
    oses = []
    editions = []
    # print "\nbuildfile %s" % buildfile
    file1 = open(buildfile, 'r')
    for line in file1.xreadlines():
        line = line.strip()
        # print "  line: %s" % str(line)
    file1.close()
    try:
        build1 = yaml.load(file(buildfile))
        # print "build1 = %s" % str(build1)
        #for k1,v1 in build1.items():
        #    print "  %s: %s" % (str(k1), str(v1))
        if not cname in build1:
            # print "%s specifies no containers" % str(buildfile)
            sys.exit(1)
        containers = build1[cname]
        for container in containers:
            # print "    container: %s" % str(container)
            for k2,v2 in container.items():
                # print "      %s: %s" % (str(k2), str(v2))
                for c1 in v2:
                    # print "        %s" % str(c1)
                    fields1 = c1.split(":")
                    os1 = fields1[1]
                    # print "          %s" % str(os1)
                    oses.append(os1)
        builds = build1[bname]
        # print "%s -> %s" % (str(bname), str(builds))
        for build in builds:
            # print "  %s" % str(build)
            #for k3,v3 in build.items():
            #    print "    %s: %s" % (str(k3), str(v3))
            edition = build['name']
            # print "      %s" % str(edition)
            editions.append(edition)
    except Exception, e:
        print "FAIL %s -> %s" % (str(buildfile), str(e))
    for ed1 in editions:
        for os1 in oses:
            print "%s %s" % (os1, ed1)

main()
