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

# testLink = "https://www.thewhiskyexchange.com/queue/p/70286/karuizawa-38-year-old-platinum-geisha"
whiskyList = []
for link in productLinks:
    r = requests.get(link, headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_="product-main__name").text.strip()

    try:
        price = soup.find('p', class_="product-action__price").text.strip()
        description = soup.find('div', class_="product-main__description").text.strip()
    except:
        price = "Out of stock"
        description = "out of stock"



    whisky = {
        'name' : name,
        'price' : price,
        'description': description
    }

    whiskyList.append(whisky)
    print('saving : ',whisky['name'])

