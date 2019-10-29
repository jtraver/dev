#!/usr/bin/env python3
#!/usr/bin/python

import optparse

def main():
    optparser = optparse.OptionParser()
    optparser.add_option("--verbose", action="store_true", default=False)
    (options, args) = optparser.parse_args()
    print "options = %s" % str(options)
    print "args = %s" % str(args)

main()
