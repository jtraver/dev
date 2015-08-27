#!/usr/bin/python

import socket
import struct

sock = None

def receivedata(sock, sz):
    pos = 0
    while pos < sz:
        chunk = sock.recv(sz - pos)
        if pos == 0:
            data = chunk
        else:
            data += chunk
        pos += len(chunk)
    return data

def readData(sock):
    # print "---------------------------------------------------------------------------------"
    # print "getting header data"
    header_data = sock.recv(8)
    # print "header_data = %s" % str(header_data)
    rv = struct.unpack('! Q', header_data)
    # print "rv = %s" % str(rv)
    version = (rv[0] >> 56) & 0xff
    # print "version = %s" % str(version)
    proto_type = (rv[0] >> 48) & 0xff
    # print "proto_type = %s" % str(proto_type)
    sz = (rv[0] & 0xFFFFFFFFFFFF)
    # print "sz = %s" % str(sz)
    if sz > 0:
        body_data = receivedata(sock, sz)
        # print "body_data = %s" % str(body_data)
        return (version, proto_type, sz, body_data)
    elif sz == 0:
        print "no data to get"
    else:
        print "ERROR: negative data size: %s" % str(sz)
    return (version, proto_type, sz, None)

# http://www.aerospike.com/docs/reference/wire-protocol/
# Example Info Message Names and Values
# name    value(s)
# yes # build   server build version, e.g., "3.5.14"
# yes # edition server edition, e.g., "Aerospike Enterprise Edition"
# yes # node    unique string representing this node's ID as a 64-bit hexadecimal number, e.g., "BB9E68F98290C00"
# no  # replicas-read   list of read replicas hosted by this node, represented as a list with entries of the form: <Namespace>:<PartitionID>;
# no  # replicas-write  list of write replicas hosted by this node, represented as a list with entries of the form: <Namespace>:<PartitionID>;
# no  # service this node's <IPAddress>:<TCPPort> where it listens for Aerospike protocol message transactions
# yes # services    semicolon-delimited list of service address and port pairs where the other nodes in this cluster can be found
# yes # statistics  semicolon-delimited list of statistics regarding this node's current state
# yes # version full server edition and build version, e.g., "Aerospike Community Edition build 3.5.14"
# features, node, edition, build, version, partition-generation, cluster-generation, statistics, services-alumni, services

def check_node(sock):
    info = {}
    # 0   version 1   current protocol version is 2
    # 1   type    1   current defined message types are: 1 ("Aerospike Info") and 3 ("Aerospike Message")
    # 2   sz  6   number (in network byte order) of bytes in this message to follow this header
    # send version 2 Aerospike Info request with no message at all
    protocol_header_data = (2 << 56) | (1 << 48) | 0
    # ! - network byte order
    # Q - 8 bytes -> version (1 byte), type (1 byte), size (6 bytes)
    buf = struct.pack("! Q", protocol_header_data)
    sock.send(buf)
    (version, ptype, size, bdata) = readData(sock)
    if version != 2:
        print "ERROR: expected version 2 but found %d" % version
    proto = {
        'version': version,
        'type': ptype,
        'data size': size,
    }
    info['proto'] = proto
    # print "check_node: version = %s" % str(version)
    # print "check_node: ptype = %s" % str(ptype)
    # print "check_node: size = %s" % str(size)
    # print "check_node: bdata = %s" % str(bdata)
    data = {}
    if bdata:
        # just all string data for this request; no binary stuff to worry about in this one
        (sdata,) = struct.unpack("! %ds" % size, bdata)
        # print "check_node: sdata = %s" % str(sdata)
        lines = sdata.split('\n');
        for line in lines:
            if line == '':
                continue
            # print "  %s" % str(line)
            kv1 = line.split('\t');
            if len(kv1) != 2:
                print "what line is this: %s" % str(line)
            else:
                k1 = kv1[0]
                v1 = kv1[1]
                # print "    %s" % str(k1)
                # print "    %s" % str(v1)
                if k1 == 'features':
                    data[k1] = v1.split(';')
                elif k1 == 'node' or k1 == 'edition' or k1 == 'build' or k1 == 'version' or k1 == 'partition-generation' or k1 == 'cluster-generation':
                    data[k1] = v1
                elif k1 == 'statistics':
                    statistics = {}
                    # print "stats %s" % str(v1)
                    stats = v1.split(';')
                    for stat in stats:
                        # batch_index_queue 0:0,0:0,0:0,0:0
                        kv1 = stat.split('=')
                        if len(kv1) == 2:
                            statistics[kv1[0]] = kv1[1]
                        else:
                            print "ERROR: %s in %s", (str(stat), str(v1))
                    data[k1] = statistics
                elif k1 == 'services-alumni' or k1 == 'services':
                    services = {}
                    hosts = v1.split(';')
                    for hostport in hosts:
                        hp = hostport.split(':')
                        if len(hp) == 2:
                            services[hp[0]] = hp[1]
                        else:
                            print "ERROR: %s in %s" % (str(hp), str(v1))
                        
                    data[k1] = services
                else:
                    print "what is key is this: %s" % str(k1)
                    print "    %s" % str(v1)
                    data[k1] = v1
    else:
        print "ERROR: found no data"
    info['data'] = data
    return info


def main():
    try:
        host = '192.168.75.246'
        port = 3000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((host, int(port)))
        print "connected"
        # print "sock = %s" % str(sock)
        # print "sock = %s" % dir(sock)
        # connected
        # sock = <socket._socketobject object at 0x10dbe5b40>
        # sock = ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_sock', 'accept', 'bind', 'close', 'connect', 'connect_ex', 'dup', 'family', 'fileno', 'getpeername', 'getsockname', 'getsockopt', 'gettimeout', 'listen', 'makefile', 'proto', 'recv', 'recv_into', 'recvfrom', 'recvfrom_into', 'send', 'sendall', 'sendto', 'setblocking', 'setsockopt', 'settimeout', 'shutdown', 'type']
        info = check_node(sock)
        # print "info = %s" % str(info)
        proto = info['proto']
        data = info['data']
        if data:
            print "data"
            if 'statistics' in data:
                print "  statistics"
                for k,v in sorted(data['statistics'].items()):
                    print "    %s %s" % (str(k), str(v))
            print "  features = %s" % str(data['features'])
            print "  node = %s" % str(data['node'])
            print "  edition = %s" % str(data['edition'])
            print "  build = %s" % str(data['build'])
            print "  version = %s" % str(data['version'])
            print "  partition-generation = %s" % str(data['partition-generation'])
            print "  cluster-generation = %s" % str(data['cluster-generation'])
            if 'services' in data:
                print "  services"
                for k,v in data['services'].items():
                    print "    %s %s" % (str(k), str(v))
            if 'services-alumni' in data:
                print "  services-alumni"
                for k,v in data['services-alumni'].items():
                    print "    %s %s" % (str(k), str(v))
        print "proto = %s" % str(proto)
    except Exception, e:
        print "e = %s" % str(e)
    if sock:
        sock.close()
    else:
        print "no connection made"

main()
