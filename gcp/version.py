#!/usr/bin/env python

import aerospike

host = "127.0.0.1"
port = 3000
config = {'hosts': [(host, port)]}
client1 = aerospike.client(config).connect()
version = client1.info('version')
print "version = %s" % str(version)
