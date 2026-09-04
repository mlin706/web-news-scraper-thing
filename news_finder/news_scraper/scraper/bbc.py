import requests
from bs4 import BeautifulSoup as bs


def get_rss_feed():

    r = requests.get(
        "https://feeds.bbci.co.uk/news/uk/rss.xml"
    )

    return bs(r.text, features="xml")

def items_from_feed(feed: bs):
    '''
    given soup object (xml parsed using BeautifulSoup), returns data in a useable format
    assumes BBC rss feed format as of 27.08.26
    we want an output that can be fed straight into context. so dictionary item that is a list of useful things
    this returns the item which presumably wants to be a list of dicts? or custom classes?
    '''

    items = feed.find_all('item')

    for item in item:
        pass