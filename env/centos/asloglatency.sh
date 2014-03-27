sudo asloglatency -l /var/log/aerospike/aerospike.log

# # sudo asloglatency -h writes_master
# sudo asloglatency --help
# 
# Usage:
#  -l log file
#     default: /var/log/aerospike/aerospike.log
#  -h histogram name
#     MANDATORY - NO DEFAULT
#     e.g. 'reads nonet'
#  -t analysis slice interval
#     default: 10
#     other e.g. 3600 or 1:00:00
#  -f log time from which to analyze
#     default: tail
#     other e.g. head or 'Sep 22 2011 22:40:14' or -3600 or -1:00:00
#  -d maximum duration for which to analyze
#     default: not set
#     e.g. 3600 or 1:00:00
#  -n number of buckets to display
#     default: 3
#  -e show 0-th then every n-th bucket
#     default: 3
#  -r (roll until user hits return key or ctrl-c)
#     default: set if -f tail, otherwise not set
