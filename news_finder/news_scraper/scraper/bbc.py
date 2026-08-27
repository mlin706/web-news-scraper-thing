import requests
from bs4 import BeautifulSoup as bs


def get_rss_feed():

    r = requests.get(
        "https://feeds.bbci.co.uk/news/uk/rss.xml"
    )

    return bs(r.text, features="xml")