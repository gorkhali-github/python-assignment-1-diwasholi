import feedparser

def get_bbc_nepali():
    feed = feedparser.parse("https://feeds.bbci.co.uk/nepali/rss.xml")

    articles = []
    for entry in feed.entries[:20]:
        articles.append({
            "title": entry.title,
            "url": entry.link,
            "source": "BBC Nepali"
        })
    return articles

