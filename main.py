import json
from datetime import datetime

from scrapers.ratopati import get_ratopati
from scrapers.onlinekhabar import get_onlinekhabar

from scrapers.bbc_nepali import get_bbc_nepali
from scrapers.kathmandupost import get_kathmandupost

LIMIT = 1000

all_news = []

sources = [
        get_ratopati,
    get_onlinekhabar,

    get_bbc_nepali,
    get_kathmandupost
]

for source in sources:
    try:
        all_news.extend(source())
    except Exception as e:
        print(f"Error loading source: {e}")

# 🔹 Remove duplicate titles
unique_news = []
seen_titles = set()

for news in all_news:
    if news["title"] not in seen_titles:
        seen_titles.add(news["title"])
        unique_news.append(news)

unique_news = unique_news[:LIMIT]

data = {
    "status": "ok",
    "country": "Nepal",
    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "total_articles": len(unique_news),
    "articles": unique_news
}

with open("combined_news.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=5)

print(" Nepali news articles combined successfully!")
