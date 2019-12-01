#!/usr/bin/env python3
#!/usr/bin/python

import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(("Encountered a start tag:", tag))

    def handle_endtag(self, tag):
        print(("Encountered an end tag :", tag))

    def handle_data(self, data):
        print(("Encountered some data  :", data))

def main():
    url = 'https://screener.finance.yahoo.com/stocks.html'
    # url = 'https://screener.finance.yahoo.com/b?sc=&im=&prmin=0&prmax=&mcmin=&mcmax=&dvymin=0&dvymax=&betamin=&betamax=&remin=&remax=&pmmin=&pmmax=&pemin=&pemax=&pbmin=&pbmax=&psmin=&psmax=&pegmin=&pegmax=&gr=&grfy=&ar=&vw=1&db=stocks'
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    # print "%s" % resp.read()
    parser = MyHTMLParser()
    parser.feed(html)

main()
