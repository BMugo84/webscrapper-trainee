#   scraping data from youtube to get the top
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.youtube.com/@JohnWatsonRooney/videos'


driver = webdriver.Firefox()
driver.get(url)


# style-scope ytd-rich-grid-media
# //*[@id="video-title"]
# //*[@id="video-title-link"]
# //*[@id="metadata-line"]/span[1]
# //*[@id="metadata-line"]/span[2]

videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')

for video in videos:
    title = video.find_element(By.XPATH, '//*[@id="video-title"]').text
    views = video.find_element(By.XPATH, '//*[@id="metadata-line"]/span[1]').text
    date  = video.find_element(By.XPATH, '//*[@id="metadata-line"]/span[2]').text

    print(title, views, date)