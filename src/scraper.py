import requests
from bs4 import BeautifulSoup
from manipulateMovieData import manipulateMovieData

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
            if 'role' in filters:
                    role = Scraper().nameScraper(filters['role'])         
            if 'release_year' in filters:
                    release_year_filters = filters['release_year']
                    if len(filters['release_year']) == 1:
                            release_year_filter = release_year_filters[0]
                            release_year = f"release_date={release_year_filter}-01-01,{release_year_filter}-12-31"
                    else:
                            release_year = f"release_date={release_year_filters[0]}-01-01,{release_year_filters[1]}-12-31"
                    
            if release_year:
                    endpoint = "&"+release_year
                    filters.pop('release_year')
            if role:
                    endpoint += f"&role={role}"
                    filters.pop('role')
            
            for key,value in filters.items():
                value = value.replace(' ', '%20') 
                endpoint += "&"+key+"="+value

            return endpoint

    def titleScraper(self, filters={}):
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL+"title/?title_type=feature,tv_movie"

        searchFilters = self.createFilters(filters)
        page = requests.get(IMDB_URL+searchFilters, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        BASE_SELECTOR = "sc-f24f1c5c-3"
        items = soup.find_all('div', class_=BASE_SELECTOR)

        manipulated_data = []

        #All the info we need is present in the <img> tag.
        for item in items:
            data = item.find('img').get('alt')
            picture_url = item.find('img').get('src')
            actors,title,year = manipulateMovieData(data)
            manipulated_data.append({"actors": actors, "title": title, "year": year, "picture_url": picture_url})

    def nameScraper(self, name):
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL+f"name/?name={name}"
        page = requests.get(IMDB_URL, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        BASE_SELECTOR = "ipc-title-link-wrapper"
        items = soup.find_all('a', class_=BASE_SELECTOR)
        actorId = items[0].get("href").split('/')[2]

        return actorId


