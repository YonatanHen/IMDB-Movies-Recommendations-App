import requests
from bs4 import BeautifulSoup as soup
#import pandas as pdp

headers = {
    'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }



# title_type added as we want to filter only the movies
IMDB_URL = "https://www.imdb.com/search/title/?title_type=feature,tv_movie"

searchFilters = "&release_date=2012-01-01,2012-12-31"

page = requests.get(IMDB_URL+searchFilters, headers=headers, verify=False)
pageSoup = soup(page.content, 'html.parser')

# print(pageSoup.find_all("a", {"class": "ipc-title-link-wrapper"}))

