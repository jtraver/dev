#!/usr/bin/python

import socket

sock = None

try:
    host = '192.168.75.246'
    port = 3000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    sock.connect((host, int(port)))
    print "connected"
except Exception, e:
    print "e = %s" % str(e)

if sock:
    sock.close()
else:
    print "no connection made"
