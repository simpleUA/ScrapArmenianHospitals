import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree


def add_data_to_pd(link_to_site):
    web_page = requests.get(link_to_site)
    link_soup = BeautifulSoup(web_page.text, "html.parser")
    dom = etree.HTML(str(link_soup))
    try:
        name = dom.xpath('/html/body/section/div/div/div[1]/div/h1')[0].text
    except ValueError:
        print("can't find name")

    try:
        address = dom.xpath('/html/body/section/div/div/div[1]/div/div[2]/div[1]/div/h5')[0].text

    except ValueError:
        print("can't find address")

    try:
        tel = dom.xpath('/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/h5')[0].text

    except ValueError:
        print("can't find tel")

    try:
        data[name] = address, tel

    except ValueError:
        print("unable to create data for " + link_to_site)


dataframe = pd.DataFrame()

data = {}

url = 'https://www.doctors.am/ru/institutions/maternity-hospitals?page=3'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

soup = soup.findAll('div', attrs={'class': 'item-img-shadow'})

for link in soup:
    print(link)
    web_link = link.find('a').get('href')
    add_data_to_pd(web_link)
    print(web_link)

df = pd.DataFrame(data.items())

df.to_excel("output.xlsx", index=False)
