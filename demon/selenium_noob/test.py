from selenium import webdriver
from selenium.webdriver.common.keys import Keys #input keystrokes

driver = webdriver.Firefox()

url = 'https://the-internet.herokuapp.com/login'

#   inspect element->copy ->XPath
//*[@id="username"]
//*[@id="password"]
//*[@id="login"]/button

#   tell the driver to find the elements
driver.find_element_by_xpath('//*[@id="username"]')
driver.find_element_by_xpath('//*[@id="password"]')
driver.find_element_by_xpath('//*[@id="login"]/button')

driver.get(url)