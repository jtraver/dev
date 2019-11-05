#!/usr/bin/python

# print "\nwhat\n"

# print "import sys"
import sys
# print "import os"
import os
# print "import platform"
import platform

sysname, nodename, release, version, machine = os.uname()
print "sysname = %s" % str(sysname)
print "nodename = %s" % str(nodename)
print "release = %s" % str(release)
print "version = %s" % str(version)
print "machine = %s" % str(machine)
# uname      uname() -> (sysname, nodename, release, version, machine) Return a tuple identifying the current operating system.
print "os.uname = %s" % str(os.uname())
print "platform = %s" % str(sys.platform)
print "os name = %s" % str(os.name)
# os.system("uname -a")
print "platform.platform = %s" % str(platform.platform())
print "platform.system = %s" % str(platform.system())
print "platform.release = %s" % str(platform.release())
print "platform.version = %s" % str(platform.version())
print "platform.linux_distrubution = %s" % str(platform.linux_distribution())
print "sys.version = %s" % str(sys.version)
print "platform.dist = %s" % str(platform.dist())
print "platform.system = %s" % str(platform.system())
print "platform.machine = %s" % str(platform.machine())
print "platform.platform = %s" % str(platform.platform())
print "platform.uname = %s" % str(platform.uname())
print "platform.version = %s" % str(platform.version())
print "platform.mac_ver = %s" % str(platform.mac_ver())
print "platform.release = %s" % str(platform.release())
print "platform.system = %s" % str(platform.system())
# platform.system_alias()
# print "platform.system_alias = %s" % str(platform.system_alias())

# sysname = Darwin
# nodename = Johns-MacBook-Pro.local
# release = 19.0.0
# version = Darwin Kernel Version 19.0.0: Wed Sep 25 20:18:50 PDT 2019; root:xnu-6153.11.26~2/RELEASE_X86_64
# machine = x86_64
# os.uname = ('Darwin', 'Johns-MacBook-Pro.local', '19.0.0', 'Darwin Kernel Version 19.0.0: Wed Sep 25 20:18:50 PDT 2019; root:xnu-6153.11.26~2/RELEASE_X86_64', 'x86_64')
# platform = darwin
# os name = posix
# platform.platform = Darwin-19.0.0-x86_64-i386-64bit
# platform.system = Darwin
# platform.release = 19.0.0
# platform.version = Darwin Kernel Version 19.0.0: Wed Sep 25 20:18:50 PDT 2019; root:xnu-6153.11.26~2/RELEASE_X86_64
# platform.linux_distrubution = ('', '', '')
# sys.version = 2.7.16 (default, Aug 24 2019, 18:37:03) 
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.32.4) (-macos10.15-objc-s
# platform.dist = ('', '', '')
# platform.system = Darwin
# platform.machine = x86_64
# platform.platform = Darwin-19.0.0-x86_64-i386-64bit
# platform.uname = ('Darwin', 'Johns-MacBook-Pro.local', '19.0.0', 'Darwin Kernel Version 19.0.0: Wed Sep 25 20:18:50 PDT 2019; root:xnu-6153.11.26~2/RELEASE_X86_64', 'x86_64', 'i386')
# platform.version = Darwin Kernel Version 19.0.0: Wed Sep 25 20:18:50 PDT 2019; root:xnu-6153.11.26~2/RELEASE_X86_64
# platform.mac_ver = ('10.15', ('', '', ''), 'x86_64')
# platform.release = 19.0.0
# platform.system = Darwin

# [jtraver@q10 centos]$ buildctl ls citrusleaf/qe.go/3.0.2/build/1.11/default/artifacts/
# TYPE      SIZE   DATE                  NAME
# f        13 MB   14 Jun 19 16:50 PDT   browser
# f        15 MB   14 Jun 19 16:50 PDT   build-worker
# f        13 MB   14 Jun 19 16:50 PDT   buildctl.darwin
# f        13 MB   14 Jun 19 16:50 PDT   buildctl.linux
# f        10 MB   14 Jun 19 16:50 PDT   longevityctl.darwin
# f        10 MB   14 Jun 19 16:50 PDT   longevityctl.linux
# f        13 MB   14 Jun 19 16:50 PDT   source-worker
# f        14 MB   14 Jun 19 16:50 PDT   test-runner.darwin
# f        14 MB   14 Jun 19 16:50 PDT   test-runner.linux
# f        13 MB   14 Jun 19 16:50 PDT   test-scheduler
# f        16 MB   14 Jun 19 16:50 PDT   test-worker
# f        14 MB   14 Jun 19 16:50 PDT   testctl.darwin
# f        14 MB   14 Jun 19 16:50 PDT   testctl.linux
# f        11 MB   14 Jun 19 16:50 PDT   webhook

# [jtraver@q10 centos]$ buildctl ls citrusleaf/aerospike-server/4.7.0.3/build/
# TYPE      SIZE   DATE                  NAME
# d            -   -                     amazonlinux-1
# d            -   -                     amazonlinux-2
# d            -   -                     centos-6
# d            -   -                     centos-7
# d            -   -                     debian-10
# d            -   -                     debian-8
# d            -   -                     debian-9
# d            -   -                     oraclelinux-7
# d            -   -                     ubuntu-14.04
# d            -   -                     ubuntu-16.04
# d            -   -                     ubuntu-18.04

# sysname = Linux
# nodename = q10
# release = 3.10.0-862.14.4.el7.x86_64
# version = #1 SMP Wed Sep 26 15:12:11 UTC 2018
# machine = x86_64
# os.uname = ('Linux', 'q10', '3.10.0-862.14.4.el7.x86_64', '#1 SMP Wed Sep 26 15:12:11 UTC 2018', 'x86_64')
# platform = linux2
# os name = posix
# platform.platform = Linux-3.10.0-862.14.4.el7.x86_64-x86_64-with-centos-7.5.1804-Core
# platform.system = Linux
# platform.release = 3.10.0-862.14.4.el7.x86_64
# platform.version = #1 SMP Wed Sep 26 15:12:11 UTC 2018
# platform.linux_distrubution = ('CentOS Linux', '7.5.1804', 'Core')
# sys.version = 2.7.5 (default, Oct 30 2018, 23:45:53) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# platform.dist = ('centos', '7.5.1804', 'Core')
# platform.system = Linux
# platform.machine = x86_64
# platform.platform = Linux-3.10.0-862.14.4.el7.x86_64-x86_64-with-centos-7.5.1804-Core
# platform.uname = ('Linux', 'q10', '3.10.0-862.14.4.el7.x86_64', '#1 SMP Wed Sep 26 15:12:11 UTC 2018', 'x86_64', 'x86_64')
# platform.version = #1 SMP Wed Sep 26 15:12:11 UTC 2018
# platform.mac_ver = ('', ('', '', ''), '')
# platform.release = 3.10.0-862.14.4.el7.x86_64
# platform.system = Linux
 
print " "
build_id = None
if sysname == "Darwin":
    build_id = "darwin"
elif sysname == "Linux":
    if "el6" in release:
        build_id = "centos-6"
    elif "el7" in release:
        build_id = "centos-7"
    elif "el8" in release:
        build_id = "centos-8"
    else:
        print "what? release = %s" % str(release)
else:
    print "what? sysname = %s" % str(sysname)

print "build_id = %s" % str(build_id)
