import apihelper
import aerospike

found = {}

def pinfo(object):
    print
    print "--------------------------------------------------------------------------------"
    print "| %s" % str(object)
    print "--------------------------------------------------------------------------------"
    apihelper.info(object)
    # print "aerospike = %s" % str(aerospike)
    # print "aerospike = %s" % dir(aerospike)
    # print "aerospike = %s" % type(aerospike)

    # print "--------------------------------------------------------------------------------"
    # print "| aerospike.Client"
    # print "--------------------------------------------------------------------------------"
    # apihelper.info(aerospike.Client)

def info(object, level = 1):
    if level > 3:
        return
    print "\n"
    print "--------------------------------------------------------------------------------"
    print "object = %s" % str(object)
    try:
        for e in dir(object):
            attr = getattr(object, e)
            if callable(attr):
                print "  e = %s" % e
                print "    attr = %s" % str(attr)
                print "    attr = %s" % type(attr)
                # print "    attr = %s" % dir(attr)
                try:
                    attr()
                except Exception, ex1:
                    print "      1 exception is %s" % str(ex1)
                # if type(attr) != int:
                if not "__" in str(e):
                    info(attr, level + 1)
    except Exception, ex2:
        print "      2 exception is %s" % str(ex2)

def info2(object):
    str1 = str(object)
    if str1 in found:
        return
    # if "<method" in str1 and "aerospike" in str1 and not "__" in str1:
    if "aerospike" in str1 and not "__" in str1:
        print "%s" % str1
        if "<method" in str1:
            found[str1] = object
        try:
            for e in dir(object):
                attr = getattr(object, e)
                info2(attr)
        except Exception, ex2:
            pass

# info(aerospike)
info2(aerospike)

print "\n"
count = 0
for k, e in found.items():
    if callable(e):
        count += 1
        print "%s %s" % (str(count), k)
        try:
            e()
        except Exception, ex:
            print "    %s" % str(ex)

def pinfos():
    pinfo(aerospike)
    pinfo(aerospike.Client)
    pinfo(aerospike.Key)
    pinfo(aerospike.Query)
    pinfo(aerospike.Scan)
    pinfo(aerospike.client)
    pinfo(aerospike.llist)
    pinfo(aerospike.lmap)
    pinfo(aerospike.lset)
    pinfo(aerospike.lstack)
    pinfo(aerospike.set_deserializer)
    pinfo(aerospike.set_log_handler)
    pinfo(aerospike.set_log_level)
    pinfo(aerospike.set_serializer)

# pinfos()
