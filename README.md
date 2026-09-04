# web-news-scraper-thing
scrapes a list of news websites to find stories containing certain keywords -- keeps you up to date with all the news you're interested and none of the stuff you're not (something something echo chamber something)

## things to do
- [ ] order stories by date
- [ ] add stories to a database
  - [ ] include fields for:
    - article_id (probably pull from the link - https://www.bbc.co.uk/news/articles/*id*)
    - title
    - previous titles (if changed on re-fetching - probably compare for uniqueness by link)
    - description
    - source (eg bbc)
    - link
    - tags? 