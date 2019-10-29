#!/usr/bin/env python3
#!/usr/bin/python

import selenium
from selenium import webdriver
import apihelper

print "\n---------------------------------------------------------------------------------"
print "selenium"
apihelper.info(selenium)
print "selenium = %s" % str(selenium)
print "selenium = %s" % str(type(selenium))
print "selenium"
print "---------------------------------------------------------------------------------\n"


print "\n---------------------------------------------------------------------------------"
print "webdriver"
apihelper.info(webdriver)
print "webdriver = %s" % str(webdriver)
print "webdriver = %s" % str(type(webdriver))
print "webdriver"
print "---------------------------------------------------------------------------------\n"


print "\n---------------------------------------------------------------------------------"
print "webdriver.Chrome"
apihelper.info(webdriver.Chrome)
print "webdriver.Chrome = %s" % str(webdriver.Chrome)
print "webdriver.Chrome = %s" % str(type(webdriver.Chrome))
print "webdriver.Chrome"
print "---------------------------------------------------------------------------------\n"


print "\n---------------------------------------------------------------------------------"
print "webdriver.Remote"
apihelper.info(webdriver.Remote)
print "webdriver.Remote = %s" % str(webdriver.Remote)
print "webdriver.Remote = %s" % str(type(webdriver.Remote))
print "webdriver.Remote"
print "---------------------------------------------------------------------------------\n"


options = webdriver.ChromeOptions()

# tell selenium to use the dev channel version of chrome
# NOTE: only do this if you have a good reason to
# options.binary_location = '/usr/bin/google-chrome-unstable'
# options.binary_location = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'

options.add_argument('headless')

# set the window size
# options.add_argument('window-size=1200x600')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

print "---------------------------------------------------------------------------------"
print "driver"
try:
    apihelper.info(driver)
except Exception, e:
    print "e = %s" % str(e)
print "driver = %s" % str(driver)
print "driver = %s" % str(type(driver))
print "driver"
print "---------------------------------------------------------------------------------"


# driver.get('https://facebook.com')
# driver.get('http://www.yahoo.com')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

# wait up to 10 seconds for the elements to become available
driver.implicitly_wait(10)
# time.sleep(3)

content_element = driver.find_element_by_id("content")
print "\n---------------------------------------------------------------------------------"
print "content_element"
try:
    apihelper.info(content_element)
except Exception, e:
    print "e = %s" % str(e)
print "content_element = %s" % str(content_element)
print "content_element = %s" % str(type(content_element))
print "content_element"
print "---------------------------------------------------------------------------------\n"

print "%s" % driver.find_element_by_id("content").text

html_element = driver.find_element_by_tag_name('html')
print "\n---------------------------------------------------------------------------------"
print "html_element"
try:
    apihelper.info(html_element)
except Exception, e:
    print "e = %s" % str(e)
print "html_element = %s" % str(html_element)
print "html_element = %s" % str(type(html_element))
print "html_element"
print "---------------------------------------------------------------------------------\n"
print "html text is %s" % html_element.text


driver.close()
