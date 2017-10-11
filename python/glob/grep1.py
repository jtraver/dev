#!/usr/bin/python

import glob
import os
import re
import sys

# http://www.aerospike.com/docs/reference/serverlogmessages
# Occurs: Periodically displayed, every 10 seconds by default, for each namespace. Basic client transactions statistics. Will only be displayed after client transactions hit this namespace on this node.
client_transaction_statistics_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) \{(?P<namespace>\w+)\} client: tsvc \((?P<client_tsvc_error>\d+),(?P<client_tsvc_timeout>\d+)\) proxy \((?P<client_proxy_complete>\d+),(?P<client_proxy_error>\d+),(?P<client_proxy_timeout>\d+)\) read \((?P<client_read_success>\d+),(?P<client_read_error>\d+),(?P<client_read_timeout>\d+),(?P<client_read_not_found>\d+)\) write \((?P<client_write_success>\d+),(?P<client_write_error>\d),(?P<client_write_timeout>\d+)\) delete \((?P<client_delete_success>\d+),(?P<client_delete_error>\d+),(?P<client_delete_timeout>\d+),(?P<client_delete_not_found>\d+)\) udf \((?P<client_udf_complete>\d+),(?P<client_udf_error>\d+),(?P<client_udf_timeout>\d+)\) lang \((?P<client_lang_read_success>\d+),(?P<client_lang_write_success>\d+),(?P<client_lang_delete_success>\d+),(?P<client_lang_error>\d+)\)(?P<remainder>.*)$')
# Occurs: Periodically displayed, every 10 seconds by default, for each namespace. Retransmit statistics. Will only be displayed if any retransmit has taken place.
client_retransmit_statistics_regex = re.compile(r'^(?P<month>\w+) (?P<day>\d+) (?P<year>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<timezone>\w+): (?P<severity>\w+) \((?P<context>\w+)\): \((?P<sourcefile>\w+\.\w+):(?P<sourceline>\d+)\) \{(?P<namespace>\w+)\} retransmits: migration (?P<migrate_record_retransmits>\d+) client-read (?P<retransmit_client_read_dup_res>\d+) client-write \((?P<retransmit_client_write_dup_res>\d+),(?P<retransmit_client_write_repl_write>\d+)\) client-delete \((?P<retransmit_client_delete_dup_res>\d+),(?P<retransmit_client_delete_repl_write>\d+)(?P<remainder>.*)$')
    # remainder ) client-udf (0,0) batch-sub 0 udf-sub (0,0) nsup 0

def main():
    home1 = os.path.expanduser("~")
    logfiles = glob.glob(home1 + "/logs/*/*/*.log")
    for logfile in logfiles:
        print "logfile %s" % logfile
        grep1(logfile)

def grep1(filename):
    with open(filename) as f:
        for line in f:
            if "client" in line:
                line = line.strip()
                print "%s: %s %s" % (str(filename), str(len(line)), str(line))
                parts1 = client_transaction_statistics_regex.match(line)
                if not parts1:
                    parts1 = client_retransmit_statistics_regex.match(line)
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
