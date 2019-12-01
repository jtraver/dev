#!/usr/bin/env python3
#!/usr/bin/python3

import glob
import os
import re
import sys

# http://www.aerospike.com/docs/reference/serverlogmessages
# Occurs: Periodically displayed, every 10 seconds by default, for each namespace. Basic client transactions statistics. Will only be displayed after client transactions hit this namespace on this node.
client_transaction_statistics_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) \{(?P<namespace>\w+)\} client: tsvc \((?P<client_tsvc_error>\d+),(?P<client_tsvc_timeout>\d+)\) proxy \((?P<client_proxy_complete>\d+),(?P<client_proxy_error>\d+),(?P<client_proxy_timeout>\d+)\) read \((?P<client_read_success>\d+),(?P<client_read_error>\d+),(?P<client_read_timeout>\d+),(?P<client_read_not_found>\d+)\) write \((?P<client_write_success>\d+),(?P<client_write_error>\d+),(?P<client_write_timeout>\d+)\) delete \((?P<client_delete_success>\d+),(?P<client_delete_error>\d+),(?P<client_delete_timeout>\d+),(?P<client_delete_not_found>\d+)\) udf \((?P<client_udf_complete>\d+),(?P<client_udf_error>\d+),(?P<client_udf_timeout>\d+)\) lang \((?P<client_lang_read_success>\d+),(?P<client_lang_write_success>\d+),(?P<client_lang_delete_success>\d+),(?P<client_lang_error>\d+)\)(?P<remainder>.*)$')
# Occurs: Periodically displayed, every 10 seconds by default, for each namespace. Retransmit statistics. Will only be displayed if any retransmit has taken place.
client_retransmit_statistics_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) \{(?P<namespace>\w+)\} retransmits: migration (?P<migrate_record_retransmits>\d+) client-read (?P<retransmit_client_read_dup_res>\d+) client-write \((?P<retransmit_client_write_dup_res>\d+),(?P<retransmit_client_write_repl_write>\d+)\) client-delete \((?P<retransmit_client_delete_dup_res>\d+),(?P<retransmit_client_delete_repl_write>\d+)\) client-udf \((?P<retransmit_client_udf_dup_res>\d+),(?P<retransmit_client_udf_repl_write>\d+)\) batch-sub (?P<retransmit_batch_sub_dup_res>\d+) udf-sub \((?P<retransmit_udf_sub_dup_res>\d+),(?P<retransmit_udf_sub_repl_write>\d+)\) nsup (?P<retransmit_nsup_repl_write>\d+)(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1710031546/192.168.121.106/aerospike.log: 95 Oct 03 2017 11:46:32 GMT: INFO (demarshal): (socket.c:708) Started client endpoint 0.0.0.0:3000
client_started_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) Started client endpoint (?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+)(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1710031546/192.168.121.118/aerospike.log: 92 Oct 03 2017 21:55:10 GMT: INFO (demarshal): (socket.c:708) Started client endpoint [::]:3000
client_started_ipv6_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) Started client endpoint (?P<ip6>\[[^]]+\]):(?P<port>\d+)(?P<remainder>.*)$')
# Occurs: Periodically displayed, every 10 seconds by default. Aggregate across all namespaces. Will only be displayed if there has been any transaction that failed early on this node.
early_fail_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\)    early-fail: demarshal (?P<demarshal_error>\d+) tsvc-client (?P<early_tsvc_client_error>\d+) tsvc-batch-sub (?P<early_tsvc_batch_sub_error>\d+) tsvc-udf-sub (?P<early_tsvc_udf_sub_error>\d+)(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1710031546/192.168.121.104/aerospike.log: 117 Oct 03 2017 22:34:20 GMT: WARNING (hb): (hb.c:4688) heartbeat TLS client handshake with {192.168.121.105:3002} failed
warning_heartbeat_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) heartbeat TLS client handshake with \{(?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+)\} failed(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1706100155/192.168.121.106/aerospike.log: 215 Jun 09 2017 19:44:07 GMT: INFO (xdr): (xdr_ship.c:242) Failed to connect to cluster 'green', code -1: Failed to connect at /work/source/modules/ee/xdr/../modules/client/src/main/aerospike/as_cluster.c:228. Retrying.
xdr_failed_to_connect_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) Failed to connect to cluster (?P<message>.*) Retrying\.(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1710101756/192.168.121.106/aerospike.log: 117 Oct 10 2017 22:56:37 GMT: WARNING (info): (thr_info.c:4631) No network interface addresses detected for client access
warning_no_network_interface_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) No network interface addresses detected for client access(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1708032013/192.168.121.118/aerospike.log: 171 Aug 04 2017 01:02:05 GMT: WARNING (rw): (write.c:1785) {mem} write_master: failed as_bin_cdt_alloc_modify_from_client() <Digest>:0x25787da8870e615e92f2e71fca1c62c0c60eef90
warning_write_master_cdt_alloc_modify_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) \{(?P<namespace>\w+)\} write_master: failed as_bin_cdt_alloc_modify_from_client(?P<message>.*)(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1708032013/192.168.121.104/aerospike.log: 163 Aug 03 2017 22:33:37 GMT: WARNING (rw): (write.c:1831) {ssd} write_master: failed as_bin_cdt_read_from_client() <Digest>:0x25787da8870e615e92f2e71fca1c62c0c60eef90
warning_write_master_cdt_read_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) \{(?P<namespace>\w+)\} write_master: failed as_bin_cdt_read_from_client(?P<message>.*)(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1709082033/192.168.121.118/aerospike.log: 129 Sep 09 2017 03:23:16 GMT: INFO (as): (signal.c:214) call stack: frame 5: /usr/bin/asd(client_replica_maps_update+0x7e) [0x513d5a]
call_stack_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) call stack: frame (?P<message>.*)(?P<remainder>.*)$')
build_version_regex = re.compile(r'^(?P<junk>.*)(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) .* Aerospike (?P<edition>\w+) Edition build (?P<version>\d+\..*)  \<.*\>(?P<remainder>.*)$')
# /home/jtraver/logs/1706091307/192.168.121.104/aerospike.log: 134 Jun 09 2017 19:12:24 GMT: INFO (as): (as.c:410) <><><><><><><><><><>  Aerospike Enterprise Edition build 3.8.4.1  <><><><><><><><><><>
# WHAT? /home/jtraver/logs/1706091307/192.168.121.105/aerospike.log: 145 Jun 09 2017 19:43:56 GMT: INFO (as): (as.c:349) <><><><><><><><><><>  Aerospike Enterprise Edition build 3.13.0-20-g8842363  <><><><><><><><><><>
error_build_version_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) (?P<message>.*) Aerospike (?P<edition>\w+) Edition build (?P<version>\d+\..*) os (?P<os>[a-z0-9.]+)(?P<remainder>.*)$')
# WHAT? /home/jtraver/logs/1706091307/192.168.121.116/aerospike.log: 139 Jun 09 2017 19:20:47 GMT: WARNING (as): (signal.c:181) SIGSEGV received, aborting Aerospike Enterprise Edition build 3.8.4.1 os ubuntu14.04

