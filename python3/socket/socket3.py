#!/usr/local/bin/python3.7

#!/usr/bin/env python3

# https://www.pythonforbeginners.com/code-snippets-source-code/dns-lookup-python

import socket

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')

print(addr1, addr2)
