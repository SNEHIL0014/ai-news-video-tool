"""
Fetches trending news using Google News RSS.
"""
from gnews import GNews

def fetch_trending_news():
    """
    Fetch top trending news articles using Google News.
    """
    google_news = GNews(
        language="en",
        country="IN",
        period="1d",
        max_results=3
    )

    news = google_news.get_top_news()
    return news


if __name__ == "__main__":
    articles = fetch_trending_news()

    print("Trending News:\n")
    for i, article in enumerate(articles, start=1):
        print(f"News {i}")
        print("Title:", article.get("title"))
        print("Description:", article.get("description"))
        print("Source:", article.get("publisher", {}).get("title"))
        print("-" * 40)
