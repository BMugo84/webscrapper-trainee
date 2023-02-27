import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.thewhiskyexchange.com/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
}

productLinks = []
for x in range(1,4):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}')

    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all('li', attrs={'class':'product-grid__item'})

    for item in productList:
        for link in item.find_all('a', href=True):
            productLinks.append(baseurl + link['href'])

print(len(productLinks))