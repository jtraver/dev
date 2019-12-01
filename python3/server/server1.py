#!/usr/bin/env python3

# example server from https://stackoverflow.com/questions/34371096/how-to-use-python-socket-settimeout-properly

import socket
import sys
fragments = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO s.bind(("192.168.1.4",9001))
s.listen(5)
while True:
    c,a = s.accept()
    c.settimeout(10.0)
    print("Someone came in Server from %s and port %s" %(a[0],a[1]))
    c.send("Welcome to system")
    while True:
        chunk = c.recv(2048)
        if not chunk.strip():
            break
        else:
            fragments.append(chunk)
            continue
    combiner = "".join(fragments)
    print(combiner)
    shutdown = str(input("Wanna Quit(Y/y) or (N/n): "))
    if shutdown == 'Y' or shutdown == 'y':
        c.close()
        sys.exit()
    else:
        continue
