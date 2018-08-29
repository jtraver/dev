#!/usr/bin/python

from selenium import webdriver

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

# driver.get('https://facebook.com')
# driver.get('http://www.yahoo.com')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

# wait up to 10 seconds for the elements to become available
driver.implicitly_wait(10)

# time.sleep(3)
print "%s" % driver.find_element_by_id("content").text
driver.close()
