import requests
from bs4 import BeautifulSoup

def get_onlinekhabar():
    url = "https://www.onlinekhabar.com"
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    articles = []

    for a in soup.select("h2 a")[:10]:
        title = a.text.strip()
        link = a.get("href")

        if title and link:
            articles.append({
                "title": title,
                "url": link,
                "source": "OnlineKhabar"
            })

    return articles
