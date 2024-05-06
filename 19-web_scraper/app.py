import requests
from bs4 import BeautifulSoup

url = 'https://www.irishnews.com/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class': 'c-heading'})

for t in title:
    print(t.getText())
