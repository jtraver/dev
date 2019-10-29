#!/usr/bin/env python3
#!/usr/bin/python

import psutil
import subprocess
import time

def main():
    args = ('count1.py')
    popen = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='.')
    proc = psutil.Process(popen.pid)
    # while True:
    for count in xrange(5):
        # A set of strings representing the status of a process. Returned by psutil.Process.status().
        # if proc.status() == psutil.STATUS_ZOMBIE:
        # proc.status() running
        # proc.status() zombie
        print "proc.status() %s" % str(proc.status())
        if proc.status() == psutil.STATUS_RUNNING or proc.status() == psutil.STATUS_SLEEPING:
            time.sleep(1)
    if proc.status() == psutil.STATUS_RUNNING or proc.status() == psutil.STATUS_SLEEPING:
        popen.terminate()
    if proc.status() == psutil.STATUS_RUNNING or proc.status() == psutil.STATUS_SLEEPING:
        popen.kill()
    out, err = popen.communicate()
    print "out = %s" % str(out)
    print "err = %s" % str(err)

# Changed in version 5.4.0: also available on AIX.
# psutil.STATUS_RUNNING
# psutil.STATUS_SLEEPING
# psutil.STATUS_DISK_SLEEP
# psutil.STATUS_STOPPED
# psutil.STATUS_TRACING_STOP
# psutil.STATUS_ZOMBIE
# psutil.STATUS_DEAD
# psutil.STATUS_WAKE_KILL
# psutil.STATUS_WAKING
# psutil.STATUS_PARKED(Linux)
# psutil.STATUS_IDLE(Linux, macOS, FreeBSD)
# psutil.STATUS_LOCKED(FreeBSD)
# psutil.STATUS_WAITING(FreeBSD)
# psutil.STATUS_SUSPENDED(NetBSD)
# A set of strings representing the status of a process. Returned by psutil.Process.status().



main()
