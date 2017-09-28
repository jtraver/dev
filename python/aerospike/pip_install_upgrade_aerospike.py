#!/usr/bin/python

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

main()
