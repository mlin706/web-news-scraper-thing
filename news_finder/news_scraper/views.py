from django.shortcuts import render
from .scraper.bbc import get_rss_feed

# Create your views here.
def index(request):

    feed = get_rss_feed()

    item = feed.find('item')

    context = {
        'name': item
    }

    return render(
        request, 'news_scraper/index.html', context
    )