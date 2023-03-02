from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #input keystrokes
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()

url = 'https://the-internet.herokuapp.com/dynamic_loading/2'



driver.get(url)

#   load dynamic content/jvascript websites

# //*[@id="start"]/button
# //*[@id="finish"]/h4

driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

#wait for js to render
driver.implicitly_wait(10)

text = driver.find_element(By.XPATH, '//*[@id="finish"]/h4').text


print(text)
