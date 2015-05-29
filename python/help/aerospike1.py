import apihelper
import aerospike

def pinfo():
    print "--------------------------------------------------------------------------------"
    print "| aerospike"
    print "--------------------------------------------------------------------------------"
    apihelper.info(aerospike)
    print "aerospike = %s" % str(aerospike)
    print "aerospike = %s" % dir(aerospike)
    print "aerospike = %s" % type(aerospike)

    print "--------------------------------------------------------------------------------"
    print "| aerospike.Client"
    print "--------------------------------------------------------------------------------"
    apihelper.info(aerospike.Client)

def info(object, level = 1):
    if level > 3:
        return
    print "\n"
    print "--------------------------------------------------------------------------------"
    print "object = %s" % str(object)
    try:
        for e in dir(object):
            print "  e = %s" % e
            attr = getattr(object, e)
            print "    attr = %s" % str(attr)
            print "    attr = %s" % type(attr)
            # print "    attr = %s" % dir(attr)
            if callable(attr):
                try:
                    attr()
                except Exception, ex1:
                    print "      1 exception is %s" % str(ex1)
            if type(attr) != int:
                info(attr, level + 1)
    except Exception, ex2:
        print "      2 exception is %s" % str(ex2)

info(aerospike)
