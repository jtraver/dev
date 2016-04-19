#!/usr/bin/python

import bs4

def main():
    filename = '0.html'
    file1 = open(filename, 'r')
    bsObj = bs4.BeautifulSoup(file1.read(), "html.parser")
    print "bsObj = %s" % str(bsObj)
    print "bsObj.option = %s" % str(bsObj.option)
    for option in bsObj.option:
        print "  option = %s" % str(option)

main()
