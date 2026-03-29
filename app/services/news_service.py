import os
from newsapi import NewsApiClient
from dotenv import load_dotenv
from datetime import datetime, timedelta
from app.services.scoring_service import score_and_sort

load_dotenv()

api = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def get_news(query: str = "tecnología OR política", hours_ago: int = 24):
    since = (datetime.utcnow() - timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%M:%S")

    response = api.get_everything(
        q=query,
        language="es",
        sort_by="popularity",
        from_param=since,
        page_size=15
    )

    articles = response.get("articles", [])

    return [
        {
            "title": a["title"],
            "description": a["description"],
            "source": a["source"]["name"],
            "url": a["url"],
            "published_at": a["publishedAt"],
            "image": a.get("urlToImage")
        }
        for a in articles if a["title"] and "[Removed]" not in a["title"]
    ]

def get_today_news():
    articles = get_news(hours_ago=24)
    return score_and_sort(articles)

def get_yesterday_news():
    articles = get_news(hours_ago=48)
    return score_and_sort(articles)