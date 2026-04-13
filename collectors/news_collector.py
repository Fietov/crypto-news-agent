import requests
from models.news import NewsArticle
from datetime import datetime
from config import config

class NewsCollector:

    # init method for remembering info that is in
    def __init__(self, api_key: str):
        self.api_key = config.news_data_api_key

    def fetch_latest(self, limit: int = 10, currencies: list[str] = None) -> list[NewsArticle]:
        # the conditions for url in cryptopanic
        url = f"{self.BASE_URL}/crypto"

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

            params["currencies"] = ",".join(uppercased)

        # making the request
        response = requests.get(url,params=params)
        # convert to dict
        print(response.status_code)
        print(response.url)
        print(response.text[:500])
        data = response.json()

        articles = []
        for item in data["results"]:
            article = NewsArticle(
                title = item["title"],
                description = item.get("description"),
                published_at = datetime.fromisoformat(item["created_at"]),
                kind = item["kind"],
                coins_mentioned = []
            )
            articles.append(article)

        return articles[:limit]

