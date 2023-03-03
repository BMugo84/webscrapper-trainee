from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

#   remove popup ads
options = Options()
options.set_preference("dom.disable_beforeunload", True)
options.set_preference("browser.tabs.warnOnClose", False)

#   load driver
driver = webdriver.Firefox(options=options)



urls = []
for x in range(1,6):
    url = f'https://www.jumia.co.ke/mobile-phones/apple--samsung--xiaomi/?rating=3-5&price=10000-192270&page={x}#catalog-listing'
    # print(url)
    driver.get(url)

    #   remove popup ads ie the newsletter. jumia detects whether you are a bot
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, 'button.cls[aria-label="newsletter_popup_close-cta"]')
        close_button.click()
    except:
        pass

    #   wait for content to load
    locator = (By.CSS_SELECTOR, 'article.prd')
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located(locator))

    #   get all phones
    phones = driver.find_elements(By.CSS_SELECTOR, 'article.prd')

    for phone in phones:
        phone_name = phone.find_element(By.CSS_SELECTOR, 'h3.name').text
        phone_price = phone.find_element(By.CSS_SELECTOR, 'div.prc').text
        print(phone_name,phone_price)