#!/usr/bin/python

import apihelper
import aerospike

found = {}
elements = {
    "Client": {
        "admin_change_password": {
        },
        "admin_create_role": {
        },
        "admin_create_user": {
        },
        "admin_drop_role": {
        },
        "admin_drop_user": {
        },
        "admin_grant_privileges": {
        },
        "admin_grant_roles": {
        },
        "admin_query_role": {
        },
        "admin_query_roles": {
        },
        "admin_query_user": {
        },
        "admin_query_users": {
        },
        "admin_revoke_privileges": {
        },
        "admin_revoke_roles": {
        },
        "admin_set_password": {
        },
        "append": {
        },
        "apply": {
        },
        "close": {
        },
        "connect": {
        },
        "exists": {
        },
        "exists_many": {
        },
        "get": {
        },
        "get_key_digest": {
        },
        "get_many": {
        },
        "get_nodes": {
        },
        "increment": {
        },
        "index_integer_create": {
        },
        "index_list_create": {
        },
        "index_map_keys_create": {
        },
        "index_map_values_create": {
        },
        "index_remove": {
        },
        "index_string_create": {
        },
        "info": {
        },
        "info_node": {
        },
        "is_connected": {
        },
        "key": {
        },
        "llist": {
        },
        "lmap": {
        },
        "lset": {
        },
        "lstack": {
        },
        "operate": {
        },
        "prepend": {
        },
        "put": {
        },
        "query": {
        },
        "remove": {
        },
        "remove_bin": {
        },
        "scan": {
        },
        "scan_apply": {
        },
        "scan_info": {
        },
        "select": {
        },
        "select_many": {
        },
        "touch": {
        },
        "udf_get": {
        },
        "udf_list": {
        },
        "udf_put": {
        },
        "udf_remove": {
        }
    },
    "Key": {
        "apply": {
        },
        "exists": {
        },
        "get": {
        },
        "put": {
        },
        "remove": {
        },
    },
    "Query": {
        "apply": {
        },
        "foreach": {
        },
        "results": {
        },
        "select": {
        },
        "where": {
        },
    },
    "Scan": {
        "foreach": {
        },
        "results": {
        },
        "select": {
        },
    },
    "client": {
    },
    "exception": {
        "AdminError": {
            "message": {
            },
            "args": {
            },
        },
        "AerospikeError": {
            "message": {
            },
            "args": {
            },
        },
        "BinExistsError": {
            "message": {
            },
            "args": {
            },
        },
        "BinIncompatibleType": {
            "message": {
            },
            "args": {
            },
        },
        "BinNameError": {
            "message": {
            },
            "args": {
            },
        },
        "BinNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "ClientError": {
            "message": {
            },
            "args": {
            },
        },
        "ClusterChangeError": {
            "message": {
            },
            "args": {
            },
        },
        "ClusterError": {
            "message": {
            },
            "args": {
            },
        },
        "DeviceOverload": {
            "message": {
            },
            "args": {
            },
        },
        "ExpiredPassword": {
            "message": {
            },
            "args": {
            },
        },
        "ForbiddenError": {
            "message": {
            },
            "args": {
            },
        },
        "ForbiddenPassword": {
            "message": {
            },
            "args": {
            },
        },
        "IllegalState": {
            "message": {
            },
            "args": {
            },
        },
        "IndexError": {
            "message": {
            },
            "args": {
            },
        },
        "IndexFoundError": {
            "message": {
            },
            "args": {
            },
        },
        "IndexNameMaxCount": {
            "message": {
            },
            "args": {
            },
        },
        "IndexNameMaxLen": {
            "message": {
            },
            "args": {
            },
        },
        "IndexNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "IndexNotReadable": {
            "message": {
            },
            "args": {
            },
        },
        "IndexOOM": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidCommand": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidCredential": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidField": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidHostError": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidPassword": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidPrivilege": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidRequest": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidRole": {
            "message": {
            },
            "args": {
            },
        },
        "InvalidUser": {
            "message": {
            },
            "args": {
            },
        },
        "LDTBinDamaged": {
            "message": {
            },
            "args": {
            },
        },
        "LDTBinExistsError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTBinNameNotString": {
            "message": {
            },
            "args": {
            },
        },
        "LDTBinNameNull": {
            "message": {
            },
            "args": {
            },
        },
        "LDTBinNameTooLong": {
            "message": {
            },
            "args": {
            },
        },
        "LDTBinNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTDeleteError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTFilterFunctionBad": {
            "message": {
            },
            "args": {
            },
        },
        "LDTFilterFunctionNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTInputParamError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTInsertError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTInternalError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTKeyFunctionBad": {
            "message": {
            },
            "args": {
            },
        },
        "LDTKeyFunctionNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSearchError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubRecNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubrecCloseError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubrecCreateError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubrecDamaged": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubrecDeleteError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubrecOpenError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubrecPoolDamaged": {
            "message": {
            },
            "args": {
            },
        },
        "LDTSubrecUpdateError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTTooManyOpenSubrecs": {
            "message": {
            },
            "args": {
            },
        },
        "LDTTopRecNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTToprecCreateError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTToprecUpdateError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTTransFunctionBad": {
            "message": {
            },
            "args": {
            },
        },
        "LDTTransFunctionNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTTypeMismatch": {
            "message": {
            },
            "args": {
            },
        },
        "LDTUniqueKeyError": {
            "message": {
            },
            "args": {
            },
        },
        "LDTUntransFunctionBad": {
            "message": {
            },
            "args": {
            },
        },
        "LDTUntransFunctionNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LDTUserModuleBad": {
            "message": {
            },
            "args": {
            },
        },
        "LDTUserModuleNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LargeItemNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "LuaFileNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "NamespaceNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "NoXDR": {
            "message": {
            },
            "args": {
            },
        },
        "NotAuthenticated": {
            "message": {
            },
            "args": {
            },
        },
        "ParamError": {
            "message": {
            },
            "args": {
            },
        },
        "QueryError": {
            "message": {
            },
            "args": {
            },
        },
        "QueryQueueFull": {
            "message": {
            },
            "args": {
            },
        },
        "QueryTimeout": {
            "message": {
            },
            "args": {
            },
        },
        "RecordBusy": {
            "message": {
            },
            "args": {
            },
        },
        "RecordError": {
            "message": {
            },
            "args": {
            },
        },
        "RecordExistsError": {
            "message": {
            },
            "args": {
            },
        },
        "RecordGenerationError": {
            "message": {
            },
            "args": {
            },
        },
        "RecordKeyMismatch": {
            "message": {
            },
            "args": {
            },
        },
        "RecordNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "RecordTooBig": {
            "message": {
            },
            "args": {
            },
        },
        "RoleExistsError": {
            "message": {
            },
            "args": {
            },
        },
        "RoleViolation": {
            "message": {
            },
            "args": {
            },
        },
        "SecurityNotEnabled": {
            "message": {
            },
            "args": {
            },
        },
        "SecurityNotSupported": {
            "message": {
            },
            "args": {
            },
        },
        "SecuritySchemeNotSupported": {
            "message": {
            },
            "args": {
            },
        },
        "ServerError": {
            "message": {
            },
            "args": {
            },
        },
        "ServerFull": {
            "message": {
            },
            "args": {
            },
        },
        "TimeoutError": {
            "message": {
            },
            "args": {
            },
        },
        "UDFError": {
            "message": {
            },
            "args": {
            },
        },
        "UDFNotFound": {
            "message": {
            },
            "args": {
            },
        },
        "UnsupportedFeature": {
            "message": {
            },
            "args": {
            },
        },
        "UserExistsError": {
            "message": {
            },
            "args": {
            },
        },
    },
    "llist": {
        "add": {
        },
        "add_many": {
        },
        "config": {
        },
        "destroy": {
        },
        "filter": {
        },
        "get": {
        },
        "remove": {
        },
        "size": {
        },
    },
    "lmap": {
        "config": {
        },
        "destroy": {
        },
        "filter": {
        },
        "get": {
        },
        "put": {
        },
        "put_many": {
        },
        "remove": {
        },
        "size": {
        },
    },
    "lset": {
        "add": {
        },
        "add_many": {
        },
        "config": {
        },
        "destroy": {
        },
        "exists": {
        },
        "filter": {
        },
        "get": {
        },
        "remove": {
        },
        "size": {
        },
    },
    "lstack": {
        "config": {
        },
        "destroy": {
        },
        "filter": {
        },
        "get_capacity": {
        },
        "peek": {
        },
        "push": {
        },
        "push_many": {
        },
        "set_capacity": {
        },
        "size": {
        },
    },
    "predicates": {
        "between": {
        },
        "contains": {
        },
        "equals": {
        },
        "range": {
        },
    },
    "set_deserializer": {
    },
    "set_log_handler": {
    },
    "set_log_level": {
    },
    "set_serializer": {
    },
}

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

