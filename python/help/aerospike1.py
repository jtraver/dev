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

def do_info2():
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


def dir1(object):
    print "\n"
    print "object = %s" % dir(object)
    for e in dir(object):
        if '__' in e:
            continue
        attr = getattr(object, e)
        # if 'builtin_function_or_method' in str(type(attr)) or type(attr) == int or type(attr) == str or 'NoneType' in str(type(attr)):
        if type(attr) == int or type(attr) == str or 'NoneType' in str(type(attr)):
            continue
        print "e = %s" % str(e)
        # e is just a string
        # print "  type e = %s" % type(e)
        # print "  dir e = %s" % dir(e)
        print "  type attr = %s" % type(attr)
        # print "    dir attr = %s" % dir(attr)


def dir2(object):
    attrs = []
    for e in dir(object):
        if '__' in e:
            continue
        attr = getattr(object, e)
        # if 'builtin_function_or_method' in str(type(attr)) or type(attr) == int or type(attr) == str or 'NoneType' in str(type(attr)):
        if type(attr) == int or type(attr) == str or 'NoneType' in str(type(attr)):
            continue
        attrs.append(e)
    return attrs

def main():
    # dir1(aerospike)
    attrs = dir2(aerospike)
    print "attrs = %s" % str(attrs)
    for e in attrs:
        print "\naerospike.%s" % e
        attr = getattr(aerospike, e)
        if 'method' in str(type(attr)):
            continue
        # dir1(attr)
        attrs2 = dir2(attr)
        print "  attrs2 = %s" % str(attrs2)
        for e2 in attrs2:
            print "\naerospike.%s.%s" % (e, e2)
            attr3 = getattr(attr, e2)
            if 'method' in str(type(attr3)):
                continue
            # dir1(attr3)
            attrs3 = dir2(attr3)
            print "  attrs3 = %s" % str(attrs3)
            for e3 in attrs3:
                print "\naerospike.%s.%s.%s" % (e, e2, e3)
                attr4 = getattr(attr3, e3)
                if 'method' in str(type(attr4)):
                    continue
                # dir1(attr4)
                attrs4 = dir2(attr4)
                print "  attrs4 = %s" % str(attrs4)

main()
