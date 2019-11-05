#!/usr/bin/python

# print "\nwhat\n"

# print "import sys"
import sys
# print "import os"
import os
# print "import platform"
import platform

# (distname,version,id)
distname, distversion, distid = platform.dist()
print "distname = %s" % str(distname)
print "distversion = %s" % str(distversion)
print "distid = %s" % str(distid)
# print "platform.dist = %s" % str(platform.dist())
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
# (distname,version,id)
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

# sysname = Linux
# nodename = jtraver
# release = 4.4.0-98-generic
# version = #121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017
# machine = x86_64
# os.uname = ('Linux', 'jtraver', '4.4.0-98-generic', '#121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017', 'x86_64')
# platform = linux2
# os name = posix
# platform.platform = Linux-4.4.0-98-generic-x86_64-with-Ubuntu-16.04-xenial
# platform.system = Linux
# platform.release = 4.4.0-98-generic
# platform.version = #121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017
# platform.linux_distrubution = ('Ubuntu', '16.04', 'xenial')
# sys.version = 2.7.12 (default, Nov 19 2016, 06:48:10) 
# [GCC 5.4.0 20160609]
# platform.dist = ('Ubuntu', '16.04', 'xenial')
# platform.system = Linux
# platform.machine = x86_64
# platform.platform = Linux-4.4.0-98-generic-x86_64-with-Ubuntu-16.04-xenial
# platform.uname = ('Linux', 'jtraver', '4.4.0-98-generic', '#121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017', 'x86_64', 'x86_64')
# platform.version = #121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017
# platform.mac_ver = ('', ('', '', ''), '')
# platform.release = 4.4.0-98-generic
# platform.system = Linux

# distname = Ubuntu
# distversion = 16.04
# distid = xenial
# sysname = Linux
# nodename = jtraver
# release = 4.4.0-98-generic
# version = #121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017
# machine = x86_64
# os.uname = ('Linux', 'jtraver', '4.4.0-98-generic', '#121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017', 'x86_64')
# platform = linux2
# os name = posix
# platform.platform = Linux-4.4.0-98-generic-x86_64-with-Ubuntu-16.04-xenial
# platform.system = Linux
# platform.release = 4.4.0-98-generic
# platform.version = #121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017
# platform.linux_distrubution = ('Ubuntu', '16.04', 'xenial')
# sys.version = 2.7.12 (default, Nov 19 2016, 06:48:10) 
# [GCC 5.4.0 20160609]
# platform.dist = ('Ubuntu', '16.04', 'xenial')
# platform.system = Linux
# platform.machine = x86_64
# platform.platform = Linux-4.4.0-98-generic-x86_64-with-Ubuntu-16.04-xenial
# platform.uname = ('Linux', 'jtraver', '4.4.0-98-generic', '#121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017', 'x86_64', 'x86_64')
# platform.version = #121-Ubuntu SMP Tue Oct 10 14:24:03 UTC 2017
# platform.mac_ver = ('', ('', '', ''), '')
# platform.release = 4.4.0-98-generic
# platform.system = Linux
 
# DEFAULT_POSTFIX = 'debian8.x86_64.deb'
# package_file += '.x86_64.deb'
# package_file += '.x86_64.rpm'
# package_file += '.x86_64.rpm'
# package_file += '.x86_64.rpm'

# amazonlinux-1 package name is aerospike-server-enterprise-4.7.0.3-1.ami.x86_64.rpm
# amazonlinux-2 package name is aerospike-server-enterprise-4.7.0.3-1.ami.x86_64.rpm
# centos-6 package name is aerospike-server-enterprise-4.7.0.3-1.el6.x86_64.rpm
# centos-7 package name is aerospike-server-enterprise-4.7.0.3-1.el7.x86_64.rpm
# debian-10 package name is aerospike-server-enterprise-4.7.0.3.debian10.x86_64.deb
# debian-8 package name is aerospike-server-enterprise-4.7.0.3.debian8.x86_64.deb
# debian-9 package name is aerospike-server-enterprise-4.7.0.3.debian9.x86_64.deb
# oraclelinux-7 package name is aerospike-server-enterprise-4.7.0.3-1.el7.x86_64.rpm
# ubuntu-14.04 package name is aerospike-server-enterprise-4.7.0.3.ubuntu14.04.x86_64.deb
# ubuntu-16.04 package name is aerospike-server-enterprise-4.7.0.3.ubuntu16.04.x86_64.deb
# ubuntu-18.04 package name is aerospike-server-enterprise-4.7.0.3.ubuntu18.04.x86_64.deb

