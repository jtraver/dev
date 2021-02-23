#!/usr/bin/env python3

from framework import do_exit, get_globals, main

def do_work():
    global g_test_import
    global globals1
    print("do_work")
    globals1 = get_globals()
    g_test_import = globals1["g_test_import"]
    print("do_work: g_test_import = %s" % str(g_test_import))


main(do_work)
