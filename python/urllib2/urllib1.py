#!/usr/bin/python

import urllib2

def main():
    # url = 'https://screener.finance.yahoo.com/stocks.html'
    url = 'https://screener.finance.yahoo.com/b?sc=&im=&prmin=0&prmax=&mcmin=&mcmax=&dvymin=0&dvymax=&betamin=&betamax=&remin=&remax=&pmmin=&pmmax=&pemin=&pemax=&pbmin=&pbmax=&psmin=&psmax=&pegmin=&pegmax=&gr=&grfy=&ar=&vw=1&db=stocks'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    print "%s" % resp.read()

main()
