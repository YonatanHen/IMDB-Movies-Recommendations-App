import requests
from bs4 import BeautifulSoup
from utils.createFilters import *
#import pandas as pdp

headers = {
    'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }



# title_type added as we want to filter only the movies
IMDB_URL = "https://www.imdb.com/search/title/?title_type=feature,tv_movie"

searchFilters = createFilters({"release_year": ["2015", "2018"]})
page = requests.get(IMDB_URL+searchFilters, headers=headers, verify=False)
soup = BeautifulSoup(page.content, 'html.parser')

print(IMDB_URL+searchFilters)
BASE_SELECTOR = "sc-f24f1c5c-3"
items = soup.find_all('div', class_=BASE_SELECTOR)

data = []
#All the info we need are present in the <img> tag.
print(items[1].find('img').get('alt'))



