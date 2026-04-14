import requests
from models.news import NewsArticle
from datetime import datetime
from config import config

class NewsCollector:

    # init method for remembering info that is in
    def __init__(self):
        self.api_key = config.news_data_api_key
        self.base_url = "https://newsdata.io/api/1"

    def fetch_latest(self, limit: int = 10, currencies: list[str] = None) -> list[NewsArticle]:
        # the conditions for url in cryptopanic
        url = f"{self.base_url}/crypto"

        # parameters that has to be sended
        params = {
            "apikey": self.api_key,
            "language": "en",
        }

        # optional but useful, if user wants to pass in specific currencies
        if currencies:
            uppercased = []
            for currency in currencies:
                uppercased.append(currency.upper())
            params["q"] = " OR ".join(uppercased)

            params["currencies"] = ",".join(uppercased)

        # making the request
        response = requests.get(url,params=params)
        # convert to dict
        data = response.json()

        articles = []
        for item in data["results"]:
            coins = item.get("coins") or []

            article = NewsArticle(
                title = item.get("title",""),
                description = item.get("description"),
                published_at = datetime.fromisoformat((item.get("pubDate", datetime.now().isoformat()))),
                kind = "news",
                coins_mentioned = coins
            )
            articles.append(article)

        return articles[:limit]

