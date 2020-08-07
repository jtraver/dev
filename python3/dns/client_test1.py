#!/usr/local/bin/python3.7

# https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm

import dnspython as dns
import dns.resolver

result = dns.resolver.query('tutorialspoint.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())# 
