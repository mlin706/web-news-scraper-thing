from django.shortcuts import render
from .scraper.bbc import get_rss_feed

class RSS_Item:

    def __init__(self, item):

        self._item = item

        self.context = {
            'title': item.title.string,
            'description': item.description.string,
            'link': item.link.string,
            'date': item.pubDate.string
        }

# Create your views here.
def index(request):

    feed = get_rss_feed()

    tags = feed.find_all('item')

    context = {
        'tags': [
            RSS_Item(tag).context for tag in tags
        ]
    }

    return render(
        request, 'news_scraper/index.html', context
    )