# distname = Ubuntu
# distversion = 14.04
# distid = trusty
# sysname = Linux
# nodename = aerospike-green-0.longevity.aerospike.com
# release = 4.2.0-35-generic
# version = #40~14.04.1-Ubuntu SMP Fri Mar 18 16:37:35 UTC 2016
# machine = x86_64
# os.uname = ('Linux', 'aerospike-green-0.longevity.aerospike.com', '4.2.0-35-generic', '#40~14.04.1-Ubuntu SMP Fri Mar 18 16:37:35 UTC 2016', 'x86_64')
# platform = linux2
# os name = posix
# platform.platform = Linux-4.2.0-35-generic-x86_64-with-Ubuntu-14.04-trusty
# platform.system = Linux
# platform.release = 4.2.0-35-generic
# platform.version = #40~14.04.1-Ubuntu SMP Fri Mar 18 16:37:35 UTC 2016
# platform.linux_distrubution = ('Ubuntu', '14.04', 'trusty')
# sys.version = 2.7.6 (default, Jun 22 2015, 17:58:13) 
# [GCC 4.8.2]
# platform.dist = ('Ubuntu', '14.04', 'trusty')
# platform.system = Linux
# platform.machine = x86_64
# platform.platform = Linux-4.2.0-35-generic-x86_64-with-Ubuntu-14.04-trusty
# platform.uname = ('Linux', 'aerospike-green-0.longevity.aerospike.com', '4.2.0-35-generic', '#40~14.04.1-Ubuntu SMP Fri Mar 18 16:37:35 UTC 2016', 'x86_64', 'x86_64')
# platform.version = #40~14.04.1-Ubuntu SMP Fri Mar 18 16:37:35 UTC 2016
# platform.mac_ver = ('', ('', '', ''), '')
# platform.release = 4.2.0-35-generic
# platform.system = Linux

# distname = Ubuntu
# distversion = 18.04
# distid = bionic
# sysname = Linux
# nodename = client-oval-0
# release = 4.15.0-1014-gcp
# version = #14-Ubuntu SMP Thu Jul 19 08:06:08 UTC 2018
# machine = x86_64
# os.uname = ('Linux', 'client-oval-0', '4.15.0-1014-gcp', '#14-Ubuntu SMP Thu Jul 19 08:06:08 UTC 2018', 'x86_64')
# platform = linux2
# os name = posix
# platform.platform = Linux-4.15.0-1014-gcp-x86_64-with-Ubuntu-18.04-bionic
# platform.system = Linux
# platform.release = 4.15.0-1014-gcp
# platform.version = #14-Ubuntu SMP Thu Jul 19 08:06:08 UTC 2018
# platform.linux_distrubution = ('Ubuntu', '18.04', 'bionic')
# sys.version = 2.7.15+ (default, Oct  7 2019, 17:39:04) 
# [GCC 7.4.0]
# platform.dist = ('Ubuntu', '18.04', 'bionic')
# platform.system = Linux
# platform.machine = x86_64
# platform.platform = Linux-4.15.0-1014-gcp-x86_64-with-Ubuntu-18.04-bionic
# platform.uname = ('Linux', 'client-oval-0', '4.15.0-1014-gcp', '#14-Ubuntu SMP Thu Jul 19 08:06:08 UTC 2018', 'x86_64', 'x86_64')
# platform.version = #14-Ubuntu SMP Thu Jul 19 08:06:08 UTC 2018
# platform.mac_ver = ('', ('', '', ''), '')
# platform.release = 4.15.0-1014-gcp
# platform.system = Linux

# distname = centos
# distversion = 7.5.1804
# distid = Core
# sysname = Linux
# nodename = x1
# release = 3.10.0-862.el7.x86_64
# version = #1 SMP Fri Apr 20 16:44:24 UTC 2018
# machine = x86_64
# os.uname = ('Linux', 'x1', '3.10.0-862.el7.x86_64', '#1 SMP Fri Apr 20 16:44:24 UTC 2018', 'x86_64')
# platform = linux2
# os name = posix
# platform.platform = Linux-3.10.0-862.el7.x86_64-x86_64-with-centos-7.5.1804-Core
# platform.system = Linux
# platform.release = 3.10.0-862.el7.x86_64
# platform.version = #1 SMP Fri Apr 20 16:44:24 UTC 2018
# platform.linux_distrubution = ('CentOS Linux', '7.5.1804', 'Core')
# sys.version = 2.7.5 (default, Oct 30 2018, 23:45:53) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# platform.dist = ('centos', '7.5.1804', 'Core')
# platform.system = Linux
# platform.machine = x86_64
# platform.platform = Linux-3.10.0-862.el7.x86_64-x86_64-with-centos-7.5.1804-Core
# platform.uname = ('Linux', 'x1', '3.10.0-862.el7.x86_64', '#1 SMP Fri Apr 20 16:44:24 UTC 2018', 'x86_64', 'x86_64')
# platform.version = #1 SMP Fri Apr 20 16:44:24 UTC 2018
# platform.mac_ver = ('', ('', '', ''), '')
# platform.release = 3.10.0-862.el7.x86_64
# platform.system = Linux
 

