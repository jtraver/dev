#!/usr/bin/env python3
#!/usr/bin/python

import datetime
import os
import time

oneday = 1 * 24 * 60 * 60 * 1000
fourdays = 4 * 24 * 60 * 60 * 1000

def main():
    stat1 = os.stat('stat1.py')
    print("stat1 = %s" % str(stat1))
    # stat1 = posix.stat_result(st_mode=33261, st_ino=782797, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=145, st_atime=1525359337, st_mtime=1456950249, st_ctime=1456950249)
    print("stat1.st_mode = %s" % str(stat1.st_mode))
    print("stat1.st_ino = %s" % str(stat1.st_ino))
    print("stat1.st_dev = %s" % str(stat1.st_dev))
    print("stat1.st_nlink = %s" % str(stat1.st_nlink))
    print("stat1.st_uid = %s" % str(stat1.st_uid))
    print("stat1.st_gid = %s" % str(stat1.st_gid))
    print("stat1.st_size = %s" % str(stat1.st_size))
    print("stat1.st_atime = %s" % str(stat1.st_atime))
    print("stat1.st_mtime = %s" % str(stat1.st_mtime))
    print("stat1.st_ctime = %s" % str(stat1.st_ctime))
    starttime = time.time()
    print("starttime = %s" % str(starttime))
    d = datetime.datetime.fromtimestamp(starttime)
    startdate = d.strftime("%y%m%d%H%M%S%f")
    print("startdate = %s" % str(startdate))

    print("\natime")
    atime = stat1.st_atime
    print("  %s" % str(atime))
    d = datetime.datetime.fromtimestamp(atime)
    adate = d.strftime("%y%m%d%H%M%S%f")
    print("  %s" % str(adate))
    diff1 = starttime - atime
    print("  %s" % str(diff1))
    print("  %s is four days" % str(fourdays))
    print("  %s is one day" % str(oneday))

    print("\nmtime")
    mtime = stat1.st_mtime
    print("  %s" % str(mtime))
    d = datetime.datetime.fromtimestamp(mtime)
    mdate = d.strftime("%y%m%d%H%M%S%f")
    print("  %s" % str(mdate))
    diff1 = starttime - mtime
    print("  %s" % str(diff1))
    print("  %s is four days" % str(fourdays))
    print("  %s is one day" % str(oneday))

    print("\nctime")
    ctime = stat1.st_ctime
    print("  %s" % str(ctime))
    d = datetime.datetime.fromtimestamp(ctime)
    cdate = d.strftime("%y%m%d%H%M%S%f")
    print("  %s" % str(cdate))
    diff1 = starttime - ctime
    print("  %s" % str(diff1))
    print("  %s is one day" % str(oneday))
    print("  %s is four days" % str(fourdays))


main()
