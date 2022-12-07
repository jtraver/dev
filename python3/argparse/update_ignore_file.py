#!/usr/bin/env python3

import argparse
import os
import sys
import yaml

def main():
    print("main")
    parser = argparse.ArgumentParser()
    defaultCompose='../../../../../../compose.yml' # expect to run from repo in a test run
    parser.add_argument('-f', '--composeFile', help='compose.yml file from test-runner run', default=defaultCompose)
    args = parser.parse_args()
    print("main: args = %s" % str(args))
    composeFile = defaultCompose
    if args.composeFile == defaultCompose:
        print("using default compose file %s" % str(defaultCompose))
    else:
        print("using non-default compose file %s" % str(args.composeFile))
        composeFile = args.composeFile
    if os.path.exists(composeFile):
        print("found compose file %s" % str(composeFile))
    else:
        print("FAIL did not find compose file %s" % str(composeFile))
        # print("FAIL parser = %s" % str(parser))
        parser.print_help()
        sys.exit(1)
    basename = os.path.basename(composeFile)
    print("basename %s" % str(basename))
    dirname = os.path.dirname(composeFile)
    print("dirname %s" % str(dirname))

main()
