import requests
import re
import time
import random
import cloudscraper
from fake_useragent import UserAgent

from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
ua = UserAgent()

def load_url(url, return_content=False):
    time.sleep(random.uniform(1, 2))
    headers = {
        'User-Agent': ua.random
    }
    response = scraper.get(url, headers=headers)
    try:
        response.raise_for_status()
        if not return_content:
            return response
        else:
            features = 'xml' if url.endswith('.xml') else 'html.parser'
            soup = BeautifulSoup(response.content, features)
            return soup
    except Exception as e:  # This is the correct syntax
        print(e)


def get_id_from_url(url):
    regex = re.search('(/[0-9]+/)|(-[0-9]+.aspx)', url)
    id_index = list(regex.span())
    result = url[id_index[0]:id_index[1]]
    return re.sub(".aspx|/|-", "", result)


def get_id_from_url__vbpl(url):
    regex = re.search('(=[0-9]+)', url)
    id_index = list(regex.span())
    return url[id_index[0]+1 : id_index[1]]



