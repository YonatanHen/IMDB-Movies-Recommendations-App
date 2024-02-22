import requests
from bs4 import BeautifulSoup
from createFilters import *
from manipulateMovieData import *

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

manipulated_data = []

#All the info we need is present in the <img> tag.
for item in items:
    data = item.find('img').get('alt')
    picture_url = item.find('img').get('src')
    actors,title,year = manipulateMovieData(data)
    manipulated_data.append({"actors": actors, "title": title, "year": year, "picture_url": picture_url})

print(manipulated_data)
    


