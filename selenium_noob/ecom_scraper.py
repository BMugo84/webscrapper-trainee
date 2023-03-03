from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

url = 'https://www.jumia.co.ke/mobile-phones/apple--samsung--xiaomi/?rating=3-5&price=10000-192270#catalog-listing'
#   remove popup ads
options = Options()
options.set_preference("dom.disable_beforeunload", True)
options.set_preference("browser.tabs.warnOnClose", False)

#   load driver
driver = webdriver.Firefox(options=options)
driver.get(url)

#   remove popup ads ie the newsletter. jumia detects whether you are a bot
try:
    close_button = driver.find_element(By.CSS_SELECTOR, 'button.cls[aria-label="newsletter_popup_close-cta"]')
    close_button.click()
except:
    pass

#   wait for content to load
driver.implicitly_wait(30)

#   get all phones
phones = driver.find_elements(By.CSS_SELECTOR, 'article.prd')



for phone in phones:
    phone_name = phone.find_element(By.CSS_SELECTOR, 'h3.name').text
    phone_price = phone.find_element(By.CSS_SELECTOR, 'div.prc').text
    print(phone_name,phone_price)
