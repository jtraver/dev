#!/usr/bin/python

def main():
    year = 60.0 * 60.0 * 24.0 * 365.0
    up = year * 0.99999
    down = year - up
    print "year = %s" % str(year)
    print "up = %s" % str(up)
    print "down = %s" % str(down)

main()
