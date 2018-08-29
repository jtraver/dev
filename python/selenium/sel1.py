#!/usr/bin/python

from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/Users/jtraver/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print "%s" % driver.find_element_by_id("content").text
driver.close()
