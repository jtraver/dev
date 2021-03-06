#!/usr/bin/python

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

def main():
    home1 = os.path.expanduser("~")
    logfiles = glob.glob(home1 + "/logs/*/*/*.log")
    for logfile in sorted(logfiles):
        print "logfile %s" % logfile
        grep1(logfile)

def grep1(filename):
    with open(filename) as f:
        for line in f:
            if "client" in line:
                line = line.strip()
                # print "%s: %s %s" % (str(filename), str(len(line)), str(line))
                parts1 = client_transaction_statistics_regex.match(line)
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
                    print "WHAT? %s: %s %s" % (str(filename), str(len(line)), str(line))
                    sys.exit(1)
                dict1 = parts1.groupdict()
                if dict1['remainder']:
                    print "  dict1 = %s" % str(dict1)
                    for key in sorted(dict1.keys()):
                        val = dict1[key]
                        print "    %s %s" % (str(key), str(val))
                    sys.exit(1)


main()
