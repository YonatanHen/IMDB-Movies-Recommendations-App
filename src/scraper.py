import requests
from bs4 import BeautifulSoup
from .constants import *

requests.packages.urllib3.disable_warnings()


class Scraper:
    """
    The Scraper class is responsible for scraping functions and their utility functions
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
        }
        self.IMDB_URL = "https://www.imdb.com/"

    def _create_filters(self, filters):
        """
        This function create an endpoint with the search parameters entered by the user.
        @param filters: The search parameters set by the user.
        @return: The endpoint used for sending the search request to imdb.com advanced search page.
        """
        release_year = None
        role = None
        actors = filters[ACTORS]
        if actors != "":
            actors = actors.strip()
            if ',' in actors:
                actors = actors.split(",")
                role = ""
                for actor in actors:
                    role += self.name_scraper(actor)+","
                role = role[:-1]
            else:
                role = self.name_scraper(filters["role"])
        if filters[RELEASE_YEAR] != "":
            release_year_filter = filters[RELEASE_YEAR]
            release_year = (
                f"release_date={release_year_filter}-01-01,{release_year_filter}-12-31"
            )

        endpoint = ""

        if release_year:
            endpoint = "&" + release_year
            filters.pop(RELEASE_YEAR)
        if role:
            endpoint += f"&role={role}"
            filters.pop("role")

        for key, value in filters.items():
            if value != "" and value != None:
                value = value.replace(" ", "%20")
                endpoint += "&" + key + "=" + value

        return endpoint

    def title_scraper(self, filters={}):
        """
        This function scrapes data from https://www.imdb.com/search/title/.
        The function returns a list of dictionaries in which each dictionary includes movie's information.
        @param filters: The search parameters set by the user.
        @return list of dictionaries in which each dictionary includes movie's information.
        """
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL + "search/title/?title_type=feature,tv_movie"

        searchFilters = self._create_filters(filters)
        page = requests.get(
            IMDB_URL + searchFilters, headers=self.headers, verify=False
        )
        soup = BeautifulSoup(page.content, "html.parser")

        BASE_SELECTOR = "sc-f24f1c5c-3"
        items = soup.find_all("div", class_=BASE_SELECTOR)
        manipulated_data = []
        # Most of the info we need is present in the <img> tag.
        for item in items:
            img_info = item.find("img")
            if img_info != None:
                picture_url = img_info.get("src")
                title = item.find("h3").text[3:]
                year = item.find("span").text
                manipulated_data.append(
                    {"title": title, "year": year, "picture_url": picture_url}
                )

        return manipulated_data

    def name_scraper(self, name):
        """
        This function scrapes data from https://www.imdb.com/search/name.
        The function recievies the actor's name and returns his IMDb ID.
        @param name: The actor/director name entered by the user.
        @return the ID of the actor from IMDb.
        """
        # title_type added as we want to filter only the movies
        IMDB_URL = self.IMDB_URL + f"search/name/?name={name}"
        page = requests.get(IMDB_URL, headers=self.headers, verify=False)
        soup = BeautifulSoup(page.content, "html.parser")

        BASE_SELECTOR = "ipc-title-link-wrapper"
        items = soup.find_all("a", class_=BASE_SELECTOR)
        actorId = items[0].get("href").split("/")[2]

        return actorId
