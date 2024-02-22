import requests
from bs4 import BeautifulSoup
from src.utils.manipulateMovieData import manipulateMovieData
from .constants import *

'''
The Scraper class is responsible for scraping functions and their utility functions
'''
class Scraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }
        self.IMDB_URL = "https://www.imdb.com/search/"

    '''
    This function create an endpoint with the search parameters entered by the user. 
    '''
    def _createFilters(self,filters):        
            release_year = None
            role = None
            if filters[ACTORS] != "":
                role = self.nameScraper(filters['role'])         
            if RELEASE_YEAR in filters:
                release_year_filter = filters[RELEASE_YEAR]
                release_year = f"release_date={release_year_filter}-01-01,{release_year_filter}-12-31"
                    
            if release_year:
                endpoint = "&"+release_year
                filters.pop(RELEASE_YEAR)
            if role:
                endpoint += f"&role={role}"
                filters.pop('role')
            
            for key,value in filters.items():
                print(key,value)
                if value != "" and value != None:
                        value = value.replace(' ', '%20') 
                        endpoint += "&"+key+"="+value

            return endpoint

    def titleScraper(self, filters={}):
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL+"title/?title_type=feature,tv_movie"

        searchFilters = self._createFilters(filters)
        page = requests.get(IMDB_URL+searchFilters, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        BASE_SELECTOR = "sc-f24f1c5c-3"
        items = soup.find_all('div', class_=BASE_SELECTOR)

        manipulated_data = []
        print(IMDB_URL+searchFilters)
        #Most of the info we need is present in the <img> tag.
        for item in items:
            img_info = item.find('img')
            if img_info != None:
                data = img_info.get('alt')
                picture_url = img_info.get('src')
                actors,title,year = manipulateMovieData(data)
                manipulated_data.append({"actors": actors, "title": title, "year": year, "picture_url": picture_url})
        
        return manipulated_data

    def nameScraper(self, name):
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL+f"name/?name={name}"
        page = requests.get(IMDB_URL, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        BASE_SELECTOR = "ipc-title-link-wrapper"
        items = soup.find_all('a', class_=BASE_SELECTOR)
        actorId = items[0].get("href").split('/')[2]

        return actorId
    
