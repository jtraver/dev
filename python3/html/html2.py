#!/usr/bin/env python3
#!/usr/bin/python

import urllib2
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

def main():
    url = "http://eoddata.com/symbols.aspx"
    url = "http://eoddata.com/stocklist/NYSE/B.htm"
    url = "http://eoddata.com/stocklist/NASDAQ/B.htm"
    url = "http://eoddata.com/stocklist/AMEX/B.htm"
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    html = resp.read()
    # print "%s" % resp.read()
    parser = MyHTMLParser()
    parser.feed(html)

main()