def dir3():
    # dir1(aerospike)
    attrs1 = dir2(aerospike)
    print "attrs1 = %s" % str(attrs1)
    for e1 in attrs1:
        print "\naerospike.%s" % e1
        attr1 = getattr(aerospike, e1)
        if 'method' in str(type(attr1)):
            continue
        # dir1(attr1)
        attrs2 = dir2(attr1)
        print "  attrs2 = %s" % str(attrs2)
        for e2 in attrs2:
            print "\naerospike.%s.%s" % (e1, e2)
            attr2 = getattr(attr1, e2)
            if 'method' in str(type(attr2)):
                continue
            # dir1(attr2)
            attrs3 = dir2(attr2)
            print "  attrs3 = %s" % str(attrs3)
            for e3 in attrs3:
                print "\naerospike.%s.%s.%s" % (e1, e2, e3)
                attr3 = getattr(attr2, e3)
                if 'method' in str(type(attr3)):
                    continue
                # dir1(attr3)
                attrs4 = dir2(attr3)
                print "  attrs4 = %s" % str(attrs4)

def check(object, name, dict1, status):
    attrs1 = dir2(object)
    for e1 in attrs1:
        attr1 = getattr(object, e1)
        if e1 in dict1:
            if 'method' in str(type(attr1)):
                # print "need a test for %s.%s" % (name, e1)
                pass
            else:
                status = check(attr1, name + "." + e1, dict1[e1], status)
        else:
            print "need tests for %s.%s" % (name, e1)
            status = False
    return status

def main():
    status = check(aerospike, 'aerospike', elements, True)
    if status:
        print "tests are good"
    else:
        print "need some tests"

main()
