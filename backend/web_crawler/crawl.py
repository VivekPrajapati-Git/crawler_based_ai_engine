from bs4 import BeautifulSoup
from .link import link

def crawl(data):
    links = link(data)

    for url in links:
        print(url)
