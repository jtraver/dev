#!/usr/bin/env python3

import datetime
import os
import sys
import time

def get_globals():
    globals1 = {}
    globals1["g_test_import"] = g_test_import
    return globals1

def do_init():
    print("def do_init():")
    sys.stdout.flush()
    sys.stderr.write("stderr do_init\n")
    global aliases
    global confref
    global VT100_BOLD
    global VT100_RED
    global VT100_GREEN
    global VT100_STOP_MARKUP
    global program_name
    global test_id
    global g_starttime
    global userhome
    global clusters
    global user
    global password
    global pyclient
    global ppclient
    global ppclients
    global retries
    global sleep_time
    global g_namespaces
    global g_has_correct_scan
    global g_nodeips
    global g_nodeids
    global g_test_import
    g_test_import = "framework imported"
    g_nodeips = None
    g_nodeids = None
    VT100_BOLD = "[0;1m"
    VT100_RED = "[0;1;31m"
    VT100_GREEN = "[0;1;32m"
    VT100_YELLOW = "[0;1;33m"
    VT100_BLUE = "[0;1;34m"
    VT100_STOP_MARKUP = "[0m"
    POLL_CONNECT_SLEEP_TIME = 3
    POLL_CONNECT_RETRIES = 300
    VERBOSE = False
    TEST_RUN_TIME_LIMIT = 300
    # DEFAULT_TIMEOUT = 1000.0   # 1000 second socket timeout
    # DEFAULT_TIMEOUT = 100.0   # 100 second socket timeout
    DEFAULT_TIMEOUT = 10.0   # 10 second socket timeout
    EXPRESSION_VERSION_52 = "5.2"
    EXPRESSION_VERSION_55 = "5.5"
    EXPRESSION_VERSION_56 = "5.6"
    confref = None
    g_starttime = time.time()
    d = datetime.datetime.now()
    test_id = d.strftime("%y%m%d%H%M%S%f")
    program_name = sys.argv[0]
    print("STARTING %s with test_id = %s" % (str(program_name), str(test_id)))
    if sys.stdout.isatty():
        print("is a tty")
    else:
        print("is a not tty")
        VT100_BOLD = ""
        VT100_RED = ""
        VT100_GREEN = ""
        VT100_STOP_MARKUP = ""
    userhome = os.path.expanduser("~")
    user = None

def do_exit(ret1):
    print("\ndef do_exit(ret1):")
    sys.stdout.flush()
    ret1 = 0
    if ret1:
        sys.stderr.write("stderr %sFAIL %s %s %s%s\n" % (VT100_RED, str(program_name), str(test_id), str(ret1), VT100_STOP_MARKUP))
        print("%sFAIL %s%s" % (VT100_RED, str(ret1), VT100_STOP_MARKUP))
    else:
        sys.stderr.write("stderr %sPASS %s %s%s\n" % (VT100_GREEN, str(program_name), str(test_id), VT100_STOP_MARKUP))
        print("%sPASS%s" % (VT100_GREEN, VT100_STOP_MARKUP))
    now = time.time()
    dur = now - g_starttime
    print("DONE %s test %s took %s seconds" % (str(program_name), str(test_id), str(dur)))
    sys.stdout.flush()
    sys.stderr.write("stderr \n")
    sys.stderr.write("stderr ")
    sys.stderr.write("stderr \n")
    sys.stderr.write("stderr DONE %s test %s took %s seconds\n" % (str(program_name), str(test_id), str(dur)))
    sys.stderr.write("stderr \n")
    sys.stderr.write("stderr ")
    sys.stderr.write("stderr \n")
    sys.exit(ret1)

def main(do_work):
    do_init()
    ret1 = do_work()
    do_exit(ret1)

# main()
# print("")
