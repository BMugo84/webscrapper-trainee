from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.jumia.co.ke/mobile-phones/?rating=3-5#catalog-listing'
driver = webdriver.Firefox()
driver.get(url)

//*[@id="close"]
//*[@id="pop"]

