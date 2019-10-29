#!/usr/bin/env python3
#!/usr/bin/python3

import subprocess
import sys

def main():
    pip_install_upgrade_aerospike()

def pip_install_upgrade_aerospike():
    installed = False
    try:
        import aerospike
        installed = True
    except Exception, e:
        pass
    if installed:
        if '__version__' in dir(aerospike):
            print "existing aerospike Python client version is %s" % aerospike.__version__
        else:
            print "existing aerospike Python client version is unknown"
    if sys.platform == 'darwin':
        cmd = ['pip', 'install', '--upgrade', 'aerospike']
    else:
        cmd = ['sudo', 'pip', 'install', '--upgrade', 'aerospike']
    run_command(cmd)
    if installed:
        reload(aerospike)
    else:
        import aerospike
    if '__version__' in dir(aerospike):
        print "installed aerospike Python client version is %s" % aerospike.__version__
    else:
        print "installed aerospike Python client version is unknown"

def run_command(cmd):
    co = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out, err = co.communicate()
    if err or co.returncode != 0:
        print "cmd = %s" % str(cmd)
        print "get_package_filename: out = %s" % str(out)
        print "get_package_filename: err = %s" % str(err)
        print "get_package_filename: rc = %s" % str(co.returncode)
        sys.exit(1)
    
main()
