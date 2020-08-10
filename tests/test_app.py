import os
import time
from appium import webdriver

"""Sets up desired capabilities and the Appium driver."""
url = 'http://127.0.0.1:4723/wd/hub'
desired_caps = {}

"""
The following desired capabilities must be set when running locally.
Make sure they are NOT set when uploading to Device Farm.

desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'aPhone'
"""
# desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = 'aPhone'

driver = webdriver.Remote(url, desired_caps)

# wait for app to load
time.sleep(10)

# find the link with the text "Click here" and click on it
link = driver.find_element_by_xpath('//*[@text="Click Here"]')
link.click()

# wait for the next screen to load
time.sleep(10)

# make sure the correct "Success" result is on the page
driver.find_element_by_xpath('//*[@text="Success"]')

# important; you will not be able to launch again if this does not happen
driver.quit()