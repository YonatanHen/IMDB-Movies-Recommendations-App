import requests
from bs4 import BeautifulSoup
from .constants import *

requests.packages.urllib3.disable_warnings()

'''
The Scraper class is responsible for scraping functions and their utility functions
'''
class Scraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }
        self.IMDB_URL = "https://www.imdb.com/"

    '''
    This function create an endpoint with the search parameters entered by the user. 
    '''
    def _create_filters(self,filters):        
            release_year = None
            role = None
            if filters[ACTORS] != "":
                role = self.name_scraper(filters['role'])         
            if filters[RELEASE_YEAR] != "":
                release_year_filter = filters[RELEASE_YEAR]
                release_year = f"release_date={release_year_filter}-01-01,{release_year_filter}-12-31"
            
            endpoint = ""
            
            if release_year:
                endpoint = "&"+release_year
                filters.pop(RELEASE_YEAR)
            if role:
                endpoint += f"&role={role}"
                filters.pop('role')
            
            for key,value in filters.items():
                if value != "" and value != None:
                        value = value.replace(' ', '%20') 
                        endpoint += "&"+key+"="+value

            return endpoint

    '''
    This function scrapes data from https://www.imdb.com/search/title/.
    The function returns a list of dictionaries in which each dictionary includes movie's information.
    '''
    def title_scraper(self, filters={}):
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL+"search/title/?title_type=feature,tv_movie"

        searchFilters = self._create_filters(filters)
        page = requests.get(IMDB_URL+searchFilters, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        BASE_SELECTOR = "sc-f24f1c5c-3"
        items = soup.find_all('div', class_=BASE_SELECTOR)
        manipulated_data = []
        #Most of the info we need is present in the <img> tag.
        for item in items:
            img_info = item.find('img')            
            if img_info != None:
                picture_url = img_info.get('src')
                movie_page_url = item.find('a').get('href')
                title = item.find('h3').text[3:]
                year = item.find('span').text
                manipulated_data.append({"title": title, "year": year, "picture_url": picture_url, "movie_page_url": self.IMDB_URL+movie_page_url[1:]})
        
        return manipulated_data

    '''
    This function scrapes data from https://www.imdb.com/search/name.
    The function recievies the actor's name and returns his IMDb ID.
    '''
    def name_scraper(self, name):
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL+f"search/name/?name={name}"
        page = requests.get(IMDB_URL, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        BASE_SELECTOR = "ipc-title-link-wrapper"
        items = soup.find_all('a', class_=BASE_SELECTOR)
        actorId = items[0].get("href").split('/')[2]

        return actorId
        
         
             
    
