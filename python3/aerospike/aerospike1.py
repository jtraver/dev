#!/usr/bin/env python3
#!/usr/bin/python3

import apihelper
import aerospike
import aerospike_helpers
import aerospike_helpers.operations
from aerospike_helpers.operations import operations


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
        "has_geo": {
        },
        "increment": {
        },
        "index_geo2dsphere_create": {
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
        "info_all": {
        },
        "info_node": {
        },
        "is_connected": {
        },
        "job_info": {
        },
        "key": {
        },
        "list_append": {
        },
        "list_clear": {
        },
        "list_extend": {
        },
        "list_get": {
        },
        "list_get_range": {
        },
        "list_insert": {
        },
        "list_insert_items": {
        },
        "list_pop": {
        },
        "list_pop_range": {
        },
        "list_remove": {
        },
        "list_remove_range": {
        },
        "list_set": {
        },
        "list_size": {
        },
        "list_trim": {
        },
        "llist": {
        },
        "lmap": {
        },
        "lset": {
        },
        "lstack": {
        },
        "map_clear": {
        },
        "map_decrement": {
        },
        "map_get_by_index": {
        },
        "map_get_by_index_range": {
        },
        "map_get_by_key": {
        },
        "map_get_by_key_list": {
        },
        "map_get_by_key_range": {
        },
        "map_get_by_rank": {
        },
        "map_get_by_rank_range": {
        },
        "map_get_by_value": {
        },
        "map_get_by_value_list": {
        },
        "map_get_by_value_range": {
        },
        "map_increment": {
        },
        "map_put": {
        },
        "map_put_items": {
        },
        "map_remove_by_index": {
        },
        "map_remove_by_index_range": {
        },
        "map_remove_by_key": {
        },
        "map_remove_by_key_list": {
        },
        "map_remove_by_key_range": {
        },
        "map_remove_by_rank": {
        },
        "map_remove_by_rank_range": {
        },
        "map_remove_by_value": {
        },
        "map_remove_by_value_list": {
        },
        "map_remove_by_value_range": {
        },
        "map_set_policy": {
        },
        "map_size": {
        },
        "operate": {
        },
        "operate_ordered": {
        },
        "prepend": {
        },
        "put": {
        },
        "query": {
        },
        "query_apply": {
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
        "shm_key": {
        },
        "touch": {
        },
        "truncate": {
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
    "GeoJSON": {
        "dumps": {
        },
        "geo_data": {
        },
        "loads": {
        },
        "unwrap": {
        },
        "wrap": {
        },
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
        "predexp": {
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
    "calc_digest": {
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
        "AlwaysForbidden": {
            "message": {
            },
            "args": {
            },
        },
        "AsyncConnectionError": {
            "message": {
            },
            "args": {
            },
        },
        "BatchDisabledError": {
            "message": {
            },
            "args": {
            },
        },
        "BatchMaxRequestError": {
            "message": {
            },
            "args": {
            },
        },
        "BatchQueueFullError": {
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
        "ClientAbortError": {
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
        "ConnectionError": {
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
        "ElementExistsError": {
            "message": {
            },
            "args": {
            },
        },
        "ElementNotFoundError": {
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
        "InvalidGeoJSON": {
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
        "InvalidNodeError": {
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
        "NoMoreConnectionsError": {
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
        "QueryAbortedError": {
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
        "ScanAbortedError": {
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
        "TLSError": {
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
    "geodata": {
    },
    "geojson": {
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
        "find_first": {
        },
        "find_first_filter": {
        },
        "find_from": {
        },
        "find_from_filter": {
        },
        "find_last": {
        },
        "find_last_filter": {
        },
        "get": {
        },
        "range_limit": {
        },
        "remove": {
        },
        "set_page_size": {
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
    "null": {
    },
    "predexp": {
        "geojson_bin": {
        },
        "geojson_contains": {
        },
        "geojson_value": {
        },
        "geojson_var": {
        },
        "geojson_within": {
        },
        "integer_bin": {
        },
        "integer_equal": {
        },
        "integer_greater": {
        },
        "integer_greatereq": {
        },
        "integer_less": {
        },
        "integer_lesseq": {
        },
        "integer_unequal": {
        },
        "integer_value": {
        },
        "integer_var": {
        },
        "list_bin": {
        },
        "list_iterate_and": {
        },
        "list_iterate_or": {
        },
        "map_bin": {
        },
        "mapkey_iterate_and": {
        },
        "mapkey_iterate_or": {
        },
        "mapval_iterate_and": {
        },
        "mapval_iterate_or": {
        },
        "predexp_and": {
        },
        "predexp_not": {
        },
        "predexp_or": {
        },
        "rec_device_size": {
        },
        "rec_digest_modulo": {
        },
        "rec_last_update": {
        },
        "rec_void_time": {
        },
        "string_bin": {
        },
        "string_equal": {
        },
        "string_regex": {
        },
        "string_unequal": {
        },
        "string_value": {
        },
        "string_var": {
        },
    },
    "predicates": {
        "between": {
        },
        "contains": {
        },
        "equals": {
        },
        "geo_contains_geojson_point": {
        },
        "geo_contains_point": {
        },
        "geo_within_geojson_region": {
        },
        "geo_within_radius": {
        },
        "geo_within": {
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
    "unset_serializers": {
    },
}


def pinfo(object):
    print()
    print("--------------------------------------------------------------------------------")
    print(("| %s" % str(object)))
    print("--------------------------------------------------------------------------------")
    apihelper.info(object)
    # print "aerospike = %s" % str(aerospike)
    # print "aerospike = %s" % dir(aerospike)
    # print "aerospike = %s" % type(aerospike)

    # print "--------------------------------------------------------------------------------"
    # print "| aerospike.Client"
    # print "--------------------------------------------------------------------------------"
    # apihelper.info(aerospike.Client)


def info(object, level=1):
    if level > 3:
        return
    print("\n")
    print("--------------------------------------------------------------------------------")
    print(("object = %s" % str(object)))
    try:
        for e in dir(object):
            attr = getattr(object, e)
            if callable(attr):
                print(("  e = %s" % e))
                print(("    attr = %s" % str(attr)))
                print(("    attr = %s" % type(attr)))
                # print "    attr = %s" % dir(attr)
                try:
                    attr()
                except Exception as ex1:
                    print(("      1 exception is %s" % str(ex1)))
                # if type(attr) != int:
                if not "__" in str(e):
                    info(attr, level + 1)
    except Exception as ex2:
        print(("      2 exception is %s" % str(ex2)))


def info2(object):
    str1 = str(object)
    if str1 in found:
        return
    # if "<method" in str1 and "aerospike" in str1 and not "__" in str1:
    if "aerospike" in str1 and not "__" in str1:
        print(("%s" % str1))
        if "<method" in str1:
            found[str1] = object
        try:
            for e in dir(object):
                attr = getattr(object, e)
                info2(attr)
        except Exception as ex2:
            pass

# info(aerospike)


def do_info2():
    info2(aerospike)

    print("\n")
    count = 0
    for k, e in list(found.items()):
        if callable(e):
            count += 1
            print(("%s %s" % (str(count), k)))
            try:
                e()
            except Exception as ex:
                print(("    %s" % str(ex)))


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
    print("\n")
    print(("object = %s" % dir(object)))
    for e in dir(object):
        if '__' in e:
            continue
        attr = getattr(object, e)
        # if 'builtin_function_or_method' in str(type(attr)) or type(attr) ==
        # int or type(attr) == str or 'NoneType' in str(type(attr)):
        if type(attr) == int or type(attr) == str or 'NoneType' in str(type(attr)):
            continue
        print(("e = %s" % str(e)))
        # e is just a string
        # print "  type e = %s" % type(e)
        # print "  dir e = %s" % dir(e)
        print(("  type attr = %s" % type(attr)))
        # print "    dir attr = %s" % dir(attr)


def dir3():
    # dir1(aerospike)
    attrs1 = do_dir(aerospike)
    print(("attrs1 = %s" % str(attrs1)))
    for e1 in attrs1:
        print(("\naerospike.%s" % e1))
        attr1 = getattr(aerospike, e1)
        if 'method' in str(type(attr1)):
            continue
        # dir1(attr1)
        attrs2 = do_dir(attr1)
        print(("  attrs2 = %s" % str(attrs2)))
        for e2 in attrs2:
            print(("\naerospike.%s.%s" % (e1, e2)))
            attr2 = getattr(attr1, e2)
            if 'method' in str(type(attr2)):
                continue
            # dir1(attr2)
            attrs3 = do_dir(attr2)
            print(("  attrs3 = %s" % str(attrs3)))
            for e3 in attrs3:
                print(("\naerospike.%s.%s.%s" % (e1, e2, e3)))
                attr3 = getattr(attr2, e3)
                if 'method' in str(type(attr3)):
                    continue
                # dir1(attr3)
                attrs4 = do_dir(attr3)
                print(("  attrs4 = %s" % str(attrs4)))


def do_dir(object):
    attrs = []
    for e in dir(object):
        print("do_dir: e = %s" % str(e))
        #if '__' in e:
        #    continue
        attr = getattr(object, e)
        if type(attr) == int or type(attr) == str or 'NoneType' in str(type(attr)):
            continue
        attrs.append(e)
    return attrs


def check(object, name, dict1, status):
    attrs1 = do_dir(object)
    print("  check: attrs1 = %s" % str(attrs1))
    for e1 in attrs1:
        print("  check: e1 = %s" % str(e1))
        attr1 = getattr(object, e1)
        if e1 in dict1:
            if 'method' in str(type(attr1)):
                print("need a test for %s.%s" % (name, e1))
                pass
            else:
                status = check(attr1, name + "." + e1, dict1[e1], status)
        else:
            print(("need tests for %s.%s" % (name, e1)))
            print("  e1 = %s" % dir(e1))
            status = False
    return status


def main():
    if '__version__' in dir(aerospike):
        print(("Python client version is %s" % aerospike.__version__))
    status = check(aerospike, 'aerospike', elements, True)
    print("\naerospike_helpers check")
    status = check(aerospike_helpers, 'aerospike_helpers', elements, True)

    print("\naerospike_helpers.operations check")
    status = check(aerospike_helpers.operations, 'aerospike_helpers.operations', elements, True)

    print("\noperations check")
    status = check(operations, 'operations', elements, True)

    if status:
        print("tests are good")
    else:
        print("need some tests")

main()
