#!/usr/bin/env python3
#!/usr/bin/python

import urllib.request, urllib.parse, urllib.error

def main():
    # url = 'https://screener.finance.yahoo.com/stocks.html'
    url = 'https://screener.finance.yahoo.com/b?sc=&im=&prmin=0&prmax=&mcmin=&mcmax=&dvymin=0&dvymax=&betamin=&betamax=&remin=&remax=&pmmin=&pmmax=&pemin=&pemax=&pbmin=&pbmax=&psmin=&psmax=&pegmin=&pegmax=&gr=&grfy=&ar=&vw=1&db=stocks'
    html = urllib.request.urlopen(url)
    print("%s" % html.read())

main()