def save_stat(node, key, value):
    new_max = False
    if not "stats" in node:
        node["stats"] = {}
    stats = node['stats']
    nname = node['name']
    if not key in stats:
        print(("new stat for %s %s %s" % (str(nname), str(key), str(value))))
        stats[key] = {}
        stats[key]["start"] = value
        stats[key]["max"] = value
        stats[key]["count"] = 1
        stats[key]["mcount"] = 1
    else:
        stats[key]["count"] += 1
        if value > stats[key]["max"]:
            new_max = True
            stats[key]["mcount"] += 1
            print(("new max %s started at %s %s %s > %s, count %s, mcount %s" % (str(nname), str(stats[key]["start"]), str(key), str(value), str(stats[key]["max"]), str(stats[key]["count"]), str(stats[key]["mcount"]))))
            stats[key]["max"] = value
            # print "node = %s" % str(node)
    return new_max

def get_value(s):
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    if s == "true":
        return True
    if s == "false":
        return False
    return s

def main():
    global nodes
    nodes = {}
    home1 = os.path.expanduser("~")
    logfiles = glob.glob(home1 + "/logs/*/*/*.log")
    for logfile in sorted(logfiles):
        print(("logfile %s" % logfile))
        grep1(logfile)

def grep1(filename):
    node = get_node(filename)
    version = None
    with open(filename) as f:
        for line in f:
            if "client" in line:
                line = line.strip()
                # print "%s: %s %s" % (str(filename), str(len(line)), str(line))
                parts1 = client_transaction_statistics_regex.match(line)
                #if parts1:
                #    dict1 = parts1.groupdict()
                #    print "  dict1 = %s" % str(dict1)
                #    for key in sorted(dict1.keys()):
                #        val = dict1[key]
                #        print "    %s %s" % (str(key), str(val))
                #    sys.exit(1)
                if not parts1:
                    parts1 = client_retransmit_statistics_regex.match(line)
                if not parts1:
                    parts1 = client_started_regex.match(line)
                if not parts1:
                    parts1 = early_fail_regex.match(line)
                if not parts1:
                    parts1 = client_started_ipv6_regex.match(line)
                if not parts1:
                    parts1 = warning_heartbeat_regex.match(line)
                if not parts1:
                    parts1 = xdr_failed_to_connect_regex.match(line)
                if not parts1:
                    parts1 = warning_no_network_interface_regex.match(line)
                if not parts1:
                    parts1 = warning_write_master_cdt_alloc_modify_regex.match(line)
                if not parts1:
                    parts1 = warning_write_master_cdt_read_regex.match(line)
                if not parts1:
                    parts1 = call_stack_regex.match(line)
                if not parts1:
                    print(("WHAT? %s: %s %s" % (str(filename), str(len(line)), str(line))))
                    sys.exit(1)
                dict1 = parts1.groupdict()
                if dict1['remainder']:
                    print(("  dict1 = %s" % str(dict1)))
                    for key in sorted(dict1.keys()):
                        val = dict1[key]
                        print(("    %s %s" % (str(key), str(val))))
                    sys.exit(1)
                for key in ["client_read_error", "client_read_not_found", "client_read_success", "client_read_timeout"]:
                    if key in dict1:
                        save_stat(node, key, get_value(dict1[key]))
                        #print "  dict1 = %s" % str(dict1)
                        #for key in sorted(dict1.keys()):
                        #    val = dict1[key]
                        #    print "    %s %s" % (str(key), str(val))
                        #sys.exit(1)
            elif "Edition build" in line:
                line = line.strip()
                # print "%s: %s %s" % (str(filename), str(len(line)), str(line))
                # sys.exit(1)
                parts1 = build_version_regex.match(line)
                if not parts1:
                    parts1 = error_build_version_regex.match(line)
                if not parts1:
                    print(("WHAT? %s: %s %s" % (str(filename), str(len(line)), str(line))))
                    sys.exit(1)
                dict1 = parts1.groupdict()
                if dict1['remainder']:
                    print(("  dict1 = %s" % str(dict1)))
                    for key in sorted(dict1.keys()):
                        val = dict1[key]
                        print(("    %s %s" % (str(key), str(val))))
                    sys.exit(1)
                version1 = dict1['version']
                if version != version1:
                    version = version1
                    print(("version %s edition %s" % (str(dict1['version']), str(dict1['edition']))))
                if 'message' in dict1:
                    print(("version %s edition %s %s os %s" % (str(dict1['version']), str(dict1['edition']), str(dict1['message']), str(dict1['os']))))

def get_node(filename):
    print(("get_node: filename = %s" % str(filename)))
# get_node: filename = /home/jtraver/logs/1706091307/192.168.121.104/aerospike.log
    parts = filename.split("/")
    #for indx in xrange(len(parts)):
    #    part = parts[indx]
    #    print "%s %s" % (str(indx), str(part))
    nname = parts[5]
    #print "node name is %s" % str(nname)
    if nname in nodes:
        return nodes[nname]
    node = { 'name': nname }
    nodes[nname] = node
    return node
    sys.stdout.flush()
    sys.exit(1)

main()
