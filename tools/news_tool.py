import os
import requests
from dotenv import load_dotenv
load_dotenv()

NEWS_API_KEY = os.environ["NEWS_API_KEY"]

def get_news(company: str) -> str:
    url = f"https://newsapi.org/v2/everything?q={company}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])

    if not articles:
        return "No recent news found."

    top_articles = articles[:3]  # Limit to top 3
    result = "\n\n".join(
        [f"📰 **{a['title']}**\n{a['description']}" for a in top_articles]
    )
    return result
