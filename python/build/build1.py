#!/usr/bin/python

import glob
import os
import yaml

def main():
    cname = 'container'
    home1 = os.path.expanduser("~")
    # print "home1 = %s" % str(home1)
    buildfiles = glob.glob(home1 + "/dev/git/citrusleaf/*/.build.yml")
    for buildfile in buildfiles:
        oses = []
        print "\nbuildfile %s" % buildfile
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
                continue
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
        except Exception, e:
            print "FAIL %s -> %s" % (str(buildfile), str(e))
        for os1 in oses:
            print "  %s" % os1

main()
