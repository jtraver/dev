#!/usr/bin/env python3
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
    print "sock = %s" % str(sock)
    print "sock = %s" % dir(sock)
# connected
# sock = <socket._socketobject object at 0x10dbe5b40>
# sock = ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_sock', 'accept', 'bind', 'close', 'connect', 'connect_ex', 'dup', 'family', 'fileno', 'getpeername', 'getsockname', 'getsockopt', 'gettimeout', 'listen', 'makefile', 'proto', 'recv', 'recv_into', 'recvfrom', 'recvfrom_into', 'send', 'sendall', 'sendto', 'setblocking', 'setsockopt', 'settimeout', 'shutdown', 'type']
except Exception, e:
    print "e = %s" % str(e)

if sock:
    sock.close()
else:
    print "no connection made"
