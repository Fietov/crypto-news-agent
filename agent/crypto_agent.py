import os
from datetime import datetime
from collections import Counter
from models.news import NewsArticle, Sentiment
from models.report import Report, CoinSummary
from collectors.news_collector import NewsCollector
from analyzers.news_analyzer import NewsAnalyzer
from dotenv import load_dotenv
from config import config
import json

load_dotenv()

class CryptoAgent:
    def __init__(self, limit: int = 10, currencies: list[str] = None):
        self.limit = config.default_limit
        self.currencies = currencies
        self.collector = NewsCollector(config.cryptopanic_api_key)
        self.analyzer = NewsAnalyzer()

    def run(self) -> Report:
        print("Fetching latest news...")
        articles = self.collector.fetch_latest(
            limit=self.limit,
            currencies=self.currencies,
        )

        print(f"Analyzing {len(articles)} articles with LLM...")
        analyzed_articles = []
        for i, article in enumerate(articles):
            analyzed = self.analyzer.analyze(article)
            analyzed_articles.append(analyzed)

        print("Building report...")
        report = self._build_report(analyzed_articles)

        return report

    def _build_report(self, articles: list[NewsArticle]) -> Report:
        coin_data = {}

        for article in articles:
            for coin in article.coins_mentioned:
                if coin not in coin_data:
                    coin_data[coin] = {
                        "positive": 0,
                        "negative": 0,
                        "neutral": 0
                    }
                if article.sentiment == Sentiment.POSITIVE:
                    coin_data[coin]["positive"] += 1
                elif article.sentiment == Sentiment.NEGATIVE:
                    coin_data[coin]["negative"] += 1
                else:
                    coin_data[coin]["neutral"] += 1

        coin_summaries = []
        for coin, counts in coin_data.items():
            overall = max(counts,key=counts.get)
            coin_summaries.append(CoinSummary(
                coin=coin,
                total_articles=sum(counts.values()),
                positive=counts["positive"],
                negative=counts["negative"],
                neutral=counts["neutral"],
                overall_sentiment=Sentiment(overall)
            ))

        return Report(
            generated_at=datetime.now(),
            total_articles=len(articles),
            coins=coin_summaries,
            articles=articles
        )
    def save_report(self,report: Report, filename: str = "report.json") -> None:
        # first make it a dictionary and only then to JSON
        report_dict = {
            "generated_at": report.generated_at.isoformat(),
            "total_articles": report.total_articles,
            "coins": [
                {
                    "coin": coin.coin,
                    "total_articles": coin.total_articles,
                    "positive": coin.positive,
                    "negative": coin.negative,
                    "neutral": coin.neutral,
                    "overall_sentiment": coin.overall_sentiment.value
                }
                for coin in report.coins
            ],
            "articles": [
                {
                    "title": article.title,
                    "description": article.description,
                    "published_at": article.published_at.isoformat(),
                    "sentiment": article.sentiment.value if article.sentiment else None,
                    "coins_mentioned": article.coins_mentioned,
                }
                for article in report.articles
            ]
        }

        with open(filename, "w") as f:
            json.dump(report_dict, f, indent=4)

        print(f"Saving report to {filename}")














