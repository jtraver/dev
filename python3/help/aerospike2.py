#!/usr/bin/env python3
#!/usr/bin/python

import apihelper
import aerospike

if '__version__' in dir(aerospike):
    print(("Python client version is %s" % aerospike.__version__))

print("---------------------------------------------------------------------------------")
print("aerospike")
apihelper.info(aerospike)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.Client")
apihelper.info(aerospike.Client)


print()
print("---------------------------------------------------------------------------------")
print("aerospike.GeoJSON")
apihelper.info(aerospike.GeoJSON)


# print
# print "---------------------------------------------------------------------------------"
# print "aerospike.Key"
# apihelper.info(aerospike.Key)


print()
print("---------------------------------------------------------------------------------")
print("aerospike.Query")
apihelper.info(aerospike.Query)


print()
print("---------------------------------------------------------------------------------")
print("aerospike.Scan")
apihelper.info(aerospike.Scan)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.calc_digest")
apihelper.info(aerospike.calc_digest)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.client")
apihelper.info(aerospike.client)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.exception")
apihelper.info(aerospike.exception)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.geodata")
apihelper.info(aerospike.geodata)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.geojson")
apihelper.info(aerospike.geojson)

try:
    print()
    print("---------------------------------------------------------------------------------")
    print("aerospike.llist")
    apihelper.info(aerospike.llist)
except Exception as e:
    print(("e = %s" % str(e)))
    print(("e = %s" % str(type(e))))

# print
# print "---------------------------------------------------------------------------------"
# print "aerospike.lmap"
# apihelper.info(aerospike.lmap)

# print
# print "---------------------------------------------------------------------------------"
# print "aerospike.lset"
# apihelper.info(aerospike.lset)

# print
# print "---------------------------------------------------------------------------------"
# print "aerospike.lstack"
# apihelper.info(aerospike.lstack)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.null")
apihelper.info(aerospike.null)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.predicates")
apihelper.info(aerospike.predicates)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.set_deserializer")
apihelper.info(aerospike.set_deserializer)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.set_log_handler")
apihelper.info(aerospike.set_log_handler)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.set_log_level")
apihelper.info(aerospike.set_log_level)

print()
print("---------------------------------------------------------------------------------")
print("aerospike.set_serializer")
apihelper.info(aerospike.set_serializer)

# print
# print "---------------------------------------------------------------------------------"
# print "aerospike.unset_serializer"
# apihelper.info(aerospike.unset_serializer)
