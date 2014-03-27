# [jtraver@localhost centos]$ asmonitor --help
# 
# Enter help for help
# 
# option --help not recognized
# Usage:
#  -c monitor.conf             Optional. Location of configuration file. Default is filename
#  -e 'Command'            Optional. eg1: '-e info' execute the info command in the shell. eg2: '-e help' show the shell help text
#  -h hostip:port          Optional. Connection info of the host(s). Must be in the 127.0.0.1 or 127.0.0.1:3000 format. Comma separated for multi hosts
#  -p default_port             Optional. Default host port number. If missing, 3000 is assumed
#  -d monitordirectory      Optional. Defaults to users home directory
#  -u                      Print out this usage text
#  
#  The '[main]' section in configuration file (default is filename, auto generated after the first asmonitor invocation):
#       hosts = Seed-HostIP:port or List of HostIP:port's (comma separated, each in format of 127.0.0.1:3000)
#       namespaces = List of namespaces (auto generated. user should not edit)
#       crawl = True Find all nodes in cluster- Works only with internal IPs
#       xdr = False. Disabled by default. To enable'xdr=True'
#       xdrport=xdr monitor port
#  Note the configuration file is auto updated after each run
# 
asmonitor -h 192.168.75.206:3000,192.168.75.205:3000,192.168.75.213:3000,192.168.75.215:3000
