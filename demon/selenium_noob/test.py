from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #input keystrokes

driver = webdriver.Firefox()

url = 'https://the-internet.herokuapp.com/login'

#   inspect element->copy ->XPath
# //*[@id="username"]
# //*[@id="password"]
# //*[@id="login"]/button

driver.get(url)

#   tell the driver to find the elements.
#   send the keys to the site changed since 2020
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
driver.find_element(By.XPATH, '//*[@id="login"]/button').click()

