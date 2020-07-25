import requests
from bs4 import BeautifulSoup

def getDetails(URL):
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')

    model = getModel(soup)
    color = getColor(soup)
    price = getPrice(soup)

    return model + '\n' +  color + '\n' + price


def getModel(soup):
    nameResults = soup.find_all('h1', {'class': 'pdp-primary-information__product-name display--small-up'})
    silhResults = soup.find_all('p', {'class': 'pdp-primary-information__badge text--bold text--upper text-color--neutral-3'})

    #model
    nameList = nameResults[0].text.split()
    name = " ".join(nameList)

    #silhoutte
    silhList = silhResults[0].text.split()
    silh = " ".join(silhList)

    return name + ' ' + silh


def getPrice(soup):
    results = soup.find_all('span', {'class': 'product-price--sales'})

    #formatting html into a str
    priceList = results[0].text.split()
    price = priceList[0]

    return price


def getColor(soup):
    results = soup.find_all('span', {'class': 'variations__label-value'})

    #formatting html into a str
    colorList = results[0].text.split()
    color = colorList[0]

    return color


def getString():
    yellowLow_URL = 'https://bit.ly/2ZW0Ow1'
    blackLow_URL = 'https://bit.ly/3jD7GGv'
    blackHigh_URL = 'https://bit.ly/2ZWipE0'

    urlList = [yellowLow_URL, blackLow_URL, blackHigh_URL]

    string = ''

    for url in urlList:
        string = string + getDetails(url) + '\n' + url + '\n\n'
        
    return string