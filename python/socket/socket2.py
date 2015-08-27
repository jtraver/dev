#!/usr/bin/python

import socket
import struct

sock = None

def readData(sock):
    status = 0
    while status == 0:
        header_data = sock.recv(8)
        print "header_data = %s" % str(header_data)
        rv = struct.unpack('! Q', header_data)
        print "rv = %s" % str(rv)
        version = (rv[0] >> 56) & 0xff
        print "version = %s" % str(version)
        proto_type = (rv[0] >> 48) & 0xff
        print "proto_type = %s" % str(proto_type)
        sz = (rv[0] & 0xFFFFFFFFFFFF)
        print "sz = %s" % str(sz)
        if sz > 0:
            body_data = sock.recv(sz)
            print "body_data = %s" % str(body_data)
        else:
            break


try:
    host = '192.168.75.246'
    port = 3000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    sock.connect((host, int(port)))
    print "connected"
    print "sock = %s" % str(sock)
    print "sock = %s" % dir(sock)
# connected
# sock = <socket._socketobject object at 0x10dbe5b40>
# sock = ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_sock', 'accept', 'bind', 'close', 'connect', 'connect_ex', 'dup', 'family', 'fileno', 'getpeername', 'getsockname', 'getsockopt', 'gettimeout', 'listen', 'makefile', 'proto', 'recv', 'recv_into', 'recvfrom', 'recvfrom_into', 'send', 'sendall', 'sendto', 'setblocking', 'setsockopt', 'settimeout', 'shutdown', 'type']

# 0   version 1   current protocol version is 2
# 1   type    1   current defined message types are: 1 ("Aerospike Info") and 3 ("Aerospike Message")
# 2   sz  6   number (in network byte order) of bytes in this message to follow this header

    # send version 2 Aerospike Info request with no message at all
    protocol_header_data = (2 << 56) | (1 << 48) | 0
    buf = struct.pack("! Q", protocol_header_data)
    sock.send(buf)
    readData(sock)

except Exception, e:
    print "e = %s" % str(e)

if sock:
    sock.close()
else:
    print "no connection made"
