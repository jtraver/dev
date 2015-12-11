#!/usr/bin/python

import apihelper
import aerospike

print "---------------------------------------------------------------------------------"
print "aerospike"
apihelper.info(aerospike)

print
print "---------------------------------------------------------------------------------"
print "aerospike.Client"
apihelper.info(aerospike.Client)


print
print "---------------------------------------------------------------------------------"
print "aerospike.GeoJSON"
apihelper.info(aerospike.GeoJSON)


print
print "---------------------------------------------------------------------------------"
print "aerospike.Key"
apihelper.info(aerospike.Key)


print
print "---------------------------------------------------------------------------------"
print "aerospike.Query"
apihelper.info(aerospike.Query)


print
print "---------------------------------------------------------------------------------"
print "aerospike.Scan"
apihelper.info(aerospike.Scan)
