import requests
from bs4 import BeautifulSoup

def nameScraper(name):
    headers = {
        'User-Agent': 
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
            }

    # title_type added as we want to filter only the movies
    IMDB_URL = f"https://www.imdb.com/search/name/?name={name}"
    page = requests.get(IMDB_URL, headers=headers, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    BASE_SELECTOR = "ipc-title-link-wrapper"
    items = soup.find_all('a', class_=BASE_SELECTOR)

    actorId = items[0].get("href").split('/')[2]

    return actorId

print(nameScraper("bruce willis"))