# amazonlinux-1 package name is aerospike-server-enterprise-4.7.0.3-1.ami.x86_64.rpm
# amazonlinux-2 package name is aerospike-server-enterprise-4.7.0.3-1.ami.x86_64.rpm
# centos-6 package name is aerospike-server-enterprise-4.7.0.3-1.el6.x86_64.rpm
# centos-7 package name is aerospike-server-enterprise-4.7.0.3-1.el7.x86_64.rpm
# debian-10 package name is aerospike-server-enterprise-4.7.0.3.debian10.x86_64.deb
# debian-8 package name is aerospike-server-enterprise-4.7.0.3.debian8.x86_64.deb
# debian-9 package name is aerospike-server-enterprise-4.7.0.3.debian9.x86_64.deb
# oraclelinux-7 package name is aerospike-server-enterprise-4.7.0.3-1.el7.x86_64.rpm
# ubuntu-14.04 package name is aerospike-server-enterprise-4.7.0.3.ubuntu14.04.x86_64.deb
# ubuntu-16.04 package name is aerospike-server-enterprise-4.7.0.3.ubuntu16.04.x86_64.deb
# ubuntu-18.04 package name is aerospike-server-enterprise-4.7.0.3.ubuntu18.04.x86_64.deb

pversion = "4.7.0.3"
service = "aerospike-server"
edition = "enterprise"
print "\n"
build_id = None
aplatform = "x86_64"
epackage = None
apackage = "did not find the right build_id info"
oversion = None
ext = None
if sysname == "Darwin":
    build_id = "darwin"
elif sysname == "Linux":
    if "el6" in release:
        build_id = "centos-6"
        epackage = "aerospike-server-enterprise-4.7.0.3-1.el6.x86_64.rpm"
        oversion = "el6"
        ext = "rpm"
        apackage = "%s-%s-%s-1.%s.%s.%s" % (service, edition, pversion, oversion, aplatform, ext)
    elif "el7" in release:
        build_id = "centos-7"
        epackage = "aerospike-server-enterprise-4.7.0.3-1.el7.x86_64.rpm"
        oversion = "el7"
        ext = "rpm"
        apackage = "%s-%s-%s-1.%s.%s.%s" % (service, edition, pversion, oversion, aplatform, ext)
    elif "el8" in release:
        build_id = "centos-8"
        oversion = "el8"
        ext = "rpm"
        apackage = "%s-%s-%s-1.%s.%s.%s" % (service, edition, pversion, oversion, aplatform, ext)
        epackage = "aerospike-server-enterprise-4.7.0.3-1.el8.x86_64.rpm"
    else:
        if distname == "Ubuntu":
            build_id = "ubuntu-%s" % str(distversion)
            ext = "deb"
            if distversion == "14.04":
                oversion = "ubuntu14.04"
                apackage = "%s-%s-%s.%s.%s.%s" % (service, edition, pversion, oversion, aplatform, ext)
                epackage = "aerospike-server-enterprise-4.7.0.3.ubuntu14.04.x86_64.deb"
            elif distversion == "16.04":
                oversion = "ubuntu16.04"
                apackage = "%s-%s-%s.%s.%s.%s" % (service, edition, pversion, oversion, aplatform, ext)
                epackage = "aerospike-server-enterprise-4.7.0.3.ubuntu16.04.x86_64.deb"
            elif distversion == "18.04":
                oversion = "ubuntu18.04"
                apackage = "%s-%s-%s.%s.%s.%s" % (service, edition, pversion, oversion, aplatform, ext)
                epackage = "aerospike-server-enterprise-4.7.0.3.ubuntu18.04.x86_64.deb"
            else:
                print "what? distversion = %s" % str(distversion)
        else:
            print "what? release = %s" % str(release)
            print "what? distname = %s" % str(distname)
else:
    print "what? sysname = %s" % str(sysname)

if apackage == epackage:
    print "build_id = %s %s" % (str(build_id), str(apackage))
else:
    print "FAIL build_id = %s %s expected %s" % (str(build_id), str(apackage), str(epackage))
